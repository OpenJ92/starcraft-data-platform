from sqlalchemy import Column, Integer, Text, LargeBinary, ForeignKey, and_
from sqlalchemy.future import select
from sqlalchemy.orm import relationship

from collections import defaultdict

from starcraft_data_orm.warehouse.replay.info import info
from starcraft_data_orm.warehouse.replay.object import object
from starcraft_data_orm.inject import Injectable
from starcraft_data_orm.warehouse.base import WarehouseBase

class unit_done_event(Injectable, WarehouseBase):
    __tablename__ = "unit_done_event"
    __table_args__ = {"schema": "events"}

    primary_id = Column(Integer, primary_key=True)

    frame = Column(Integer)
    second = Column(Integer)

    info_id = Column(Integer, ForeignKey("replay.info.primary_id"))
    info = relationship("info", back_populates="unit_done_events")

    unit_id = Column(Integer, ForeignKey("replay.object.primary_id"))
    unit = relationship("object", back_populates="unit_done_events")

    @classmethod
    @property
    def __tableschema__(self):
        return "events"

    @classmethod
    def process(cls, replay, session):
       events = replay.events_dictionary['UnitDoneEvent']

       _events = []
       for event in events:
           data = cls.get_data(event)
           parents =  cls.process_dependancies(event, replay, session)

           _events.append(cls(**data, **parents))

       session.add_all(_events)

    @classmethod
    def process_dependancies(cls, event, replay, session):
       _info, _unit = replay.filehash, event.unit_id
       parents = defaultdict(lambda:None)

       info_statement = select(info).where(info.filehash == _info)
       info_result =  session.execute(info_statement)
       _info = info_result.scalar()
       parents['info_id'] = _info.primary_id

       unit_statement = select(object).where(
               and_(object.info_id == _info.primary_id, object.id == _unit))
       unit_result =  session.execute(unit_statement)
       _unit = unit_result.scalar()
       parents['unit_id'] = _unit.primary_id

       return parents

    columns = \
        { "frame"
        , "second"
        }
