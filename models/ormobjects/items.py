from sqlalchemy import Column, Integer, Sequence, Boolean

from http_app import Base


class Item(Base):

    __tablename__ = 'items'

    id = Column(Integer, primary_key=True)
    item_type = Column(Integer)
    stack_count = Column(Integer)
    stack_weight = Column(Integer)
    damaged = Column(Integer)
    is_dressed = Column(Boolean)
