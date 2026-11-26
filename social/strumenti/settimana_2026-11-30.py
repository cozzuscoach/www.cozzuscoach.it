"""Settimana 30 novembre - 6 dicembre 2026 (7 post + 28 storie)."""
from comune import *

# ------------------------------------------------------------------ POST DELLE 13:00
carosello("2026-11-30-buio", "2026-11-30T13:00", [
    dict(kind="cover", label="Sicurezza", title="Correre col buio: 5 regole", sub="Da salvare per le uscite di dicembre", photo="56", tsize=118),
    dict(kind="point", n=1, title="Fatti vedere", body="Colori chiari, inserti riflettenti o un gilet ad alta visibilità. Il nero è elegante, ma di sera ti rende invisibile.", photo="11", foot="1/5"),
    dict(kind="point", n=2, title="Una luce davanti, una dietro", body="Una frontale o una luce sul petto per vedere buche e gradini, una lucina rossa dietro per farti vedere da chi arriva.", photo="51", foot="2/5"),
    dict(kind="point", n=3, title="Fuori città, contro il traffico", body="Dove non c’è marciapiede corri sul margine sinistro della strada: vedi le auto che ti vengono incontro e loro vedono te.", photo="40", foot="3/5"),
    dict(kind="point", n=4, title="Percorsi illuminati, o la pista", body="Strade che conosci, ben illuminate e con pochi incroci. Se puoi, le ripetute serali falle in pista.", photo="03", foot="4/5"),
    dict(kind="point", n=5, title="Dillo a qualcuno", body="Avvisa del percorso e porta il telefono. Musica a volume basso, o una sola cuffia: devi sentire cosa succede intorno.", photo="15", foot="5/5"),
    dict(kind="cta", title="Al buio, prima di tutto sicuro", body="Un programma costruito sui tuoi dati, rivisto e seguito dal coach.", photo="37"),
], "Correre col buio: 5 regole da salvare 🔦🏃\n\n"
   "1️⃣ Fatti vedere: colori chiari e inserti riflettenti\n"
   "2️⃣ Una luce davanti e una lucina rossa dietro\n"
   "3️⃣ Fuori città, senza marciapiede: sul margine sinistro, contro il traffico\n"
   "4️⃣ Percorsi illuminati e conosciuti, o la pista\n"
   "5️⃣ Avvisa qualcuno e tieni la musica bassa\n\n"
   "Tu corri prima del lavoro o dopo? Scrivilo nei commenti 👇" + CTA + "\n\n" + HT + " #sicurezza #correrealbuio #inverno")

video("2026-12-01-allunghi", "2026-12-01T13:00", [
    dict(clip=clip(3), start=1.0, dur=3.0, fx=.4, text=dict(label="Tecnica", title="Cosa sono gli allunghi?", tsize=108, pos="top")),
    dict(clip=clip(2), start=6.0, dur=3.4, vertical=True, text=dict(title="20 secondi in progressione", sub="Parti piano, arrivi veloce ma sciolto.", tsize=104, pos="top")),
    dict(clip=clip(10), start=4.0, dur=3.4, fx=.5, text=dict(title="Veloce, non al massimo", sub="Mani morbide, viso rilassato.", tsize=108, pos="top")),
    dict(clip=clip(7), start=4.0, dur=3.2, vertical=True, text=dict(title="Recupero completo, camminando", tsize=100, pos="top")),
    dict(clip=clip(1), start=2.0, dur=3.4, fx=.45, text=dict(title="4–6 alla fine di una corsa facile", tsize=100, pos="top")),
    dict(clip=clip(3), start=11.0, dur=3.6, fx=.45, text=dict(title="Passo veloce, gambe sciolte", cta=True, pos="mid", dim=True, tsize=104)),
], "Gli allunghi: 20 secondi per un passo più sciolto ⚡🏃\n\n"
   "Sono brevi accelerazioni in progressione, da fare alla fine di una corsa facile o prima di un lavoro veloce:\n\n"
   "⏱️ 15–20 secondi, partendo piano e arrivando veloce\n"
   "😌 veloce ma sciolto, mai al massimo\n"
   "🚶 recupero completo camminando\n"
   "🔁 4–6 ripetizioni, un paio di volte a settimana\n\n"
   "Ricordano alle gambe come si corre veloci senza aggiungere fatica." + CTA + "\n\n" + HT + " #tecnicadicorsa #allunghi",
    bpm=108, seed=13)

carosello("2026-12-02-fratture", "2026-12-02T13:00", [
    dict(kind="cover", label="Infortuni del runner · Ep. 7", title="Le fratture da stress", sub="Quando l’osso chiede tregua", photo="21", tsize=124),
    dict(kind="point", title="Come si presenta", body="Un dolore in un punto preciso dell’osso, spesso tibia o piede, che fa male anche premendo con un dito. All’inizio c’è solo correndo, poi anche camminando.", photo="00"),
    dict(kind="point", title="Perché succede", body="L’osso riceve più carico di quanto riesca a ripararne: chilometri aumentati in fretta, poco recupero, poco sonno, mangiare troppo poco rispetto a quanto ti alleni.", photo="04"),
    dict(kind="point", title="Cosa fare", body="Smetti di correre su quel dolore: non stringere i denti. Un dolore che peggiora a ogni uscita non passa “sciogliendosi”.", photo="20"),
    dict(kind="point", title="Come prevenirle", body="Un carico che cresce con calma, una settimana più leggera ogni tanto, forza due volte a settimana, sonno e pasti all’altezza dell’allenamento.", photo="06"),
    dict(kind="point", title="Quando farti vedere", body="Dolore puntuale che non passa in pochi giorni, che senti camminando o a riposo, o con gonfiore. Serve una valutazione medica: a volte la prima radiografia non la mostra.", photo="14", bsize=38),
    dict(kind="cta", title="Ossa forti, carico che cresce con calma", body="Un programma costruito sui tuoi dati, rivisto e seguito dal coach.", photo="05", tsize=96,
         note="Indicazioni di orientamento: non sostituiscono il parere di un professionista."),
], "Infortuni del runner · Ep. 7 — Le fratture da stress 🦴\n\n"
   "Un dolore in un punto preciso della tibia o del piede che non se ne va? Nelle slide:\n"
   "📍 come si presenta\n❓ perché succede\n✅ cosa fare (e cosa non fare)\n🛡️ come prevenirle\n🚩 quando farti vedere\n\n"
   "Salvalo e giralo a chi “corre sopra” ogni dolore." + ORIENT + CTA + "\n\n" + HT + " #infortuni #fratturadastress #prevenzione")

video("2026-12-03-andamento", "2026-12-03T13:00", [
    dict(clip=clip(3), start=5.0, dur=3.0, fx=.42, text=dict(label="Come funziona", title="Come sai se stai migliorando?", tsize=100, pos="top")),
    dict(clip=clip(2), start=1.0, dur=3.4, vertical=True, text=dict(title="Non da una sola uscita", sub="Una giornata storta capita a tutti.", tsize=104, pos="top")),
    dict(clip=clip(10), start=8.0, dur=3.4, fx=.5, text=dict(title="Nell’Andamento vedi i volumi, settimana dopo settimana", tsize=88, pos="top")),
    dict(clip=clip(7), start=6.0, dur=3.4, vertical=True, text=dict(title="La stima della forma, con i tempi previsti", sub="5 km, 10 km, mezza, maratona.", tsize=92, pos="top")),
    dict(clip=clip(0), start=12.0, dur=3.4, fx=.4, text=dict(title="Il carico conta anche forza, bici e nuoto", tsize=94, pos="top")),
    dict(clip=clip(1), start=12.0, dur=3.6, fx=.45, text=dict(title="Guarda la tendenza, non il giorno", cta=True, pos="mid", dim=True, tsize=100)),
], "Come sai se stai migliorando? 📈🏃\n\n"
   "Non da una sola uscita: il vento, il sonno, una giornata pesante al lavoro cambiano tutto. Conta la tendenza.\n\n"
   "Nella sezione Andamento dell’app Cozzu’s Coach trovi:\n"
   "📊 i volumi settimana dopo settimana\n"
   "🏁 una stima della forma, con i tempi previsti su 5 km, 10 km, mezza e maratona\n"
   "🚴 il carico di allenamento di tutti gli sport, non solo della corsa\n\n"
   "E il coach guarda gli stessi dati con te." + CTA + "\n\n" + HT + " #pianodiallenamento #coachdicorsa #progressi",
    bpm=96, seed=14)

carosello("2026-12-04-gare", "2026-12-04T13:00", [
    dict(kind="cover", label="Gare del weekend", title="Domenica 6 dicembre", sub="In Puglia, al Sud, in Italia e a Valencia", photo="42", tsize=120),
    dict(kind="point", title="In Puglia", body="Mezzamaratona Città di Monopoli\nMonopoli (BA) · 21,1 km\nLa mezza pugliese in calendario questa domenica.", photo="54"),
    dict(kind="point", title="Al Sud", body="10 km di Capo Peloro · Messina\nCagliariRespira · Cagliari · 21,1 km\nMezza di Termini Imerese (PA) · 21,1 km\nMaratona di Latina · 42,2 km", photo="53"),
    dict(kind="point", title="In Italia e all’estero", body="Sanremo · 42,2 e 21,1 km\nComo Lake Half Marathon · 21,1 km\nMartedì 8: Mezza di San Miniato (PI)\nMaratona di Valencia · 42,2 km", photo="52"),
    dict(kind="cta", title="Buona gara a chi corre domenica", body="Il 13 dicembre c’è la Salento Half Marathon a Collepasso. Il calendario completo è su cozzuscoach.it/calendario", photo="55", tsize=98),
], "Gare del weekend: domenica 6 dicembre 🏁\n\n"
   "📍 Mezzamaratona Città di Monopoli · Monopoli (BA) · 21,1 km\n"
   "📍 10 km di Capo Peloro · Messina · 10 km\n"
   "📍 CagliariRespira · Cagliari · 21,1 km\n"
   "📍 Mezza Maratona Città di Termini Imerese (PA) · 21,1 km\n"
   "📍 Maratona di Latina · 42,2 km\n"
   "✈️ E poi Sanremo (maratona e mezza), Como Lake Half Marathon e la Maratona di Valencia. Martedì 8 dicembre la Mezza di San Miniato (PI).\n\n"
   "Domenica 13 tocca al Salento: Salento Half Marathon a Collepasso (LE).\n\n"
   "Controlla sempre orari e iscrizioni sui siti degli organizzatori. Calendario completo su cozzuscoach.it/calendario\n\n"
   "Chi corre? Scrivi la tua gara nei commenti e tagga chi viene con te 👇" + CTA + "\n\n" + HT + " #monopoli #mezzamaratona #maratona #valenciamarathon #sanremo")

video("2026-12-05-dicembre", "2026-12-05T13:00", [
    dict(clip=clip(0), start=2.0, dur=3.2, fx=.4, text=dict(title="Dicembre: cene, feste, giornate corte", tsize=100, pos="top")),
    dict(clip=clip(7), start=1.0, dur=3.0, vertical=True, text=dict(title="Qualche uscita salterà", tsize=110, pos="top")),
    dict(clip=clip(3), start=7.5, dur=3.2, fx=.45, text=dict(title="Non serve la settimana perfetta", tsize=108, pos="top")),
    dict(clip=clip(2), start=3.0, dur=3.4, vertical=True, text=dict(title="Serve non fermarsi del tutto", sub="Anche 30 minuti facili contano.", tsize=104, pos="top")),
    dict(clip=clip(10), start=12.0, dur=3.0, fx=.5, text=dict(title="Buona gara a chi corre domani 💪", tsize=104, pos="top")),
    dict(clip=clip(1), start=17.0, dur=3.6, fx=.45, text=dict(title="Chiudi l’anno correndo", cta=True, pos="mid", dim=True, tsize=108)),
], "Dicembre non deve essere perfetto 🎄🏃\n\n"
   "Pranzi, cene, regali, il buio alle cinque. Qualche uscita salterà, ed è normale. "
   "Quello che fa la differenza a gennaio non è la settimana perfetta: è non fermarsi del tutto. Anche 30 minuti facili tengono vivo il filo.\n\n"
   "Qual è la tua uscita salva-dicembre? Scrivila nei commenti 👇\n\n"
   "E buona gara a chi corre domani a Monopoli, Sanremo e Valencia 💙" + CTA + "\n\n" + HT + " #motivazione #costanza #dicembre",
    bpm=100, seed=15)

carosello("2026-12-06-settimana", "2026-12-06T13:00", [
    dict(kind="cover", label="Da salvare", title="La settimana in 5 consigli", sub="Il ripasso di tutto quello che abbiamo visto", photo="35"),
    dict(kind="point", n=1, title="Al buio, fatti vedere", body="Colori chiari, una luce davanti e una dietro. Fuori città, senza marciapiede, contro il traffico.", photo="36", foot="1/5"),
    dict(kind="point", n=2, title="Allunghi veloci ma sciolti", body="15–20 secondi in progressione, recupero camminando, 4–6 alla fine di una corsa facile.", photo="10", foot="2/5"),
    dict(kind="point", n=3, title="Dolore in un punto dell’osso? Fermati", body="Se non passa in pochi giorni o lo senti camminando, fatti vedere. Il carico cresce con calma.", photo="17", foot="3/5"),
    dict(kind="point", n=4, title="Guarda la tendenza", body="La forma non si giudica da una sola uscita. Volumi e tempi previsti si leggono settimana dopo settimana.", photo="16", foot="4/5"),
    dict(kind="point", n=5, title="Dicembre non deve essere perfetto", body="Qualche uscita salterà. Conta non fermarsi del tutto: anche 30 minuti facili.", photo="33", foot="5/5"),
    dict(kind="cta", title="Una nuova settimana inizia domani", body="Corri con un programma costruito sui tuoi dati, rivisto e seguito dal coach.", photo="32",
         note="Indicazioni di orientamento: non sostituiscono il parere di un medico o di un fisioterapista."),
], "La settimana in 5 consigli 📌\n\n"
   "🔦 Al buio: fatti vedere e corri contro il traffico\n"
   "⚡ Allunghi: veloci ma sciolti\n"
   "🦴 Dolore in un punto dell’osso: fermati e fatti vedere\n"
   "📈 Progressi: guarda la tendenza, non il giorno\n"
   "🎄 Dicembre: non serve la settimana perfetta\n\n"
   "Hai corso oggi? Raccontaci com’è andata nei commenti 👇" + ORIENT + CTA + "\n\n" + HT)

# ------------------------------------------------------------------ STORIE
giorni = ["2026-11-30", "2026-12-01", "2026-12-02", "2026-12-03", "2026-12-04", "2026-12-05", "2026-12-06"]

consigli = [  # 07:00
    ("Esci col buio? Accendi la luce", "Una frontale davanti e una lucina rossa dietro: costano poco e ti fanno vedere da lontano.", "13"),
    ("Gli allunghi non sono sprint", "Veloci ma sciolti: se stringi i denti o alzi le spalle, stai andando troppo forte.", "10"),
    ("Ogni tanto una settimana leggera", "Dopo 3 o 4 settimane di carico, una con meno chilometri aiuta il corpo ad assorbire il lavoro fatto.", "35"),
    ("Confronta mesi, non giorni", "Una sola uscita storta non dice niente sulla tua forma. Guarda come cambiano le settimane.", "59"),
    ("Parti più piano di quanto vorresti", "In gara il primo chilometro troppo veloce si paga alla fine. Lascia che siano gli altri a scappare.", "41"),
    ("Dopo la corsa, cambiati subito", "D’inverno i vestiti bagnati di sudore ti raffreddano in pochi minuti. Porta una maglia asciutta.", "48"),
    ("Cura i piedi", "Unghie corte, calze tecniche e niente cotone: meno vesciche, più chilometri sereni.", "08"),
]
fatti = [  # 15:30 (venerdì: gare del weekend)
    dict(big="1908", title="Dorando Pietri", body="Londra: entra per primo nello stadio, cade più volte e viene aiutato a tagliare il traguardo. Squalificato, la regina Alessandra gli dona una coppa d’argento.", photo="45", bigsize=210),
    dict(big="42,195", title="chilometri", body="La distanza della maratona di Londra 1908 diventa la misura ufficiale nel 1921. Prima le maratone olimpiche avevano lunghezze diverse.", photo="43", bigsize=200),
    dict(big="206", title="ossa", body="Sono quelle dello scheletro di un adulto. L’osso è un tessuto vivo: si rinnova di continuo e si adatta ai carichi che riceve.", photo="31", bigsize=230),
    dict(big="1984", title="Joan Benoit", body="Los Angeles: la prima maratona olimpica femminile della storia. La vince l’americana Joan Benoit in 2:24:52.", photo="49", bigsize=210),
    None,
    dict(big="127", title="partenti", body="La prima maratona di New York, nel 1970, si corse tutta dentro Central Park: 127 al via, 55 all’arrivo.", photo="44", bigsize=230),
    dict(big="13", title="runner", body="Il primo parkrun, a Bushy Park (Londra) nel 2004: 5 km gratuiti, cronometrati, ogni sabato mattina. Oggi si corre in tutto il mondo.", photo="34", bigsize=230),
]
gare = dict(kind="story", label="Gare del weekend", title="Domenica 6 dicembre", body="In Puglia e non solo:", tsize=104, photo="46",
            items=["Mezzamaratona Città di Monopoli (BA) · 21,1 km", "10 km di Capo Peloro · Messina",
                   "Sanremo · 42,2 e 21,1 km", "Maratona di Valencia · 42,2 km"],
            note="Domenica 13: Salento Half Marathon a Collepasso.\nCalendario completo su cozzuscoach.it/calendario")
allenamenti = [  # 18:30
    ("Corsa facile 40’", "Se esci col buio:", ["luce davanti e dietro, colori chiari", "ritmo da conversazione", "10’ di mobilità a casa"], "30"),
    ("Facile + allunghi", "Prova quelli del reel di oggi:", ["35’ di corsa facile", "6 allunghi da 20 secondi", "recupero camminando, poi 5’ sciolti"], "57"),
    ("Forza 20’", "3 serie per esercizio:", ["12 squat", "10 affondi indietro per gamba", "15 sollevamenti sui talloni", "plank 30 secondi"], "38"),
    ("Ripetute 6 × 3’", "Dopo 15’ di riscaldamento:", ["6 × 3’ a ritmo 10 km", "recupero 2’ di corsa lenta", "10’ di defaticamento"], "29"),
    ("Vigilia di gara?", "Se domenica corri:", ["riposo, oppure 20’ facili", "3 allunghi sciolti", "a letto presto"], "25"),
    ("Collinare 50’", "Se domenica non gareggi:", ["percorso ondulato", "in salita stesso sforzo, non stesso ritmo", "discese morbide, passi corti"], "36"),
    ("Lungo facile", "Se oggi non hai gareggiato:", ["1h–1h20’ tutto a ritmo facile", "acqua se superi l’ora", "poi vestiti asciutti e mobilità"], "24"),
]
domani = [  # 21:00, anteprima del post del giorno dopo
    ("Cosa sono gli allunghi?", "Il reel di tecnica: 20 secondi per un passo più sciolto.", "26"),
    ("Le fratture da stress", "Ep. 7 degli infortuni del runner: quando l’osso chiede tregua.", "23"),
    ("Come sai se stai migliorando?", "Volumi, forma e tempi previsti: la sezione Andamento.", "17"),
    ("Gare del weekend", "Monopoli, Sanremo, Valencia: chi corre domenica?", "53"),
    ("Dicembre non deve essere perfetto", "Il reel del sabato per chi teme le feste.", "56"),
    ("La settimana in 5 consigli", "Il ripasso da salvare.", "28"),
    ("Si riparte domani", "Un consiglio al mattino, un post alle 13, l’allenamento alle 18:30. Attiva le notifiche.", "58"),
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
