from sqlalchemy import Column, Integer, Text, LargeBinary, ForeignKey
from sqlalchemy.orm import relationship

from database.base import Base

from database.raw.replay.info import info
from database.raw.replay.player import player
from database.raw.datapack.unit_type import unit_type


class object(Base):
    __tablename__ = "object"
    __table_args__ = {"schema": "replay"}

    __id__ = Column(Integer, primary_key=True)

    id = Column(Integer)
    started_at = Column(Integer)
    finished_at = Column(Integer)
    died_at = Column(Integer)
    name = Column(Text)

    location_x = Column(Integer)
    location_y = Column(Integer)

    __info__ = Column(Integer, ForeignKey("replay.info.__id__"))
    replay = relationship("info", back_populates="objects")

    __owner__ = Column(Integer, ForeignKey("replay.player.__id__"))
    owner = relationship(
        "player",
        primaryjoin="object.__owner__==player.__id__",
        back_populates="owned_objects",)

    __killing_player__ = Column(Integer, ForeignKey('replay.player.__id__'))
    killing_player = relationship(
        "player",
        primaryjoin='object.__killing_player__==player.__id__',
        back_populates='killed_objects')

    __killing_unit__ = Column(Integer, ForeignKey("replay.object.__id__"), nullable=True)
    killing_unit = relationship("object", remote_side=[__id__], backref="killed_units")

    __unit_type__ = Column(Integer, ForeignKey("datapack.unit_type.__id__"))
    unit_type = relationship(
        "unit_type",
        primaryjoin='object.__unit_type__==unit_type.__id__',
        back_populates="objects")
