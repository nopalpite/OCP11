from models.club import Club
import server


def test_points_display_board(client, mocker):
    # Arrange
    clubs = [
        Club(name="Simply Lift", email="john@simplylift.co", points=13),
        Club(name="Iron Temple", email="admin@irontemple.com", points=4),
        Club(name="She Lifts", email="kate@shelifts.co.uk", points=12),
    ]

    # Act
    mocker.patch.object(server, 'clubs', clubs)
    response = client.get('/board')
    
    # Assert
    response.status_code == 200
    