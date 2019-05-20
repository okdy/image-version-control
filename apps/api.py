from flask import Blueprint, render_template, request

from database.project import Project


api = Blueprint('api', __name__)

@api.route('/test/<int:project_id>')
def test(project_id):
	
	data = Project.get_by_id(project_id)

	return data.name


@api.route('/<project_name>')
def view_project(project_name):

	data = Project.get_by_name(project_name)

	return render_template('view.html', project=data)


@api.route('/new', methods=['GET', 'POST'])
def new_project():
	
	if request.method == 'GET':

		return render_template('new.html')

	elif request.method == 'POST':

		return 'post process'