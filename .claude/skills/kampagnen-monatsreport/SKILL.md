---
name: kampagnen-monatsreport
description: >
  Berechnet die Meeting Requests des ABGELAUFENEN Monats je Kunde aus der
  amplifa-Plattform und schreibt sie in die Notion-Datenbank "Kampagne Überblick":
  wochenweise (Woche 1-4), als Monatssumme ("<Monat>") und auf 10 gedeckelt
  ("<Monat> richtig"), plus Ampel-Report (🔴 ROT / 🟡 GELB / ⚪ WEIß / 🟢 GRÜN) auf
  Basis des Paket Modells. Was geschrieben wird, hängt vom Betreuer der Zeile ab
  ("Kampagne betreut von (1)": Mo, Anthony Filipiak oder leer). Läuft als
  Cloud-Routine am 07. jedes Monats UNBEAUFSICHTIGT – stellt daher KEINE
  Rückfragen, trifft Best-Effort-Entscheidungen und protokolliert Unklarheiten am
  Ende. Manuell nutzbar mit "mach den Monatsreport für <Monat>".
---

# Kampagnen-Monatsreport (Routine)

Diese SKILL.md ist der vollständige Routine-Prompt. Sie läuft ohne Vorwissen aus dem
Chat. Nichts löschen, nichts an Kunden senden – nur Plattform lesen, rechnen, Notion
schreiben, am Ende berichten.

## 0. Lauftermin

Die Routine läuft **am 07. jedes Monats**. Der Termin liegt bewusst eine Woche nach
Monatswechsel: spät klassifizierte Antworten aus den letzten Tagen des Berichtsmonats
sind dann erfasst.

Guard: Ist heute nicht der 07. und wurde kein Monat ausdrücklich genannt, sofort
abbrechen und nur „Kein Lauftag (heute TT.MM., Lauftag 07.)" melden. Bei einem
manuellen Aufruf mit genanntem Monat entfällt der Guard.

## 1. Berichtsmonat bestimmen

Berichtsmonat = **der Monat davor**. Lauf am 07.11. → Berichtsmonat **Oktober**.
Lauf am 07.01. → **Dezember des Vorjahres** (`JAHR` ist dann das Vorjahr).

Merke dir `JAHR`, `MONAT_NR`, `MONAT_DE` (Januar … Dezember) und `LETZTER_TAG`.

Daraus ergeben sich zwei Spaltennamen:

| Variable | Spalte | Beispiel |
|---|---|---|
| `SPALTE_MONAT` | `<MONAT_DE>` | „Oktober" |
| `SPALTE_RICHTIG` | `<MONAT_DE> richtig` | „Oktober richtig" |

Altlast: Die Februar-Spalte heißt in der DB **„Februaur"** (Tippfehler, nicht
korrigieren – sonst brechen bestehende Views). Für Februar gilt also
`SPALTE_MONAT = "Februaur"`, `SPALTE_RICHTIG = "Februar richtig"`.

## 2. Wochenraster

Fix, unabhängig vom Wochentag:

| Bucket | Tage |
|---|---|
| Woche 1 | 01. – 07. |
| Woche 2 | 08. – 14. |
| Woche 3 | 15. – 21. |
| Woche 4 | 22. – LETZTER_TAG |

`SUMME` = Woche 1 + Woche 2 + Woche 3 + Woche 4.
`RICHTIG` = `min(SUMME, 10)` – nur deckeln, **nicht** halbieren oder anders
umrechnen (die alten Spalten „Juli richtige Rechnung" / „August richtige Rechnung"
haben teils halbiert; das gilt nicht mehr).

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
Berichtsmonats kein Sprung klafft. Sonst fehlende Seite nachladen.

## 4. „Keine Antwort erhalten" ermitteln (für ⚪ WEIß)

⚪ WEIß bedeutet: von diesem Kunden kam im Berichtsmonat **überhaupt keine
E-Mail-Antwort** – nicht nur kein Meeting.

Dafür zusätzlich die anderen Antworttypen global sweepen, jeweils mit
`mcp__Amplifa__conversation_list_by_status`:
`interested`, `not_interested`, `wrong_person`.

Hat eine Organisation im Berichtsmonat **null Antworten jeglicher Art** → ⚪ WEIß.
Hat sie Antworten, aber 0 Meeting Requests → normale Ampel nach Paket (also 🔴).

## 5. Notion-Board öffnen

Datenbank **„Kampagne Überblick"**
Data Source: `collection://2a78174b-42df-81d2-80e3-000bc6b01cd6`

Zuerst das Schema holen (`mcp__Notion__notion-fetch` auf die Data Source) und nur
die Spaltenliste auswerten – die Antwort ist groß, nicht ganz in den Kontext lesen.

**Fehlende Spalten anlegen.** Wenn `SPALTE_MONAT` oder `SPALTE_RICHTIG` fehlt:
```
mcp__Notion__notion-update-data-source
  data_source_id: collection://2a78174b-42df-81d2-80e3-000bc6b01cd6
  statements: ADD COLUMN "<SPALTE_MONAT>" NUMBER; ADD COLUMN "<SPALTE_RICHTIG>" NUMBER
```
(nur die Spalte(n) anlegen, die wirklich fehlen). Vorher prüfen, ob es die Spalte
mit Leerzeichen am Ende schon gibt (`"August "`) – Notion erlaubt beides und
Duplikate sind schwer zu bemerken.

Nicht anfassen, nicht umbenennen, nicht löschen: „Oktober 1", „Juli richtige
Rechnung", „August richtige Rechnung".

Dann alle Zeilen laden (Vormonatsspalte nur mitnehmen, wenn sie existiert):
```sql
SELECT url, "Unternehmensname", "Kampagne betreut von (1)", "ICP-Status",
       "Paket Modell", "Domains Name", "Website-URL", "<VORMONAT_SPALTE>"
FROM "collection://2a78174b-42df-81d2-80e3-000bc6b01cd6"
```

## 6. Betreuer bestimmt, was geschrieben wird

Spalte **„Kampagne betreut von (1)"** (Personenfeld, Wert wie `["user://<id>"]`).
Nach der User-ID entscheiden, nicht nach dem Anzeigenamen:

| Betreuer | User-ID | Woche 1–4 | `SPALTE_MONAT` | `SPALTE_RICHTIG` | Ampel + Report |
|---|---|---|---|---|---|
| **Mo** | `27fd872b-594c-813a-ad8d-0002915432bb` | schreiben | `SUMME` | `min(SUMME, 10)` | ja |
| **Anthony Filipiak** | `128d872b-594c-8195-ac0d-00020b9004a5` | schreiben | **nicht schreiben** | **nicht schreiben** | ja |
| leer | – | nichts | nichts | nichts | nein → „Offene Punkte" |
| anderer User | – | nichts | nichts | nichts | nein → „Offene Punkte" |

- Bei Anthony-Zeilen die beiden Monatsspalten **gar nicht in den Update-Call
  aufnehmen** – vorhandene Werte bleiben stehen, es wird auch keine 0 geschrieben.
- **Gekündigte Zeilen** (ICP-Status enthält „Gekündigt") werden genauso behandelt wie
  alle anderen: zählen, Ampel, Report. Der Betreuer entscheidet, nicht der ICP-Status.
- Hat eine Mo- oder Anthony-Zeile keine passende Plattform-Organisation, gelten alle
  Wochenwerte als 0 und die Ampel ist ⚪ WEIß (siehe Schritt 9).

## 7. Organisation ↔ Notion-Zeile zuordnen

Plattform-Name und Board-Titel weichen oft ab. Vorgehen je Organisation:

1. Exakter Treffer auf `Unternehmensname` (Groß-/Kleinschreibung ignorieren).
2. Sonst Normalisierung: Rechtsform (GmbH, AG, & Co. KG), Bindestriche,
   Leerzeichen und Umlaute (ae/oe/ue/ss) entfernen und erneut vergleichen.
3. Sonst über die **Sende-Domains** verifizieren: `mailbox.email` bzw.
   `from_address` der Conversations gegen `Domains Name` und `Website-URL` der
   Kandidatenzeile prüfen. Das ist der verlässlichste Anker.
4. Bei mehreren Kandidaten die Zeile **mit Betreuer** und echtem `ICP-Status`
   nehmen, **nicht** die leeren Formular-Duplikate mit „Neu - keine infos und
   Materiallien".

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

## 8. Paket Modell auslesen

Aus der Spalte **„Paket Modell"** (Select):

| Wert | Stufe |
|---|---|
| 🔵 Klein Paket 3 Domains | Starter |
| 🟡 Mittlere Paket 6 Domains | Medium |
| 🟢 Großes Paket 9 Domains | Groß |
| ⚪ Kein Paket / leer | keine Bewertung → ⚪ WEIß |

Niemals aus „Domains Anzahl" oder „Domains Name" ableiten – die Felder sind
unzuverlässig gepflegt.

## 9. Ampel bestimmen

Basis ist immer die **ungedeckelte `SUMME`** der vier Wochen – nie der
`RICHTIG`-Wert (mit dem Deckel bei 10 wäre Grün für Medium und Groß unerreichbar).
Das gilt auch für Anthony-Zeilen, bei denen die Summe nicht in eine Spalte
geschrieben wird.

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

## 10. Notion schreiben

Pro Mo- oder Anthony-Zeile ein `mcp__Notion__notion-update-page` mit
`command: "update_properties"`.

Mo-Zeile:
```json
{
  "Woche 1": <a>, "Woche 2": <b>, "Woche 3": <c>, "Woche 4": <d>,
  "<SPALTE_MONAT>": <SUMME>,
  "<SPALTE_RICHTIG>": <min(SUMME, 10)>,
  "Report": "<Reporttext>"
}
```

Anthony-Zeile:
```json
{
  "Woche 1": <a>, "Woche 2": <b>, "Woche 3": <c>, "Woche 4": <d>,
  "Report": "<Reporttext>"
}
```

Regeln:
- **Immer 0 schreiben, nie leer lassen** – in allen Feldern, die für die Zeile laut
  Schritt 6 geschrieben werden. Eine leere Zelle liest sich als „nicht erfasst".
- Zeilen ohne Betreuer nicht anfassen.
- Werte anderer Monate nicht überschreiben.
- Zahlen als JSON-Number, nicht als String.
- Schlägt ein Update fehl: einmal wiederholen, sonst Zeile unter „Offene Punkte"
  melden und weitermachen.

**Selbstkontrolle nach dem Schreiben (Pflicht):** per SQL prüfen und Abweichungen
korrigieren:
- jede Mo-Zeile hat `SPALTE_MONAT` = Woche 1+2+3+4 und
  `SPALTE_RICHTIG` = min(`SPALTE_MONAT`, 10), nichts ist NULL,
- keine Zeile hat `SPALTE_RICHTIG` > 10,
- jede Anthony-Zeile hat Woche 1–4 gefüllt,
- Summe aller Wochenwerte im Board = Anzahl der zugeordneten Meeting Requests aus
  Schritt 3.

## 11. Reporttext

Deutsch, sachlich, ohne Floskeln. Aufbau:

```
<AMPEL> · <MONAT_DE> <JAHR> · <Paketstufe> (<n> Domains)

Meetings <MONAT_DE>: <SUMME> – Ziel <Zielwert der Stufe>
Abrechenbar (max. 10): <RICHTIG>
Wochen: W1 <a> · W2 <b> · W3 <c> · W4 <d>
Vormonat: <Wert> (<+/-x> ggü. Vormonat)

Analyse: <2–4 Sätze: Wo lag die Leistung, wie ist der Verlauf über die Wochen,
was fällt auf – Anlauf erst spät im Monat, Einbruch nach Woche 2, gleichmäßig
verteilt, alles aus einer Woche?>

Maßnahme: <1–3 konkrete, umsetzbare Schritte. Keine Allgemeinplätze.>
```

- Zielwert je Stufe: Starter „ab 4", Medium „ab 11", Groß „ab 23".
- Die Zeile „Abrechenbar (max. 10)" **nur bei Mo-Zeilen**; bei Anthony-Zeilen
  weglassen.
- Vormonatswert aus der Monatsspalte des Vormonats lesen; ist sie leer oder fehlt
  sie, die Zeile weglassen statt „k. A." zu schreiben.
- Bei gekündigten Kunden in der Analyse kurz vermerken, dass die Kampagne gekündigt
  ist; als Maßnahme dann nur, was noch sinnvoll ist (z. B. offene Meeting Requests
  übergeben), keine Optimierungsvorschläge.

**Was in der Analyse stehen soll – je nach Lage:**
- 🟢 Was trägt, und ob der Vorsprung stabil ist oder auf einer starken Woche beruht.
- 🟡 Wie weit zum Ziel, und welcher Hebel am schnellsten greift (Volumen, Sequenz,
  Zielgruppe, Absenderzahl).
- 🔴 Ob es an Aussteuerung (pausierte Agenten, kein Versand) oder an Wirkung
  (Versand läuft, keine Termine) liegt.
- ⚪ Was genau fehlt, damit im nächsten Monat bewertet werden kann.

Für 🔴- und ⚪-Zeilen mit `mcp__Amplifa__organization_agent_info_list` gegenprüfen:
pausierte Agenten, Playbook-Status, `sent_emails_count` gegen `total_leads_count`.
Ausnahme: gekündigte Zeilen und Zeilen ohne Plattform-Organisation – dort keinen
Call verbrennen. Für 🟢 und 🟡 reicht die Meeting-Zahl.

## 12. Abschlussmeldung

Am Ende in den Chat (kein Notion, keine Mail):

1. Verteilung 🟢 / 🟡 / ⚪ / 🔴 mit Anzahl und Meeting-Summe je Gruppe – getrennt
   für Mo und Anthony Filipiak.
2. Summe `SPALTE_MONAT` und Summe `SPALTE_RICHTIG` über alle Mo-Zeilen, plus Liste
   der Zeilen, bei denen der Deckel gegriffen hat (SUMME > 10).
3. Top 3 und Flop 3 nach Meetings.
4. Veränderungen ggü. Vormonat, die auffallen (Absturz oder Sprung > 50 %).
5. **Offene Punkte** – der wichtigste Teil, hier steht, was ein Mensch nachpflegen
   muss:
   - Zeilen ohne Betreuer, deren Organisation im Berichtsmonat Meeting Requests
     hatte (mit Anzahl),
   - Organisationen mit Meeting Requests ohne Board-Zeile,
   - Mo-/Anthony-Zeilen ohne Paket Modell,
   - nicht zuordenbare Namen, neu angelegte Spalten, fehlgeschlagene Updates.

## Grenzen

- Die Domains-Seite (`/admin/organizations/<id>/domains`) ist über den Amplifa-MCP
  **nicht** abrufbar. Die Paketgröße kommt deshalb ausschließlich aus „Paket Modell".
- `conversation_list_by_status` liefert nur Konversationen mit Status `open`. Das
  entspricht dem Admin-Filter und ist so gewollt.
- Läuft die Routine unbeaufsichtigt, niemals eine Rückfrage stellen – Annahme
  treffen, ausführen, unter „Offene Punkte" dokumentieren.
- „Woche 1–4" sind keine Monatsspalten: jeder Lauf überschreibt sie mit dem
  aktuellen Berichtsmonat.
- Ein erneuter Lauf für denselben Monat überschreibt die Werte idempotent – ein
  Nachlauf ist gefahrlos möglich.
