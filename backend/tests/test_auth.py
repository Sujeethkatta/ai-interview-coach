"""
Authentication tests.
"""
import pytest
from fastapi.testclient import TestClient

from app.main import app
from app.core.security import hash_password, create_access_token
from app.db.session import SessionLocal
from app.models.user import User

client = TestClient(app)


@pytest.fixture(autouse=True)
def setup():
    """Setup test database."""
    db = SessionLocal()
    # Clean up
    db.query(User).delete()
    db.commit()
    db.close()
    yield


def test_register_user():
    """Test user registration."""
    response = client.post(
        "/api/v1/auth/register",
        json={
            "email": "test@example.com",
            "username": "testuser",
            "password": "TestPassword123",
        },
    )
    assert response.status_code == 200
    assert response.json()["email"] == "test@example.com"


def test_login_user():
    """Test user login."""
    # Create user
    db = SessionLocal()
    user = User(
        email="test@example.com",
        username="testuser",
        hashed_password=hash_password("TestPassword123"),
    )
    db.add(user)
    db.commit()
    db.close()
    
    # Login
    response = client.post(
        "/api/v1/auth/login",
        json={
            "email": "test@example.com",
            "password": "TestPassword123",
        },
    )
    assert response.status_code == 200
    assert "access_token" in response.json()


def test_login_invalid_credentials():
    """Test login with invalid credentials."""
    response = client.post(
        "/api/v1/auth/login",
        json={
            "email": "test@example.com",
            "password": "WrongPassword",
        },
    )
    assert response.status_code == 401
