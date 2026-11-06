// Ricezione push da Garmin: attività concluse e revoche dell'utente.
// Deployare con --no-verify-jwt. Accetta solo utenti collegati nel database.
import { createClient } from "npm:@supabase/supabase-js@2";

const sb = createClient(Deno.env.get("SUPABASE_URL")!, Deno.env.get("SUPABASE_SERVICE_ROLE_KEY")!);

// Tipi Garmin -> sport dell'app
const SPORT: Record<string, string> = {
  RUNNING: "corsa", TRAIL_RUNNING: "corsa", TREADMILL_RUNNING: "corsa",
  CYCLING: "bici", INDOOR_CYCLING: "bici", LAP_SWIMMING: "nuoto", OPEN_WATER_SWIMMING: "nuoto",
  STRENGTH_TRAINING: "palestra",
};

// Data locale dell'attività (Europe/Rome) a partire dall'istante di inizio e dall'offset Garmin
function giornoLocale(startSec: number, offsetSec: number): string {
  return new Date((startSec + offsetSec) * 1000).toISOString().slice(0, 10);
}

// Crea (o aggiorna) l'allenamento in `workouts` e collega l'attività
async function collegaAllenamento(a: any, userId: string) {
  const sport = SPORT[a.activityType] || "altro";
  const day = giornoLocale(a.startTimeInSeconds, a.startTimeOffsetInSeconds ?? 0);
  const km = a.distanceInMeters ? +(a.distanceInMeters / 1000).toFixed(2) : null;
  const sec = a.durationInSeconds ?? null;

  // Seduta pianificata dello stesso giorno (solo corsa)
  let ps: any = null;
  if (sport === "corsa") {
    const { data } = await sb.from("planned_sessions").select("id,type")
      .eq("athlete_id", userId).eq("session_date", day).eq("is_current", true).limit(1);
    ps = data?.[0] ?? null;
  }

  // Numero progressivo della giornata
  const { count } = await sb.from("workouts").select("id", { count: "exact", head: true })
    .eq("athlete_id", userId).eq("day", day);

  const { data: w, error } = await sb.from("workouts").insert({
    athlete_id: userId,
    day,
    sport,
    session_no: (count ?? 0) + 1,
    type: sport === "corsa" ? (ps?.type ?? "altro") : "altro",
    planned_session_id: ps?.id ?? null,
    distance_km: km,
    duration_s: sec,
    avg_pace_s: sport === "corsa" && km && sec ? Math.round(sec / km) : null,
    avg_hr: a.averageHeartRateInBeatsPerMinute ?? null,
    details: { garmin_summary_id: String(a.summaryId), garmin_type: a.activityType },
    rpe: null,
    source: "garmin",
    notes_private: false,
  }).select("id").single();
  if (error) { console.error("workout insert", error.message); return; }

  await sb.from("garmin_activities").update({ workout_id: w.id }).eq("summary_id", String(a.summaryId));
}

// Utente collegato dal suo ID Garmin
async function utentePerGarmin(garminUserId: string): Promise<string | null> {
  const { data } = await sb.from("garmin_connections").select("user_id").eq("garmin_user_id", garminUserId).maybeSingle();
  return data?.user_id ?? null;
}

// Aggiorna solo i campi che arrivano da Garmin: gli altri (gambe, umore, peso, note) restano invariati
async function aggiornaCheckin(userId: string, day: string, campi: Record<string, number | null>) {
  const v = Object.fromEntries(Object.entries(campi).filter(([, x]) => x !== null && x !== undefined));
  if (!Object.keys(v).length || !day) return;
  const { error } = await sb.from("daily_checkins").upsert({ athlete_id: userId, day, ...v }, { onConflict: "athlete_id,day" });
  if (error) console.error("checkin upsert", error.message);
}

Deno.serve(async (req) => {
  if (req.method !== "POST") return new Response("ok");
  const p = await req.json().catch(() => ({}));
  // Registra i tipi di notifica ricevuti (per verificare quali dati di salute arrivano)
  console.info("tipi", Object.keys(p).join(","), "conteggi", JSON.stringify(Object.fromEntries(Object.entries(p).map(([k, v]: [string, any]) => [k, Array.isArray(v) ? v.length : typeof v]))));

  for (const a of p.activities ?? []) {
    const { data: c } = await sb.from("garmin_connections")
      .select("user_id").eq("garmin_user_id", a.userId).maybeSingle();
    if (!c) continue;

    // Evita duplicati se Garmin rinvia la stessa attività
    const { data: gia } = await sb.from("garmin_activities").select("workout_id")
      .eq("summary_id", String(a.summaryId)).maybeSingle();
    if (gia?.workout_id) continue;

    await sb.from("garmin_activities").upsert({
      summary_id: String(a.summaryId),
      user_id: c.user_id,
      garmin_user_id: a.userId,
      activity_type: a.activityType ?? null,
      started_at: a.startTimeInSeconds ? new Date(a.startTimeInSeconds * 1000).toISOString() : null,
      duration_s: a.durationInSeconds ?? null,
      distance_m: a.distanceInMeters ?? null,
      avg_hr: a.averageHeartRateInBeatsPerMinute ?? null,
      max_hr: a.maxHeartRateInBeatsPerMinute ?? null,
      avg_speed_mps: a.averageSpeedInMetersPerSecond ?? null,
      raw: a,
    });
    await collegaAllenamento(a, c.user_id);
  }

  // Diagnostica: nomi dei campi del primo elemento di ogni tipo di dato
  for (const k of ["dailies", "stressDetails", "sleeps", "hrv"]) {
    const primo = (p as any)[k]?.[0];
    if (primo) console.info("campi", k, Object.keys(primo).join(","));
  }

  // Dati di salute: frequenza a riposo, Body Battery, sonno, HRV
  for (const d of p.dailies ?? []) {
    const u = await utentePerGarmin(d.userId);
    if (u) await aggiornaCheckin(u, d.calendarDate, { rhr_bpm: d.restingHeartRateInBeatsPerMinute ?? null });
  }
  for (const s of p.stressDetails ?? []) {
    const u = await utentePerGarmin(s.userId);
    // Body Battery del risveglio; se manca, ultimo valore della giornata
    const ultimo = Object.entries(s.timeOffsetBodyBatteryValues ?? {})
      .sort((a: any, b: any) => Number(a[0]) - Number(b[0])).pop()?.[1] ?? null;
    const bb = s.bodyBatteryAtWakeTime ?? ultimo;
    if (u) await aggiornaCheckin(u, s.calendarDate, { body_battery: bb as number | null });
  }
  for (const s of p.sleeps ?? []) {
    const u = await utentePerGarmin(s.userId);
    if (u) await aggiornaCheckin(u, s.calendarDate, {
      sleep_min: s.durationInSeconds != null ? Math.round(s.durationInSeconds / 60) : null,
      sleep_score: s.sleepScores?.overall?.value ?? s.overallSleepScore?.value ?? null,
    });
  }
  for (const h of p.hrv ?? []) {
    const u = await utentePerGarmin(h.userId);
    if (u) await aggiornaCheckin(u, h.calendarDate, { hrv_ms: h.lastNightAvg ?? null });
  }

  for (const d of p.deregistrations ?? []) {
    await sb.from("garmin_activities").delete().eq("garmin_user_id", d.userId);
    await sb.from("garmin_connections").delete().eq("garmin_user_id", d.userId);
  }
  return new Response("ok");
});
