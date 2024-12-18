from sqlalchemy import Column, Integer, Text, ForeignKey
from sqlalchemy.orm import relationship

from database.base import Base

from database.warehouse.replay.info import info
from database.warehouse.replay.player import player
from database.warehouse.datapack.unit_type import unit_type

class unit_died_event(Base):
    __tablename__ = "unit_died_event"
    __table_args__ = {"schema": "events"}

    __id__ = Column(Integer, primary_key=True)

    frame = Column(Integer)
    second = Column(Integer)
    name = Column(Text)
    unit_id_index = Column(Integer)
    unit_id_recycle = Column(Integer)
    unit_id = Column(Integer)
    killer_pid = Column(Integer)
    x = Column(Integer)
    y = Column(Integer)

    __unit__ = Column(Integer, ForeignKey("replay.object.__id__"))
    unit = relationship(
        "object",
        primaryjoin="unit_died_event.__unit__==object.__id__",
        back_populates="death_event",)

    __killing_unit__ = Column(Integer, ForeignKey("replay.object.__id__"))
    killing_unit = relationship(
        "object",
        primaryjoin="UnitDiedEvent.__killing_unit__==object.__id__",
        back_populates="kill_event",)

    __info__ = Column(Integer, ForeignKey("replay.info.__id__"))
    info = relationship("info", back_populates="unit_died_events")

    __player__ = Column(Integer, ForeignKey("replay.player.__id__"))
    killing_player = relationship("player", back_populates="unit_died_events")

