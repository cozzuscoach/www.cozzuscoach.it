// Garmin Connect: collegamento, consenso IA separato, revoca.
// Usa le funzioni Edge garmin-api; le variabili sb, $ e me sono definite in index.html.
const GARMIN_API = "https://pnoxjvssvtusjvbwpkkh.supabase.co/functions/v1/garmin-api";
const GARMIN_KEY = "sb_publishable_ol7Ds9jbamCSwpNpGEPT9Q_ZZvxNHy3";

async function garminCall(body){
  try {
    const { data } = await sb.auth.getSession();
    const r = await fetch(GARMIN_API, {
      method: "POST",
      headers: { "Content-Type": "application/json", apikey: GARMIN_KEY, Authorization: "Bearer " + data.session.access_token },
      body: JSON.stringify(body),
    });
    const j = await r.json().catch(() => ({}));
    if (!r.ok && !j.error) j.error = "HTTP " + r.status;
    return j;
  } catch (e) { return { error: "connessione: " + (e && e.message ? e.message : e) }; }
}

const GARMIN_ESITI = {
  ok: "Garmin collegato. Le nuove attività arriveranno in automatico.",
  annullato: "Collegamento annullato.",
  scaduto: "Il collegamento è scaduto: riprova.",
  err: "Collegamento non riuscito: riprova più tardi.",
};

async function renderGarmin(){
  const box = $("garmin-box");
  if (!box) return;
  const q = new URLSearchParams(location.search).get("garmin");
  if (q) history.replaceState(null, "", location.pathname);
  const esito = q && GARMIN_ESITI[q] ? `<div class="msg ${q === "ok" ? "ok" : "err"}" style="margin-bottom:10px">${GARMIN_ESITI[q]}</div>` : "";

  const s = await garminCall({ action: "status" });
  if (s.error) { box.innerHTML = esito + `<p class="sub">Sezione non disponibile: ${esc(s.error)}</p>`; return; }

  if (!s.connected) {
    box.innerHTML = esito + `
      <p class="sub">Collega Garmin Connect: le attività salvate sull'orologio arrivano all'app subito dopo la fine.</p>
      <label style="display:flex;gap:8px;margin-top:12px;align-items:flex-start">
        <input type="checkbox" id="gm-ai" style="margin-top:3px">
        <span class="sub">Acconsento a usare i dati Garmin (ritmo, frequenza cardiaca, durata) per il commento automatico del coach. Facoltativo e revocabile in ogni momento.</span>
      </label>
      <p class="sub" style="margin-top:8px">Dati trattati e tempi di conservazione: <a class="link" href="/privacy" target="_blank" rel="noopener">informativa</a>.</p>
      <button class="btn primary full" id="gm-go" style="margin-top:12px">Collega Garmin</button>
      <div id="gm-msg" class="msg"></div>`;
    $("gm-go").onclick = async () => {
      $("gm-go").disabled = true;
      const r = await garminCall({ action: "connect", consent_ai: $("gm-ai").checked });
      if (r.url) { location.href = r.url; return; }
      $("gm-go").disabled = false;
      $("gm-msg").className = "msg err";
      $("gm-msg").textContent = "Collegamento non avviato: " + (r.error || "riprova");
    };
    return;
  }

  const d = s.connected_at ? new Date(s.connected_at).toLocaleDateString("it-IT") : "–";
  box.innerHTML = esito + `
    <p class="sub">Garmin collegato dal ${d}. Le attività arrivano in automatico.</p>
    <label style="display:flex;gap:8px;margin-top:12px;align-items:flex-start">
      <input type="checkbox" id="gm-ai2" style="margin-top:3px" ${s.consent_ai ? "checked" : ""}>
      <span class="sub">Uso dei dati Garmin per il commento automatico del coach (IA).</span>
    </label>
    <button class="btn soft full" id="gm-save" style="margin-top:12px">Salva consenso</button>
    <button class="btn full" id="gm-off" style="margin-top:8px;color:var(--warn)">Scollega Garmin</button>
    <div id="gm-msg" class="msg"></div>`;

  $("gm-save").onclick = async () => {
    const r = await garminCall({ action: "consent", consent_ai: $("gm-ai2").checked });
    $("gm-msg").className = r.error ? "msg err" : "msg ok";
    $("gm-msg").textContent = r.error ? "Non salvato: " + r.error : "Consenso aggiornato.";
  };
  $("gm-off").onclick = async () => {
    if (!confirm("Scollegare Garmin ed eliminare le attività ricevute?")) return;
    const r = await garminCall({ action: "revoke" });
    if (r.error) { $("gm-msg").className = "msg err"; $("gm-msg").textContent = "Non riuscito: " + r.error; return; }
    renderGarmin();
  };
}
