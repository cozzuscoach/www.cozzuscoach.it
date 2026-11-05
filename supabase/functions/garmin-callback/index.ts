// Ritorno OAuth da Garmin: scambia il codice per i token e salva il collegamento.
// Deve essere deployata con verify_jwt disattivato (--no-verify-jwt).
import { createClient } from "npm:@supabase/supabase-js@2";

const sb = createClient(Deno.env.get("SUPABASE_URL")!, Deno.env.get("SUPABASE_SERVICE_ROLE_KEY")!);
const CID = Deno.env.get("GARMIN_CLIENT_ID")!;
const SEC = Deno.env.get("GARMIN_CLIENT_SECRET")!;
const REDIR = Deno.env.get("GARMIN_REDIRECT_URI")!;
const APP = "https://www.cozzuscoach.it/app/";

const back = (esito: string, passo = "") =>
  Response.redirect(`${APP}?garmin=${esito}${passo ? "&passo=" + passo : ""}`, 302);

Deno.serve(async (req) => {
  const url = new URL(req.url);
  if (url.searchParams.get("error")) return back("annullato");
  const code = url.searchParams.get("code");
  const state = url.searchParams.get("state");
  if (!code || !state) {
    console.error("parametri", url.search);
    return back("err", "parametri");
  }

  const { data: st } = await sb.from("garmin_oauth_states").select("*").eq("state", state).maybeSingle();
  if (!st) return back("err", "stato");
  await sb.from("garmin_oauth_states").delete().eq("state", state); // uso singolo
  if (Date.now() - new Date(st.created_at).getTime() > 15 * 60e3) return back("scaduto");

  const tr = await fetch("https://diauth.garmin.com/di-oauth2-service/oauth/token", {
    method: "POST",
    headers: {
      "Content-Type": "application/x-www-form-urlencoded",
      Authorization: "Basic " + btoa(`${CID}:${SEC}`),
    },
    body: new URLSearchParams({
      grant_type: "authorization_code",
      code,
      code_verifier: st.code_verifier,
      redirect_uri: REDIR,
      client_id: CID,
      client_secret: SEC,
    }),
  });
  if (!tr.ok) {
    console.error("token", tr.status, await tr.text());
    return back("err", "token" + tr.status);
  }
  const t = await tr.json();

  const ur = await fetch("https://apis.garmin.com/wellness-api/rest/user/id", {
    headers: { Authorization: "Bearer " + t.access_token },
  });
  if (!ur.ok) {
    console.error("userid", ur.status, await ur.text());
    return back("err", "utente" + ur.status);
  }
  const { userId } = await ur.json();

  // Un account Garmin collegato a un solo atleta
  await sb.from("garmin_connections").delete().eq("garmin_user_id", userId).neq("user_id", st.user_id);

  const now = new Date();
  const { error } = await sb.from("garmin_connections").upsert({
    user_id: st.user_id,
    garmin_user_id: userId,
    access_token: t.access_token,
    refresh_token: t.refresh_token ?? null,
    expires_at: new Date(now.getTime() + (t.expires_in ?? 0) * 1000).toISOString(),
    consent_ai: st.consent_ai,
    consent_at: now.toISOString(),
    connected_at: now.toISOString(),
  });
  if (error) console.error("upsert", error.message);
  return back(error ? "err" : "ok", error ? "salvataggio" : "");
});
