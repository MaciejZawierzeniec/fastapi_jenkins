from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_read_pokemon():
    response = client.get("/pokemon/pikachu")
    assert response.status_code == 200
    assert response.json()["name"] == "pikachu"

def test_pokemon_not_found():
    response = client.get("/pokemon/unknownpokemon")
    assert response.status_code == 404
  
