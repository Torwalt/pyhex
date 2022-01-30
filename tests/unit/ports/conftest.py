import fastapi
import pytest
from fastapi import testclient

from src import main


@pytest.fixture
def app():
    return main.app


@pytest.fixture
def test_client(app: fastapi.FastAPI):
    return testclient.TestClient(app)
