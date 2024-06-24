import pytest
from flask import url_for
from app.models import Product

@pytest.mark.usefixtures("mock_create_product", "mock_create_price")
def test_create_product(client):
    
    product_data = {
        'name' : 'supatee_test',
        'description' : 'supatee_test_description',
        'price' : 399,
    }

    response = client.post(
        '/api/products',
        data=product_data,
        follow_redirects=True
    )

    assert response.status_code == 200
    
    product = Product.query.filter_by(name='supatee_test').first()
    assert product is not None
    assert product.name == 'supatee_test'
    assert product.description == 'supatee_test_description'
    assert product.price == 399
    assert product.stripe_price_id == 'price_test_id'
    assert product.stripe_product_id == 'prod_test_id'