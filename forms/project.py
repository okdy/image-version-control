from wtforms import Form, StringField, DateField
from wtforms.validators import Length


class ProjectForm(Form):
	name = StringField('name', [Length(min=1, max=30)])
	description = StringField('description', [Length(max=140)])
	deadline = DateField('deadline')