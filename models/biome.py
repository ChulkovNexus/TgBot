from dataclasses import dataclass
from typing import List

from models.biometile import BiomeTile
from utils import nested_dataclass


@dataclass
class Biome:
    id: int
    name: str
    color: int
    tiles: List[BiomeTile]
    unpassabledefaults: List[str]
