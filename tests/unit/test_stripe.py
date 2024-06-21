import pytest

def test_config(client):
    response = client.get('/stripe/config')
    assert response.status_code == 200
    response_data = response.get_json()
    assert response_data == {"public_key": 'test_public_key'}

def test_create_checkout(client, mock_create_checkout_session):
    payload = {
            'price_id': 'price_test_id'
        }
    response = client.post(
        '/stripe/create-checkout-session',
        json=payload
    )
    import pdb; pdb.set_trace()
    assert response.status_code == 200
    response_data = response.get_json()
    assert response_data == {'sessionId' : 'test_session_id'}
    assert 'price' in mock_create_checkout_session['line_items'][0]
    assert mock_create_checkout_session['payment_method_types'] == ['card']
    assert mock_create_checkout_session['mode'] == 'payment'
    assert mock_create_checkout_session['line_items'][0]['price'] == 'price_test_id'
    assert mock_create_checkout_session['success_url'] == 'http://localhost/success?session_id=test_session_id'  
    