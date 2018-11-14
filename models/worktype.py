from dataclasses import dataclass
from typing import List

from models.worktypegroup import WorkTypeGroup


@dataclass
class WorkType:
    id: int
    description: str
    workTypeGroup: WorkTypeGroup
    resources: List[int]
    buildings: List[int]
    main_skill: int
    required_skill_level: int
    baseWorkTime: int = 0
    stealthFactor: int = 0

