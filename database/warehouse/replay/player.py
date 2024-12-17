from sqlalchemy import Column, Integer, Text, Boolean, BigInteger, ForeignKey
from sqlalchemy.orm import relationship

from database.base import Base

class player(Base):
    __tablename__ = "player"
    __table_args__ = {"schema": "replay"}

    __id__ = Column(Integer, primary_key=True)

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

    owner_objects = relationship( "object", primaryjoin="object.__owner__==player.__id__", back_populates="owner")
    killed_objects = relationship("object", primaryjoin="object.__killing_player__==player.__id__", back_populates="killing_player")

    __info__ = Column(Integer, ForeignKey("replay.info.__id__"))
    replay = relationship("info", back_populates="players")
