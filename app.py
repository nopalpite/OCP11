from flask import Flask
from data.data_loader import load_clubs, load_competitions


app = Flask(__name__)
app.secret_key = "something special"

clubs = load_clubs()
competitions = load_competitions()

from controllers.routes import *
if __name__ == '__name__':
    app.run()
