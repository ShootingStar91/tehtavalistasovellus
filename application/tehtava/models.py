from application import db
from application.models import Pohja

class Tehtava(Pohja):

    pvm = db.Column(db.DateTime)
    kuvaus = db.Column(db.TEXT, nullable=True)
    valmis = db.Column(db.Boolean, nullable=False)
    kayttajaid = db.Column(db.Integer, db.ForeignKey('kayttaja.id'),
                            nullable=False)

    aiheet = db.relationship("TehtavaAihe", backref='tehtava', lazy=True)

    def __init__(self, nimi):
        self.nimi = nimi
        self.valmis = False



