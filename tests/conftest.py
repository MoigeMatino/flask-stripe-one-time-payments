import pytest
from app import create_app, db

@pytest.fixture(scope='module')
def app():
    app = create_app('testing')    
    with app.app_context():
        db.create_all()
        yield app
    db.session.remove()
    db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()

