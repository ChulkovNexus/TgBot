from dataclasses import dataclass
from typing import List

from dataclasses_jsonschema import JsonSchemaMixin

from models.worktype import WorkType

@dataclass
class Building(JsonSchemaMixin):
    id: int
    name: str
    description: str
    requiredBuildingsIds: List[int]
    allowedWorkTypes: List[WorkType]
    energyOutput: int = 0
    energyRequered: int = 0
    temperatureOtput: int = 0

