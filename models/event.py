from dataclasses import dataclass
from typing import List


@dataclass
class Event:
    id: int
    eventText: str
    probability: float
    probabilityFromAttentionFactor: float
    probabilityFromStealthFactor: float
    isGlobal: bool
    eventText: List[str]
