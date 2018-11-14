from models.bodyparts import BodyParts
from models.ormobjects.items import Item
from models.ormobjects.user import User, BodyPartStatus


def add_maxweight_debuff(user):
    max_weight_body_part_status = BodyPartStatus()
    max_weight_body_part_status.body_part = BodyParts.Body
    max_weight_body_part_status.text
    user.statuses += max_weight_body_part_status

