from fastapi.testclient import TestClient
from toxic_server.http_server import app, cnt

client = TestClient(app)


def test_toxic():
    response = client.get("/predict", params={"text": "Listen here you dumbass"})
    assert response.status_code == 200
    assert response.json()["is_toxic"]


def test_non_toxic():
    response = client.get(
        "/predict", params={"text": "Thank you, have a pleasant evening"}
    )
    assert not response.json()["is_toxic"]
    assert response.status_code == 200


def test_counter():
    start = cnt._value.get()
    client.get("/predict", params={"text": "Thank you, have a pleasant evening"})
    client.get("/predict", params={"text": "Thank you, have a pleasant evening"})
    end = cnt._value.get()
    assert end > start


def test_metrics():
    response = client.get("/metrics")
    assert response.status_code == 200
