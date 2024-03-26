import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from LOC.db import get_db

bp = Blueprint('lobby', __name__, url_prefix='/lobby')

@bp.route('/createLobby')
def create_lobby():
    print('Creating Lobby')
    print(session['session_id']) 
    
      
    session_id = session.get('session_id')
    return redirect(url_for('lobby.start_lobby', lobby_id=session_id))

@bp.route('/<int:lobby_id>')
def start_lobby(lobby_id):
    print('Starting Lobby')
    players = ["player1", "player2", "player3", "player4", "player5",
               "player6", "player7", "player8", "player9", "player10"]
    return render_template('lobby/lobby.html', firsthalf=players[:5], secondhalf=players[5:])

#TODO: Add the ability to change the amount of players in the lobby.

@bp.route('/<int:lobby_id>/GameSurvey')
def game_survey(lobby_id):
    return render_template('lobby/game_survey.html')
