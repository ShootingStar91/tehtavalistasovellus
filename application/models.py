# application/models.py

from application import db

class Pohja(db.Model):

    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
    nimi = db.Column(db.String(144), nullable=False)
