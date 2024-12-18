from sqlalchemy import Column, Integer, Text, LargeBinary
from sqlalchemy.orm import relationship

from database.base import Base


class map(Base):
    __tablename__ = "map"
    __table_args__ = {"schema": "replay"}

    __id__ = Column(Integer, primary_key=True)

    filename = Column(Text)
    filehash = Column(Text)
    name = Column(Text)
    author = Column(Text)
    description = Column(Text)
    website = Column(Text)
    minimap = Column(LargeBinary)

    replays = relationship("info", back_populates="map")
