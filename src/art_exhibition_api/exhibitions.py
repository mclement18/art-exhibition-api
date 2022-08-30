from flask import Blueprint

from .db import all_exhibitions

bp = Blueprint('exhibitons', __name__, url_prefix='/exhibitions')

@bp.get('')
def index():
    return all_exhibitions(), 200
