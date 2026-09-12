import pytest

from app.main import create_app


@pytest.fixture
def app():
    return create_app(database_uri="sqlite:///:memory:")


@pytest.fixture
def client(app):
    return app.test_client()
