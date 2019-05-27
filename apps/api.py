from flask import Blueprint, render_template, request, redirect, url_for, flash

from sqlalchemy import insert

from database.project import Project
from database.draft import Draft

from forms.draft import DraftForm
from forms.project import ProjectForm


api = Blueprint('api', __name__)


@api.route('/new', methods=['GET', 'POST'])
def new_project():

	if request.method == 'GET':

		return render_template('new_project.html')

	elif request.method == 'POST':

		form = ProjectForm(request.form)

		if form.validate():
			Project.add_project(
				form.name.data,
				form.description.data,
				form.deadline.data
			)
			flash('success')
			return redirect('/')

		else:
			flash('fail')
			return redirect(url_for('api.new_project'))


@api.route('/<project_name>')
def view_project(project_name):

	project = Project.get_by_name(project_name)

	drafts = Draft.get_all_draft()

	return render_template('view.html', project=project, drafts=drafts)


@api.route('/<project_name>/new', methods=['GET', 'POST'])
def new_draft(project_name):
	
	if request.method == 'GET':

		data = Project.get_by_name(project_name)

		return render_template('new.html', data=data)

	elif request.method == 'POST':

		form = DraftForm(request.form)

		if form.validate():
			return 'success'

		else:
			return 'fail'