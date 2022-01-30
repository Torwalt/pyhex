import pytest

from src import config
from src.adapters.parts.db import database, models

# def get_db() -> SessionLocal:
#     try:
#         db = SessionLocal()
#         yield db
#     finally:
#         db.close()


@pytest.fixture
def test_settings():
    return config.Settings()


@pytest.fixture
def test_db(test_settings: config.Settings):
    db = database.create_db(test_settings)
    db.query(models.Part).delete()
    db.commit()
    yield db
