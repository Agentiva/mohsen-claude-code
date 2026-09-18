# Referenz – Clay Lead-List-Builder

Nachschlagewerk zu SKILL.md. Alle Zahlen stammen aus einem echten Durchlauf
(VertiGIS ConnectMaster, DACH, 25 Firmen, 1.625 Rohpersonen) – nicht geschätzt.

## Spaltenschema (verbindlich)

`lead_import_template.csv` **und** die Ausgabe dieses Skills:

```
email,first_name,last_name,full_name,job_title,company,company_website,linkedin_url,location
```

| Spalte | Inhalt | Firmenliste |
|---|---|---|
| `email` | **immer leer** – amplifa findet die Adresse selbst | leer |
| `first_name` / `last_name` | Vor-/Nachname | leer |
| `full_name` | „Vorname Nachname" | leer |
| `job_title` | Jobtitel im Original (nicht eindeutschen) | leer |
| `company` | Firmenname wie geführt (Rechtsform behalten) | **gefüllt** |
| `company_website` | nackte Domain, ohne Schema/`www.`/Pfad | **gefüllt** |
| `linkedin_url` | `https://linkedin.com/in/...` bzw. `/company/...` | optional |
| `location` | Stadt bzw. „Stadt, Land" | optional |

**Warum die leere email-Spalte:** `agent_import_leads` verlangt zwingend ein
gemapptes `email`-Feld und bricht sonst ab:

```
column_mapping must map a CSV column to email
```

`lead_import_preview` akzeptiert dieselbe Datei **ohne** email und meldet nur
`unmapped_fields: ["email"]`. Der Preview validiert also das Mapping, **nicht die
Importfähigkeit**. Eine E-Mail-Anreicherung in Clay/Apollo bleibt trotzdem falsch:
sie kostet Credits für Daten, die amplifa selbst beschafft.

## Gemessene Werkzeuglage

| Werkzeug | Filter | Volumen | Daten | Kosten |
|---|---|---|---|---|
| Clay `find-and-enrich-contacts-at-company` | ✅ Titel | 0–20/Firma | vollständig **inkl. Stadt** | 1 Call/Firma |
| Clay `run_subroutine_direct` „Find People at Company" | ❌ ignoriert | hart 10/Firma | vollständig, Land statt Stadt | 1 Call/≤1000 Firmen |
| Apollo `apollo_mixed_people_api_search` | ✅ stark | 100/Seite | **Nachname maskiert**, keine LinkedIn/Domain | – |
| Apollo `apollo_mixed_companies_search` | ✅ | 100/Seite | Name + `primary_domain` | **1 Credit/Request** |

Präzision im Test: gefilterte Route **~75 %**, Batch-Route **3 %**.
Der Batch lieferte aus 182 Firmen 1.625 Rohpersonen und daraus nur 48 ICP-Treffer.

### Fallstricke, die keinen Fehler werfen

- **Batch-Filter werden verschluckt.** `run_subroutine_direct` mit
  `Job Title Keywords`, `Seniority`, `Limit` gibt exakt dieselben 10 Personen
  zurück wie ohne. Die Inputs erscheinen brav im Echo der Antwort – wirkungslos.
- **`locations` in `contactFilters` halbiert bis drittelt die Ausbeute.**
  Dieselbe Firma: ohne Ortsfilter 20 Treffer, mit Ortsfilter 3. Land per
  `--countries` im Skript nachfiltern.
- **`isComplete: false`.** `get-task-context` antwortet auch, während Clay noch
  rechnet. Im Test waren beim ersten Abruf 66 von 90 Firmen leer. Das Skript
  warnt; erneut abrufen.
- **Domain-Mismatch = 0 Treffer.** `gasag.de` → Clay führt „GASAG Gruppe" unter
  `gasag-gruppe.de`. Die kanonische Domain steht in der Antwort unter
  `companies.<key>.domain`.
- **Falsche Firma hinter der Domain.** `mvv.de` löst auf „MVV Enamic GmbH"
  (131 MA) statt MVV Energie auf. `employee_count` in der Antwort gegenprüfen.

## Onboarding als ICP-Quelle

| Ziel | Tool |
|---|---|
| Onboardings finden | `onb_list(company="<Kunde>")` |
| ICPs, Personas, Produktgruppen, Value Props | `onb_get_website_analysis` |
| Blacklist, Senders, Meetings, Dokumente | `onb_get` – **sprengt den Kontext** |

`onb_get` liefert ~140k Zeichen und wird deshalb automatisch auf Platte
geschrieben. Nie in den Kontext lesen, sondern parsen:

```python
raw = open(pfad, encoding="utf-8").read()
j = raw.find('"entries"', raw.find('"blacklist"'))
k = raw.find('[', j); depth = 0
for n, ch in enumerate(raw[k:], k):
    depth += (ch == '[') - (ch == ']')
    if depth == 0:
        end = n + 1
        break
entries = json.loads(raw[k:end])
namen = sorted({e["company_name"].strip() for e in entries if e.get("company_name")})
```

Abgleich gegen Firmennamen **umlaut- und rechtsform-tolerant** (NFKD-Normalisierung,
`ae/oe/ue/ss`, alles Nicht-Alphanumerische raus, Teilstring-Match in beide
Richtungen). Sonst rutschen „Stadtwerke Karlsruhe GmbH" und „Stadtwerke Karlsruhe"
aneinander vorbei. Im Test entfernte das 13 von 203 Firmen aus dem Pool.

## Titel- und Negativlisten

Titelliste = eine Zeile pro Begriff, `#` für Kommentare. Quelle:
`selected_personas[].example_titles` aus dem Onboarding, plus die operativen
Rollen darunter. Deutsch **und** Englisch, denn Clay matcht Titel-Strings.

**Negativliste ist Pflicht, sobald „Asset Management" im ICP steht** – der Begriff
fängt sonst Finanz-, IT- und Immobilienrollen mit. Im Test bewährt:

```
Portfolio Management / Portfoliomanagement / IT - Finance / Finanzspezialist
Trading / Immobilien / Estate Management
Working Student / Werkstudent / Trainee / Praktikant
Personalleiter / Human Resources / Recruiting
Dozent / Professor
Einkäufer / Einkauf / Buyer / Beschaffung
Assistent / Assistant / Vorstandsassistent
```

**Kurze Begriffe brauchen Wortgrenzen.** `cto` steckt in „Dire*cto*r",
`gis` in „Lo*gis*tik". `clay_task_to_rows.py` baut daraus
`\b<wort>[\s\-/]*<wort>\b` – Filter nie ad hoc mit `in` nachbauen.

Rollen, die beim ersten Lauf **zu Unrecht** rausflogen und in die Titelliste
gehören, wenn das Produkt Netzinventar/-dokumentation ist: `Network Engineer`,
`Network Design`, `Netzdesign`, `NOC`, `SOC`, `Netzentwicklung`, `Systemführung`,
`Betriebsführer`, `Schalttechniker`, `Rollout`, `Trasse`, `Fiber`.

## Ausbeute pro Firmentyp (gemessen)

| Typ | Treffer/Firma | Konsequenz |
|---|---|---|
| Telco-/Glasfaser-Carrier (FTTH, Wholesale) | **15–20** | zuerst abgrasen |
| Große Versorger / Netzgesellschaften | 5–12 | solide Basis |
| Konzern-Holdings mit Auslandstöchtern | 4–8 | `--countries` zwingend |
| Firmen < ~200 Mitarbeitende | 0–2 | überspringen |

Planungsformel: **~8 Leads je Firma, 1 Clay-Call je Firma.** 500 Leads ≈ 60 Firmen.

## Clay – Route B (im Browser)

Nur wenn Route A nicht reicht: bestehende Clay-Tabelle, UI-only-Enrichment,
Table-Export. Chromium ist vorinstalliert, `PLAYWRIGHT_BROWSERS_PATH=/opt/pw-browsers`,
`PLAYWRIGHT_SKIP_BROWSER_DOWNLOAD=1`. **Kein `playwright install`.** Anderer
Playwright-Pin → `executablePath: '/opt/pw-browsers/chromium'`.

Browser mit persistentem User-Data-Dir starten, `https://app.clay.com` öffnen,
Login prüfen. Nicht eingeloggt → **abbrechen und auf Route A wechseln**; niemals
nach Passwort/2FA fragen, keine Zugangsdaten in Code oder Dateien.

## amplifa-Import

Reihenfolge: `organization_list` → `agent_list` → `lead_import_preview` (Probe)
→ `agent_import_leads` → `lead_import_status` (bis fertig).

```bash
base64 -w0 leads.csv          # -> lead_file_base64 (+ lead_filename)
# oder als Data-URI:
printf 'data:text/csv;name=leads.csv;base64,%s' "$(base64 -w0 leads.csv)"
```

**In Blöcke von ~100 Zeilen teilen.** Die Base64-Payload muss in den Tool-Call
geschrieben werden; kürzere Strings senken das Übertragungsrisiko und jeder Block
ist einzeln über seine `lead_import_id` verifizierbar.

| Symptom | Ursache / Behebung |
|---|---|
| `column_mapping must map a CSV column to email` | email-Spalte fehlt → CSV neu bauen, Werte leer lassen |
| Preview ok, Import scheitert | Preview prüft die email-Pflicht nicht – siehe oben |
| `status: pending`, `total_rows: 0`, `started_at: null` | Job ist nur eingereiht. **Kein Ergebnis** – weiter pollen |
| Organisation nicht gefunden | `organization_list` mit kürzerem `search`; **nie neu anlegen** |
| Mehrere Agents | Zielmarkt entscheidet Suche und Sprache → beim User rückfragen |
| Agent hat bereits `total_leads_count > 0` | Dublettengefahr – im Report vermerken |

Der Import ist **nicht ohne Weiteres rückgängig** zu machen: lieber ein Preview zu
viel als ein Fehlimport in die Organisation des falschen Kunden.

## Skripte

```bash
build_leadlist_csv.py [--mode people|company] EINGABE... [-o AUSGABE]
clay_task_to_rows.py  EINGABE... --titles titles.txt [--exclude exclude.txt]
                      [--countries "Germany,Austria,Switzerland"] [--jsonl] [--stats-only] [-o hits.json]
```

- `build_leadlist_csv.py` – Eingabe CSV oder JSON; mehrere Dateien werden gemerged
  (erste gewinnt, fehlende Felder werden nachgezogen); erkennt gängige Clay-/Apollo-
  Feldnamen; erzwingt Kopfzeile und email-Spalte; Statistik auf stderr.
- `clay_task_to_rows.py` – liest `get-task-context`-Dateien (beide Clay-Formen) oder
  mit `--jsonl` selbst geschriebene Zeilen-JSON; filtert wortgrenzen-sicher;
  warnt bei `isComplete: false`.

## Verwandte Skills

| Skill | Wofür |
|---|---|
| `bedarfsliste` | Bedarfsqualifizierte Firmenliste (Name+Domain) – **fertiger Input für Schritt 3** |
| `firmen-deepresearch` | Firmen per Websuche, wenn Apollo/Clay ausdrücklich nicht genutzt werden soll |
| `market-intel-report` | Kunden-/Marktkontext, wenn kein Onboarding existiert |
| `icp-definer`, `persona-definer` | ICP und Buying Center schärfen |
| `prospect-list` | Allgemeine Prospect-Liste **ohne** amplifa-Import |
