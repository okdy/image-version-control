from wtforms import Form, StringField
from wtforms.validators import Length, Email


class LoginForm(Form):
	email = StringField('email', [Email()])
	password = StringField('password')


class NewAccountForm(Form):
	name = StringField('name', [Length(min=1, max=10)])
	email = StringField('email', [Email()])
	password = StringField('password')