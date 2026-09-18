---
name: clay-lead-list
description: Baut über Clay die passende Lead-Liste für einen amplifa-Kunden (Firmenliste ODER Personenliste) und lädt sie eigenständig in die richtige Organisation auf der amplifa-Plattform hoch. IMMER nutzen, wenn der User sinngemäß sagt "such mir eine Liste für den Kunden X", "bau mir eine Lead-Liste über Clay", "Firmenliste/Personenliste für Kunde Y", "zieh die Kontakte für Kunde Z und lad sie hoch" oder "finde mehr" zu einer laufenden Liste. Liefert IMMER eine CSV im exakten amplifa-Importschema (identisch zum lead_import_template, aber OHNE email-Spalte) plus den bestätigten Import in die richtige Kunden-Organisation.
argument-hint: [kunde + listentyp (firmen|personen) + anzahl + zielmarkt/ICP]
---

# Clay Lead-List-Builder → amplifa-Import

Eine Pipeline vom Kundenauftrag bis zur importierten Liste: **Clay findet die Leads → Skript erzwingt das Importschema → amplifa bekommt sie in der richtigen Organisation.**

Zwei Listentypen, ein Schema:
- **Personenliste** (Default): konkrete Ansprechpartner mit Titel und Firma – das, was eine Sequenz direkt anschreiben kann.
- **Firmenliste**: nur Unternehmen + Domain, Personenspalten leer. Für Account-first-Kampagnen oder wenn die Kontakte später in amplifa/Clay nachgezogen werden.

## Schritt 0 – Auftrag fixieren (kurz, nicht ausfragen)

Nötig sind nur vier Dinge. Was im Prompt steht, wird nicht nachgefragt:

| Punkt | Wenn nicht genannt |
|---|---|
| **Kunde / Organisation** | Über `organization_list` auflösen (Schritt 5). Nur bei Mehrdeutigkeit fragen. |
| **Listentyp** | Personen als Default – außer der User sagt „Firmenliste"/„Unternehmensliste". |
| **Anzahl** | 200 Kontakte bzw. 300 Firmen als Startbatch, dann nachladen. |
| **ICP / Zielmarkt** | Aus dem Kundenprodukt herleiten (Schritt 1) – nicht raten, sondern recherchieren. |

## Schritt 1 – Kundenkontext & ICP (IMMER zuerst)

Nie blind suchen. Bevor Clay angefasst wird:

1. **Kunde verstehen:** Website des Kunden + Web-Recherche. Was verkauft er, welches Problem löst er, an wen.
2. **Vorhandenes Material nutzen, statt es neu zu erfinden:** existiert schon eine Bedarfsliste (`bedarfsliste`), ein Market-Intel-Report (`market-intel-report`) oder ein Onboarding zu dem Kunden in amplifa (`onb_get`, `onb_get_website_analysis`) → das ist der ICP, nicht die eigene Vermutung.
3. **ICP schriftlich fixieren** und dem User in 5 Zeilen zeigen, *bevor* Credits fließen: Branchen/Sub-Sektoren · Größenband · Region/Land · Bedarfssignale · harte Ausschlüsse.
4. **Bei Personenlisten zusätzlich das Buying Center:** Tier-1-Titel (Entscheider/Budget) und Tier-2-Titel (Nutzer/operativ), deutsch **und** englisch – Clay matcht über Titel-Strings.

Kurze Bestätigung des Users abwarten, wenn der ICP nennenswert interpretiert wurde. Steht der ICP klar im Prompt: direkt weiter.

## Schritt 2 – Clay aufrufen

**Route A (Default): Clay-Connector.** Ist bereits authentifiziert, liefert strukturierte Daten und kostet keine Login-Akrobatik. Läuft im selben Clay-Workspace wie die UI – vorher mit `get-current-workspace` bestätigen, in welchen Workspace gearbeitet wird.

**Route B: Clay im Browser.** Über Playwright/Chromium (vorinstalliert), wenn Route A nicht reicht – etwa für eine bestehende Clay-Tabelle, einen fertigen Table-Export oder ein Workspace-Enrichment, das nur in der UI existiert. Mechanik und Grenzen: `reference.md` → „Clay im Browser". Kein Login-Zustand vorhanden → das **sagen und auf Route A wechseln**, niemals nach Zugangsdaten fragen oder sie hart eintragen.

Regel: Route A versuchen, Route B nur mit Grund. Welcher Weg genommen wurde, gehört in den Abschlussreport.

## Schritt 3 – Liste in Clay bauen

**Firmenliste:** Firmen nach ICP-Filtern ziehen (Branche × Größenband × Region als mehrere Teilsuchen, nicht eine Mega-Query). Jeden Batch sofort wegschreiben.

**Personenliste:** erst die Zielfirmen (wie oben oder aus einer vorhandenen `liste.csv`), dann pro Firma über die Tier-1/Tier-2-Titel die Kontakte. Pro Firma das **Buying Center, nicht das Org-Chart** – 2–5 Kontakte sind das sinnvolle Band.

**Enrichments nur, wenn der User sie ausdrücklich will – sie kosten Credits.** Insbesondere:

> **Niemals E-Mails in Clay anreichern.** Die E-Mail-Spalte ist bewusst nicht Teil des Importschemas – **amplifa findet die Adressen selbst**. Eine Clay-E-Mail-Anreicherung verbrennt hier nur Credits.

Die eigentliche Bedarfsprüfung pro Firma gehört als Claygent-/Sculptor-Prompt nach Clay, nicht in Claudes Tokens (Vorlage: `bedarfsliste/clay_sculptor_prompt.md`).

## Schritt 4 – CSV ins Importschema zwingen (nie von Hand)

Rohdaten aus Clay (JSON oder CSV) immer durch das Skript schicken – es normalisiert, dedupliziert und erzwingt das Schema:

```bash
python3 ${CLAUDE_SKILL_DIR}/scripts/build_leadlist_csv.py --mode people  clay_batch1.json -o leads.csv
python3 ${CLAUDE_SKILL_DIR}/scripts/build_leadlist_csv.py --mode company firmen.json     -o leads.csv
```

Ausgabeschema – **exakt die Spalten des `lead_import_template`, nur ohne `email`**:

```
first_name,last_name,full_name,job_title,company,company_website,linkedin_url,location
```

- **Reihenfolge und Schreibweise sind fix.** Keine Zusatzspalten, keine Umbenennung, keine `email`-Spalte – auch dann nicht, wenn Clay eine mitliefert (das Skript wirft sie raus).
- **Firmenliste:** identische Kopfzeile, Personenspalten leer. Das Schema bleibt dasselbe, damit der amplifa-Import unverändert greift.
- Das Skript normalisiert Domains (`https://www.acme.de/x` → `acme.de`) und LinkedIn-URLs, baut `full_name` aus Vor-/Nachname (und umgekehrt) und dedupliziert über LinkedIn-URL bzw. Domain.
- Es meldet auf stderr, wie viele Zeilen sauber, doppelt oder unvollständig waren – **diese Zahlen in den Report übernehmen**.

## Schritt 5 – Import in die richtige amplifa-Organisation

Der empfindliche Teil: Leads landen in einer echten Kunden-Organisation. Reihenfolge strikt einhalten.

1. **Organisation auflösen:** `organization_list` mit dem Kundennamen als `search`.
   - **Genau ein eindeutiger Treffer → eigenständig weiterarbeiten.**
   - Mehrere Treffer oder kein Treffer → **fragen, nicht raten.** Niemals eine Organisation anlegen, nur weil der Name nicht gefunden wurde.
2. **Agent wählen:** `agent_list` für die Organisation. Genau ein aktiver/passender Agent → nehmen. Mehrere → den vom User genannten, sonst kurz fragen. Keiner → ohne Agent importieren und das im Report vermerken.
3. **Trockenlauf:** `lead_import_preview` mit der CSV und dem expliziten `column_mapping` (siehe unten). Prüfen: erkannte Zeilenzahl, Mapping aller acht Spalten, gemeldete Fehler. **Nur bei sauberem Preview weiter.**
4. **Import:** `agent_import_leads` mit derselben CSV, demselben `column_mapping`, `organization_name` und `agent_name`.
5. **Verifizieren:** `lead_import_status` mit der zurückgegebenen `lead_import_id`, bis der Import durch ist. Importierte Anzahl, Fehler und Übersprungene festhalten.

Das `column_mapping` ist 1:1 – die CSV-Header heißen schon wie die Zielfelder:

```json
{"first_name":"first_name","last_name":"last_name","full_name":"full_name",
 "job_title":"job_title","company":"company","company_website":"company_website",
 "linkedin_url":"linkedin_url","location":"location"}
```

Details zum Upload (Data-URI/Base64) und zu Fehlerbildern: `reference.md` → „amplifa-Import".

## Schritt 6 – Report

Zum Abschluss immer, kurz:

- Kunde/Organisation + Agent, in die importiert wurde
- Listentyp, Anzahl sauberer Zeilen, Dubletten/Verworfene (Zahlen aus Schritt 4)
- `lead_import_id` + Endstatus aus `lead_import_status`
- ICP-Kurzfassung und welche Clay-Route (A oder B) genutzt wurde
- Pfad zur CSV – **immer mitliefern, auch wenn der Import geklappt hat**

## „Finde mehr"

`leads.csv` ist der Master. Neuen Batch ziehen (bereits gefundene Firmen/Kontakte in Clay ausschließen) und beides gemeinsam durchs Skript schicken – die Reihenfolge bestimmt, welcher Datensatz gewinnt:

```bash
python3 ${CLAUDE_SKILL_DIR}/scripts/build_leadlist_csv.py --mode people leads.csv batch2.json -o leads.csv
```

Dann **nur den neuen Teil** importieren, nicht die komplette Masterliste erneut – sonst entstehen Dubletten in amplifa.

## Eiserne Regeln

- **Keine `email`-Spalte.** Nie in der CSV, nie im Mapping, nie in Clay angereichert – amplifa macht das.
- **Spaltenschema exakt wie oben.** Abweichung = kaputter Import.
- **Nie erfundene Personen, Firmen, Domains oder LinkedIn-URLs.** Unklar → Zeile raus. Das Skript verwirft unvollständige Zeilen automatisch; diese Verwerfung nicht durch Auffüllen umgehen.
- **Zielzahl nicht mit Schrott auffüllen.** Sind nur 340 passende Firmen im Markt, wird das gemeldet – nicht auf 1000 aufgefüllt.
- **Immer erst `lead_import_preview`, dann `agent_import_leads`.** Kein Import ohne sauberen Trockenlauf.
- **Organisation nie raten.** Eindeutig → eigenständig importieren. Mehrdeutig → fragen. Nie neu anlegen.
- **Enrichments kosten Credits** – nur auf ausdrücklichen Wunsch, E-Mails grundsätzlich nie.
- **CSV immer durch das Skript**, nie von Hand zusammenbauen.
