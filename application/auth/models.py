from application import db




class Kayttaja(db.Model):

    __tablename__ = "kayttaja"

    id = db.Column(db.Integer, primary_key=True)

    nimi = db.Column(db.String(144), nullable=False)
    tunnus = db.Column(db.String(144), nullable=False)
    salasana = db.Column(db.String(144), nullable=False)

    tehtavat = db.relationship("Tehtava", backref='kayttaja', lazy=True)

    def __init__(self, nimi, tunnus, salasana):
        self.nimi = nimi
       # En ole varma onko nämä tarpeelliset
       # self.tunnus = tunnus
       # self.salasana = salasana

    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True

