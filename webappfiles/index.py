from flask import render_template, url_for
from flask_login import current_user

from flask import Blueprint
bp = Blueprint('index', __name__)


@bp.route('/', methods=['GET', 'POST'])
def index():
    return render_template('base.html')