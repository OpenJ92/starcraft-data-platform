from sqlalchemy import Column, Integer, Text, ForeignKey
from sqlalchemy.future import select
from sqlalchemy.exc import IntegrityError, OperationalError
from sqlalchemy.orm import relationship

from sqlalchemy.orm import relationship

from database.inject import Injectable
from database.base import Base

class user(Injectable, Base):
    __tablename__ = "user"
    __table_args__ = { "schema" : "replay" }

    primary_id = Column(Integer, primary_key=True)

    name = Column(Text)
    uid = Column(Integer)
    region = Column(Integer)
    subregion = Column(Integer)

    players = relationship("player", back_populates="user")

    @classmethod
    @property
    def __tableschema__(self):
        return "replay"

    @classmethod
    async def process(cls, replay, session):
        try:

            users = []
            for player in replay.players:
                if await cls.process_existence(player, session):
                    continue

                data = cls.get_data(player)
                users.append(cls(**data))

            session.add_all(users)

        except IntegrityError as e:
            await session.rollback()
            print(f"IntegrityError: {e.orig}")
            # Handle specific cases like unique constraint violations
        except OperationalError as e:
            await session.rollback()
            print(f"OperationalError: {e.orig}")
            # Handle deadlocks or connection issues
        except Exception as e:
            await session.rollback()
            print(f"Unexpected error: {e}")
            # Gracefully handle all other exceptions


    @classmethod
    async def process_existence(cls, obj, session):
        statement = select(cls).where(cls.uid == obj.uid)
        result = await session.execute(statement)
        return result.scalar()

    @classmethod
    def get_data(cls, obj):
        return { "name"      : obj.name
               , "uid"       : obj.detail_data.get("bnet").get("uid")
               , "region"    : obj.detail_data.get("bnet").get("region")
               , "subregion" : obj.detail_data.get("bnet").get("subregion")
               }

    columns = \
        { "name"
        , "uid"
        , "region"
        , "subregion"
        }

