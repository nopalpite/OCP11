
def test_known_email_login(client, valid_club):
    #Arrange
    known_email = valid_club.email
    
    #Act
    response = client.post('/showSummary', data={'email': known_email})
    
    #Assert
    assert response.status_code == 200

def test_unknown_email_login(client):
    #Arrange
    unknown_email = "unknown@random.com"

    #Act
    response = client.post('/showSummary', data={'email': unknown_email})
    
    #Assert
    assert response.status_code == 404
    assert "no club found with this email" in str(response.data)

def test_empty_email_login(client):
    #Arrange
    empty_email = ""

    #Act
    response = client.post('/showSummary', data={'email': empty_email})
    
    #Assert
    assert response.status_code == 400
    assert "please enter an email" in str(response.data)