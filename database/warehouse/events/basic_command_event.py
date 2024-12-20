from sqlalchemy import Column, Integer, Text, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from database.base import Base

from database.warehouse.datapack.ability import ability
from database.warehouse.replay.info import info
from database.warehouse.replay.player import player


class basic_command_event(Base):
    __tablename__ = "basic_command_event"
    __table_args__ = {"schema": "events"}

    __id__ = Column(Integer, primary_key=True)

    pid = Column(Integer)
    frame = Column(Integer)
    second = Column(Integer)
    is_local = Column(Boolean)
    name = Column(Text)
    has_ability = Column(Boolean)
    ability_link = Column(Integer)
    command_index = Column(Integer)
    ability_name = Column(Text)

    __player__ = Column(Integer, ForeignKey("replay.player.__id__"))
    player = relationship("player", back_populates="basic_command_events")

    __info__ = Column(Integer, ForeignKey("replay.info.__id__"))
    info = relationship("info", back_populates="basic_command_events")

    __ability__ = Column(Integer, ForeignKey("datapack.ability.__id__"))
    ability = relationship("ability", back_populates="basic_command_events")

