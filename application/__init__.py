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



# Kirjautuminen

from os import urandom
app.config["SECRET_KEY"] = urandom(32)

from flask_login import LoginManager, current_user
login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = "auth_kirjaudu"
login_manager.login_message = "Kirjaudu sisään käyttääksesi toimintoa"

from functools import wraps 

def login_required(_func=None, *, role="ANY"):
    def wrapper(func):
        @wraps(func)
        def decorated_view(*args, **kwargs):
            if not (current_user and current_user.is_authenticated):
                return login_manager.unauthorized()

            acceptable_roles = set(("ANY", *current_user.roles()))

            if role not in acceptable_roles:
                return login_manager.unauthorized()

            return func(*args, **kwargs)
        return decorated_view
    return wrapper if _func is None else wrapper(_func)


from application import views

from application.tehtava import models
from application.tehtava import views

from application.auth import models
from application.auth import views

from application.aihe import models

from application.auth.models import Kayttaja

from datetime import datetime

def muotoile_pvm(pvm):
    return pvm[8:10]+"."+pvm[5:7]+"."+pvm[0:4]

app.jinja_env.globals.update(muotoile_pvm=muotoile_pvm)

@login_manager.user_loader
def lataa_kayttaja(user_id):
    kayttaja = Kayttaja.query.get(user_id)
    
    return kayttaja

try:
    db.create_all()
except:
    pass
