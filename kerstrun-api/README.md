# kerstrun-api

Kleine API die het totaal aantal gekochte Kerstrun-rondjes (som van `D2:D` in de Google Sheet) serveert,
zodat de statische website de actuele teller kan tonen.

```
GET /rondjes  ->  {"rondjes": 52, "updated_at": "2026-11-22T14:03:00+00:00", "last_attempt_at": "...", "stale": false}
GET /health
```

## Betrouwbaarheid

- De API vraagt Google elke `REFRESH_SECONDS` (standaard 60 s) op de achtergrond; een request wacht nooit op Google.
- Lukt een refresh niet, dan blijft de laatst geslaagde waarde geserveerd (`stale: true`).
- De laatst geslaagde waarde wordt bewaard in `/data/state.json` (Docker volume), dus ook na een herstart.
- Op de website toont de browser meteen de laatst gekende waarde (localStorage, of `rondjes_verkocht` uit
  `_data/kerstrun.yml` als die nieuwer is) en vervangt die zodra de API antwoordt. Is de API onbereikbaar,
  dan blijft die waarde staan.

## Setup

1. **Service account** – In Google Cloud Console: maak een project, activeer de *Google Sheets API*,
   maak een service account en download een JSON-key.
2. **Deel de sheet** met het e-mailadres van het service account (`...@...iam.gserviceaccount.com`) als *Lezer*.
3. Zet de key op de server als `kerstrun-api/secrets/service-account.json` (staat in `.gitignore`).
4. Start:
   ```sh
   cd kerstrun-api
   docker compose up -d --build
   docker compose logs -f   # verwacht: "Refreshed: N rondjes"
   ```
5. Zet er een HTTPS reverse proxy voor (de website draait op https, dus de API moet ook https zijn),
   bv. Caddy:
   ```
   kerstrun.arnodece.com {
       reverse_proxy localhost:8080
   }
   ```
6. Zet die URL in `_data/kerstrun.yml` als `api_url` (bv. `https://kerstrun.arnodece.com/rondjes`).
   Leeg laten schakelt de live teller uit.

## Configuratie (env vars)

| Variabele | Standaard | Uitleg |
|---|---|---|
| `SPREADSHEET_ID` | Kerstrun sheet | ID uit de sheet-URL |
| `SHEET_GID` | `1174835771` | `gid` van het tabblad (tabnaam mag dus wijzigen) |
| `SUM_RANGE` | `D2:D` | Bereik dat opgeteld wordt |
| `REFRESH_SECONDS` | `60` | Hoe vaak Google bevraagd wordt (min. 10) |
| `ALLOWED_ORIGINS` | `https://ajokvzw.be,https://www.ajokvzw.be` | CORS origins, komma-gescheiden, of `*` |
| `GOOGLE_APPLICATION_CREDENTIALS` | `/secrets/service-account.json` | Pad naar de service-account key |
| `STATE_FILE` | `/data/state.json` | Waar de laatste waarde bewaard wordt |
| `PORT` | `8080` | |
