## Tehtävälistasovellus

Tehtävälistasovellus on web-sivustolla toimiva sovellus, johon käyttäjä kirjautuu sisään tunnuksella ja salasanalla. Tämän jälkeen käyttäjä voi lisätä itselleen tehtäviä joita hänen täytyy tulevaisuudessa tehdä, esimerkiksi rautakaupassa käyminen, keittiön siivoaminen, tai kokeeseen lukeminen. Tehtäville voi halutessaan merkitä päivämäärän johon mennessä tehtävän tulee olla tehty. Tehtävillä on jokin otsikko eli nimi, ja myös tarkempi kuvaus tehtävän sisällöstä. Tehtävillä on myös prioriteettiaste, sekä mahdollisesti aihe tai aiheita joita tehtävään liittyy. Yksi aihe voi olla siis useammassa tehtävässä ja yhdellä tehtävällä voi olla useampi aihe, vaikkapa koulu ja matematiikka. Tehtävän voi myös merkitä tehdyksi.

Omia tehtäviä voi myös tarkastella sovelluksessa. Niitä voi järjestää ja näyttää ominaisuuksien mukaan. Esimerkiksi käyttäjä voi katsoa sellaiset tehtävät joita ei olla vielä tehty ja joiden päivämäärä on vaikkapa seuraavan viikon sisällä, tai sellaiset tehtävät joiden aiheissa on "koulu".

### Toimintoja:

+ Tehtävän lisääminen
  + Useita aiheita yhdelle tehtävälle
  + Aiheen voi tehtävää lisättäessä valita joko aiemmista itse lisäämistä aiheista, tai luoda uuden. Aiheet näkyvät vain itselle.
+ Tehtävien katselu
  + Tehtävien suodattaminen kriteerien mukaan (esim. aihe tai päivämäärä)
  + Näytettävien tehtävien järjestäminen
+ Tehtävän merkitseminen tehdyksi
+ Tehtävän muokkaaminen (päivämäärän siirtäminen, kuvauksen muuttaminen)
+ Tunnuksen luominen, sisäänkirjautuminen
+ Käyttäjätunnuksen poistaminen, jolloin kaikki tunnuksen tehtävät poistuvat tietokannasta

### Tietokantakaavio

![Tietokantakaavio (tehtävälistasovellus)](
https://github.com/ShootingStar91/tehtavalistasovellus/blob/master/tehtavalistasovellus.png
 "Tietokantakaavio")

