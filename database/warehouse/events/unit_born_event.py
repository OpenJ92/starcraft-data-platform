from sqlalchemy import Column, Integer, Text, Float, ForeignKey
from sqlalchemy.orm import relationship

from database.base import Base

from database.warehouse.replay.player import player
from database.warehouse.replay.info import info
from database.warehouse.replay.object import object


class unit_born_event(Base):
    __tablename__ = "unit_born_event"
    __table_args__ = {"schema": "events"}

    primary_id = Column(Integer, primary_key=True)

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

    info_id = Column(Integer, ForeignKey("replay.info.primary_id"))
    info = relationship("info", back_populates="unit_born_events")

    object_id = Column(Integer, ForeignKey("replay.object.primary_id"))
    unit = relationship("object", back_populates="unit_born_events")

    player_id = Column(Integer, ForeignKey("replay.player.primary_id"))
    unit_controller = relationship("player", back_populates="unit_born_events")
