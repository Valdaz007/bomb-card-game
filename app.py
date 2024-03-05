from flask import Flask, render_template, redirect, session
import requests
from threelip.threelip import Deck

app = Flask(__name__)
app.secret_key = "secret_key"

@app.route('/')
def index():
    if "deck_id" in session:
        return render_template('index.html', deck=session['deck_id'])
    else:
        response = requests.get("https://www.deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1").json()
        if response['success']:
            session['deck_id'] = response['deck_id']
            print(session['deck_id'])
            deck = Deck(response['deck_id'])
            return render_template('index.html', deck=deck.get_DeckID())
        else:
            return redirect(url('error'))

@app.route('/error')
def error():
    return render_template('error.html')

@app.route('/deck_id')
def deckID():
    if 'deck_id' in session:
        return render_template('deckid.html', deck=session['deck_id'])
    else:
        return render_template('error.html')

@app.route('/draw')
def draw():
    response = requests.get(f'https://www.deckofcardsapi.com/api/deck/{session["deck_id"]}/draw/?count=2').json()
    return render_template('deckid.html', deck=session['deck_id'], response=response)

@app.route('/return')
def redeck():
    response = requests.get(f'https://www.deckofcardsapi.com/api/deck/{session["deck_id"]}/return/').json()
    return render_template('deckid.html', deck=session['deck_id'], response=response)

@app.route('/pile')
def deckPile():
    response = requests.get(f'https://www.deckofcardsapi.com/api/deck/{session["deck_id"]}/draw/?count=1').json()
    card = response['cards'][0]['code']
    response = requests.get(f'https://www.deckofcardsapi.com/api/deck/{session["deck_id"]}/pile/discard/add/?cards={card}').json()
    return render_template('deckid.html', deck=session['deck_id'], response=response)


if __name__ == "__main__":
    app.run(debug=True)