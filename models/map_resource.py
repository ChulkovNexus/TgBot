from dataclasses import dataclass


@dataclass
class MapResource:
    id: int
    name: str
    description: str