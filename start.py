from flask import Flask

from apps.main import main
from apps.api import api
from apps.auth import auth

app = Flask(__name__)

app.secret_key = 'secret_key_for_debugging_only'

app.register_blueprint(main)
app.register_blueprint(api)
app.register_blueprint(auth, url_prefix='/account')