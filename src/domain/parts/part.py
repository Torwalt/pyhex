from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class Test:
    """
    Represents tests that can be run on `Parts` during the manufacturing
    process to ensure their quality.

    id: Unique identifier of a Test.
    part_id: Unique identifier of the part that was tested.
    timestamp: The time when the Test was run.
    successful: Indicate whether the Test ran successfully.
    data: Additional information about the Test instance (type, name, notes, etc.).
    """

    id: int
    part_id: int
    successful: bool
    data: dict
    timestamp: datetime = field(default_factory=datetime.utcnow)


@dataclass
class Part:
    """
    Represents a part of the physical objects that can be manufactured or used in the
    manufacturing process (bolts, screws, speaker drivers and cabinets, cables,
    fully assembled modules, ...).

    id: Unique identifier of a Part.
    name: The name of a Part.
    tests: Test that were run on a Part.
    updated_at: The timestamp when a Part was last modified.
    """

    id: int
    name: str
    tests: list[Test]
    updated_at: datetime = field(default_factory=datetime.utcnow)
