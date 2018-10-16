from dataclasses import dataclass
from typing import List


@dataclass
class MapTile:

    id: int
    posX: int
    posY: int
    biomeId: int
    buildingsIds: List[int]
    eventsIds: List[int]
    availableWorkTypesIds: List[int]
    thisTileCustomDescription: str
    nextTileCustomDescription: str
    customFarBehindText: str
    editedAfterBiomeSetted: bool
    canSeeThrow: bool
    isUnpassable: bool
    moveSpeedFactor: float
    stealthFactor: float
    additionalMoveSpeed: int
    additionalStealth: int
