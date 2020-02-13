from flask import Flask
app = Flask(__name__)

from flask_sqlalchemy import SQLAlchemy

import os

if os.environ.get("HEROKU"):
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
else:
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///tehtava.db"
    app.config["SQLALCHEMY_ECHO"] = True

db = SQLAlchemy(app)


from application import views

from application.tehtava import models
from application.tehtava import views

from application.auth import models
from application.auth import views

from application.aihe import models



# Kirjautuminen

from application.auth.models import Kayttaja
from os import urandom
app.config["SECRET_KEY"] = urandom(32)

from flask_login import LoginManager
login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = "auth_kirjaudu"
login_manager.login_message = "Kirjaudu sisään käyttääksesi toimintoa"

@login_manager.user_loader
def lataa_kayttaja(user_id):
    return Kayttaja.query.get(user_id)

try:
    db.create_all()
except:
    pass
