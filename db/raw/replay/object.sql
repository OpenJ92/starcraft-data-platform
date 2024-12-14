CREATE TABLE IF NOT EXISTS replay.object (
    __id__ SERIAL PRIMARY KEY,        -- Auto-incrementing primary key

    id INTEGER,                       -- Unique identifier for the object
    started_at INTEGER,               -- Frame at which the object started
    finished_at INTEGER,              -- Frame at which the object finished
    died_at INTEGER,                  -- Frame at which the object died
    name TEXT,                        -- Name of the object

    location_x INTEGER,               -- X-coordinate of the object
    location_y INTEGER,               -- Y-coordinate of the object

    __info__ INTEGER,                 -- Foreign key reference to INFO table
    __owner__ INTEGER,                -- Foreign key reference to PLAYER table
    __unit_type__ INTEGER,            -- Foreign key reference to UNIT_TYPE table

    CONSTRAINT object_info_fkey FOREIGN KEY (__info__)
        REFERENCES replay.INFO (__id__) ON DELETE CASCADE,
    CONSTRAINT object_player_fkey FOREIGN KEY (__owner__)
        REFERENCES replay.PLAYER (__id__) ON DELETE SET NULL,
    CONSTRAINT object_unit_type_fkey FOREIGN KEY (__unit_type__)
        REFERENCES datapack.UNIT_TYPE (__id__) ON DELETE SET NULL
);

