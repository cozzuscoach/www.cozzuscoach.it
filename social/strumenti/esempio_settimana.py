"""Esempio: settimana 2-8 novembre 2026 (7 post + 28 storie)."""
from comune import *

# ------------------------------------------------------------------ POST DELLE 13:00
carosello("2026-11-02-freddo", "2026-11-02T13:00", [
    dict(kind="cover", label="Inverno", title="Correre col freddo: 5 regole", sub="Da salvare prima della prossima uscita all’alba", photo="11"),
    dict(kind="point", n=1, title="Vestiti a strati", body="Maglia tecnica traspirante, uno strato termico e un antivento. Esci con un po’ di freddo addosso: dopo 10 minuti sarai alla temperatura giusta.", photo="15", foot="1/5"),
    dict(kind="point", n=2, title="Copri le estremità", body="Mani, orecchie e collo disperdono tanto calore. Guanti leggeri e una fascia valgono più di una giacca pesante.", photo="51", foot="2/5"),
    dict(kind="point", n=3, title="Scaldati più a lungo", body="Con il freddo muscoli e tendini sono più rigidi. Porta il riscaldamento a 10–15 minuti, con qualche andatura e un paio di allunghi.", photo="38", foot="3/5"),
    dict(kind="point", n=4, title="Bevi anche senza sete", body="D’inverno la sete si sente meno, ma con il sudore e il respiro i liquidi si perdono lo stesso.", photo="07", foot="4/5"),
    dict(kind="point", n=5, title="Fatti vedere", body="Il buio arriva presto. Colori chiari, una luce frontale o lampeggiante se corri su strada, e sempre contromano.", photo="36", foot="5/5"),
    dict(kind="cta", title="Il freddo è una stagione di allenamento", body="Un programma costruito sui tuoi dati, rivisto e seguito dal coach. Anche d’inverno.", photo="34"),
], "Correre col freddo: 5 regole da salvare 🥶🏃\n\n"
   "1️⃣ Vestiti a strati: esci con un po’ di freddo addosso\n"
   "2️⃣ Copri mani, orecchie e collo\n"
   "3️⃣ Riscaldamento più lungo: 10–15 minuti\n"
   "4️⃣ Bevi anche se non hai sete\n"
   "5️⃣ Fatti vedere: colori chiari e una luce se corri al buio\n\n"
   "Quale dimentichi più spesso? Scrivilo nei commenti 👇" + CTA + "\n\n" + HT + " #inverno #correreconilfreddo")

video("2026-11-03-cadenza", "2026-11-03T13:00", [
    dict(clip=clip(3), start=0.5, dur=3.0, fx=.22, text=dict(label="Tecnica", title="Corri a passi lunghi?", pos="top")),
    dict(clip=clip(3), start=4.5, dur=3.2, fx=.42, text=dict(title="Ogni passo davanti al corpo è una frenata", tsize=96, pos="top")),
    dict(clip=clip(2), start=2.0, dur=3.2, vertical=True, text=dict(title="Prova passi più corti e più frequenti", tsize=96, pos="top")),
    dict(clip=clip(7), start=1.0, dur=3.4, vertical=True, text=dict(title="Conta i passi in 30 secondi", sub="Moltiplica per 2: è la tua cadenza al minuto.", tsize=100, pos="top")),
    dict(clip=clip(3), start=9.0, dur=3.2, fx=.45, text=dict(title="Aumentala del 5%. Non di più.", sub="Il resto lo fa l’abitudine.", tsize=100, pos="top")),
    dict(clip=clip(2), start=8.0, dur=3.6, vertical=True, text=dict(title="Più leggeri, non più lenti", cta=True, pos="mid", dim=True, tsize=110)),
], "Più passi, meno frenate 👣\n\n"
   "Se fai passi molto lunghi, il piede atterra davanti al corpo e a ogni appoggio frena un po’. "
   "Prova così:\n\n"
   "⏱️ conta i passi di un piede in 30 secondi e moltiplica per 4 (oppure tutti i passi e moltiplica per 2)\n"
   "➕ aumenta la cadenza di circa il 5%, non di più\n"
   "🎧 un metronomo nelle cuffie aiuta per le prime uscite\n\n"
   "Non serve inseguire un numero magico: serve un passo più leggero." + CTA + "\n\n" + HT + " #tecnicadicorsa #cadenza",
    bpm=100, seed=1)

carosello("2026-11-04-achille", "2026-11-04T13:00", [
    dict(kind="cover", label="Infortuni del runner · Ep. 3", title="Il tendine d’Achille", sub="Riconoscerlo presto, gestirlo senza fermarsi del tutto", photo="21", tsize=130),
    dict(kind="point", title="Dove fa male", body="Dietro la caviglia, sopra il tallone. Rigidità al mattino o nei primi minuti di corsa, che spesso migliora quando ti scaldi.", photo="23"),
    dict(kind="point", title="Perché succede", body="Quasi sempre è un carico cresciuto troppo in fretta: più chilometri, salite o velocità tutti insieme. Contano anche polpacci poco forti e un cambio brusco di scarpe.", photo="14"),
    dict(kind="point", title="Cosa fare", body="Riduci il carico invece di fermarti del tutto: meno salite e meno ritmi veloci per qualche settimana, e lavora sulla forza dei polpacci.", photo="60"),
    dict(kind="point", title="L’esercizio base", body="Sollevamenti sui talloni: 3 serie da 15, scendendo lentamente. Prima su due piedi, poi su uno. Il fastidio durante l’esercizio deve restare lieve.", photo="18"),
    dict(kind="point", title="Quando farti vedere", body="Dolore che peggiora di giorno in giorno, gonfiore, zoppia o un “colpo” improvviso dietro la caviglia: fermati e rivolgiti a un medico o a un fisioterapista.", photo="59"),
    dict(kind="cta", title="La prima prevenzione è un carico che cresce con calma", body="Un programma costruito sui tuoi dati, rivisto e seguito dal coach.", photo="29", tsize=92,
         note="Indicazioni di orientamento: non sostituiscono il parere di un professionista."),
], "Infortuni del runner · Ep. 3 — Il tendine d’Achille 🦶\n\n"
   "Rigidità dietro la caviglia al mattino o nei primi minuti di corsa? Nelle slide:\n"
   "📍 dove fa male\n❓ perché succede\n✅ cosa fare senza fermarti del tutto\n🏋️ l’esercizio base per i polpacci\n🚩 quando farti vedere\n\n"
   "Salvalo e giralo a chi corre con te." + ORIENT + CTA + "\n\n" + HT + " #infortuni #tendinedachille #prevenzione")

video("2026-11-05-metodo", "2026-11-05T13:00", [
    dict(clip=clip(1), start=2.0, dur=3.0, fx=.45, text=dict(label="Come funziona", title="Hai una gara in mente?", pos="top")),
    dict(clip=clip(7), start=3.0, dur=3.4, vertical=True, text=dict(title="Scegli la gara e inserisci i tuoi tempi", sub="Chilometri a settimana, giorni liberi, giorni di riposo.", tsize=96, pos="top")),
    dict(clip=clip(3), start=2.0, dur=3.2, fx=.35, text=dict(title="Il programma è costruito sui tuoi dati", sub="Ritmi e zone di frequenza cardiaca su misura.", tsize=96, pos="top")),
    dict(clip=clip(10), start=1.0, dur=3.2, fx=.5, text=dict(title="Il coach lo rivede e lo segue con te", tsize=100, pos="top")),
    dict(clip=clip(2), start=5.0, dur=3.4, vertical=True, text=dict(title="Ogni mattina alle 7 la seduta del giorno", sub="E il perché di quella seduta.", tsize=96, pos="top")),
    dict(clip=clip(0), start=4.0, dur=3.6, fx=.45, text=dict(title="Corri con un metodo", cta=True, pos="mid", dim=True)),
], "Come funziona Cozzu’s Coach 📱🏃\n\n"
   "1️⃣ Scegli la tua gara: 5 km, 10 km, mezza o maratona\n"
   "2️⃣ Inserisci tempi recenti, chilometri a settimana e giorni disponibili\n"
   "3️⃣ Il programma viene costruito sui tuoi dati, diviso in fasi fino al giorno della gara\n"
   "4️⃣ Il coach lo rivede, lo sistema se serve e lo segue con te\n"
   "5️⃣ Ogni mattina alle 7 ricevi la seduta del giorno, con il perché\n\n"
   "Per chi ha lavoro, famiglia e vuole allenarsi con metodo, senza farsi male." + CTA + "\n\n" + HT + " #pianodiallenamento #coachdicorsa",
    bpm=96, seed=2)

carosello("2026-11-06-cena-gara", "2026-11-06T13:00", [
    dict(kind="cover", label="Gara nel weekend?", title="La cena della sera prima", sub="Cosa mangiare (e cosa rimandare) prima della gara", photo="43"),
    dict(kind="point", n=1, title="Niente esperimenti", body="Mangia cose che conosci e che hai già provato prima dei lunghi. Il giorno della gara non è il giorno delle novità.", photo="48", foot="1/5"),
    dict(kind="point", n=2, title="Carboidrati, senza esagerare", body="Pasta o riso in porzione normale, condimento semplice. Le scorte si costruiscono nei giorni prima, non in una sera.", photo="02", foot="2/5"),
    dict(kind="point", n=3, title="Poche fibre e pochi grassi", body="Legumi, verdure crude, fritti e sughi pesanti meglio rimandarli a dopo il traguardo.", photo="41", foot="3/5"),
    dict(kind="point", n=4, title="Bevi con regolarità", body="Acqua durante la giornata, senza riempirti la sera. Il brindisi si fa all’arrivo.", photo="50", foot="4/5"),
    dict(kind="point", n=5, title="Colazione 3 ore prima", body="Qualcosa di semplice e già provato: fette biscottate, marmellata, una banana, il caffè se lo bevi di solito.", photo="16", foot="5/5"),
    dict(kind="cta", title="Buona gara a chi corre questo weekend", body="La preparazione si vede al traguardo. Noi la costruiamo insieme, settimana dopo settimana.", photo="55", tsize=98,
         note="Indicazioni di orientamento: per esigenze specifiche rivolgiti a un nutrizionista."),
], "Gara nel weekend? La cena della sera prima 🍝🏁\n\n"
   "1️⃣ Niente esperimenti: solo cose già provate\n"
   "2️⃣ Carboidrati in porzione normale, condimento semplice\n"
   "3️⃣ Pochi grassi e poche fibre: legumi e fritti dopo la gara\n"
   "4️⃣ Bevi durante la giornata, senza riempirti la sera\n"
   "5️⃣ Colazione semplice circa 3 ore prima del via\n\n"
   "Chi corre questo weekend? Scrivi la tua gara nei commenti 👇" + CTA + "\n\n" + HT + " #pregara #alimentazionerunner #mezzamaratona")

video("2026-11-07-motivazione", "2026-11-07T13:00", [
    dict(clip=clip(0), start=1.0, dur=3.0, fx=.4, text=dict(title="Nessuno vede le uscite col freddo", tsize=104, pos="top")),
    dict(clip=clip(2), start=0.0, dur=3.0, vertical=True, text=dict(title="Né i chilometri che corri da solo", tsize=104, pos="top")),
    dict(clip=clip(7), start=4.0, dur=3.0, vertical=True, text=dict(title="Si vede solo il traguardo", tsize=110, pos="top")),
    dict(clip=clip(3), start=6.0, dur=3.0, fx=.5, text=dict(title="Ma il traguardo è fatto di queste mattine", tsize=100, pos="top")),
    dict(clip=clip(1), start=8.0, dur=3.0, fx=.45, text=dict(title="Buona gara a chi corre domani 💪", tsize=104, pos="top")),
    dict(clip=clip(10), start=6.0, dur=3.6, fx=.5, text=dict(title="Allenati con un piano", cta=True, pos="mid", dim=True)),
], "Nessuno vede le uscite col freddo. Si vede solo il traguardo. 🏁\n\n"
   "Ma il traguardo è fatto proprio di quelle mattine: della sveglia presto, del lento quando non avevi voglia, della costanza.\n\n"
   "Buona gara a chi corre domani, e in bocca al lupo al Cozzu’s Team 💙" + CTA + "\n\n" + HT + " #motivazione #costanza",
    bpm=104, seed=3)

carosello("2026-11-08-settimana", "2026-11-08T13:00", [
    dict(kind="cover", label="Da salvare", title="La settimana in 5 consigli", sub="Il ripasso di tutto quello che abbiamo visto", photo="33"),
    dict(kind="point", n=1, title="Col freddo, a strati", body="Esci con un po’ di freddo addosso e copri le estremità. Il riscaldamento si allunga a 10–15 minuti.", photo="15", foot="1/5"),
    dict(kind="point", n=2, title="Cadenza +5%", body="Passi un po’ più corti e frequenti: il piede atterra più vicino al corpo e il passo diventa più leggero.", photo="57", foot="2/5"),
    dict(kind="point", n=3, title="Achille: carico con calma", body="Rigidità dietro la caviglia? Meno salite e ritmi veloci, più forza nei polpacci. E se peggiora, fatti vedere.", photo="21", foot="3/5"),
    dict(kind="point", n=4, title="Pre-gara senza sorprese", body="Cena semplice e già provata, colazione 3 ore prima. Le novità restano a casa.", photo="45", foot="4/5"),
    dict(kind="point", n=5, title="Il lento è lento", body="Se riesci a parlare in frasi intere sei al ritmo giusto. È lì che costruisci la base.", photo="35", foot="5/5"),
    dict(kind="cta", title="Una nuova settimana inizia domani", body="Corri con un programma costruito sui tuoi dati, rivisto e seguito dal coach.", photo="56"),
], "La settimana in 5 consigli 📌\n\n"
   "🥶 Col freddo: strati e riscaldamento più lungo\n"
   "👣 Cadenza: +5%, passi più leggeri\n"
   "🦶 Tendine d’Achille: carico con calma e polpacci forti\n"
   "🍝 Pre-gara: niente esperimenti\n"
   "🐢 Il lento deve essere lento\n\n"
   "Salvalo per ripassarlo prima della prossima uscita." + CTA + "\n\n" + HT)

# ------------------------------------------------------------------ STORIE
giorni = ["2026-11-02", "2026-11-03", "2026-11-04", "2026-11-05", "2026-11-06", "2026-11-07", "2026-11-08"]

consigli = [  # 07:00
    ("Il lento deve essere lento", "Se riesci a parlare in frasi intere sei al ritmo giusto. Se ti manca il fiato, rallenta.", "24"),
    ("Il giorno dopo un lavoro duro", "Corri piano o riposa. La forma arriva nel recupero, non solo nell’allenamento.", "56"),
    ("Scarpe nuove? A gradi", "Alternale con quelle vecchie per 2–3 settimane prima di usarle in un lungo o in gara.", "26"),
    ("Aumenta poco alla volta", "Pochi chilometri in più a settimana, e ogni 3–4 settimane una settimana più leggera.", "35"),
    ("Prima della gara niente novità", "Né scarpe, né gel, né colazione mai provati. Tutto quello che usi in gara va testato in allenamento.", "42"),
    ("Il lungo costruisce la base", "Un’uscita lunga e tranquilla a settimana regge tutto il resto del programma.", "40"),
    ("Dormire è allenamento", "Sette-otto ore di sonno valgono più di qualsiasi integratore.", "58"),
]
fatti = [  # 15:30
    dict(big="160–170", title="passi al minuto", body="È la cadenza tipica di un runner amatore. Gli atleti d’élite spesso superano i 180.", photo="30", bigsize=170),
    dict(big="2–3×", title="il tuo peso", body="È la forza che il piede riceve a ogni appoggio quando corri.", photo="13"),
    dict(big="N. 1", title="tra i tendini", body="Il tendine d’Achille è il più robusto del corpo umano. Ma va caricato con gradualità.", photo="37"),
    dict(big="42,195", title="chilometri", body="La maratona ha questa misura dalle Olimpiadi di Londra del 1908.", photo="57", bigsize=200),
    dict(big="30°", title="chilometro", body="È lì che in maratona arriva spesso “il muro”: le scorte di carboidrati nei muscoli si stanno esaurendo.", photo="47"),
    dict(big="2–3", title="settimane", body="Dopo due o tre settimane di stop completo la capacità aerobica comincia a calare in modo misurabile.", photo="49"),
    dict(big="↓", title="La discesa", body="Correre in discesa affatica i quadricipiti più della salita: per questo fanno male dopo una gara ondulata.", photo="28"),
]
allenamenti = [  # 18:30
    ("Corsa lenta 40’", "Ritmo da conversazione, poi:", ["4 allunghi da 20 secondi", "recupero camminando tra uno e l’altro"], "10"),
    ("Ripetute in pista", "Dopo 15’ di riscaldamento:", ["6 × 400 m a ritmo 5 km", "recupero 200 m di corsa lenta", "10’ di defaticamento"], "26"),
    ("Forza 20’", "3 giri, 40 secondi per esercizio:", ["affondi alternati", "ponte glutei", "sollevamenti sui talloni", "plank"], "19"),
    ("Fartlek 35’", "Dentro una corsa lenta:", ["8 × (1’ svelto + 1’ piano)", "chiudi con 10’ tranquilli"], "32"),
    ("Scarico", "Il giorno prima di un lungo o di una gara:", ["riposo, oppure 30’ molto facili", "qualche minuto di mobilità"], "37"),
    ("Il lungo", "Ritmo tranquillo, sempre:", ["1h15’–1h30’ in base al livello", "colazione leggera 2 ore prima", "acqua se fa caldo o se superi l’ora"], "33"),
    ("Corsa di recupero", "Dopo la gara o il lungo:", ["30’ molto facili oppure una camminata", "10’ di stretching e mobilità"], "00"),
]
domani = [  # 21:00, anteprima del post del giorno dopo
    ("Più passi, meno frenate", "Il reel sulla cadenza: come correre più leggeri in 15 secondi.", "61"),
    ("Il tendine d’Achille", "Ep. 3 degli infortuni del runner: segnali, cosa fare, quando farti vedere.", "21"),
    ("Come funziona Cozzu’s Coach", "Dal tuo obiettivo alla seduta di ogni mattina, in 20 secondi.", "16"),
    ("La cena prima della gara", "Cosa mangiare e cosa rimandare se corri nel weekend.", "02"),
    ("Si vede solo il traguardo", "Un reel per chi corre domenica.", "55"),
    ("La settimana in 5 consigli", "Il ripasso di tutto, da salvare.", "34"),
    ("Una nuova settimana", "Nuovi consigli ogni giorno. Attiva le notifiche per non perderli.", "13"),
]
for g, d, (t, b, ph), f, (ta, ba, it, pa), (tn, bn, pn) in zip(giorni, range(7), consigli, fatti, allenamenti, domani):
    storia(f"{g}-0700-consiglio", f"{g}T07:00", dict(kind="story", label="Consiglio del giorno", title=t, body=b, photo=ph))
    storia(f"{g}-1530-lo-sapevi", f"{g}T15:30", dict(kind="story", label="Lo sapevi?", **f))
    storia(f"{g}-1830-allenamento", f"{g}T18:30", dict(kind="story", label="Allenamento di oggi", title=ta, body=ba, items=it, note="Esempio: adattalo al tuo livello.", photo=pa))
    storia(f"{g}-2100-domani", f"{g}T21:00", dict(kind="story", label="Domani alle 13", title=tn, body=bn, photo=pn))

salva("settimana")
