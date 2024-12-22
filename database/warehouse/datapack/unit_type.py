from sqlalchemy import Column, Integer, Text, Boolean, UniqueConstraint, PrimaryKeyConstraint
from sqlalchemy.future import select
from sqlalchemy.orm import relationship

from asyncio import Lock

from database.inject import Injectable
from database.base import Base

class unit_type(Base, Injectable):
    _lock = Lock()
    __tablename__ = "unit_type"
    __table_args__ = ( UniqueConstraint("id", "release_string", name="unit_type_id_release_string_unique")
                     , { "schema": 'datapack' } )

    primary_id = Column(Integer, primary_key=True)
    release_string = Column(Text)
    id = Column(Integer, nullable=False)
    str_id = Column(Text, nullable=False)
    name = Column(Text)
    title = Column(Text)
    race = Column(Text)
    minerals = Column(Integer)
    vespene = Column(Integer)
    supply = Column(Integer)
    is_building = Column(Boolean)
    is_army = Column(Boolean)
    is_worker = Column(Boolean)

    abilities = relationship("ability", back_populates="build_unit")
    objects = relationship("object", back_populates="unit_type")

    @classmethod
    @property
    def __tableschema__(self):
        return "datapack"

    @classmethod
    async def process(cls, replay, session):
        async with cls._lock:
            try:
                if await cls.process_existence(replay, session):
                    return

                units, release_string = [], replay.release_string
                for _, unit in unit_type.get_unique(replay).items():
                    units.append(cls(release_string=release_string, **vars(unit)))

                session.add_all(units)

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
    async def process_existence(cls, replay, session):
        statement = select(cls).where(cls.release_string == replay.release_string)
        result = await session.execute(statement)
        return result.first()

    @classmethod
    def get_unique(cls, replay):
        units = {}
        for _, unit in replay.datapack.units.items():
            if unit.id not in units.keys():
                units[unit.id] = unit
        return units
