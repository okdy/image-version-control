from flask import abort
from sqlalchemy import Column
from database.db import session

from sqlalchemy.types import Integer, String, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm.exc import NoResultFound

Base = declarative_base()


class Draft(Base):
	__tablename__ = 'draft'

	id = Column(Integer, primary_key=True)
	project_id = Column(Integer)
	draft_version = Column(Integer)
	headings = Column(String)
	description = Column(String)
	file = Column(String)
	date = Column(TIMESTAMP)

	def get_by_id(id):
		return session.query(Draft).filter_by(project_id=id).all()

	def get_by_id_headings(id, headings):
		try:
			return session.query(Draft).filter_by(project_id=id, headings=headings).one()

		except NoResultFound:
			abort(404)

	def add_draft(project_id, draft_version, headings, description, file):
		new_draft = Draft(
			project_id=project_id,
			draft_version=draft_version,
			headings=headings,
			description=description,
			file=file
		)
		session.add(new_draft)
		session.commit()