from dataclasses import dataclass
from typing import List

from models.maptile import MapTile


@dataclass
class WorldMap:
    id: int
    defaultLeftMovingTexts: List[str]
    defaultRightMovingTexts: List[str]
    defaultLookingForWayPrefix: List[str]
    beginningPhrases: List[str]
    defaultTopMovingTexts: List[str]
    defaultBottomMovingTexts: List[str]
    defaultBehindsTexts: List[str]
    defaultUnpassableText: List[str]
    tiles: List[List[MapTile]]

