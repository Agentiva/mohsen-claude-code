---
name: kampagnen-monatsreport
description: >
  Berechnet die Meeting Requests des ABGELAUFENEN Monats je Kunde aus der
  amplifa-Plattform, schreibt sie wochenweise (Woche 1-4) plus Monatssumme in die
  Notion-Datenbank "Kampagne Überblick – Board" und hinterlegt pro Zeile einen
  Ampel-Report (🔴 ROT / 🟡 GELB / ⚪ WEIß / 🟢 GRÜN) auf Basis des Paket Modells.
  Läuft als Cloud-Routine 3 Tage vor Monatsende UNBEAUFSICHTIGT – stellt daher
  KEINE Rückfragen, trifft Best-Effort-Entscheidungen und protokolliert Unklarheiten
  am Ende. Manuell nutzbar mit "mach den Monatsreport für <Monat>".
---

# Kampagnen-Monatsreport (Routine)

Diese SKILL.md ist der vollständige Routine-Prompt. Sie ist so geschrieben, dass sie
ohne Vorwissen aus dem Chat läuft. Nichts löschen, nichts an Kunden senden – nur
Plattform lesen, rechnen, Notion schreiben, am Ende kurz berichten.

## 0. Termin-Guard (nur bei automatischem Lauf)

Die Routine feuert täglich am 25.–28. Prüfe zuerst:

```
zieltag = letzter_Tag_des_aktuellen_Monats − 3
```

Ist **heute ≠ zieltag**, brich sofort ab und melde nur „Kein Lauftag (heute TT.MM.,
Zieltag TT.MM.)". Keine weiteren Tool-Calls.

Beispiele: August (31 Tage) → 28.08. · September (30) → 27.09. · Februar (28) → 25.02.

Bei manuellem Aufruf entfällt der Guard.

## 1. Berichtsmonat bestimmen

Berichtsmonat = **der Monat davor**. Lauf Ende August → Berichtsmonat **Juli**.
Merke dir `JAHR`, `MONAT_NR`, `MONAT_DE` (Januar … Dezember) und `LETZTER_TAG`.

Achtung Altlast: Die Spalte für Februar heißt in der DB **„Februaur"** (Tippfehler,
nicht korrigieren – sonst brechen bestehende Views).

## 2. Wochenraster

Fix, unabhängig vom Wochentag:

| Bucket | Tage |
|---|---|
| Woche 1 | 01. – 07. |
| Woche 2 | 08. – 14. |
| Woche 3 | 15. – 21. |
| Woche 4 | 22. – LETZTER_TAG |

Monatswert = Woche 1 + Woche 2 + Woche 3 + Woche 4.

## 3. Meeting Requests aus der Plattform holen

Entspricht dem Admin-Filter
`app.amplifa.ai/admin/replies?status=open&reply_type=meeting_request`.

1. `mcp__Amplifa__conversation_list_by_status` mit `status="meeting_request"`,
   `per_page=100`, Seite 1 → `pagination.total_pages` lesen.
2. Alle Seiten durchlaufen, bis das Datumsfenster des Berichtsmonats sicher
   überschritten ist. Die Liste ist **absteigend nach letzter Antwort** sortiert –
   du kannst aufhören, sobald eine Seite nur noch Daten **vor** dem 01. des
   Berichtsmonats enthält, musst aber die Seite davor vollständig haben.
3. Die Antworten sind groß und landen meist in einer Datei. Lies sie **nie** ganz
   in den Kontext – werte sie mit `jq`/`python3` aus.
4. **Nach Conversation-ID deduplizieren.** Pagination kann Einträge doppeln.

**Stichtag je Conversation:** `last_reply_at`, und nur falls `null`, ersatzweise
`created_at`. Nach `YYYY-MM` des Berichtsmonats filtern.

**Gruppierung:** nach `organization.organization_name` (die amplifa-Kundenorganisation),
**nicht** nach `lead.company` (das ist die angeschriebene Zielfirma).

**Lückenprüfung (Pflicht):** Sortiere die geladenen Datumswerte absteigend und prüfe,
dass zwischen der ältesten Seite oberhalb und der jüngsten Seite unterhalb des
Berichtsmonats kein Sprung klafft. Sonst fehlende Seite nachladen. Ein Zählfehler
hier fällt sofort im Board auf.

## 4. „Keine Antwort erhalten" ermitteln (für ⚪ WEIß)

⚪ WEIß bedeutet: von diesem Kunden kam im Berichtsmonat **überhaupt keine
E-Mail-Antwort** – nicht nur kein Meeting.

Dafür zusätzlich die anderen Antworttypen global sweepen, jeweils mit
`mcp__Amplifa__conversation_list_by_status`:
`interested`, `not_interested`, `wrong_person`.

Baue daraus je Organisation die Menge der Monate mit irgendeiner Antwort. Hat eine
Organisation im Berichtsmonat **null Antworten jeglicher Art** → ⚪ WEIß.
Hat sie Antworten, aber 0 Meeting Requests → normale Ampel nach Paket (also 🔴).

## 5. Notion-Board öffnen

Datenbank **„Kampagne Überblick – Board"**
Data Source: `collection://2a78174b-42df-81d2-80e3-000bc6b01cd6`

Alle Zeilen laden:
```sql
SELECT url, "Unternehmensname", "Paket Modell", "Report"
FROM "collection://2a78174b-42df-81d2-80e3-000bc6b01cd6"
```

**Monatsspalte anlegen, falls sie fehlt.** Vorhanden sind aktuell: Januar, Februaur,
März, Mai, Juni, Juli, Oktober, November, Dezember. Es fehlen April, August,
September. Wenn `MONAT_DE` fehlt:
```
mcp__Notion__notion-update-data-source
  data_source_id: collection://2a78174b-42df-81d2-80e3-000bc6b01cd6
  statements: ADD COLUMN "<MONAT_DE>" NUMBER
```
Vorher prüfen, ob eine Spalte mit Leerzeichen am Ende existiert (`"August "`) –
Notion erlaubt beides und Duplikate sind schwer zu bemerken.

## 6. Organisation ↔ Notion-Zeile zuordnen

Plattform-Name und Board-Titel weichen oft ab. Vorgehen je Organisation:

1. Exakter Treffer auf `Unternehmensname` (Groß-/Kleinschreibung ignorieren).
2. Sonst Normalisierung: Rechtsform (GmbH, AG, & Co. KG), Bindestriche,
   Leerzeichen und Umlaute (ae/oe/ue/ss) entfernen und erneut vergleichen.
3. Sonst über die **Sende-Domains** verifizieren: `mailbox.email` bzw.
   `from_address` der Conversations gegen `Domains Name` und `Website-URL` der
   Kandidatenzeile prüfen. Das ist der verlässlichste Anker.
4. Bei mehreren Kandidaten die Zeile mit echtem `ICP-Status` (Live, Optimieren,
   Emails Approven, Leads hinzufügen …) nehmen, **nicht** die leeren
   Formular-Duplikate mit „Neu - keine infos und Materiallien".

Verifizierte Sonderfälle (Stand 08/2026) – erst prüfen, ob sie noch gelten:

| Plattform-Organisation | Notion-Zeile |
|---|---|
| Voccom Audio | Passmedientechnik GmbH |
| Kömmerling | profine |
| epneo | ebm-papst neo GmbH & Co. KG |
| Graebert GmbH | Gräbert GmbH |
| Jaeger TTC | Gebrüder Jaeger GmbH |
| Intro (engesser.de) | Engesser (Intro BC) |
| emsbo solar GmbH | Embso SOlar |
| IQ Services | IQ-Service |
| Ledibelle | LediBelle / Appenzeller Naturkosmetik AG |
| Wilhelm König MTM | WILHELM KOENIG MTM GmbH |
| Remira Deutschland | REMIRA Austria GmbH |
| Amplifa | Amplifa MO New |
| LINDNER | Lindner Recyclingtech |
| Zeller+Gmelin | Zeller+Gmelin - MO |
| Optenda | OPTENDA GmbH |
| Magnetworld | Magnet WORLD |
| datango | Datango |
| ELO | Elo Digital |
| EQYO | EQYO (Saint-Gobain) |
| Schaltbau | Schaltbau GmbH |
| Firma Bock | Bock Handelsunternehmen |
| Norbert Kempf | Norbert Kempf CNC-Technik GmbH |
| Byload Logistics | Byload GmbH |
| GBN Systems | GBN Systems GmbH |
| Denodo | Denodo Technologies GmbH |
| SEGGER Microcontroller | Segger |
| Gradical GmbH | Gradical |
| Siemers Spezialisten | Siemers Spezialisten GmbH |
| Twist & Schirm Social Media | Twist und Schirm |
| Weimer Media | Weimer Media Group |
| Lookthrough | lookthrough |
| photovest | photovest GmbH |
| Ergopack | ErgoPack |
| ProContur | ProContur Individuelle Feinblech- und Kunststoffprodukte GmbH |

Organisationen **ohne** Board-Zeile: nicht raten, keine Zeile anlegen – am Ende
unter „Offene Punkte" melden.

## 7. Paket Modell auslesen

Aus der Spalte **„Paket Modell"** (Select):

| Wert | Stufe |
|---|---|
| 🔵 Klein Paket 3 Domains | Starter |
| 🟡 Mittlere Paket 6 Domains | Medium |
| 🟢 Großes Paket 9 Domains | Groß |
| ⚪ Kein Paket / leer | keine Bewertung → ⚪ WEIß |

Niemals aus „Domains Anzahl" oder „Domains Name" ableiten – die Felder sind
unzuverlässig gepflegt.

## 8. Ampel bestimmen

Meetings des Berichtsmonats gegen die Paketstufe:

| Stufe | 🔴 ROT | 🟡 GELB | 🟢 GRÜN |
|---|---|---|---|
| Starter | ≤ 0 | 1 – 3 | ≥ 4 |
| Medium | ≤ 5 | 6 – 10 | ≥ 11 |
| Groß | ≤ 15 | 16 – 22 | ≥ 23 |

**⚪ WEIß** überschreibt alles, wenn einer dieser Fälle zutrifft:
- im Berichtsmonat kam vom Kunden **keine einzige E-Mail-Antwort** (Schritt 4), oder
- **Paket Modell** ist „⚪ Kein Paket" oder leer, oder
- die Organisation existiert in der Plattform nicht.

Exakt diese Schreibweise verwenden: **🔴 ROT**, **🟡 GELB**, **⚪ WEIß**, **🟢 GRÜN**.

## 9. Notion schreiben

Pro zugeordneter Zeile ein `mcp__Notion__notion-update-page` mit
`command: "update_properties"`:

```json
{
  "Woche 1": <n>, "Woche 2": <n>, "Woche 3": <n>, "Woche 4": <n>,
  "<MONAT_DE>": <summe>,
  "Report": "<Reporttext>"
}
```

Regeln:
- **Immer 0 schreiben, nie leer lassen.** Eine leere Zelle liest sich als „nicht
  erfasst"; genau daran ist ein früherer Lauf aufgefallen.
- Nur Zeilen anfassen, denen eine Plattform-Organisation zugeordnet ist.
- Bestehende Werte anderer Monate nicht überschreiben.
- Zahlen als JSON-Number, nicht als String.

## 10. Reporttext

Deutsch, sachlich, ohne Floskeln. Aufbau:

```
<AMPEL> · <MONAT_DE> <JAHR> · <Paketstufe> (<n> Domains)

Meetings <MONAT_DE>: <summe> – Ziel <Zielwert der Stufe>
Wochen: W1 <a> · W2 <b> · W3 <c> · W4 <d>
Vormonat: <Wert> (<+/-x> ggü. Vormonat)

Analyse: <2–4 Sätze: Wo lag die Leistung, wie ist der Verlauf über die Wochen,
was fällt auf – Anlauf erst spät im Monat, Einbruch nach Woche 2, gleichmäßig
verteilt, alles aus einer Woche?>

Maßnahme: <1–3 konkrete, umsetzbare Schritte. Keine Allgemeinplätze.>
```

Der Zielwert je Stufe: Starter „ab 4", Medium „ab 11", Groß „ab 23".

Vormonatswert aus der entsprechenden Monatsspalte lesen, falls vorhanden; sonst die
Zeile weglassen statt „k. A." zu schreiben.

**Was in der Analyse stehen soll – je nach Lage:**
- 🟢 Was trägt, und ob der Vorsprung stabil ist oder auf einer starken Woche beruht.
- 🟡 Wie weit zum Ziel, und welcher Hebel am schnellsten greift (Volumen, Sequenz,
  Zielgruppe, Absenderzahl).
- 🔴 Ob es an Aussteuerung (pausierte Agenten, kein Versand) oder an Wirkung
  (Versand läuft, keine Termine) liegt. Wenn möglich mit
  `mcp__Amplifa__organization_agent_info_list` gegenprüfen: pausierte Agenten,
  Playbook-Status, `sent_emails_count` gegen `total_leads_count`.
- ⚪ Was genau fehlt, damit im nächsten Monat bewertet werden kann.

Für 🔴- und ⚪-Zeilen lohnt der zusätzliche `organization_agent_info_list`-Call.
Für 🟢 reicht die Meeting-Zahl – dort keine Zeit verbrennen.

## 11. Abschlussmeldung

Am Ende in den Chat (kein Notion, keine Mail):

1. Verteilung: 🟢 / 🟡 / ⚪ / 🔴 mit Anzahl und Meeting-Summe je Gruppe.
2. Top 3 und Flop 3 nach Meetings.
3. Veränderungen ggü. Vormonat, die auffallen (Absturz oder Sprung > 50 %).
4. **Offene Punkte:** Organisationen ohne Board-Zeile, Zeilen ohne Paket Modell,
   nicht zuordenbare Namen, fehlende Monatsspalten. Das ist der wichtigste Teil –
   hier steht, was ein Mensch nachpflegen muss.

## Grenzen

- Die Domains-Seite (`/admin/organizations/<id>/domains`) ist über den Amplifa-MCP
  **nicht** abrufbar; es gibt kein Domain- oder Mailbox-Tool. `sender_list` liefert
  die Sender-Personas, aber **keine** Mailbox-Anzahl. Die Paketgröße kommt deshalb
  ausschließlich aus „Paket Modell".
- `conversation_list_by_status` liefert nur Konversationen mit Status `open`. Das
  entspricht dem Admin-Filter und ist so gewollt.
- Läuft die Routine unbeaufsichtigt, niemals eine Rückfrage stellen – Annahme
  treffen, ausführen, unter „Offene Punkte" dokumentieren.
