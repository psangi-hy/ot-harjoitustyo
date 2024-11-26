# Ohjelmistotekniikka, harjoitustyö

Miinaharavapeli, jossa graafinen käyttöliittymä ja mahdollisuus tallentaa pelitulokset.

[vaatimusmäärittely](/dokumentaatio/vaatimusmaarittely.md)
[tuntikirjanpito](/dokumentaatio/tuntikirjanpito.md)
[muutosloki](/dokumentaatio/changelog.md)
[arkkitehtuuri](/dokumentaatio/arkkitehtuuri.md)

## Ohje

Projekti vaatii Pythonin version 3.9 tai tätä uudemman sekä Poetryn.
Riippuvuuksien asennus onnistoo komennolla

	poetry install

ja ohjelman suoritus, testaus, testikattavuusraportin luonti ja linttaus tämän jälkeen komennoilla

	poetry run invoke {start|test|coverage-report|lint}
