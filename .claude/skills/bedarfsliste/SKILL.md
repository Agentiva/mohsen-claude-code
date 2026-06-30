---
name: bedarfsliste
description: Baut bedarfsqualifizierte B2B-Firmenlisten (Unternehmensname + Domain) als CSV für ein bestimmtes Kundenprodukt und Zielland. IMMER nutzen, wenn der User sagt "such mir X Unternehmen in Land Y für das Produkt von Z", eine Firmenliste/Zielfirmenliste/Bedarfsliste braucht, oder "finde mehr / finde 1000 mehr" zu einer laufenden Liste sagt. Recherchiert IMMER zuerst das Kundenprodukt, leitet daraus den echten Bedarf ab, entfernt günstig die offensichtlichen Nicht-Passer und liefert IMMER vier Artefakte: (1) saubere CSV mit Name+Domain, (2) einen fertigen Clay-Sculptor-/Claygent-Qualifizierungs-Prompt für die Pro-Firma-Bedarfsprüfung in Clay, (3) ~25 komma-separierte Tier-1/Tier-2-Jobtitel für "Find People" in Clay, (4) eine Apollo-ICP-Filter-Tabelle (Jobtitel/Industrie/Mitarbeiter/Standort/Seniority/Keywords) je ICP.
argument-hint: [kunde/produkt + anzahl + zielland]
allowed-tools: Bash(python3 *)
---

# Bedarfsliste-Generator (amplifa)

Erzeugt eine saubere CSV mit **Unternehmensname + Domain** – aber nur von Firmen, die einen **echten, nachvollziehbaren Bedarf** für das Produkt des Kunden haben. Skalierbar in die Tausende, iterativ nachladbar.

Default-Aufruf: „Such mir für das Produkt von {Kunde} {Anzahl} Unternehmen in {Land}." Mehr ist nicht nötig.

## Schritt 1 – Produkt-/Bedarfsanalyse (IMMER zuerst, nie überspringen)

Bevor irgendeine Firma gesucht wird:

1. Das Kundenprodukt recherchieren (Web + Kundendomain): Was wird verkauft, welches Problem löst es, für wen.
2. Daraus das **Bedarfsprofil** ableiten – das ist das Qualifizierungskriterium für „echter Bedarf":
   - Welche Branchen/Sub-Sektoren haben dieses Problem konkret?
   - Welche Firmengröße/Reife passt (zu klein = kein Budget, zu groß = anderer Beschaffungsweg)?
   - Welche beobachtbaren Merkmale/Signale deuten auf Bedarf (Maschinenpark, Prozesse, Tech, Wachstum, Regulatorik)?
   - Harte Ausschlusskriterien (wer hat definitiv keinen Bedarf).
3. Das Bedarfsprofil kurz festhalten und dem User zeigen, bevor in die Masse gegangen wird. So ist die Liste am Ende wirklich passgenau und nicht nur „Firmen im Land".

Format und Beispiele des Bedarfsprofils: siehe `reference.md`.

## Schritt 2 – Suchstrategie ableiten

Das Bedarfsprofil in konkrete Suchfilter übersetzen. Da „Bedarf" selten ein einzelner Filter ist, in **mehrere Teilsuchen zerlegen** (pro Branche/Sub-Sektor × Größenband × Region), um den Markt abzudecken statt nur die offensichtlichsten Treffer. Zielland strikt anwenden.

## Schritt 3 – Discovery (iterativ, bis Zielzahl erreicht)

1. Über den **Apollo**-Connector (Organization Search) bzw. **Clay** Firmen nach den Filtern ziehen.
2. **Paginieren und über die Teilsuchen iterieren**, bis die gewünschte Anzahl erreicht ist. Große Zielzahlen (z. B. 2000) in Batches sammeln.
3. Jeden Batch sofort in eine Arbeits-CSV schreiben.
4. Nach jedem Batch dedupen (Skript, Schritt 5).

Mapping-Hinweise zu Apollo/Clay-Filtern: `reference.md`.

## Schritt 4 – Günstige Firmographie-Vorqualifizierung (KEIN Pro-Firma-Webscan durch Claude)

Ziel: die offensichtlichen Nicht-Passer **billig** rauswerfen, ohne pro Firma die Website zu lesen (das frisst Tokens und lohnt nicht). Nur mit den Daten, die die Discovery schon liefert:

- **NAICS/Branche-Fit:** Jede Firma auf 3-stelligen NAICS-Fit mappen. Physische Palettenware (Herstellung/Handel mit eigenem Versand) = behalten; Branchen ohne Palettenfluss (Info/IT, Finanz/Versicherung, Beratung, Personentransport/Post/Bahn, Retail-Filialen, Gesundheit/Bildung) = raus.
- **Namens-/Domain-Ausschluss:** Klare Nicht-Passer per Keyword entfernen (consulting, beratung, software, agentur, versicherung, immobilien, kanzlei, hotel, e.V./Verein, Uni/Hochschule/Klinik …).
- **Größe/Land:** Größenband und Zielland hart anwenden.

→ Ergebnis: ein firmographisch sauberer Pool. **Die intelligente Pro-Firma-Bedarfsprüfung wird NICHT von Claude per Website gemacht, sondern an Clay übergeben** (Schritt 5b). So bleibt es token-günstig und skaliert in die Tausende.

## Schritt 5a – Dedupe & CSV-Output

```bash
python3 ${CLAUDE_SKILL_DIR}/scripts/merge_dedupe.py master.csv neuer_batch.csv > liste.csv
```

- Dedupe nach normalisierter Domain (www./Schema/Pfad egal).
- **Output-CSV: genau zwei Spalten – `company_name,domain`.** Nichts weiter, sofern nicht ausdrücklich mehr gewünscht.
- Das Skript meldet Gesamtzahl + wie viele neu sind.

## Schritt 5b – Clay-Sculptor-Qualifizierungs-Prompt (IMMER mitliefern)

Zusätzlich zur CSV **immer** einen fertigen Claygent-/Sculptor-Prompt ausgeben, mit dem der User in Clay jede Firma der Liste auf echten Bedarf prüft (das ist die teure, intelligente Stufe – sie läuft in Clays Credits, nicht in Claudes Tokens). Den Prompt **auf das konkrete Kundenprodukt zuschneiden** (Vorlage: `clay_sculptor_prompt.md`):

- Inputs: `{{company_name}}`, `{{domain}}`.
- Produktbeschreibung + Definition „echter Bedarf" + harte C-Ausschlüsse aus dem Bedarfsprofil (Schritt 1) einsetzen.
- Vorgehen: Website besuchen, Bedarfssignale prüfen.
- Strukturierter JSON-Output: `fit_tier` (A/B/C), `ships_pallets`/Kernfrage (yes/no/unclear), `key_signal`, `reason`.
- Hinweis an den User: in Clay nach `fit_tier` ∈ {A,B} filtern, dann exportieren.

Die Vorlage steht in `clay_sculptor_prompt.md` – Platzhalter durch das jeweilige Kundenprodukt ersetzen.

## Schritt 5c – Jobtitel für „Find People" in Clay (IMMER mitliefern)

Zusätzlich zur CSV und zum Sculptor-Prompt **immer** eine Liste von **genau ~25 Jobtiteln, komma-separiert in EINER Zeile** ausgeben, mit der der User in Clay „Find People / Find Contacts" auf die qualifizierten Firmen anwendet. Die Titel **auf das konkrete Kundenprodukt / die Buying-Center-Persona zuschneiden** (aus dem Bedarfsprofil, Schritt 1):

- **Tier 1 (Entscheider / Economic Buyer):** die Rollen, die das Produkt budgetieren/freigeben (z. B. bei einer Spedition: Leiter Logistik, Head of Supply Chain, Geschäftsführer, Werkleiter).
- **Tier 2 (Nutzer / Influencer / operative Ebene):** die Rollen, die operativ damit arbeiten oder den Bedarf melden (z. B. Versandleiter, Disponent, Einkauf Logistikdienstleistungen, Lagerleiter).
- Beide Tiers in **derselben Zeile** mischen, deutsche UND gängige englische Varianten aufnehmen (Clay matcht über Titel-Strings), Singular-Form bevorzugen.
- Format: eine einzige komma-separierte Zeile, copy-paste-fertig für das Clay-Titelfeld. Keine Nummerierung, keine Erklärtexte in der Zeile.
- Kurz dazuschreiben, welche Titel Tier 1 vs. Tier 2 sind (außerhalb der copy-paste-Zeile), damit der User in Clay ggf. priorisieren kann.

## Schritt 5d – Apollo-ICP-Filter-Tabelle (IMMER mitliefern)

Zusätzlich **immer** pro ICP/Zielsegment (bei mehreren Playbooks: je eine Tabelle) eine **Apollo-ready ICP-Filter-Tabelle** im exakt folgenden Markdown-Format ausgeben. Sie übersetzt das Bedarfsprofil (Schritt 1) 1:1 in Apollo-Filterfelder, sodass der User sie direkt in Apollo „Companies/People → Filters" setzen kann. Werte in **Apollo-Schreibweise** (Industrie in Apollos kleingeschriebener Taxonomie, Seniority als Apollo-Tokens), nicht erfinden.

Format (genau diese Zeilen, in dieser Reihenfolge):

```
## ICP <N> — <Segmentname>

| Kriterium | Werte |
|---|---|
| **Jobtitel** | <~20–25 reale Jobtitel, DE+EN gemischt, Tier 1 zuerst, komma-separiert> |
| **Industrie** | <Apollo-Industrien, kleingeschrieben, komma-separiert – z. B. real estate, financial services, …> |
| **Mitarbeiter** | <Größenband, z. B. 50–5.000 (Sweet Spot 50–1.000)> |
| **Standort** | <Zielland/-länder; ggf. (Ausschluss: …)> |
| **Seniority** | <Apollo-Seniority-Tokens: head, director, manager, senior, lead, owner, partner, c_suite> |
| **Keywords (bedarfsorientiert)** | <bedarfstreibende Begriffe/Signale aus Schritt 1, DE+EN, inkl. relevanter Normen/Hersteller/Verfahren> |

> **Tier 1:** <Entscheider-Titel> · **Tier 2:** <Nutzer-/Influencer-Titel>
```

Regeln:
- **Jobtitel** = dieselbe Buying-Center-Logik wie Schritt 5c (Tier 1 Entscheider zuerst, dann Tier 2), nur hier als Tabellenzeile.
- **Industrie** = Apollo-Branchen-Strings (kleingeschrieben, wie Apollo sie führt: `real estate`, `financial services`, `machinery`, `automotive`, `mechanical or industrial engineering`, `renewables & environment`, …). Passend zum NAICS-Fit aus Schritt 4.
- **Mitarbeiter/Standort** strikt aus dem Bedarfsprofil; Standort = Zielland (plus erlaubte Nachbarländer, falls im Auftrag), Ausschlüsse explizit.
- **Seniority** nur aus den gültigen Apollo-Tokens.
- **Keywords (bedarfsorientiert)** = die echten Bedarfssignale (Verfahren, Maschinen/Hersteller, Normen, Produktbegriffe) – DE und EN, weil Apollo über Strings matcht.
- Wenn `reference.md` ein erweitertes Mapping enthält, daran halten.

## „Finde mehr" / „Finde 1000 mehr"

Die bestehende `liste.csv` ist der master. Neue Treffer (weitere Teilsuchen / nächste Seiten, bereits gefundene Domains ausgeschlossen) als neuen Batch sammeln und mit dem Skript draufmergen:

```bash
python3 ${CLAUDE_SKILL_DIR}/scripts/merge_dedupe.py liste.csv batch2.csv > liste.csv
```

So wächst die Liste dublettenfrei weiter, ohne dass schon gefundene Firmen erneut auftauchen.

## Qualitätsregeln (eisern)

- **Erst Produkt verstehen, dann suchen.** Nie Schritt 1 überspringen.
- Nur Firmen mit nachvollziehbarem Bedarf – keine Auffüllung mit irrelevanten Firmen, nur um die Zahl zu treffen.
- Zielland/Region hart anwenden.
- Keine erfundenen Firmen oder Domains. Domain unbekannt → Firma raus oder Domain verifizieren, nie raten.
- Wenn die Zielzahl an passenden Firmen realistisch nicht erreichbar ist, das **ehrlich melden** (z. B. „im Markt sind ~1300 passende Firmen") statt mit Schrott aufzufüllen.
- Endausgabe immer durch das Dedup-Skript schicken.
- **Niemals pro Firma die Website durch Claude lesen lassen, um zu qualifizieren** – das ist token-teuer und skaliert nicht. Claude macht nur die günstige Firmographie-Filterung; die intelligente Pro-Firma-Bedarfsprüfung läuft über den Clay-Sculptor-Prompt in Clay.
- **Immer alle vier Artefakte liefern:** (1) `liste.csv` (Name+Domain), (2) den auf das Kundenprodukt zugeschnittenen Clay-Sculptor-Prompt, (3) die ~25 komma-separierten Tier-1/Tier-2-Jobtitel für „Find People" in Clay (Schritt 5c), (4) die Apollo-ICP-Filter-Tabelle je ICP (Schritt 5d).
