import functools
import random
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from LOC.db import get_db

bp = Blueprint('home', __name__, url_prefix='/home')

@bp.route("", methods=('GET', 'POST'))
def home():
    
    session['session_id'] = random.randint(0, 1000000)

    return render_template('home/home.html')

@bp.route("/<int:pool_id>", methods=('GET', 'POST'))
def share():
    #Share the Player pool with the people in team formation. 
    #This is the page that will be shared with the team members.
    #Voting on Team Generation method among the team members.
    #Creating a pool 
    return