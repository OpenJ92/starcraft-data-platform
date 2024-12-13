from sqlalchemy import Column, Integer, Text, Boolean
from sqlalchemy.orm import relationship

from db.base import Base

class unit_type(Base):
    __tablename__ = "unit_type"
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

    abilities = relationship("ability", back_populates="build_unit")
