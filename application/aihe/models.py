from application import db
from application.models import Pohja

# many-to-many kokeilua
from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

tehtavaAihe = Table('tehtavaAihe', Pohja.metadata,
    Column('tehtavaid', Integer, ForeignKey('tehtava.id')),
    Column('aiheid', Integer, ForeignKey('aihe.id')))

class Aihe(Pohja):

    __tablename__ = "aihe"

    tehtavat = db.relationship("TehtavaAihe", backref='aihe', lazy=True)

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


