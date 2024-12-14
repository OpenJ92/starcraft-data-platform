CREATE TABLE IF NOT EXISTS replay.MAP (
    __id__ SERIAL PRIMARY KEY,        -- Auto-incrementing primary key

    filename TEXT,                    -- Name of the map file
    filehash TEXT,                    -- Unique hash of the map file
    name TEXT,                        -- Name of the map
    author TEXT,                      -- Author of the map
    description TEXT,                 -- Description of the map
    website TEXT,                     -- Website associated with the map
    minimap BYTEA                     -- Binary data for the minimap image
);

