from dataclasses import dataclass
from typing import List, Optional


@dataclass
class MapTile:

    id: int
    posX: int
    posY: int
    biomeId: int
    buildingsIds: List[int]
    eventsIds: List[int]
    availableWorkTypesIds: List[int]
    editedAfterBiomeSetted: bool
    isUnpassable: bool
    moveSpeedFactor: float
    stealthFactor: float
    additionalMoveSpeed: int
    additionalStealth: int
    thisTileCustomDescription: str = ""
    nextTileCustomDescription: str = ""
    customFarBehindText: str = ""
    canSeeThrow: bool = False
