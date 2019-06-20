from flask import Blueprint, render_template
from sqlalchemy import desc

from database.db import session
from database.project import Project
from database.draft import Draft

from sqlalchemy.orm.exc import NoResultFound

from apps.auth import login_required

main = Blueprint('main', __name__)


@main.route('/')
@login_required
def home():
	projects = session.query(Project).order_by(desc(Project.id)).all()

	return render_template('index.html', projects=projects)