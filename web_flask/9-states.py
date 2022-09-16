#!/usr/bin/python3
"""
Write a script that starts a Flask web application
"""

from flask import Flask
from flask import render_template
from models import storage
from models import State

app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(exception=None):
    storage.close()


@app.route('/states', strict_slashes=False)
@app.route('/states/<state_id>', strict_slashes=False)
def states_id(state_id):
    if state_id:
        state_id = "State." + state_id
    return render_template("9-states.html",
                           dict=storage.all(State), state_id=state_id)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
