from sqlalchemy import Column, Integer, BigInteger, Float, Text, Boolean, DateTime
from sqlalchemy.orm import relationship

from database.base import Base
from database.warehouse.replay.map import map


class info(Base):
    __tablename__ = "info"
    __table_args__ = {"schema": "replay"}

    __id__ = Column(Integer, primary_key=True)

    filename = Column(Text)
    filehash = Column(Text)
    load_level = Column(Integer)
    speed = Column(Text)
    type = Column(Text)
    game_type = Column(Text)
    real_type = Column(Text)
    category = Column(Text)
    is_ladder = Column(Boolean)
    is_private = Column(Boolean)
    map_hash = Column(Text)
    region = Column(Text)
    game_fps = Column(Float)
    frames = Column(Integer)
    build = Column(Integer)
    base_build = Column(Integer)
    release_string = Column(Text)
    amm = Column(Integer)
    competitive = Column(Integer)
    practice = Column(Integer)
    cooperative = Column(Integer)
    battle_net = Column(Integer)
    hero_duplicates_allowed = Column(Integer)
    map_name = Column(Text)
    expansion = Column(Text)
    windows_timestamp = Column(BigInteger)
    unix_timestamp = Column(BigInteger)
    end_time = Column(DateTime)
    time_zone = Column(Float)
    start_time = Column(DateTime)
    date = Column(DateTime)

    players = relationship("player", back_populates="replay")
    objects = relationship("object", back_populates="replay")
