# Setup – Meeting-Performance-Report (tägliche Cloud-Routine)

Diese Routine läuft 1× täglich in der Cloud, loggt sich per Headless-Browser in
`app.amplifa.ai` ein, zählt die Meetings pro Kunde (rollierende 7 Tage) und
schreibt einen Snapshot nach Notion. Drei Dinge müssen **einmalig** eingerichtet
werden:

## 1. Egress-Policy öffnen (Pflicht)
Aktuell blockt die Netzwerk-Policy dieser Cloud-Umgebung `app.amplifa.ai`
(403 / „policy denial"). Ohne Freigabe kann die Routine die App nicht erreichen.
→ In der Umgebungskonfiguration (Claude Code on the web) `app.amplifa.ai` zur
erlaubten Egress-Liste hinzufügen. Doku: https://code.claude.com/docs/en/claude-code-on-the-web

## 2. Secrets hinterlegen (Pflicht)
Als Umgebungs-Secrets (nicht im Repo!):
- `AMPLIFA_EMAIL` – Login-E-Mail eines amplifa-Accounts mit Admin/Reports-Zugriff
- `AMPLIFA_PASSWORD` – zugehöriges Passwort (App-eigener Login, **kein** Google-SSO)

Optional:
- `AMPLIFA_BASE_URL` (Default `https://app.amplifa.ai`)
- `AMPLIFA_REPORTS_PATH` (Default `/admin/reports`, falls die Reports woanders liegen)

## 3. Täglichen Trigger anlegen (Pflicht)
Der richtige Mechanismus für eine dauerhafte tägliche Cloud-Routine ist ein
**wiederkehrender geplanter Trigger/Session** in der Claude-Code-Web-Oberfläche,
der diesen Skill aufruft. Empfohlener Prompt des Triggers:

> Führe den Skill `meeting-performance-report` aus.

Empfohlene Zeit: morgens, z. B. 07:57 lokale Zeit (krumme Minute, damit nicht
alle Jobs gleichzeitig feuern). In-Session-Crons (`CronCreate`) sind hierfür
**nicht** geeignet – sie sterben mit der Session und feuern in einer ephemeren
Umgebung nicht zuverlässig.

## Erststart / Kalibrierung
Beim allerersten Lauf kennt der Scraper die echten Selektoren von amplifa noch
nicht. Die Routine (SKILL.md, Schritt 1) inspiziert dann die echte Seite,
schreibt die ermittelten Selektoren nach `selectors.json` und committet sie.
Ab dann laufen die täglichen Läufe deterministisch über `scrape.mjs`.

**Schneller geht's mit deiner Hilfe:** Schick mir einmal die Reports-Seite
(Screenshot oder den HTML-Ausschnitt der Tabelle) + die exakte URL des
Admin/Reports-Bereichs. Dann trage ich die Selektoren sofort in `selectors.json`
ein und die Kalibrierungs-Runde entfällt.

## Manueller Testlauf (lokal oder nach Policy-Freigabe)
```bash
cd .claude/skills/meeting-performance-report
npm install
npx playwright install chromium
AMPLIFA_EMAIL=... AMPLIFA_PASSWORD=... SCRAPE_DEBUG=1 node scrape.mjs
```
Bei Problemen liegen Screenshot + HTML unter `debug/` zum Kalibrieren der
Selektoren in `selectors.json`.

## Notion
Die Routine legt die DB **„amplifa Meeting-Performance (7-Tage)"** beim ersten
Lauf selbst an (Schema in SKILL.md) und schreibt täglich pro Kunde einen
Snapshot mit Trend und Einordnung (Gut / Mittel / Schwach / Neu). Die Ansicht
„Heute – Handlungsbedarf" sortiert die optimierungsbedürftigen Kunden nach oben.
