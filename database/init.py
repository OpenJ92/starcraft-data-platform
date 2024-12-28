from sqlalchemy import create_engine

from database.warehouse.datapack.unit_type import unit_type
from database.warehouse.datapack.ability import ability

from database.warehouse.replay.map import map
from database.warehouse.replay.user import user
from database.warehouse.replay.info import info
from database.warehouse.replay.player import player
from database.warehouse.replay.object import object

from database.warehouse.events.basic_command_event import basic_command_event
from database.warehouse.events.chat_event import chat_event
from database.warehouse.events.player_leave_event import player_leave_event
from database.warehouse.events.player_stats_event import player_stats_event
from database.warehouse.events.unit_born_event import unit_born_event
from database.warehouse.events.unit_died_event import unit_died_event
from database.warehouse.events.unit_done_event import unit_done_event
from database.warehouse.events.unit_init_event import unit_init_event
from database.warehouse.events.upgrade_complete_event import upgrade_complete_event

from database.config import engine
from database.base import Base

import asyncio
from sqlalchemy.sql import text

async def init_db():
    """Asynchronously initialize the database schema."""

    async with engine.begin() as conn:
        # Create schemas if they do not exist
        await conn.execute(text("CREATE SCHEMA IF NOT EXISTS datapack;"))
        await conn.execute(text("CREATE SCHEMA IF NOT EXISTS events;"))
        await conn.execute(text("CREATE SCHEMA IF NOT EXISTS replay;"))

        # Create all tables
        await conn.run_sync(Base.metadata.create_all)

    await engine.dispose()

if __name__ == "__main__":
    asyncio.run(init_db())
