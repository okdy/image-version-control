from sqlalchemy import Column
from sqlalchemy.types import Integer, String, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Project(Base):
	__tablename__ = 'project'

	id = Column(Integer, primary_key=True)
	name = Column(String)
	description = Column(String)
	start_time = Column(TIMESTAMP)
	deadline = Column(TIMESTAMP)