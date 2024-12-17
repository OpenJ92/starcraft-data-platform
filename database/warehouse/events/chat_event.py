from sqlalchemy import Column, Integer, Text, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from database.base import Base

from database.warehouse.replay.player import player
from database.warehouse.replay.info import info


class chat_event(Base):
    __tablename__ = "chat_event"
    __table_args__ = {"schema": "events"}

    __id__ = Column(Integer, primary_key=True)

    pid = Column(Integer)
    frame = Column(Integer)
    second = Column(Integer)
    name = Column(Text)
    target = Column(Integer)
    text = Column(Text)
    to_all = Column(Boolean)
    to_allies = Column(Boolean)
    to_observers = Column(Boolean)

    __player__ = Column(Integer, ForeignKey("replay.player.__id__"))
    player = relationship("player", back_populates="chat_events")

    __info__ = Column(Integer, ForeignKey("replay.info.__id__"))
    info = relationship("info", back_populates="chat_events")
