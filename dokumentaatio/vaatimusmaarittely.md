Sovelluksen tarkoitus
=====================

Sovelluksen avulla käyttäjän on mahdollista viihdyttää itseään klassisen
miinaharava-pelin parissa. Tässä dokumentissa oletetaan, että lukija tuntee
suurin piirtein miinaharavan säännöt.

Toiminnallisuus
===============

Käyttäjä voi

- aloittaa pelin joko ennalta määritellyllä tai käyttäjän määrittelemällä
  vaikeustasolla (pelikentän koko ja miinojen lkm).
  (tehty)
- nähdä pelin aikana kuluneen ajan.
  (tehty)
- ratkaistuaan pelin tallentaa saavuttamansa ajan tuloslistalle.
  (tehty)
- tarkastella aiempia tuloksia.

Käyttöliittymä
==============

Peliä pelataan lopullisessa versiossa hiirellä. Käyttäjä voi pelin aikana

- avata (kaivaa) ruudun. Jos tässä tai missään sitä ympäröivässä ruudussa ei
  ole miinaa, avautuvat myös ympäröivät ruudut. Tämä jatkuu rekursiivisesti.
  Avatussa ruudussa lukee sitä ympäröivien miinojen lukumäärä.
  (tehty)
- merkitä (liputtaa) ruudun, jonka hän uskoo olevan miinoitettu.
- avata kaikki tiettyä avattua ruutua ympäröivät, merkitsemättömät ruudut.
