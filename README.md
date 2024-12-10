# Ohjelmistotekniikka, harjoitustyö

Miinaharavapeli, jossa graafinen käyttöliittymä ja mahdollisuus tallentaa pelitulokset.

[käyttöohje](/dokumentaatio/kayttoohje.md)
[vaatimusmäärittely](/dokumentaatio/vaatimusmaarittely.md)
[tuntikirjanpito](/dokumentaatio/tuntikirjanpito.md)
[muutosloki](/dokumentaatio/changelog.md)
[arkkitehtuuri](/dokumentaatio/arkkitehtuuri.md)

[release 1](https://github.com/psangi-hy/ot-harjoitustyo/releases/tag/viikko5)

## Ohje

Projekti vaatii Pythonin version 3.9 tai tätä uudemman sekä Poetryn.
Riippuvuuksien asennus onnistuu komennolla

	poetry install

ja ohjelman suoritus, testaus, testikattavuusraportin luonti ja linttaus tämän jälkeen komennoilla

	poetry run invoke {start|test|coverage-report|lint}
