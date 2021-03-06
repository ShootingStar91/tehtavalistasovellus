from application import db
from application.models import Pohja
from application.aihe.models import tehtavaAihe

class Tehtava(Pohja):

    pvm = db.Column(db.DateTime)
    kuvaus = db.Column(db.TEXT, nullable=True)
    valmis = db.Column(db.Boolean, nullable=False)
    kayttajaid = db.Column(db.Integer, db.ForeignKey('kayttaja.id', ondelete="CASCADE"),
                            nullable=False)

    aiheet = db.relationship('Aihe', backref='Tehtava', secondary=tehtavaAihe)


    def __init__(self, nimi):
        self.nimi = nimi
        self.valmis = False



