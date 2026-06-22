---
name: prospect-list
description: Baut B2B-Prospect-Listen als CSV für amplifa-Kampagnen, orchestriert über Clay und Apollo. IMMER nutzen, wenn der User eine Prospect-Liste, Lead-Liste, Zielfirmen-/Kontaktliste, ein ICP-Segment oder einen CSV-Export von Firmen/Kontakten braucht. Liefert ein standardisiertes Spaltenformat.
argument-hint: [ICP-beschreibung: branche, größe, region, titel]
allowed-tools: Bash(*)
---

# Prospect-List-Builder (amplifa)

Erzeugt saubere, deduplizierte Prospect-Listen für DACH-Outbound. Nutzt die verbundenen Clay-/Apollo-Connectoren zur Anreicherung.

## Ablauf

1. **ICP fixieren:** Branche/Sektor, Firmengröße (MA/Umsatz), Region, Ziel-Titel, Ausschlüsse. Lücken kurz erfragen statt raten.
2. **Firmen finden** (Apollo/Clay) nach ICP. Region und Branche strikt anwenden.
3. **Kontakte finden** je Firma nach Ziel-Titeln; pro Firma sinnvolle Anzahl (Buying Center, nicht das ganze Org-Chart).
4. **Anreichern** (E-Mail etc.) nur, wenn ausdrücklich gewünscht – Enrichments kosten Credits.
5. **Dedupe:** Doppelte Firmen und Kontakte entfernen (Domain bzw. E-Mail als Schlüssel).
6. **Export** als CSV im Standardformat (unten).

## Standard-Spaltenformat

`first_name,last_name,title,company,domain,linkedin_url,location,language,email,signal`

- `language` per Region ableiten (DE/EN/FR/IT) – konsistent mit dem Sprach-Routing der Cold-Email-Logik.
- `signal` = Buying-Signal/Trigger, falls vorhanden (sonst leer).
- `email` nur befüllen, wenn Enrichment gewünscht war.

## Qualitätsregeln

- Region/Branche hart filtern; keine ICP-fremden Firmen "zur Auffüllung".
- Keine erfundenen E-Mails oder Titel. Unbekannt = leer lassen.
- Bei 0 Treffern Filter schrittweise lockern (Titel breiter, dann Region, dann Größe) und das transparent machen.
- Französische/italienische Kontakte korrekt mit `language` FR/IT markieren, damit keine DE-Ansprache passiert.
