"""30 ottobre - 1 novembre: ponte prima della prima settimana programmata."""
from comune import *

carosello("2026-10-31-lungo", "2026-10-31T13:00", [
    dict(kind="cover", label="Weekend", title="Il lungo del weekend: 5 regole", sub="Per tornare a casa stanco, non distrutto", photo="33"),
    dict(kind="point", n=1, title="Più lento di quanto pensi", body="Il lungo si corre a ritmo da conversazione. Se a metà non riesci più a parlare, sei partito troppo forte.", photo="35", foot="1/5"),
    dict(kind="point", n=2, title="Allunga con calma", body="Aggiungi 10–15 minuti alla volta rispetto al lungo precedente. Il corpo si adatta al tempo che passi in piedi, non alla fretta.", photo="13", foot="2/5"),
    dict(kind="point", n=3, title="Acqua e carboidrati", body="Oltre l’ora e mezza porta acqua e qualcosa da mangiare. Il lungo è il momento giusto per provare quello che userai in gara.", photo="02", foot="3/5"),
    dict(kind="point", n=4, title="Scegli il percorso", body="Pianeggiante, sicuro, con una fontana o un punto di appoggio a metà. Il lungomare va benissimo.", photo="58", foot="4/5"),
    dict(kind="point", n=5, title="Dopo, recupera", body="Mangia entro un’ora, bevi, cammina un po’. Il giorno dopo corsa leggera o riposo.", photo="19", foot="5/5"),
    dict(kind="cta", title="Il lungo è la base di ogni gara", body="Un programma costruito sui tuoi dati ti dice quanto e quando allungare.", photo="34"),
], "Il lungo del weekend: 5 regole 🏃‍♂️🌅\n\n"
   "1️⃣ Più lento di quanto pensi: ritmo da conversazione\n"
   "2️⃣ Allunga di 10–15 minuti alla volta\n"
   "3️⃣ Oltre l’ora e mezza: acqua e qualcosa da mangiare\n"
   "4️⃣ Percorso piatto e sicuro, con un punto di appoggio\n"
   "5️⃣ Dopo: mangia, bevi e recupera\n\n"
   "Quanto dura il tuo lungo di questo weekend? 👇" + CTA + "\n\n" + HT + " #lungo #mezzamaratona #maratona")

carosello("2026-11-01-fatica", "2026-11-01T13:00", [
    dict(kind="cover", label="Ascolta il corpo", title="La fatica da 1 a 10", sub="La scala dello sforzo percepito, senza orologio", photo="47"),
    dict(kind="point", title="1–3 · Facile", body="Respiro tranquillo, parli senza problemi. È il ritmo del riscaldamento, del recupero e della maggior parte delle uscite lente.", photo="40"),
    dict(kind="point", title="4–6 · Moderato", body="Parli a frasi brevi. È il ritmo del lungo progressivo e delle uscite medie.", photo="30"),
    dict(kind="point", title="7–8 · Impegnativo", body="Riesci a dire poche parole. È la zona delle ripetute e del ritmo gara su 10 km.", photo="57"),
    dict(kind="point", title="9–10 · Massimo", body="Non parli più. Si tocca solo negli ultimi metri di una gara o in sprint brevissimi.", photo="55"),
    dict(kind="point", title="Perché serve", body="Il ritmo cambia con caldo, vento, salite e stanchezza. La sensazione di sforzo no: è il tuo strumento sempre acceso, anche quando l’orologio sbaglia.", photo="16"),
    dict(kind="cta", title="Allenati alla fatica giusta", body="Nel programma ogni seduta ha il suo ritmo, le sue zone e il perché.", photo="32"),
], "La fatica da 1 a 10 💬🏃\n\n"
   "1–3 facile: parli senza problemi\n"
   "4–6 moderato: frasi brevi\n"
   "7–8 impegnativo: poche parole\n"
   "9–10 massimo: non parli più\n\n"
   "Il ritmo cambia con caldo, vento e salite. La sensazione di sforzo resta il tuo strumento più affidabile.\n\n"
   "Di solito a che numero corri il lento? Sii sincero 👇" + CTA + "\n\n" + HT + " #sforzopercepito #rpe")

storie = [
    ("2026-10-30T18:30", "allenamento", dict(label="Allenamento di oggi", title="Scarico del venerdì", body="Se domani fai il lungo:", items=["riposo, oppure 30’ molto facili", "qualche minuto di mobilità"], note="Esempio: adattalo al tuo livello.", photo="37")),
    ("2026-10-30T21:00", "domani", dict(label="Domani alle 13", title="Il lungo del weekend", body="5 regole per tornare a casa stanco, non distrutto.", photo="24")),
    ("2026-10-31T07:00", "consiglio", dict(label="Consiglio del giorno", title="Parti piano, chiudi bene", body="Nel lungo i primi 20 minuti sono i più lenti. Se ti senti bene, accelera un poco solo nell’ultimo quarto.", photo="56")),
    ("2026-10-31T15:30", "lo-sapevi", dict(label="Lo sapevi?", big="60%", title="del corpo", body="Circa il 60% del peso di un adulto è acqua. Basta perderne poco con il sudore per sentire la fatica salire.", photo="50")),
    ("2026-10-31T18:30", "allenamento", dict(label="Allenamento di oggi", title="Il lungo", body="Ritmo tranquillo, sempre:", items=["1h–1h30’ in base al livello", "ultimi 10’ un po’ più sciolti, se stai bene", "acqua oltre l’ora"], note="Esempio: adattalo al tuo livello.", photo="22")),
    ("2026-10-31T21:00", "domani", dict(label="Domani alle 13", title="La fatica da 1 a 10", body="Come riconoscere il ritmo giusto senza guardare l’orologio.", photo="47")),
    ("2026-11-01T07:00", "consiglio", dict(label="Consiglio del giorno", title="Festa? Corri lo stesso", body="Anche 30 minuti facili tengono vivo il ritmo della settimana. Meglio poco che niente.", photo="28")),
    ("2026-11-01T15:30", "lo-sapevi", dict(label="Lo sapevi?", big="10%", title="regola d’oro", body="Una regola pratica molto usata: non aumentare il volume settimanale di molto più del 10% alla volta.", photo="10")),
    ("2026-11-01T18:30", "allenamento", dict(label="Allenamento di oggi", title="Recupero attivo", body="Dopo il lungo di ieri:", items=["30’ molto facili oppure una camminata", "10’ di mobilità per anche e polpacci"], note="Esempio: adattalo al tuo livello.", photo="00")),
    ("2026-11-01T21:00", "domani", dict(label="Domani alle 13", title="Correre col freddo", body="5 regole da salvare per l’inverno.", photo="11")),
]
for q, k, s in storie:
    storia(f"{q[:10]}-{q[11:13]}{q[14:]}-{k}", q, dict(kind="story", **s))
salva("ponte")
