from dataclasses import dataclass
from typing import List


@dataclass
class BiomeTile:
    id: int
    probability: float
    moveSpeedFactor: float
    additionalMoveSpeed: int
    stealthFactor: float
    additionalStealth: int
    availableWorkTypesIds: List[int]
    possibleEventsIds: List[int]
    initialBuildingsIds: List[int]
    thisTileCustomDescription: str
    canSeeThrow: bool
    isUnpassable: bool
    nextTileCustomDescription: str
    customFarBehindText: str

