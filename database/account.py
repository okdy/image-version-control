from flask import abort

from database.db import session

from sqlalchemy import Column
from sqlalchemy.types import Integer, String, TIMESTAMP
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class Account(Base):
	__tablename__ = 'account'

	id = Column(Integer, primary_key=True)
	name = Column(String)
	email = Column(String)
	password = Column(String)
	date = Column(TIMESTAMP)

	def login(_email, _password):
		try:
			return session.query(Account).filter_by(email=_email, password=_password).one()
			
		except NoResultFound:
			return None

	def new(_name, _email, _password):
		account = Account(
			name = _name,
			email = _email,
			password = _password
		)
		session.add(account)
		session.commit()