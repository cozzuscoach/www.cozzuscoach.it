// Controlli deterministici sul testo del commento. Nessuna dipendenza da Deno: il file si può testare anche in Node.
// Il testo generato dall'IA passa questi controlli prima di essere salvato; se non passa, si riprova o si usa il messaggio di riserva.

export function parole(t: string): number {
  return t.trim().split(/\s+/).filter(Boolean).length;
}

export function frasi(t: string): number {
  return t.split(/[.!?]+/).map((s) => s.trim()).filter(Boolean).length;
}

// frasi vietate in ogni caso
const VIETATE: [RegExp, string][] = [
  [/intelligenza artificiale|\bIA\b|\bapp\b|sistem[ai] automatic/i, "non nominare IA, app o sistemi automatici"],
  [/target stabilit|ritmi stabilit|avevamo stabilito|avevamo concordato|ritmo che avevamo/i, "non inventare target concordati"],
  [/riscald|defatic/i, "non nominare riscaldamento o defaticamento"],
  [/\bultim[oi] \d|\btratto\b|ultimo km/i, "non giudicare tratti interni alla fase"],
];

// affermazioni positive sul ritmo: vietate quando il dato è fuori zona
const POSITIVO = /perfettament|in linea|da manuale|dentro (il|i) (ritmo|ritmi|target|zone)|ritmi giusti|ritmo giusto|esattamente (il|i) ritmo/i;
// affermazioni di eccesso: vietate quando il dato è dentro zona
const ECCESSO = /troppo (svelt|forte|veloc)|più (svelt|veloc|forte)|sopra (la|le) zona|oltre il ritmo/i;

const CASI_POSITIVI_FALSI = ["qualita_veloce", "facile_troppo_forte", "volume_alto", "giornata_storta", "sotto_ritmo"];
const CASI_ECCESSO_FALSO = ["qualita_ok", "facile_ok", "piano_multiplo"];

export function valida(testo: string, fatti: string[], caso: string): string[] {
  const problemi: string[] = [];
  const dati = fatti.join("\n");

  const n = parole(testo);
  if (n > 110) problemi.push(`troppo lungo (${n} parole, massimo 100)`);
  const f = frasi(testo);
  if (f < 2 || f > 5) problemi.push(`${f} frasi, ne servono da 3 a 5`);

  for (const [re, msg] of VIETATE) if (re.test(testo)) problemi.push(msg);

  if (/sonn|dormi|dormit|notte/i.test(testo) && !/Sonno/.test(dati)) problemi.push("parli del sonno senza un dato sul sonno");
  if (/blocc/i.test(testo) && !/blocco per blocco|blocchi|Ripetute/i.test(dati)) problemi.push("citi blocchi che non esistono nella seduta");

  // ogni numero di almeno due cifre deve comparire tra i dati della seduta
  const numeri = testo.match(/\d+(?:[.,]\d+)?/g) || [];
  for (const x of numeri) {
    const c = x.replace(",", ".");
    if (c.replace(".", "").length < 2) continue;
    if (!dati.includes(c)) problemi.push(`il numero ${x} non compare nei dati`);
  }

  // coerenza tra giudizio e dati
  if (CASI_POSITIVI_FALSI.includes(caso) && POSITIVO.test(testo)) problemi.push("dici che il ritmo è in linea, ma i dati dicono il contrario");
  if (CASI_ECCESSO_FALSO.includes(caso) && ECCESSO.test(testo)) problemi.push("dici che hai corso troppo forte, ma i dati dicono il contrario");
  if (caso === "dolore" && /bravo|compliment|ottim|grand/i.test(testo)) problemi.push("con un dolore segnalato niente complimenti sulla prestazione");

  return problemi;
}
