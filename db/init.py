from sqlalchemy import create_engine
from db.base import Base

from db.raw.datapack.unit_type import unit_type
from db.raw.datapack.ability import ability

from db.config import engine

#create schema
with engine.connect() as connection:
    connection.execute("CREATE SCHEMA IF NOT EXISTS datapack;")
    connection.execute("CREATE SCHEMA IF NOT EXISTS events;")
    connection.execute("CREATE SCHEMA IF NOT EXISTS replay;")

# Create all tables
Base.metadata.create_all(bind=engine)
