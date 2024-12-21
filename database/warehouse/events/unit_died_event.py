from sqlalchemy import Column, Integer, Text, ForeignKey
from sqlalchemy.orm import relationship

from database.base import Base

from database.warehouse.replay.info import info
from database.warehouse.replay.player import player
from database.warehouse.datapack.unit_type import unit_type

class unit_died_event(Base):
    __tablename__ = "unit_died_event"
    __table_args__ = {"schema": "events"}

    primary_id = Column(Integer, primary_key=True)

    frame = Column(Integer)
    second = Column(Integer)
    name = Column(Text)
    unit_id_index = Column(Integer)
    unit_id_recycle = Column(Integer)
    unit_id = Column(Integer)
    killer_pid = Column(Integer)
    x = Column(Integer)
    y = Column(Integer)

    unit_id = Column(Integer, ForeignKey("replay.object.primary_id"))
    unit = relationship(
        "object",
        primaryjoin="unit_died_event.unit_id==object.primary_id",
        back_populates="death_event",)

    killing_unit_id = Column(Integer, ForeignKey("replay.object.primary_id"))
    killing_unit = relationship(
        "object",
        primaryjoin="unit_died_event.killing_unit_id==object.primary_id",
        back_populates="kill_events",)

    info_id = Column(Integer, ForeignKey("replay.info.primary_id"))
    info = relationship("info", back_populates="unit_died_events")

    player_id = Column(Integer, ForeignKey("replay.player.primary_id"))
    killing_player = relationship("player", back_populates="unit_died_events")

