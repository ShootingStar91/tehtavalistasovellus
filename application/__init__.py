from flask import Flask
app = Flask(__name__)

from flask_sqlalchemy import SQLAlchemy

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///tehtava.db"

app.config["SQLALCHEMY_ECHO"] = True

db = SQLAlchemy(app)


from application import views

from application.tehtava import models
from application.tehtava import views

db.create_all()
