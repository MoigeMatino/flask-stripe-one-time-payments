import pytest
from app import create_app, db
from app.models import Product
from unittest.mock import patch, MagicMock

@pytest.fixture(scope='module')
def app():
    app = create_app('testing') 
    app.config['STRIPE_PUBLISHABLE_KEY'] = 'test_public_key'   
    app.config['BASE_URL'] = 'http://localhost/'
    app.config['STRIPE_SECRET_KEY'] = 'test_secret_key'
    with app.app_context():
        db.create_all()
        yield app
    
    with app.app_context():
        try:
            db.session.remove()
        except RuntimeError as e:
            print(f"RuntimeError during session removal: {e}")
        except Exception as e:
            print(f"Exception during session removal: {e}")
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

@pytest.fixture
def mock_create_price():
    mock_price = MagicMock()
    mock_price.id = "price_test_id"
    with patch("stripe.Price.create", return_value=mock_price):
        yield mock_price

@pytest.fixture
def mock_create_product():
    mock_product = MagicMock()
    mock_product.id = "prod_test_id"
    with patch("stripe.Product.create", return_value=mock_product):
        yield mock_product

@pytest.fixture
def mock_create_checkout_session():
    mock_response = {
        'id': 'test_session_id',
        'line_items': [
            {
                'price': 'price_test_id',
                'quantity': 1
            }
        ],
        'success_url': 'http://localhost/success?session_id=test_session_id',
        'cancel_url': 'http://localhost/cancelled',
        'payment_method_types': ['card'],
        'mode': 'payment'
    }
    with patch('stripe.checkout.Session.create', return_value=mock_response):
        yield mock_response
