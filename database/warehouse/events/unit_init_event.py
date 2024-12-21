from sqlalchemy import Column, Integer, Text, LargeBinary, ForeignKey
from sqlalchemy.orm import relationship

from database.base import Base

from database.warehouse.replay.object import object
from database.warehouse.replay.info import info

class unit_init_event(Base):
    __tablename__ = "unit_init_event"
    __table_args__ = {"schema": "events"}

    primary_id = Column(Integer, primary_key=True)

    frame = Column(Integer)
    second = Column(Integer)
    name = Column(Text)
    unit_id_index = Column(Integer)
    unit_id_recycle = Column(Integer)
    unit_id = Column(Integer)

    info_id = Column(Integer, ForeignKey("replay.info.primary_id"))
    info = relationship("info", back_populates="unit_init_events")

    object_id = Column(Integer, ForeignKey("replay.object.primary_id"))
    unit = relationship("object", back_populates="unit_init_events")

