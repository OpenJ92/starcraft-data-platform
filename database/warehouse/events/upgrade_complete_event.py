from sqlalchemy import Column, Integer, Text, ForeignKey
from sqlalchemy.orm import relationship

from database.base import Base

from database.warehouse.replay.info import info
from database.warehouse.replay.player import player

class upgrade_complete_event(Base):
    __tablename__ = "upgrade_complete_event"
    __table_args__ = {"schema": "events"}

    __id__ = Column(Integer, primary_key=True)

    pid = Column(Integer)
    frame = Column(Integer)
    second = Column(Integer)
    name = Column(Text)
    upgrade_type_name = Column(Text)
    count = Column(Integer)

    __player__ = Column(Integer, ForeignKey("replay.player.__id__"))
    player = relationship("player", back_populates="upgrade_complete_events")

    __info__ = Column(Integer, ForeignKey("replay.info.__id__"))
    info = relationship("info", back_populates="upgrade_complete_events")
