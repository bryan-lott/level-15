from flask import Flask, render_template
from collections import namedtuple
app = Flask(__name__)


Card = namedtuple("Card", ['id', 'name', 'text'])


@app.route("/")
def hello():
    return "Hello World from Flask - live edits!"


@app.route("/browse")
def browse():
    cards = all_cards()
    return render_template('browse.html', all_cards=cards)

@app.route("/edit/<int:card_id>")
def edit(card_id):
    return render_template('edit_card.html', card_id=card_id)


@app.route("/link")
def link():
    pass


@app.route("/create", methods=['POST'])
def create():
    pass


@app.route("/delete", methods=['POST'])
def delete():
    pass


@app.route("/view/<int:card_id>")
def view(card_id):
    return render_template('view_card.html', card_id=card_id)

def all_cards():
    """Queries neo4j to grab all cards"""
    # TODO: do databasey stuff here to get all nodes
    return [Card(id=1, name='test card', text='this is only a test...')]

if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host='0.0.0.0', debug=True, port=8080)
