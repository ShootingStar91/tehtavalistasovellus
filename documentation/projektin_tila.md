# Projektin tila

Tässä tiedostossa pidän kirjaa tehtävälistasovellus-harjoitusprojektin tilasta.

**Tilanne 14.2.2020**

+ Monesta-moneen suhde toteutettu. Tilastot-sivulla nyt pystyy listaamaan aiheet joita käyttäjä on syöttänyt, eli haku tapahtuu taulujen kautta näin: aihe->tehtavaaihe->tehtava->kayttaja
+ Autorisointia ei vielä toteutettu muuten kuin login_required määreellä joka opetettiin jo viikolla 3. Koitin toteuttaa viikon 5 materiaalin mukaisesti, mutta en saanut toimimaan.


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


