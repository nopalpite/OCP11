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


def test_book_future_competition(client, mocker):
    # Arrange
    clubs = [Club("club_name", "club@email.com", 20)]
    competitions = [Competition("competition_name", "2150-03-27 10:00:00", 50)]
    club_name = "club_name"
    competition_name = "competition_name"
    

    # Act
    mocker.patch.object(server, 'clubs', clubs)
    mocker.patch.object(server, 'competitions', competitions)
    response = client.get(f'/book/{competition_name}/{club_name}')

    # Assert
    assert response.status_code == 200
    

def test_book_past_competition(client, mocker):
    # Arrange
    clubs = [Club("club_name", "club@email.com", 20)]
    competitions = [Competition("competition_name", "1950-03-27 10:00:00", 50)]
    club_name = "club_name"
    competition_name = "competition_name"

    # Act
    mocker.patch.object(server, 'clubs', clubs)
    mocker.patch.object(server, 'competitions', competitions)
    response = client.get(f"/book/{competition_name}/{club_name}")

    # Assert
    assert response.status_code == 400
    assert "This competition is over!" in str(response.data)