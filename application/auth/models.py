from application import db
from application.models import Pohja
from sqlalchemy.sql import text
from application.aihe.models import Aihe


class Kayttaja(Pohja):

    __tablename__ = "kayttaja"

    tunnus = db.Column(db.String(144), nullable=False)
    salasana = db.Column(db.String(144), nullable=False)

    tehtavat = db.relationship("Tehtava", cascade="all, delete-orphan", backref="kayttaja")

    def __init__(self, nimi, tunnus, salasana):
        self.nimi = nimi
        self.tunnus = tunnus
        self.salasana = salasana

    # Hae käyttäjän omat tehtävät
    @staticmethod
    def hae_tehtavat(kayttajaid):
        kysely = text("SELECT tehtava.nimi, tehtava.kuvaus, tehtava.pvm, tehtava.valmis, tehtava.id"
                    " FROM tehtava WHERE"
                    " tehtava.kayttajaid = :kayttajaid").params(kayttajaid=kayttajaid)

        tulos = db.engine.execute(kysely)

        palautus = []
        for rivi in tulos:
            palautus.append({"nimi":rivi[0], "kuvaus":rivi[1], "pvm":rivi[2], "valmis":rivi[3], 
                             "id":rivi[4]})

        return palautus

    @staticmethod
    def hae_aiheet(kayttajaid):

        kysely = text("SELECT DISTINCT aihe.nimi, aihe.id FROM aihe"
		    " LEFT JOIN tehtavaaihe ON aihe.id = tehtavaaihe.aiheid"
		    " LEFT JOIN tehtava ON tehtavaaihe.tehtavaid = tehtava.id"
		    " WHERE tehtava.kayttajaid = :kayttaja_id").params(kayttaja_id=kayttajaid)

        aiheet = []
        tulos = db.engine.execute(kysely)
        for rivi in tulos:
    	    aiheet.append({"nimi":rivi[0], "id":rivi[1]})

        return aiheet

    @staticmethod
    def onko_olemassa(tunnus):

        kysely = text("SELECT * FROM kayttaja WHERE tunnus = :tunnus").params(tunnus=tunnus)

        tulos = db.engine.execute(kysely).first()

        return tulos != None


    @staticmethod
    def hae_aiheiden_maara(kayttajaid):

        kysely = text(
            "SELECT COUNT(DISTINCT tehtavaaihe.aiheid) AS maara FROM aihe"
            " JOIN tehtavaaihe ON aihe.id = tehtavaaihe.aiheid"
            " JOIN tehtava ON tehtavaaihe.tehtavaid = tehtava.id"
            " WHERE tehtava.kayttajaid = :kayttajaid").params(kayttajaid=kayttajaid)
        
        tulos = db.engine.execute(kysely).first()[0]

        return tulos


    @staticmethod
    def hae_tehtavien_keskiarvo():

        kysely = text(
            "SELECT AVG(maara) FROM ("
            " SELECT COUNT(tehtava.id) AS maara FROM tehtava"
            " RIGHT JOIN kayttaja ON kayttaja.id = tehtava.kayttajaid"
            " GROUP BY kayttaja.id"
            ") AS keskiarvo")
        
        tulos = db.engine.execute(kysely).first()[0]

        return round(tulos, 2)


    @staticmethod
    def muuta_tietoja(id, nimi, tunnus, salasana):
        
        kysely = text("UPDATE kayttaja SET (nimi, tunnus, salasana) ="
                      " (:nimi, :tunnus, :salasana) WHERE kayttaja.id = :id").params(id=id, nimi=nimi, tunnus=tunnus,
                      salasana=salasana)

        db.engine.execute(kysely)

    @staticmethod
    def poista_tiedot(kayttajaid):
        
        kysely = text("DELETE FROM tehtavaaihe USING tehtava WHERE tehtava.id = tehtavaaihe.tehtavaid AND tehtava.kayttajaid = :kayttajaid").params(kayttajaid=kayttajaid)
        db.engine.execute(kysely)

        kysely = text("DELETE FROM tehtava WHERE tehtava.kayttajaid = :kayttajaid").params(kayttajaid=kayttajaid)
        db.engine.execute(kysely)

        kysely = text("DELETE FROM kayttaja WHERE kayttaja.id = :kayttajaid").params(kayttajaid=kayttajaid)
        db.engine.execute(kysely)
        
        kysely = text("DELETE FROM aihe WHERE NOT EXISTS (SELECT 1 FROM tehtavaaihe WHERE tehtavaaihe.aiheid = aihe.id)")
        db.engine.execute(kysely)

    @staticmethod
    def poista_tehtava(tehtavaid):

        kysely = text("DELETE FROM tehtavaaihe WHERE tehtavaaihe.tehtavaid = :tehtavaid").params(tehtavaid=tehtavaid)
        db.engine.execute(kysely)

        kysely = text("DELETE FROM tehtava WHERE tehtava.id = :tehtavaid").params(tehtavaid=tehtavaid)
        db.engine.execute(kysely)

        kysely = text("DELETE FROM aihe WHERE NOT EXISTS ("
                      " SELECT 1 FROM tehtavaaihe WHERE tehtavaaihe.aiheid = aihe.id)")
        db.engine.execute(kysely)


    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True

    def roles(self):
        if self.tunnus=="taikuri54":
            return ["ADMIN"]
        return ["USER"]


