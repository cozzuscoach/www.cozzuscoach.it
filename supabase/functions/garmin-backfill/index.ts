// Funzione temporanea di test: chiede a Garmin di rinviare i dati di salute degli ultimi 2 giorni.
// Gli esiti arrivano al webhook come notifiche. Eliminare dopo il test.
import { createClient } from "npm:@supabase/supabase-js@2";

const sb = createClient(Deno.env.get("SUPABASE_URL")!, Deno.env.get("SUPABASE_SERVICE_ROLE_KEY")!);

Deno.serve(async () => {
  const fine = Math.floor(Date.now() / 1000);
  const inizio = fine - 2 * 86400;
  const { data: conn } = await sb.from("garmin_connections").select("garmin_user_id, access_token").limit(5);
  const esiti: Record<string, unknown> = {};
  for (const c of conn ?? []) {
    const risultati: Record<string, number> = {};
    for (const tipo of ["sleeps", "hrv", "stressDetails", "dailies"]) {
      const url = `https://apis.garmin.com/wellness-api/rest/backfill/${tipo}?summaryStartTimeInSeconds=${inizio}&summaryEndTimeInSeconds=${fine}`;
      const r = await fetch(url, { headers: { Authorization: "Bearer " + c.access_token } });
      risultati[tipo] = r.status;
    }
    esiti[c.garmin_user_id] = risultati;
  }
  return new Response(JSON.stringify(esiti, null, 2), { headers: { "Content-Type": "application/json" } });
});
