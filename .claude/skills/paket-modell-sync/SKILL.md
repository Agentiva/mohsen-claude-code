---
name: paket-modell-sync
description: >
  Tägliche Routine: prüft im Notion-Board „Kampagne Überblick – Board" alle
  Unternehmen, deren Spalte „Paket Modell" leer ist oder auf „⚪ Kein Paket"
  steht, gleicht sie gegen die Vertrags- und Abo-Daten im amplifa Sales Hub ab
  und setzt das passende Paket (🔵 Klein / 🟡 Mittlere / 🟢 Großes), sobald ein
  Vertrag existiert. Läuft UNBEAUFSICHTIGT als Cloud-Routine – keine
  Rückfragen, keine Downgrades, nur Hochstufungen von „leer/Kein Paket" auf ein
  echtes Paket. Auch manuell nutzbar, wenn der User sagt „prüf die Paket-Modelle",
  „gleich die Pakete im Board ab" oder „welche Kunden haben inzwischen einen Vertrag".
---

# Paket-Modell-Sync (Routine)

Diese SKILL.md ist der vollständige Routine-Prompt. Sie läuft 1× täglich
unbeaufsichtigt. **Keine Rückfragen stellen.** Bei Unklarheit: Zeile
unverändert lassen und im Digest als „geprüft, offen" listen.

## Ziel in einem Satz
Kunden, die im Board noch als „ohne Paket" geführt werden, aber inzwischen einen
Vertrag oder ein aktives Stripe-Abo haben, bekommen automatisch das richtige
Paket-Modell zugewiesen.

## Fixe Adressen

**Notion-Board:** „Kampagne Überblick – Board"
- Datenbank-ID: `14a55068-b099-4214-88e8-827673182558`
- Data Source: `collection://2a78174b-42df-81d2-80e3-000bc6b01cd6`
- Titel-Spalte: `Unternehmensname`
- Zielspalte: `Paket Modell` (Typ: select)

Die vier gültigen Optionen — **exakt so schreiben, inkl. Emoji und Leerzeichen**:
```
⚪ Kein Paket
🔵 Klein Paket 3 Domains
🟡 Mittlere Paket 6 Domains
🟢 Großes Paket 9 Domains
```

**Amplifa Sales Hub (MCP):** Tabellen über `raw_query` (read-only SELECT)
- `deal_contracts` → `company_name, product_name, product_price, contract_start, growth_start, trial_end, cancelled_at`
- `stripe_customers` → `company_name, mrr, status, subscription_status`
- `deals` → `company, stage, deal_value, won_date`

## Ablauf

### 1. Kandidaten aus Notion holen
```sql
SELECT url, "Unternehmensname", "Paket Modell"
FROM "collection://2a78174b-42df-81d2-80e3-000bc6b01cd6"
WHERE "Paket Modell" IS NULL OR "Paket Modell" = '⚪ Kein Paket'
ORDER BY "Unternehmensname"
```
Zeilen ohne Unternehmensname (leere Karten) überspringen.

### 2. Vertragsdaten holen
Einmal alle Verträge ziehen und lokal matchen – nicht pro Firma einzeln abfragen:
```sql
SELECT company_name, product_name, product_price, contract_start, cancelled_at
FROM deal_contracts
```
Fallback für Firmen ohne Vertragszeile:
```sql
SELECT company_name, mrr, status, subscription_status FROM stripe_customers
```

### 3. Namens-Matching
Die Schreibweisen weichen zwischen Notion und Sales Hub systematisch ab. Vor dem
Vergleich normalisieren:
- Kleinschreibung, Umlaute auflösen (ä→ae, ö→oe, ü→ue, ß→ss)
- Rechtsformen entfernen: GmbH, AG, SE, KG, GmbH & Co. KG, Holding, Ltd, LLC, „& Co."
- Bindestriche, Punkte, Leerzeichen und TLDs (`.at`, `.de`, `.com`) entfernen
- Danach: exakter Treffer > Präfix-Treffer > Substring-Treffer

Bewährte Beispiele: `Gräbert GmbH`↔`Graebert`, `Gießerei Heunisch GmbH`↔`Heunisch`,
`Werner Bauser GmbH`↔`Bauser`, `Pamminger.at`↔`Pamminger Verpackungstechnik`,
`Media Focus Schweiz`↔`Mediafocus`, `Roland Dg`↔`Rolanddga`, `Ah-Se`↔`AH SE`,
`Gebrüder Jaeger GmbH`↔`Jaeger-ttc`, `Paul H. Kübler …`↔`kuebler`,
`Weidmuller`↔`Weidmueller`, `Datimo`↔`datimo (Optimo Service AG)`.

**Mehrdeutig = kein Match.** Passen zwei verschiedene Firmen gleich gut, nicht raten.

### 4. Monatswert bestimmen
Maßgeblich ist der **monatliche Vertragswert**:
- Standardvertrag (Basic/Starter/Pro/Growth/Scale) → `product_price` = Monatspreis.
- Pilot-/Prepaid-/Einmalzahlungs-Modelle → Gesamtbetrag ÷ Laufzeit in Monaten.
  (Beispiel: „Professional Pilot 4 Monate, 7.999 €" → ~2.000 €/Monat.)
  Steht die Laufzeit nur im `product_name`, dort herauslesen.
- Reine Erfolgsvergütungs-Modelle ohne festen Monatsbetrag → Setup-/Grundbetrag
  als Monatswert nehmen.
- Kein `deal_contracts`-Treffer, aber `stripe_customers.mrr > 0` und
  `subscription_status = 'active'` → `mrr` als Monatswert nehmen.

### 5. Paket zuordnen
| Monatswert | Paket Modell |
|---|---|
| ≤ 1.499 € | `🔵 Klein Paket 3 Domains` |
| 1.500 – 2.749 € | `🟡 Mittlere Paket 6 Domains` |
| ≥ 2.750 € | `🟢 Großes Paket 9 Domains` |

Kein Vertrag, kein aktives Abo, Monatswert 0 → **nichts ändern**. Steht die Zeile
noch auf leer, `⚪ Kein Paket` setzen; steht sie schon darauf, unverändert lassen.

### 6. Notion aktualisieren
`update_page` mit `command: update_properties`, `properties: {"Paket Modell": "<Option>"}`.

**Harte Regeln:**
- Nur Zeilen anfassen, die leer sind oder auf `⚪ Kein Paket` stehen.
- Ein bereits gesetztes 🔵/🟡/🟢 **niemals** überschreiben oder herabstufen – auch
  dann nicht, wenn die Vertragsdaten etwas anderes sagen. Solche Abweichungen
  gehören in den Digest, nicht ins Board.
- Gekündigte Verträge (`cancelled_at` gesetzt): Paket trotzdem setzen, wenn die
  Zeile leer war, und im Digest als „gekündigt" markieren.
- Doppelte Karten zur selben Firma: **alle** betroffenen Zeilen gleich setzen und
  die Dublette im Digest melden.

### 7. Digest
**Nur posten, wenn sich etwas geändert hat.** Ohne Änderung: still beenden, keine
Nachricht.

Bei Änderungen eine kurze Slack-DM an den User (`mg@amplifa.ai`):
- **Neu zugeordnet:** Firma → Paket (Monatswert, Produktname)
- **Weiter ohne Paket:** Anzahl + Firmen, die weiterhin keinen Vertrag haben
- **Zur Prüfung:** Namens-Mehrdeutigkeiten, Dubletten, und Fälle, in denen ein
  bestehendes Paket im Board nicht zum Vertragswert passt

Knapp und scanbar, maximal ~15 Zeilen.

## Nicht tun
- Keine Zeilen im Board anlegen oder löschen.
- Keine anderen Properties als `Paket Modell` schreiben.
- Keine Schreibzugriffe auf den Sales Hub (nur `raw_query`/SELECT).
- Keine Mails oder Nachrichten an Kunden.

## Kalibrierung (Stand 28.08.2026)
Die Preisstaffel bildet den Vertragswert ab. Einzelne Altbestände im Board wurden
nach tatsächlicher Domain-Anzahl gepflegt und weichen davon ab (z.B. IAR Group
und polysecure stehen auf 🟡 trotz Basic-Vertrag, lookthrough auf 🔵 trotz Growth).
Deshalb gilt Regel 6: bestehende Werte bleiben unangetastet, Abweichungen nur
melden.
