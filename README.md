## Tehtävälistasovellus

Tehtävälistasovellus on web-sivustolla toimiva sovellus, johon käyttäjä kirjautuu sisään tunnuksella ja salasanalla. Tämän jälkeen käyttäjä voi lisätä itselleen tehtäviä joita hänen täytyy tulevaisuudessa tehdä, esimerkiksi rautakaupassa käyminen, keittiön siivoaminen, tai kokeeseen lukeminen. Tehtäville voi merkitä päivämäärän johon mennessä tehtävän tulee olla tehty. Tehtävillä on jokin otsikko eli nimi, ja myös tarkempi kuvaus tehtävän sisällöstä. Tehtävillä on myös aihe tai aiheita joita tehtävään liittyy. Yksi aihe voi olla siis useammassa tehtävässä ja yhdellä tehtävällä voi olla useampi aihe, vaikkapa koulu ja matematiikka. Tehtävän voi myös merkitä tehdyksi.

Omia tehtäviä voi myös tarkastella sovelluksessa. Niitä voi järjestää ja näyttää ominaisuuksien mukaan. Esimerkiksi käyttäjä voi katsoa sellaiset tehtävät joita ei olla vielä tehty ja joiden päivämäärä on vaikkapa seuraavan viikon sisällä, tai sellaiset tehtävät joiden aiheissa on "koulu".
___
### Toiminnot

+ Tehtävän lisääminen
  + Useita aiheita yhdelle tehtävälle
  + Aiheen voi tehtävää lisättäessä valita joko aiemmista itse lisäämistä aiheista, tai luoda uuden. Aiheet näkyvät vain itselle.
  + Jos tehtävälle ei anna päivämäärää, sovellus lisää sille sen hetken päivämäärän.
+ Tehtävien katselu
  + Tehtävien suodattaminen kriteerien mukaan (aiheiden tai valmiuden mukaan, tai päivämäärällä suodattaminen)
  + Näytettävien tehtävien järjestäminen aiheen tai päivämäärän mukaan
+ Tehtävän merkitseminen tehdyksi
+ Tunnuksen luominen, sisäänkirjautuminen, tunnuksen muuttaminen
+ Käyttäjätunnuksen poistaminen, jolloin kaikki tunnuksen tehtävät poistuvat tietokannasta
+ Ylläpitäjä näkee tiedon montako tehtävää käyttäjillä on sovelluksessa keskimäärin.

___
### Käyttöohje

Sovellukseen luodaan oma käyttäjätili painamalla Rekisteröidy-linkkiä ylävalikossa. Kirjautuminen ja uloskirjautuminen tapahtuu myös yläpalkista. Kirjautunut käyttäjä voi luoda omia tehtäviä Lisää tehtävä-linkin kautta. Tehtäviin täytyy laittaa vähintään nimi. Päivämäärä tulee olla muodossa dd.mm.yyyy, seuraavat kelpaa: 01.12.2020, 1.4.2021. Jos päivämäärää ei syötä, sen hetkinen päivämäärä tulee tehtävään automaattisesti. Tehtävään voi lisätä aiheita joko aiemmin käyttäjän itse lisäämistä aiheista tai sitten lisätä uusia tekstikenttään pilkulla erotettuna, esimerkiksi: "autoilu,vapaa-aika". Tehtävien katselu tapahtuu Listaa tehtävät-linkistä yläpalkista. Tehtäviä voi merkata tehdyiksi tai poistaa listauksen oikeasta laidasta.
___
### Heroku

+ [Herokuapp](https://tehtavalistasovellus.herokuapp.com/tehtava)
+ Admin-testitunnus herokuun:
  + __Tunnus__: taikuri54
  + __Salasana__: ismo
  + Voit myös luoda uuden tunnuksen ja kokeilla toimintoja sillä. Yllä mainittu testitunnus on ainoa jolla on admin-oikeudet.
___
### Dokumentaatio

+ [Projektin tila](https://github.com/ShootingStar91/tehtavalistasovellus/blob/master/documentation/projektin_tila.md)
+ [Käyttötapaukset](https://github.com/ShootingStar91/tehtavalistasovellus/blob/master/documentation/kayttotapaukset.md)
+ [Asennusohje](https://github.com/ShootingStar91/tehtavalistasovellus/blob/master/documentation/asennusohje.md)

+ Tietokantakaavio:

![Tietokantakaavio (tehtävälistasovellus)](
https://github.com/ShootingStar91/tehtavalistasovellus/blob/master/documentation/tietokantakaavio.jpg
 "Tietokantakaavio")
