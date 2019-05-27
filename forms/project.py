from wtforms import (
	Form,
	IntegerField,
	StringField,
	FileField,
	DateField,
	validators as val
)


class ProjectForm(Form):
	name = StringField('name', [val.Length(min=1, max=30)])
	description = StringField('description', [val.Length(max=140)])
	deadline = DateField('deadline')