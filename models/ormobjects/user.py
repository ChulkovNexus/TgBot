from typing import List

from sqlalchemy import Column, Integer, Sequence, String, ARRAY, Boolean

from http_app import Base
from models.ormobjects.items import Item
from worldprocessing import body_parts_processing

skill_ranges = [(0, 1000), (1000, 3000), (3000, 6000), (6000, 10000), (10000, 15000), (15000, 21000), (21000, 28000),
                (28000, 36000), (36000, 45000), (45000, 55000), (55000, 66000), (66000, 78000), (78000, 91000),
                (91000, 105000), (105000, 120000), (120000, 136000), (136000, 153000), (153000, 171000),
                (171000, 190000), (190000, 210000)]

SKILL_NONE = 0
SKILL_SPEED = 0x0001
SKILL_STEALTH = 0x0002
SKILL_MELEE = 0x0003
SKILL_RANGE = 0x0004
SKILL_LABOR = 0x0005
SKILL_INT = 0x0006
SKILL_MEDIC = 0x0007


class BodyPartStatus(Base):
    __tablename__ = 'body_part_status'

    id = Column(Integer, Sequence('body_part_status_id_seq'), primary_key=True)
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


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    name = Column(String(50))
    fullname = Column(String(50))
    password = Column(String(50))
    party = Column(Integer)
    xPosition = Column(Integer)
    yPosition = Column(Integer)
    backpack_weight = Column(Integer)
    statuses = Column("dressed_items_ids", ARRAY(BodyPartStatus))
    dressed_items = Column("dressed_items_ids", ARRAY(Item))
    backpack = Column("backpack_items_ids", ARRAY(Item))

    # skills
    speed = Column(Integer)
    stealth = Column(Integer)
    melee_fighter = Column(Integer)
    range_fighter = Column(Integer)
    labor = Column(Integer)
    constitution = Column(Integer)
    intelligence_work = Column(Integer)
    medic = Column(Integer)

    def __repr__(self):
        return "<User(name='%s', fullname='%s', password='%s')>" % (self.name, self.fullname, self.password)

    def skill_exp_to_skill_level(self, exp):
        for idx, skill_range in enumerate(skill_ranges):
            if exp in skill_range:
                return idx
            else:
                return skill_ranges.__len__() - 1

    def get_userskill_by_id(self, id):
        if id == SKILL_SPEED:
            return self.speed
        if id == SKILL_STEALTH:
            return self.stealth
        if id == SKILL_MELEE:
            return self.melee_fighter
        if id == SKILL_RANGE:
            return self.range_fighter
        if id == SKILL_LABOR:
            return self.labor
        if id == SKILL_INT:
            return self.intelligence_work
        if id == SKILL_MEDIC:
            return self.medic
        return SKILL_NONE

    def get_current_work_id(self):
        return self.id

    def put_items_to_backstack(self, items: Item):
        self.backpack.append(items)
        self.append_max_weigth(self, items)

    def get_user_max_weight(self):
        return (self.constitution * 10) + 50

    def append_max_weigth(self, items: Item):
        self.backpack_weight += items.stack_weight
        if self.backpack_weight < self.get_user_max_weight():
            body_parts_processing.add_maxweight_debuff(self)

