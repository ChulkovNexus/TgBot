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

    def getRightCell(self, curr_x, curr_y, offset=1):
        if curr_x + offset < self.tiles[curr_y].__len__():
            return self.tiles[curr_y][curr_x + offset]
        else:
            return None

    def getLeftCell(self, curr_x: int, curr_y: int, count: int = 1):
        if curr_x - count >= 0:
            return self.tiles[curr_y][curr_x - count]
        else:
            return None

    def getTopCell(self, curr_x: int, curr_y: int, count: int = 1):
        if curr_y - count >= 0:
            return self.tiles[curr_y - count][curr_x]
        else:
            return None

    def getBottomCell(self, curr_x: int, curr_y: int, count: int = 1):
        if curr_y + count < self.tiles.size:
            return self.tiles[curr_y + count][curr_x]
        else:
            return None
