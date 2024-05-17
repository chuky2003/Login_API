import pytest

from server import app as asd, db

@pytest.fixture()
def app():
    app = asd

    with app.app_context():
        db.create_all()

    yield app

@pytest.fixture()
def client(app):
    return app.test_client()