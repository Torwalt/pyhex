from unittest import mock

from fastapi import testclient

from src import main
from src.domain.parts import service
from tests.unit.domain import factories


def test__parts__get_all_parts():
    m_p = mock.Mock(service.PartService)
    p = factories.PartFactory.create()
    t = factories.TestFactory.create(part_id=p.id)
    p.tests.append(t)

    m_p.get_parts.return_value = [p]
    app = main.create_app(m_p)
    test_client = testclient.TestClient(app)

    resp = test_client.get("/api/parts")

    assert resp.status_code == 200
    assert resp.json() == [
        {
            "id": p.id,
            "name": p.name,
            "modified_timestamp": p.updated_at.isoformat(),
            "tests": [
                {
                    "id": t.id,
                    "part_id": p.id,
                    "successful": t.successful,
                    "data": t.data,
                    "timestamp": t.timestamp.isoformat(),
                }
            ],
        }
    ]


def test__parts__create_part():
    m_p = mock.Mock(service.PartService)
    p = factories.PartFactory.create()

    m_p.create_part.return_value = p
    app = main.create_app(m_p)
    test_client = testclient.TestClient(app)

    data = {"name": "test"}
    resp = test_client.post("/api/parts/", json=data)

    assert resp.status_code == 201
    assert resp.json() == {
        "id": p.id,
        "name": p.name,
        "modified_timestamp": p.updated_at.isoformat(),
        "tests": [],
    }


def test__parts__create_test():
    m_p = mock.Mock(service.PartService)
    p = factories.PartFactory.create()
    t = factories.TestFactory.create(part_id=p.id)
    m_p.create_test.return_value = t

    app = main.create_app(m_p)
    test_client = testclient.TestClient(app)

    data = {
        "part_id": p.id,
        "successful": t.successful,
        "data": t.data,
        "timestamp": t.timestamp.isoformat(),
    }
    resp = test_client.post("/api/parts/tests", json=data)

    assert resp.status_code == 201
    assert resp.json() == {
        "id": t.id,
        "part_id": p.id,
        "successful": t.successful,
        "data": t.data,
        "timestamp": t.timestamp.isoformat(),
    }
