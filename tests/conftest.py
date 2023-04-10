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
