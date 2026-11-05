-- Garmin Connect: stati OAuth, collegamento, attività ricevute
create table if not exists garmin_oauth_states (
  state text primary key,
  user_id uuid not null references profiles(id) on delete cascade,
  code_verifier text not null,
  consent_ai boolean not null default false,
  created_at timestamptz not null default now()
);

create table if not exists garmin_connections (
  user_id uuid primary key references profiles(id) on delete cascade,
  garmin_user_id text unique not null,
  access_token text not null,
  refresh_token text,
  expires_at timestamptz,
  consent_ai boolean not null default false,
  consent_at timestamptz,
  connected_at timestamptz not null default now()
);

create table if not exists garmin_activities (
  summary_id text primary key,
  user_id uuid not null references profiles(id) on delete cascade,
  garmin_user_id text not null,
  activity_type text,
  started_at timestamptz,
  duration_s integer,
  distance_m numeric,
  avg_hr integer,
  max_hr integer,
  avg_speed_mps numeric,
  raw jsonb,
  received_at timestamptz not null default now()
);

-- Token e dati grezzi accessibili solo al backend (service role)
alter table garmin_oauth_states enable row level security;
alter table garmin_connections enable row level security;
alter table garmin_activities enable row level security;

-- L'atleta legge solo le proprie attività
create policy "garmin_activities_own_select" on garmin_activities
  for select using (auth.uid() = user_id);
