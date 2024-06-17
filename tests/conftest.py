import pytest
from app import create_app, db
from app.models import Product

@pytest.fixture(scope='module')
def app():
    app = create_app('testing')    
    with app.app_context():
        db.create_all()
        yield app
    db.session.remove()
    db.drop_all()

@pytest.fixture(scope='module')
def client(app):
    return app.test_client()

@pytest.fixture
def init_database(app):
    with app.app_context():
        product = Product(name='Test Product', description='A product for testing', price=999)
        db.session.add(product)
        db.session.commit()
        yield db
        db.session.remove()
        db.drop_all()

