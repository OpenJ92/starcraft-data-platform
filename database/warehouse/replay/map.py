from sqlalchemy import Column, Integer, Text, LargeBinary
from sqlalchemy.exc import IntegrityError, OperationalError
from sqlalchemy.future import select
from sqlalchemy.orm import relationship

from database.inject import Injectable
from database.base import Base

from asyncio import Lock

class map(Injectable, Base):
    __tablename__ = "map"
    __table_args__ = {"schema": "replay"}
    _lock = Lock()

    primary_id = Column(Integer, primary_key=True)

    filename = Column(Text)
    filehash = Column(Text)
    name = Column(Text)
    author = Column(Text)
    description = Column(Text)
    website = Column(Text)

    replays = relationship("info", back_populates="map")

    @classmethod
    @property
    def __tableschema__(self):
        return "replay"

    @classmethod
    async def process(cls, replay, session):
        async with cls._lock:
            if await cls.process_existence(replay.map_hash, session):
                return

            # Load map if not exists
            replay.load_map()

            data = cls.get_data(replay.map)
            session.add(cls(**data))

    @classmethod
    async def process_existence(cls, filehash, session):
        statement = select(cls).where(cls.filehash == filehash)
        result = await session.execute(statement)
        return result.scalar()

    columns = \
        { "filename"
        , "filehash"
        , "name"
        , "author"
        , "description"
        , "website"
        }
