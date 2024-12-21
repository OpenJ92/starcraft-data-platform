from sqlalchemy import Column, Integer, Text, ForeignKey
from sqlalchemy.orm import relationship

from database.base import Base

from database.warehouse.replay.info import info
from database.warehouse.replay.player import player

class upgrade_complete_event(Base):
    __tablename__ = "upgrade_complete_event"
    __table_args__ = {"schema": "events"}

    primary_id = Column(Integer, primary_key=True)

    pid = Column(Integer)
    frame = Column(Integer)
    second = Column(Integer)
    name = Column(Text)
    upgrade_type_name = Column(Text)
    count = Column(Integer)

    player_id = Column(Integer, ForeignKey("replay.player.primary_id"))
    player = relationship("player", back_populates="upgrade_complete_events")

    info_id = Column(Integer, ForeignKey("replay.info.primary_id"))
    info = relationship("info", back_populates="upgrade_complete_events")
