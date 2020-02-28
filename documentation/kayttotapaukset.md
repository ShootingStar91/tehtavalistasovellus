# Käyttötapaukset

### Opiskelija nimeltä Pekka

Pekka on matematiikan opiskelija yliopistolla. Hän käyttää tehtävälistasovellusta pitääkseen kirjaa asioista, joita hänen on arjessa muistettava hoitaa.
Pekka haluaa tehdä seuraavia asioita sovelluksella:

+ Lisätä tehtäviä joissa on useita aiheita

```SQL
INSERT INTO aihe (nimi) VALUES ("koulu");

INSERT INTO tehtava (nimi, kuvaus, pvm, valmis)
VALUES ('Matikan tentti', 'Osat 3-5', '01-05-2020', false);

INSERT INTO tehtavaaihe (tehtavaid, aiheid) VALUES (
    (SELECT MAX(id) FROM aihe),
    (SELECT MAX(id)-1 FROM aihe)
)
```

+ Asettaa lisäämäänsä tehtävään deadlinen
+ Katsoa mitä tehtäviä hän on aiemmin lisännyt
+ Pekka haluaa tarkastella niitä tehtäviä, joita ei ole vielä saanut valmiiksi, järjestettynä päivämäärän mukaan
+ Pekka haluaa katsella tiettyyn aiheeseen liittyviä tehtäviä tietyltä ajanjaksolta
+ Pekka haluaa nähdä montako aihetta hänellä on sovelluksessa

### Itseopiskelija nimeltä Irma

Irma on työtön, joka haluaa kehittää itseään ja opiskelee innokkaasti asioita itsenäisesti. Hän lukee kirjoja ja urheilee.

Irma haluaa tehdä sovelluksella seuraavia asioita:

+ Lisätä sovellukseen tehtävänä kirjan jonka hän aikoo lukea
+ Irma haluaa lenkillä käytyään voida lisätä lenkin kyseiselle päivälle ja tiedon että se on jo tehty
+ Irma haluaa muokata sovellukseen antamaansa nimeä, tunnusta ja salasanaa
+ Irma haluaa poistaa tilinsä ja kaikki siihen liittyvät tiedot sovelluksesta pysyvästi

### Ylläpitäjä nimeltä Ismo

Ismo on sovelluksen ylläpitäjä. Hän on luonut sovelluksen, ja haluaa käyttää sitä normaalisti, mutta myös katsoa tietoja siitä, miten keskimääräiset käyttäjät käyttää sovellusta.

+ Ylläpitäjänä Ismo haluaa nähdä miten monta aihetta käyttäjillä on sovelluksessa keskimäärin
