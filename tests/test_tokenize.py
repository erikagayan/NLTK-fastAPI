from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_tokenize():
    response = client.post("/tokenize", json={"text": "Hello, world!"})
    assert response.status_code == 200
    assert "tokens" in response.json()
    assert response.json()["tokens"] == ["Hello", ",", "world", "!"]
