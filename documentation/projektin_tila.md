# Projektin tila

Tässä tiedostossa pidän kirjaa tehtävälistasovellus-harjoitusprojektin tilasta.

**Tilanne 26.2.2020**

+ Tilastot-sivu on korvattu Tilin hallinta -sivulla, josta tunnuksen tietoja voi muuttaa ja sen voi poistaa (ei välttämättä toimi herokussa (postgresql) vielä, paikallisesti kyllä)
  + Admin näkee sivulla montako tehtävää käyttäjillä on keskimäärin
  + Adminin linkki josta näki kaikkien käyttäjien tehtävät poistettu pysyvästi
+ User storyjä ei vielä päivitetty eikä muutakaan dokumentaatiota eli alla näkyvä rakennekin on vanhentunut


___

### Projektin nykyinen rakenne

**Kansiot** lihavoituna, *python-tiedostot* kursivoituna

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


