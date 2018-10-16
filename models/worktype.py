from dataclasses import dataclass
from models.worktypegroup import WorkTypeGroup


@dataclass
class WorkType:
    id: int
    description: str
    workTypeGroup: WorkTypeGroup
    baseWorkTime: int = 0
    stealthFactor: int = 0

