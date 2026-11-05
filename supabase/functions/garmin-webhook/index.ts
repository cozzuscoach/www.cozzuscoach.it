// Ricezione push da Garmin: attività concluse e revoche dell'utente.
// Deployare con --no-verify-jwt. Accetta solo utenti collegati nel database.
import { createClient } from "npm:@supabase/supabase-js@2";

const sb = createClient(Deno.env.get("SUPABASE_URL")!, Deno.env.get("SUPABASE_SERVICE_ROLE_KEY")!);

Deno.serve(async (req) => {
  if (req.method !== "POST") return new Response("ok");
  const p = await req.json().catch(() => ({}));

  for (const a of p.activities ?? []) {
    const { data: c } = await sb.from("garmin_connections")
      .select("user_id").eq("garmin_user_id", a.userId).maybeSingle();
    if (!c) continue;
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
  }

  for (const d of p.deregistrations ?? []) {
    await sb.from("garmin_activities").delete().eq("garmin_user_id", d.userId);
    await sb.from("garmin_connections").delete().eq("garmin_user_id", d.userId);
  }
  return new Response("ok");
});
