# Projektin tila

Tässä tiedostossa pidän kirjaa tehtävälistasovellus-harjoitusprojektin tilasta.

**Tilanne 20.2.2020**

+ Monesta-moneen suhde toteutettu. Tilastot-sivulla nyt pystyy listaamaan aiheet joita käyttäjä on syöttänyt, eli haku tapahtuu taulujen kautta näin: aihe->tehtavaaihe->tehtava->kayttaja
+ Isoja päivityksiä ulkoasuun listauksen osalta, mutta paljon on vielä tehtävää.
+ Validoinnit pitäisi olla nyt pääpiirteittäin OK.
+ Virheviestejä tarvitaan tehtävän luomislomakkeeseen
+ Listausrajaukset ja järjestelyt tarvitaan

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


