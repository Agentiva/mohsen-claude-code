# Routine einrichten (täglich 09:00)

Die Routine existiert bereits: `trig_014zXqmGeNjjak3uuqDegDMX`,
Cron `0 7 * * *` (UTC) = 09:00 Europe/Berlin, frische Session pro Lauf.

⚠️ **Connectors müssen in der claude.ai-Routines-Oberfläche angehängt werden.**
Der `connectors`-Parameter von `create_trigger`/`update_trigger` wird von dieser
Organisation abgelehnt („the connectors parameter is not available for this
organization"). Ohne **Amplifa**, **Amplifa_Sales_Hub** und **Notion** startet
die Routine ohne Zugriff und bricht ab.

⚠️ **Zeitumstellung:** Der Cron steht in UTC. `0 7 * * *` ist 09:00 Berlin nur
während der Sommerzeit; ab dem 25.10.2026 wird daraus 08:00. Dann auf
`0 8 * * *` ändern.

## Einstellungen

| Feld | Wert |
|---|---|
| Name | `ICP-Status Daily (täglich 9:00)` |
| Zeitplan | `0 7 * * *` UTC = täglich 09:00 Uhr (Europe/Berlin, Sommerzeit) |
| Session | jedes Mal eine neue Session |
| Connectors | `Amplifa`, `Amplifa_Sales_Hub`, `Notion` |
| Benachrichtigung | Push |
| Repo / Branch | `Agentiva/mohsen-claude-code`, Branch mit diesem Skill |

## Prompt (1:1 einfügen)

```
Führe die tägliche ICP-Status-Routine aus.

Rufe dazu ZUERST den Skill `icp-status-daily` auf (Skill-Tool, Name ohne Slash)
und folge seiner SKILL.md sowie der reference.md im selben Verzeichnis Punkt für
Punkt. Der Skill liegt im Repo unter `.claude/skills/icp-status-daily/`; falls er
nicht in der Skill-Liste auftaucht, lies die beiden Dateien direkt aus dem Repo
und arbeite sie ab.

Kurzfassung des Auftrags (Details stehen im Skill):
1. Organisationen aus der Notion-Datenbank „Kampagne Überblick"
   (collection://2a78174b-42df-81d2-80e3-000bc6b01cd6) laden – Zeilen mit
   `Gekündigt` per WHERE-Filter ausschließen, sie sind nicht Teil des Laufs.
2. Für jede Organisation die ICP-Status-MENGE bestimmen: genau ein Basisstatus
   (Live / Pausiert / Kampgane erstellen) plus null bis drei Zusatzstatus
   (Optimieren / Leads hinzufügen / Keine Emails raus gesendet). Daten aus den
   MCP-Servern Amplifa und Amplifa_Sales_Hub.
   „Pausiert" nur, wenn ALLE Agenten der Organisation auf `paused` stehen.
3. Schreiben in dieser Reihenfolge: `onb_update` mit dem Primärstatus →
   `onb_sync_notion` → bei mehr als einem Status `notion-update-page` mit dem
   vollständigen Array. Nie umgekehrt, sonst überschreibt der Sync die
   Mehrfachauswahl. Geschützte Status (Emails Approven, Alle Informationen und
   Materialien eingereicht) NIE überschreiben.
4. Eine Tagesseite in der Notion-Datenbank „Täglicher Report"
   (collection://8ff2e52d-9ebc-4f1a-9a41-d392983a06f3) anlegen, mit Tabelle aller
   Änderungen, Statusverteilung, Übersprungenen und Fehlern.

Du läufst unbeaufsichtigt: keine Rückfragen, keine anderen Felder anfassen,
nichts löschen, keine Mails senden, keine Agenten oder Playbooks ändern.
Unklarheiten gehören in den Report, nicht in eine Rückfrage. Arbeite alle
Organisationen ab, auch wenn einzelne Fehler auftreten.
```

## Ohne Routine

Der Skill lässt sich jederzeit manuell starten: `/icp-status-daily`.
