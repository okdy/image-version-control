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