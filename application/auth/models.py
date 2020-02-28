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
        stmt = text("SELECT tehtava.nimi, tehtava.kuvaus, tehtava.pvm, tehtava.valmis, tehtava.id"
                    " FROM tehtava WHERE"
                    " tehtava.kayttajaid = :kayttajaid").params(kayttajaid=kayttajaid)

        tulos = db.engine.execute(stmt)

        palautus = []
        for rivi in tulos:
            palautus.append({"nimi":rivi[0], "kuvaus":rivi[1], "pvm":rivi[2], "valmis":rivi[3], 
                             "id":rivi[4]})

        return palautus

    @staticmethod
    def hae_aiheet(kayttajaid):

        stmt = text("SELECT DISTINCT aihe.nimi, aihe.id FROM aihe"
		    " LEFT JOIN tehtavaaihe ON aihe.id = tehtavaaihe.aiheid"
		    " LEFT JOIN tehtava ON tehtavaaihe.tehtavaid = tehtava.id"
		    " WHERE tehtava.kayttajaid = :kayttaja_id").params(kayttaja_id=kayttajaid)

        aiheet = []
        tulos = db.engine.execute(stmt)
        for rivi in tulos:
    	    aiheet.append({"nimi":rivi[0], "id":rivi[1]})

        return aiheet

    @staticmethod
    def onko_olemassa(tunnus):

        kysely = text("SELECT * FROM kayttaja WHERE tunnus = :tunnus").params(tunnus=tunnus)

        tulos = db.engine.execute(kysely).first()

        return tulos != None

    ''' TÄMÄ POISTETAAN LOPUKSI
    @staticmethod
    def hae_kayttajat_joilla_tehtavia():

        stmt = text("SELECT DISTINCT kayttaja.nimi FROM kayttaja"
                    " LEFT JOIN tehtava ON tehtava.kayttajaid = kayttaja.id"
                    " GROUP BY kayttaja.nimi"
                    " HAVING COUNT(tehtava.id) > 0")
        kayttajat = []
        tulos = db.engine.execute(stmt)
        for rivi in tulos:

    '''

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
    def hae_aiheiden_keskiarvo():

        kysely = text(
            "SELECT AVG(maara) FROM ("
            " SELECT COUNT(DISTINCT tehtavaaihe.aiheid) AS maara FROM aihe"
            " JOIN tehtavaaihe ON aihe.id = tehtavaaihe.aiheid"
            " JOIN tehtava ON tehtavaaihe.tehtavaid = tehtava.id"
            " GROUP BY tehtava.kayttajaid"
            ") as keskiarvo")
        
        tulos = db.engine.execute(kysely).first()[0]

        return round(tulos, 2)



    @staticmethod
    def hae_tehtavien_keskiarvo():

        kysely = text(
            "SELECT AVG(maara) FROM ("
            " SELECT COUNT(kayttajaid) AS maara FROM tehtava GROUP BY kayttajaid"
            ") as keskiarvo")
        
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
        
        # Käyttäjään liittyvät aiheet talteen
        kysely = text("SELECT aihe.id as id, aihe.nimi as nimi FROM aihe"
                    " JOIN tehtavaaihe ON aihe.id = tehtavaaihe.aiheid"
                    " JOIN tehtava ON tehtavaaihe.tehtavaid = tehtava.id"
                    " WHERE tehtava.kayttajaid = :kayttajaid").params(kayttajaid=kayttajaid)
        tulos = db.engine.execute(kysely)
        db.engine.connect()

        kysely = text("DELETE FROM tehtavaaihe USING tehtava WHERE tehtava.id = tehtavaaihe.tehtavaid AND tehtava.kayttajaid = :kayttajaid").params(kayttajaid=kayttajaid)
        db.engine.execute(kysely)

        kysely = text("DELETE FROM tehtava WHERE tehtava.kayttajaid = :kayttajaid").params(kayttajaid=kayttajaid)
        db.engine.execute(kysely)

        kysely = text("DELETE FROM kayttaja WHERE kayttaja.id = :kayttajaid").params(kayttajaid=kayttajaid)
        db.engine.execute(kysely)
        aihelista = []
        
        for rivi in tulos:
            aihelista.append(rivi[0])

        for aiheid in aihelista:
            Aihe.query.filter(Aihe.id==aiheid).delete()
            db.session().commit()


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


