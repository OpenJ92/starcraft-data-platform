CREATE TABLE datapack.ABILITY (
	__id__ SERIAL PRIMARY KEY,        -- Auto-incrementing primary key
    	release_string TEXT,
    	id INTEGER,
    	version TEXT,
    	name TEXT,
    	title TEXT,
    	is_build BOOLEAN,
    	build_time INTEGER,
    	__UNIT_TYPE__ INTEGER,
    	CONSTRAINT ability_unit_type_fkey FOREIGN KEY (__UNIT_TYPE__)
    	    REFERENCES datapack.UNIT_TYPE (__id__) ON DELETE SET NULL
);
