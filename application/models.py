# application/models.py

from application import db

class Pohja(db.Model):

    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
    nimi = db.Column(db.String(144), nullable=False)


class TehtavaAihe(db.Model):

    __tablename__ = "tehtavaaihe"

    id        = db.Column(db.Integer, primary_key=True)
    tehtavaid = db.Column(db.Integer, db.ForeignKey('tehtava.id'))
    aiheid    = db.Column(db.Integer, db.ForeignKey('aihe.id'))

    liitostehtava = db.relationship("Tehtava", backref='tehtavaaihe', lazy=True)
    liitosaihe    = db.relationship("Aihe",    backref='tehtavaaihe', lazy=True)


    def __init__(self, tehtavaid, aiheid):
        self.tehtavaid = tehtavaid
        self.aiheid = aiheid

    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True


