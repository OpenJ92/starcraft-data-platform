from sqlalchemy import Column, Integer, Text, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from database.base import Base

from database.warehouse.replay.player import player
from database.warehouse.replay.info import info


class player_leave_event(Base):
    __tablename__ = "player_leave_event"
    __table_args__ = {"schema": "events"}

    primary_id = Column(Integer, primary_key=True)

    pid = Column(Integer)
    frame = Column(Integer)
    second = Column(Integer)
    name = Column(Text)
    is_local = Column(Boolean)

    leave_reason = Column(Integer)

    player_id = Column(Integer, ForeignKey("replay.player.primary_id"))
    player = relationship("player", back_populates="player_leave_events")

    info_id = Column(Integer, ForeignKey("replay.info.primary_id"))
    info = relationship("info", back_populates="player_leave_events")
