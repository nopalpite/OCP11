import json
from models.club import Club
from models.competition import Competition

def load_clubs():
    with open('./data/clubs.json') as c:
         clubs_data = json.load(c)['clubs']
         return list(map(lambda club: Club(**club), clubs_data))

def load_competitions():
    with open('./data/competitions.json') as c:
         competitions_data = json.load(c)['competitions']
         return list(map(lambda competition: Competition(**competition), competitions_data))
     