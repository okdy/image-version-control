from flask import Blueprint, render_template
from database.db import session
from database.project import Project

from sqlalchemy.orm.exc import NoResultFound

api = Blueprint('api', __name__)

@api.route('/test/<int:project_id>')
def test(project_id):
	
	try:
		data = session.query(Project).filter_by(id=project_id).one()

		return data.name

	except NoResultFound:
		return "no data"