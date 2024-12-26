from sqlalchemy import Column, Integer, Text, LargeBinary, ForeignKey, and_
from sqlalchemy.future import select
from sqlalchemy.orm import relationship

from collections import defaultdict

from database.warehouse.replay.info import info
from database.warehouse.replay.player import player
from database.warehouse.replay.user import user
from database.warehouse.datapack.unit_type import unit_type
from database.inject import Injectable
from database.base import Base


class object(Injectable, Base):
    __tablename__ = "object"
    __table_args__ = {"schema": "replay"}

    primary_id = Column(Integer, primary_key=True)

    id = Column(Integer)
    started_at = Column(Integer)
    finished_at = Column(Integer)
    died_at = Column(Integer)
    name = Column(Text)

    info_id = Column(Integer, ForeignKey("replay.info.primary_id"))
    replay = relationship("info", back_populates="objects")

    owner_id = Column(Integer, ForeignKey("replay.player.primary_id"))
    owner = relationship(
        "player",
        primaryjoin="object.owner_id==player.primary_id",
        back_populates="owned_objects",)


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

    @classmethod
    @property
    def __tableschema__(self):
        return "replay"

    @classmethod
    async def process(cls, replay, session):
        _objects = []
        for _, obj in replay.objects.items():
            data = cls.get_data(obj)
            parents = await cls.process_dependancies(obj, replay, session)
            if not parents:
                continue

            _objects.append(cls(**data, **parents))

        session.add_all(_objects)
        breakpoint()


    @classmethod
    async def process_dependancies(cls, obj, replay, session):
        _unit, _info, _player = obj._type_class, replay.filehash, obj.owner
        if not (_unit and _info and _player and _unit.race != "Neutral"):
            return None

        unit_statement = select(unit_type).where(
                and_(unit_type.release_string == replay.release_string, unit_type.id == _unit.id))
        unit_result = await session.execute(unit_statement)
        _unit = unit_result.scalar()

        info_statement = select(info).where(info.filehash == _info)
        info_result = await session.execute(info_statement)
        _info = info_result.scalar()

        user_statement = select(user).where(user.uid == _player.detail_data.get("bnet").get("uid"))
        user_result = await session.execute(user_statement)
        _user = user_result.scalar()

        player_statement = select(player).where(
                and_(player.info_id == _info.primary_id, player.user_id == _user.primary_id))
        player_result = await session.execute(player_statement)
        _player = player_result.scalar()

        parents = defaultdict(lambda:None)
        parents["unit_type_id"] = _unit.primary_id
        parents["info_id"] = _info.primary_id
        parents["owner_id"] = _player.primary_id

        return parents

    columns = \
        { "id"
        , "started_at"
        , "finished_at"
        , "died_at"
        , "name"
        }
