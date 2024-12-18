from sqlalchemy import Column, Integer, Text, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from database.base import Base

from database.warehouse.replay.player import player
from database.warehouse.replay.info import info


class player_leave_event(Base):
    __tablename__ = "player_leave_event"
    __table_args__ = {"schema": "events"}

    __id__ = Column(Integer, primary_key=True)

    pid = Column(Integer)
    frame = Column(Integer)
    second = Column(Integer)
    name = Column(Text)
    is_local = Column(Boolean)

    leave_reason = Column(Integer)

    __player__ = Column(Integer, ForeignKey("replay.player.__id__"))
    player = relationship("player", back_populates="player_leave_events")

    __info__ = Column(Integer, ForeignKey("replay.info.__id__"))
    info = relationship("info", back_populates="player_leave_events")
