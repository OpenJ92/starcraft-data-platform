from sqlalchemy import Column, Integer, Text, Boolean, UniqueConstraint
from sqlalchemy.future import select
from sqlalchemy.orm import relationship


from database.inject import Injectable
from database.base import Base

class unit_type(Injectable, Base):
    __tablename__ = "unit_type"
    __table_args__ = ( UniqueConstraint("id", "release_string", name="unit_type_id_release_string_unique")
                     , { "schema": 'datapack' } )

    __id__ = Column(Integer, primary_key=True)
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
    def process(cls, replay, session):
        if cls.process_existence(replay, session):
            session.add_all(cls.extract_data(replay))

    @classmethod
    def process_existence(cls, replay, session):
        statement = select(cls).where(cls.release_string == replay.release_string)
        result = session.execute(statement)
        return result.first() == None

    @classmethod
    def extract_data(cls, replay):
        units, release_string = [], replay.release_string
        for _, unit in unit_type.get_unique(replay).items():
            units.append(cls(release_string=release_string, **vars(unit)))
        return units

    @classmethod
    def get_unique(cls, replay):
        units = {}
        for _, unit in replay.datapack.units.items():
            if unit.id not in units.keys():
                units[unit.id] = unit
        return units
