from sqlalchemy import create_engine
from database.base import Base

from database.raw.datapack.unit_type import unit_type
from database.raw.datapack.ability import ability

from database.raw.replay.map import map
from database.raw.replay.info import info
from database.raw.replay.player import player
from database.raw.replay.object import object


from database.config import engine

#create schema
with engine.connect() as connection:
    connection.execute("CREATE SCHEMA IF NOT EXISTS datapack;")
    connection.execute("CREATE SCHEMA IF NOT EXISTS events;")
    connection.execute("CREATE SCHEMA IF NOT EXISTS replay;")

# Create all tables
Base.metadata.create_all(bind=engine)
