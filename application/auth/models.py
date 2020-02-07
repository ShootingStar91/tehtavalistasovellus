from application import db
from application.models import Pohja
from sqlalchemy.sql import text

class Kayttaja(Pohja):

    __tablename__ = "kayttaja"

    tunnus = db.Column(db.String(144), nullable=False)
    salasana = db.Column(db.String(144), nullable=False)


    def __init__(self, nimi, tunnus, salasana):
        self.nimi = nimi
        self.tunnus = tunnus
        self.salasana = salasana

    # Hae käyttäjän omat tehtävät
    @staticmethod
    def hae_tehtavat(kayttajaid):
        stmt = text("SELECT Tehtava.nimi, Tehtava.kuvaus, Tehtava.pvm, Tehtava.valmis, Tehtava.id"
                    " FROM Tehtava WHERE"
                    " Tehtava.kayttajaid = :kayttajaid").params(kayttajaid=kayttajaid)

        tulos = db.engine.execute(stmt)

        palautus = []
        for rivi in tulos:
            palautus.append({"nimi":rivi[0], "kuvaus":rivi[1], "pvm":rivi[2], "valmis":rivi[3], 
                             "id":rivi[4]})

        return palautus

    @staticmethod
    def hae_aiheet(kayttajaid):

        stmt = text("SELECT Aihe.nimi, Tehtava.nimi FROM Aihe"
		    " LEFT JOIN TehtavaAihe ON Aihe.id = TehtavaAihe.aiheid"
		    " LEFT JOIN Tehtava ON TehtavaAihe.tehtavaid = Tehtava.id"
		    " WHERE Tehtava.kayttajaid = :kayttaja_id").params(kayttaja_id=kayttajaid)

        aiheet = []
        tulos = db.engine.execute(stmt)
        for rivi in tulos:
    	    aiheet.append({"nimi":rivi[0], "tehtavanimi":rivi[1]})

        return aiheet


    # Kirjastojen vaatimat metodit
    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True

