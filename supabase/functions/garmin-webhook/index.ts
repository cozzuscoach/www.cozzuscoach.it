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

Deno.serve(async (req) => {
  if (req.method !== "POST") return new Response("ok");
  const p = await req.json().catch(() => ({}));

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

  for (const d of p.deregistrations ?? []) {
    await sb.from("garmin_activities").delete().eq("garmin_user_id", d.userId);
    await sb.from("garmin_connections").delete().eq("garmin_user_id", d.userId);
  }
  return new Response("ok");
});
