from models.club import Club
from models.competition import Competition
import server


def test_book_with_enough_points(client, mocker):
    # Arrange
    clubs = [Club("club_name", "club@email.com", 20)]
    competitions = [Competition("competition_name", "2020-03-27 10:00:00", 30)]
    form = {
        'competition': "competition_name",
        'club': "club_name",
        'places': 10
    }

    # Act
    mocker.patch.object(server, 'clubs', clubs)
    mocker.patch.object(server, 'competitions', competitions)
    response = client.post('/purchasePlaces', data=form)

    # Assert
    assert response.status_code == 200
    assert "Great-booking complete!" in str(response.data)


def test_book_with_more_than_available_points(client, mocker):
    # Arrange
    clubs = [Club("club_name", "club@email.com", 20)]
    competitions = [Competition("competition_name", "2020-03-27 10:00:00", 30)]
    form = {
        'competition': "competition_name",
        'club': "club_name",
        'places': 25
    }

    # Act
    mocker.patch.object(server, 'clubs', clubs)
    mocker.patch.object(server, 'competitions', competitions)
    response = client.post('/purchasePlaces', data=form)

    # Assert
    assert response.status_code == 400
    assert "Not enough points!" in str(response.data)


def test_book_with_more_than_twelve_points(client, mocker):
    # Arrange
    clubs = [Club("club_name", "club@email.com", 20)]
    competitions = [Competition("competition_name", "2020-03-27 10:00:00", 30)]
    form = {
        'competition': "competition_name",
        'club': "club_name",
        'places': 13
    }

    # Act
    mocker.patch.object(server, 'clubs', clubs)
    mocker.patch.object(server, 'competitions', competitions)
    response = client.post('/purchasePlaces', data=form)

    # Assert
    assert response.status_code == 400
    assert "No more than 12 points!" in str(response.data)


def test_book_with_more_than_competition_places(client, mocker):
    # Arrange
    clubs = [Club("club_name", "club@email.com", 20)]
    competitions = [Competition("competition_name", "2020-03-27 10:00:00", 10)]
    form = {
        'competition': "competition_name",
        'club': "club_name",
        'places': 11
    }

    # Act
    mocker.patch.object(server, 'clubs', clubs)
    mocker.patch.object(server, 'competitions', competitions)
    response = client.post('/purchasePlaces', data=form)

    # Assert
    assert response.status_code == 400
    assert "Not enough places available!" in str(response.data)
