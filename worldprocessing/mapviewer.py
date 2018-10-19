from models.maptile import MapTile
from worldprocessing import cache
import random


def _get_range_depended_text(next_cell, view_range):
    if not isinstance(next_cell, MapTile):
        raise TypeError(f"Forward reference must be a MapTile -- got {next_cell!r}")
    else:
        if view_range == 1:
            return next_cell.nextTileCustomDescription
        else:
            return next_cell.customFarBehindText


def _get_current_tile_text(map_tile):
    if map_tile is None:
        return " -not filled- "
    return map_tile.thisTileCustomDescription


def _see_throw_condition(next_cell):
    return next_cell.canSeeThrow is not False


def _get_unpassable_defaults(tile: MapTile):
    biome = next(b for b in cache.memoryCache.biomes if b.id == tile.biomeId)
    result = random.choice(biome.unpassabledefaults)
    if result is None:
        return ""
    else:
        return result


class MapViewer:
    vision_range = 2

    def _get_side_text(self, tile: MapTile, view_range: int, func):
        text = ''
        next_cell = func(view_range)
        if next_cell is None:
            text += _get_unpassable_defaults(tile)
        elif next_cell.isUnpassable:
            text += _get_unpassable_defaults(next_cell)
            if _see_throw_condition(next_cell) & self.vision_range > view_range:
                text += " " + self._get_side_text(tile, view_range+1, func)
        else:
            text += _get_range_depended_text(next_cell, view_range) or " -not filled- "
            if _see_throw_condition(next_cell) & self.vision_range > view_range:
                text += ", " + random.choice(cache.memoryCache.map.defaultBehindsTexts) + " " + self._get_side_text(tile, view_range + 1, func)
        return text

    def get_north_text(self, map_tile):
        text = random.choice(cache.memoryCache.map.defaultTopMovingTexts) or ""
        text += self._get_side_text(map_tile, 1, lambda v_range: cache.memoryCache.map.getTopCell(map_tile.posX, map_tile.posY, v_range))
        return ''

    def get_east_text(self, map_tile):
        text = random.choice(cache.memoryCache.map.defaultRightMovingTexts) or ""
        text += self._get_side_text(map_tile, 1, lambda v_range: cache.memoryCache.map.getRightCell(map_tile.posX, map_tile.posY, v_range))
        return text

    def get_west_text(self, map_tile):
        text = random.choice(cache.memoryCache.map.defaultLeftMovingTexts) or ""
        text += self._get_side_text(map_tile, 1, lambda v_range: cache.memoryCache.map.getLeftCell(map_tile.posX, map_tile.posY, v_range))
        return text

    def get_south_text(self, map_tile):
        text = random.choice(cache.memoryCache.map.defaultBottomMovingTexts) or ""
        text += self._get_side_text(map_tile, 1, lambda v_range: cache.memoryCache.map.getBottomCell(map_tile.posX, map_tile.posY, v_range))
        return text
