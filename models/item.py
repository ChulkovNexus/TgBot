from dataclasses import dataclass
from typing import List

from models.bodyparts import BodyParts
from models.itemgroup import ItemGroup
from models.weartype import WearType

@dataclass
class Item:
    id: int
    name: str
    descr: str
    weight: int
    accuracy: int
    range: int
    minDps: int
    maxDps: int
    temperatureModificator: int
    itemGroup: ItemGroup
    wearType: WearType
    accuracyRangeFactor: float
    rangeDamageFactor: float
    armor: float
    maxHealth: int
    bodyPartCoverage: List[BodyParts]
    effects: str
