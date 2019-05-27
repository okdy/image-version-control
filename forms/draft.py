from wtforms import (
	Form,
	IntegerField,
	StringField,
	FileField,
	validators as val
)


class DraftForm(Form):
	id = IntegerField('id')
	headings = StringField('headings', [val.Length(min=1)])
	description = StringField('description', [val.Length(max=140)])
	file = FileField('file')