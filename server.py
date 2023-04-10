from flask import Flask, render_template, request, redirect, flash, url_for
from datetime import datetime
from data.data_loader import load_clubs, load_competitions


app = Flask(__name__)
app.secret_key = "something special"

clubs = load_clubs()
competitions = load_competitions()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/showSummary', methods=['POST'])
def show_summary():
    email = request.form['email']
    club = next((c for c in clubs if c.email == email), None)
    if club is not None:
        return render_template('welcome.html', club=club, competitions=competitions)
    else:
        if email == "":
            flash("please enter an email")
            return render_template('index.html'), 400
        else:
            flash("no club found with this email")
            return render_template('index.html'), 404


@app.route('/book/<competition>/<club>')
def book(competition, club):
    found_club = [c for c in clubs if c.name == club][0]
    found_competition = [c for c in competitions if c.name == competition][0]
    if found_club and found_competition:
        if found_competition.date < datetime.today().strftime('%Y-%m-%d %H:%M:%S'):
            flash("This competition is over!")
            return render_template('welcome.html', club=found_club, competitions=competitions), 400
        else:
            return render_template('booking.html', club=found_club, competition=found_competition)
    else:
        flash("Something went wrong-please try again")
        return render_template('welcome.html', club=club, competitions=competitions)


@app.route('/purchasePlaces', methods=['POST'])
def purchase_places():
    competition = next((c for c in competitions if c.name ==
                       request.form['competition']), None)
    club = next((c for c in clubs if c.name == request.form['club']), None)
    places_required = int(request.form['places'])
    if places_required > club.points:
        flash("Not enough points!")
        return render_template('welcome.html', club=club, competitions=competitions), 400
    elif places_required > competition.number_of_places:
        flash("Not enough places available!")
        return render_template('welcome.html', club=club, competitions=competitions), 400
    elif places_required > 12:
        flash("No more than 12 points!")
        return render_template('welcome.html', club=club, competitions=competitions), 400
    else:
        competition.number_of_places = int(
            competition.number_of_places) - places_required
        flash('Great-booking complete!')
        return render_template('welcome.html', club=club, competitions=competitions)


# TODO: Add route for points display


@app.route('/logout')
def logout():
    return redirect(url_for('index'))
