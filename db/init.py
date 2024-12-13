from sqlalchemy import create_engine
from db.base import Base

from db.raw.datapack.unit_type import UNIT_TYPE
from db.raw.datapack.ability import ABILITY

from db.config import engine

# Create all tables
Base.metadata.create_all(bind=engine)
