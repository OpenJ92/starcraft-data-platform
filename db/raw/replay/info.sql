CREATE TABLE IF NOT EXISTS replay.INFO (
    __id__ SERIAL PRIMARY KEY,        -- Auto-incrementing primary key

    filename TEXT,                    -- Name of the replay file
    filehash TEXT,                    -- Unique hash of the replay file
    load_level INTEGER,               -- Load level of the replay
    speed TEXT,                       -- Game speed
    type TEXT,                        -- Game type (general category)
    game_type TEXT,                   -- Specific game type
    real_type TEXT,                   -- Real game type
    category TEXT,                    -- Replay category
    is_ladder BOOLEAN,                -- Whether the game is a ladder match
    is_private BOOLEAN,               -- Whether the replay is private
    map_hash TEXT,                    -- Unique hash of the map
    region TEXT,                      -- Game region
    game_fps FLOAT,                   -- Game frames per second
    frames INTEGER,                   -- Total number of frames
    build INTEGER,                    -- Game build version
    base_build INTEGER,               -- Base build version
    release_string TEXT,              -- Game release string
    amm INTEGER,                      -- Automatic Matchmaking ID
    competitive INTEGER,              -- Competitive setting
    practice INTEGER,                 -- Practice mode setting
    cooperative INTEGER,              -- Cooperative mode setting
    battle_net INTEGER,               -- Battle.net mode setting
    hero_duplicates_allowed INTEGER,  -- Whether duplicate heroes are allowed
    map_name TEXT,                    -- Name of the map
    expansion TEXT,                   -- Game expansion pack
    windows_timestamp BIGINT,         -- Windows timestamp of the replay
    unix_timestamp BIGINT,            -- Unix timestamp of the replay
    end_time TIMESTAMP,               -- End time of the replay
    time_zone FLOAT,                  -- Time zone of the replay
    start_time TIMESTAMP,             -- Start time of the replay
    date TIMESTAMP,                   -- Date of the replay

    __MAP__ INTEGER,                  -- Foreign key reference to MAP table
    CONSTRAINT info_map_fkey FOREIGN KEY (__map__)
        REFERENCES replay.MAP (__id__) ON DELETE SET NULL
);

