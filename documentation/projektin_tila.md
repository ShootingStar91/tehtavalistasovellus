# Projektin tila

Tässä tiedostossa pidän kirjaa tehtävälistasovellus-harjoitusprojektin tilasta.

**Tilanne viikon 4 kohdalla**

+ Tehtävään voi lisätä aiheita pilkulla eroteltuna
  + Esimerkiksi: koulu,matematiikka,tentti
  + Aiheita ei voi kuitenkaan herokussa katsoa. Paikallisesti toimii jo ominaisuus, jossa tilastot-sivun kautta pystyy katsomaan omat lisätyt aiheet. Tämä ei kuitenkaan toimi jostain syystä Herokussa.
  + Ongelma liittynee monesta moneen -taulun toteutukseen jotenkin.
+ Herokussa pystyy näkemään yhteenvetokyselyn tuloksen, eli listauksen käyttäjistä, joilla on vähintään 1 tehtävä sovelluksessa.


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
      + **auth**
        + kirjautumislomake.html
        + rekisteroitymislomake.html
      + **tehtava**
        + list.html
        + uusi.html
        + tilastot.html
        + listaa_aiheet.html
        + listaa_kayttajat.html
  + **documentation**
    + kayttotapaukset.md
    + projektin_tila.md
    + tietokantakaavio.png


