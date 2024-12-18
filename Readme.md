# ajok-website
## Todo's

### Inhoudelijk
/

### Required features
/

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
For faster static website loading times, it is best to compress all your images. I used [XnConvert](https://www.xnview.com/en/xnconvert/#downloads) for this. (I also tried some jekyll plugins, but those give less compression configuration options and are not supported on the Github runner)

In input, select `assets-original` as source folder. Set the output to the `assets` folder, format `WebP` , with `File size` e.g. `100kbytes` as settings. 

You can check the loading speeds with sites like this one: https://gtmetrix.com/

Before using compressed images: Homepage 1.4s to fully load, 17.5 MB (https://gtmetrix.com/reports/arnodeceuninck.github.io/SdANANEp/)
After compressing to 100kb and converting to webp: Homepage 0.8s to fully load, 2.53Mb (https://gtmetrix.com/reports/arnodeceuninck.github.io/tAtjmTx8/)

### Lazy loading
Enable lazy loading for all images by adding `loading="lazy"`. More info: https://gtmetrix.com/defer-offscreen-images.html