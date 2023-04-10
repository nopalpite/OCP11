from models.club import Club
from models.competition import Competition


def test_create_club():
    # Arrange
    name = "club_name"
    email = "club_mail@gmail.com"
    points = 20

    # Act
    club = Club(name, email, points)

    # Assert
    assert club.name == name
    assert club.email == email
    assert club.points == points


def test_create_competition():
    # Arrange
    name = "competition_name"
    date = "2020-03-27 10:00:00"
    number_of_places = 20

    # Act
    competition = Competition(name, date, number_of_places)

    # Assert
    assert competition.name == name
    assert competition.date == date
    assert competition.number_of_places == number_of_places
