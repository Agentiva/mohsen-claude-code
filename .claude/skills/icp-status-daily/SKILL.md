---
name: icp-status-daily
description: >
  Tägliche Routine: bestimmt für jede aktive Organisation in der Notion-Datenbank
  „Kampagne Überblick" den ICP-Status als MEHRFACHAUSWAHL (Live / Optimieren /
  Pausiert / Leads hinzufügen / Keine Emails raus gesendet / Kampgane erstellen /
  Neu - keine infos und Materiallien), schreibt den Primärstatus in den Sales Hub
  und die vollständige Statusmenge nach Notion, und protokolliert alle Änderungen
  als Tagesseite in der Notion-Datenbank „Täglicher Report".
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

Notion hat historisch gewachsene Tippfehler in den Optionen. **Immer
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

### `ICP-Status` ist eine MEHRFACHAUSWAHL

Seit 29.08.2026 ist die Notion-Spalte `ICP-Status` ein **Multi-Select**. Eine
Organisation kann mehrere Status gleichzeitig tragen, z.B.
`Live` + `Optimieren` + `Leads hinzufügen`: die Kampagne läuft, ein Playbook
braucht Änderungen, und der Lead-Vorrat geht zur Neige.

Beim Schreiben nach Notion daher **immer ein JSON-Array** übergeben, nie einen
einzelnen String:

```jsonc
{"ICP-Status": ["Live", "Optimieren", "Leads hinzufügen"]}
```

Der Sales Hub (`onboardings.icp_status`) ist dagegen ein **einzelnes Textfeld**
und kann die Menge nicht abbilden. Deshalb gilt die Aufteilung aus Abschnitt 4:
Sales Hub bekommt den **Primärstatus**, Notion die **vollständige Menge**.

### Geschützte Status – NIE überschreiben

`Gekündigt`, `Emails Approven`, `Alle Informationen und Materialien eingereicht`.
Trägt eine Zeile einen davon → Organisation überspringen, im Report als
„übersprungen (geschützt)" führen.

(`Deaktiviert` existiert seit dem Options-Umbau vom 28.08.2026 nicht mehr als
Option – siehe Warnung in `reference.md`. Taucht der Wert wieder auf, ebenfalls
als geschützt behandeln.)

### `Gekündigt` = dauerhaft aus der Routine raus

Organisationen mit `Gekündigt` werden **gar nicht erst geladen**. Sie sind kein
„übersprungen", sondern nicht Teil der Grundgesamtheit – sie erscheinen weder in
den Zählern noch in der Statusverteilung des Tagesreports. Die Query in
Abschnitt 4.1 filtert sie direkt weg.

---

## 2. Statusbestimmung – Basisstatus + Zusatzstatus

Eine Organisation bekommt **genau einen Basisstatus** und **beliebig viele
Zusatzstatus**. Die Vereinigung beider ist die Menge, die nach Notion geht.

### 2a. Ausschluss und Onboarding-Gate (exklusiv)

```
0) Aktueller Notion-Status enthält Gekündigt
   → gar nicht laden (Abschnitt 4.1).
   Enthält er Emails Approven / Alle Informationen und Materialien eingereicht
   → ÜBERSPRINGEN, nichts schreiben.

1) ONBOARDING-GATE – gilt NUR, wenn die Organisation noch keine Kampagne hat,
   also: keine Amplifa-Organisation gefunden ODER (0 Playbooks UND 0 Agenten).
     a) Alle vier Pflicht-Inputs vorhanden (Website, Kontakt, Domains, Absender)?
        JA   → {"Kampgane erstellen"}
        NEIN → {"Neu - keine infos und Materiallien"}
   Das Gate liefert IMMER eine einelementige Menge – keine Zusatzstatus.
   Hat die Organisation bereits Playbooks oder Agenten, wird dieses Gate
   ÜBERSPRUNGEN – ein laufender Kunde fällt nie auf „Neu" zurück.
```

### 2b. Basisstatus – genau einer, in dieser Reihenfolge

```
Live               ≥1 Playbook `approved` UND ≥1 Agent `active`
Pausiert           sonst, wenn die Organisation ≥1 Agent hat
                   und ALLE Agenten auf `paused` stehen
Kampgane erstellen sonst (kein freigegebenes Playbook oder kein aktiver Agent)
```

⚠️ **„Pausiert" verlangt ALLE Agenten auf `paused`, nicht nur einen.** Läuft
noch ein einziger Agent, ist die Kampagne nicht pausiert – dann greift `Live`
(sofern ein Playbook freigegeben ist) oder `Kampgane erstellen`.

`Live` und `Pausiert` schließen sich automatisch aus: `Pausiert` verlangt, dass
kein Agent mehr `active` ist, `Live` verlangt mindestens einen.

### 2c. Zusatzstatus – null bis drei, unabhängig voneinander

```
Optimieren                 ≥1 Playbook mit Status `changes_requested`
                           (gilt bei jedem Basisstatus)

Leads hinzufügen           KEIN Agent mit Sequenz-Step ≤ 5
                           (alle Agenten bei Step ≥ 6 bzw. ohne Lead-Vorrat)
                           NUR wenn Basisstatus = Live

Keine Emails raus gesendet Letzte 7 Tage KEINE E-Mail raus ODER KEINE Antwort
                           NUR wenn Basisstatus = Live
```

**Warum die letzten beiden nur bei `Live` gelten:** Bei einer Kampagne, die gar
nicht läuft (`Kampgane erstellen`) oder bewusst steht (`Pausiert`), ist „nichts
rausgegangen" die Folge des Basisstatus und keine eigene Handlung. Der Hinweis
wäre reines Rauschen. `Optimieren` dagegen ist immer relevant – ein Playbook mit
Änderungswunsch muss bearbeitet werden, egal ob die Kampagne läuft.

### 2d. Primärstatus – was in den Sales Hub geht

Der Sales Hub kann nur einen Wert speichern. Der **Primärstatus** ist der
dringendste Handlungsbedarf aus der Menge, nach dieser Priorität:

```
1. Neu - keine infos und Materiallien   (Gate)
2. Kampgane erstellen                   (Gate)
3. Optimieren
4. Pausiert
5. Leads hinzufügen
6. Keine Emails raus gesendet
7. Live
8. Kampgane erstellen                   (Basisstatus)
```

Das ist exakt die alte Kaskadenreihenfolge – „Aktion vor Betrieb" bleibt damit
erhalten: Steht in der Menge irgendein Handlungsbedarf, gewinnt er gegenüber
`Live`.

### 2e. Beispiele

| Datenlage | Notion-Menge | Sales Hub |
|---|---|---|
| Playbook approved, Agent active, ø-Step 1,7, Versand + Antwort < 7 T | `["Live"]` | `Live` |
| dito, zusätzlich 1 Playbook `changes_requested` | `["Live", "Optimieren"]` | `Optimieren` |
| dito, zusätzlich ø-Step 5,8 bei allen Agenten | `["Live", "Optimieren", "Leads hinzufügen"]` | `Optimieren` |
| Playbook approved, 3 Agenten – 1 active, 2 paused | `["Live"]` | `Live` |
| Playbook approved, 3 Agenten – alle 3 paused | `["Pausiert"]` | `Pausiert` |
| alle Agenten `draft`, Playbook `changes_requested` | `["Kampgane erstellen", "Optimieren"]` | `Optimieren` |
| keine Amplifa-Org, alle vier Inputs da | `["Kampgane erstellen"]` | `Kampgane erstellen` |

---

## 3. Wie die vier Bedingungen (a)–(d) gemessen werden

(a) und (b) entscheiden über den Basisstatus (`Live` / `Pausiert` /
`Kampgane erstellen`), (c) über den Zusatzstatus „Keine Emails raus gesendet",
(d) über den Zusatzstatus „Leads hinzufügen".

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

Für den Basisstatus zwei getrennte Zählungen über **alle** Agenten der
Organisation:

```
aktive_agenten  = Anzahl Agenten mit status == "active"
alle_agenten    = Anzahl Agenten insgesamt
paused_agenten  = Anzahl Agenten mit status == "paused"

Live      ⟸ aktive_agenten ≥ 1  UND  ≥1 Playbook `approved`
Pausiert  ⟸ alle_agenten ≥ 1    UND  paused_agenten == alle_agenten
```

⚠️ Nicht „irgendein Agent pausiert" prüfen. Eine Organisation mit 5 Agenten,
von denen 4 pausiert sind und 1 läuft, ist **nicht** `Pausiert` – dort läuft
die Kampagne weiter. Erst wenn der letzte Agent steht, ist sie pausiert.

Agenten in `draft`, `ready` oder `completed` verhindern `Pausiert`, weil dann
`paused_agenten != alle_agenten` gilt. Das ist gewollt: Solche Organisationen
sind nicht pausiert, sondern gar nicht erst gestartet → `Kampgane erstellen`.

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
nicht unter die harte Zusatzregel fällt. Ist sie verletzt und der Basisstatus
`Live`, kommt der Zusatzstatus „Leads hinzufügen" in die Menge.

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

1. **Organisationsliste ziehen – ohne `Gekündigt`.**
   `mcp__Notion__notion-query-data-sources` (SQL) auf
   `collection://2a78174b-42df-81d2-80e3-000bc6b01cd6`:

   ```sql
   SELECT url, "Unternehmensname", "ICP-Status", "Onboarding-ID"
   FROM "collection://2a78174b-42df-81d2-80e3-000bc6b01cd6"
   WHERE "ICP-Status" IS NULL
      OR "ICP-Status" NOT LIKE '%Gekündigt%'
   ORDER BY "Unternehmensname"
   ```

   `ICP-Status` ist ein Multi-Select und kommt als JSON-Array-String zurück
   (`["Live","Optimieren"]`), deshalb `NOT LIKE '%Gekündigt%'` statt `!=`.
   Stand 29.08.2026: 127 Zeilen gesamt, davon 35 `Gekündigt` → **92 Zeilen**
   bleiben in der Routine.

   Gekündigte Organisationen sind damit dauerhaft raus: Sie tauchen weder in
   `Geprüft` noch in der Statusverteilung noch in „Übersprungen" auf. Nur die
   Gesamtzahl der ausgefilterten Zeilen kommt als Fußnote in den Tagesreport.

   **Doppelte Unternehmensnamen sind normal** (z.B. „AFG Healthcare GmbH" mit
   zwei Onboarding-IDs). Jede Zeile einzeln behandeln und beide auf dieselbe
   berechnete Statusmenge setzen – die Bewertung der Amplifa-Organisation muss
   dafür nur einmal gemacht und wiederverwendet werden.
2. **Onboardings einmalig laden.** `onb_list` mit `full: true`, `limit: 100`,
   über `offset` paginieren, bis alle da sind. Map bauen:
   `onboarding_id → {company_name, company_website, primary_contact_*, icp_status}`.
3. **Pro Organisation bewerten.** In Blöcken von ~10 Organisationen arbeiten,
   unabhängige Tool-Calls parallel absetzen:
   - `organization_agent_info_list(organization_name)` – Name = `Unternehmensname`
     aus Notion; findet er nichts, mit `organization_list(search: ...)` einen
     Treffer suchen (Groß-/Kleinschreibung und Rechtsform ignorieren).
   - `playbook_list(organization_name)`
   - je nach Zweig: `conversation_list_for_organization` bzw.
     `onb_list_domains` + `onb_list_senders`
   - Abschnitt 2 anwenden → **Statusmenge** + daraus abgeleiteter
     **Primärstatus** (2d).
4. **Schreiben – nur wenn die Statusmenge ≠ der aktuellen Notion-Menge ist**
   (Mengenvergleich, Reihenfolge egal). Die drei Schritte **in dieser
   Reihenfolge**, sonst überschreibt der Sync die Mehrfachauswahl wieder:

   a) `onb_update({onboarding_id, patch: {icp_status: "<PRIMÄRSTATUS>"}})`
   b) `onb_sync_notion({onboarding_id})` – schreibt den Primärstatus als
      **einelementige** Menge nach Notion.
   c) **Nur wenn die Menge mehr als einen Status hat:** danach
      `notion-update-page` mit dem vollständigen Array:
      `{"ICP-Status": ["Live", "Optimieren", "Leads hinzufügen"]}`

   ⚠️ Schritt (c) **muss nach** (b) laufen. `onb_sync_notion` kennt nur das
   einzelne Sales-Hub-Feld und setzt die Notion-Zelle auf genau einen Wert –
   liefe es nach (c), wären die Zusatzstatus weg.

   d) Existiert kein Onboarding zur Notion-Zeile, entfallen (a) und (b);
      dann nur (c) mit der vollständigen Menge.
   e) Stichprobe: bei den ersten 3 Änderungen nach dem Schreiben per Notion-Query
      prüfen, dass die Menge vollständig angekommen ist.
   f) `onb_update` gibt den **kompletten** Onboarding-Datensatz zurück (sehr
      groß). Nur `icp_status` und `ok` daraus prüfen, nichts davon in den Report
      übernehmen.

   **Bekannte Einschränkung:** Läuft `onb_sync_notion` später aus einem anderen
   Kontext erneut (z.B. Sales-Hub-Automatik), fällt die Notion-Zelle wieder auf
   den Primärstatus zurück. Die Zusatzstatus sind dann bis zum nächsten
   Routine-Lauf weg. Solange der Sales Hub kein Mehrwert-Feld hat, ist das nicht
   zu verhindern – im Tagesreport unter „Fehler & Unklarheiten" vermerken, wenn
   es auffällt.

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

Mehrere Status werden mit ` + ` verkettet:

```
29.08.2026 · Live → Live + Optimieren + Leads hinzufügen · PB 570 changes_requested, ø-Step 5,8
29.08.2026 · Live (unverändert) · ø-Step 1,7 · Versand + Antwort < 7 T
29.08.2026 · Live → Pausiert · alle 3 Agenten paused
29.08.2026 · übersprungen (geschützt: Emails Approven)
29.08.2026 · Fehler – keine Amplifa-Organisation zum Namen gefunden
```

Geschrieben wird die Spalte per `notion-update-page` auf der Zeilen-`url`:
`{"Täglichen Report": "<Zeile>"}`. Das ist die **einzige** Ausnahme von der
Regel „nur ICP-Status schreiben".

Kann in denselben `notion-update-page`-Call gepackt werden wie die Statusmenge
aus Schritt 4c – das spart die Hälfte der Schreibvorgänge:

```jsonc
{"ICP-Status": ["Live", "Optimieren"],
 "Täglichen Report": "29.08.2026 · Live → Live + Optimieren · PB 570 changes_requested"}
```

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
| MPA GmbH | Live | Live + Keine Emails raus gesendet | letzter Versand vor 12 T |
| AFG Healthcare GmbH | Leads hinzufügen | Pausiert | alle 2 Agenten `paused` |

## Statusverteilung nachher
| Status | Anzahl |
|---|---|

## Übersprungen
- Firma X – geschützter Status „Emails Approven"

## Fehler & Unklarheiten
- Firma Y – keine Amplifa-Organisation zum Notion-Namen gefunden

---
35 Organisationen mit `Gekündigt` sind nicht Teil des Laufs.
```

Der Abschnitt **Änderungen** ist der Kern – gab es keine, ausdrücklich
„Keine Statusänderungen." schreiben. Kurz und scanbar, kein Fließtext.

**Statusverteilung bei Mehrfachauswahl:** Jeder Status wird einzeln gezählt, eine
Organisation kann also in mehreren Zeilen auftauchen. Die Summe der Spalte
„Anzahl" ist damit größer als `Geprüft` – das ist korrekt und muss nicht
ausgeglichen werden. Zusätzlich eine Zeile „Organisationen mit >1 Status" mit
aufnehmen.

---

## 6. Leitplanken (unbeaufsichtigt!)

- **Nur `ICP-Status` und die Notion-Spalte `Täglichen Report` schreiben.**
  Keine anderen Onboarding- oder Notion-Felder anfassen, keine Agenten
  starten/pausieren, keine Playbooks ändern, keine Leads importieren, keine
  Mails senden. Insbesondere `Amplifa Plattform` nicht überschreiben – die
  Spalte wird separat gepflegt.
- **Gekündigte Organisationen gar nicht erst laden** (Abschnitt 4.1).
- **Geschützte Status nie überschreiben** (Abschnitt 1).
- **Nichts löschen.** Keine Notion-Seite und kein Onboarding entfernen.
- **Keine neuen Optionen erzeugen** – nur die sieben exakten Strings aus
  Abschnitt 1. Das Schema **nie** per `notion-update-data-source` anfassen.
- **Statusmenge immer als Array schreiben**, auch bei nur einem Wert:
  `{"ICP-Status": ["Live"]}`. Ein blanker String funktioniert bei einem
  Multi-Select nicht zuverlässig.
- **Reihenfolge einhalten:** erst `onb_update` + `onb_sync_notion`, dann
  `notion-update-page` mit der vollen Menge – nie umgekehrt (Abschnitt 4.4).
- **Keine Rückfragen.** Unklarheiten in den Report, nicht an den User.
- Bei komplett leerer Datenlage (Notion-Query liefert 0 Zeilen): Report mit
  `Lauf-Status: Fehlgeschlagen` und Begründung anlegen, sonst nichts tun.
