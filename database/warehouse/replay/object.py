from sqlalchemy import Column, Integer, Text, LargeBinary, ForeignKey
from sqlalchemy.orm import relationship

from database.base import Base

from database.warehouse.replay.info import info
from database.warehouse.replay.player import player
from database.warehouse.datapack.unit_type import unit_type


class object(Base):
    __tablename__ = "object"
    __table_args__ = {"schema": "replay"}

    primary_id = Column(Integer, primary_key=True)

    id = Column(Integer)
    started_at = Column(Integer)
    finished_at = Column(Integer)
    died_at = Column(Integer)
    name = Column(Text)

    location_x = Column(Integer)
    location_y = Column(Integer)

    info_id = Column(Integer, ForeignKey("replay.info.primary_id"))
    replay = relationship("info", back_populates="objects")

    owner_id = Column(Integer, ForeignKey("replay.player.primary_id"))
    owner = relationship(
        "player",
        primaryjoin="object.owner_id==player.primary_id",
        back_populates="owned_objects",)

    killing_player_id = Column(Integer, ForeignKey('replay.player.primary_id'))
    killing_player = relationship(
        "player",
        primaryjoin='object.killing_player_id==player.primary_id',
        back_populates='killed_objects')

    killing_unit_id = Column(Integer, ForeignKey("replay.object.primary_id"), nullable=True)
    killing_unit = relationship("object", remote_side=[primary_id], backref="killed_units")

    unit_type_id = Column(Integer, ForeignKey("datapack.unit_type.primary_id"))
    unit_type = relationship(
        "unit_type",
        primaryjoin='object.unit_type_id==unit_type.primary_id',
        back_populates="objects")

    unit_born_events = relationship("unit_born_event", back_populates="unit")
    unit_done_events = relationship("unit_done_event", back_populates="unit")
    unit_init_events = relationship("unit_init_event", back_populates="unit")
    death_event = relationship(
        "unit_died_event", primaryjoin="unit_died_event.unit_id==object.primary_id",
        back_populates="unit",
    )
    kill_events = relationship(
        "unit_died_event",
        primaryjoin="unit_died_event.killing_unit_id==object.primary_id",
        back_populates="killing_unit",
    )
