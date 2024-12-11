CREATE TABLE IF NOT EXISTS events.PLAYER_STATS_EVENT (
    __id__ SERIAL PRIMARY KEY,          -- Auto-incrementing primary key

    name TEXT,                          -- Name of the event
    second FLOAT,                       -- Time in seconds
    minerals_current FLOAT,             -- Current minerals count
    vespene_current FLOAT,              -- Current vespene count
    minerals_collection_rate FLOAT,     -- Rate of mineral collection
    vespene_collection_rate FLOAT,      -- Rate of vespene collection
    workers_active_count FLOAT,         -- Number of active workers
    minerals_used_in_progress_army FLOAT,
    minerals_used_in_progress_economy FLOAT,
    minerals_used_in_progress_technology FLOAT,
    minerals_used_in_progress FLOAT,
    vespene_used_in_progress_army FLOAT,
    vespene_used_in_progress_economy FLOAT,
    vespene_used_in_progress_technology FLOAT,
    vespene_used_in_progress FLOAT,
    resources_used_in_progress FLOAT,
    minerals_used_current_army FLOAT,
    minerals_used_current_economy FLOAT,
    minerals_used_current_technology FLOAT,
    minerals_used_current FLOAT,
    vespene_used_current_army FLOAT,
    vespene_used_current_economy FLOAT,
    vespene_used_current_technology FLOAT,
    vespene_used_current FLOAT,
    resources_used_current FLOAT,
    minerals_lost_army FLOAT,
    minerals_lost_economy FLOAT,
    minerals_lost_technology FLOAT,
    minerals_lost FLOAT,
    vespene_lost_army FLOAT,
    vespene_lost_economy FLOAT,
    vespene_lost_technology FLOAT,
    vespene_lost FLOAT,
    resources_lost FLOAT,
    minerals_killed_army FLOAT,
    minerals_killed_economy FLOAT,
    minerals_killed_technology FLOAT,
    minerals_killed FLOAT,
    vespene_killed_army FLOAT,
    vespene_killed_economy FLOAT,
    vespene_killed_technology FLOAT,
    vespene_killed FLOAT,
    resources_killed FLOAT,
    food_used FLOAT,
    food_made FLOAT,
    minerals_used_active_forces FLOAT,
    vespene_used_active_forces FLOAT,
    ff_minerals_lost_army FLOAT,
    ff_minerals_lost_economy FLOAT,
    ff_minerals_lost_technology FLOAT,
    ff_vespene_lost_army FLOAT,
    ff_vespene_lost_economy FLOAT,
    ff_vespene_lost_technology FLOAT,

    __PLAYER__ INTEGER,                 -- Foreign key to replay.PLAYER
    __INFO__ INTEGER,                   -- Foreign key to replay.INFO

    CONSTRAINT player_stats_event_player_fkey FOREIGN KEY (__PLAYER__)
        REFERENCES replay.PLAYER (__id__) ON DELETE SET NULL,
    CONSTRAINT player_stats_event_info_fkey FOREIGN KEY (__INFO__)
        REFERENCES replay.INFO (__id__) ON DELETE CASCADE
);

