CREATE TABLE IF NOT EXISTS events.UNIT_BORN_EVENT (
    __id__ SERIAL PRIMARY KEY,          -- Auto-incrementing primary key

    frame INTEGER,                      -- Frame number when the unit was born
    second INTEGER,                     -- Time in seconds
    name TEXT,                          -- Name of the event
    unit_id_index INTEGER,              -- Unit ID index
    unit_id_recycle INTEGER,            -- Unit ID recycle
    unit_id INTEGER,                    -- Unit ID
    unit_type_name TEXT,                -- Type of the unit
    control_pid INTEGER,                -- Controlling player ID
    upkeep_pid INTEGER,                 -- Upkeep player ID
    x FLOAT,                            -- X-coordinate of the unit
    y FLOAT,                            -- Y-coordinate of the unit

    __PLAYER__ INTEGER,                 -- Foreign key to replay.PLAYER
    __INFO__ INTEGER,                   -- Foreign key to replay.INFO
    __OBJECT__ INTEGER,                 -- Foreign key to replay.OBJECT

    CONSTRAINT unit_born_event_player_fkey FOREIGN KEY (__PLAYER__)
        REFERENCES replay.PLAYER (__id__) ON DELETE SET NULL,
    CONSTRAINT unit_born_event_info_fkey FOREIGN KEY (__INFO__)
        REFERENCES replay.INFO (__id__) ON DELETE CASCADE,
    CONSTRAINT unit_born_event_object_fkey FOREIGN KEY (__OBJECT__)
        REFERENCES replay.OBJECT (__id__) ON DELETE SET NULL
);

