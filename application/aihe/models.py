from application import db
from application.models import Pohja

# many-to-many kokeilua
from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

tehtavaAihe = db.Table('tehtavaAihe',
    db.Column('tehtavaid', db.Integer, db.ForeignKey('tehtava.id'), nullable=False),
    db.Column('aiheid', db.Integer, db.ForeignKey('aihe.id'), nullable=False),
    db.PrimaryKeyConstraint('tehtavaid', 'aiheid'))

class Aihe(Pohja):

    __tablename__ = "aihe"

    tehtavat = db.relationship("Tehtava", secondary=tehtavaAihe, backref='aihe')

    def __init__(self, nimi):
        self.nimi = nimi

    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True


