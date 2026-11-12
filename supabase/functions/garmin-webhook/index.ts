// Ricezione push da Garmin: attività, dati di salute e revoche.
// Deployare con --no-verify-jwt. Accetta solo utenti collegati nel database.
import { createClient } from "npm:@supabase/supabase-js@2";

const sb = createClient(Deno.env.get("SUPABASE_URL")!, Deno.env.get("SUPABASE_SERVICE_ROLE_KEY")!);

// Tipi Garmin -> sport dell'app
const SPORT: Record<string, string> = {
  RUNNING: "corsa", TRAIL_RUNNING: "corsa", TREADMILL_RUNNING: "corsa", TRACK_RUNNING: "corsa",
  CYCLING: "bici", INDOOR_CYCLING: "bici", LAP_SWIMMING: "nuoto", OPEN_WATER_SWIMMING: "nuoto",
  STRENGTH_TRAINING: "palestra",
};
const PAUSA_MAX_S = 30 * 60; // attività più vicine di 30 minuti fanno parte dello stesso allenamento

// Giorno locale dell'attività a partire dall'istante di inizio e dall'offset Garmin
function giornoLocale(startSec: number, offsetSec: number): string {
  return new Date((startSec + offsetSec) * 1000).toISOString().slice(0, 10);
}

// Utente collegato dal suo ID Garmin
async function utentePerGarmin(garminUserId: string): Promise<string | null> {
  const { data } = await sb.from("garmin_connections").select("user_id").eq("garmin_user_id", garminUserId).maybeSingle();
  return data?.user_id ?? null;
}

// Ricostruisce gli allenamenti di un atleta in un giorno: un allenamento per gruppo di attività vicine
async function ricalcolaGiorno(userId: string, day: string, sport: string) {
  // Finestra larga in UTC, poi filtro sul giorno locale
  const dal = new Date(day + "T00:00:00+01:00").getTime() - 3 * 3600e3;
  const al = dal + 30 * 3600e3;
  const { data: righe } = await sb.from("garmin_activities")
    .select("summary_id, duration_s, distance_m, avg_hr, max_hr, activity_type, workout_id, raw")
    .eq("user_id", userId)
    .gte("started_at", new Date(dal).toISOString()).lte("started_at", new Date(al).toISOString());

  const attivita = (righe ?? [])
    .filter((r: any) => r.raw?.startTimeInSeconds && SPORT[r.activity_type] === sport
      && giornoLocale(r.raw.startTimeInSeconds, r.raw.startTimeOffsetInSeconds ?? 0) === day)
    .sort((a: any, b: any) => a.raw.startTimeInSeconds - b.raw.startTimeInSeconds);
  if (!attivita.length) return;

  // Gruppi di attività vicine
  const gruppi: any[][] = [];
  let corrente: any[] = [];
  for (const a of attivita) {
    const ultima = corrente[corrente.length - 1];
    if (ultima && a.raw.startTimeInSeconds - (ultima.raw.startTimeInSeconds + (ultima.duration_s ?? 0)) > PAUSA_MAX_S) {
      gruppi.push(corrente); corrente = [];
    }
    corrente.push(a);
  }
  if (corrente.length) gruppi.push(corrente);

  for (const g of gruppi) {
    const ids = g.map((a: any) => a.summary_id);
    const esistenti = [...new Set(g.map((a: any) => a.workout_id).filter((x: any) => x != null))].sort((x: any, y: any) => x - y) as number[];
    const tieni = esistenti[0] ?? null;
    const scarta = esistenti.slice(1);
    if (scarta.length) {
      await sb.from("workout_blocks").delete().in("workout_id", scarta);
      await sb.from("workouts").delete().in("id", scarta).eq("source", "garmin");
    }

    // Totali del gruppo
    const sec = g.reduce((t: number, a: any) => t + (a.duration_s ?? 0), 0);
    const metri = g.reduce((t: number, a: any) => t + (a.distance_m ?? 0), 0);
    const km = metri ? +(metri / 1000).toFixed(2) : null;
    const conHr = g.filter((a: any) => a.avg_hr != null && a.duration_s);
    const durHr = conHr.reduce((t: number, a: any) => t + a.duration_s, 0);
    const hrMedia = durHr ? Math.round(conHr.reduce((t: number, a: any) => t + a.avg_hr * a.duration_s, 0) / durHr) : null;
    const hrMax = Math.max(...g.map((a: any) => a.max_hr ?? 0)) || null;

    // Seduta pianificata del giorno (solo corsa)
    let ps: any = null;
    if (sport === "corsa") {
      const { data } = await sb.from("planned_sessions").select("id,type").eq("athlete_id", userId)
        .eq("session_date", day).eq("is_current", true).limit(1);
      ps = data?.[0] ?? null;
    }

    const campi = {
      distance_km: km,
      duration_s: sec || null,
      avg_pace_s: sport === "corsa" && km && sec ? Math.round(sec / km) : null,
      avg_hr: hrMedia,
      max_hr: hrMax,
      type: sport === "corsa" ? (ps?.type ?? "altro") : "altro",
      planned_session_id: ps?.id ?? null,
      details: { garmin_summary_ids: ids, garmin_types: [...new Set(g.map((a: any) => a.activity_type))] },
    };

    let wid = tieni;
    if (wid) {
      await sb.from("workouts").update(campi).eq("id", wid);
    } else {
      const { count } = await sb.from("workouts").select("id", { count: "exact", head: true })
        .eq("athlete_id", userId).eq("day", day);
      const { data: w, error } = await sb.from("workouts").insert({
        athlete_id: userId, day, sport, session_no: (count ?? 0) + 1,
        notes_private: false, source: "garmin", ...campi,
      }).select("id").single();
      if (error) { console.error("workout insert", error.message); continue; }
      wid = w.id;
    }

    // Blocchi: un blocco per attività, fase in base alla posizione
    await sb.from("workout_blocks").delete().eq("workout_id", wid);
    const n = g.length;
    const blocchi = g.map((a: any, i: number) => ({
      workout_id: wid,
      athlete_id: userId,
      ord: i + 1,
      phase: n === 1 ? "lavoro" : i === 0 ? "riscaldamento" : (n >= 3 && i === n - 1) ? "defaticamento" : "lavoro",
      label: `${a.raw?.activityName ?? "Attività"} (${i + 1}/${n})`,
      distance_km: a.distance_m ? +(a.distance_m / 1000).toFixed(2) : null,
      duration_s: a.duration_s ?? null,
      avg_hr: a.avg_hr ?? null,
      max_hr: a.max_hr ?? null,
      details: { garmin_summary_id: String(a.summary_id) },
    }));
    const { error: eb } = await sb.from("workout_blocks").insert(blocchi);
    if (eb) console.error("blocks insert", eb.message);

    await sb.from("garmin_activities").update({ workout_id: wid }).in("summary_id", ids);
  }
}

// Dati di salute: aggiorna solo i campi ricevuti, gli altri restano invariati
async function aggiornaCheckin(userId: string, day: string, campi: Record<string, number | null>) {
  const v = Object.fromEntries(Object.entries(campi).filter(([, x]) => x !== null && x !== undefined));
  if (!Object.keys(v).length || !day) return;
  const { error } = await sb.from("daily_checkins").upsert({ athlete_id: userId, day, ...v }, { onConflict: "athlete_id,day" });
  if (error) console.error("checkin upsert", error.message);
}

Deno.serve(async (req) => {
  if (req.method !== "POST") return new Response("ok");
  const p = await req.json().catch(() => ({}));
  console.info("tipi", Object.keys(p).join(","));

  for (const a of p.activities ?? []) {
    const u = await utentePerGarmin(a.userId);
    if (!u) continue;
    await sb.from("garmin_activities").upsert({
      summary_id: String(a.summaryId),
      user_id: u,
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
    const sport = SPORT[a.activityType] || "altro";
    if (SPORT[a.activityType]) {
      await ricalcolaGiorno(u, giornoLocale(a.startTimeInSeconds, a.startTimeOffsetInSeconds ?? 0), sport);
    }
  }

  // Dati di salute
  for (const d of p.dailies ?? []) {
    const u = await utentePerGarmin(d.userId);
    if (u) await aggiornaCheckin(u, d.calendarDate, { rhr_bpm: d.restingHeartRateInBeatsPerMinute ?? null });
  }
  for (const s of p.stressDetails ?? []) {
    const u = await utentePerGarmin(s.userId);
    if (!u) continue;
    // Body Battery del risveglio: massimo tra le 00:00 e le 08:00 (ora locale)
    const offLocale = s.startTimeOffsetInSeconds ?? 0;
    let massimo: number | null = null;
    for (const [off, val] of Object.entries(s.timeOffsetBodyBatteryValues ?? {})) {
      const ora = (((s.startTimeInSeconds + Number(off) + offLocale) % 86400) + 86400) % 86400;
      if (ora < 8 * 3600 && typeof val === "number" && (massimo === null || val > massimo)) massimo = val;
    }
    await aggiornaCheckin(u, s.calendarDate, { body_battery: massimo });
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
