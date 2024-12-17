from sqlalchemy import Column, Integer, Text, Boolean from sqlalchemy.orm import relationship

from db.base import Base

class unit_type(Base):
    __tablename__ = "unit_type"
    __table_args__ = ( {"schema": "datapack"},
      UniqueConstraint("id", "release_string", name="unit_type_id_release_string_unique"),)

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
