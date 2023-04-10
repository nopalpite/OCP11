from models.club import Club
import server


def test_known_email_login(client, mocker):
    # Arrange
    clubs = [Club("club_name", "club@email.com", 20)]
    form = {'email': "club@email.com"}

    # Act
    mocker.patch.object(server, 'clubs', clubs)
    response = client.post('/showSummary', data=form)

    # Assert
    assert response.status_code == 200


def test_unknown_email_login(client, mocker):
    # Arrange
    clubs = [Club("club_name", "club@email.com", 20)]
    form = {'email': "unknown@email.com"}

    # Act
    mocker.patch.object(server, 'clubs', clubs)
    response = client.post('/showSummary', data=form)

    # Assert
    assert response.status_code == 404
    assert "no club found with this email" in str(response.data)


def test_empty_email_login(client, mocker):
    # Arrange
    clubs = [Club("club_name", "club@email.com", 20)]
    form = {'email': ""}

    # Act
    mocker.patch.object(server, 'clubs', clubs)
    response = client.post('/showSummary', data=form)

    # Assert
    assert response.status_code == 400
    assert "please enter an email" in str(response.data)
