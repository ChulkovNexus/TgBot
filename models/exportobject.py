import dataclasses
from dataclasses import dataclass
from enum import Enum
from typing import List, Optional
import json

from models.biome import Biome
from models.event import Event
from models.item import Item
from models.worktype import WorkType
from models.worldmap import WorldMap
from utils import nested_dataclass


@nested_dataclass
class ExportObject:
    biomes: List[Biome]
    events: List[Event]
    workTypes: List[WorkType]
    items: List[Item]
    map: WorldMap


class ExportObjectJSONEncoder(json.JSONEncoder):
    def default(self, o):
        if dataclasses.is_dataclass(o):
            return dataclasses.asdict(o)
        if isinstance(o, Enum):
            return o.name

        return super().default(o)


class ExportObjectJSONDecoder(json.JSONDecoder):
    def default(self, o):
        if dataclasses.is_dataclass(o):
            return dataclasses.asdict(o)
        if isinstance(o, Enum):
            return o.name

        return super().default(o)

