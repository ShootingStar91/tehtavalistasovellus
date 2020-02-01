from application import db
from application.models import Pohja

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


