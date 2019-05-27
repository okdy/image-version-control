from flask import Flask

from apps.main import main
from apps.api import api

app = Flask(__name__)

app.secret_key = 'secret_key_for_debugging_only'

app.register_blueprint(main)
app.register_blueprint(api)