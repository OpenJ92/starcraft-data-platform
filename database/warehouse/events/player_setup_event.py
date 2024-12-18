from sqlalchemy import Column, Integer, Text, ForeignKey
from sqlalchemy.orm import relationship

from database.base import Base

from database.warehouse.replay.info import info

class player_setup_event(Base):
    __tablename__ = "player_setup_event"
    __table_args__ = {"schema": "events"}

    __id__ = Column(Integer, primary_key=True)

    pid = Column(Integer)
    frame = Column(Integer)
    second = Column(Integer)
    name = Column(Text)
    type = Column(Integer)
    uid = Column(Integer)
    sid = Column(Integer)

    __info__ = Column(Integer, ForeignKey("replay.info.__id__"))
    info = relationship("info", back_populates="player_setup_events")
