# Projektin tila

Tässä tiedostossa pidän kirjaa tehtävälistasovellus-harjoitusprojektin tilasta.

**Tilanne 28.2.2020**

+ Sovellukseen lisätty monimutkaisemmat yhteenvetokyselyt
+ Dokumentaatiota päivitetty, sovellus enää loppuhiontaa vailla

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
    + tietokantakaavio.png


