CREATE TABLE IF NOT EXISTS events.upgrade_complete_event (
    __id__ SERIAL PRIMARY KEY,          -- Auto-incrementing primary key

    pid INTEGER,                        -- Player ID associated with the event
    frame INTEGER,                      -- Frame number when the upgrade was completed
    second INTEGER,                     -- Time in seconds
    name TEXT,                          -- Name of the event
    upgrade_type_name TEXT,             -- Type of the upgrade completed
    count INTEGER,                      -- Count of the upgrade level

    __player__ INTEGER,                 -- Foreign key to replay.PLAYER
    __info__ INTEGER,                   -- Foreign key to replay.INFO

    CONSTRAINT upgrade_complete_event_player_fkey FOREIGN KEY (__player__)
        REFERENCES replay.PLAYER (__id__) ON DELETE SET NULL,
    CONSTRAINT upgrade_complete_event_info_fkey FOREIGN KEY (__info__)
        REFERENCES replay.INFO (__id__) ON DELETE CASCADE
);

