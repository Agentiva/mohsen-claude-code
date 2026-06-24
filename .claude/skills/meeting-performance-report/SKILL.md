---
name: meeting-performance-report
description: >
  Tägliche Cloud-Routine: öffnet app.amplifa.ai per Headless-Browser
  (App-eigener Login, kein Google-SSO), liest im Admin/Reports pro Kunde die
  Meetings der rollierenden letzten 7 Tage aus und schreibt einen täglichen
  Snapshot in eine Notion-Datenbank – inkl. Trend (vs. Vorwoche) und Einordnung
  (Gut / Mittel / Schwach / Neu), damit auf einen Blick sichtbar ist, welche
  Kunden performen und wo optimiert werden muss. Läuft UNBEAUFSICHTIGT – stellt
  KEINE Rückfragen, trifft Best-Effort-Entscheidungen und loggt Unklarheiten.
---

# Meeting-Performance-Report (Routine)

Diese SKILL.md ist der **Routine-Prompt**. Sie läuft 1× täglich unbeaufsichtigt
(geplanter Trigger / Cron, siehe `SETUP.md`). Keine Rückfragen, keine
destruktiven Aktionen. Nur: einloggen → Zahlen lesen → Snapshot nach Notion.

Voraussetzungen (siehe `SETUP.md`): Secrets `AMPLIFA_EMAIL`, `AMPLIFA_PASSWORD`
gesetzt und `app.amplifa.ai` in der Egress-Policy der Umgebung freigegeben.

## 0. Vorbereitung (jeder Lauf)
Arbeitsverzeichnis: `.claude/skills/meeting-performance-report/`.
- Abhängigkeiten sicherstellen (idempotent):
  `npm install --no-audit --no-fund` und falls Chromium fehlt
  `npx playwright install chromium`.
- Prüfen, ob `selectors.json` existiert. Wenn nicht → **erst Schritt 1
  (Kalibrierung)**, sonst direkt Schritt 2.

## 1. Kalibrierung (nur Erststart oder wenn der Scraper fehlschlägt)
Der Scraper ist deterministisch und braucht die echten Selektoren von amplifa.
Beim allerersten Lauf (oder wenn `node scrape.mjs` mit
„Selektoren kalibrieren / keine Kundenzeilen" abbricht):
1. Mit Playwright die echte Seite inspizieren – Login-Seite öffnen, einloggen,
   `selectors.example.json → reports.path` ansteuern. Bei Bedarf
   `debug/*.html` + `debug/*.png` (vom letzten Scraper-Fehlversuch) lesen.
2. Die echten Selektoren ermitteln für: Login (E-Mail-, Passwort-Feld,
   Submit, Logged-in-Marker), Reports-Pfad, ggf. 7-Tage-Filter, und die
   Tabelle (Zeile, Kundenname, Meeting-Zahl-Spalte).
3. `selectors.example.json` nach `selectors.json` kopieren, die ermittelten
   Werte eintragen, **committen und pushen** (damit künftige ephemere Cloud-Läufe
   sie haben). Branch: der aktuelle Arbeitsbranch.
4. Danach Schritt 2 normal ausführen.

Wichtig: Passwörter/Secrets niemals in `selectors.json`, Logs oder Commits
schreiben – nur Selektoren.

## 2. Zahlen ziehen (Normalbetrieb)
- `node scrape.mjs` ausführen. Erwartete Ausgabe (eine JSON-Zeile):
  `{ ok:true, rangeDays:7, customers:[{ name, meetings }, ...] }`.
- Bei `ok:false`: einmalig Schritt 1 (Kalibrierung) versuchen, dann erneut.
  Schlägt es wieder fehl → Notion-Snapshot mit Status-Hinweis „Scrape
  fehlgeschlagen" (siehe unten) anlegen statt still zu sterben, und den Fehler
  inkl. `debug/`-Pfad in der Snapshot-Notiz vermerken.

## 3. Notion-Datenbank pflegen
Ziel-DB: **„amplifa Meeting-Performance (7-Tage)"**. Existiert sie nicht,
einmalig mit diesem Schema anlegen (per Notion-MCP):

| Feld | Typ | Inhalt |
|---|---|---|
| Kunde | Title | Kundenname |
| Datum | Date | Snapshot-Datum (heute, lokale Zeit) |
| Meetings 7T | Number | Meetings der letzten 7 Tage |
| Vorwoche 7T | Number | „Meetings 7T" aus dem Snapshot von vor 7 Tagen (sofern vorhanden) |
| Δ Woche | Number | Meetings 7T − Vorwoche 7T |
| Trend | Select | ▲ steigend / → stabil / ▼ fallend |
| Einordnung | Select | Gut / Mittel / Schwach / Neu |
| Quelle | URL | Reports-URL |

Pro Lauf **ein neuer Snapshot-Eintrag pro Kunde** (kein Überschreiben – die
Historie ist gewollt, daraus entstehen Trends).

## 4. Einordnung & Trend berechnen (transparent, pro Kunde)
Vor dem Schreiben für jeden Kunden seine **bestehende Historie** aus der Notion-DB
lesen (frühere Snapshots, nur Datum < heute):
- **Baseline** = Durchschnitt von „Meetings 7T" über die letzten bis zu 4
  vorherigen Snapshots dieses Kunden.
- **Vorwoche 7T** = Wert aus dem Snapshot, der ~7 Tage zurückliegt (nächst-
  gelegener). Fehlt er → leer lassen, Δ/Trend dann leer.
- **Trend**: Δ ≥ +1 → „▲ steigend"; Δ ≤ −1 → „▼ fallend"; sonst „→ stabil".
- **Einordnung**:
  - keine Historie → **Neu**
  - `meetings == 0` ODER `meetings ≤ 0.7 × Baseline` → **Schwach**
  - `meetings ≥ 1.1 × Baseline` → **Gut**
  - sonst → **Mittel**

Bei fehlgeschlagenem Scrape: einen einzigen Eintrag „⚠ Scrape fehlgeschlagen"
(Kunde-Feld) mit heutigem Datum + Fehlernotiz anlegen, restliche Felder leer.

## 5. Sortier-Ansicht sicherstellen
Einmalig eine Notion-Ansicht „Heute – Handlungsbedarf" anlegen/erhalten:
gefiltert auf Datum = heute, sortiert nach Einordnung (Schwach zuerst), dann Δ
aufsteigend. So stehen die optimierungsbedürftigen Kunden oben.

## Leitplanken (unbeaufsichtigt!)
- Keine Rückfragen. Bei Unklarheit Best-Effort + Notiz im Snapshot.
- Nichts in Notion löschen/überschreiben – nur anlegen/ergänzen.
- Secrets niemals loggen, committen oder nach Notion schreiben.
- Egress-Block (`app.amplifa.ai` nicht erreichbar) ist KEIN Code-Fehler:
  einen „⚠ Quelle nicht erreichbar"-Snapshot anlegen und beenden.
- Nur lesen auf amplifa-Seite – niemals dort etwas anklicken/ändern, das Daten
  verändert (keine Buttons außer Navigation/Filter).
