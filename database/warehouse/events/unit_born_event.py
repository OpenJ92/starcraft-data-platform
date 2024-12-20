from sqlalchemy import Column, Integer, Text, Float, ForeignKey
from sqlalchemy.orm import relationship

from database.base import Base

from database.warehouse.replay.player import player
from database.warehouse.replay.info import info
from database.warehouse.replay.object import object


class unit_born_event(Base):
    __tablename__ = "unit_born_event"
    __table_args__ = {"schema": "events"}

    __id__ = Column(Integer, primary_key=True)

    frame = Column(Integer)
    second = Column(Integer)
    name = Column(Text)
    unit_id_index = Column(Integer)
    unit_id_recycle = Column(Integer)
    unit_id = Column(Integer)
    unit_type_name = Column(Text)
    control_pid = Column(Integer)
    upkeep_pid = Column(Integer)
    x = Column(Float)
    y = Column(Float)

    __info__ = Column(Integer, ForeignKey("replay.info.__id__"))
    info = relationship("info", back_populates="unit_born_events")

    __object__ = Column(Integer, ForeignKey("replay.object.__id__"))
    unit = relationship("object", back_populates="unit_born_events")

    __player__ = Column(Integer, ForeignKey("replay.player.__id__"))
    unit_controller = relationship("player", back_populates="unit_born_events")
