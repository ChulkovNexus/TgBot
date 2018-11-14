from sqlalchemy import Sequence, Integer, Column, String

from http_app import Base


class BuildingDto(Base):
    __tablename__ = 'buildings'

    id = Column(String, Sequence('building_id_x_y_combination'), primary_key=True)
    owner = Column(Integer)
    map_tile_x = Column(Integer)
    map_tile_y = Column(Integer)
    cache_building_id = Column(Integer)
    current_work = Column(Integer)

    def __init__(self, map_tile_x, map_tile_y, cache_building_id):
        self.map_tile_x = map_tile_x,
        self.map_tile_y = map_tile_y,
        self.cache_building_id = cache_building_id
        self.id = '{}|{}|{}'.format(cache_building_id, map_tile_x, map_tile_y)
