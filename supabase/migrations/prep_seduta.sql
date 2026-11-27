-- Preparazione mentale alle sedute di qualità
-- Eseguire nell'SQL editor di Supabase. Idempotente.

-- 1. Libreria delle risposte pronte (scritte dal coach)
create table if not exists prep_replies (
  fear text not null,          -- ritmo | finire | partenza | fatica | gambe | nervi
  session_kind text not null,  -- ripetute | medio | lungo
  feel text not null,          -- teso | stanco | carico
  body text not null,
  primary key (fear, session_kind, feel)
);

-- 2. Preparazioni inviate dagli atleti
create table if not exists session_prep (
  id bigserial primary key,
  athlete_id uuid not null references profiles(id) on delete cascade,
  day date not null,
  fear text not null,
  feel text not null,
  note text,
  reply_body text,
  flagged boolean not null default false,
  created_at timestamptz not null default now(),
  unique (athlete_id, day)
);

alter table prep_replies enable row level security;
alter table session_prep enable row level security;

drop policy if exists "prep_replies_leggi" on prep_replies;
create policy "prep_replies_leggi" on prep_replies for select to authenticated using (true);

drop policy if exists "prep_leggi_propria" on session_prep;
create policy "prep_leggi_propria" on session_prep for select to authenticated using (athlete_id = auth.uid());

drop policy if exists "prep_leggi_coach" on session_prep;
create policy "prep_leggi_coach" on session_prep for select to authenticated
  using (exists (select 1 from profiles p where p.id = auth.uid() and p.role = 'coach'));

-- 3. Funzione chiamata dall'atleta: salva la preparazione e invia la risposta pronta
create or replace function prep_seduta(p_day date, p_kind text, p_fear text, p_feel text, p_note text)
returns json
language plpgsql
security definer
set search_path = public
as $$
declare
  v_athlete uuid := auth.uid();
  v_coach uuid;
  v_body text;
  v_flag boolean;
begin
  if v_athlete is null then
    raise exception 'non autenticato';
  end if;

  if exists (select 1 from session_prep where athlete_id = v_athlete and day = p_day) then
    return json_build_object('status', 'exists');
  end if;

  select id into v_coach from profiles where role = 'coach' limit 1;
  if v_coach is null then
    raise exception 'coach non trovato';
  end if;

  -- segnali di disagio: nessuna risposta automatica, il coach legge
  v_flag := p_note is not null and p_note ~* 'suicid|autolesion|farmi del male|ammazz|vomit|abbuff|digiun|non mangio|depress';

  if v_flag then
    insert into session_prep (athlete_id, day, fear, feel, note, flagged)
    values (v_athlete, p_day, p_fear, p_feel, p_note, true);
    return json_build_object('status', 'flagged');
  end if;

  select body into v_body from prep_replies
   where fear = p_fear and session_kind = p_kind and feel = p_feel;
  if v_body is null then
    raise exception 'risposta non trovata in libreria';
  end if;

  insert into session_messages (athlete_id, day, author_id, body)
  values (v_athlete, p_day, v_coach, v_body);

  insert into session_prep (athlete_id, day, fear, feel, note, reply_body)
  values (v_athlete, p_day, p_fear, p_feel, p_note, v_body);

  return json_build_object('status', 'sent', 'body', v_body, 'coach_id', v_coach);
end;
$$;

revoke all on function prep_seduta(date, text, text, text, text) from public;
grant execute on function prep_seduta(date, text, text, text, text) to authenticated;

-- 4. Libreria: 6 paure x 3 tipi di seduta x 3 stati (54 risposte)
insert into prep_replies (fear, session_kind, feel, body) values
-- ritmo
('ritmo','ripetute','teso','Il passo di oggi è una guida, non un voto. Parti sciolto nelle prime ripetute e prendi il ritmo strada facendo.'),
('ritmo','ripetute','stanco','Se oggi le gambe sono piene, il ritmo può scendere un po'': va bene. Finisci le ripetute con la testa, non con il cronometro.'),
('ritmo','ripetute','carico','Hai la condizione per tenere il ritmo. Entra nella prima ripetuta con calma e lascia che il passo si stabilizzi.'),
('ritmo','medio','teso','Il tempo del medio non va difeso con la forza. Respira, guarda il passo solo ogni tanto e torna al ritmo appena puoi.'),
('ritmo','medio','stanco','Oggi il ritmo sarà quello che il corpo regge. Non rincorrere il numero: tieni un''andatura controllata fino in fondo.'),
('ritmo','medio','carico','Il ritmo è alla tua portata. Tienilo con costanza, senza spingere di più nei primi minuti.'),
('ritmo','lungo','teso','Sul lungo il ritmo conta meno del passo sostenibile. Se ti senti teso, scendi di qualche secondo e riprendi quando ti sciogli.'),
('ritmo','lungo','stanco','Stanchezza e lungo vanno insieme. Mantieni l''andatura facile che hai programmato: il ritmo arriva da solo.'),
('ritmo','lungo','carico','Lungo con buone sensazioni: non regalare nulla nella prima parte. Il ritmo si costruisce nella parte finale.'),
-- finire
('finire','ripetute','teso','Non devi chiudere ogni ripetuta alla perfezione. Pensa solo alla prossima, una alla volta.'),
('finire','ripetute','stanco','Se le ultime ripetute pesano, è normale. Fermati solo se il corpo lo chiede davvero, altrimenti completa con calma.'),
('finire','ripetute','carico','Le hai già nelle gambe. Obiettivo: chiuderle tutte con la stessa qualità, non il massimo alla prima.'),
('finire','medio','teso','Il blocco va finito anche se non è perfetto. Dividilo in pezzi di un minuto e conta quelli.'),
('finire','medio','stanco','Chiudi il blocco con regolarità. Se devi rallentare, rallenta ma non fermarti.'),
('finire','medio','carico','Hai la capacità di chiudere il blocco. Tieni la testa sul pezzo che stai facendo.'),
('finire','lungo','teso','Il lungo non si decide nei primi chilometri. Accetta che finirà con più fatica del previsto: va bene.'),
('finire','lungo','stanco','Ogni chilometro in più è costruzione. Non guardare la fine, guarda il prossimo tratto.'),
('finire','lungo','carico','Buone sensazioni: proteggi la parte finale del lungo, quella che conta per la costanza.'),
-- partenza
('partenza','ripetute','teso','La prima ripetuta va presa più lenta di quanto ti sembra giusto: il corpo si scalda e le successive escono meglio.'),
('partenza','ripetute','stanco','Oggi parti morbido: la prima ripetuta serve a sentire le gambe, non a dimostrare nulla.'),
('partenza','ripetute','carico','Parti regolare e lascia che il ritmo cresca nella seconda parte della seduta.'),
('partenza','medio','teso','I primi minuti del medio vanno presi con calma. Non cercare il ritmo a tutti i costi all''inizio.'),
('partenza','medio','stanco','Parti più piano di quanto vorresti. Il medio si costruisce nel mezzo, non all''inizio.'),
('partenza','medio','carico','Non bruciare la carica nei primi minuti: entra nel ritmo gradualmente.'),
('partenza','lungo','teso','Parti piano, più piano di quanto ti sembri necessario. Il lungo si decide negli ultimi chilometri.'),
('partenza','lungo','stanco','Il lungo inizia lento per scelta. Il primo tratto è il riscaldamento di corpo e testa.'),
('partenza','lungo','carico','Hai energia: è proprio il momento di trattenerla. Parti con il passo del lungo, non oltre.'),
-- fatica
('fatica','ripetute','teso','La fatica nelle prime ripetute è normale e non dice nulla sul resto della seduta. Respira e vai avanti.'),
('fatica','ripetute','stanco','Sentirsi stanchi subito è un segnale da ascoltare, non da combattere. Rallenta un po'' e riprendi.'),
('fatica','ripetute','carico','Se senti fatica presto, il corpo si sta solo attivando. Concentrati sulla respirazione.'),
('fatica','medio','teso','La fatica iniziale del medio passa. Conta i respiri e torna al ritmo.'),
('fatica','medio','stanco','Fatica precoce: non giudicare il primo tratto. Cerca un''andatura che puoi tenere.'),
('fatica','medio','carico','È normale sentire fatica presto nel medio. Stai dentro il lavoro, non sopra.'),
('fatica','lungo','teso','Sul lungo la fatica iniziale è una sensazione, non un limite. Scendi di passo e ritrova il respiro.'),
('fatica','lungo','stanco','Il lungo chiede pazienza: la fatica dei primi chilometri non è il risultato di oggi.'),
('fatica','lungo','carico','Fatica presto e buone sensazioni insieme: resta nel passo, senza accelerare.'),
-- gambe
('gambe','ripetute','teso','Gambe pesanti sono una sensazione che passa. Riduci il passo di qualche secondo e riprendi.'),
('gambe','ripetute','stanco','Gambe piene: oggi chiedi meno alla velocità e più alla costanza. Va bene così.'),
('gambe','ripetute','carico','Se le gambe sono pesanti a metà seduta, è normale. Accorcia la falcata e torna al ritmo.'),
('gambe','medio','teso','Pesantezza a metà medio è comune. Alleggerisci il passo, respira e poi riprendi.'),
('gambe','medio','stanco','Gambe pesanti nel medio: tieni il passo sotto controllo e non forzare la falcata.'),
('gambe','medio','carico','Se senti le gambe pesanti, cambia ritmo per un minuto e poi torna. Nessun dramma.'),
('gambe','lungo','teso','Sul lungo le gambe pesanti nella parte centrale sono la norma. Mantieni il passo sostenibile.'),
('gambe','lungo','stanco','Gambe pesanti sul lungo: rallenta senza fermarti e lascia che il corpo si sciolga.'),
('gambe','lungo','carico','Gambe pesanti in un lungo con buone sensazioni: passano. Continua con l''andatura scelta.'),
-- nervi
('nervi','ripetute','teso','Il nervosismo è energia. Oggi il compito è fare il lavoro in programma, non dimostrare nulla.'),
('nervi','ripetute','stanco','Sei teso e stanco: va bene così. Concentrati sulla prima ripetuta e il resto viene.'),
('nervi','ripetute','carico','Sei carico: canalizza la tensione in una ripetuta alla volta.'),
('nervi','medio','teso','Teso prima del medio è normale. Respira lento prima di partire, poi lavora sul pezzo che hai davanti.'),
('nervi','medio','stanco','Stanco e teso: parti con calma, la tensione scende da sola nei primi minuti.'),
('nervi','medio','carico','La carica di oggi è un vantaggio. Usala per restare concentrato, non per correre più forte.'),
('nervi','lungo','teso','Sul lungo la tensione è comune. Scegli un ritmo che ti tranquillizza e mantienilo.'),
('nervi','lungo','stanco','Stanco e teso prima del lungo: parti piano e cerca la routine del passo.'),
('nervi','lungo','carico','Hai voglia di partire: bene, ma il lungo premia chi resta costante.')
on conflict (fear, session_kind, feel) do update set body = excluded.body;
