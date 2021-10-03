from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_get():
    response = client.get("/")
    assert response.status_code == 200


def test_post():
    test_value = "value"
    response = client.post("/post", json={
        "some_value": test_value
    })
    assert response.status_code == 200
    json = response.json()
    assert json["some_value"] == test_value
