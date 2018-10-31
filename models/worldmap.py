from dataclasses import dataclass
from typing import List

from models.maptile import MapTile


@dataclass
class WorldMap:
    def __init__(self,
                 id: int,
                 defaultLeftMovingTexts: List[str],
                 defaultRightMovingTexts: List[str],
                 defaultLookingForWayPrefix: List[str],
                 beginningPhrases: List[str],
                 defaultTopMovingTexts: List[str],
                 defaultBottomMovingTexts: List[str],
                 defaultBehindsTexts: List[str],
                 defaultUnpassableText: List[str],
                 tiles: List[List[MapTile]]):

        self.id = id
        self.defaultLeftMovingTexts = defaultLeftMovingTexts
        self.defaultRightMovingTexts = defaultRightMovingTexts
        self.defaultLookingForWayPrefix = defaultLookingForWayPrefix
        self.beginningPhrases = beginningPhrases
        self.defaultTopMovingTexts = defaultTopMovingTexts
        self.defaultBottomMovingTexts = defaultBottomMovingTexts
        self.defaultUnpassableText = defaultUnpassableText
        self.defaultBehindsTexts = defaultBehindsTexts
        self.tiles = tiles

        for y in range(self.tiles.__len__()):
            for x in range(self.tiles[y].__len__()):
                cell = self.tiles[y][x]
                if isinstance(cell, dict):
                    self.tiles[y][x] = MapTile(**cell)

    def getTile(self, curr_x: int, curr_y: int):
        return self.tiles[curr_y][curr_x]

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
        if curr_y + count < self.tiles.__len__():
            return self.tiles[curr_y + count][curr_x]
        else:
            return None

    def getXLenght(self):
        return self.tiles[0].__len__() or 0

    def getYLenght(self):
        return self.tiles.__len__() or 0
