# Projektin tila

### Toteutetut ominaisuudet ja korjaamatta jääneet ongelmat

+ Sovellus toimii pääosin hyvin.
+ Tehtävää lisätessä lomake ei tyhjene. En keksinyt mikä tähän tepsisi, uuden lomakkeen luominen GET-sivua muodostaessa ei auttanut, ja jos laittoi redirectauksen render_templaten sijasta, siihen ei saanut syötettyä parametrejä mukaan (halusin näkyviin Tehtävä lisätty -tekstin). Tiedon olisi voinut kuljettaa varmaan jollain selaimen sessioilla tai tyhjentää lomakkeet javascriptillä mutten halunnut ryhtyä selvittämään näitä koska asia oli lopulta melko pieni haitta.
+ Kun tehtävän poistaa tai merkkaa valmiiksi, sovellus heittää takaisin tehtävien hakuehtolomakkeeseen. Poisto tai muutto tekee POST-pyynnön, ja en keksinyt miten saman äsken näytetyn listauksen saisi välitettyä uudestaan GET-sivulle.
+ SQLite ei tykkää peräkkäisistä kyselyistä joita Kayttaja-luokan joissain metoideissa on ja sovellus ei tue sitä. PostgreSQL:n kanssa sovellus kuitenkin toimii mainiosti.
+ Poistamisesta tuli hieman monimutkaista kun en päässyt perille CASCADING DELETE -toiminnallisuuksista. Sain kuitenkin tehtyä poistolauseen joka poistaa aiheet joille ei jää yhtään viittausta, eli käyttämättömät aiheet poistetaan aina tehtävän poistamisen jälkeen ja kun käyttäjä poistaa kaikki tietonsa sovelluksesta.
+ Kyselyjä olisi yksinkertaistanut suuresti, jos aihe-taulussa olisi ollut viiteavain kayttaja-tauluun. Toisaalta opin ehkä enemmän kun toteutin sovelluksen ilman tätä, mutta se olisi ollut varmaankin järkevämpi toteutus jälkeenpäin mietittynä.


### Millainen sovelluksen kirjoittaminen oli kokemuksena?

Tässä tuli opittua todella paljon uutta, paitsi tekniikoista kuten Flask, SQL, PostgreSQL, niin myös isomman sovelluksen kirjoittamisesta. Vaikka olen ohjelmoinut jo vuosia, en ole näin isoa yhtenäistä projektia koskaan tehnyt koska mielenkiinto on aina loppunut (varmaan juuri siksi, että isommassa projektissa tulee vaikeuksia vastaan). Yksi isoimpia asioita oli se, että alussa tietokantaa suunnitellessa ei oikein pystynyt tajuamaan kaikkia mahdollisia ongelmia. Pidin tietokannan hyvin yksinkertaisena koska tästä oli minua varoiteltu, mutta silti yllätti, miten paljon koko ajan tuli uusia asioita pohdittavaksi. Oli vaivalloista koittaa ymmärtää sekä Flask-SQLAlchemyn toimintaa ja myös PostgreSQL:n vaatimuksia ja ominaisuuksia sovellusta tehdessä. Välillä paloi käämi näiden asioiden kanssa, mutta lopulta kurssi oli yksi antoisimpia tähän asti sen takia, että siinä tehtiin selkeästi omaa projektia koko ajan ja lopulta näkee kädenjälkensä ja huomaa konkreettisesti sen, miten paljon oppi kurssin aikana.

___

### Projektin nykyinen rakenne

+ **tehtavalistasovellus**
  + *run.py*
  + README.md
  + Procfile
  + requirements.txt
  + **application**
    + *\_\_init\_\_.py*
    + *models.py*
    + *views.py*
    + **tehtava**
      + *models.py*
      + *views.py*
      + *forms.py*
    + **auth**
      + *models.py*
      + *forms.py*
      + *views.py*
    + **aihe**
      + *models.py*
    + **templates**
      + index.html
      + layout.html
      + muuta_tietoja.html
      + poista.html
      + **auth**
        + kirjautumislomake.html
        + rekisteroitymislomake.html
        + hallinta.html
      + **tehtava**
        + index.html
        + list.html
        + uusi.html
        + listaa_kayttajat.html
  + **documentation**
    + kayttotapaukset.md
    + projektin_tila.md
    + asennusohje.md
    + tietokantakaavio.png


