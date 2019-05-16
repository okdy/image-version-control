from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from settings import *

# database connect URI
URI = "{}://{}:{}@{}/{}?charset=utf8".format(DB_ENGINE, DB_USER, DB_PASS, DB_HOST, DB_DB)

# sqlalchemy application
engine = create_engine(URI)

Session = sessionmaker(bind=engine)
session = Session()