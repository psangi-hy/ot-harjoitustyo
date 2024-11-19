En kyllä tiedä,
mitä tässä ajettiin takaa,
mutta toivon säälipisteitä yrityksestä.

```mermaid
 classDiagram
    Monopolipeli "1" -- "2" Noppa
    Monopolipeli "1" -- "1" Pelilauta
    Pelilauta "1" -- "40" Ruutu
    Ruutu "1" -- "1" Ruutu : seuraava
    Ruutu "1" -- "0..8" Pelinappula
    Pelinappula "1" -- "1" Pelaaja
    Pelaaja "2..8" -- "1" Monopolipeli
    Aloitusruutu --|> Ruutu
    Vankila --|> Ruutu
    Satumaa --|> Ruutu
    Yhteismaa --|> Ruutu
    Asema tai laitos --|> Ruutu
    Katu --|> Ruutu
    Aloitusruuru "1" -- "1" Monopolipeli
    Vankila "1" -- "1" Monopolipeli
    Toiminto "1" -- "1" Ruutu
    Kortti "30" -- "3" Satumaa
    Kortti "30" -- "3" Yhteismaa
    Toiminto "1" -- "1" Kortti
    Talo "0..4" -- "1" Katu
    Hotelli "0..1" -- "1" Katu
    Pelaaja "0..1" -- "1" Katu
    Lompakko "1" -- "1" Pelaaja
```
