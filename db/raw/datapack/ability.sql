CREATE TABLE IF NOT EXISTS datapack.ability (
	__id__ SERIAL PRIMARY KEY,        -- Auto-incrementing primary key
    	release_string TEXT NOT NULL,     -- Version of Starcraft
    	id INTEGER NOT NULL,              -- Abilities ID in the game
    	version TEXT,                     -- related Starcraft II Expansion
    	name TEXT,                        -- ability name
    	title TEXT,                       -- printable title of this abililty
    	is_build BOOLEAN,                 -- Boolean flagging this ability as creating a new unit
    	build_time INTEGER,               -- The number of seconds required to build this unit. 0 if not ``is_build``
    	__unit_type__ INTEGER,            -- A reference to the table `Unit_Type` that built by this ability. Default to None.
    	CONSTRAINT ability_unit_type_fkey FOREIGN KEY (__unit_type__)
    	    REFERENCES datapack.UNIT_TYPE (__id__) ON DELETE SET NULL
	CONSTRAINT ability_id_release_string_unique UNIQUE (id, release_string)
);
