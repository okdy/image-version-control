from wtforms import Form, IntegerField, StringField, FileField
from wtforms.validators import Length


class DraftForm(Form):
	id = IntegerField('id')
	headings = StringField('headings', [Length(min=1)])
	description = StringField('description', [Length(max=140)])
	file = FileField('file')