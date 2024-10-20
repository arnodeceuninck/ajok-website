# ajok-website
## Todo's

### Inhoudelijk
- [ ] Inhoud van alle teksten moet sowieso nog eens afgecheckt worden, is nu gewoon overgenomen van mockups, maar zitten ook wel dingen tussen waar ik m'n twijfels bij heb
- [ ] Doe een gift -> geen automatische vermelding op site zou ik denken, is pas voor peter/meter
- Regels op kamp en evenementen heb ik weggehouden van de vrijwilligerspagina (evenementen staan nu ook nergens, want die info kan heel makkelijk outdated worden). Indien toch gewenst, mss beter iets maken in de stijl van "Houd onze facebook in 't oog voor onze evenementen"

### Required features
- [ ] Copyright jaartal onderaan (startjaar, eindjaar updatet al automatisch)

### Required bugfixes
/

### Nice to have bugfixes
- [ ] tekst overlapt soms boompjes in  de achtergrond
- [ ] Huidige heuveltjes afbeelding is een te lage resolutie, beter ergens een svg vinden

### Nice to haves
- [ ] Meer variatie in secties, dat het niet altijd exact dezelfde boompjes en heuveltjes zijn
- [ ] QR code voor peter/meter betaling?

## Aanpassingen

### Tekst
Wil je info over kampen updaten? Pas dan het bestand `_data/kampen.yml` aan. 

Wil je algemene tekst op de site updaten? Afhankelijk van de pagina, kan je dan `index.html`, `over-ons.html`, ... updaten (in de hoofd folder).  

### Foto's
Op dezelfde plaatsen waar je tekst kan updaten, kan je ook de foto's updaten. Upload hiervoor eerst de afbeelding onder `assets/images`. Meeste foto's moeten in twee formaten geupload worden: verticaal (bv. 4:5, voor op desktop) en horizontaal (bv. 16:9, voor de gsm layout). 

## Development
Not familiar with jekyll, but already familiar with html/css/js? Here is a small step-by-step tutorial to get started with jekyll. https://jekyllrb.com/docs/step-by-step/01-setup/

### installing
- Install jekyll: https://jekyllrb.com/docs/installation/windows/
- `bundle install`

### running
```
bundle exec jekyll serve
```

### image compression
For faster static website loading times, it is best to compress all your images. I used XnConvert for this. 

In input, select `assets-original` as source folder. Set the output to the `assets` folder, format `WebP` , with `File size` e.g. `100kbytes` as settings. 

You can check the loading speeds with sites like this one: https://gtmetrix.com/reports/arnodeceuninck.github.io/SdANANEp/

Before using compressed images: Homepage 1.4s to fully load, 17.5 MB
After compressing to 100kb and converting to webp: 