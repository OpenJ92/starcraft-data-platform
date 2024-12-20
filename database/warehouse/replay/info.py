from sqlalchemy import Column, Integer, BigInteger, Float, Text, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from database.base import Base
from database.warehouse.replay.map import map


class info(Base):
    __tablename__ = "info"
    __table_args__ = {"schema": "replay"}

    primary_id = Column(Integer, primary_key=True)

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

    map_id = Column(Integer, ForeignKey("replay.map.primary_id"))
    map = relationship("map", back_populates="replays")

    basic_command_events = relationship("basic_command_event", back_populates="info")
    chat_events = relationship("chat_event", back_populates="info")
    player_stats_events = relationship("player_stats_event", back_populates="info")
    player_leave_events = relationship("player_leave_event", back_populates="info")
    player_setup_events = relationship("player_setup_event", back_populates="info")
    upgrade_complete_events = relationship("upgrade_complete_event", back_populates="info")
    unit_born_events = relationship("unit_born_event", back_populates="info")
    unit_done_events = relationship("unit_done_event", back_populates="info")
    unit_init_events = relationship("unit_init_event", back_populates="info")
    unit_died_events = relationship("unit_died_event", back_populates="info")
