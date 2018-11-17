from sqlalchemy import Integer, Sequence, Column, String, Boolean

from http_app import Base


class BodyPartStatus(Base):
    __tablename__ = 'body_part_status'

    id = Column(Integer, primary_key=True)
    text = Column(String(50))
    body_part = Column(String(20))
    effect_strenght = Column(Integer)
    is_modyfication = Column(Boolean)
    is_removed = Column(Boolean)

    speed_modificator = Column(Integer)
    stealth_modificator = Column(Integer)
    melee_fighter_modificator = Column(Integer)
    range_fighter_modificator = Column(Integer)
    labor_modificator = Column(Integer)
    constitution_modificator = Column(Integer)
    intelligence_work_modificator = Column(Integer)
    medic_modificator = Column(Integer)
