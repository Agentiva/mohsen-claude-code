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

## Notion-Query: Organisationsliste

```sql
SELECT url,
       "Unternehmensname",
       "ICP-Status",
       "Onboarding-ID"
FROM "collection://2a78174b-42df-81d2-80e3-000bc6b01cd6"
ORDER BY "Unternehmensname"
```

`url` ist gleichzeitig die `page_id` für `notion-update-page`.
Stand 2026-08-28: 126 Zeilen, alle mit gesetzter `Onboarding-ID`.

Hinweis: Der Notion-SQL-Endpunkt kann bei breiten Abfragen in ein 60s-Timeout
laufen. Dann nur die vier Spalten oben selektieren und ggf. mit
`LIMIT`/`OFFSET` in Blöcken von 50 Zeilen abfragen.

## ICP-Status – exakte Select-Optionen der Notion-DB

```
Alle Informationen und Materialien eingereicht
Live
Pausiert
Gekündigt
Leads hinzufügen
Emails Approven
Optimieren
Kampgane erstellen                  ← Tippfehler, so schreiben
Deaktiviert
Neu - keine infos und Materiallien  ← doppeltes l, so schreiben
```

Von der Routine gesetzt werden nur: `Live`, `Optimieren`, `Pausiert`,
`Leads hinzufügen`, `Kampgane erstellen`, `Neu - keine infos und Materiallien`.

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

## Verifizierter Schreibpfad (Test am 2026-08-28)

Am Beispiel „AFG Healthcare GmbH" (2 Agenten `paused` → Kaskade Regel 3):

```
onb_update  { onboarding_id: "48731671-…", patch: { icp_status: "Pausiert" } }  → ok, icp_status "Pausiert"
onb_sync_notion { onboarding_id: "48731671-…" }                                 → ok, action "updated"
Notion-Query                                                                    → ICP-Status "Pausiert"
```

Ergebnis: Der Sync übernimmt den String 1:1, es entsteht **keine** neue
Select-Option in Notion. Der Pfad `onb_update` → `onb_sync_notion` ist damit der
Standardweg; `notion-update-page` bleibt reiner Fallback.

⚠️ `onb_update` antwortet mit dem kompletten Onboarding-Datensatz (inkl.
`website_analysis`, `suggested_*`, `selected_*` – mehrere tausend Zeilen).
Nur `ok` und `data.icp_status` auswerten.
