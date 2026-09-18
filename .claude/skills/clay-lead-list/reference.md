# Referenz – Clay Lead-List-Builder

Nachschlagewerk zu SKILL.md. Nur lesen, wenn der jeweilige Schritt es braucht.

## Spaltenschema (verbindlich)

`lead_import_template.csv` des Kunden:

```
email,first_name,last_name,full_name,job_title,company,company_website,linkedin_url,location
```

Was dieser Skill erzeugt – **identisch, nur ohne `email`**:

```
first_name,last_name,full_name,job_title,company,company_website,linkedin_url,location
```

| Spalte | Inhalt | Firmenliste |
|---|---|---|
| `first_name` | Vorname | leer |
| `last_name` | Nachname | leer |
| `full_name` | „Vorname Nachname" | leer |
| `job_title` | Jobtitel im Original (nicht eindeutschen) | leer |
| `company` | Firmenname wie geführt (Rechtsform behalten) | **gefüllt** |
| `company_website` | nackte Domain, ohne Schema/`www.`/Pfad | **gefüllt** |
| `linkedin_url` | `https://linkedin.com/in/...` bzw. `/company/...` | optional |
| `location` | Stadt bzw. „Stadt, Land" | optional |

Warum keine E-Mail: amplifa betreibt seine eigene Adressfindung. Eine Clay-E-Mail-Anreicherung kostet Credits und wird beim Import nicht gebraucht.

## Clay – Route A (Connector, Default)

| Ziel | Tool |
|---|---|
| Workspace bestätigen | `get-current-workspace` |
| Einzelne Firma prüfen/anreichern | `find-and-enrich-company` |
| Kontakte nach Rolle/Titel je Firma | `find-and-enrich-contacts-at-company` |
| Namentlich bekannte Kontakte | `find-and-enrich-list-of-contacts` |
| Nachträglich anreichern (Task-ID nötig) | `add-contact-data-points`, `add-company-data-points` |
| Laufenden Task/Ergebnisse abholen | `get-task` (seitenweise, 100 Entities/Seite) |
| Eigene Accounts/CRM-Daten des Workspace | `query-objects`, `ask-question-about-accounts` |
| Workspace-eigene Enrichment-Funktionen | `list_subroutines`, `run_subroutine` |

Praxis:
- `companyIdentifier` ist **Domain oder LinkedIn-Company-URL**, nie der bloße Firmenname.
- Zusammengesetzte Titel bleiben **ein** String: `["Head of Logistics"]`, nicht `["Head","Logistics"]`.
- Filter sind UND-verknüpft, Werte innerhalb eines Filters ODER.
- Spezifisch filtern: `"Software Engineer"` statt `"Engineer"` (sonst matcht „Sales Engineer").
- Suchen laufen asynchron: Task-ID merken und mit `get-task` pollen, statt zu raten.
- **Keine `dataPoints` setzen, die der User nicht verlangt hat** – jede Anreicherung kostet Credits. `Email` grundsätzlich nie.
- Ergebnisse als JSON in eine Datei schreiben und durchs Skript schicken, nicht im Chat umformatieren.

## Clay – Route B (im Browser)

Nur, wenn Route A die Aufgabe nicht abdeckt: bestehende Clay-Tabelle, UI-only-Enrichment, fertiger Table-Export.

Umgebung: Chromium ist vorinstalliert, `PLAYWRIGHT_BROWSERS_PATH=/opt/pw-browsers`, `PLAYWRIGHT_SKIP_BROWSER_DOWNLOAD=1`. **Kein `playwright install` ausführen.** Pinnt ein Projekt eine andere Playwright-Version, mit `executablePath: '/opt/pw-browsers/chromium'` starten.

Ablauf:
1. Browser mit **persistentem User-Data-Dir** starten, damit eine bestehende Clay-Session wiederverwendet wird.
2. `https://app.clay.com` öffnen und prüfen, ob eingeloggt.
3. Eingeloggt → Tabelle ansteuern, Daten bzw. CSV-Export ziehen, Datei durchs Skript schicken.
4. **Nicht eingeloggt → abbrechen, dem User sagen, auf Route A wechseln.** Niemals nach Passwort/2FA fragen, keine Zugangsdaten in Code oder Dateien schreiben, keine Login-Automatisierung bauen.

Grenzen ehrlich benennen: Die Clay-UI ändert sich, Selektoren brechen. Bricht Route B, ist das ein Grund für Route A – kein Grund, Daten zu erfinden oder eine halbe Liste als vollständig zu verkaufen.

## amplifa-Import

Reihenfolge: `organization_list` → `agent_list` → `lead_import_preview` → `agent_import_leads` → `lead_import_status`.

**CSV übergeben** – zwei Wege, beide erwartet dieselbe Datei:

```bash
# Variante A: Data-URI
printf 'data:text/csv;name=leads.csv;base64,%s' "$(base64 -w0 leads.csv)"
# Variante B: lead_file_base64 + lead_filename
base64 -w0 leads.csv
```

`column_mapping` ist Pflicht und hier 1:1 (CSV-Header = Zielfeld):

```json
{"first_name":"first_name","last_name":"last_name","full_name":"full_name",
 "job_title":"job_title","company":"company","company_website":"company_website",
 "linkedin_url":"linkedin_url","location":"location"}
```

Kein `"email"`-Eintrag im Mapping – die Spalte existiert nicht.

Fehlerbilder:

| Symptom | Ursache / Behebung |
|---|---|
| Preview zeigt weniger Zeilen als die CSV | Zeilenumbrüche/Quoting kaputt → CSV erneut durchs Skript schicken |
| Spalte wird nicht gemappt | Header weicht ab → Skript erzwingt das Schema, CSV neu erzeugen |
| Organisation nicht gefunden | Name ungenau → `organization_list` mit kürzerem `search`; **nie neu anlegen** |
| Mehrere Organisationen passen | Beim User rückfragen, welche gemeint ist |
| Kein Agent vorhanden | Ohne `agent_name` importieren und im Report vermerken |
| Import bleibt „running" | `lead_import_status` erneut abfragen, bevor der Report geschrieben wird |

Der Import ist **nicht ohne Weiteres rückgängig** zu machen: lieber ein Preview zu viel als ein Fehlimport in die Organisation des falschen Kunden.

## Skript

```bash
python3 ${CLAUDE_SKILL_DIR}/scripts/build_leadlist_csv.py [--mode people|company] EINGABE... [-o AUSGABE]
```

- Eingabe: CSV oder JSON (Liste von Objekten, oder Objekt mit `results`/`data`/`rows`/`contacts`/`companies`/`entities`).
- Mehrere Eingaben werden gemerged; die **erste Datei gewinnt** bei Dubletten, fehlende Felder werden aus der Dublette nachgezogen.
- Erkennt gängige Clay-/Apollo-Feldnamen (`fullName`, `companyName`, `domain`, `person_linkedin_url`, `headline`, `city`, …).
- Verwirft Zeilen ohne Person bzw. ohne Firma+Domain; wirft jede E-Mail-Spalte weg.
- Statistik geht auf stderr, CSV auf stdout – `-o` schreibt direkt in eine Datei.

## Verwandte Skills

| Skill | Wofür |
|---|---|
| `bedarfsliste` | Bedarfsqualifizierte Firmenliste (Name+Domain) + Claygent-Prompt + Jobtitel – **idealer Input für Schritt 3** |
| `firmen-deepresearch` | Firmen rein per Websuche, wenn Apollo/Clay ausdrücklich nicht genutzt werden soll |
| `market-intel-report` | Kunden-/Marktkontext und ICP für Schritt 1 |
| `icp-definer`, `persona-definer` | ICP und Buying Center schärfen |
| `prospect-list` | Allgemeine Prospect-Liste **ohne** amplifa-Import |
