# Projektin tila

Tässä tiedostossa pidän kirjaa tehtävälistasovellus-harjoitusprojektin tilasta.

Osan 3 vaatimukset valmiit.

+ Rekisteröityminen, kirjautuminen
+ Tehtävän CRUD: Luominen, listaaminen, muokkaaminen ja poistaminen
  + Muokkaaminen tarkoittaa tässä vaiheessa vain tehtävän merkkaamista tehdyksi
  + Tehtävän voi poistaa "poista"-linkistä tehtävien listauksessa
+ Tehtävillä ei ole vielä päivämääräominaisuutta.
+ Vain kaksi taulua toistaiseksi: kayttaja ja tehtava.
+ Aiemmin suunnittelemani prioriteetti-ominaisuus poistettu.
  + Ei kuulunut niin hyvin sovelluksen ajatukseen, joka kehittyi viime viikon käyttäjäkertomuksia kirjoittaessa.

### Projektin nykyinen rakenne

**Kansiot** lihavoituna, *python-tiedostot* kursivoituna

+ **tehtavalistasovellus**
  + *run.py*
  + README.md
  + Procfile
  + requirements.txt
  + **application**
    + *__init__.py*
    + *models.py*
    + tehtava.db
    + *views.py*
    + **tehtava**
      + *models.py*
      + *views.py*
      + *forms.py*
    + **auth**
      + *models.py*
      + *views.py*
    + **aihe**
      + *models.py*
    + **templates**
      + index.html
      + layout.html
      + **auth**
        + *forms.py*
        + kirjautumislomake.html
        + rekisteroitymislomake.html
      + **tehtava**
        + list.html
        + uusi.html
  + **documentation**
    + kayttotapaukset.md
    + projektin_tila.md
    + tietokantakaavio.png


