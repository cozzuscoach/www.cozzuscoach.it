// Supabase Edge Function: commento (Google Gemini)
// 1. { workout_id }  → commento del coach alla seduta appena registrata (salvato in "feedback")
// 2. { cibo: {...} } → spunti su cosa mangiare adesso (non salvati)
// Il giudizio sulla seduta lo decide il codice con le regole del coach: l'IA varia solo le parole.
// Il giudizio guarda SOLO la fase di lavoro: riscaldamento e defaticamento non si commentano.
// deno-lint-ignore-file no-explicit-any
import { createClient } from "npm:@supabase/supabase-js@2";

const cors = {
  "Access-Control-Allow-Origin": "*",
  "Access-Control-Allow-Headers": "authorization, x-client-info, apikey, content-type",
};
const secretKey = Deno.env.get("SUPABASE_SERVICE_ROLE_KEY")
  || Object.values(JSON.parse(Deno.env.get("SUPABASE_SECRET_KEYS") || "{}"))[0] as string;
const sb = createClient(Deno.env.get("SUPABASE_URL")!, secretKey);

/* ---------- modelli Gemini (come nella funzione nutrienti) ---------- */
let cache: { at: number; lista: string[] } = { at: 0, lista: [] };
async function modelliDisponibili(key: string): Promise<string[]> {
  const forzato = Deno.env.get("GEMINI_MODEL");
  if (forzato) return [forzato];
  if (Date.now() - cache.at < 3600e3 && cache.lista.length) return cache.lista;
  const r = await fetch(`https://generativelanguage.googleapis.com/v1beta/models?key=${key}`);
  if (!r.ok) return ["gemini-flash-latest"];
  const d = await r.json();
  const nomi: string[] = (d.models || [])
    .filter((m: any) => m.supportedGenerationMethods?.includes("generateContent") &&
      /flash/.test(m.name) && !/(image|tts|transcribe|omni|robotics|computer|banana)/.test(m.name))
    .map((m: any) => m.name.replace("models/", ""));
  nomi.sort((a, b) => (b.includes("lite") ? 1 : 0) - (a.includes("lite") ? 1 : 0));
  cache = { at: Date.now(), lista: nomi.slice(0, 4) };
  return cache.lista;
}
async function gemini(key: string, prompt: string, opt: { json?: boolean; temperature?: number; max?: number } = {}) {
  for (const model of await modelliDisponibili(key)) {
    const r = await fetch(`https://generativelanguage.googleapis.com/v1beta/models/${model}:generateContent?key=${key}`, {
      method: "POST",
      headers: { "content-type": "application/json" },
      body: JSON.stringify({
        contents: [{ role: "user", parts: [{ text: prompt }] }],
        generationConfig: {
          temperature: opt.temperature ?? 0.9,
          maxOutputTokens: opt.max ?? 500,
          ...(opt.json ? { responseMimeType: "application/json" } : {}),
          thinkingConfig: { thinkingBudget: 0 },
        },
      }),
    });
    if (r.status === 429) return null;                       // limite raggiunto: si usa il messaggio di riserva
    if (!r.ok) { console.error(model, (await r.text()).slice(0, 160)); continue; }
    const d = await r.json();
    const raw = (d?.candidates?.[0]?.content?.parts || []).map((p: any) => p.text || "").join("").trim();
    if (raw) return { text: raw, model };
  }
  return null;
}

/* ---------- utilità ---------- */
const addDays = (s: string, n: number) => { const d = new Date(s + "T12:00:00Z"); d.setUTCDate(d.getUTCDate() + n); return d.toISOString().slice(0, 10); };
const daysBetween = (a: string, b: string) => Math.round((Date.parse(b + "T12:00:00Z") - Date.parse(a + "T12:00:00Z")) / 864e5);
const pace = (s: number) => `${Math.floor(s / 60)}'${String(Math.round(s % 60)).padStart(2, "0")}"`;
const fmtT = (s: number) => { s = Math.round(s); const h = Math.floor(s / 3600), m = Math.floor(s % 3600 / 60), x = s % 60;
  return h ? `${h}h${String(m).padStart(2, "0")}'${String(x).padStart(2, "0")}"` : `${m}'${String(x).padStart(2, "0")}"`; };
const ore = (min: number) => `${Math.floor(min / 60)}h${String(min % 60).padStart(2, "0")}`;
const pick = <T,>(a: T[]) => a[Math.floor(Math.random() * a.length)];

// Riassunto della sola fase di lavoro: è su questa che si giudica la seduta.
function faseLavoro(B: any[], w: any) {
  const lav = B.filter((b: any) => b.phase === "lavoro" && (b.distance_km || b.duration_s));
  const km  = lav.reduce((s: number, b: any) => s + (+b.distance_km || 0), 0);
  const sec = lav.reduce((s: number, b: any) => s + (+b.duration_s  || 0), 0);
  const hrs = lav.map((b: any) => +(b.avg_hr ?? b.details?.avg_hr) || 0).filter(Boolean);
  const altre = (p: string) => B.filter((b: any) => b.phase === p)
    .reduce((s: number, b: any) => s + (+b.distance_km || 0), 0);
  return {
    distinta: lav.length > 0 && km > 0 && sec > 0,
    km: +km.toFixed(2),
    sec,
    pace: km > 0 && sec > 0 ? Math.round(sec / km) : (w.work_pace_s || null),
    hr: hrs.length ? Math.round(hrs.reduce((a, b) => a + b, 0) / hrs.length) : null,
    risc: +altre("riscaldamento").toFixed(2),
    def:  +altre("defaticamento").toFixed(2),
  };
}

const TIPI: Record<string, string> = { recupero: "corsa di recupero", lento: "lento", medio: "medio", soglia: "soglia", vo2max: "ripetute VO2max",
  ritmo_gara: "ritmo gara", lungo: "lungo", lungo_progressivo: "lungo progressivo", test: "test", gara: "gara", altro: "altro" };
const SPORT: Record<string, string> = { palestra: "lavoro di forza", bici: "bici", nuoto: "nuoto", altro: "altra attività" };
const ZONA_TIPO: Record<string, string> = { soglia: "T", vo2max: "I", ritmo_gara: "RG", medio: "M", test: "I" };
const ZNOMI: Record<string, string> = { R: "recupero", E: "lento", M: "medio", T: "soglia", RG: "ritmo gara", I: "VO2max" };
const QUALITA = ["medio", "soglia", "vo2max", "ritmo_gara", "test"];
const FACILI = ["lento", "recupero", "lungo"];
const DOLORE = /dolor|fastidi|fitt[ae]|male (a|al|alla|allo|ai|agli|alle)\b|infiamm|tendin|contrattur|stiram|strapp|distorsion|gonfi|zoppic|cramp|periostit|fascit/i;
const NEGAZIONE = /(nessun|nessuna|senza|niente|zero|non ho (avuto|sentito)?)\s+(\w+\s+)?(dolor\w*|fastidi\w*|male)/gi;

/* ---------- le regole del coach ---------- */
const CASI: Record<string, string> = {
  qualita_ok: "Seduta di qualità eseguita nei ritmi previsti. Gratificalo in modo concreto e spiega cosa ha costruito per la gara.",
  qualita_veloce: "Seduta di qualità corsa più veloce del ritmo previsto. Riconosci la buona gamba, ma spiega che oltre il ritmo previsto non si allena di più: si accumula fatica che costa nella seduta successiva. Invitalo a restare nei ritmi.",
  sotto_ritmo: "Seduta di qualità più lenta del previsto ma con fatica bassa: aveva margine. Incoraggialo a osare un po' di più la prossima volta, senza rimproverarlo.",
  giornata_storta: "Seduta più faticosa del normale (ritmo più lento o fatica alta). Niente rimproveri: capita. Rassicuralo, invitalo a guardare sonno e recupero e a scriverti se la stanchezza continua.",
  facile_ok: "Corsa facile o lungo eseguiti come previsto, con fatica bassa. Gratificalo spiegando il valore della corsa lenta per la base aerobica.",
  facile_troppo_forte: "Corsa che doveva essere facile, corsa troppo forte (ritmo o frequenza sopra la zona). Spiega perché il lento deve restare lento: costruisce la base e fa recuperare; correrlo forte toglie freschezza alle sedute di qualità.",
  volume_alto: "Seduta corsa bene ma con molti più km del previsto. Riconosci l'impegno e spiega che il volume in più si paga nei giorni successivi: meglio restare sul programma.",
  gara: "Ha appena corso una gara. Complimentati, valorizza il lavoro che c'è dietro e ricorda che nei prossimi giorni serve solo corsa facile.",
  fuori_programma: "Oggi non era prevista una seduta di corsa (riposo o giorno libero). Riconosci la voglia, ma ricorda che il riposo fa parte del programma.",
  altro_sport: "Allenamento diverso dalla corsa. Valorizza il lavoro complementare per la corsa e invitalo a tenere d'occhio la stanchezza delle gambe.",
  dolore: "L'atleta ha segnalato dolore o un fastidio fisico. NIENTE complimenti sulla prestazione. Digli con calma di non forzare, di non correre sopra il dolore e di scriverti per decidere insieme come proseguire. Nessuna diagnosi, nessun rimedio.",
  generico: "Allenamento registrato senza riferimenti sufficienti per un giudizio sui ritmi. Riconosci la costanza e l'utilità di registrare tutto.",
  piano_multiplo: "Seduta di qualità con passi diversi per blocco, scritti nel piano del coach. Giudicala come farebbe un allenatore: confronta il lavoro svolto con ciascun passo previsto, blocco per blocco. Se un blocco è dentro circa 3-5 secondi al km dal previsto, dillo senza enfasi. Se è più veloce, spiega che la fatica in più non allena di più. Se è più lento, dillo con misura e spiega se la fatica suggeriva margine. Se la progressione è stata rispettata, riconoscilo. Riscaldamento e defaticamento non si giudicano MAI, nemmeno se sono più corti del previsto: l'atleta può non avere tempo.",
};
// esempi del tono di Biagio: guidano l'IA e fanno da messaggi di riserva
const ESEMPI: Record<string, string[]> = {
  qualita_ok: [
    "{NOME}, ripetute chiuse tutte dentro il ritmo: è esattamente il lavoro che sposta in avanti il tuo ritmo gara. Bravo anche nella gestione, senza calare alla fine. Ora recupera bene: il prossimo lento, lento davvero.",
    "Seduta da manuale, {NOME}: ritmi giusti e fatica sotto controllo. Sono queste le giornate che in gara fanno la differenza, perché alzano la soglia senza svuotarti.",
  ],
  qualita_veloce: [
    "{NOME}, la gamba c'è e si vede: sei andato più forte del previsto. Però la soglia si allena al ritmo di soglia, non sopra: oltre accumuli fatica che pagherai nella prossima qualità. Tieni il ritmo, la forza ti servirà in gara.",
    "Bella grinta oggi, ma hai tirato oltre il ritmo previsto. Più veloce non vuol dire più allenante: il prossimo lento fallo tranquillo e nella prossima seduta resta dentro le zone.",
  ],
  sotto_ritmo: [
    "Seduta portata a casa, {NOME}, un po' sotto i ritmi previsti, e la fatica mi dice che avevi margine. La prossima volta prova ad agganciare il ritmo dalla prima ripetuta: ce l'hai.",
  ],
  giornata_storta: [
    "{NOME}, oggi le gambe non giravano e la fatica è stata più alta del solito. Capita, non è un passo indietro. Guarda come dormi nei prossimi giorni e se la stanchezza resta scrivimi.",
    "Giornata pesante, si vede da tempi e fatica. Non farne un dramma: una seduta storta in mezzo a tante buone non conta. Stasera mangia bene e dormi, domani si riparte.",
  ],
  facile_ok: [
    "Lento fatto come si deve, {NOME}: ritmo tranquillo e fatica bassa. Sembra poco, ma è il mattone su cui poggia tutto il resto. Avanti così.",
    "Uscita facile e ben gestita, senza fretta e con il cuore basso. È così che si accumulano chilometri senza pagarli.",
  ],
  facile_troppo_forte: [
    "{NOME}, il lento è andato via troppo svelto rispetto alla tua zona. Il lento serve a costruire la base e a recuperare: se lo corri forte non fa bene né l'una né l'altra cosa. Rallenta senza paura, la velocità la facciamo nelle qualità.",
    "Oggi il ritmo da conversazione è diventato un medio. Capita quando ci si sente bene, ma è proprio lì che conviene frenare: arrivare fresco alla prossima qualità vale di più.",
  ],
  volume_alto: [
    "{NOME}, bella uscita, ma sei andato oltre i km previsti. Il volume in più non si sente oggi, si sente tra qualche giorno: resta sul programma, i km giusti sono già quelli.",
  ],
  gara: [
    "{NOME}, gara portata a termine! Goditela: dietro questo risultato ci sono settimane di lavoro. Nei prossimi giorni solo corsa facile, poi guardiamo insieme cosa ci ha detto.",
  ],
  fuori_programma: [
    "Uscita registrata anche se oggi non era prevista. Muoversi va bene, ma il riposo fa parte del programma quanto l'allenamento: tienilo presente nei prossimi giorni.",
  ],
  altro_sport: [
    "Bel lavoro complementare, {NOME}: forza e altri sport proteggono dagli infortuni e rendono la corsa più efficiente. Tieni d'occhio le gambe in vista della prossima seduta di corsa.",
  ],
  dolore: [
    "{NOME}, leggo che hai sentito dolore. Prima di tutto non forzare e non correrci sopra. Domani valuta come stai e scrivimi, così decidiamo insieme come andare avanti.",
    "Hai segnalato un fastidio: la priorità adesso è quella. Niente sedute impegnative finché non ne parliamo, scrivimi appena puoi.",
  ],
  generico: [
    "Allenamento registrato, {NOME}: bravo per la costanza. Ogni seduta nel diario mi aiuta a capire come stai rispondendo al lavoro.",
  ],
  piano_multiplo: [
    "{NOME}, il lavoro di oggi l'hai fatto con la testa: la progressione è partita tranquilla e ha chiuso con la gamba. È il modo giusto di costruire il ritmo gara.",
    "Seduta portata a casa, {NOME}. Dove hai spinto di più l'hai fatto restando dentro il piano: continua così, senza correre oltre quello che ti ho scritto.",
  ],
};

/* ---------- commento alla seduta ---------- */
async function commentoSeduta(userId: string, workoutId: number, key: string | undefined) {
  const { data: w } = await sb.from("workouts").select("*").eq("id", workoutId).maybeSingle();
  if (!w || w.athlete_id !== userId) return { status: 404, body: { error: "allenamento non trovato" } };

  // Dati da Garmin: il commento IA richiede il consenso specifico dell'atleta
  if (w.source === "garmin") {
    const { data: gc } = await sb.from("garmin_connections").select("consent_ai").eq("user_id", userId).maybeSingle();
    if (!gc?.consent_ai) return { status: 200, body: { skipped: "consenso IA assente" } };
  }

  const [blocchi, prof, zone, check, prima, gare, vecchi] = await Promise.all([
    sb.from("workout_blocks").select("*").eq("workout_id", workoutId).order("ord"),
    sb.from("profiles").select("full_name").eq("id", userId).maybeSingle(),
    sb.from("zones").select("*").eq("athlete_id", userId).lte("valid_from", w.day).order("valid_from", { ascending: false }),
    sb.from("daily_checkins").select("*").eq("athlete_id", userId).gte("day", addDays(w.day, -7)).lte("day", w.day),
    sb.from("workouts").select("id,day,sport,type,rpe").eq("athlete_id", userId).gte("day", addDays(w.day, -3)).lte("day", w.day).neq("id", workoutId),
    sb.from("races").select("name,race_date,priority").eq("athlete_id", userId).gte("race_date", w.day).order("race_date").limit(3),
    sb.from("feedback").select("body").eq("athlete_id", userId).eq("kind", "seduta").order("created_at", { ascending: false }).limit(4),
  ]);
  let ps: any = null;
  if (w.planned_session_id) ps = (await sb.from("planned_sessions").select("*").eq("id", w.planned_session_id).maybeSingle()).data;
  if (!ps) ps = (await sb.from("planned_sessions").select("*").eq("athlete_id", userId).eq("session_date", w.day).eq("is_current", true).limit(1)).data?.[0] || null;

  const Z: Record<string, any> = {};
  (zone.data || []).forEach((z: any) => { if (!Z[z.code]) Z[z.code] = z; });
  const B = blocchi.data || [];
  const ck = (check.data || []).find((c: any) => c.day === w.day);
  const fatti: string[] = [];
  const sp = w.sport || "corsa";
  let caso = "generico";

  // note e dolore
  const note = [w.notes, ck?.notes].filter(Boolean).join(" ").slice(0, 300);
  const dolore = DOLORE.test(note.replace(NEGAZIONE, ""));
  if (note) fatti.push(`Note dell'atleta: "${note}"`);

  if (sp !== "corsa") {
    caso = "altro_sport";
    const d = w.details || {};
    fatti.push(`Attività: ${SPORT[sp] || sp}${w.duration_s ? `, durata ${fmtT(w.duration_s)}` : ""}${w.distance_km ? `, ${w.distance_km} km` : ""}`);
    if (sp === "palestra" && d.mode === "esercizi" && d.exercises?.length) fatti.push(`Esercizi: ${d.exercises.map((e: any) => e.name).join(", ")}`);
    if (sp === "palestra" && d.mode === "circuito" && d.wod) fatti.push(`Circuito: ${String(d.wod).slice(0, 150)}`);
    if (sp === "bici" && d.speed_kmh) fatti.push(`Velocità media ${d.speed_kmh} km/h`);
  } else {
    const tipo = w.type;
    if (ps && ps.type !== "riposo") fatti.push(`Seduta prevista: ${ps.title}${ps.target_km ? ` (${ps.target_km} km previsti)` : ""}`);

    // ► il giudizio guarda la sola fase di lavoro
    const L = faseLavoro(B, w);
    if (L.distinta) {
      fatti.push(`LAVORO, è questo che va commentato: ${TIPI[tipo] || tipo}, ${L.km} km in ${fmtT(L.sec)}${L.pace ? `, passo ${pace(L.pace)}/km` : ""}${L.hr ? `, FC media ${L.hr}` : ""}`);
      const cont = [L.risc ? `${L.risc} km di riscaldamento` : "", L.def ? `${L.def} km di defaticamento` : ""].filter(Boolean).join(" e ");
      if (cont) fatti.push(`Contorno da NON giudicare: ${cont}. Totale di giornata ${w.distance_km ?? "?"} km, da non citare come se fosse il lavoro.`);
    } else {
      fatti.push(`Seduta registrata senza fasi distinte: ${TIPI[tipo] || tipo}, ${w.distance_km ?? "?"} km in ${w.duration_s ? fmtT(w.duration_s) : "?"}${w.avg_pace_s ? `, passo medio ${pace(w.avg_pace_s)}/km` : ""}`);
    }

    // ripetute
    const reps = B.filter((b: any) => b.phase === "lavoro" && b.details?.group && b.distance_km && b.duration_s);
    if (reps.length >= 2) {
      const pp = reps.map((b: any) => b.duration_s / b.distance_km);
      fatti.push(`Ripetute: ${reps.map((b: any) => fmtT(b.duration_s)).join(", ")} (passi ${pp.map(pace).join(", ")} al km)`);
      const d = Math.round(pp[pp.length - 1] - pp[0]);
      fatti.push(Math.abs(d) <= 1 ? "Ritmo costante dalla prima all'ultima ripetuta"
        : d < 0 ? `Ultima ripetuta più veloce della prima di ${-d}" al km` : `Ultima ripetuta più lenta della prima di ${d}" al km`);
    }
    const lav = L.pace || w.work_pace_s || w.avg_pace_s;
    const hrGiu = L.hr || w.avg_hr;

    // piano con passi diversi per blocco (es. "2 km a 4'25" + 3 km a 4'19""): il giudizio è dell'allenatore, non della zona
    const passiPiano = (ps?.description || "").match(/\d+'\d{2}"/g) || [];
    const multiPasso = passiPiano.length >= 2 && !reps.length;
    if (multiPasso && ps?.description) {
      const piano = String(ps.description).split("\n").filter((r: string) => /\d+'\d{2}"|lavoro/i.test(r) && !/riscald|defatic/i.test(r)).join(" ").slice(0, 400);
      fatti.push(`Lavoro previsto dal coach: ${piano}`);
      const blocchi = B.filter((b: any) => b.phase === "lavoro" && b.distance_km && b.duration_s);
      if (blocchi.length) fatti.push(`Lavoro svolto, blocco per blocco: ${blocchi.map((b: any) => `${b.distance_km} km a ${pace(b.duration_s / b.distance_km)}/km`).join("; ")}`);
      if (L.hr) fatti.push(`FC media del lavoro ${L.hr}`);
      caso = "piano_multiplo";
    }
    else if (tipo === "gara") caso = "gara";
    else if (!ps || ps.type === "riposo") caso = "fuori_programma";
    else if (caso === "piano_multiplo") { /* giudizio già impostato sopra */ }
    else if (QUALITA.includes(tipo)) {
      const code = reps[0]?.details?.zone || ZONA_TIPO[tipo];
      const z = Z[code];
      if (z && lav) {
        fatti.push(`Ritmo previsto (${ZNOMI[code]}): ${pace(z.pace_min_s)}-${pace(z.pace_max_s)}/km; passo di lavoro ${pace(lav)}/km`);
        if (lav < z.pace_min_s - 3) caso = "qualita_veloce";
        else if (lav > z.pace_max_s + 3) caso = (w.rpe || 0) >= 8 ? "giornata_storta" : "sotto_ritmo";
        else caso = (w.rpe || 0) >= 10 ? "giornata_storta" : "qualita_ok";
        if (reps.length) {
          const dentro = reps.filter((b: any) => { const p = b.duration_s / b.distance_km; return p >= z.pace_min_s - 3 && p <= z.pace_max_s + 3; }).length;
          fatti.push(`${dentro} ripetute su ${reps.length} dentro il ritmo previsto`);
        }
        if (z.hr_min && hrGiu) fatti.push(`FC della fase di lavoro ${hrGiu}, zona prevista ${z.hr_min}-${z.hr_max}`);
      } else caso = (w.rpe || 0) >= 9 ? "giornata_storta" : "qualita_ok";
    } else if (FACILI.includes(tipo) || tipo === "lungo_progressivo") {
      const z = Z[tipo === "recupero" ? "R" : "E"] || Z.E;
      const veloce = tipo !== "lungo_progressivo" && z && lav && lav < z.pace_min_s - 5;
      const fcAlta = tipo !== "lungo_progressivo" && z?.hr_max && hrGiu && hrGiu > z.hr_max + 3;
      if (z) fatti.push(`Zona prevista (${ZNOMI[tipo === "recupero" ? "R" : "E"]}): ${pace(z.pace_min_s)}-${pace(z.pace_max_s)}/km${z.hr_max ? `, FC ${z.hr_min}-${z.hr_max}` : ""}${hrGiu ? `; FC del lavoro ${hrGiu}` : ""}`);
      caso = veloce || fcAlta ? "facile_troppo_forte" : (w.rpe || 0) >= 8 ? "giornata_storta" : "facile_ok";
    }
    if (ps?.target_km && w.distance_km && w.distance_km > ps.target_km * 1.15 + 1) {
      fatti.push(`Km totali ${w.distance_km} contro ${ps.target_km} previsti`);
      if (caso === "qualita_ok" || caso === "facile_ok") caso = "volume_alto";
    }
  }
  if (w.rpe) fatti.push(`Fatica percepita (RPE): ${w.rpe}/10`);

  // contesto: sonno, carico recente, gara
  const altri = (check.data || []).filter((c: any) => c.day !== w.day && c.sleep_min);
  if (ck?.sleep_min) {
    const media = altri.length ? altri.reduce((t: number, c: any) => t + c.sleep_min, 0) / altri.length : null;
    if (ck.sleep_min < 360 || (media && ck.sleep_min < media - 45)) fatti.push(`Sonno della notte: ${ore(ck.sleep_min)}${media ? `, sotto la sua media di ${ore(Math.round(media))}` : ""}`);
  }
  const duri = (prima.data || []).filter((x: any) => QUALITA.includes(x.type) || String(x.type).startsWith("lungo") || (x.rpe || 0) >= 8).length;
  if (duri >= 2) fatti.push(`Negli ultimi 3 giorni aveva già fatto ${duri} sedute impegnative`);
  const gara = (gare.data || []).find((g: any) => g.priority === "A") || gare.data?.[0];
  if (gara && caso !== "gara") fatti.push(`Gara obiettivo tra ${daysBetween(w.day, gara.race_date)} giorni: ${gara.name}`);

  if (dolore) caso = "dolore";

  // testo
  const nome = String(prof.data?.full_name || "").split(" ")[0];
  const conNome = (t: string) => t.replace(/\{NOME\},?\s*/g, (m) => nome ? m.replace("{NOME}", nome) : "").replace(/^\s*[a-zà-ù]/, (c) => c.toUpperCase());
  let testo = "", origin = "riserva";
  if (key) {
    const precedenti = (vecchi.data || []).map((v: any) => `- ${v.body}`).join("\n");
    const prompt = `Sei la voce di Biagio, allenatore di corsa di Cozzu's Coach, in Salento. Scrivi il commento che Biagio farebbe al suo atleta subito dopo l'allenamento appena registrato.

IL GIUDIZIO È GIÀ DECISO, non cambiarlo e non aggiungerne altri:
${CASI[caso]}

DATI DELLA SEDUTA:
${fatti.map((f) => "- " + f).join("\n")}

REGOLE:
- Italiano parlato, del tu, caldo e diretto, da allenatore che conosce bene l'atleta.
- Se vuoi chiamarlo per nome scrivi esattamente {NOME}.
- Da 2 a 4 frasi, al massimo 70 parole. Niente elenchi, titoli o firme. Al massimo una emoji.
- Cita uno o due dati reali tra quelli sopra; non inventare dati.
- Commenta SOLO la fase di lavoro. Riscaldamento e defaticamento non si giudicano MAI, nemmeno se sono più brevi del previsto (l'atleta può non avere tempo): non nominarli e non citarne i chilometri. Non sommare mai le fasi e non citare il totale di giornata come se fosse il lavoro.
- Quando è indicata una gara obiettivo, lega il giudizio a quella: di' cosa questa fase di lavoro costruisce per quella distanza.
- Spiega il perché in modo semplice: cosa allena la seduta, cosa comporta per la prossima o per la gara.
- Non modificare il programma, non prescrivere sedute diverse, non dare indicazioni mediche o diagnosi.
- Non nominare intelligenza artificiale, app o sistemi automatici.
- Varia aperture e giri di frase. Non ripetere le formule di questi commenti recenti:
${precedenti || "- (nessuno)"}

ESEMPI DEL TONO DI BIAGIO (ispirati, non copiarli):
${ESEMPI[caso].map((e) => "- " + e).join("\n")}

Scrivi solo il commento.`;
    const r = await gemini(key, prompt, { temperature: 0.95, max: 400 });
    if (r) { testo = r.text.replace(/^["«]|["»]$/g, "").replace(/\s+/g, " ").trim().slice(0, 600); origin = "ai"; }
  }
  if (!testo) testo = pick(ESEMPI[caso]);
  testo = conNome(testo);

  await sb.from("feedback").delete().eq("workout_id", workoutId).eq("kind", "seduta");
  await sb.from("feedback").insert({ athlete_id: userId, workout_id: workoutId, day: w.day, kind: "seduta", caso, facts: { fatti }, body: testo, origin });
  return { status: 200, body: { body: testo, caso, origin } };
}

/* ---------- spunti per l'alimentazione ---------- */
async function spuntiCibo(c: any, key: string | undefined) {
  if (!key) return { status: 500, body: { error: "Manca GEMINI_API_KEY nei secrets" } };
  const n = (x: any) => Math.max(0, Math.round(Number(x) || 0));
  const s = (x: any, l = 80) => String(x ?? "").slice(0, l);
  const ob = c.obiettivo || {}, mg = c.mangiato || {};
  const pasti = (Array.isArray(c.pasti) ? c.pasti : []).slice(0, 6).map((p: any) => "- " + s(p, 200)).join("\n") || "- nessun pasto registrato";
  const prompt = `Sei Biagio, allenatore di corsa di Cozzu's Coach, in Salento. Un tuo atleta ti chiede cosa mangiare adesso. Dagli 2 o 3 spunti concreti per il prossimo pasto o spuntino.

DATI DI OGGI:
- Ora: ${s(c.ora, 5)}
- Obiettivo di oggi: carboidrati ${n(ob.cho?.[0])}-${n(ob.cho?.[1])} g, proteine ${n(ob.pro?.[0])}-${n(ob.pro?.[1])} g, grassi almeno ${n(ob.fat)} g
- Mangiato finora: carboidrati ${n(mg.cho)} g, proteine ${n(mg.pro)} g, grassi ${n(mg.fat)} g
- Pasti registrati:
${pasti}
- Allenamento di oggi: ${s(c.oggi)}${c.oggi_fatto ? " (già fatto)" : " (non ancora registrato)"}
- Allenamento di domani: ${s(c.domani)}

REGOLE:
- Cibi semplici della cucina italiana e salentina, con porzioni indicative (grammi o unità).
- Copri soprattutto ciò che manca rispetto all'obiettivo e tieni conto dell'allenamento di oggi e di domani (carboidrati prima delle sedute impegnative, proteine dopo l'allenamento).
- Se l'obiettivo è già raggiunto, dillo con serenità e proponi solo qualcosa di leggero se ha fame.
- Mai suggerire di saltare pasti, di mangiare meno del fabbisogno, di dimagrire o di contare calorie. Mai colpevolizzare.
- Niente integratori, tranne bevande o gel sportivi durante o subito dopo l'allenamento. Nessuna indicazione medica.
- Non nominare intelligenza artificiale o app.

Rispondi SOLO con un JSON valido:
{"intro":"una frase breve sulla giornata","idee":[{"titolo":"nome breve del piatto o spuntino","cosa":"cosa e quanto","perche":"perché adesso, in una frase"}]}`;
  const r = await gemini(key, prompt, { json: true, temperature: 0.8, max: 700 });
  if (!r) return { status: 502, body: { error: "spunti non disponibili" } };
  try {
    const d = JSON.parse(r.text.replace(/```json|```/g, "").trim());
    const idee = (d.idee || []).slice(0, 3).map((i: any) => ({ titolo: s(i.titolo, 60), cosa: s(i.cosa, 200), perche: s(i.perche, 200) }))
      .filter((i: any) => i.titolo && i.cosa);
    return { status: 200, body: { intro: s(d.intro, 200), idee } };
  } catch (_) {
    return { status: 502, body: { error: "risposta non interpretabile" } };
  }
}

Deno.serve(async (req) => {
  if (req.method === "OPTIONS") return new Response("ok", { headers: cors });
  const json = (o: unknown, status = 200) =>
    new Response(JSON.stringify(o), { status, headers: { ...cors, "Content-Type": "application/json" } });
  const token = (req.headers.get("Authorization") || "").replace("Bearer ", "");
  const { data: { user } } = await sb.auth.getUser(token);
  if (!user) return json({ error: "non autenticato" }, 401);

  // senza consenso ai dati di salute non si elabora nulla
  const { data: prof } = await sb.from("profiles").select("health_consent_at").eq("id", user.id).maybeSingle();
  if (!prof?.health_consent_at) return json({ error: "consenso mancante" }, 403);

  const key = Deno.env.get("GEMINI_API_KEY");
  const body = await req.json().catch(() => ({}));
  try {
    const r = body.cibo ? await spuntiCibo(body.cibo, key)
      : body.workout_id ? await commentoSeduta(user.id, Number(body.workout_id), key)
      : { status: 400, body: { error: "richiesta non valida" } };
    return json(r.body, r.status);
  } catch (e) {
    console.error(e);
    return json({ error: "errore interno" }, 500);
  }
});