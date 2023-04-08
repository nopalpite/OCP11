from models.club import Club
from models.competition import Competition
from server import clubs, competitions

def test_book_with_enough_points(client, valid_club, valid_competition):
    #Arrange
    club = valid_club
    competition = valid_competition
    places  = club.points - 1 if club.points > 0 else 0
    
    #Act
    response = client.post('/purchasePlaces', data={
    'competition': competition.name,
    'club': club.name,
    'places': places
    })
    
    #Assert
    assert response.status_code == 200
    assert "Great-booking complete!" in str(response.data)

    
def test_book_with_more_than_available_points(client, club_with_10_points, valid_competition):
    #Arrange
    club = club_with_10_points
    competition = valid_competition
    
    #Act
    response = client.post('/purchasePlaces', data={
    'competition': competition.name,
    'club': club.name,
    'places': 14
    })
    
    #Assert
    assert response.status_code == 400
    assert "Not enough points!"  in str(response.data)