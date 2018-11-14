from dataclasses import dataclass
from typing import List

from http_app import Session
from models.ormobjects.buildings import BuildingDto
from models.ormobjects.user import User
from worldprocessing import cache


@dataclass
class MapTile:

    def __init__(self,
                id: int,
                posX: int,
                posY: int,
                biomeId: int,
                buildingsIds: List[int],
                eventsIds: List[int],
                availableWorkTypesIds: List[int],
                editedAfterBiomeSetted: bool,
                isUnpassable: bool,
                mapResources: List[int],
                moveSpeedFactor: float,
                stealthFactor: float,
                additionalMoveSpeed: int,
                additionalStealth: int,
                thisTileCustomDescription: str = "",
                nextTileCustomDescription: str = "",
                customFarBehindText: str = "",
                canSeeThrow: bool = False):
        self.id = id
        self.posX = posX
        self.posY = posY
        self.biomeId = biomeId
        self.eventsIds = eventsIds
        self.availableWorkTypesIds = availableWorkTypesIds
        self.editedAfterBiomeSetted = editedAfterBiomeSetted
        self.isUnpassable = isUnpassable
        self.mapResources = mapResources
        self.moveSpeedFactor = moveSpeedFactor
        self.stealthFactor = stealthFactor
        self.additionalMoveSpeed = additionalMoveSpeed
        self.additionalStealth = additionalStealth
        self.thisTileCustomDescription = thisTileCustomDescription
        self.nextTileCustomDescription = nextTileCustomDescription
        self.customFarBehindText = customFarBehindText
        self.canSeeThrow = canSeeThrow

        def init_database_buildings():
            sess = Session()
            for buildingId in buildingsIds:
                sess.add(BuildingDto(buildingId, posX, posY))

        init_database_buildings()

    def get_available_buildings(self, user: User):
        sess = Session()
        database_buildings = sess.query(BuildingDto).filter_by(map_tile_x=self.posX, map_tile_y=self.posY).all()
        available_buildings = []
        for building_dto in database_buildings:
            cache_building = next((building for building in cache.memoryCache.buildings if building.id == building_dto.cache_building_id), None)
            if cache_building and cache_building.owners.__contains__(user.id):
                available_buildings.append(cache_building)

        return available_buildings


