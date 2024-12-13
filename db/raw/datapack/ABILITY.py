from sqlalchemy import Column, Integer, Text, ForeignKey
from sqlalchemy.orm import relationship

from db.base import Base

class ABILITY(Model):
    __tablename__ = "ABILITY"
    __table_args__ = {"schema": "datapack"}

    __id__ = Column(Integer, primary_key=True)

    release_string = Column(Text)
    id = Column(Integer)
    version = Column(Text)
    name = Column(Text)
    title = Column(Text)
    is_build = Column(Boolean)
    build_time = Column(Integer)

    __UNIT_TYPE__ = Column(Integer, ForeignKey("datapack.UNIT_TYPE.__id__"))
    build_unit = relationship("UNIT_TYPE", back_populates="abilities")
