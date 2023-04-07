import pytest
from models.club import Club


def test_known_email_login(client):
    #Arrange
    known_email = "john@simplylift.co"
    
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
    assert "email not found" in str(response.data)

def test_empty_email_login(client):
    #Arrange
    empty_email = "empty@random.com"

    #Act
    response = client.post('/showSummary', data={'email': empty_email})
    
    #Assert
    assert response.status_code == 400
    assert "please enter an email" in str(response.data)