# Messe-Aussteller-Scraper – erste 10 Messen

Scrapt die Aussteller (Firmen) der ersten 10 Messen aus
`Messen in Deutschland.xlsx` und liefert pro Messe eine CSV plus eine
Gesamtdatei (`out/alle_aussteller.csv` + `.xlsx`).

## ⚠️ Voraussetzung: offener Netzwerk-Egress

Dieses Repo wurde in einer **Claude-Code-on-the-web-Umgebung mit Modus
„Package managers only"** erstellt. In diesem Modus ist **jeder** Zugriff auf
Messe-Websites gesperrt (403 am Gateway – verifiziert für `airtec.aero`,
`virtualmarket.cms-berlin.de`, `meine-afa.de`, sogar `google.com`). Nur
Paket-Registries (pypi, npm …) sind erreichbar. **Deshalb konnte der Scrape
nicht in der Umgebung selbst laufen.**

Zum Live-Scrapen brauchst du eine der beiden Freischaltungen:

1. **Environment-Netzwerk-Policy** beim Erstellen der Umgebung auf
   **„All domains"** (bzw. erweiterte Allowlist) stellen, dann Session neu
   starten. Danach kann Claude den Scrape direkt hier ausführen.
2. Org-Ebene: **claude.ai → Settings → Capabilities → Code Execution →
   *Allow Network Egress* → Domain Allowlist** und die unten stehenden Domains
   eintragen.

Alternativ läuft das Repo **lokal auf jeder Maschine mit Internet**.

### Minimale Domain-Allowlist (falls kein „All domains")

```
meine-afa.de, www.meine-afa.de, afag.de, www.afag.de
airtec.aero, www.airtec.aero
biomessen.info, www.biomessen.info, messeaugsburg.de, www.messeaugsburg.de
jagenundfischen.de, www.jagenundfischen.de
regioagrar-bayern.de, www.regioagrar-bayern.de
vendtra.com, www.vendtra.com
abenteuer-allrad.de, www.abenteuer-allrad.de
barconvent.com, www.barconvent.com
bazaar-berlin.de, www.bazaar-berlin.de, virtualmarket.bazaar-berlin.de
cms-berlin.de, www.cms-berlin.de, virtualmarket.cms-berlin.de
```
Hinweis: Directory-Plattformen laden Daten oft von Sub-/Fremd-Hosts
(CDNs, API-Domains). Falls einzelne Messen leer bleiben, ist „All domains"
der robusteste Weg.

## Ausführen

```bash
pip install -r requirements.txt
python -m playwright install chromium      # in CCR bereits vorhanden (PLAYWRIGHT_BROWSERS_PATH)
python scrape.py                 # alle 10 Messen
python scrape.py --only 9,10     # nur Bazaar + CMS (die mit XLS-Direktdownload)
python scrape.py --headful       # Browser sichtbar zum Debuggen
```

Ergebnis: `out/01_afa.csv … out/10_cms_berlin.csv`, `out/alle_aussteller.csv`,
`out/alle_aussteller.xlsx`. Spalten:
`messe, ort, aussteller, website, domain, stadt, land, halle_stand, quelle`.

## Wie es scrapt (Methode je Messe)

| # | Messe | Ort | Methode | Quelle |
|---|-------|-----|---------|--------|
| 1 | afa | Augsburg | browser (+PDF-Fallback) | meine-afa.de/ausstellerverzeichnis/ |
| 2 | AIRTEC | Augsburg | browser | airtec.aero/exhibitors2025/ |
| 3 | BioSüd | Augsburg | browser | biomessen.info/biosued/ |
| 4 | Jagen und Fischen | Augsburg | browser | jagenundfischen.de/…/ausstellerverzeichnis |
| 5 | RegioAgrar Bayern | Augsburg | browser | regioagrar-bayern.de/ausstellerverzeichnis/ |
| 6 | VENDTRA | Augsburg | browser | vendtra.com |
| 7 | Abenteuer & Allrad | Bad Kissingen | browser | abenteuer-allrad.de |
| 8 | Bar Convent Berlin | Berlin | browser (RX-JSON) | barconvent.com/…/exhibitor-directory.html |
| 9 | Bazaar Berlin | Berlin | **download XLS** | virtualmarket.bazaar-berlin.de/download/exhibitor-lists/Ausstellerliste.xls |
| 10 | CMS Berlin | Berlin | **download XLS** | virtualmarket.cms-berlin.de/…/Ausstellerliste.xls |

**Kernidee des Browser-Modus:** Beim Rendern wird der komplette XHR/fetch-Traffic
mitgeschnitten. Aussteller-Verzeichnisse laden ihre Daten praktisch immer aus
einer JSON-API – der Scraper fischt automatisch das JSON-Array mit den Firmen
heraus (vollständig, inkl. Website/Stand). Erst wenn kein JSON gefunden wird,
greift die DOM-Extraktion per CSS-Selektor (mit Auto-Scroll & „Mehr laden").

## Robustheit / bekannte Stolpersteine

- **Selektoren/URLs sind Best-Effort** und in `fairs.json` zentral anpassbar.
  Konnte in der gesperrten Umgebung nicht gegen die Live-Seiten getestet werden.
- Ändert eine Messe ihre Directory-URL (Jahres-Slug wie `exhibitors2025`),
  in `fairs.json` aktualisieren.
- Der **VMP-XLS-Download** (Messe Berlin) ist der zuverlässigste Weg; falls die
  Datei 404't, springt der Code automatisch auf den Browser-Modus der
  `/ausstellerliste`-Seite.
- PDF-Extraktion (afa) ist heuristisch – Ergebnis stichprobenartig prüfen.

## Rechtliches

Nur öffentlich zugängliche Ausstellerverzeichnisse. `robots.txt`/AGB der
Betreiber und DSGVO (bei personenbezogenen Kontaktdaten) beachten; moderate
Request-Rate. Für rein kommerzielle Adressnutzung ggf. die offiziellen,
lizenzierten Listen der Veranstalter verwenden.
