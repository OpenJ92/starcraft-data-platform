CREATE TABLE IF NOT EXISTS datapack.unit_type (
	__id__ SERIAL PRIMARY KEY,        -- Auto-incrementing primary key
    	release_string TEXT NOT NULL,              -- Version of Starcraft
    	id INTEGER NOT NULL,                       -- Unit's ID in the game
    	str_id TEXT,                      -- String identifier for the unit
    	name TEXT,                        -- Name of the unit
    	title TEXT,                       -- Title or description of the unit
    	race TEXT,                        -- Race to which the unit belongs
    	minerals INTEGER,                 -- Cost in minerals for the unit
    	vespene INTEGER,                  -- Cost in vespene gas for the unit
    	supply INTEGER,                   -- Supply requirement for the unit
    	is_building BOOLEAN,              -- Indicates if the unit is a building
    	is_army BOOLEAN,                  -- Indicates if the unit is part of the army
    	is_worker BOOLEAN,                -- Indicates if the unit is a worker
	CONSTRAINT unit_type_id_release_string_unique UNIQUE (id, release_string),
);
