import random

from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for, session
)
from werkzeug.exceptions import abort

from LOC.auth import login_required
from LOC.db import get_db

bp = Blueprint('account', __name__, url_prefix='/account')


@bp.route('', methods=("GET", "POST"))
@login_required
def account():

    return render_template('acc/account.html')

# TODO: Add Personality test into the account Page.
# TODO: Add the ability to change the password.
# TODO: Add viewing past matches win/loss record.
# Todo: add tips based on trends noticed in win lost record. 
    # i.e. "You seem to lose more when you play with a certain person, 
    # maybe you should try playing with someone else."
