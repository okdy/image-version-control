from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask.views import MethodView

from functools import wraps
from werkzeug import secure_filename

from sqlalchemy import insert
from database.account import Account

from forms.auth import LoginForm, NewAccountForm


auth = Blueprint('auth', __name__)


# login required
def login_required(f):
	@wraps(f)
	def wrap(*args, **kwargs):
		if 1:
			return 'please login'
		return f(*args, **kwargs)

	return wrap


# account/login
class Login(MethodView):

	template_name = 'auth/login.html'

	def get(self):
		return render_template(self.template_name)

	def post(self):
		form = LoginForm(request.form)

		if form.validate():
			a = Account.login(form.email.data, form.password.data)

			if a is None:
				return 'none user'
			else:
				return 'yes user'

		else:
			flash('fail')
			return redirect(url_for('auth.login'))


# account/new
class New(MethodView):

	template_name = 'auth/new.html'

	def get(self):
		return render_template(self.template_name)

	def post(self):
		form = NewAccountForm(request.form)

		if form.validate():
			Account.new(form.name.data, form.email.data, form.password.data)
			flash('success')
			return redirect(url_for('main.home'))

		else:
			flash('fail')
			return redirect(url_for('auth.new'))


auth.add_url_rule('/login', view_func=Login.as_view('login'))
auth.add_url_rule('/new', view_func=New.as_view('new'))