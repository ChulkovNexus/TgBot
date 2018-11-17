from models.maptile import MapTile
from utils import random_or_none
from worldprocessing import cache


class MapViewer:
    vision_range = 2

    def _get_side_text(self, tile: MapTile, view_range: int, func):
        text = ''
        next_cell = func(view_range)
        if next_cell is None:
            text += self._get_unpassable_defaults(tile)
        elif next_cell.isUnpassable:
            text += self._get_unpassable_defaults(next_cell)
            if self._see_throw_condition(next_cell) & self.vision_range > view_range:
                text += " " + self._get_side_text(tile, view_range+1, func)
        else:
            text += self._get_range_depended_text(next_cell, view_range) or " -not filled- "
            if self._see_throw_condition(next_cell) & self.vision_range > view_range:
                text += ", " + random_or_none(cache.memoryCache.map.defaultBehindsTexts) + " " + self._get_side_text(tile, view_range + 1, func)
        return text

    def get_nearest_description(self, tile: MapTile):
        text = self._get_current_tile_text(tile)
        loking_for_way_prefix = random_or_none(cache.memoryCache.map.defaultLookingForWayPrefix) or ""
        text += '{0} {1}, {2}, {3}, {4}, '.format(loking_for_way_prefix, self.get_north_text(tile),
                                                  self.get_east_text(tile), self.get_south_text(tile),
                                                  self.get_west_text(tile))
        return text

    def get_north_text(self, map_tile):
        text = random_or_none(cache.memoryCache.map.defaultTopMovingTexts) or ""
        text += self._get_side_text(map_tile, 1, lambda v_range: cache.memoryCache.map.getTopCell(map_tile.posX, map_tile.posY, v_range))
        return ''

    def get_east_text(self, map_tile):
        text = random_or_none(cache.memoryCache.map.defaultRightMovingTexts) or ""
        text += self._get_side_text(map_tile, 1, lambda v_range: cache.memoryCache.map.getRightCell(map_tile.posX, map_tile.posY, v_range))
        return text

    def get_west_text(self, map_tile):
        text = random_or_none(cache.memoryCache.map.defaultLeftMovingTexts) or ""
        text += self._get_side_text(map_tile, 1, lambda v_range: cache.memoryCache.map.getLeftCell(map_tile.posX, map_tile.posY, v_range))
        return text

    def get_south_text(self, map_tile):
        text = random_or_none(cache.memoryCache.map.defaultBottomMovingTexts) or ""
        text += self._get_side_text(map_tile, 1, lambda v_range: cache.memoryCache.map.getBottomCell(map_tile.posX, map_tile.posY, v_range))
        return text

    def _get_range_depended_text(self, next_cell, view_range):
        if not isinstance(next_cell, MapTile):
            raise TypeError(f"Forward reference must be a MapTile -- got {next_cell!r}")
        else:
            if view_range == 1:
                return next_cell.nextTileCustomDescription
            else:
                return next_cell.customFarBehindText

    def _get_current_tile_text(self, map_tile):
        if map_tile is None:
            return " -not filled- "
        return map_tile.thisTileCustomDescription

    def _see_throw_condition(self, next_cell):
        return next_cell.canSeeThrow is not False

    def _get_unpassable_defaults(self, tile: MapTile):
        biome = next((b for b in cache.memoryCache.biomes if b.id == tile.biomeId), None)
        result = random_or_none(biome.unpassabledefaults) if biome else None
        return result or ""
