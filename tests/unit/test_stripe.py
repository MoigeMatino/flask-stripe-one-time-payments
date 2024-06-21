def test_config(client):
    response = client.get('/stripe/config')
    assert response.status_code == 200
    response_data = response.get_json()
    assert response_data == {"public_key": 'test_public_key'}

