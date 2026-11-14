from main import app
from fastapi.testclient import TestClient

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200


def test_countries():
    response = client.get("/countries")
    assert response.status_code == 200
    assert sorted(response.json()) == ["England", "France", "Germany", "Italy", "Peru", "Portugal", "Spain"]


def test_cities_for_spain():
    """Return Spain's cities from the cities endpoint."""
    response = client.get("/countries/Spain/cities")
    assert response.status_code == 200
    assert response.json() == ["Seville"]