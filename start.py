from flask import Flask

from apps.main import main
from apps.api import api

app = Flask(__name__)

app.register_blueprint(main)
app.register_blueprint(api)