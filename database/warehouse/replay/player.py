from sqlalchemy import Column, Integer, Text, Boolean, BigInteger, ForeignKey
from sqlalchemy.orm import relationship

from database.base import Base

class player(Base):
    __tablename__ = "player"
    __table_args__ = {"schema": "replay"}

    primary_id = Column(Integer, primary_key=True)

    sid = Column(Integer)
    team_id = Column(Integer)
    is_human = Column(Boolean)
    is_observer = Column(Boolean)
    is_referee = Column(Boolean)
    region = Column(Text)
    subregion = Column(Integer)
    toon_id = Column(BigInteger)
    uid = Column(Integer)
    clan_tag = Column(Text)
    name = Column(Text)
    combined_race_levels = Column(BigInteger)
    highest_league = Column(Integer)
    pid = Column(Integer)
    result = Column(Text)
    pick_race = Column(Text)
    play_race = Column(Text)

    id = Column(Integer)

    owned_objects = relationship( "object", primaryjoin="object.owner_id==player.primary_id", back_populates="owner")
    killed_objects = relationship("object", primaryjoin="object.killing_player_id==player.primary_id", back_populates="killing_player")

    info_id = Column(Integer, ForeignKey("replay.info.primary_id"))
    replay = relationship("info", back_populates="players")

    basic_command_events = relationship("basic_command_event", back_populates="player")
    chat_events = relationship("chat_event", back_populates="player")
    player_stats_events = relationship("player_stats_event", back_populates="player")
    player_leave_events = relationship("player_leave_event", back_populates="player")
    unit_born_events = relationship("unit_born_event", back_populates="unit_controller")
    unit_died_events = relationship("unit_died_event", back_populates="killing_player")
    upgrade_complete_events = relationship("upgrade_complete_event", back_populates="player")
