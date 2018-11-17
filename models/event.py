from dataclasses import dataclass
from typing import List

from utils import nested_dataclass


@nested_dataclass
class Event:
    id: int
    eventText: str
    probability: float
    probabilityFromAttentionFactor: float
    probabilityFromStealthFactor: float
    isGlobal: bool
    eventText: List[str]
