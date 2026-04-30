from fastapi.testclient import TestClient
from src.app import app

# Arrange-Act-Assert (AAA) pattern example for FastAPI

def test_root_endpoint():
    # Arrange
    client = TestClient(app)

    # Act
    response = client.get("/", follow_redirects=True)

    # Assert
    assert response.status_code == 200
    assert b"Mergington High School" in response.content

# Add more tests following the AAA pattern as needed
