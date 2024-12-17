create schema if not exists datapack;
create schema if not exists replay;
create schema if not exists events;

\i datapack/schema.sql
\i replay/schema.sql
\i events/schema.sql
