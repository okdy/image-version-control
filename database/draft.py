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

	def get_all_draft():
		return session.query(Draft).all()

	#project_id, draft_version headings, description, file
	def add_draft(project_id, draft_version headings, description, file):
		newDraft = Draft(
			project_id=project_id,
			draft_version=draft_version,
			headings=headings,
			description=description,
			file=file
		)
		session.add(newDraft)
		session.commit()