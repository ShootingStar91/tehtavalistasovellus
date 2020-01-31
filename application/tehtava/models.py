from application import db

class Tehtava(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    pvm = db.Column(db.DateTime)
    nimi = db.Column(db.String(144), nullable=False)
    kuvaus = db.Column(db.TEXT, nullable=True)
    valmis = db.Column(db.Boolean, nullable=False)
    kayttajaid = db.Column(db.Integer, db.ForeignKey('kayttaja.id'), 
                            nullable=False)


    def __init__(self, nimi):
        self.nimi = nimi
        self.valmis = False



