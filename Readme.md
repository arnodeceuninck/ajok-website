# ajok-website

## Aanpassingen maken

[Klik hier](https://www.youtube.com/watch?v=QJXtWoqfDSU&list=PLWCUHLJwOfQaGwZz7ynJWnXey5gZwPfw5&ab_channel=ArnoDeceuninck) voor een playlist met de videos die hieronder vermeld staan.

### Github Account
Om de website te kunnen aanpassen, moet je [een account op GitHub aanmaken](https://github.com/signup). 

[Video: Github Account Aaanmaken](https://youtu.be/QJXtWoqfDSU)

Eens dit gebeurd is, kan je je gebruikersnaam en email doorgeven, zodat je toegevoegd kan worden aan de bewerkers van de site.

[Video: Accept invitation](https://youtu.be/rD1mVDDCnD4)

_Note: bij deze videos had ik nog niet door dat mijn microfoon uitstond, maar ik ben ervan overtuigd dat je deze stappen kan zonder uitleg_

### Waar aanpassingen maken
Dingen die typisch vaak veranderen, staan in de `_data` folder. 
Bv:
- `_data/kampen.yml` om info over kampen te updaten (datum, beschrijving...)
- `_data/peter_meters.yml` om peters en meters te updaten
- `_data/forms.yml` om inschrijvingsformulieren te updaten

[Video: Overlopen _data folder](https://youtu.be/MQvd1eHGmwI)

Wil je algemene tekst op de site updaten? Afhankelijk van de pagina, kan je dan `index.html`, `over-ons.html`, ... updaten.
De makkelijkste manier om te weten waar je iets moet aanpassen is door een stukje van de bestaande tekst die je wil aanpassen
op te zoeken via de zoekbalk bovenaan. 


#### Foto's
Op dezelfde plaatsen waar je tekst kan updaten, kan je ook de foto's updaten. Upload hiervoor eerst de afbeelding onder `assets/images`. Meeste foto's moeten in twee formaten geupload worden: verticaal (bv. 4:5, voor op desktop) en horizontaal (bv. 16:9, voor de gsm layout).

### Hoe aanpassen via GitHub website
Via de GitHub website kan je op het edit potloodje drukken, je tekst/datum/form/... aanpassen, op Commit changes drukken
en een Pull Request openen. Deze link kan je dan naar iemand anders doorsturen om je aanpassingen na te kijken. 

[Video: Aanpassen via Github website](https://youtu.be/m1l8Xl6JnqE)


### Pull Request
Om je code op de 'main' branch te krijgen, en dus live te zetten op de website, open je een Pull Request. Eens dit gebeurt is kan iemand anders je update nakijken en goedkeuren. Als dit gebeurt is, kan je de code naar de 'main'  branch brengen. Dan loopt er een actie die na enkele minuten je wijzigen effectief op de site zet. 

[Video: Pull Request Reviewen](https://youtu.be/f1QAfB5LxE0)

### Lokaal
Je kan ook de code op je eigen computer zetten om aanpassingen te maken en bv. te testen hoe je wijzigingen eruit gaan
zien. Hiervoor zijn er wel wat dingen die je moet doen:

- Github Desktop downloaden (of gewoon Git)
    - https://desktop.github.com/download/
- Visual Studio Code downloaden
    - https://code.visualstudio.com/
    - [Video: Github Desktop en Visual Studio Code Downloaden](https://youtu.be/KXOUwiUGD_4)
- Code lokaal krijgen
    - `Clone Git repository...` in Visual Studio Code selecteren
    - [Video: Bestanden op je computer krijgen](https://youtu.be/I_SLpZI-KAE)
- Jekyll downloaden
    - https://jekyllrb.com/docs/installation/windows/
    - [Video: Installatie Ruby en Jekyll](https://youtu.be/Im1LNr-MEdo)
- Website lokaal starten
    - `bundle install`
    - `bundle exec jekyll serve`
    - [Video: Website lokaal draaien](https://youtu.be/AutghP6-5j4)
    - [Video: Lokaal live aanpassing voorbeeld](https://youtu.be/C1p9v3GGfmY)

Eens dit in orde is, kan je lokaal aanpassingen maken en die (via een branch die niet 'main' is) terug
committen en naar de server brengen, zodat die via een pull request in de 'main' branch kunnen komen 
en dus op de website verschijnen. 

[Video: Waar code bewerken in meer detail](https://youtu.be/vFmH0GY2NTM)

[Video: Aanpassingen doorvoeren op website](https://youtu.be/UZYdBTQZRm4)

#### Branching
De code die je standaard op GitHub ziet is de 'main' branch. De code die hierop staat, komt overeen met de website. Daarom kan je niet rechstreeks daar wijzigingen toevoegen. Als je een nieuwe wijziging wil maken, maak je een nieuwe branch aan (gaat door bv. linksonder op 'main' te klikken en dan "Create new branch"). 

Hierop kan je je wijzigingen doen en testen. Eens dit klaar is, kan je je wijzigingen 'committen' (samenbundelen) en 'pushen' (van je lokale versie naar de GitHub server brengen). 


 

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