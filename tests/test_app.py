import pytest
import sys
import os

# Solution fiable pour les imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.app import app


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_home_route(client):
    response = client.get("/")
    assert response.status_code == 200
    data = response.get_json()
    assert data["message"] == "Hello, World!"
    assert data["status"] == "success"


def test_health_route(client):
    response = client.get("/health")
    assert response.status_code == 200
    data = response.get_json()
    assert data["status"] == "healthy"


def test_get_existing_user(client):
    response = client.get("/users/1")
    assert response.status_code == 200
    data = response.get_json()
    assert data["id"] == 1
    assert data["name"] == "John Doe"


def test_get_unknown_user(client):
    response = client.get("/users/999")
    assert response.status_code == 200
    data = response.get_json()
    assert data["id"] == 999


def test_get_invalid_user(client):
    response = client.get("/users/0")
    assert response.status_code == 404
    data = response.get_json()
    assert "error" in data


def test_calculate_route(client):
    response = client.get("/calculate/10/5")
    assert response.status_code == 200
    data = response.get_json()
    assert data["sum"] == 15
    assert data["difference"] == 5
    assert data["product"] == 50
