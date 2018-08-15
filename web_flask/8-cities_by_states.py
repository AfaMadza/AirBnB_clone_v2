#!/usr/bin/python3
"""
This module contains a function that starts a Flask web app
"""
from flask import Flask, render_template
from models import storage


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/states_list')
def states_list():
    """
    Returns State data from database and insert into template
    """
    state_inst = storage.all('States').values()
    state_data = dict([state.name, state.id] for state in state_inst)
    return render_template('7-states_list.html', state_data=state_data)


@app.route('/cities_by_states')
def display_cities():
    """
    Returns State data from database and insert into template
    """
    state_inst = storage.all('States').values()
    state_data = dict([state.name, state] for state in state_inst)
    return render_template('8-cities_by_states.html', state_data=state_data)


@app.teardown_appcontext
def teardown_db(exception):
    """
    Handles teardown of app context
    """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
