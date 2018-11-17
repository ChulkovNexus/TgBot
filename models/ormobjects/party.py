from sqlalchemy import Sequence, Integer, Column, ARRAY

from http_app import Base


class Party(Base):
    __tablename__ = 'parties'

    id = Column(Integer, primary_key=True)
    owner = Column(Integer)
    mates = Column("mates_ids", ARRAY(Integer))