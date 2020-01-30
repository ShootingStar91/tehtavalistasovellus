from application import db




class User(db.Model):

    __tablename__ = "kayttaja"

    id = db.Column(db.Integer, primary_key=True)

    nimi = db.Column(db.String(144), nullable=False)
    tunnus = db.Column(db.String(144), nullable=False)
    salasana = db.Column(db.String(144), nullable=False)

    def __init__(self, nimi, tunnus, salasana):
        self.nimi = nimi
        self.tunnus = tunnus
        self.salasana = salasana

    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True

