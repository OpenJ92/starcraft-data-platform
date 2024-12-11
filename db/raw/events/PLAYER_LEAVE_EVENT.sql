CREATE TABLE IF NOT EXISTS events.PLAYER_LEAVE_EVENT (
    __id__ SERIAL PRIMARY KEY,          -- Auto-incrementing primary key

    pid INTEGER,                        -- Player ID
    frame INTEGER,                      -- Frame number at which the event occurred
    second INTEGER,                     -- Time in seconds
    name TEXT,                          -- Name of the event
    is_local BOOLEAN,                   -- Whether the event is local

    leave_reason INTEGER,               -- Reason for the player leaving the game

    __PLAYER__ INTEGER,                 -- Foreign key to replay.PLAYER
    __INFO__ INTEGER,                   -- Foreign key to replay.INFO

    CONSTRAINT player_leave_event_player_fkey FOREIGN KEY (__PLAYER__)
        REFERENCES replay.PLAYER (__id__) ON DELETE SET NULL,
    CONSTRAINT player_leave_event_info_fkey FOREIGN KEY (__INFO__)
        REFERENCES replay.INFO (__id__) ON DELETE CASCADE
);

