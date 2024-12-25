from sqlalchemy import Column, Integer, Text, LargeBinary
from sqlalchemy.exc import IntegrityError, OperationalError
from sqlalchemy.future import select
from sqlalchemy.orm import relationship

from asyncio import Lock

from database.inject import Injectable
from database.base import Base


class map(Injectable, Base):
    _lock = Lock()
    __tablename__ = "map"
    __table_args__ = {"schema": "replay"}

    primary_id = Column(Integer, primary_key=True)

    filename = Column(Text)
    filehash = Column(Text)
    name = Column(Text)
    author = Column(Text)
    description = Column(Text)
    website = Column(Text)
    minimap = Column(LargeBinary) ## Store elsewhere?

    replays = relationship("info", back_populates="map")

    @classmethod
    @property
    def __tableschema__(self):
        return "replay"

    @classmethod
    async def process(cls, replay, session):
        async with cls._lock:
            try:
                if await cls.process_existence(replay.map.filehash, session):
                    return

                data = cls.get_data(replay.map)
                breakpoint()
                session.add(cls(**data))

            except IntegrityError as e:
                await session.rollback()
                print(f"IntegrityError: {e.orig}")
                # Handle specific cases like unique constraint violations
            except OperationalError as e:
                await session.rollback()
                print(f"OperationalError: {e.orig}")
                # Handle deadlocks or connection issues
            except Exception as e:
                await session.rollback()
                print(f"Unexpected error: {e}")
                # Gracefully handle all other exceptions

    @classmethod
    async def process_existence(cls, filehash, session):
        statement = select(cls).where(cls.filehash == filehash)
        result = await session.execute(statement)
        breakpoint()
        return result.scalar()

    @classmethod
    def get_data(cls, obj):
        parameters = {}
        for variable, value in vars(obj).items():
            if variable in cls.columns:
                parameters[variable] = value
        return parameters

    columns = \
        { "filename"
        , "filehash"
        , "name"
        , "author"
        , "description"
        , "website"
        , "minimap"
        }
