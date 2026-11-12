"""Settimana 16-22 novembre 2026 (7 post + 28 storie)."""
from comune import *

# ------------------------------------------------------------------ POST DELLE 13:00
carosello("2026-11-16-zone-fc", "2026-11-16T13:00", [
    dict(kind="cover", label="Metodo", title="Le zone di frequenza cardiaca", sub="Cosa sono e come calcolarle sui tuoi numeri", photo="17", tsize=118),
    dict(kind="point", n=1, title="Due numeri di partenza", body="FC a riposo: misurala al mattino appena sveglio, per qualche giorno. FC massima: meglio da un test o da una gara. Le formule con l’età danno solo una stima.", photo="59", foot="1/5"),
    dict(kind="point", n=2, title="La riserva cardiaca", body="È la differenza tra FC massima e FC a riposo. Con il metodo Karvonen la FC di lavoro è: FC a riposo + una percentuale della riserva. Così conta anche quanto sei allenato.", photo="16", foot="2/5"),
    dict(kind="point", n=3, title="Un esempio", body="FC a riposo 55, massima 185: la riserva è 130.\nZona lenta, 62–72%: 55 + 0,62 × 130 = 136 e 55 + 0,72 × 130 = 149.\nIl lento si corre tra 136 e 149 battiti.", photo="13", foot="3/5"),
    dict(kind="point", n=4, title="Le 5 zone", body="Recupero 50–62%\nLento 62–72%\nMedio 75–82%\nSoglia 82–88%\nVO2max 92–98% della riserva", photo="35", foot="4/5"),
    dict(kind="point", n=5, title="Il cardio non è tutto", body="La FC sale con caldo, stanchezza e poca acqua, e nelle ripetute brevi arriva in ritardo. Usala insieme al ritmo e alle sensazioni.", photo="03", foot="5/5"),
    dict(kind="cta", title="Ritmi e zone sui tuoi numeri", body="Prova il calcolatore su cozzuscoach.it/strumenti, oppure corri con un programma costruito sui tuoi dati, rivisto e seguito dal coach.", photo="32", tsize=98),
], "Le zone di frequenza cardiaca, spiegate semplici ❤️🏃\n\n"
   "1️⃣ Ti servono due numeri: FC a riposo (al mattino, appena sveglio) e FC massima (meglio da un test o da una gara che da una formula)\n"
   "2️⃣ Riserva cardiaca = FC massima − FC a riposo\n"
   "3️⃣ Metodo Karvonen: FC di lavoro = FC a riposo + % della riserva\n"
   "4️⃣ Esempio: riposo 55, massima 185 → il lento si corre tra 136 e 149 battiti\n"
   "5️⃣ La FC va letta insieme al ritmo e alle sensazioni\n\n"
   "Conosci la tua FC a riposo? Scrivila nei commenti 👇\n\n"
   "Indicazioni di orientamento: se hai problemi di cuore o prendi farmaci che modificano la frequenza, chiedi prima al tuo medico." + CTA + "\n\n" + HT + " #frequenzacardiaca #zonecardio #karvonen")

video("2026-11-17-salita", "2026-11-17T13:00", [
    dict(clip=clip(2), start=0.0, dur=3.0, vertical=True, text=dict(label="Tecnica", title="In salita vai in crisi?", pos="top")),
    dict(clip=clip(3), start=5.5, dur=3.4, fx=.45, text=dict(title="Corri a sforzo costante, non a ritmo", sub="In salita il cronometro rallenta: è normale.", tsize=96, pos="top")),
    dict(clip=clip(2), start=8.0, dur=3.2, vertical=True, text=dict(title="Passi più corti e più frequenti", tsize=100, pos="top")),
    dict(clip=clip(10), start=4.0, dur=3.4, fx=.19, text=dict(title="Busto un po’ avanti, dalle caviglie", sub="Non piegarti in vita.", tsize=96, pos="top")),
    dict(clip=clip(7), start=6.0, dur=3.2, vertical=True, text=dict(title="Sguardo avanti, braccia attive", tsize=104, pos="top")),
    dict(clip=clip(3), start=11.0, dur=3.6, fx=.45, text=dict(title="In cima non fermarti: rilancia", cta=True, pos="mid", dim=True, tsize=100)),
], "Le salite si corrono con la testa ⛰️🏃\n\n"
   "Il Salento è quasi tutto piatto, ma quando la salita arriva (in gara o sulla strada di casa) sono questi i dettagli che contano:\n\n"
   "⏱️ sforzo costante, non ritmo costante: il cronometro rallenta ed è giusto così\n"
   "👣 passi più corti e frequenti\n"
   "📐 busto leggermente in avanti dalle caviglie, senza piegarti in vita\n"
   "👀 sguardo una decina di metri avanti, braccia che lavorano\n"
   "🔁 in cima non fermarti: riprendi il tuo ritmo dopo qualche passo\n\n"
   "Qual è la salita che temi di più? 👇" + CTA + "\n\n" + HT + " #tecnicadicorsa #salita",
    bpm=100, seed=7)

carosello("2026-11-18-bandelletta", "2026-11-18T13:00", [
    dict(kind="cover", label="Infortuni del runner · Ep. 5", title="La bandelletta ileotibiale", sub="Il dolore all’esterno del ginocchio", photo="21", tsize=118),
    dict(kind="point", title="Dove fa male", body="Sul lato esterno del ginocchio. Compare spesso dopo un certo numero di chilometri, quasi sempre lo stesso, e peggiora in discesa o scendendo le scale.", photo="01"),
    dict(kind="point", title="Perché succede", body="Di solito un carico cresciuto troppo in fretta, tante discese, la pista corsa sempre nello stesso senso o strade molto inclinate. Spesso c’entrano anche glutei poco forti.", photo="04"),
    dict(kind="point", title="Cosa fare", body="Riduci i chilometri ed evita per un po’ discese e pista. Corri sotto la soglia del fastidio: se compare, accorcia. Bici e nuoto aiutano, se non fanno male.", photo="36"),
    dict(kind="point", title="Rinforza le anche", body="Il gluteo medio tiene stabile il bacino: conchiglia, passi laterali con elastico e plank laterale, 2–3 volte a settimana. Il rullo può dare sollievo, ma da solo non basta.", photo="26"),
    dict(kind="point", title="Quando farti vedere", body="Dolore che non migliora dopo 2–3 settimane di carico ridotto, gonfiore, ginocchio che si blocca o dolore anche camminando: rivolgiti a un medico o a un fisioterapista.", photo="20"),
    dict(kind="cta", title="La prevenzione passa da un carico che cresce con calma", body="Un programma costruito sui tuoi dati, rivisto e seguito dal coach.", photo="56", tsize=86,
         note="Indicazioni di orientamento: non sostituiscono il parere di un professionista."),
], "Infortuni del runner · Ep. 5 — La bandelletta ileotibiale 🦵\n\n"
   "Dolore all’esterno del ginocchio che arriva sempre allo stesso chilometro? Nelle slide:\n"
   "📍 dove fa male\n❓ perché succede\n✅ cosa fare senza fermarti del tutto\n🏋️ gli esercizi per le anche\n🚩 quando farti vedere\n\n"
   "Salvalo e giralo a chi si ferma sempre a metà lungo." + ORIENT + CTA + "\n\n" + HT + " #infortuni #bandellettaileotibiale #ginocchio #prevenzione")

video("2026-11-19-fasi", "2026-11-19T13:00", [
    dict(clip=clip(1), start=3.0, dur=3.2, fx=.45, text=dict(label="Come funziona", title="Come si arriva al giorno della gara?", tsize=100, pos="top")),
    dict(clip=clip(3), start=1.0, dur=3.4, fx=.42, text=dict(title="Fase 1: base", sub="Tanta corsa facile per costruire il motore.", tsize=110, pos="top")),
    dict(clip=clip(10), start=8.0, dur=3.4, fx=.5, text=dict(title="Fase 2: costruzione", sub="Arrivano soglia e ripetute.", tsize=110, pos="top")),
    dict(clip=clip(2), start=2.0, dur=3.4, vertical=True, text=dict(title="Fase 3: specifica", sub="Allenamenti sempre più simili alla gara.", tsize=110, pos="top")),
    dict(clip=clip(7), start=6.0, dur=3.4, vertical=True, text=dict(title="Fase 4: scarico", sub="Meno volume, gambe fresche per il via.", tsize=110, pos="top")),
    dict(clip=clip(0), start=13.0, dur=3.6, fx=.45, text=dict(title="Ogni fase al momento giusto", cta=True, pos="mid", dim=True, tsize=104)),
], "Base, costruzione, specifica, scarico: le 4 fasi di un programma 🗓️🏃\n\n"
   "1️⃣ Base: tanta corsa facile, per costruire resistenza e abitudine\n"
   "2️⃣ Costruzione: entrano soglia, ripetute e un po’ di forza\n"
   "3️⃣ Specifica: gli allenamenti somigliano sempre di più alla gara che hai scelto\n"
   "4️⃣ Scarico: meno volume nelle ultime settimane, per arrivare al via con le gambe fresche\n\n"
   "La durata di ogni fase dipende dalla gara e dal tuo punto di partenza. Con Cozzu’s Coach il programma è costruito sui tuoi dati, rivisto e seguito dal coach, e ogni mattina ti dice anche perché fai quella seduta." + CTA + "\n\n" + HT + " #pianodiallenamento #coachdicorsa #periodizzazione",
    bpm=96, seed=8)

carosello("2026-11-20-gare", "2026-11-20T13:00", [
    dict(kind="cover", label="Gare del weekend", title="Domenica 22 novembre", sub="In Puglia, al Sud e i grandi appuntamenti in Italia", photo="53", tsize=120),
    dict(kind="point", title="Taranto nel Cuore", body="Taranto · 10 km\nLa gara su strada in Puglia in calendario questa domenica.", photo="45"),
    dict(kind="point", title="Al Sud", body="Mezza Reggia-Reggia · Caserta · 21,1 km\nLa 10 km della Perla dello Jonio · Soverato (CZ)\nStraFloridia · Floridia (SR) · 10 km", photo="46"),
    dict(kind="point", title="Nel resto d’Italia", body="Milano21 · Milano · mezza e 10 km\nSan Francesco Marathon · Assisi · 42,2, 21,1 e 10 km\nHalf Marathon Riviera delle Palme · Grottammare (AP)\nIl calendario completo è su cozzuscoach.it/calendario", photo="44"),
    dict(kind="cta", title="Buona gara a chi corre domenica", body="Prossimo obiettivo? Costruiamo insieme la preparazione, settimana dopo settimana.", photo="47", tsize=98),
], "Gare del weekend: domenica 22 novembre 🏁\n\n"
   "📍 Taranto nel Cuore · Taranto · 10 km\n"
   "📍 Mezza Reggia-Reggia · Caserta · 21,1 km\n"
   "📍 La 10 km della Perla dello Jonio · Soverato (CZ)\n"
   "📍 StraFloridia · Floridia (SR) · 10 km\n"
   "✈️ Nel resto d’Italia: Milano21 (mezza e 10 km) e San Francesco Marathon ad Assisi (maratona, mezza e 10 km)\n\n"
   "Controlla sempre orari e iscrizioni sui siti degli organizzatori. Calendario completo su cozzuscoach.it/calendario\n\n"
   "Chi corre? Scrivi la tua gara nei commenti e tagga chi viene con te 👇" + CTA + "\n\n" + HT + " #taranto #tarantonelcuore #10km #mezzamaratona #maratona")

video("2026-11-21-voglia", "2026-11-21T13:00", [
    dict(clip=clip(7), start=0.0, dur=3.0, vertical=True, text=dict(title="Oggi non hai voglia?", tsize=110, pos="top")),
    dict(clip=clip(0), start=1.0, dur=3.0, fx=.4, text=dict(title="La motivazione va e viene", tsize=104, pos="top")),
    dict(clip=clip(2), start=3.0, dur=3.0, vertical=True, text=dict(title="L’abitudine resta", tsize=110, pos="top")),
    dict(clip=clip(3), start=7.0, dur=3.4, fx=.45, text=dict(title="Scarpe ai piedi e 10 minuti. Poi decidi.", tsize=96, pos="top")),
    dict(clip=clip(10), start=12.0, dur=3.0, fx=.5, text=dict(title="Buona gara a chi corre domani 💪", tsize=104, pos="top")),
    dict(clip=clip(1), start=15.0, dur=3.6, fx=.45, text=dict(title="Una corsa alla volta", cta=True, pos="mid", dim=True)),
], "Non serve avere voglia. Serve iniziare. 👟\n\n"
   "La motivazione va e viene, soprattutto con le giornate corte e il freddo. L’abitudine invece resta. "
   "Il trucco è semplice: scarpe ai piedi e 10 minuti di corsa facile. Se dopo 10 minuti vuoi tornare a casa, torni. Quasi sempre, però, continui.\n\n"
   "Buona gara a chi corre domani a Taranto, Caserta, Milano e Assisi 💙" + CTA + "\n\n" + HT + " #motivazione #costanza #abitudine",
    bpm=104, seed=9)

carosello("2026-11-22-settimana", "2026-11-22T13:00", [
    dict(kind="cover", label="Da salvare", title="La settimana in 5 consigli", sub="Il ripasso di tutto quello che abbiamo visto", photo="34"),
    dict(kind="point", n=1, title="Zone sulla riserva", body="FC a riposo + una percentuale della differenza con la FC massima. Il lento sta tra il 62 e il 72% della riserva.", photo="17", foot="1/5"),
    dict(kind="point", n=2, title="Salita a sforzo costante", body="Passi corti, busto un po’ avanti dalle caviglie, sguardo avanti. Il ritmo cala ed è giusto così.", photo="40", foot="2/5"),
    dict(kind="point", n=3, title="Ginocchio esterno", body="Fastidio sempre allo stesso chilometro? Meno discese e pista, più forza nei glutei. Se non passa, fatti vedere.", photo="60", foot="3/5"),
    dict(kind="point", n=4, title="Quattro fasi", body="Base, costruzione, specifica e scarico: ogni allenamento ha il suo momento.", photo="30", foot="4/5"),
    dict(kind="point", n=5, title="Dieci minuti", body="Nei giorni senza voglia: scarpe ai piedi e dieci minuti facili. Poi decidi.", photo="24", foot="5/5"),
    dict(kind="cta", title="Una nuova settimana inizia domani", body="Corri con un programma costruito sui tuoi dati, rivisto e seguito dal coach.", photo="37"),
], "La settimana in 5 consigli 📌\n\n"
   "❤️ Zone cardio: calcolale sulla riserva cardiaca\n"
   "⛰️ Salita: sforzo costante e passi corti\n"
   "🦵 Bandelletta: meno discese, glutei più forti\n"
   "🗓️ Le 4 fasi: base, costruzione, specifica, scarico\n"
   "👟 Senza voglia? Dieci minuti, poi decidi\n\n"
   "Hai corso oggi? Raccontaci com’è andata nei commenti 👇" + CTA + "\n\n" + HT)

# ------------------------------------------------------------------ STORIE
giorni = ["2026-11-16", "2026-11-17", "2026-11-18", "2026-11-19", "2026-11-20", "2026-11-21", "2026-11-22"]

consigli = [  # 07:00
    ("Metti le uscite in agenda", "Scrivi le corse della settimana come appuntamenti. Quello che è in agenda si fa, quello che “se trovo tempo” no.", "51"),
    ("In salita conta lo sforzo", "Non inseguire il ritmo che tieni in piano: tieni costante la fatica e accorcia il passo.", "40"),
    ("Varia il terreno", "Sulla pista cambia senso di marcia ogni tanto. Su strada, quando puoi, scegli tratti piatti e sicuri come il lungomare.", "58"),
    ("Chiedi sempre il perché", "Ogni seduta ha uno scopo: base, soglia, recupero. Se sai a cosa serve, la corri meglio.", "61"),
    ("Studia il percorso", "Gara domenica? Guarda altimetria, ristori e punti difficili. Sapere dove arriva la salita aiuta a dosare le forze.", "54"),
    ("Dieci minuti valgono", "Giornata piena? Una corsa breve è meglio di niente: tiene viva l’abitudine e libera la testa.", "10"),
    ("Scarpe bagnate? Niente termosifone", "Togli le solette e riempile di carta di giornale. Il calore diretto rovina colla e intersuola.", "08"),
]
fatti = [  # 15:30 (venerdì: gare del weekend)
    dict(big="1957", title="Martti Karvonen", body="Il medico finlandese pubblica lo studio da cui nasce il metodo della riserva cardiaca: FC a riposo più una percentuale della differenza con la FC massima.", photo="59", bigsize=210),
    dict(big="1000 m", title="di dislivello", body="È il Vertical Kilometer: una gara tutta in salita, con 1000 metri di dislivello positivo in pochi chilometri.", photo="13", bigsize=210),
    dict(big="2:15:16", title="Abebe Bikila", body="Roma, Olimpiadi del 1960: l’etiope vince la maratona correndo scalzo, con l’arrivo sotto l’Arco di Costantino.", photo="41", bigsize=190),
    dict(big="1960", title="Arthur Lydiard", body="Ai Giochi di Roma due suoi atleti, Peter Snell negli 800 e Murray Halberg nei 5000, vincono l’oro. Il neozelandese è considerato il padre dell’allenamento a fasi, partendo da una lunga base aerobica.", photo="30", bigsize=210),
    None,
    dict(big="3:59.4", title="Roger Bannister", body="Oxford, 6 maggio 1954: il primo miglio corso sotto i 4 minuti. Aveva 25 anni e studiava medicina.", photo="49", bigsize=200),
    dict(big="VO2max", title="A. V. Hill", body="Negli anni ’20 il fisiologo inglese, Nobel per la medicina nel 1922, descrive il massimo consumo di ossigeno: quanto ossigeno il corpo riesce a usare al massimo durante uno sforzo.", photo="39", bigsize=190),
]
gare = dict(kind="story", label="Gare del weekend", title="Domenica 22 novembre", body="In Puglia e non solo:", tsize=104, photo="43",
            items=["Taranto nel Cuore · Taranto · 10 km", "Mezza Reggia-Reggia · Caserta · 21,1 km",
                   "La 10 km della Perla dello Jonio · Soverato (CZ)", "Milano21 e San Francesco Marathon (Assisi)"],
            note="Calendario completo su cozzuscoach.it/calendario")
allenamenti = [  # 18:30
    ("Corsa lenta in zona", "45 minuti nella zona Lento:", ["tra il 62 e il 72% della riserva cardiaca", "se la FC sale troppo, rallenta", "4 allunghi finali da 20 secondi"], "32"),
    ("Ripetute in salita", "Dopo 15’ di riscaldamento:", ["8 × 45 secondi in salita, sforzo sostenuto", "recupero scendendo di corsa lenta", "10’ di defaticamento"], "36"),
    ("Forza per le anche 20’", "3 giri, 40 secondi per esercizio:", ["conchiglia, per lato", "passi laterali con elastico", "ponte glutei", "plank laterale"], "19"),
    ("Corsa media 45’", "Un lavoro di resistenza:", ["15’ facili", "20’ a ritmo medio", "10’ facili"], "57"),
    ("Mobilità 15’", "A casa, a fine giornata:", ["cerchi con le anche", "slanci della gamba, avanti e di lato", "gatto-cammello", "cerchi con le caviglie"], "29"),
    ("Il lungo 1h–1h20’", "Se domenica non corri:", ["ritmo da conversazione, sempre", "acqua se superi l’ora", "il giorno dopo facile o riposo"], "33"),
    ("Dopo la gara", "Defaticamento e recupero:", ["10’ di corsa o camminata facile", "bevi e mangia qualcosa entro un’ora", "domani riposo o 20–30’ facilissimi"], "55"),
]
domani = [  # 21:00, anteprima del post del giorno dopo
    ("In salita vai in crisi?", "Il reel di tecnica: come affrontare le salite senza scoppiare.", "28"),
    ("La bandelletta ileotibiale", "Ep. 5 degli infortuni del runner: il dolore all’esterno del ginocchio.", "23"),
    ("Le 4 fasi del programma", "Dalla base allo scarico: come si arriva al giorno della gara.", "03"),
    ("Gare del weekend", "Taranto, Caserta, Milano, Assisi: chi corre domenica?", "42"),
    ("Oggi non hai voglia?", "Un reel per i giorni senza motivazione.", "11"),
    ("La settimana in 5 consigli", "Il ripasso da salvare.", "31"),
    ("Una nuova settimana", "Nuovi consigli ogni giorno. Attiva le notifiche per non perderli.", "15"),
]
for g, (t, b, ph), f, (ta, ba, it, pa), (tn, bn, pn) in zip(giorni, consigli, fatti, allenamenti, domani):
    storia(f"{g}-0700-consiglio", f"{g}T07:00", dict(kind="story", label="Consiglio del giorno", title=t, body=b, photo=ph))
    if f:
        storia(f"{g}-1530-lo-sapevi", f"{g}T15:30", dict(kind="story", label="Lo sapevi?", **f))
    else:
        storia(f"{g}-1530-gare", f"{g}T15:30", gare)
    storia(f"{g}-1830-allenamento", f"{g}T18:30", dict(kind="story", label="Allenamento di oggi", title=ta, body=ba, items=it, note="Esempio: adattalo al tuo livello.", photo=pa))
    storia(f"{g}-2100-domani", f"{g}T21:00", dict(kind="story", label="Domani alle 13", title=tn, body=bn, photo=pn))

salva("settimana")
