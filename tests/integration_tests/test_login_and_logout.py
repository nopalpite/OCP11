def test_login_and_logout(client):
    # Test login
    form = {'email': "john@simplylift.co"}
    response = client.post('/showSummary', data=form)
    assert response.status_code == 200

    # Test logout
    response = client.get('/logout', follow_redirects=True)
    assert response.status_code == 200
    assert "Welcome to the GUDLFT Registration Portal!" in str(response.data)