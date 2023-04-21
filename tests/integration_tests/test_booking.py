def test_login_booking_logout(client):
    # Test login
    form = {'email': "john@simplylift.co"}
    response = client.post('/showSummary', data=form)
    assert response.status_code == 200

    # Test booking
    form = {'competition': "Fail Classic",
            'club': "Simply Lift",
            'places': 2
            }
    response = client.get('/book/Fail Classic/Simply Lift')
    assert response.status_code == 200
    response = client.post('/purchasePlaces', data=form)
    assert "Great-booking complete!" in str(response.data)

    # Test logout
    response = client.get('/logout', follow_redirects=True)
    assert response.status_code == 200
    print(response.data)
    assert "Welcome to the GUDLFT Registration Portal!" in str(response.data)
