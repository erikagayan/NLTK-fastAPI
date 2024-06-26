from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_ner():
    response = client.post("/ner", json={"text": "Apple is located in Cupertino."})
    assert response.status_code == 200
    assert "entities" in response.json()
    assert any(entity["chunk"] == "Apple" for entity in response.json()["entities"])
