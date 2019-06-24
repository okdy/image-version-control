from flask import abort
from sqlalchemy import Column
from database.db import session

from sqlalchemy.types import Integer, String, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm.exc import NoResultFound

Base = declarative_base()


class Project(Base):
	__tablename__ = 'project'

	id = Column(Integer, primary_key=True)
	name = Column(String)
	description = Column(String)
	start_time = Column(TIMESTAMP)
	deadline = Column(TIMESTAMP)

	def get_by_id(prject_id):
		try:
			return session.query(Project).filter_by(id=prject_id).one()

		except NoResultFound:
			return abort(404)

	def get_by_name(project_name):
		try:
			return session.query(Project).filter_by(name=project_name).one()

		except NoResultFound:
			return abort(404)

	def add_project(name, description, deadline):
		new_project = Project(
			name=name,
			description=description,
			deadline=deadline
		)
		session.add(new_project)
		session.commit()

	def search(project_name):
		return session.query(Project).filter(
			Project.name.like('%' + project_name +'%')
		).all()
