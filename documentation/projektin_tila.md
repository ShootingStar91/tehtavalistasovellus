# Projektin tila

Tässä tiedostossa pidän kirjaa tehtävälistasovellus-harjoitusprojektin tilasta.

**Tilanne 22.2.2020**

+ Huomio herokusta arvioijille: Sovellus ei välillä ole auennut hetkeen - vika vaikuttaa olevan Herokun päässä sillä muutoksia ei tehty tuona aikana ja se alkoi taas toimimaan yhtäkkiä.
+ Ulkoasua kehitetty huomattavasti tärkeimpien sivujen osalta. HTML:n ja CSS:n validiutta ei vielä kuitenkaan ole huomioitu, eikä käytettävyyden hienostuneempia asioita.
+ Aiheiden lisäys alkaa olla hyvällä mallilla, joskin vaatii vielä varmentavaa testausta ja säätöä että duplikaattiaiheita ei samalle käyttäjälle tule
+ Tehtäviä voi lisätä ja niissä on aihe ja päivämäärä ja kuvaus ja valmius, ja niitä voi katsella. Listauksessa on myös järjestys. Nämä ominaisuudet on valmiita ja toimii. 

##### Seuraavaksi lisättäviä ominaisuuksia

+ Aiheiden mukaan listaus on tarkoitus lisätä, ja sen jälkeen kaikki user storyt pitäisi täyttyä.
+ Tarkoitus on myös lisätä mahdollisuus käyttäjätilin managerointiin, eli kaikkien tilitietojen muokkaamiseen sekä koko tilin poistamiseen pysyvästi - mukaanlukien kaikki tiliin liittyvät tehtävät ja aiheet.

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


