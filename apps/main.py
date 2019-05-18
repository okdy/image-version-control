from flask import Blueprint, render_template
from sqlalchemy import desc

from database.db import session
from database.project import Project
from database.draft import Draft

from sqlalchemy.orm.exc import NoResultFound

main = Blueprint('main', __name__)


@main.route('/')
def home():
	projects = session.query(Project).order_by(desc(Project.id)).all()

	return render_template('index.html', projects=projects)