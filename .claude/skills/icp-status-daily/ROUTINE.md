# Routine einrichten (täglich 09:00)

Die Routine muss **in der claude.ai-Routines-Oberfläche** angelegt werden, nicht
per Tool: nur dort lassen sich die Connectors **Amplifa**, **Amplifa_Sales_Hub**
und **Notion** an die Routine hängen. Ohne diese drei Connectors startet die
Routine ohne Zugriff auf Amplifa und Notion und kann nichts ausrichten.

## Einstellungen

| Feld | Wert |
|---|---|
| Name | `ICP-Status Daily (09:00)` |
| Zeitplan | täglich 09:00 Uhr (Europe/Berlin) |
| Session | jedes Mal eine neue Session |
| Connectors | `Amplifa`, `Amplifa_Sales_Hub`, `Notion` |
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
1. Alle Organisationen aus der Notion-Datenbank „Kampagne Überblick"
   (collection://2a78174b-42df-81d2-80e3-000bc6b01cd6) laden.
2. Für jede Organisation den ICP-Status über die Entscheidungskaskade des Skills
   bestimmen (Daten aus den MCP-Servern Amplifa und Amplifa_Sales_Hub).
3. Geänderte Status via `onb_update` + `onb_sync_notion` schreiben. Geschützte
   Status (Gekündigt, Deaktiviert, Emails Approven, Alle Informationen und
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
