from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_pos_tag():
    response = client.post("/pos_tag", json={"text": "Hello, world!"})
    assert response.status_code == 200
    assert "pos_tags" in response.json()
    expected_tags = [["Hello", "NNP"], [",", ","], ["world", "NN"], ["!", "."]]
    assert response.json()["pos_tags"] == expected_tags
