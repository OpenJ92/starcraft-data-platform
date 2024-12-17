CREATE TABLE IF NOT EXISTS events.UNIT_DIED_EVENT (
    __id__ SERIAL PRIMARY KEY,          -- Auto-incrementing primary key

    frame INTEGER,                      -- Frame number when the unit died
    second INTEGER,                     -- Time in seconds
    name TEXT,                          -- Name of the event
    unit_id_index INTEGER,              -- Unit ID index
    unit_id_recycle INTEGER,            -- Unit ID recycle
    unit_id INTEGER,                    -- Unit ID
    killer_pid INTEGER,                 -- Player ID of the killer
    x INTEGER,                          -- X-coordinate of the unit when it died
    y INTEGER,                          -- Y-coordinate of the unit when it died

    __UNIT__ INTEGER,                   -- Foreign key to replay.OBJECT (died unit)
    __KILLING_UNIT__ INTEGER,           -- Foreign key to replay.OBJECT (killing unit)
    __INFO__ INTEGER,                   -- Foreign key to replay.INFO
    __PLAYER__ INTEGER,                 -- Foreign key to replay.PLAYER (killing player)

    CONSTRAINT unit_died_event_unit_fkey FOREIGN KEY (__UNIT__)
        REFERENCES replay.OBJECT (__id__) ON DELETE SET NULL,
    CONSTRAINT unit_died_event_killing_unit_fkey FOREIGN KEY (__KILLING_UNIT__)
        REFERENCES replay.OBJECT (__id__) ON DELETE SET NULL,
    CONSTRAINT unit_died_event_info_fkey FOREIGN KEY (__INFO__)
        REFERENCES replay.INFO (__id__) ON DELETE CASCADE,
    CONSTRAINT unit_died_event_player_fkey FOREIGN KEY (__PLAYER__)
        REFERENCES replay.PLAYER (__id__) ON DELETE SET NULL
);

