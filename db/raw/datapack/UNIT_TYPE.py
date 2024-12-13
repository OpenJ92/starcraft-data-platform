from sqlalchemy import Column, Integer, Text, Boolean
from db.base import Base

class UNIT_TYPE(Base):
    __tablename__ = "UNIT_TYPE"
    __table_args__ = {"schema": "datapack"}

    __id__ = Column(Integer, primary_key=True)

    release_string = Column(Text)
    id = Column(Integer)
    str_id = Column(Text)
    name = Column(Text)
    title = Column(Text)
    race = Column(Text)
    minerals = Column(Integer)
    vespene = Column(Integer)
    supply = Column(Integer)
    is_building = Column(Boolean)
    is_army = Column(Boolean)
    is_worker = Column(Boolean)

    abilities = relationship("ABILITY", back_populates="build_unit")
