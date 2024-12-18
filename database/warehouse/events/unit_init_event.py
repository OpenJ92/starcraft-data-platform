from sqlalchemy import Column, Integer, Text, LargeBinary, ForeignKey
from sqlalchemy.orm import relationship

from database.base import Base

from database.warehouse.replay.object import object
from database.warehouse.replay.info import info

class unit_init_event(Base):
    __tablename__ = "unit_init_event"
    __table_args__ = {"schema": "events"}

    __id__ = Column(Integer, primary_key=True)

    frame = Column(Integer)
    second = Column(Integer)
    name = Column(Text)
    unit_id_index = Column(Integer)
    unit_id_recycle = Column(Integer)
    unit_id = Column(Integer)

    __info__ = Column(Integer, ForeignKey("replay.info.__id__"))
    info = relationship("info", back_populates="unit_init_events")

    __object__ = Column(Integer, ForeignKey("replay.object.__id__"))
    unit = relationship("object", back_populates="unit_init_events")

