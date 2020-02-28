# Käyttötapaukset

### Tietokantataulun luonti

Create-table lauseet

### Opiskelija nimeltä Pekka

Pekka on matematiikan opiskelija yliopistolla. Hän käyttää tehtävälistasovellusta pitääkseen kirjaa asioista, joita hänen on arjessa muistettava hoitaa.
Pekka haluaa tehdä seuraavia asioita sovelluksella:

+ Lisätä tehtävän jossa on useita aiheita

```SQL
INSERT INTO aihe (nimi) VALUES ("koulu");
INSERT INTO aihe (nimi) VALUES ("matematiikka");

INSERT INTO tehtava (nimi, kuvaus, pvm, valmis, kayttajaid)
VALUES ('Matikan tentti', 'Osat 3-5', '01-05-2020', false, 5);

INSERT INTO tehtavaaihe (tehtavaid, aiheid) VALUES (
    (SELECT MAX(id) FROM tehtava),
    (SELECT MAX(id)-1 FROM aihe)
)

INSERT INTO tehtavaaihe (tehtavaid, aiheid) VALUES (
    (SELECT MAX(id) FROM tehtava),
    (SELECT MAX(id) FROM aihe)
)
```

+ Katsoa mitä tehtäviä hän on aiemmin lisännyt

```SQL
SELECT * FROM tehtava
JOIN kayttaja ON tehtava.kayttajaid = kayttaja.id
WHERE kayttaja.tunnus = 'pekka';
```

+ Pekka haluaa tarkastella niitä tehtäviään, joita ei ole vielä saanut valmiiksi, järjestettynä aikajärjestyksessä

```SQL
SELECT * FROM tehtava
JOIN kayttaja ON tehtava.kayttajaid = kayttaja.id
WHERE kayttaja.tunnus = 'pekka'
AND tehtava.valmis = false ORDER BY pvm ASC;
```


+ Pekka haluaa katsella kouluun liittyviä tehtäviään vuoden 2020 tammikuulta
```SQL
SELECT * FROM tehtava
JOIN kayttaja ON tehtava.kayttajaid = kayttaja.id
JOIN tehtavaaihe ON tehtava.id = tehtavaaihe.tehtavaid
JOIN aihe ON tehtavaaihe.aiheid = aihe.id
WHERE aihe.nimi = 'koulu'
AND tehtava.pvm BETWEEN '2020-01-01' AND '2020-01-31'
AND kayttaja.tunnus = 'pekka';

```

+ Pekka haluaa nähdä montako aihetta hänellä on sovelluksessa

```SQL
SELECT COUNT(DISTINCT tehtavaaihe.aiheid) AS maara FROM aihe
JOIN tehtavaaihe ON aihe.id = tehtavaaihe.aiheid
JOIN tehtava ON tehtavaaihe.tehtavaid = tehtava.id
JOIN kayttaja ON tehtava.kayttajaid = kayttaja.id
WHERE kayttaja.tunnus = 'pekka';
```

+ Pekka haluaa muokata sovellukseen antamaansa nimeä, tunnusta ja salasanaa

```SQL
UPDATE kayttaja SET (nimi, tunnus, salasana) = ('Pekka', 'pekka', 'uusiSalasana123');
```

+ Pekka haluaa poistaa tilinsä ja kaikki siihen liittyvät tiedot sovelluksesta pysyvästi

```SQL
DELETE FROM tehtavaaihe USING tehtava WHERE tehtava.id = tehtavaaihe.tehtavaid AND tehtava.kayttajaid = 5;

DELETE FROM tehtava WHERE tehtava.kayttajaid = 5;

DELETE FROM kayttaja WHERE kayttaja.id = 5;

DELETE FROM aihe WHERE aihe.id IN (5, 6, 8, 10, 15, 17);
```

### Ylläpitäjä nimeltä Ismo

Ismo on sovelluksen ylläpitäjä. Hän on luonut sovelluksen, ja haluaa käyttää sitä normaalisti, mutta myös katsoa tietoja siitä, miten keskimääräiset käyttäjät käyttää sovellusta.

+ Ylläpitäjänä Ismo haluaa nähdä miten monta aihetta käyttäjillä on sovelluksessa keskimäärin

```SQL
SELECT AVG(maara) FROM 
(
    SELECT COUNT(tehtava.id) AS maara FROM tehtava
    RIGHT JOIN kayttaja ON kayttaja.id = tehtava.kayttajaid
    GROUP BY kayttaja.id
) AS keskiarvo
```


