import pytest
from random import choice
from server import app, clubs, competitions
from models.club import Club
from models.competition import Competition

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

@pytest.fixture
def valid_club():
    return choice(clubs)

@pytest.fixture
def club_with_10_points():
    club = Club(name="club with 10 points", email="test@test.com", points=10)
    clubs.append(club)
    return club

@pytest.fixture
def club_with_50_points():
    club = Club(name="club with 50 points", email="test@test.com", points=50)
    clubs.append(club)
    return club

@pytest.fixture
def valid_competition():
    return choice(competitions)