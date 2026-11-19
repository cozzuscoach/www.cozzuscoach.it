"""Settimana 23-29 novembre 2026 (7 post + 28 storie)."""
from comune import *

# ------------------------------------------------------------------ POST DELLE 13:00
carosello("2026-11-23-respiro", "2026-11-23T13:00", [
    dict(kind="cover", label="Consiglio", title="Respirare quando corri: 5 consigli", sub="Meno affanno, più controllo", photo="39", tsize=112),
    dict(kind="point", n=1, title="Naso e bocca insieme", body="Quando corri ti serve tanta aria: respirare anche con la bocca è normale. Non forzarti a usare solo il naso.", photo="28", foot="1/5"),
    dict(kind="point", n=2, title="Respira con la pancia", body="Prova da sdraiato, una mano sulla pancia: quando inspiri deve alzarsi lei, non le spalle. Poi porta lo stesso respiro nella corsa.", photo="24", foot="2/5"),
    dict(kind="point", n=3, title="Il respiro ti dice il ritmo", body="Nella corsa facile riesci a parlare in frasi intere. Se riesci a dire solo poche parole, stai andando più forte di quanto pensi.", photo="35", foot="3/5"),
    dict(kind="point", n=4, title="Trova una cadenza", body="Nel facile molti si trovano bene inspirando per 3 passi ed espirando per 2. Non è una regola: è un modo per restare calmi.", photo="30", foot="4/5"),
    dict(kind="point", n=5, title="Col freddo, uno scaldacollo", body="Tenuto davanti alla bocca nei primi minuti, riscalda un po’ l’aria che respiri e rende l’avvio più piacevole.", photo="51", foot="5/5"),
    dict(kind="cta", title="Respiro calmo, passo regolare", body="Un programma costruito sui tuoi dati, rivisto e seguito dal coach.", photo="33",
         note="Indicazioni di orientamento: se l’affanno è insolito o hai asma, chiedi al tuo medico."),
], "Respirare quando corri: 5 consigli 🌬️🏃\n\n"
   "1️⃣ Naso e bocca insieme: è normale\n"
   "2️⃣ Respira con la pancia, non con le spalle\n"
   "3️⃣ Il respiro ti dice il ritmo: nel facile parli in frasi intere\n"
   "4️⃣ Trova una cadenza, per esempio 3 passi inspiri e 2 espiri\n"
   "5️⃣ Col freddo, uno scaldacollo davanti alla bocca nei primi minuti\n\n"
   "Tu come respiri quando corri? Scrivilo nei commenti 👇\n\n"
   "Indicazioni di orientamento: se l’affanno è insolito o hai asma, chiedi al tuo medico." + CTA + "\n\n" + HT + " #respirazione #corsafacile")

video("2026-11-24-postura", "2026-11-24T13:00", [
    dict(clip=clip(2), start=0.5, dur=3.0, vertical=True, text=dict(label="Tecnica", title="Quando sei stanco ti curvi?", tsize=104, pos="top")),
    dict(clip=clip(3), start=3.0, dur=3.4, fx=.42, text=dict(title="Corri alto", sub="Come se un filo ti tirasse su dalla testa.", tsize=110, pos="top")),
    dict(clip=clip(7), start=2.0, dur=3.2, vertical=True, text=dict(title="Sguardo avanti, non sui piedi", tsize=100, pos="top")),
    dict(clip=clip(1), start=6.0, dur=3.2, fx=.45, text=dict(title="Spalle basse, petto aperto", tsize=104, pos="top")),
    dict(clip=clip(10), start=10.0, dur=3.4, fx=.5, text=dict(title="Bacino alto, non “seduto”", sub="Il piede atterra più vicino al corpo.", tsize=100, pos="top")),
    dict(clip=clip(0), start=8.0, dur=3.6, fx=.45, text=dict(title="Corri alto, corri leggero", cta=True, pos="mid", dim=True, tsize=104)),
], "Corri alto 📏🏃\n\n"
   "Negli ultimi chilometri la postura è la prima cosa che se ne va: spalle che salgono, sguardo a terra, bacino che “si siede”. Tre controlli da fare ogni tanto mentre corri:\n\n"
   "👀 sguardo una quindicina di metri avanti\n"
   "🙆 spalle basse e petto aperto\n"
   "⬆️ bacino alto, come se un filo ti tirasse su dalla testa\n\n"
   "Un trucco: scegli un segnale (un lampione, un incrocio) e ogni volta che lo vedi fai il controllo." + CTA + "\n\n" + HT + " #tecnicadicorsa #postura",
    bpm=100, seed=10)

carosello("2026-11-25-polpaccio", "2026-11-25T13:00", [
    dict(kind="cover", label="Infortuni del runner · Ep. 6", title="Lo stiramento del polpaccio", sub="La fitta improvvisa dietro la gamba", photo="18", tsize=118),
    dict(kind="point", title="Come si presenta", body="Una fitta improvvisa nella parte posteriore della gamba, tra ginocchio e tallone, spesso in accelerazione o in salita. A volte invece è un indurimento che cresce chilometro dopo chilometro.", photo="60"),
    dict(kind="point", title="Perché succede", body="Polpacci stanchi o poco allenati alla forza, aumenti bruschi di velocità o di salite, poco recupero tra un lavoro e l’altro, un cambio veloce verso scarpe più basse. Con gli anni il rischio cresce.", photo="14"),
    dict(kind="point", title="Cosa fare", body="Fermati subito: non finire l’uscita “per arrivare a casa di corsa”. Nei giorni dopo cammina se non fa male. Riprendi a correre piano quando cammini e sali sulle punte senza dolore.", photo="10"),
    dict(kind="point", title="Rinforza i polpacci", body="Sollevamenti sui talloni a gamba tesa e a ginocchio piegato, 3 serie da 15, scendendo lentamente. Due o tre volte a settimana, anche quando stai bene.", photo="19"),
    dict(kind="point", title="Quando farti vedere", body="Dolore forte, livido, gonfiore, difficoltà a camminare o a salire sulle punte. E un polpaccio gonfio, caldo e dolente senza un trauma va sempre visto da un medico.", photo="23"),
    dict(kind="cta", title="Polpacci forti, carico che cresce con calma", body="Un programma costruito sui tuoi dati, rivisto e seguito dal coach.", photo="34", tsize=92,
         note="Indicazioni di orientamento: non sostituiscono il parere di un professionista."),
], "Infortuni del runner · Ep. 6 — Lo stiramento del polpaccio 🦵\n\n"
   "Una fitta improvvisa dietro la gamba mentre acceleri o sei in salita? Nelle slide:\n"
   "📍 come si presenta\n❓ perché succede\n✅ cosa fare (e cosa non fare)\n🏋️ come rinforzare i polpacci\n🚩 quando farti vedere\n\n"
   "Salvalo e giralo a chi “tanto è solo un crampo”." + ORIENT + CTA + "\n\n" + HT + " #infortuni #polpaccio #prevenzione")

video("2026-11-26-ritmi", "2026-11-26T13:00", [
    dict(clip=clip(1), start=9.0, dur=3.0, fx=.45, text=dict(label="Come funziona", title="Corri sempre allo stesso ritmo?", tsize=100, pos="top")),
    dict(clip=clip(3), start=7.0, dur=3.4, fx=.42, text=dict(title="Ogni seduta ha il suo ritmo", sub="Facile, medio, soglia, ripetute.", tsize=104, pos="top")),
    dict(clip=clip(2), start=10.0, dur=3.4, vertical=True, text=dict(title="Si ricavano da un tuo tempo recente", sub="Una 5 km, una 10 km, una mezza.", tsize=96, pos="top")),
    dict(clip=clip(7), start=5.0, dur=3.4, vertical=True, text=dict(title="Nel diario vedi le ripetute accanto al ritmo previsto", tsize=88, pos="top")),
    dict(clip=clip(10), start=13.0, dur=3.4, fx=.5, text=dict(title="Provalo su cozzuscoach.it/strumenti", tsize=96, pos="top")),
    dict(clip=clip(0), start=15.0, dur=3.6, fx=.45, text=dict(title="Il facile facile, il veloce veloce", cta=True, pos="mid", dim=True, tsize=100)),
], "Un ritmo per ogni seduta ⏱️🏃\n\n"
   "Correre sempre allo stesso ritmo “medio” stanca, ma fa migliorare poco. In un programma ogni seduta ha uno scopo e un ritmo:\n\n"
   "🐢 facile, per costruire la base\n"
   "🚶‍♂️➡️🏃 medio e soglia, per tenere un ritmo più a lungo\n"
   "⚡ ripetute, per alzare il motore\n\n"
   "Con Cozzu’s Coach i ritmi si ricavano da un tuo tempo recente con il metodo VDOT di Jack Daniels, e nel diario vedi ogni ripetuta accanto al ritmo previsto. "
   "Vuoi provare? Il calcolatore è su cozzuscoach.it/strumenti" + CTA + "\n\n" + HT + " #pianodiallenamento #coachdicorsa #ritmo",
    bpm=96, seed=11)

carosello("2026-11-27-gare", "2026-11-27T13:00", [
    dict(kind="cover", label="Gare del weekend", title="Domenica 29 novembre", sub="In Puglia, al Sud e le grandi maratone d’autunno", photo="44", tsize=120),
    dict(kind="point", title="CorriaMola... Insieme", body="Mola di Bari (BA) · 10 km\nLa gara su strada in Puglia in calendario questa domenica.", photo="45"),
    dict(kind="point", title="Al Sud", body="Half Marathon Mazara · Mazara del Vallo (TP) · 21,1 km\nTrofeo Santa Barbara · Paternò (CT) · 10 km\nFiumicino Half Marathon · Fiumicino (RM)", photo="46"),
    dict(kind="point", title="Nel resto d’Italia", body="Firenze Marathon · 42,2 e 10 km\nTorino City Marathon · 42,2 e 21,1 km\nMezza di Palmanova (UD) · 21,1 km\nIl calendario completo è su cozzuscoach.it/calendario", photo="43"),
    dict(kind="cta", title="Buona gara a chi corre domenica", body="Prossimo obiettivo? Costruiamo insieme la preparazione, settimana dopo settimana.", photo="57", tsize=98),
], "Gare del weekend: domenica 29 novembre 🏁\n\n"
   "📍 CorriaMola... Insieme · Mola di Bari (BA) · 10 km\n"
   "📍 Half Marathon Mazara · Mazara del Vallo (TP) · 21,1 km\n"
   "📍 Trofeo Santa Barbara · Paternò (CT) · 10 km\n"
   "📍 Fiumicino Half Marathon · Fiumicino (RM)\n"
   "✈️ Nel resto d’Italia: Firenze Marathon (maratona e 10 km), Torino City Marathon (maratona e mezza), Mezza Maratona Città di Palmanova\n\n"
   "Controlla sempre orari e iscrizioni sui siti degli organizzatori. Calendario completo su cozzuscoach.it/calendario\n\n"
   "Chi corre? Scrivi la tua gara nei commenti e tagga chi viene con te 👇" + CTA + "\n\n" + HT + " #moladibari #firenzemarathon #torinocitymarathon #10km #mezzamaratona #maratona")

video("2026-11-28-primavera", "2026-11-28T13:00", [
    dict(clip=clip(0), start=12.0, dur=3.0, fx=.4, text=dict(title="Novembre: giornate corte, nessuna gara vicina", tsize=96, pos="top")),
    dict(clip=clip(2), start=4.0, dur=3.0, vertical=True, text=dict(title="Sembra un mese “di mezzo”", tsize=106, pos="top")),
    dict(clip=clip(3), start=10.0, dur=3.2, fx=.45, text=dict(title="È il mese in cui si costruisce", tsize=106, pos="top")),
    dict(clip=clip(7), start=0.0, dur=3.2, vertical=True, text=dict(title="Le gare di primavera si preparano adesso", tsize=100, pos="top")),
    dict(clip=clip(1), start=14.0, dur=3.0, fx=.45, text=dict(title="Buona gara a chi corre domani 💪", tsize=104, pos="top")),
    dict(clip=clip(10), start=1.0, dur=3.6, fx=.5, text=dict(title="Inizia oggi la tua primavera", cta=True, pos="mid", dim=True, tsize=104)),
], "Le gare di primavera si preparano a novembre 🌱🏃\n\n"
   "Giornate corte, freddo, nessun pettorale in vista: sembra un mese di passaggio. In realtà è proprio adesso che si costruisce la base per la mezza o la maratona di marzo e aprile: tanta corsa facile, un po’ di forza, costanza.\n\n"
   "Qual è il tuo obiettivo per la primavera? Scrivilo nei commenti 👇\n\n"
   "E buona gara a chi corre domani a Mola di Bari, Firenze e Torino 💙" + CTA + "\n\n" + HT + " #motivazione #costanza #obiettivi",
    bpm=104, seed=12)

carosello("2026-11-29-settimana", "2026-11-29T13:00", [
    dict(kind="cover", label="Da salvare", title="La settimana in 5 consigli", sub="Il ripasso di tutto quello che abbiamo visto", photo="32"),
    dict(kind="point", n=1, title="Respira con la pancia", body="Naso e bocca insieme, spalle ferme. Nel facile riesci a parlare in frasi intere.", photo="24", foot="1/5"),
    dict(kind="point", n=2, title="Corri alto", body="Sguardo avanti, spalle basse, bacino alto. Fai il controllo ogni volta che vedi un lampione.", photo="57", foot="2/5"),
    dict(kind="point", n=3, title="Fitta al polpaccio? Fermati", body="Non finire l’uscita. Riprendi quando cammini e sali sulle punte senza dolore. E rinforza i polpacci.", photo="18", foot="3/5"),
    dict(kind="point", n=4, title="Un ritmo per ogni seduta", body="Il facile facile, il veloce veloce. I ritmi si ricavano da un tuo tempo recente.", photo="16", foot="4/5"),
    dict(kind="point", n=5, title="Novembre costruisce", body="Le gare di primavera si preparano adesso, con tanta corsa facile e costanza.", photo="36", foot="5/5"),
    dict(kind="cta", title="Una nuova settimana inizia domani", body="Corri con un programma costruito sui tuoi dati, rivisto e seguito dal coach.", photo="13"),
], "La settimana in 5 consigli 📌\n\n"
   "🌬️ Respiro: con la pancia, naso e bocca insieme\n"
   "📏 Postura: corri alto\n"
   "🦵 Polpaccio: alla prima fitta ci si ferma\n"
   "⏱️ Ritmi: ogni seduta ha il suo\n"
   "🌱 Novembre: la primavera si prepara adesso\n\n"
   "Hai corso oggi? Raccontaci com’è andata nei commenti 👇" + CTA + "\n\n" + HT)

# ------------------------------------------------------------------ STORIE
giorni = ["2026-11-23", "2026-11-24", "2026-11-25", "2026-11-26", "2026-11-27", "2026-11-28", "2026-11-29"]

consigli = [  # 07:00
    ("Prepara tutto la sera prima", "Scarpe, vestiti e orologio carico pronti accanto alla porta: al mattino esci senza pensarci.", "25"),
    ("Guarda l’orizzonte", "Lo sguardo una quindicina di metri avanti tiene dritti collo e schiena, e il respiro più libero.", "30"),
    ("Polpacci stanchi? Ascoltali", "Dopo ripetute o salite, il giorno dopo corri facile. Una fitta improvvisa è il segnale per fermarsi.", "01"),
    ("Il facile deve essere facile", "Correre tutto a ritmo medio stanca e fa migliorare poco. Facile quando è facile, veloce quando è veloce.", "26"),
    ("Guarda il meteo della gara", "Vento, pioggia e temperatura: decidi la sera prima cosa indossare e tieni una maglia vecchia per l’attesa in griglia.", "42"),
    ("Corri in compagnia", "Un appuntamento con un amico rende molto più difficile restare a letto.", "34"),
    ("Il riposo fa parte del piano", "Uno o due giorni senza corsa a settimana non sono tempo perso: è lì che il corpo si adatta.", "58"),
]
fatti = [  # 15:30 (venerdì: gare del weekend)
    dict(big="12–20", title="respiri al minuto", body="È la frequenza respiratoria normale di un adulto a riposo. Durante uno sforzo intenso può superare i 40.", photo="39", bigsize=190),
    dict(big="3 ori", title="Emil Zátopek", body="Helsinki 1952: il ceco vince 5000, 10000 e maratona nella stessa Olimpiade. Era la prima maratona della sua vita.", photo="41", bigsize=190),
    dict(big="3 capi", title="il tricipite della sura", body="I due gemelli e il soleo formano il polpaccio e si uniscono in basso nel tendine d’Achille.", photo="19", bigsize=190),
    dict(big="80/20", title="il modello polarizzato", body="Gli studi di Stephen Seiler mostrano che molti atleti di resistenza d’élite fanno circa l’80% dell’allenamento a bassa intensità.", photo="35", bigsize=200),
    None,
    dict(big="2 ori", title="maratona olimpica", body="Gli italiani che l’hanno vinta: Gelindo Bordin a Seul 1988 e Stefano Baldini ad Atene 2004.", photo="57", bigsize=200),
    dict(big="1967", title="Kathrine Switzer", body="Corre la maratona di Boston con un pettorale ufficiale, quando le donne non erano ammesse. Dal 1972 la gara si apre ufficialmente alle donne.", photo="49", bigsize=210),
]
gare = dict(kind="story", label="Gare del weekend", title="Domenica 29 novembre", body="In Puglia e non solo:", tsize=104, photo="53",
            items=["CorriaMola... Insieme · Mola di Bari (BA) · 10 km", "Half Marathon Mazara · Mazara del Vallo (TP)",
                   "Firenze Marathon · 42,2 e 10 km", "Torino City Marathon · 42,2 e 21,1 km"],
            note="Calendario completo su cozzuscoach.it/calendario")
allenamenti = [  # 18:30
    ("Corsa facile 40’", "Ascoltando il respiro:", ["ritmo da conversazione", "prova a inspirare per 3 passi ed espirare per 2", "4 allunghi finali da 20 secondi"], "32"),
    ("Corsa facile + postura", "45’ tranquilli, e ogni 5 minuti:", ["sguardo avanti", "spalle basse", "bacino alto", "poi 6 allunghi da 80 m"], "10"),
    ("Forza per i polpacci 15’", "3 serie per esercizio:", ["15 sollevamenti sui talloni a gamba tesa", "15 a ginocchio piegato", "20 saltelli leggeri sul posto"], "06"),
    ("Soglia 3 × 8’", "Dopo 15’ di riscaldamento:", ["3 × 8’ a ritmo soglia", "recupero 2’ di corsa lenta", "10’ di defaticamento"], "29"),
    ("Allenamento alternativo", "Se domenica non corri gare:", ["40’ di bici o cyclette facile", "oppure 45’ di camminata svelta", "10’ di mobilità"], "38"),
    ("Lungo con finale", "Se domenica non corri gare:", ["1h–1h20’ a ritmo facile", "ultimi 10’ a ritmo medio", "acqua se superi l’ora"], "22"),
    ("Recupero 30’", "Dopo la gara o il lungo:", ["30’ molto facili oppure una camminata", "10’ di mobilità", "a tavola, carboidrati e proteine"], "47"),
]
domani = [  # 21:00, anteprima del post del giorno dopo
    ("Quando sei stanco ti curvi?", "Il reel di tecnica: tre controlli per correre alto e leggero.", "61"),
    ("Lo stiramento del polpaccio", "Ep. 6 degli infortuni del runner: la fitta improvvisa dietro la gamba.", "21"),
    ("Un ritmo per ogni seduta", "Come si ricavano i tuoi ritmi da un tempo recente.", "26"),
    ("Gare del weekend", "Mola di Bari, Firenze, Torino: chi corre domenica?", "54"),
    ("Le gare di primavera", "Un reel per le uscite di novembre: è adesso che si costruisce.", "56"),
    ("La settimana in 5 consigli", "Il ripasso da salvare.", "52"),
    ("Una nuova settimana", "Nuovi consigli ogni giorno. Attiva le notifiche per non perderli.", "33"),
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
