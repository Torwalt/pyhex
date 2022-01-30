from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class CreateTest:
    part_id: int
    successful: bool
    data: dict
    timestamp: datetime = field(default_factory=datetime.utcnow)


@dataclass
class CreatePart:
    name: str
