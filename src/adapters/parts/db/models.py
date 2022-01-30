from datetime import datetime

from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.orm import as_declarative, declared_attr, relationship
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import JSON, Boolean


@as_declarative()
class Base(object):
    """A class describing the declarative base of the model classes

    Attributes
    ----------
    id: int
        The primary key of a an instance of Base
    """

    @declared_attr
    def __tablename__(cls) -> str:
        """A declared attribute for __tablename__

        The __tablename__ for a classed derived from Base is its own name in
        lowercase by default.

        Returns
        -------
        str
            The class name in lowercase
        """

        return str(cls.__name__.lower())  # type: ignore # noqa # pragma: no cover

    id = Column(Integer, primary_key=True)


class Part(Base):  # type: ignore
    """
    SQLAlchemy model describing domain object Parts.
    """

    name = Column(String, nullable=False)
    modified_timestamp = Column(DateTime(timezone=True), nullable=False)
    tests = relationship("Test", cascade="all, delete")

    def __init__(
        self,
        name: str,
        modified_timestamp: datetime,
    ):
        self.name = name
        self.modified_timestamp = modified_timestamp


class Test(Base):  # type: ignore
    """
    SQLAlchemy model describing domain object Test.
    """

    part_id = Column(
        "part_id", ForeignKey("part.id", ondelete="CASCADE"), nullable=False
    )
    successful = Column(Boolean, nullable=False)
    data = Column(JSON, nullable=False)
    timestamp = Column(DateTime(timezone=True), nullable=False)

    def __init__(
        self,
        part_id: int,
        successful: bool,
        data: dict,
        timestamp: datetime,
    ):
        self.part_id = part_id
        self.successful = successful
        self.data = data
        self.timestamp = timestamp
