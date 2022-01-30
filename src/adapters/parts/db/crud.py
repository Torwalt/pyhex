import datetime
from typing import List

from sqlalchemy import delete, select
from sqlalchemy.orm import Session

from src.adapters.parts.db import models
from src.domain.parts import action, part


class PartRepository:
    """
    Handle the retrieval of part objects from a RDBS.
    """

    def __init__(self, db: Session) -> None:
        self.db = db

    def get_all(self) -> List[part.Part]:
        """
        Retrieve all Part objects from the db.
        """
        stmt = select(models.Part).join(models.Part.tests, isouter=True)
        db_parts: List[models.Part] = self.db.execute(stmt).scalars().all()
        return [to_part(p, []) for p in db_parts]

    def create(self, cp: action.CreatePart) -> part.Part:
        """
        Create a Part object in the db.
        """
        p_db = from_part(cp)
        self.db.add(p_db)
        self.db.commit()

        p = to_part(p_db, [])
        return p

    def create_test(self, ct: action.CreateTest) -> part.Test:
        """
        Create a Test object in the db.
        """
        t_db = from_test(ct)
        self.db.add(t_db)
        self.db.commit()
        return to_test(t_db)

    def delete_by_id(self, id: int) -> None:
        """
        Delete a Part object from the db.
        """
        stmt = delete(models.Part).where(models.Part.id == id)
        self.db.execute(stmt)
        self.db.commit()


def to_part(p: models.Part, tests: list[models.Test]) -> part.Part:
    """
    Create a domain Part object from a database Part representation.
    """
    return part.Part(id=p.id, name=p.name, updated_at=p.modified_timestamp, tests=tests)  # type: ignore


def from_part(p: action.CreatePart) -> models.Part:
    """
    Create a database Part representation from a domain Part object.
    """
    return models.Part(name=p.name, modified_timestamp=datetime.datetime.now())


def to_test(t: models.Test) -> part.Test:
    """
    Create a domain Test object from a database Test representation.
    """
    return part.Test(
        id=t.id,
        part_id=t.part_id,  # type: ignore
        successful=t.successful,  # type: ignore
        data=t.data,  # type: ignore
        timestamp=t.timestamp,  # type: ignore
    )


def from_test(t: action.CreateTest) -> models.Test:
    """
    Create a database Test representation from a domain Test object.
    """
    return models.Test(
        part_id=t.part_id,
        successful=t.successful,
        data=t.data,
        timestamp=t.timestamp,
    )
