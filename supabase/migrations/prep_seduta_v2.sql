-- Preparazione mentale alle sedute di qualità, versione 2
-- Più paure e più stati, risposte più motivanti. Eseguire dopo prep_seduta.sql. Idempotente.

-- 1. Colonne per tutte le scelte dell'atleta (fear/feel restano la prima scelta)
alter table session_prep add column if not exists fears text[];
alter table session_prep add column if not exists feels text[];

-- 2. Frasi aggiuntive per le paure secondarie
create table if not exists prep_rinforzi (
  fear text primary key,
  body text not null
);
alter table prep_rinforzi enable row level security;
drop policy if exists "prep_rinforzi_leggi" on prep_rinforzi;
create policy "prep_rinforzi_leggi" on prep_rinforzi for select to authenticated using (true);

insert into prep_rinforzi (fear, body) values
('ritmo',   'Il ritmo non è un giudizio su di te: è il punto da cui parti per crescere.'),
('finire',  'Ogni ripetuta chiusa è un mattone: non deve essere perfetta, deve arrivare in fondo.'),
('partenza','Chi gestisce il primo tratto è quello che finisce forte: parti con intelligenza.'),
('fatica',  'La fatica dei primi minuti è il corpo che si accende: lasciala salire, non ti ferma.'),
('gambe',   'Le gambe pesanti oggi sono solo rumore di fondo: concentrati sul ritmo del respiro.'),
('nervi',   'I nervi sono il segnale che ci tieni: usali come carburante, non come freno.')
on conflict (fear) do update set body = excluded.body;

-- 3. Libreria rinnovata (stessa chiave, testi nuovi)
insert into prep_replies (fear, session_kind, feel, body) values
-- ritmo
('ritmo','ripetute','teso','Il ritmo di oggi lo costruisci, non lo subisci. Parti sciolto, prendi confidenza con la prima ripetuta e poi mostra chi sei.'),
('ritmo','ripetute','stanco','Le gambe possono essere piene e tu puoi comunque essere lucido: tieni il ritmo quanto basta e metti la testa dove serve. È questa la differenza tra chi si allena e chi corre.'),
('ritmo','ripetute','carico','Hai la condizione giusta per tenere il ritmo. Entra nella prima ripetuta con autorità e lascia che il passo diventi tuo.'),
('ritmo','medio','teso','Il medio non si difende con la forza: si governa con la testa. Respira, guarda il passo solo ogni tanto e torna dentro il ritmo appena puoi.'),
('ritmo','medio','stanco','Oggi il ritmo sarà quello che il corpo regge, e va bene così: stai allenando la costanza. Tienila fino in fondo.'),
('ritmo','medio','carico','Il ritmo è alla tua portata: prendilo e tienilo con costanza. Non serve spingere di più nei primi minuti per fare la differenza.'),
('ritmo','lungo','teso','Il lungo chiede un passo che puoi sostenere, non uno che ti spaventa. Se senti tensione, scendi un poco e riprendi quando ti sciogli.'),
('ritmo','lungo','stanco','Stanchezza e lungo vanno insieme: è qui che si costruisce il fondo. Mantieni l’andatura scelta e il ritmo arriverà da solo.'),
('ritmo','lungo','carico','Buone sensazioni nel lungo: non regalare niente nella prima parte. Il ritmo si decide negli ultimi chilometri, e lì ci sei tu.'),
-- finire
('finire','ripetute','teso','Non devi chiudere ogni ripetuta alla perfezione: devi chiuderle con la testa. Pensa solo alla prossima, una alla volta.'),
('finire','ripetute','stanco','Se le ultime ripetute pesano, il corpo ti chiede di essere ascoltato, non di mollare. Completa con calma e con orgoglio.'),
('finire','ripetute','carico','Le hai già nelle gambe. Obiettivo: chiuderle tutte con la stessa qualità, dalla prima all’ultima.'),
('finire','medio','teso','Il blocco va finito anche se non è perfetto. Dividilo in pezzi piccoli e contali: ogni pezzo chiuso è una vittoria.'),
('finire','medio','stanco','Chiudi il blocco con regolarità. Se devi rallentare, rallenta, ma non fermarti: è questo il lavoro che ti fa crescere.'),
('finire','medio','carico','Hai la capacità di chiudere il blocco. Tieni la testa sul pezzo che stai facendo e fallo tuo.'),
('finire','lungo','teso','Il lungo non si decide nei primi chilometri. Accetta che finirà con più fatica del previsto: è proprio il punto in cui cresci.'),
('finire','lungo','stanco','Ogni chilometro in più è costruzione. Non guardare la fine: guarda il prossimo tratto e portalo a casa.'),
('finire','lungo','carico','Buone sensazioni: proteggi la parte finale del lungo, quella che separa chi si allena da chi si allena davvero.'),
-- partenza
('partenza','ripetute','teso','La prima ripetuta va presa più lenta di quanto ti sembri giusto: il corpo si scalda e le successive escono meglio. Pazienza, poi attacchi.'),
('partenza','ripetute','stanco','Oggi parti morbido: la prima ripetuta serve a sentire le gambe. Il lavoro vero è nella seconda metà della seduta.'),
('partenza','ripetute','carico','Parti regolare e lascia che il ritmo cresca. Chi dosa la prima parte è quello che finisce forte.'),
('partenza','medio','teso','I primi minuti del medio vanno presi con calma. Non cercare il ritmo a tutti i costi: si trova da solo, un passo alla volta.'),
('partenza','medio','stanco','Parti più piano di quanto vorresti: il medio si costruisce nel mezzo, non all’inizio. Ci arriverai con il controllo giusto.'),
('partenza','medio','carico','Non bruciare la carica nei primi minuti: entra nel ritmo gradualmente e tienila per la parte che conta.'),
('partenza','lungo','teso','Parti piano, più piano di quanto ti sembri necessario. Il lungo si decide negli ultimi chilometri, e lì farai la differenza.'),
('partenza','lungo','stanco','Il lungo inizia lento per scelta. Il primo tratto serve a scaldare corpo e testa: è la parte che ti prepara al resto.'),
('partenza','lungo','carico','Hai energia da vendere: è il momento di trattenerla. Parti con il passo del lungo e non oltre, il resto verrà.'),
-- fatica
('fatica','ripetute','teso','La fatica nelle prime ripetute è normale e non dice nulla sul resto della seduta. Respira forte e vai avanti: è il tuo lavoro.'),
('fatica','ripetute','stanco','Sentirsi stanchi subito è un segnale da ascoltare, non da combattere. Rallenta un po’ e riprendi con determinazione.'),
('fatica','ripetute','carico','Se senti fatica presto, il corpo si sta solo accendendo. Concentrati sul respiro e lascia che salga.'),
('fatica','medio','teso','La fatica iniziale del medio passa, lo sai. Conta i respiri e torna al ritmo: bastano pochi secondi.'),
('fatica','medio','stanco','Fatica precoce: non giudicare il primo tratto. Cerca un’andatura che puoi tenere e costruisci da lì.'),
('fatica','medio','carico','È normale sentire fatica presto nel medio. Stai dentro il lavoro, non sopra: è esattamente dove devi stare.'),
('fatica','lungo','teso','Sul lungo la fatica iniziale è una sensazione, non un limite. Scendi di passo, ritrova il respiro e lascia che il corpo si sciolga.'),
('fatica','lungo','stanco','Il lungo chiede pazienza: la fatica dei primi chilometri non è il risultato di oggi. Il risultato arriva alla fine.'),
('fatica','lungo','carico','Fatica presto e buone sensazioni insieme: resta nel passo, senza accelerare. Il lungo premia chi non si fa prendere dall’entusiasmo.'),
-- gambe
('gambe','ripetute','teso','Le gambe pesanti sono una sensazione che passa, sempre. Riduci il passo di qualche secondo e riprendi con decisione.'),
('gambe','ripetute','stanco','Gambe piene: oggi chiedi meno alla velocità e più alla costanza. È un lavoro di qualità anche così, e lo porti a casa.'),
('gambe','ripetute','carico','Se le gambe si appesantiscono a metà seduta, è normale. Accorcia la falcata, alza il ritmo del respiro e torna dentro.'),
('gambe','medio','teso','La pesantezza a metà del medio è comune e passa. Alleggerisci il passo, respira e riprendi con la stessa convinzione.'),
('gambe','medio','stanco','Gambe pesanti nel medio: controlla il passo e non forzare la falcata. Ti basta restare dentro il lavoro.'),
('gambe','medio','carico','Se senti le gambe pesanti, cambia ritmo per un minuto e poi torna. Non è un problema: è la prova che stai allenando.'),
('gambe','lungo','teso','Sul lungo le gambe pesanti nella parte centrale sono la norma. Mantieni il passo sostenibile e aspetta che il corpo si sciolga.'),
('gambe','lungo','stanco','Gambe pesanti sul lungo: rallenta senza fermarti. È proprio in queste sensazioni che si costruisce il fondo.'),
('gambe','lungo','carico','Gambe pesanti in un lungo con buone sensazioni: passano. Continua con l’andatura scelta e fidati del lavoro fatto.'),
-- nervi
('nervi','ripetute','teso','Il nervosismo è energia: usala. Oggi il compito è fare il lavoro in programma, non dimostrare niente a nessuno.'),
('nervi','ripetute','stanco','Sei teso e stanco insieme: va bene così. Concentrati sulla prima ripetuta e il resto verrà da solo.'),
('nervi','ripetute','carico','Sei carico: bene, incanalala in una ripetuta alla volta. È così che si diventa pericolosi.'),
('nervi','medio','teso','Teso prima del medio è normale, anche per i migliori. Respira lento prima di partire, poi lavora sul pezzo che hai davanti.'),
('nervi','medio','stanco','Stanco e teso: parti con calma, la tensione scende da sola nei primi minuti. Fidati di come ti sei preparato.'),
('nervi','medio','carico','La carica di oggi è un vantaggio. Usala per restare concentrato, non per correre più forte di quanto serve.'),
('nervi','lungo','teso','Sul lungo la tensione è comune. Scegli un ritmo che ti tranquillizza e mantienilo: la calma è la tua arma.'),
('nervi','lungo','stanco','Stanco e teso prima del lungo: parti piano e cerca la routine del passo. Il resto lo fa la costanza.'),
('nervi','lungo','carico','Hai voglia di partire: ottimo, ma il lungo premia chi resta costante. Vai con la testa, poi con le gambe.')
on conflict (fear, session_kind, feel) do update set body = excluded.body;

-- 4. Funzione v2: più paure e più stati. Primo elemento = scelta principale.
drop function if exists prep_seduta(date, text, text, text, text);

create or replace function prep_seduta(p_day date, p_kind text, p_fears text[], p_feels text[], p_note text)
returns json
language plpgsql
security definer
set search_path = public
as $$
declare
  v_athlete uuid := auth.uid();
  v_coach uuid;
  v_body text;
  v_extra text;
  v_flag boolean;
begin
  if v_athlete is null then
    raise exception 'non autenticato';
  end if;
  if coalesce(array_length(p_fears, 1), 0) = 0 or coalesce(array_length(p_feels, 1), 0) = 0 then
    raise exception 'scegli almeno una paura e uno stato';
  end if;

  if exists (select 1 from session_prep where athlete_id = v_athlete and day = p_day) then
    return json_build_object('status', 'exists');
  end if;

  select id into v_coach from profiles where role = 'coach' limit 1;
  if v_coach is null then
    raise exception 'coach non trovato';
  end if;

  v_flag := p_note is not null and p_note ~* 'suicid|autolesion|farmi del male|ammazz|vomit|abbuff|digiun|non mangio|depress';

  if v_flag then
    insert into session_prep (athlete_id, day, fear, feel, fears, feels, note, flagged)
    values (v_athlete, p_day, p_fears[1], p_feels[1], p_fears, p_feels, p_note, true);
    return json_build_object('status', 'flagged');
  end if;

  -- risposta principale: prima paura + primo stato
  select body into v_body from prep_replies
   where fear = p_fears[1] and session_kind = p_kind and feel = p_feels[1];
  if v_body is null then
    raise exception 'risposta non trovata in libreria';
  end if;

  -- frasi di rinforzo per le paure successive alla prima
  select string_agg(r.body, ' ' order by u.ord) into v_extra
    from unnest(p_fears) with ordinality as u(f, ord)
    join prep_rinforzi r on r.fear = u.f
   where u.ord > 1;
  if v_extra is not null then
    v_body := v_body || ' ' || v_extra;
  end if;

  insert into session_messages (athlete_id, day, author_id, body)
  values (v_athlete, p_day, v_coach, v_body);

  insert into session_prep (athlete_id, day, fear, feel, fears, feels, note, reply_body)
  values (v_athlete, p_day, p_fears[1], p_feels[1], p_fears, p_feels, p_note, v_body);

  return json_build_object('status', 'sent', 'body', v_body, 'coach_id', v_coach);
end;
$$;

revoke all on function prep_seduta(date, text, text[], text[], text) from public;
grant execute on function prep_seduta(date, text, text[], text[], text) to authenticated;
