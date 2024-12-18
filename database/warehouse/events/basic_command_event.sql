CREATE TABLE IF NOT EXISTS events.basic_command_event (
    __id__ SERIAL PRIMARY KEY,         -- Auto-incrementing primary key

    pid INTEGER,                       -- Player ID
    frame INTEGER,                     -- Frame at which the event occurred
    second INTEGER,                    -- Time in seconds
    is_local BOOLEAN,                  -- Whether the event is local
    name TEXT,                         -- Name of the event
    has_ability BOOLEAN,               -- Whether the event involves an ability
    ability_link INTEGER,              -- Link to the ability
    command_index INTEGER,             -- Command index
    ability_name TEXT,                 -- Name of the ability

    __player__ INTEGER,                -- Foreign key to replay.PLAYER
    __info__ INTEGER,                  -- Foreign key to replay.INFO
    __ability__ INTEGER,               -- Foreign key to datapack.ABILITY

    CONSTRAINT basic_command_event_player_fkey FOREIGN KEY (__player__)
        REFERENCES replay.PLAYER (__id__) ON DELETE SET NULL,
    CONSTRAINT basic_command_event_info_fkey FOREIGN KEY (__info__)
        REFERENCES replay.INFO (__id__) ON DELETE CASCADE,
    CONSTRAINT basic_command_event_ability_fkey FOREIGN KEY (__ability__)
        REFERENCES datapack.ABILITY (__id__) ON DELETE SET NULL
);
