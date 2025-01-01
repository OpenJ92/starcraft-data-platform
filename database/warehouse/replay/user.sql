CREATE TABLE IF NOT EXISTS replay.user (
	primary_id SERIAL PRIMARY KEY,
	name TEXT NOT NULL,
	uid INTEGER NOT NULL,
	region INTEGER,
	subregion INTEGER,
);

