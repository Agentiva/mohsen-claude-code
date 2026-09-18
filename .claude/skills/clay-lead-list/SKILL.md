---
name: clay-lead-list
description: Baut über Clay die passende Lead-Liste für einen amplifa-Kunden (Firmenliste ODER Personenliste) und lädt sie eigenständig in die richtige Organisation auf der amplifa-Plattform hoch. IMMER nutzen, wenn der User sinngemäß sagt "such mir eine Liste für den Kunden X", "bau mir eine Lead-Liste über Clay", "Firmenliste/Personenliste für Kunde Y", "zieh die Kontakte für Kunde Z und lad sie hoch" oder "finde mehr" zu einer laufenden Liste. Liefert IMMER eine CSV im exakten amplifa-Importschema (identisch zum lead_import_template, email-Spalte leer) plus den verifizierten Import in die richtige Kunden-Organisation.
argument-hint: [kunde + listentyp (firmen|personen) + anzahl + zielmarkt/ICP]
---

# Clay Lead-List-Builder → amplifa-Import

Pipeline vom Kundenauftrag bis zur importierten Liste: **Clay findet die Leads → Skript erzwingt das Importschema → amplifa bekommt sie in der richtigen Organisation.**

Alle Zahlen und Regeln unten sind an einem echten Durchlauf (VertiGIS ConnectMaster, DACH) gemessen, nicht geschätzt. Die teuren Irrwege stehen in `reference.md` → „Gemessene Werkzeuglage".

## Die fünf Fallen, die den Lauf kosten

Diese zuerst lesen. Jede einzelne hat im Test Zeit oder Qualität gekostet:

1. **Die `email`-Spalte ist Pflicht — auch wenn sie leer bleibt.** `agent_import_leads` bricht ab mit `column_mapping must map a CSV column to email`. **`lead_import_preview` winkt dieselbe Datei ohne email durch** — der Preview ist also *kein* verlässlicher Wächter für den Import.
2. **Titelfilter am Clay-Batch werden stillschweigend ignoriert.** `run_subroutine_direct` nimmt `Job Title Keywords`/`Seniority` entgegen und liefert exakt dieselben 10 Zufallspersonen. Kein Fehler, kein Hinweis.
3. **Ein `locations`-Filter in der gefilterten Clay-Suche zerstört die Ausbeute** — im Test 20 → 3 Treffer bei derselben Firma. Land immer *lokal* nachfiltern, nie in der Query.
4. **Apollo-Personensuche liefert keine importfähigen Zeilen.** Nachnamen sind maskiert (`Eg***i`), LinkedIn und Domain fehlen. Nur für Firmen-Discovery nutzen.
5. **Kurze Titel-Keywords als Substring sind Gift.** `cto` matcht in „Dire**cto**r", `gis` in „Lo**gis**tik". Das Skript matcht auf Wortgrenzen — Filter nie von Hand nachbauen.

## Schritt 0 – Auftrag fixieren (kurz, nicht ausfragen)

| Punkt | Wenn nicht genannt |
|---|---|
| **Kunde / Organisation** | Über `organization_list` auflösen. Nur bei Mehrdeutigkeit fragen. |
| **Ziel-Agent** | `agent_list` prüfen. **Mehrere Agents mit verschiedenen Märkten → fragen**, das entscheidet Zielland und Sprache der ganzen Suche. |
| **Listentyp** | Personen als Default – außer der User sagt „Firmenliste"/„Unternehmensliste". |
| **Anzahl** | 200 Kontakte bzw. 300 Firmen als Startbatch, dann nachladen. |
| **ICP / Zielmarkt** | Aus dem Onboarding holen (Schritt 1) – nicht raten. |

## Schritt 1 – Kundenkontext & ICP (IMMER zuerst)

Das Onboarding ist die Goldgrube: es enthält **vom Kunden bestätigte** ICPs, Personas und die Blacklist. Nie den ICP selbst erfinden, solange das da ist.

1. `onb_list(company="<Kunde>")` – findet die Onboardings. Mehrere → das mit `status: submitted` und dem konkreteren `company_website` (oft die Produktseite, z. B. `/connectmaster/`) ist das relevante.
2. **`onb_get_website_analysis` nutzen, NICHT `onb_get`.** `onb_get` sprengt mit ~140k Zeichen das Kontextlimit; die Analyse liefert kompakt `selected_icps`, `selected_personas`, `selected_product_groups` und `value_propositions`.
3. **Blacklist holen.** Sie steckt nur in `onb_get`. Dessen Ergebnis wird bei Überlänge automatisch auf Platte geschrieben – die Datei mit einem Skript nach `"blacklist"` → `entries` parsen, statt sie in den Kontext zu laden. Rezept: `reference.md` → „Blacklist".
4. **ICP in 5 Zeilen festhalten** und zeigen, *bevor* Credits fließen: Branchen · Größenband · Region · Bedarfssignale · harte Ausschlüsse.
5. **Bei Personenlisten die Titelliste bauen** – aus `selected_personas.example_titles`, deutsch **und** englisch. Diese Liste ist eine Datei (eine Zeile pro Begriff), Eingabe für das Filterskript.

Steht der ICP klar im Prompt: direkt weiter. Wurde er nennenswert interpretiert: kurz bestätigen lassen.

## Schritt 2 – Clay aufrufen

**Route A (Default): Clay-Connector.** Authentifiziert, strukturierte Daten. Mit `get-current-workspace` bestätigen, in welchem Workspace gearbeitet wird, und das in den Report schreiben.

**Route B: Clay im Browser** (Playwright/Chromium, vorinstalliert) nur, wenn Route A die Aufgabe nicht abdeckt – bestehende Clay-Tabelle, UI-only-Enrichment, Table-Export. Kein Login-Zustand → **sagen und auf Route A wechseln**, nie nach Zugangsdaten fragen. Mechanik: `reference.md`.

## Schritt 3 – Liste bauen: die richtige Route wählen

Gemessen an 25 Firmen und 1.625 Rohpersonen:

| Route | Titelfilter | Ausbeute | Präzision | Calls |
|---|---|---|---|---|
| `find-and-enrich-contacts-at-company` | ✅ echt | 0–20/Firma | **~75 %** | 1 **pro Firma** |
| `run_subroutine_direct` „Find People at Company" | ❌ ignoriert | hart 10/Firma | **3 %** | 1 für bis zu 1000 Firmen |

**Die gefilterte Route ist der Arbeitspferd-Weg.** Der Batch lohnt nur als billiger Breitensweep über viele Firmen, wenn Vollständigkeit wichtiger ist als Präzision.

**Firmen-Discovery** (Domains beschaffen): `apollo_mixed_companies_search` mit NAICS + `organization_locations` + `organization_num_employees_ranges`, `per_page: 100`. **1 Credit pro Request** – dem User vorher sagen. Liefert `primary_domain` (Bucket `organizations`) bzw. `domain` (Bucket `accounts`). Alternativ die fertige CSV aus dem `bedarfsliste`-Skill.

**Kontakte je Firma** – so und nicht anders aufrufen:

```
find-and-enrich-contacts-at-company(
  companyIdentifier = "<domain>",
  contactFilters = { job_title_keywords: [ ...12–14 ICP-Begriffe... ] }   // KEIN locations!
)
```

Welche Firmen sich lohnen (im Test gemessen):

- **Telco- und Glasfaser-Carrier: 15–20 Treffer/Firma** – mit Abstand die beste Ader für Netz-/Inventory-Produkte.
- **Große Versorger/Netzgesellschaften: 5–12.**
- **Firmen unter ~200 Mitarbeitenden: 0–2** – überspringen, der Call lohnt nicht.
- **0 Treffer trotz großer Firma = Domain-Mismatch.** Clay führt die Firma unter einer anderen Domain (`gasag.de` → `gasag-gruppe.de`). Die Antwort nennt unter `companies.<key>.domain` die kanonische Domain – damit erneut suchen.

**Enrichments nur auf ausdrücklichen Wunsch – sie kosten Credits. E-Mails grundsätzlich nie** (amplifa findet sie selbst; die Spalte bleibt leer).

## Schritt 4 – Ergebnisse einsammeln, ohne den Kontext zu sprengen

**Der Batch-Weg ist transkriptionsfrei:** `get-task-context` liefert bei Überlänge automatisch eine Datei statt Kontext. Das ist erwünscht – die Datei direkt ans Skript geben:

```bash
python3 ${CLAUDE_SKILL_DIR}/scripts/clay_task_to_rows.py <task-context-datei>... \
    --titles titles.txt --exclude exclude.txt \
    --countries "Germany,Austria,Switzerland,Deutschland,Österreich,Schweiz" \
    -o hits.json
```

- **`isComplete: false` heißt: Clay war noch nicht fertig.** Im Test fehlten so 66 von 90 Firmen. Das Skript warnt; dann `get-task-context` erneut aufrufen, nicht weiterrechnen.
- `--exclude` ist Pflicht bei „Asset Management" im ICP – es fängt sonst Finanz-, IT-Portfolio-, Immobilien- und Einkaufsrollen mit. Vorlage: `reference.md`.
- `--countries` ersetzt den verbotenen `locations`-Query-Filter und wirft Treffer internationaler Konzerne aus Italien/Rumänien/UK raus.

**Der gefilterte Weg landet im Kontext** und muss von Hand in eine JSONL-Datei geschrieben werden (ein Objekt pro Zeile, Felder wie im Schema). Das ist der eigentliche Engpass des Verfahrens – **~8 Leads pro Firma, ~1 Call pro Firma**. Für 500 Leads sind das rund 60 Firmen. Realistisch planen und dem User die Rechnung nennen, statt still bei 150 aufzuhören.

## Schritt 5 – CSV ins Importschema zwingen (nie von Hand)

```bash
python3 ${CLAUDE_SKILL_DIR}/scripts/build_leadlist_csv.py --mode people  hits.json -o leads.csv
python3 ${CLAUDE_SKILL_DIR}/scripts/build_leadlist_csv.py --mode company firmen.json -o leads.csv
```

Ausgabeschema – **byte-identisch mit `lead_import_template`**:

```
email,first_name,last_name,full_name,job_title,company,company_website,linkedin_url,location
```

- **`email` ist als Spalte Pflicht, die Werte bleiben leer.** Ohne sie scheitert der Import (Falle 1). Das Skript legt die Spalte an und verwirft mitgelieferte E-Mail-Werte.
- **Firmenliste:** identische Kopfzeile, Personenspalten leer.
- Das Skript normalisiert Domains und LinkedIn-URLs, baut `full_name` in beide Richtungen, dedupliziert über LinkedIn-URL bzw. Domain und meldet die Zahlen auf stderr – **diese Zahlen in den Report übernehmen**.
- **Blacklist zuletzt noch einmal gegen die Firmennamen der Leads prüfen**, nicht nur gegen den Firmenpool: über den Batch-Weg rutschen sonst Bestandskunden rein.

## Schritt 6 – Import in die richtige amplifa-Organisation

1. **Organisation:** `organization_list(search="<Kunde>")`. Genau ein Treffer → eigenständig weiter. Mehrere oder keiner → **fragen, nie raten, nie neu anlegen.**
2. **Agent:** `agent_list`. Dabei `total_leads_count` ansehen – **hat der Agent schon Leads, ist Dublettengefahr real**; das in den Report schreiben.
3. **Preview:** `lead_import_preview` mit einer **3-Zeilen-Probe** der fertigen CSV. Prüft Mapping, Umlaute und Quoting billig. Achtung: er prüft **nicht** die email-Pflicht.
4. **Import:** `agent_import_leads`. Die CSV geht als Base64 in den Call – **in Blöcke von ~100 Zeilen teilen**. Kleinere Payloads senken das Übertragungsrisiko und jeder Block ist einzeln verifizierbar.
5. **Verifizieren:** `lead_import_status` mit der `lead_import_id` **bis `status` nicht mehr `pending`/`running` ist.** Erst dann `created_count`, `skipped_count`, `blacklisted_count` und `errors_detail` in den Report. Ein frisch angelegter Import steht auf `total_rows: 0` – das ist *kein* Ergebnis.

`column_mapping` ist 1:1, die CSV-Header heißen wie die Zielfelder:

```json
{"email":"email","first_name":"first_name","last_name":"last_name","full_name":"full_name",
 "job_title":"job_title","company":"company","company_website":"company_website",
 "linkedin_url":"linkedin_url","location":"location"}
```

## Schritt 7 – Report

- Organisation + Agent, in die importiert wurde (und wie viele Leads dort vorher lagen)
- Listentyp, saubere Zeilen, Dubletten/Verworfene, durch Blacklist entfernt
- `lead_import_id` + **Endstatus** aus `lead_import_status`
- ICP-Kurzfassung, genutzte Clay-Route, Clay-Workspace
- Pfad zur CSV – **immer mitliefern**
- **Wurde die Zielzahl nicht erreicht: die Zahl nennen und sagen, was fehlt** (z. B. „172 von 500; für den Rest ~40 weitere Firmen à 1 Clay-Call")

## „Finde mehr"

`leads.csv` ist der Master. Neuen Batch ziehen, beides gemeinsam durchs Skript – die erste Datei gewinnt bei Dubletten:

```bash
python3 ${CLAUDE_SKILL_DIR}/scripts/build_leadlist_csv.py --mode people leads.csv batch2.json -o leads.csv
```

Dann **nur den neuen Teil** importieren, nie die ganze Masterliste erneut.

## Eiserne Regeln

- **`email` als Spalte immer, Werte immer leer.** Nie in Clay/Apollo anreichern.
- **Spaltenschema exakt wie oben.** Abweichung = kaputter Import.
- **Nie erfundene Personen, Firmen, Domains oder LinkedIn-URLs.** Unklar → Zeile raus.
- **Zielzahl nicht mit Schrott auffüllen** – lieber weniger und ehrlich melden.
- **Kein Import ohne Preview und ohne abschließenden `lead_import_status`.**
- **Organisation nie raten, nie neu anlegen. Bei mehreren Agents fragen.**
- **CSV immer durch das Skript**, nie von Hand zusammenbauen.
