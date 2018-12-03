# ADA_hf

A fájlban **két függvény található**.

### degrees2meters(lat, long)
A hosszúsági és szélességi koordinátákat alakítja [Mercator-vetületre](https://hu.wikipedia.org/wiki/Mercator-vet%C3%BClet). Bemenete egy hosszúság/szélesség értékpár, kimenete egy Mercator-féle x és y érték.

### from_lat_long_to_mercator_array(lat, long)
A degrees2meters függvényt használja fel abból a célból, hogy tömböket is könynen lehessen konvertálni vele.

### Felhasznált könyvtárak:
 * numpy
 * webbrowser (a localhostról történő ellenőrzés miatt)
