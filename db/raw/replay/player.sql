CREATE TABLE IF NOT EXISTS replay.player (
    __id__ SERIAL PRIMARY KEY,        -- Auto-incrementing primary key

    sid INTEGER,                      -- Session ID for the player
    team_id INTEGER,                  -- Team ID to which the player belongs
    is_human BOOLEAN,                 -- Indicates if the player is human
    is_observer BOOLEAN,              -- Indicates if the player is an observer
    is_referee BOOLEAN,               -- Indicates if the player is a referee
    region TEXT,                      -- Region of the player
    subregion INTEGER,                -- Subregion of the player
    toon_id BIGINT,                   -- Toon ID (longer unique identifier)
    uid INTEGER,                      -- Short unique identifier
    clan_tag TEXT,                    -- Clan tag of the player
    name TEXT,                        -- Name of the player
    combined_race_levels BIGINT,      -- Combined race levels for the player
    highest_league INTEGER,           -- Highest league achieved
    pid INTEGER,                      -- Player ID in the match
    result TEXT,                      -- Result of the match for the player (e.g., Win, Loss)
    pick_race TEXT,                   -- Race selected at match start
    play_race TEXT,                   -- Race actually played

    id INTEGER,                       -- Another player ID field (possible duplicate or legacy?)

    __info__ INTEGER,                 -- Foreign key reference to INFO table
    CONSTRAINT player_info_fkey FOREIGN KEY (__info__)
        REFERENCES replay.INFO (__id__) ON DELETE CASCADE
);

