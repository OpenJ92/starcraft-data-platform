CREATE TABLE IF NOT EXISTS events.UNIT_INIT_EVENT (
    __id__ SERIAL PRIMARY KEY,          -- Auto-incrementing primary key

    frame INTEGER,                      -- Frame number when the unit was initialized
    second INTEGER,                     -- Time in seconds
    name TEXT,                          -- Name of the event
    unit_id_index INTEGER,              -- Unit ID index
    unit_id_recycle INTEGER,            -- Unit ID recycle
    unit_id INTEGER,                    -- Unit ID

    __INFO__ INTEGER,                   -- Foreign key to replay.INFO
    __OBJECT__ INTEGER,                 -- Foreign key to replay.OBJECT

    CONSTRAINT unit_init_event_info_fkey FOREIGN KEY (__INFO__)
        REFERENCES replay.INFO (__id__) ON DELETE CASCADE,
    CONSTRAINT unit_init_event_object_fkey FOREIGN KEY (__OBJECT__)
        REFERENCES replay.OBJECT (__id__) ON DELETE SET NULL
);

