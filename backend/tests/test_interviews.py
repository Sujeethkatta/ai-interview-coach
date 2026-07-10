"""
Interview API tests.
"""
import pytest
from fastapi.testclient import TestClient
from uuid import uuid4

from app.main import app
from app.core.security import create_access_token, hash_password
from app.db.session import SessionLocal
from app.models.user import User

client = TestClient(app)


@pytest.fixture
def auth_token():
    """Create test user and return auth token."""
    db = SessionLocal()
    user = User(
        email="test@example.com",
        username="testuser",
        hashed_password=hash_password("TestPassword123"),
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    token = create_access_token(str(user.id))
    db.close()
    return token


def test_start_interview(auth_token):
    """Test starting an interview."""
    response = client.post(
        "/api/v1/interviews/start",
        headers={"Authorization": f"Bearer {auth_token}"},
        json={
            "interview_type": "technical",
            "difficulty": "intermediate",
        },
    )
    assert response.status_code == 200
    data = response.json()
    assert data["interview_type"] == "technical"
    assert data["difficulty"] == "intermediate"


def test_list_interviews(auth_token):
    """Test listing interviews."""
    response = client.get(
        "/api/v1/interviews/list",
        headers={"Authorization": f"Bearer {auth_token}"},
    )
    assert response.status_code == 200
    data = response.json()
    assert "interviews" in data
    assert "total" in data
