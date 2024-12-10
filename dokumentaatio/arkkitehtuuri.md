Arkkitehtuurikuvaus
===================

Rakenne
-------

![pakkauskaavio](./img/pakkauskaavio.jpg)

Ohjelman koodi noudattaa eräänlaista kerrosrakennetta ja jakautuu pääasiallisesti
pakkauksiin `ui` ja `game`,
joista ensimmäinen sisältää käyttöliittymäkoodia ja jälkimmäinen sovelluslogiikkaa.
Pakkaus `ui` sisältää moduulit `text_ui` ja `graphical_ui`,
joiden funktioita kutsutaan suoraan `main`-moduulista, josta ohjelman suoritus alkaa.
Sovellusta ajettaessa käytetään käyttöliittymämoduuleista **jompaa kumpaa**.
Pakkauksen `ui` moduulit keräävät käyttäjän syötettä ja esittävät tälle pelin tilan.

Käyttäjän syötteen perusteella käyttöliittymä puhuttelee `game`-pakkauksen moduuleja,
jotka ovat `game_state` ja `scores`.
Moduuli `game_state` sisältää luokan `GameState`, jonka metodit muodostavat rajapinnan
käyttöliittymän ja pelilogiikan välille.
Moduuli `scores` taas sisältää funktioita, jotka liittyvät pelitulosten tallentamiseen
tietokantaan sekä tallennettujen pelitulosten hakemiseen.

Graafinen käyttöliittymä
------------------------

Graafista käyttöliittymää käytettäessä ohjelmassa on päänäkymä, jossa itse peliä pelataan.
Kun jokin toiminto vaatii käyttäjältä teksti- tai numeromuotoista syötettä,
avaa ohjelma tätä varten ali-ikkunan.
Päänäkymä sisältää yläpalkin, jonka kautta käyttäjä voi aloitta uuden pelin,
sekä pelikentän, jonka ruutuja käyttäjä voi napsauttaa hiiren vasemmalla tai
oikealla painikkeella tahi keskipainikkeella.

Tietokanta
----------

Tietokanta varastoi pelituloksia.
Se sisältää taulukon `score`, johon tallettuvat pelin kesto ja peliasetukset.
Lisäksi siinä on sarake, joka viittaa taulukon `user` riviin.
Taulukko `user` sisältää tuloksen tallentaneen käyttäjän tiedot.
Käyttäjä määritetään tuloksen tallentamisen yhteydessä syötetyn nimimerkin perusteella.

Ylimääräistä
------------

Tässä ompi `scores`-moduulin funktion `save_score` sekvenssikaavio,
kun tietokantaa ei ole entuudestaan olemassa.

```mermaid
sequenceDiagram
  participant main
  create participant wrapper
  main ->> wrapper: save_score(32, "alpertti", 10, 10, 10)
  create participant create_database
  wrapper ->> create_database: create_database()
  create participant db
  create_database ->> db: connect()
  create_database ->> db: cursor()
  create participant cur
  db ->> cur: ...
  db -->> create_database: cur
  create_database ->> cur: execute(...)
  create_database ->> cur: execute(...)
  create_database -->> wrapper: db
  create participant save_score
  wrapper ->> save_score: save_score(db, 32, "alpertti", 10, 10, 10)
  save_score ->> db: cursor()
  db -->> save_score: cur
  save_score ->> cur: execute(..., ("alpertti"))
  cur -->> save_score: None
  save_score ->> cur: execute(..., ("alpertti"))
  cur -->> save_score: 1
  save_score ->> cur: execute(..., (32, 1, 10, 10, 10))
  save_score ->> db: commit()
```
