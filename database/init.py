from sqlalchemy import create_engine
from database.base import Base

from database.warehouse.datapack.unit_type import unit_type
from database.warehouse.datapack.ability import ability

from database.warehouse.replay.map import map
from database.warehouse.replay.info import info
from database.warehouse.replay.player import player
from database.warehouse.replay.object import object

from database.warehouse.events.basic_command_event import basic_command_event
from database.warehouse.events.chat_event import chat_event
from database.warehouse.events.player_leave_event import player_leave_event
from database.warehouse.events.player_setup_event import player_setup_event

from database.config import engine

#create schema
with engine.connect() as connection:
    connection.execute("CREATE SCHEMA IF NOT EXISTS datapack;")
    connection.execute("CREATE SCHEMA IF NOT EXISTS events;")
    connection.execute("CREATE SCHEMA IF NOT EXISTS replay;")

# Create all tables
Base.metadata.create_all(bind=engine)
