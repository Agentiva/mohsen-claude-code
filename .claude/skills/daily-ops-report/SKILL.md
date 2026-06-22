---
name: daily-ops-report
description: >
  Tägliche Routine: scannt die letzten 24h in Slack (Channels + private DMs) und im
  Outlook-Postfach, zieht Kunden-Aufgaben heraus und pflegt ein dauerhaftes Bug- &
  Optimierungs-Backlog (Notion-Datenbank) für die amplifa-Software. Liefert
  anschließend ein Daily-Digest per Slack-DM. Läuft UNBEAUFSICHTIGT
  als Cloud-Routine – muss daher komplett selbsterklärend sein und darf KEINE
  Rückfragen stellen, sondern trifft Best-Effort-Entscheidungen und loggt
  Unklarheiten.
---

# Daily Ops Report (Routine)

Diese SKILL.md ist der **Routine-Prompt**. Sie läuft 1x täglich unbeaufsichtigt.
Keine Rückfragen, keine destruktiven Aktionen, keine Antworten an Kunden – nur
lesen, klassifizieren, ins Backlog schreiben, Digest posten.

## Zeitfenster
Letzte 24 Stunden (bzw. seit dem letzten Lauf). Lokale Zeitzone.

## 1. Quellen einsammeln
- **Slack:** Kunden-/Shared-Channels + private Channels und Direktnachrichten (DMs)
  der letzten 24h lesen. Auf Aufgaben, Anfragen, Beschwerden, Bug-Meldungen und
  Verbesserungsideen achten.
- **Outlook-Postfach:** neue/ungelesene Mails der letzten 24h. Gleiche Signale
  extrahieren. (Nur Outlook – kein Gmail.)

## 2. Jeden Fund klassifizieren in eine von drei Kategorien
- **Kunden-Aufgabe** – To-do gegenüber einem Kunden (mit Kunde, Fälligkeit,
  Priorität, Quelle).
- **Software-Bug** – Fehlverhalten in der amplifa-Plattform.
- **Optimierung / Feature-Request** – Verbesserungswunsch / Idee.

Reine Infos/FYI ohne Handlungsbedarf: ignorieren.

## 3. Backlog pflegen (Notion – dauerhaft)
Ziel-Datenbank: **„amplifa Bug- & Optimierungs-Backlog"** (Schema unten).
- Vor dem Anlegen **gegen bestehende Einträge deduplizieren** (Signatur =
  Quelle + Kurzbeschreibung, semantisch ähnlich = Dublette).
- Neuer Bug/Optimierung → neuer Eintrag, Status `Neu`.
- Bereits vorhanden → **nicht doppeln**, sondern „Erneut gemeldet"-Zähler +1 und
  `Zuletzt gemeldet` aktualisieren (Signal für Häufigkeit/Priorität).
- Kunden-Aufgaben gehören NICHT ins Software-Backlog – die kommen nur in den
  Digest (optional separate Task-DB, falls vorhanden).

## 4. Daily-Digest posten (Slack-DM)
Als **private Direktnachricht (DM) an den User** posten (nicht in einen
öffentlichen Channel):
- **Heutige Kunden-Aufgaben** (gruppiert nach Kunde, mit Priorität)
- **Neu geloggte Bugs** (Titel + Kunde/Quelle)
- **Neu geloggte Optimierungen**
- **Top 3 zum sofort Anpacken** (eigene Priorisierung)
- Eine Zeile zu Unklarheiten, die geprüft werden sollten.

Knapp, scanbar, kein Roman.

## Notion-Schema: „amplifa Bug- & Optimierungs-Backlog"
| Feld | Typ | Werte |
|---|---|---|
| Titel | Title | Kurzname |
| Typ | Select | Bug / Optimierung |
| Beschreibung | Text | Detail |
| Kunde/Quelle | Text | Kunde + Channel/Mail |
| Priorität | Select | Hoch / Mittel / Niedrig |
| Status | Select | Neu / In Arbeit / Erledigt / Verworfen |
| Erstmals gemeldet | Date | |
| Zuletzt gemeldet | Date | |
| Erneut gemeldet | Number | Zähler |

Existiert die DB noch nicht: einmalig mit diesem Schema anlegen, dann befüllen.

## Leitplanken (unbeaufsichtigt!)
- Niemals an Kunden antworten oder etwas in Slack/Mail nach außen schicken außer
  den Digest als private DM an den User.
- Nichts löschen/überschreiben – nur anlegen/aktualisieren.
- Bei leeren Quellen: kurzen „nichts Neues"-Digest posten.
