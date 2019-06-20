from flask import Blueprint, render_template, flash, request
from flask import redirect, url_for, session, g
from flask.views import MethodView

from functools import wraps
from werkzeug import secure_filename

from sqlalchemy import insert
from database.account import Account

from forms.auth import LoginForm, NewAccountForm

from resources.flash import AUTH


auth = Blueprint('auth', __name__)


# login required
def login_required(f):
	@wraps(f)
	def wrap(*args, **kwargs):
		if 'logined' not in session:
			flash(AUTH['PLEASE_LOGIN'])
			return redirect(url_for('auth.login'))
		else:
			g.user = Account.get_data(session['user_id'])
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
			user = Account.login(form.email.data, form.password.data)

			if user is None:
				flash(AUTH['LOGIN_FAIL'])
				return redirect(url_for('auth.login'))
				
			else:
				session['logined'] = True
				session['user_id'] = user.id
				return redirect(url_for('main.home'))

		else:
			flash(AUTH['LOGIN_FAIL'])
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
			flash(AUTH['NEW_SUCCESS'])
			return redirect(url_for('main.home'))

		else:
			return redirect(url_for('auth.new'))


auth.add_url_rule('/login', view_func=Login.as_view('login'))
auth.add_url_rule('/new', view_func=New.as_view('new'))