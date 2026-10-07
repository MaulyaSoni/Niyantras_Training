import os

# os.environ["DATABASE_URL"] = "sqlite://"

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from main import app
from database.db import get_db
from database.schema import Base, Users, URL
from dependencies.context import current_user_context
import operations.tasks as tasks


# # Shared in-memory SQLite database.
# TEST_DATABASE_URL = "sqlite://"

engine = create_engine(
    TEST_DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)

TestingSessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False,
)


@pytest.fixture
def db(monkeypatch):
    Base.metadata.create_all(bind=engine)

    session = TestingSessionLocal()

    # Background tasks must use a separate session,
    # but the same test database.
    monkeypatch.setattr(tasks, "SessionLocal", TestingSessionLocal)

    try:
        yield session
    finally:
        session.rollback()
        session.close()
        Base.metadata.drop_all(bind=engine)


@pytest.fixture
def client(db):
    def override_get_db():
        yield db

    app.dependency_overrides[get_db] = override_get_db

    with TestClient(app) as test_client:
        yield test_client

    app.dependency_overrides.pop(get_db, None)


@pytest.fixture
def test_user(db):
    user = Users(
        username="pytest_user",
        email="pytest@example.com",
        hashed_password="test_password",
        user_role="User",
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    return user


@pytest.fixture
def authenticated_client(client, db, test_user):
    def override_current_user_context():
        return {
            "db": db,
            "current_user": test_user,
        }

    app.dependency_overrides[current_user_context] = (
        override_current_user_context
    )

    yield client

    app.dependency_overrides.pop(current_user_context, None)


@pytest.fixture
def created_url(db, test_user):
    url = URL(
        url="https://example.com/test-page",
        short_link="TEST123",
        owner_id=test_user.userid,
        total_clicks=0,
    )

    db.add(url)
    db.commit()
    db.refresh(url)

    return url