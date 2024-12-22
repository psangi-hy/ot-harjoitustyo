Käyttöohje
==========

Asenna ennen pelin käynnistämistä tarvittavat riippuvuudet komennolla

	poetry install

Tämän jälkeen peli käynnistyy komennolla

	poetry run invoke start

Pelaaminen
----------

Jos ajat ohjelman graafisella työpöydällä, pitäisi pelin avautua uudessa ikkunassa.
Yläpalkin Uusi peli -valikosta voit aloittaa pelin haluamillasi asetuksilla.
Helppo, Keskitaso ja Vaikea ovat esimääriteltyjä vaikeustasoja,
kun taas Mukautettu pyytää sinua erikseen syöttämään pelikentän koon ja miinojen lukumäärän.

Peli asettelee miinat satunnaisesti pelikentälle.
Pelikentän ruudun voi avata napsauttamalla sitä hiiren vasemmalla painikkeella.
Jos ruudussa on miina, häviät pelin.
Muussa tapauksessa ruutuun ilmestyy numero, joka ilmaisee sen,
kuinka monessa ympäröivässä ruudussa on miina.

Napsauttamalla avaammatonta ruutua hiiren oikealla painikkeella asetat siihen lipun.
Lipulla voit merkitä niitä ruutuja, jotka tiedät miinoitetuiksi.
Lipulla merkittyä ruutua ei voi avata, ennen kuin siitä poistaa lipun
napsauttamalla sitä uudestaan hiiren oikealla painikkeella.

Napsauttamalla jo avattua ruutua hiiren keskipainikkeella voit avata kaikki sitä
ympäröivät, avaamattomat ruudut.
Tämä edellyttää sitä, että ruudussa lukevaa numeroa vastaava lukumäärä ympäröiviä
ruutuja on merkitty lipulla.

Kun olet avannut kaikki ruudut paitsi ne, joissa on miinoja, voitat pelin.
Tällöin on sinulla mahdollisuus tallentaa pelituloksesi syöttämällä nimimerkkisi.
Yläpalkin Tuloslista-painike avaa uudessa ikkunassa näkymän,
jossa on kymmenen parasta nykyistä vaikeustasoa vastaavaa tulosta nimimerkkeineen.
