from models.bodyparts import BodyParts
from models.ormobjects.bodypartstatuses import BodyPartStatus


def add_maxweight_debuff(user):
    max_weight_body_part_status = BodyPartStatus()
    max_weight_body_part_status.body_part = BodyParts.Body
    max_weight_body_part_status.text = "too much weight"
    user.statuses += max_weight_body_part_status
