from flask import Blueprint

bp = Blueprint('oa', __name__, url_prefix='/')


@bp.route('/')
def index():
	pass