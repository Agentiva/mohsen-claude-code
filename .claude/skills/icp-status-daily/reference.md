# Referenz – IDs, Feldmappings, Snippets

## IDs

| Objekt | ID / URL |
|---|---|
| Notion-DB „Kampagne Überblick" (Data Source) | `collection://2a78174b-42df-81d2-80e3-000bc6b01cd6` |
| Notion-DB „Kampagne Überblick" (Seite) | https://app.notion.com/p/2a78174b42df81b5be38cdc8240dced2 |
| Notion-DB „Täglicher Report" (Data Source) | `collection://8ff2e52d-9ebc-4f1a-9a41-d392983a06f3` |
| Notion-DB „Täglicher Report" (Seite) | https://app.notion.com/p/45648fec1e46446398608a22f79efb5b |
| Elternseite beider DBs | „Mohsen - Kampagne", `2a78174b-42df-802e-865a-c6841b637362` |
| Amplifa Admin | https://app.amplifa.ai/admin/organizations/&lt;id&gt; |
| Onboarding-Formular | https://proposal.amplifa.ai/onboardings/&lt;onboarding_id&gt; |

## Notion-Query: Organisationsliste (ohne Gekündigt)

```sql
SELECT url,
       "Unternehmensname",
       "ICP-Status",
       "Onboarding-ID"
FROM "collection://2a78174b-42df-81d2-80e3-000bc6b01cd6"
WHERE "ICP-Status" IS NULL
   OR "ICP-Status" NOT LIKE '%Gekündigt%'
ORDER BY "Unternehmensname"
```

`ICP-Status` ist seit 29.08.2026 ein **Multi-Select** und kommt als
JSON-Array-String zurück: `["Live","Optimieren"]`. Deshalb `NOT LIKE`, nicht
`!=`. Zum Auswerten in Python/jq das Array parsen, nicht auf Stringgleichheit
prüfen.

Die Spalte `Täglichen Report` (Text) in derselben DB nimmt pro Organisation das
Tagesergebnis auf – siehe SKILL.md Abschnitt 5a.
Die Spalte `Amplifa Plattform` (Text) trägt den Admin-Deeplink und wird von der
Routine **nicht** geschrieben.

`url` ist gleichzeitig die `page_id` für `notion-update-page`.

Stand 2026-08-29: **127 Zeilen gesamt**, davon 35 `Gekündigt` → **92 Zeilen** im
Lauf. 2 Zeilen ohne `Unternehmensname` (leere Platzhalter) → als Fehler zählen
und überspringen.

Hinweis: Der Notion-SQL-Endpunkt kann bei breiten Abfragen in ein 60s-Timeout
laufen. Dann nur die vier Spalten oben selektieren und ggf. mit
`LIMIT`/`OFFSET` in Blöcken von 50 Zeilen abfragen.

## ICP-Status – Multi-Select, exakte Optionen der Notion-DB

Seit **29.08.2026** ist `ICP-Status` ein **Multi-Select** (vorher Single-Select).
Die zehn Optionen, exakt so:

```
Alle Informationen und Materialien eingereicht
Live
Pausiert
Gekündigt
Leads hinzufügen
Emails Approven
Optimieren
Kampgane erstellen                  ← Tippfehler, so schreiben
Neu - keine infos und Materiallien  ← doppeltes l, so schreiben
Keine Emails raus gesendet          ← am 28.08.2026 ergänzt
```

`Deaktiviert` existiert **nicht mehr** – die Option ist beim Options-Umbau am
28.08.2026 verschwunden (siehe Warnung unten). Keine Zeile stand darauf.

Von der Routine gesetzt werden nur: `Live`, `Optimieren`, `Pausiert`,
`Leads hinzufügen`, `Keine Emails raus gesendet`, `Kampgane erstellen`,
`Neu - keine infos und Materiallien`.

### Schreiben

Immer als Array, auch bei einem einzigen Wert:

```jsonc
mcp__Notion__notion-update-page {
  "page_id": "<url der Zeile>",
  "command": "update_properties",
  "properties": { "ICP-Status": ["Live", "Optimieren"] }
}
```

### Umstellung auf Multi-Select (29.08.2026, erledigt)

```sql
ALTER COLUMN "ICP-Status" SET MULTI_SELECT(
  'Alle Informationen und Materialien eingereicht', 'Live', 'Pausiert',
  'Gekündigt', 'Leads hinzufügen', 'Emails Approven', 'Optimieren',
  'Kampgane erstellen', 'Neu - keine infos und Materiallien',
  'Keine Emails raus gesendet')
```

Vorher/Nachher-Verteilung verglichen – **kein Datenverlust**: 35 Gekündigt,
32 Live, 19 Pausiert, 14 Keine Emails raus gesendet, 9 Kampgane erstellen,
5 Optimieren, 5 Leads hinzufügen, 3 Neu, 3 Emails Approven, 2 leer.
Farben beim `ALTER` weglassen – mit Farbangabe schlägt der Call fehl
(„Cannot update color of select with name: …").

⚠️ **Optionen nie per `ALTER COLUMN ... SET SELECT/MULTI_SELECT(...)`
nachziehen.** Notion vergibt dabei die Options-IDs neu: beim Anlegen von
„Keine Emails raus gesendet" erbte die neue Option die ID von „Deaktiviert",
und „Deaktiviert" verschwand. Das ging nur gut, weil keine einzige Zeile
auf „Deaktiviert" stand – hätte eine draufgestanden, würde sie heute
fälschlich „Keine Emails raus gesendet" anzeigen. Weitere Optionen deshalb in
der Notion-Oberfläche anlegen und danach hier eintragen. Vor jedem unvermeidbaren
Schema-Eingriff die Verteilung sichern und danach vergleichen.

⚠️ Der Sales Hub führt teilweise die Variante `Neu - keine infos und Materialien`
(einfaches „l"). Beim Schreiben über `onb_update` **immer die Notion-Schreibweise
mit doppeltem „l"** verwenden und nach dem `onb_sync_notion` stichprobenartig
prüfen, dass in Notion keine zweite Select-Option entstanden ist. Falls doch:
Wert per `notion-update-page` auf die korrekte Option zurücksetzen und im Report
vermerken.

## Status-Enums der Amplifa-API

```
Playbook: draft | changes_requested | approved | archived
Agent:    draft | ready | active | paused | completed
```

## Tool-Calls

```jsonc
// Agenten + Playbook + Statistiken + campaign_status in einem Call
mcp__Amplifa__organization_agent_info_list { "organization_name": "MPA GmbH" }

// Alle Playbooks (auch ohne Agent) – nötig für "Optimieren"
mcp__Amplifa__playbook_list { "organization_name": "MPA GmbH" }

// Organisation zum Notion-Namen suchen, wenn der exakte Name nicht greift
mcp__Amplifa__organization_list { "search": "MPA", "limit": 20 }

// Neueste Konversation (7-Tage-Antwortcheck)
mcp__Amplifa__conversation_list_for_organization { "organization_name": "MPA GmbH", "per_page": 1 }

// Onboardings in Blöcken
mcp__Amplifa_Sales_Hub__onb_list { "full": true, "limit": 100, "offset": 0 }

// Nur im Onboarding-Gate
mcp__Amplifa_Sales_Hub__onb_list_domains { "onboarding_id": "<uuid>" }
mcp__Amplifa_Sales_Hub__onb_list_senders { "onboarding_id": "<uuid>" }

// Schreiben
mcp__Amplifa_Sales_Hub__onb_update { "onboarding_id": "<uuid>", "patch": { "icp_status": "Live" } }
mcp__Amplifa_Sales_Hub__onb_sync_notion { "onboarding_id": "<uuid>" }
```

## Große Conversation-Antwort mit jq auswerten

`conversation_list_for_organization` liefert komplette Mail-Bodies und sprengt
das Kontextlimit; die Harness legt das Ergebnis dann als Datei ab und nennt den
Pfad. **Datei nie ganz lesen** – nur diese Felder ziehen:

```bash
F=<pfad-aus-der-tool-antwort>

# Antwort-Check: Zeitpunkt der letzten Antwort + Gesamtzahl Konversationen
jq -c '{last_reply_at: .conversations[0].last_reply_at,
        total: .pagination.total_count}' "$F"

# Sende-Check: jüngste ausgehende Nachricht
jq -r '[.conversations[].messages[]
        | select(.direction=="outbound") | .message_at] | max' "$F"
```

Landet das Ergebnis ausnahmsweise direkt im Kontext, dieselben Felder direkt
ablesen.

## Relevante Felder aus `organization_agent_info_list`

```jsonc
agent.status                              // active | paused | ...
agent.playbook.status                     // approved | changes_requested | ...
statistics.sent_emails_count              // Zähler für ø-Step
statistics.leads_in_sequence_count        // Nenner für ø-Step
campaign_status.leads_sent_today          // Sende-Check (Fallback)
campaign_status.scheduled_sends_today     // Sende-Check (Fallback)
campaign_status.leads_eligible_now        // harte Zusatzregel Sequenzende
campaign_status.leads_not_yet_contacted   // harte Zusatzregel Sequenzende
campaign_status.paused / paused_at        // Zusatzbeleg für "Pausiert"
```

Beispiel MPA GmbH (2026-08-28):
`sent_emails_count 34.046 / leads_in_sequence_count 19.929 = ø-Step 1,7` → ≤ 5,
Playbook `approved`, Agent `active` → Live-Bedingungen (a), (b), (d) erfüllt.

## Bekannte Näherung: Sequenz-Step

Die Admin-Oberfläche zeigt unter „Lead Sequence" die echte Step-Verteilung der
Leads. Diese Verteilung ist über MCP **nicht** abrufbar, deshalb der
Durchschnitts-Proxy `sent_emails_count / leads_in_sequence_count`.

Sobald ein Tool die echte Step-Verteilung liefert, hat diese Vorrang: dann gilt
„mindestens ein Agent mit Step ≤ 5" wörtlich auf der Verteilung, und dieser
Abschnitt sowie Abschnitt 3 (d) der SKILL.md sind zu aktualisieren.

## Namensabgleich Notion ↔ Amplifa

Notion-`Unternehmensname` und Amplifa-`organization_name` weichen häufig ab
(z.B. Notion „IQ-Service" vs. Amplifa „IQ Services", Notion „Pamminger.at" vs.
Amplifa „Pamminger Verpackungstechnik"). Vorgehen:

1. Exakter Treffer auf `organization_name`.
2. Sonst `organization_list(search: <erstes Wort des Notion-Namens>)` und
   normalisiert vergleichen (Kleinschreibung, ohne Rechtsform GmbH/AG/e.K.,
   ohne Bindestriche/Punkte, ohne TLD-Endungen wie `.at`/`.de`).
3. Sonst über die Website-Domain aus dem Onboarding (`company_website`)
   gegen `Website-URL` der Notion-Zeile abgleichen.
4. Kein eindeutiger Treffer → Organisation als **Fehler** in den Report,
   Status nicht ändern.

## Spalte „Amplifa Plattform"

Textspalte in „Kampagne Überblick", enthält den Deeplink in die Admin-UI:

```
https://app.amplifa.ai/admin/organizations/<organization_id>
```

`organization_id` kommt aus `mcp__Amplifa__organization_list`. Die Zuordnung
Notion-`Unternehmensname` → `organization_id` folgt denselben Regeln wie der
Namensabgleich weiter unten.

Die **Routine schreibt diese Spalte nicht** – sie wird separat gepflegt, weil
sich die Org-ID praktisch nie ändert. Neu angelegte Organisationen bekommen den
Link beim nächsten manuellen Durchlauf.

Stand 29.08.2026: 101 der 127 Zeilen haben eine zuordenbare Amplifa-Org.
26 Zeilen ohne Org – überwiegend gekündigte Altkunden plus die Neuzugänge ohne
Plattform-Anlage: All for One Group SE, CRMFIRST, Dermaceutical GmbH,
ENWITO GmbH, montratec GmbH, Passmedientechnik GmbH, Peter Pan gmbh,
QA-Test Formcheck, Vertigis, profine.

⚠️ `REMIRA Austria GmbH` ist auf die generische Org `Remira` (59) gemappt – es
gibt keine eigene Austria-Organisation. Vor Verwendung prüfen.

## Verifizierter Schreibpfad

**Single-Status (Test am 2026-08-28)** – „AFG Healthcare GmbH", 2 Agenten `paused`:

```
onb_update  { onboarding_id: "48731671-…", patch: { icp_status: "Pausiert" } }  → ok, icp_status "Pausiert"
onb_sync_notion { onboarding_id: "48731671-…" }                                 → ok, action "updated"
Notion-Query                                                                    → ICP-Status ["Pausiert"]
```

Der Sync übernimmt den String 1:1 und erzeugt **keine** neue Option in Notion.

**Multi-Status** – zusätzlicher dritter Schritt, zwingend **nach** dem Sync:

```
onb_update      { patch: { icp_status: "<PRIMÄRSTATUS>" } }
onb_sync_notion { onboarding_id: … }                       → Notion = ["<PRIMÄRSTATUS>"]
notion-update-page { properties: { "ICP-Status": ["Live","Optimieren"] } }
```

`onb_sync_notion` kennt nur das einzelne Sales-Hub-Textfeld und setzt die
Notion-Zelle auf genau einen Wert. Läuft es nach `notion-update-page`, sind die
Zusatzstatus wieder weg.

⚠️ `onb_update` antwortet mit dem kompletten Onboarding-Datensatz (inkl.
`website_analysis`, `suggested_*`, `selected_*` – mehrere tausend Zeilen).
Nur `ok` und `data.icp_status` auswerten.
