"""Settimana 9-15 novembre 2026 (7 post + 28 storie)."""
from comune import *

# ------------------------------------------------------------------ POST DELLE 13:00
carosello("2026-11-09-forza", "2026-11-09T13:00", [
    dict(kind="cover", label="Forza", title="5 esercizi di forza per chi corre", sub="A casa, senza attrezzi, in 20 minuti", photo="38", tsize=118),
    dict(kind="point", n=1, title="Squat", body="Piedi alla larghezza delle spalle, scendi come per sederti e risali spingendo sui talloni. Ginocchia nella direzione delle punte.", photo="06", foot="1/5"),
    dict(kind="point", n=2, title="Affondo indietro", body="Un passo indietro e scendi con il ginocchio verso terra, il busto dritto. È il gesto più vicino alla spinta della corsa.", photo="19", foot="2/5"),
    dict(kind="point", n=3, title="Ponte su una gamba", body="Sdraiato a pancia in su, un piede a terra e l’altra gamba tesa: solleva il bacino. Glutei forti, bacino più stabile quando corri.", photo="20", foot="3/5"),
    dict(kind="point", n=4, title="Sollevamenti sui talloni", body="Sali sulle punte e scendi lentamente, prima su due piedi e poi su uno. Polpacci e tendini lavorano a ogni appoggio.", photo="18", foot="4/5"),
    dict(kind="point", n=5, title="Plank laterale", body="Appoggio sull’avambraccio, corpo in linea dalla testa ai piedi. 20–30 secondi per lato, senza far cadere il bacino.", photo="29", foot="5/5"),
    dict(kind="cta", title="Due volte a settimana bastano", body="Nel programma la forza ha il suo spazio, accanto alla corsa: costruito sui tuoi dati, rivisto e seguito dal coach.", photo="34"),
], "5 esercizi di forza per chi corre 💪🏃\n\n"
   "1️⃣ Squat\n"
   "2️⃣ Affondo indietro\n"
   "3️⃣ Ponte su una gamba\n"
   "4️⃣ Sollevamenti sui talloni\n"
   "5️⃣ Plank laterale\n\n"
   "3 giri, 40 secondi per esercizio, due volte a settimana. Bastano 20 minuti e un tappetino.\n\n"
   "La fai già la forza o la salti sempre? Sii sincero 👇" + CTA + "\n\n" + HT + " #forzaperrunner #esercizi")

video("2026-11-10-braccia", "2026-11-10T13:00", [
    dict(clip=clip(3), start=0.5, dur=3.0, fx=.2, text=dict(label="Tecnica", title="Cosa fanno le tue braccia?", pos="top")),
    dict(clip=clip(3), start=5.0, dur=3.2, fx=.45, text=dict(title="Gomiti piegati a circa 90°", tsize=100, pos="top")),
    dict(clip=clip(2), start=3.0, dur=3.2, vertical=True, text=dict(title="Avanti e indietro, non davanti al petto", tsize=96, pos="top")),
    dict(clip=clip(7), start=2.0, dur=3.4, vertical=True, text=dict(title="Spalle basse, mani morbide", sub="Come se tenessi una patatina senza romperla.", tsize=100, pos="top")),
    dict(clip=clip(10), start=2.0, dur=3.2, fx=.19, text=dict(title="In salita spingi di più con le braccia", tsize=96, pos="top")),
    dict(clip=clip(3), start=10.0, dur=3.6, fx=.45, text=dict(title="Braccia sciolte, passo leggero", cta=True, pos="mid", dim=True, tsize=104)),
], "Le braccia corrono con te 🙌\n\n"
   "Se si irrigidiscono o incrociano davanti al petto, il busto ruota e sprechi energia. Tre dettagli:\n\n"
   "💪 gomiti piegati a circa 90°\n"
   "↕️ movimento avanti e indietro, lungo i fianchi\n"
   "🤲 spalle basse e mani morbide, senza stringere i pugni\n\n"
   "In salita usale di più: il ritmo delle braccia trascina quello delle gambe." + CTA + "\n\n" + HT + " #tecnicadicorsa #postura",
    bpm=100, seed=4)

carosello("2026-11-11-tibia", "2026-11-11T13:00", [
    dict(kind="cover", label="Infortuni del runner · Ep. 4", title="La periostite tibiale", sub="Il dolore lungo la tibia: riconoscerlo e gestirlo", photo="57", tsize=128),
    dict(kind="point", title="Dove fa male", body="Lungo il bordo interno della tibia, di solito nella parte bassa, su qualche centimetro. All’inizio compare nei primi minuti di corsa e poi si attenua.", photo="14"),
    dict(kind="point", title="Perché succede", body="Un carico cresciuto troppo in fretta: tipico di chi ha iniziato da poco o riprende dopo una pausa. Contano anche scarpe consumate e tanto asfalto tutto insieme.", photo="31"),
    dict(kind="point", title="Cosa fare", body="Riduci chilometri e ritmi veloci finché il dolore lo permette. Bici o nuoto aiutano a mantenere la forma, poi si riprende a correre con gradualità.", photo="40"),
    dict(kind="point", title="Rinforza e varia", body="Polpacci e muscoli del piede forti assorbono meglio gli appoggi. Quando puoi, alterna l’asfalto con sterrato o pista.", photo="26"),
    dict(kind="point", title="Quando farti vedere", body="Dolore in un punto preciso che fa male a toccarlo, dolore anche a riposo o di notte, zoppia: fermati e rivolgiti a un medico. Può servire escludere una frattura da stress.", photo="21"),
    dict(kind="cta", title="La prevenzione passa da un carico che cresce con calma", body="Un programma costruito sui tuoi dati, rivisto e seguito dal coach.", photo="32", tsize=86,
         note="Indicazioni di orientamento: non sostituiscono il parere di un professionista."),
], "Infortuni del runner · Ep. 4 — La periostite tibiale 🦵\n\n"
   "Dolore lungo la tibia nei primi minuti di corsa? Nelle slide:\n"
   "📍 dove fa male\n❓ perché succede\n✅ cosa fare senza fermarti del tutto\n🏋️ come rinforzare e variare\n🚩 quando farti vedere\n\n"
   "Salvalo e giralo a chi ha appena iniziato a correre." + ORIENT + CTA + "\n\n" + HT + " #infortuni #periostite #prevenzione")

video("2026-11-12-check-in", "2026-11-12T13:00", [
    dict(clip=clip(0), start=2.0, dur=3.0, fx=.45, text=dict(label="Come funziona", title="Hai dormito male?", pos="top")),
    dict(clip=clip(7), start=1.0, dur=3.4, vertical=True, text=dict(title="Ogni mattina il check-in", sub="Sonno, frequenza a riposo, HRV e sensazioni.", tsize=100, pos="top")),
    dict(clip=clip(3), start=3.0, dur=3.4, fx=.45, text=dict(title="La sera i dati si confrontano con la tua media", tsize=90, pos="top")),
    dict(clip=clip(2), start=6.0, dur=3.4, vertical=True, text=dict(title="Se qualcosa non torna, arriva una proposta al coach", tsize=88, pos="top")),
    dict(clip=clip(10), start=3.0, dur=3.4, fx=.19, text=dict(title="Decide sempre il coach", sub="Per esempio: il lavoro duro slitta di un giorno.", tsize=100, pos="top")),
    dict(clip=clip(3), start=9.0, dur=3.6, fx=.45, text=dict(title="Un programma che ti ascolta", cta=True, pos="mid", dim=True, tsize=104)),
], "Dormito male? Il programma se ne accorge 😴➡️🏃\n\n"
   "Con Cozzu’s Coach ogni mattina fai un check-in veloce: sonno, frequenza a riposo, HRV, sensazioni.\n\n"
   "1️⃣ La sera i tuoi dati vengono confrontati con la tua media\n"
   "2️⃣ Se qualcosa non torna, al coach arriva una proposta per la seduta di domani\n"
   "3️⃣ Decide sempre il coach: spostare le ripetute, accorciare, oppure lasciare tutto com’è\n\n"
   "Perché il piano è importante, ma conta anche la settimana che stai vivendo." + CTA + "\n\n" + HT + " #pianodiallenamento #coachdicorsa #recupero",
    bpm=96, seed=5)

carosello("2026-11-13-gare", "2026-11-13T13:00", [
    dict(kind="cover", label="Gare del weekend", title="Domenica 15 novembre", sub="Le gare in Puglia, e due grandi appuntamenti fuori regione", photo="44", tsize=120),
    dict(kind="point", title="Due Mari Marathon", body="Taranto · 42,2 km\nLa maratona tra Mar Grande e Mar Piccolo.", photo="43"),
    dict(kind="point", title="Mezza Maratona della Grecìa Salentina", body="Calimera (LE) · 21,1 km\nLa mezza di casa nostra, tra i paesi della Grecìa.", photo="53", tsize=70),
    dict(kind="point", title="San Giovanni in Run", body="San Giovanni Rotondo (FG) · 10 km\nUna 10 km sul Gargano per chiudere la stagione su strada.", photo="41"),
    dict(kind="point", title="Fuori regione", body="Maratona e mezza di Verona, Maratona e mezza di Palermo.\nIl calendario completo è su cozzuscoach.it/calendario", photo="42"),
    dict(kind="cta", title="Buona gara a chi corre domenica", body="Prossimo obiettivo? Costruiamo insieme la preparazione, settimana dopo settimana.", photo="55", tsize=98),
], "Gare del weekend: domenica 15 novembre 🏁\n\n"
   "📍 Due Mari Marathon · Taranto · 42,2 km\n"
   "📍 Mezza Maratona della Grecìa Salentina · Calimera (LE) · 21,1 km\n"
   "📍 San Giovanni in Run · San Giovanni Rotondo (FG) · 10 km\n"
   "✈️ Fuori regione: Verona e Palermo, maratona e mezza\n\n"
   "Controlla sempre orari e iscrizioni sui siti degli organizzatori. Calendario completo su cozzuscoach.it/calendario\n\n"
   "Chi corre? Scrivi la tua gara nei commenti e tagga chi viene con te 👇" + CTA + "\n\n" + HT + " #taranto #calimera #greciasalentina #mezzamaratona #maratona")

video("2026-11-14-inizia", "2026-11-14T13:00", [
    dict(clip=clip(2), start=0.0, dur=3.0, vertical=True, text=dict(title="Pensi di essere troppo lento?", tsize=104, pos="top")),
    dict(clip=clip(0), start=6.0, dur=3.2, fx=.4, text=dict(title="Ogni runner ha iniziato da un primo chilometro", tsize=96, pos="top")),
    dict(clip=clip(7), start=5.0, dur=3.0, vertical=True, text=dict(title="Il ritmo giusto è il tuo", tsize=110, pos="top")),
    dict(clip=clip(0), start=12.0, dur=3.2, fx=.4, text=dict(title="Conta tornare a correre la settimana dopo", tsize=96, pos="top")),
    dict(clip=clip(3), start=11.0, dur=3.0, fx=.45, text=dict(title="Buona gara a chi corre domani 💪", tsize=104, pos="top")),
    dict(clip=clip(2), start=9.0, dur=3.6, vertical=True, text=dict(title="Inizia da dove sei", cta=True, pos="mid", dim=True, tsize=110)),
], "Non esiste un ritmo “da runner”. Esiste il tuo. 🏃‍♀️\n\n"
   "Ognuno ha iniziato da un primo chilometro, magari camminando a tratti. "
   "Quello che fa la differenza non è la velocità di oggi, ma tornare a correre la settimana dopo, e quella dopo ancora.\n\n"
   "Buona gara a chi corre domani a Taranto, Calimera e San Giovanni Rotondo 💙" + CTA + "\n\n" + HT + " #motivazione #principianti #primacorsa",
    bpm=104, seed=6)

carosello("2026-11-15-settimana", "2026-11-15T13:00", [
    dict(kind="cover", label="Da salvare", title="La settimana in 5 consigli", sub="Il ripasso di tutto quello che abbiamo visto", photo="33"),
    dict(kind="point", n=1, title="Forza, 2 volte a settimana", body="Squat, affondi, ponte, polpacci e plank laterale: 20 minuti a casa, senza attrezzi.", photo="38", foot="1/5"),
    dict(kind="point", n=2, title="Braccia sciolte", body="Gomiti a circa 90°, movimento avanti e indietro, spalle basse e mani morbide.", photo="30", foot="2/5"),
    dict(kind="point", n=3, title="Tibia: carico con calma", body="Dolore lungo la tibia? Meno chilometri e meno ritmi veloci, più forza nei polpacci. Se il dolore è in un punto preciso, fatti vedere.", photo="57", foot="3/5"),
    dict(kind="point", n=4, title="Ascolta il mattino", body="Sonno e sensazioni dicono molto: dopo una notte difficile, il lavoro duro può aspettare un giorno.", photo="39", foot="4/5"),
    dict(kind="point", n=5, title="Prima del via, scaldati", body="10–15 minuti facili, un po’ di mobilità e qualche allungo. Poi parti più piano di quanto vorresti.", photo="54", foot="5/5"),
    dict(kind="cta", title="Una nuova settimana inizia domani", body="Corri con un programma costruito sui tuoi dati, rivisto e seguito dal coach.", photo="24"),
], "La settimana in 5 consigli 📌\n\n"
   "💪 Forza: 20 minuti, due volte a settimana\n"
   "🙌 Braccia: gomiti a 90°, spalle basse\n"
   "🦵 Periostite: carico con calma e polpacci forti\n"
   "😴 Il check-in del mattino conta\n"
   "🔥 Prima della gara: riscaldamento e partenza prudente\n\n"
   "Hai corso oggi? Raccontaci com’è andata nei commenti 👇" + CTA + "\n\n" + HT)

# ------------------------------------------------------------------ STORIE
giorni = ["2026-11-09", "2026-11-10", "2026-11-11", "2026-11-12", "2026-11-13", "2026-11-14", "2026-11-15"]

consigli = [  # 07:00
    ("Il lunedì riparti piano", "Dopo il weekend, una corsa facile o il riposo. La settimana si costruisce un giorno alla volta.", "36"),
    ("Spalle giù, mani morbide", "Se senti il collo rigido mentre corri, scuoti le braccia per qualche secondo e riparti.", "51"),
    ("Ascolta i piccoli segnali", "Un fastidio che ti cambia il passo non va ignorato: rallenta, accorcia l’uscita e, se non passa, fermati.", "28"),
    ("Annota come ti senti", "Due righe dopo ogni uscita, con sonno e sensazioni: in poche settimane vedi cose che l’orologio non dice.", "39"),
    ("Due giorni alla gara", "Il lavoro ormai è fatto. Riposa, dormi bene e mangia come al solito.", "45"),
    ("Gara domani? Prepara tutto stasera", "Pettorale, spille, chip, scarpe e vestiti adatti al meteo. Domattina pensi solo alla colazione.", "25"),
    ("Dopo il traguardo", "Cammina qualche minuto, bevi e mangia qualcosa entro un’ora. La festa viene dopo il defaticamento.", "55"),
]
fatti = [  # 15:30 (venerdì: gare del weekend)
    dict(big="< 60", title="battiti al minuto", body="Molti runner allenati hanno la frequenza a riposo sotto i 60 battiti: con l’allenamento il cuore pompa più sangue a ogni battito.", photo="59", bigsize=200),
    dict(big="1:59:40", title="Eliud Kipchoge", body="Vienna, ottobre 2019: la prima maratona corsa sotto le 2 ore. Non vale come record, perché corsa con lepri a rotazione e in condizioni controllate.", photo="46", bigsize=190),
    dict(big="26", title="ossa in ogni piede", body="E più di 30 articolazioni. A ogni appoggio lavorano insieme per assorbire il colpo e spingerti avanti.", photo="14"),
    dict(big="VDOT", title="Jack Daniels", body="Il metodo per ricavare i ritmi di allenamento dai tempi di gara viene dall’allenatore e fisiologo americano Jack Daniels, autore di “Daniels’ Running Formula” (1998).", photo="16", bigsize=200),
    None,
    dict(big="1896", title="la prima maratona olimpica", body="Atene, prima Olimpiade moderna: vinse il greco Spyridon Louis, su un percorso di circa 40 km.", photo="41", bigsize=210),
    dict(big="≈ 1", title="kcal per kg per km", body="Correndo si spende circa una caloria per ogni chilo di peso per ogni chilometro, quasi a qualsiasi velocità.", photo="34", bigsize=210),
]
gare = dict(kind="story", label="Gare del weekend", title="Domenica 15 novembre", body="In Puglia e non solo:", tsize=104, photo="42",
            items=["Due Mari Marathon · Taranto · 42,2 km", "Mezza Maratona della Grecìa Salentina · Calimera (LE) · 21,1 km",
                   "San Giovanni in Run · San Giovanni Rotondo (FG) · 10 km", "Maratona di Palermo · 42,2 km"],
            note="Calendario completo su cozzuscoach.it/calendario")
allenamenti = [  # 18:30
    ("Forza a casa 25’", "3 giri, 40 secondi per esercizio:", ["squat", "affondi indietro", "ponte su una gamba", "plank laterale"], "06"),
    ("Ripetute da 1000", "Dopo 15’ di riscaldamento:", ["5 × 1000 m a ritmo 10 km", "recupero 2’ di corsa lenta", "10’ di defaticamento"], "03"),
    ("Corsa facile + tecnica", "45’ a ritmo da conversazione, poi:", ["skip e calciata, 2 × 30 m ciascuno", "4 allunghi da 80 m"], "40"),
    ("Progressivo 40’", "Un ritmo che sale piano:", ["15’ facili", "15’ a ritmo medio", "10’ svelti ma controllati"], "57"),
    ("Corsa facile 30’", "Se domenica corri:", ["30’ facili, niente di più", "qualche minuto di mobilità"], "37"),
    ("Pre-gara 20’", "Il giorno prima della gara:", ["20’ molto facili", "3 allunghi da 15 secondi", "a letto presto"], "58"),
    ("Riscaldamento di gara", "Prima del via:", ["10–15’ di corsa facile", "mobilità dinamica", "3 allunghi brevi", "in griglia 10’ prima della partenza"], "54"),
]
domani = [  # 21:00, anteprima del post del giorno dopo
    ("Cosa fanno le tue braccia?", "Il reel di tecnica: tre dettagli per correre più sciolti.", "30"),
    ("La periostite tibiale", "Ep. 4 degli infortuni del runner: il dolore lungo la tibia.", "31"),
    ("Hai dormito male?", "Come il programma tiene conto di sonno e sensazioni.", "17"),
    ("Gare del weekend", "Taranto, Calimera, San Giovanni Rotondo: chi corre?", "43"),
    ("Inizia da dove sei", "Un reel per chi pensa di essere troppo lento.", "13"),
    ("La settimana in 5 consigli", "Il ripasso da salvare.", "32"),
    ("Una nuova settimana", "Nuovi consigli ogni giorno. Attiva le notifiche per non perderli.", "24"),
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
