from flask import Blueprint, render_template

api = Blueprint('api', __name__)

@api.route('/test/<int:data>')
def test(data):
	return str(data)