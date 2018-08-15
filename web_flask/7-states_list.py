#!/usr/bin/python3
"""
This module contains a function that starts a Flask web app
"""
import sys
import os
sys.path.append(os.getcwd())
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/states_list')
def states_list():
    """
    Returns State data from database and insert into template
    """
    state_inst = storage.all('State').values()
    state_data = dict([state.name, state.id] for state in state_inst)
    return render_template('7-states_list.html', state_data=state_data)


@app.teardown_appcontext
def teardown_db(exception):
    """
    Handles teardown of app context
    """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
