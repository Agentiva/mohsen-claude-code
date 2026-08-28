---
name: icp-status-daily
description: >
  Tägliche Routine: bestimmt für JEDE Organisation in der Notion-Datenbank
  „Kampagne Überblick" den korrekten ICP-Status (Live / Optimieren / Pausiert /
  Leads hinzufügen / Kampgane erstellen / Neu - keine infos und Materiallien),
  schreibt ihn in den Sales Hub und synct ihn nach Notion, und protokolliert alle
  Änderungen als Tagesseite in der Notion-Datenbank „Täglicher Report".
  IMMER nutzen, wenn der User sagt "ICP-Status prüfen/aktualisieren/bestimmen",
  "ICP-Status Routine laufen lassen", "welche Kunden sind Live", oder wenn die
  Cloud-Routine um 09:00 feuert. Läuft UNBEAUFSICHTIGT – keine Rückfragen,
  Best-Effort-Entscheidungen, Unklarheiten werden im Report protokolliert.
---

# ICP-Status Daily (Routine)

Diese SKILL.md ist der **Routine-Prompt**. Sie läuft 1x täglich um 09:00 Uhr
unbeaufsichtigt. Keine Rückfragen. Nur lesen, bewerten, ICP-Status schreiben,
Tagesreport in Notion anlegen.

Alle IDs, Feldmappings und jq-Snippets stehen in `reference.md` – **vor dem
ersten Schreibvorgang lesen**.

---

## 0. Grundgerüst

| Was | Wo |
|---|---|
| Organisationsliste (Quelle der Wahrheit) | Notion-DB **Kampagne Überblick**, `collection://2a78174b-42df-81d2-80e3-000bc6b01cd6` |
| Kampagnen-/Agent-/Playbook-Daten | MCP **Amplifa** |
| Onboarding-Daten (Website, Kontakt, Domains, Absender) | MCP **Amplifa_Sales_Hub** (`onb_*`) |
| Schreibziel ICP-Status | Sales Hub `onb_update` → `onb_sync_notion` |
| Tagesprotokoll | Notion-DB **Täglicher Report**, `collection://8ff2e52d-9ebc-4f1a-9a41-d392983a06f3` |

**Stichtag:** Laufdatum. „Letzte 7 Tage" = `Laufdatum - 7 Tage` bis jetzt.

---

## 1. Die sieben Status (EXAKTE Schreibweise!)

Notion hat historisch gewachsene Tippfehler in den Select-Optionen. **Immer
genau diese Strings schreiben**, sonst legt Notion neue Optionen an:

| Status | EXAKTER String |
|---|---|
| Live | `Live` |
| Optimieren | `Optimieren` |
| Pausiert | `Pausiert` |
| Leads hinzufügen | `Leads hinzufügen` |
| Kampagne erstellen | `Kampgane erstellen` ← Tippfehler ist Absicht |
| Neu | `Neu - keine infos und Materiallien` ← doppeltes „l" ist Absicht |
| Keine Emails raus gesendet | `Keine Emails raus gesendet` |

**Geschützte Status – NIE überschreiben:** `Gekündigt`, `Deaktiviert`,
`Emails Approven`, `Alle Informationen und Materialien eingereicht`.
Steht in Notion schon einer davon → Organisation überspringen, im Report als
„übersprungen (geschützt)" führen.

---

## 2. Entscheidungskaskade (Aktion vor Betrieb)

Die **erste** zutreffende Regel gewinnt. Von oben nach unten prüfen.

```
0) Aktueller Notion-Status ∈ {Gekündigt, Deaktiviert, Emails Approven,
   Alle Informationen und Materialien eingereicht}
   → ÜBERSPRINGEN, nichts schreiben.

1) ONBOARDING-GATE – gilt NUR, wenn die Organisation noch keine Kampagne hat,
   also: keine Amplifa-Organisation gefunden ODER (0 Playbooks UND 0 Agenten).
     a) Alle vier Pflicht-Inputs vorhanden (Website, Kontakt, Domains, Absender)?
        JA   → "Kampgane erstellen"
        NEIN → "Neu - keine infos und Materiallien"
   Hat die Organisation bereits Playbooks oder Agenten, wird dieses Gate
   ÜBERSPRUNGEN – ein laufender Kunde fällt nie auf „Neu" zurück.

2) ≥1 Playbook mit Status `changes_requested`
   → "Optimieren"

3) ≥1 Agent mit Status `paused`
   → "Pausiert"

4) Sequenz-Vorrat erschöpft – KEIN Agent mit Sequenz-Step ≤ 5
   (alle Agenten stehen bei Step ≥ 6 bzw. haben keinen Lead-Vorrat mehr)
   → "Leads hinzufügen"

5) Letzte 7 Tage: KEINE E-Mail rausgeschickt ODER KEINE Antwort erhalten
   → "Keine Emails raus gesendet"

6) LIVE-CHECK – jetzt müssen nur noch (a) und (b) stimmen, denn (c) und (d)
   sind durch die Regeln 4 und 5 bereits abgehandelt:
     a) ≥1 Playbook mit Status `approved`      (= „Active" in der Admin-UI)
     b) ≥1 Agent mit Status `active`
     c) Letzte 7 Tage ≥1 Versand UND ≥1 Antwort   (durch Regel 5 sichergestellt)
     d) ≥1 Agent mit Sequenz-Step ≤ 5             (durch Regel 4 sichergestellt)
   → "Live"

7) SONST – (a) oder (b) verletzt, also kein freigegebenes Playbook oder kein
   aktiver Agent → "Kampgane erstellen"
```

**Warum Regel 4 vor Regel 5 steht:** Sind die Leads am Sequenzende, ist „nichts
rausgegangen" nur das Symptom – die Ursache und die Handlung ist „Leads
hinzufügen". „Keine Emails raus gesendet" bleibt damit für die Fälle, in denen
Vorrat da ist, aber trotzdem nichts läuft (Versand steht, Zustellprobleme,
Kampagne tot) oder in denen zwar gesendet wird, aber seit 7 Tagen keine einzige
Antwort kam.

---

## 3. Wie die vier Bedingungen (a)–(d) gemessen werden

(a) und (b) entscheiden über „Live" bzw. „Kampgane erstellen", (c) über
„Keine Emails raus gesendet", (d) über „Leads hinzufügen".

Ein Tool-Call liefert fast alles: `mcp__Amplifa__organization_agent_info_list`
(Agenten + deren Playbook + Statistiken + campaign_status in einem Rutsch).
Zusätzlich `mcp__Amplifa__playbook_list` für Playbooks ohne Agent.

### (a) Playbook „Active"
Amplifa kennt keinen Playbook-Status „active". Mapping:

| Admin-UI | API-Status |
|---|---|
| Active | `approved` |
| Changes Requested | `changes_requested` |
| Draft | `draft` |
| Archived | `archived` |

→ „mindestens ein Active" = mindestens ein Playbook mit `status: "approved"`.

**Vom Auftraggeber bestätigt (28.08.2026):** Playbook „Active" ist gleich
`approved`. Nicht neu interpretieren – `draft` und `archived` zählen nie als
Active, auch wenn der Agent dazu läuft.

### (b) Agent-Status
Direkt aus `agent.status`: `draft` / `ready` / `active` / `paused` / `completed`.

### (c) 7-Tage-Aktivität (E-Mail raus + Antwort rein)

Diese Bedingung entscheidet über den Status **„Keine Emails raus gesendet"**:
Sie ist verletzt, sobald **eines** von beiden fehlt – kein Versand ODER keine
Antwort in den letzten 7 Tagen.

**Antwort erhalten:** `mcp__Amplifa__conversation_list_for_organization`
mit `per_page: 1`, Seite 1. Konversationen sind absteigend nach Aktualität
sortiert – die neueste Konversation genügt.
→ erfüllt, wenn `conversations[0].last_reply_at` innerhalb der letzten 7 Tage liegt.
→ 0 Konversationen (`pagination.total_count == 0`) → nicht erfüllt.

⚠️ **Die Antwort dieses Tools ist riesig** (volle Mail-Bodies, oft >500k Zeichen)
und wird von der Harness in eine Datei ausgelagert. Das ist gewollt: Danach nur
noch mit `jq` die zwei benötigten Felder herausziehen, **niemals** die Datei
komplett lesen. Snippets in `reference.md`.

**E-Mail rausgeschickt:** erfüllt, wenn eines davon zutrifft
1. In der geladenen Konversation gibt es eine Nachricht mit
   `direction == "outbound"` und `message_at` innerhalb der letzten 7 Tage, ODER
2. bei irgendeinem Agenten der Organisation gilt
   `campaign_status.leads_sent_today > 0` oder `scheduled_sends_today > 0`.

### (d) Sequenz-Step ≤ 5

Die Amplifa-MCP-Schnittstelle liefert **keine** Step-Verteilung der Leads. Der
Step wird deshalb pro Agent als Durchschnitt berechnet:

```
ø-Step = sent_emails_count / max(leads_in_sequence_count, 1)
```

- `ø-Step ≤ 5` → Agent hat noch Sequenz-Vorrat → Bedingung (d) erfüllt.
- `ø-Step ≥ 6` → Agent ist am Sequenzende → Leads nachlegen.
- **Harte Zusatzregel:** ist bei einem Agenten
  `campaign_status.leads_eligible_now == 0` UND `leads_not_yet_contacted == 0`,
  gilt er unabhängig vom ø-Step als „am Ende" (kein Vorrat mehr).

Bedingung (d) ist erfüllt, sobald **mindestens ein** Agent ø-Step ≤ 5 hat und
nicht unter die harte Zusatzregel fällt. Ist sie verletzt, greift Kaskaden-Regel 4
(„Leads hinzufügen") – und zwar vor der 7-Tage-Prüfung.

Den berechneten ø-Step pro Agent im Report mitschreiben, damit die Näherung
nachvollziehbar bleibt.

### Onboarding-Pflicht-Inputs (nur für das Gate in Schritt 1)

| Input | Quelle | Erfüllt wenn |
|---|---|---|
| Website | `onb_list` (`full: true`) → `company_website` | nicht leer |
| Kontakt | `onb_list` → `primary_contact_name` **oder** `primary_contact_email` | nicht leer |
| Domains | `onb_list_domains` | ≥1 Domain-Eintrag |
| Absender | `onb_list_senders` | ≥1 Sender-Eintrag |

Die beiden Extra-Calls (`onb_list_domains`, `onb_list_senders`) **nur** im
Gate-Zweig ausführen – nicht für laufende Kunden.

---

## 4. Ablauf

1. **Organisationsliste ziehen.** `mcp__Notion__notion-query-data-sources` (SQL)
   auf `collection://2a78174b-42df-81d2-80e3-000bc6b01cd6`:
   `url`, `Unternehmensname`, `ICP-Status`, `Onboarding-ID`. (~126 Zeilen.)
   **Doppelte Unternehmensnamen sind normal** (z.B. „AFG Healthcare GmbH" mit
   zwei Onboarding-IDs). Jede Zeile einzeln behandeln und beide auf denselben
   berechneten Status setzen – die Bewertung der Amplifa-Organisation muss dafür
   nur einmal gemacht und wiederverwendet werden.
2. **Onboardings einmalig laden.** `onb_list` mit `full: true`, `limit: 100`,
   über `offset` paginieren, bis alle da sind. Map bauen:
   `onboarding_id → {company_name, company_website, primary_contact_*, icp_status}`.
3. **Pro Organisation bewerten.** In Blöcken von ~10 Organisationen arbeiten,
   unabhängige Tool-Calls parallel absetzen:
   - `organization_agent_info_list(organization_name)` – Name = `Unternehmensname`
     aus Notion; findet er nichts, mit `organization_list(search: ...)` einen
     Treffer suchen (Groß-/Kleinschreibung und Rechtsform ignorieren).
   - `playbook_list(organization_name)`
   - je nach Kaskade: `conversation_list_for_organization` bzw.
     `onb_list_domains` + `onb_list_senders`
   - Kaskade aus Abschnitt 2 anwenden → Ziel-Status.
4. **Schreiben – nur wenn Ziel-Status ≠ aktueller Notion-Status:**
   a) `onb_update({onboarding_id, patch: {icp_status: "<EXAKTER String>"}})`
   b) `onb_sync_notion({onboarding_id})`
   c) Danach stichprobenartig (erste 3 Änderungen) via Notion prüfen, ob der
      Wert korrekt angekommen ist. Weicht er ab oder existiert kein Onboarding,
      direkt per `notion-update-page` die Notion-Zeile setzen
      (`{"ICP-Status": "<EXAKTER String>"}`).
   d) `onb_update` gibt den **kompletten** Onboarding-Datensatz zurück (sehr
      groß). Nur `icp_status` und `ok` daraus prüfen, nichts davon in den Report
      übernehmen.

4b. **Spalte `Täglichen Report` setzen – für JEDE geprüfte Organisation**,
   auch ohne Statusänderung (Abschnitt 5a).
5. **Tagesreport anlegen** (Abschnitt 5).

**Fehlerverhalten:** Ein Fehler bei einer Organisation bricht den Lauf NICHT ab.
Organisation als „Fehler" zählen, Grund notieren, weitermachen.

---

## 5. Report in Notion – zwei Ebenen

### 5a. Pro Organisation: Spalte „Täglichen Report"

Die Notion-DB **Kampagne Überblick** hat die Text-Spalte `Täglichen Report`.
Dort kommt für JEDE geprüfte Organisation das Tagesergebnis rein – auch bei
unverändertem Status. Eine Zeile, kein Fließtext, der Vortagswert wird
überschrieben (die Historie steckt in den Tagesseiten aus 5b):

```
28.08.2026 · Live → Keine Emails raus gesendet · letzter Versand vor 12 T, letzte Antwort vor 15 T
28.08.2026 · Live (unverändert) · ø-Step 1,7 · Versand + Antwort < 7 T
28.08.2026 · übersprungen (geschützt: Gekündigt)
28.08.2026 · Fehler – keine Amplifa-Organisation zum Namen gefunden
```

Geschrieben wird die Spalte per `notion-update-page` auf der Zeilen-`url`:
`{"Täglichen Report": "<Zeile>"}`. Das ist die **einzige** Ausnahme von der
Regel „nur icp_status schreiben".

### 5b. Pro Tag: Sammelseite

Eine neue Seite in **Täglicher Report**
(`collection://8ff2e52d-9ebc-4f1a-9a41-d392983a06f3`) via `notion-create-pages`.
Existiert für das Datum schon eine Seite, diese stattdessen aktualisieren.

**Properties**

| Property | Wert |
|---|---|
| `Report` | `ICP-Status – TT.MM.JJJJ` |
| `date:Datum:start` | `JJJJ-MM-TT` |
| `Routine` | `ICP-Status` |
| `Lauf-Status` | `OK` / `Mit Warnungen` (≥1 Fehler) / `Fehlgeschlagen` (Abbruch) |
| `Geprüft`, `Geändert`, `Unverändert`, `Übersprungen`, `Fehler` | Zahlen |

**Seiteninhalt**

```markdown
## Änderungen
| Organisation | Vorher | Nachher | Begründung |
|---|---|---|---|
| MPA GmbH | Live | Keine Emails raus gesendet | letzter Versand vor 12 T |
| AFG Healthcare GmbH | Leads hinzufügen | Pausiert | 2 Agenten `paused` |

## Statusverteilung nachher
| Status | Anzahl |
|---|---|

## Übersprungen
- Firma X – geschützter Status „Gekündigt"

## Fehler & Unklarheiten
- Firma Y – keine Amplifa-Organisation zum Notion-Namen gefunden
```

Der Abschnitt **Änderungen** ist der Kern – gab es keine, ausdrücklich
„Keine Statusänderungen." schreiben. Kurz und scanbar, kein Fließtext.

---

## 6. Leitplanken (unbeaufsichtigt!)

- **Nur `icp_status` und die Notion-Spalte `Täglichen Report` schreiben.**
  Keine anderen Onboarding- oder Notion-Felder anfassen, keine Agenten starten/pausieren, keine Playbooks ändern, keine
  Leads importieren, keine Mails senden.
- **Geschützte Status nie überschreiben** (Abschnitt 1).
- **Nichts löschen.** Keine Notion-Seite und kein Onboarding entfernen.
- **Keine neuen Select-Optionen erzeugen** – nur die sechs exakten Strings.
- **Keine Rückfragen.** Unklarheiten in den Report, nicht an den User.
- Bei komplett leerer Datenlage (Notion-Query liefert 0 Zeilen): Report mit
  `Lauf-Status: Fehlgeschlagen` und Begründung anlegen, sonst nichts tun.
