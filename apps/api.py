from flask import Blueprint, render_template, request

from sqlalchemy import insert

from database.project import Project
from database.draft import Draft

from forms.draft import DraftForm


api = Blueprint('api', __name__)


@api.route('/test/<int:project_id>')
def test(project_id):
	
	data = Project.get_by_id(project_id)

	return data.name


@api.route('/<project_name>')
def view_project(project_name):

	project = Project.get_by_name(project_name)

	drafts = Draft.get_all_draft()

	return render_template('view.html', project=project, drafts=drafts)


@api.route('/<project_name>/new', methods=['GET', 'POST'])
def new_project(project_name):
	
	if request.method == 'GET':

		data = Project.get_by_name(project_name)

		return render_template('new.html', data=data)

	elif request.method == 'POST':

		form = DraftForm(request.form)

		if form.validate():
			return 'success'

		else:
			return 'fail'