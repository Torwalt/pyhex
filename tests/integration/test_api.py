from datetime import datetime

from fastapi import testclient

from src import main


def test__crud__part(test_db):
    ps = main.build_part_service(main.settings)
    app = main.create_app(ps)
    test_client = testclient.TestClient(app)

    part_name = "test"
    data = {"name": part_name}
    resp = test_client.post("/api/parts/", json=data)

    assert resp.status_code == 201
    part = resp.json()
    part_id = part["id"]
    assert part
    assert part["name"] == part_name

    resp = test_client.get("/api/parts")

    assert resp.status_code == 200
    parts = resp.json()
    assert len(parts) == 1
    assert parts[0]["name"] == part_name

    resp = test_client.delete(f"/api/parts/{part_id}")
    assert resp.status_code == 200


def test__create__test(test_db):
    ps = main.build_part_service(main.settings)
    app = main.create_app(ps)
    test_client = testclient.TestClient(app)

    part_name = "test"
    data = {"name": part_name}
    resp = test_client.post("/api/parts/", json=data)

    assert resp.status_code == 201
    part = resp.json()
    assert part
    part_id = part["id"]

    data = {
        "part_id": part_id,
        "successful": True,
        "data": {"note": "super successful"},
        "timestamp": datetime.utcnow().isoformat(),
    }
    resp = test_client.post("/api/parts/tests", json=data)

    assert resp.status_code == 201
    test = resp.json()
    assert test["id"]
    assert test["part_id"] == part_id
