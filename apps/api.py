from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask.views import MethodView

from werkzeug import secure_filename

from sqlalchemy import insert
from database.draft import Draft
from database.project import Project

from forms.draft import DraftForm
from forms.project import ProjectForm

from apps.auth import login_required

api = Blueprint('api', __name__)


# /new
class NewProject(MethodView):

	html = 'new_project.html'
	decorators = [login_required]

	def get(self):
		return render_template(self.html)

	def post(self):
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
			return redirect(url_for('api.new'))


# /<project_name>/new
class NewDraft(MethodView):

	html = 'new.html'
	decorators = [login_required]

	def get(self, project_name):
		data = Project.get_by_name(project_name)
		return render_template(self.html, data=data)

	def post(self, project_name):
		form = DraftForm(request.form)

		#project_id, draft_version, headings, description, file
		if form.validate():
			Draft.add_draft(
				form.id.data,
				1,
				form.headings.data,
				form.description.data,
				form.file.data
			)
			file = request.files['file']
			file.save('uploads/' + secure_filename(file.filename))
			flash('success')
			return redirect(url_for('api.view_project', project_name=project_name))

		else:
			flash('fail')
			return redirect(url_for('api.new_draft', project_name=project_name))


@api.route('/<project_name>')
@login_required
def view_project(project_name):

	project = Project.get_by_name(project_name)
	drafts = Draft.get_by_id(project.id)

	return render_template('view.html', project=project, drafts=drafts)


@api.route('/<project_name>/<headings>')
@login_required
def view_draft(project_name, headings):

	project = Project.get_by_name(project_name)
	draft = Draft.get_by_id_headings(project.id, headings)

	return render_template('view_draft.html', project=project, draft=draft)


@api.route('/search/<project_name>')
@login_required
def search_project(project_name):

	result = Project.search(project_name)

	return render_template('search.html', result=result)


api.add_url_rule('/new', view_func=NewProject.as_view('new'))
api.add_url_rule('/<project_name>/new', view_func=NewDraft.as_view('new_draft'))