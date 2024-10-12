# ajok-website
## Todo's
### Required features
- [ ] Template afbeeldingen updaten, dat er niet overal dezelfde afbeelding staat
- [ ] Vrijwilligers pagina
- [ ] Steun pagina
- [ ] Contact pagina
- [ ] Copyright jaartal onderaan (startjaar, eindjaar updatet al automatisch)
- [ ] Inschrijvingspagina (ik ben niet zo'n fan van embeded forms, liever inees doorlinken naar google forms), maar daarvoor nog algeemene pagina met inschrijvingsvoorwaarden kan wel handig zijn
- [ ] Makkeelijk aanpasbare variabel voor inschrijvigsvorm

### Required bugfixes
- [ ] Sections die niet altijd mooi aansluiten, bv. omdat de afbeelding te groot is
- [ ] Kamp aanbod tegels klikbaar maken
- [ ] Paaskamp knop gaat somehow niet nar paaskamp

### Nice to have bugfixes
- [ ] tekst overlapt soms boompjes in  de achtergrond
- [ ] Huidige heuveltjes afbeelding is een te lage resolutie, beter ergens een svg vinden

### Nice to haves
- [ ] Neem contact met ons op heeft nog wat layout updates nodig
- [ ] Meer variatie in secties, dat het niet altijd exact dezelfde boompjes en heuveltjes zijn
- [ ] Kamp aanbod tegels variabelen uit kampen.yml laten gebruiken

## Aanpassingen

### Tekst
Wil je info over kampen updaten? Pas dan het bestand `_data/kampen.yml` aan. 

Wil je algemene tekst op de site updaten? Afhankelijk van de pagina, kan je dan `index.html`, `over-ons.html`, ... updaten (in de hoofd folder).  

### Foto's
Op dezelfde plaatsen waar je tekst kan updaten, kan je ook de foto's updaten. Upload hiervoor eerst de afbeelding onder `assets/images`. Meeste foto's moeten in twee formaten geupload worden: verticaal (bv. 4:5, voor op desktop) en horizontaal (bv. 16:9, voor de gsm layout). 

## Development
Not familiar with jekyll, but already familiar with html/css/js? Here is a small step-by-step tutorial to get started with jekyll. https://jekyllrb.com/docs/step-by-step/01-setup/

## running
```
bundle exec jekyll serve
```