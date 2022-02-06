from flask import render_template, url_for
from flask_login import current_user

from flask import Blueprint
bp = Blueprint('index', __name__)


@bp.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@bp.route('/jobs', methods=['GET', 'POST'])
def jobs():
    return render_template('jobs.html')