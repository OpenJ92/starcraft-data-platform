CREATE TABLE IF NOT EXISTS events.unit_done_event (
    __id__ SERIAL PRIMARY KEY,          -- Auto-incrementing primary key

    frame INTEGER,                      -- Frame number when the unit was completed
    second INTEGER,                     -- Time in seconds
    name TEXT,                          -- Name of the event
    unit_id_index INTEGER,              -- Unit ID index
    unit_id_recycle INTEGER,            -- Unit ID recycle
    unit_id INTEGER,                    -- Unit ID

    __info__ INTEGER,                   -- Foreign key to replay.INFO
    __object__ INTEGER,                 -- Foreign key to replay.OBJECT

    CONSTRAINT unit_done_event_info_fkey FOREIGN KEY (__info__)
        REFERENCES replay.INFO (__id__) ON DELETE CASCADE,
    CONSTRAINT unit_done_event_object_fkey FOREIGN KEY (__object__)
        REFERENCES replay.OBJECT (__id__) ON DELETE SET NULL
);
