// Azioni dell'app atleta: stato, avvio collegamento, consenso IA, revoca.
// Richiede il JWT dell'utente (verify_jwt attivo).
import { createClient } from "npm:@supabase/supabase-js@2";

const sb = createClient(Deno.env.get("SUPABASE_URL")!, Deno.env.get("SUPABASE_SERVICE_ROLE_KEY")!);
// Origini ammesse: l'app può essere aperta con o senza "www"
const ORIGINI = ["https://www.cozzuscoach.it", "https://cozzuscoach.it"];
let ORIGIN = ORIGINI[0];
const corsDi = () => ({
  "Access-Control-Allow-Origin": ORIGIN,
  "Access-Control-Allow-Headers": "authorization, x-client-info, apikey, content-type",
  "Access-Control-Allow-Methods": "POST, OPTIONS",
  "Vary": "Origin",
});
const json = (b: unknown, s = 200) =>
  new Response(JSON.stringify(b), { status: s, headers: { ...corsDi(), "Content-Type": "application/json" } });

const b64u = (buf: ArrayBuffer) =>
  btoa(String.fromCharCode(...new Uint8Array(buf))).replace(/\+/g, "-").replace(/\//g, "_").replace(/=+$/, "");
const rnd = (n: number) => b64u(crypto.getRandomValues(new Uint8Array(n)).buffer);

Deno.serve(async (req) => {
  const o = req.headers.get("Origin") || "";
  ORIGIN = ORIGINI.includes(o) ? o : ORIGINI[0];
  if (req.method === "OPTIONS") return new Response("ok", { headers: corsDi() });
  if (req.method !== "POST") return json({ error: "metodo non valido" }, 405);

  const jwt = (req.headers.get("Authorization") || "").replace("Bearer ", "");
  const { data: { user } } = await sb.auth.getUser(jwt);
  if (!user) return json({ error: "non autenticato" }, 401);
  const uid = user.id;
  const body = await req.json().catch(() => ({}));

  switch (body.action) {
    case "status": {
      const { data } = await sb.from("garmin_connections")
        .select("consent_ai, connected_at").eq("user_id", uid).maybeSingle();
      return json({ connected: !!data, consent_ai: !!data?.consent_ai, connected_at: data?.connected_at ?? null });
    }

    case "connect": {
      const verifier = rnd(48);
      const challenge = b64u(await crypto.subtle.digest("SHA-256", new TextEncoder().encode(verifier)));
      const state = rnd(24);
      // pulizia degli stati scaduti (oltre 1 ora)
      await sb.from("garmin_oauth_states").delete().lt("created_at", new Date(Date.now() - 3600e3).toISOString());
      const { error } = await sb.from("garmin_oauth_states").insert({
        state, user_id: uid, code_verifier: verifier, consent_ai: !!body.consent_ai,
      });
      if (error) return json({ error: error.message }, 500);
      const u = new URL("https://connect.garmin.com/oauth2Confirm");
      u.search = new URLSearchParams({
        response_type: "code",
        client_id: Deno.env.get("GARMIN_CLIENT_ID")!,
        code_challenge: challenge,
        code_challenge_method: "S256",
        redirect_uri: Deno.env.get("GARMIN_REDIRECT_URI")!,
        state,
      }).toString();
      return json({ url: u.toString() });
    }

    case "consent": {
      const { error } = await sb.from("garmin_connections")
        .update({ consent_ai: !!body.consent_ai, consent_at: new Date().toISOString() }).eq("user_id", uid);
      return json(error ? { error: error.message } : { ok: true });
    }

    case "revoke": {
      const { data: c } = await sb.from("garmin_connections").select("access_token").eq("user_id", uid).maybeSingle();
      if (c) {
        // Scollega l'utente lato Garmin; l'esito non blocca la cancellazione locale
        await fetch("https://apis.garmin.com/wellness-api/rest/user/registration", {
          method: "DELETE", headers: { Authorization: "Bearer " + c.access_token },
        }).catch(() => {});
      }
      await sb.from("garmin_activities").delete().eq("user_id", uid);
      await sb.from("garmin_connections").delete().eq("user_id", uid);
      return json({ ok: true });
    }

    default:
      return json({ error: "azione sconosciuta" }, 400);
  }
});
