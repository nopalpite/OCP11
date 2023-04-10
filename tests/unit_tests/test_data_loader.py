import json
from models.club import Club
from models.competition import Competition
from data.data_loader import load_clubs, load_competitions


def test_load_clubs(mocker):
    # Arrange
    expected_clubs = [
        Club(name="Simply Lift", email="john@simplylift.co", points=13),
        Club(name="Iron Temple", email="admin@irontemple.com", points=4),
        Club(name="She Lifts", email="kate@shelifts.co.uk", points=12),
    ]

    clubs_data = {"clubs": [
        {
            "name": "Simply Lift",
            "email": "john@simplylift.co",
            "points": "13"
        },
        {
            "name":  "Iron Temple",
            "email": "admin@irontemple.com",
            "points": "4"
        },
        {"name": "She Lifts",
         "email": "kate@shelifts.co.uk",
         "points": "12"
         }
    ]
    }

    # Act
    mocker.patch('builtins.open', mocker.mock_open(
        read_data=json.dumps(clubs_data)))
    result = load_clubs()

    # Assert
    assert result == expected_clubs


def test_load_competitions(mocker):
    # Arrange
    expected_competitions = [
        Competition(name="Spring Festival",
                    date="2020-03-27 10:00:00", number_of_places=25),
        Competition(name="Fall Classic",
                    date="2020-10-22 13:30:00", number_of_places=13)
    ]
    competitions_data = {
        "competitions": [
            {
                "name": "Spring Festival",
                "date": "2020-03-27 10:00:00",
                "number_of_places": "25"
            },
            {
                "name": "Fall Classic",
                "date": "2020-10-22 13:30:00",
                "number_of_places": "13"
            }
        ]
    }
    # Act
    mocker.patch('builtins.open', mocker.mock_open(
        read_data=json.dumps(competitions_data)))
    result = load_competitions()

    # Assert
    assert result == expected_competitions
