Testaus
=======

Sovellusta ollaan testattu automaattisesti yksikkötestein
sekä manuaalisesti pelaamalla peliä ja toteamalla,
että se toimii.
Testikattavuusraportin alaisina ovat tiedosto `main.py`
sekä `game`-hakemiston tiedostot `game_state.py` ja `scores.py`.
Haaraumakattavuus on näissä 91%.
Tiedostossa `main.py` ei ole funktioita joita testata,
ja sen olisikin ehkä voinut jättää testikattavuuden ulkopuolelle.
Tiedostossa `game_state.py` taas on jäänyt testaamatta ensinnäkin tietyt haarat,
jotka käsittelevät miinojen satunnaisasettelua,
sillä muissa testeissä käytetään enimmäkseen esimääriteltyä asettelua.
Itse satunnaisasettelun toimivuutta testataan kuitenkin automaattisesti.
Lisäksi automaattitestausta vailla ovat triviaalit funktiot,
jotka ilmoittavat,
onko peli hävitty tai voitettu.
Manuaalisessa testauksessa nämäkin ovat joka tapauksessa osoittautuneet toimiviksi.
