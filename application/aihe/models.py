from application import db
from application.models import Pohja
from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

tehtavaAihe = db.Table('tehtavaaihe',
    db.Column('tehtavaid', db.Integer, db.ForeignKey('tehtava.id'), nullable=False),
    db.Column('aiheid', db.Integer, db.ForeignKey('aihe.id'), nullable=False))

class Aihe(Pohja):

    __tablename__ = "aihe"

    tehtavat = db.relationship('Tehtava', secondary=tehtavaAihe, backref='Aihe', viewonly=True)

    def __init__(self, nimi):
        self.nimi = nimi

