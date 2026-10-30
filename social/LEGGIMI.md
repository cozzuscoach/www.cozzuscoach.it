# Social di Cozzu's Coach

Questa cartella è gestita dalla chat "social cozzus coach" (progetto claude.ai). Il resto del sito non si tocca da qui.

## Come funziona
- **Calendario:** `calendario.json` contiene tutte le uscite. Il workflow `.github/workflows/pubblica.yml` gira ogni mezz'ora (minuti 2 e 32) e pubblica su Instagram (e sulla Pagina Facebook, tranne le storie) le voci `programmato` con orario passato. Lo script è `scripts/pubblica_ig.py`.
- **Media:** stanno in `media/` e sono serviti da `https://cozzuscoach.it/social/media/<file>`. Le immagini sono JPEG, i video MP4.
- **Libreria:** `libreria/foto/NN.jpg` (62 foto Pexels) e `libreria/video/NN.mp4` (12 clip Pexels). Le fonti sono in `fonti-*.txt`.
- **Grafiche:** `strumenti/render.py`, con le storie a 1080×1920 e i caroselli a 1080×1350. I reel si fanno con `strumenti/reel.py`, con musica sintetizzata originale. Le funzioni comuni sono in `strumenti/comune.py`.
- **Font:** Barlow e Barlow Condensed in `risorse/fonts`, con licenza OFL.

## Piano fisso: 5 uscite al giorno
| Ora | Uscita | Contenuto |
|---|---|---|
| 07:00 | storia | consiglio del giorno |
| 13:00 | post (IG + FB) | lun carosello consiglio · mar reel tecnica · mer carosello infortuni del runner (serie a episodi) · gio reel metodo/servizio · ven carosello gare del weekend o pre-gara · sab reel motivazione · dom carosello (risultati del team se ci sono, altrimenti ripasso della settimana) |
| 15:30 | storia | lo sapevi? (dati veri e verificabili) |
| 18:30 | storia | allenamento di oggi (esempio, "adattalo al tuo livello") |
| 21:00 | storia | domani alle 13 (anteprima del post del giorno dopo) |

## Produzione settimanale (giovedì)
1. Si legge `calendario.json` per non ripetere i temi già usati: la serie degli infortuni continua con l'episodio successivo.
2. Si scrive `strumenti/settimana_AAAA-MM-GG.py` sul modello di `esempio_settimana.py`, per la settimana da lunedì a domenica, e lo si esegue con `COZZUS_TMP=/tmp/cozzus python3 social/strumenti/settimana_....py`.
3. Si controllano le grafiche con un foglio di miniature, e si sistemano foto tagliate male o testi troppo lunghi.
4. `python3 social/strumenti/calendario.py aggiungi /tmp/cozzus/settimana.json`, poi `approva AAAA-MM-GG AAAA-MM-GG` per i giorni della settimana. I contenuti con atleti veri restano in `bozza` fino all'ok di Biagio.
5. `python3 social/strumenti/calendario.py pulisci 10` toglie i media già pubblicati.
6. Commit e push su `main`, poi si pubblica l'anteprima della settimana come artifact e si manda il riepilogo a Biagio.

## Regole sui contenuti
- Niente prezzi, pagamenti, abbonamenti o offerte. L'invito è sempre "Richiedi il tuo programma" (sito o DM).
- Il servizio si descrive come "costruito sui tuoi dati, rivisto e seguito dal coach". Mai scrivere che ogni seduta è scritta a mano. Mai nominare l'intelligenza artificiale.
- Nessuna promessa di risultati e nessuna affermazione medica. Infortuni e alimentazione portano la nota "indicazioni di orientamento".
- Atleti veri solo con il loro consenso. Le persone delle foto stock non sono mai atleti del team.
- Sempre foto o video di persone che corrono, mai solo grafiche. Lo stile è sportivo, pulito e mediterraneo.
- Colori: #0A5C73, #0D7A96, #073F50, #DDF0F4, #F2A93B, #15222A, #5B6B73, #EEF3F4.
