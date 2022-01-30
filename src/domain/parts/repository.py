from dataclasses import dataclass
from typing import Protocol

from src.domain.parts import action, part


@dataclass
class PartRepositoryError(Exception):
    """
    Generic repository error.
    """

    msg: str


@dataclass
class PartRepositoryNotFoundError(PartRepositoryError):
    """
    Entity was not found in repository.
    """


class PartRepository(Protocol):
    def get_all(self) -> list[part.Part]:
        ...

    def create(self, cp: action.CreatePart) -> part.Part:
        ...

    def delete_by_id(self, id: int) -> None:
        ...

    def create_test(self, ct: action.CreateTest) -> part.Test:
        ...
