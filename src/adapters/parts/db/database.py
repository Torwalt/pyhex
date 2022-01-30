from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session

from src.config import Settings


def create_db(s: Settings) -> Session:
    """
    Create the database access object.
    """
    engine = create_engine(s.SQLALCHEMY_DATABASE_URI, pool_pre_ping=True)
    sm = sessionmaker(autocommit=False, autoflush=False, future=True, bind=engine)
    session = sm()
    return session
