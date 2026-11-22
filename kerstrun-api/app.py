"""Kerstrun rondjes API.

Small HTTP service that periodically reads the total number of bought
Kerstrun rondjes from a Google Sheet (sum of column D, from row 2 down)
and serves the last successfully fetched value as JSON.

- Google is polled in the background; requests never wait on Google.
- If a refresh fails, the last good value keeps being served.
- The last good value is persisted to disk, so it survives restarts.
"""

import json
import logging
import os
import threading
import time
from datetime import datetime, timezone
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import quote

from google.auth.transport.requests import AuthorizedSession
from google.oauth2 import service_account

SPREADSHEET_ID = os.environ.get("SPREADSHEET_ID", "1d3_Fa4MsWha5LlijVDB9v5NOqDsaU_0kK0moxnINH6Y")
SHEET_GID = int(os.environ.get("SHEET_GID", "1174835771"))
SUM_RANGE = os.environ.get("SUM_RANGE", "D2:D")
CREDENTIALS_FILE = os.environ.get("GOOGLE_APPLICATION_CREDENTIALS", "/secrets/service-account.json")
STATE_FILE = os.environ.get("STATE_FILE", "/data/state.json")
REFRESH_SECONDS = max(10, int(os.environ.get("REFRESH_SECONDS", "60")))
PORT = int(os.environ.get("PORT", "8080"))
# Comma separated list of origins allowed to call the API, or "*".
ALLOWED_ORIGINS = [o.strip() for o in os.environ.get("ALLOWED_ORIGINS", "https://ajokvzw.be,https://www.ajokvzw.be").split(",") if o.strip()]

SHEETS_API = "https://sheets.googleapis.com/v4/spreadsheets"
SCOPES = ["https://www.googleapis.com/auth/spreadsheets.readonly"]

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
log = logging.getLogger("kerstrun-api")


def now_iso():
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


class State:
    def __init__(self, path):
        self.path = path
        self.lock = threading.Lock()
        self.rondjes = None
        self.updated_at = None  # time of last successful fetch
        self.last_attempt_at = None
        self.last_error = None
        self._load()

    def _load(self):
        try:
            with open(self.path, encoding="utf-8") as f:
                data = json.load(f)
            self.rondjes = data["rondjes"]
            self.updated_at = data["updated_at"]
            log.info("Loaded persisted value %s (from %s)", self.rondjes, self.updated_at)
        except FileNotFoundError:
            log.info("No persisted state yet at %s", self.path)
        except Exception:
            log.exception("Could not read persisted state, starting empty")

    def set_success(self, rondjes):
        with self.lock:
            self.rondjes = rondjes
            self.updated_at = self.last_attempt_at = now_iso()
            self.last_error = None
            snapshot = {"rondjes": self.rondjes, "updated_at": self.updated_at}
        try:
            os.makedirs(os.path.dirname(self.path) or ".", exist_ok=True)
            tmp = self.path + ".tmp"
            with open(tmp, "w", encoding="utf-8") as f:
                json.dump(snapshot, f)
            os.replace(tmp, self.path)  # atomic, never leaves a half-written file
        except Exception:
            log.exception("Could not persist state")

    def set_failure(self, error):
        with self.lock:
            self.last_attempt_at = now_iso()
            self.last_error = str(error)

    def snapshot(self):
        with self.lock:
            return {
                "rondjes": self.rondjes,
                "updated_at": self.updated_at,
                "last_attempt_at": self.last_attempt_at,
                "stale": self.last_error is not None,
            }


def to_number(value):
    if isinstance(value, bool):
        return 0
    if isinstance(value, (int, float)):
        return value
    if isinstance(value, str):
        text = value.strip().replace(" ", "").replace(",", ".")
        if not text:
            return 0
        try:
            return float(text)
        except ValueError:
            return 0
    return 0


class SheetReader:
    def __init__(self):
        creds = service_account.Credentials.from_service_account_file(CREDENTIALS_FILE, scopes=SCOPES)
        self.session = AuthorizedSession(creds)
        self.sheet_title = None

    def _resolve_sheet_title(self):
        resp = self.session.get(
            f"{SHEETS_API}/{SPREADSHEET_ID}",
            params={"fields": "sheets.properties(sheetId,title)"},
            timeout=15,
        )
        resp.raise_for_status()
        for sheet in resp.json().get("sheets", []):
            props = sheet.get("properties", {})
            if props.get("sheetId") == SHEET_GID:
                return props["title"]
        raise RuntimeError(f"No sheet with gid {SHEET_GID} in spreadsheet")

    def fetch_total(self):
        # Resolve the tab name from its gid every time, so renaming the tab doesn't break us.
        self.sheet_title = self._resolve_sheet_title()
        a1 = "'" + self.sheet_title.replace("'", "''") + "'!" + SUM_RANGE
        resp = self.session.get(
            f"{SHEETS_API}/{SPREADSHEET_ID}/values/{quote(a1, safe='')}",
            params={"valueRenderOption": "UNFORMATTED_VALUE", "majorDimension": "COLUMNS"},
            timeout=15,
        )
        resp.raise_for_status()
        columns = resp.json().get("values", [])
        total = sum(to_number(v) for col in columns for v in col)
        return int(total) if float(total).is_integer() else round(total, 2)


def refresh_loop(state, stop):
    reader = None
    while not stop.is_set():
        try:
            if reader is None:
                reader = SheetReader()
            total = reader.fetch_total()
            state.set_success(total)
            log.info("Refreshed: %s rondjes", total)
        except Exception as exc:
            state.set_failure(exc)
            log.warning("Refresh failed, keeping last value %s: %s", state.rondjes, exc)
        stop.wait(REFRESH_SECONDS)


def make_handler(state):
    class Handler(BaseHTTPRequestHandler):
        server_version = "kerstrun-api"

        def _cors(self):
            origin = self.headers.get("Origin")
            if "*" in ALLOWED_ORIGINS:
                self.send_header("Access-Control-Allow-Origin", "*")
            elif origin and origin in ALLOWED_ORIGINS:
                self.send_header("Access-Control-Allow-Origin", origin)
                self.send_header("Vary", "Origin")

        def _json(self, status, body, cache_seconds=0):
            payload = json.dumps(body).encode("utf-8")
            self.send_response(status)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.send_header("Content-Length", str(len(payload)))
            self.send_header("Cache-Control", f"public, max-age={cache_seconds}" if cache_seconds else "no-store")
            self._cors()
            self.end_headers()
            self.wfile.write(payload)

        def do_OPTIONS(self):
            self.send_response(204)
            self._cors()
            self.send_header("Access-Control-Allow-Methods", "GET, OPTIONS")
            self.send_header("Access-Control-Max-Age", "86400")
            self.end_headers()

        def do_GET(self):
            path = self.path.split("?", 1)[0].rstrip("/") or "/"
            if path in ("/", "/rondjes"):
                snap = state.snapshot()
                if snap["rondjes"] is None:
                    self._json(503, {"error": "no value available yet", **snap})
                else:
                    self._json(200, snap, cache_seconds=min(30, REFRESH_SECONDS))
            elif path == "/health":
                self._json(200, {"ok": True, **state.snapshot()})
            else:
                self._json(404, {"error": "not found"})

        def log_message(self, fmt, *args):
            pass  # keep logs focused on refreshes

    return Handler


def main():
    state = State(STATE_FILE)
    stop = threading.Event()
    threading.Thread(target=refresh_loop, args=(state, stop), daemon=True).start()
    server = ThreadingHTTPServer(("0.0.0.0", PORT), make_handler(state))
    log.info("Listening on :%s, refreshing every %ss", PORT, REFRESH_SECONDS)
    try:
        server.serve_forever()
    finally:
        stop.set()


if __name__ == "__main__":
    main()
