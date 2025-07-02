import pytest
from app import app

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_homepage_get(client):
    """Test GET request to the homepage"""
    response = client.get("/")
    assert response.status_code == 200
    assert b"Weather" in response.data  # Optional: check if 'Weather' appears in response

def test_homepage_post(client):
    """Test POST request with a sample city"""
    response = client.post("/", data={"city": "London"})
    assert response.status_code == 200
    assert b"London" in response.data or b"temperature" in response.data  # fuzzy check
