CREATE TABLE IF NOT EXISTS events.PLAYER_SETUP_EVENT (
    __id__ SERIAL PRIMARY KEY,          -- Auto-incrementing primary key

    pid INTEGER,                        -- Player ID
    frame INTEGER,                      -- Frame number at which the event occurred
    second INTEGER,                     -- Time in seconds
    name TEXT,                          -- Name of the event
    type INTEGER,                       -- Type of the event
    uid INTEGER,                        -- Unique ID for the player
    sid INTEGER,                        -- Session ID for the player

    __INFO__ INTEGER,                   -- Foreign key to replay.INFO

    CONSTRAINT player_setup_event_info_fkey FOREIGN KEY (__INFO__)
        REFERENCES replay.INFO (__id__) ON DELETE CASCADE
);

