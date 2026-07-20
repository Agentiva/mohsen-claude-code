---
name: apollo-filter-builder
description: >
  Erstellt präzise Apollo.io-Zielgruppen-Filter (Jobtitel, Industrie, Mitarbeiter, Standort,
  Keywords, Ausschluss-Keywords) für eine konkrete Firma bzw. ein Amplifa-Playbook. Nutze
  diesen Skill IMMER, wenn der User einen Apollo-Filter, Apollo.io-Filter, eine Apollo-Suche,
  einen Zielgruppen-/Lead-/ICP-Filter für Apollo, eine Apollo-Query oder Suchkriterien für
  Apollo bauen will. Trigger auch bei: "Apollo Filter für [Firma]", "bau mir den Apollo-Filter",
  "Apollo Suchkriterien", "Keywords für Apollo", "Zielgruppe in Apollo einstellen",
  "Apollo Filter aus dem Playbook", "perfekter Apollo Filter". Der Skill orientiert sich strikt
  an den COI-Referenzfiltern (coi.de): Keywords (bedarfsorientiert) enthalten AUSSCHLIESSLICH
  echte Bedarfssignale aus der Welt des Zielkunden; Ausschluss-Keywords enthalten die eigenen
  Produkt-/Markennamen und Wettbewerber. Alles wird auf die jeweilige Firma, ihr Playbook und
  den vorhandenen Kontext angepasst.
---

# Apollo.io Filter Builder

Du baust **präzise, sofort einsetzbare Apollo.io-Filter** für eine konkrete Firma bzw. deren
Amplifa-Playbook. Maßstab und Formatvorlage sind die **zwei COI-Referenzfilter** (coi.de),
siehe `references/coi-examples.md`. Übernimm deren Tabellenstruktur 1:1 — **passe aber jeden
Inhalt auf die jeweilige Firma, ihr Playbook und alle vorhandenen Informationen an.**

Die zwei COI-Beispiele sind kein Kopiervorlage-Inhalt, sondern der **Qualitäts- und
Denkstandard**. Lies sie vor jedem Build.

---

## Die zwei eisernen Regeln (das Herz dieses Skills)

### Regel 1 — Keywords (bedarfsorientiert): NUR echte Bedarfssignale

Ein Keyword ist **nur dann erlaubt**, wenn gilt: *Wenn eine Firma oder Person diesen Begriff
im Profil trägt, verrät sie damit, dass sie den Bedarf hat, den unser Kunde löst.*

Keywords beschreiben die **Welt des Zielkunden** — niemals das, was unser Auftraggeber verkauft.

**Der Käufer-oder-Anbieter-Test (bei JEDEM Keyword anwenden):**
> „Finde ich mit diesem Wort einen **KÄUFER** (jemand mit dem Problem) — oder einen
> **ANBIETER/WETTBEWERBER** (jemand, der dasselbe verkauft wie wir)?"
>
> - Käufer → **Keyword behalten**
> - Anbieter/Wettbewerber → **raus aus Keywords, rein in die Ausschluss-Liste**

Fünf Quellen für echte Bedarfssignale (aus dem Playbook ableiten):

1. **Stack / Umgebung** — Systeme, Plattformen, Materialien, Tools, die der Zielkunde einsetzt
   (COI: `SAP`, `S/4HANA`, `SAP ECC`, `ArchiveLink`; D2C-Brand: `Shopify`, `Klaviyo`).
2. **Projekte / Initiativen** — laufende Vorhaben, die den Schmerz auslösen
   (COI: `SAP migration`, `S/4HANA migration`, `system consolidation`, `SAP rollout`).
3. **Prozesse / Funktionsfelder** — der operative Bereich, in dem der Schmerz sitzt
   (COI: `Kreditorenbuchhaltung`, `invoice processing`, `Rechnungsverarbeitung`, `records management`).
4. **Regulatorik / Compliance-Treiber** — Vorgaben, die zum Handeln zwingen
   (COI: `GoBD`, `ZUGFeRD`, `XRechnung`, `E-Rechnung`, `audit`, `Aufbewahrung`, `retention`).
5. **Schmerz-Artefakte** — die konkreten problembehafteten Objekte
   (COI: `legacy data`, `Altdaten`, `master data`, `Stammdaten`, `document archiving`).

**Sonderfall — wenn der Zielkunde SELBST die Produktkategorie ist:** Verkauft der Auftraggeber
Lohn-/Auftragsfertigung oder eine Komponente in das Produkt des Kunden, gilt trotzdem Regel 1,
aber die Quelle verschiebt sich:
- **Komponenten-/Zulieferfall** (z. B. Magnete in Motoren): Keyword = **Endprodukt-Welt des
  Kunden** (`Antriebstechnik`, `Aufzugbau`, `Wärmepumpe`) — der Komponentenname (`Magnet`, `NdFeB`)
  gehört in die **Ausschluss-Liste** (findet sonst Wettbewerber).
- **Lohnfertigungs-/Category-Fall** (z. B. Private-Label-Kosmetik für Beauty-Brands): Keyword =
  **Produktwelt des Kunden** (`Naturkosmetik`, `Skincare`, `Bartöl`, `feste Kosmetik`) — die eigenen
  Leistungsbegriffe (`Lohnhersteller`, `Private-Label-Hersteller`, `CDMO`, `Auftragsfertigung`)
  gehören in die **Ausschluss-Liste**.

Immer **zweisprachig (DE + EN)** ausschreiben und **Synonyme/Varianten** ergänzen. Die
Verengung auf echte Zielkunden passiert PRIMÄR über **Industrie + Jobtitel + Seniority**, nicht
über künstlich verengte Keywords. Ziel: breite, aber saubere Trefferwolke (Faustregel
4.000–5.000 statt ~400 durch zu enge Listen).

### Regel 2 — Ausschluss-Keywords: eigene Produkte + Wettbewerber

In die Ausschluss-Liste gehören genau drei Dinge (wie bei COI: `COI, BusinessFlow, PharmaSuite,
DOCU APP, DMS-Anbieter, ECM-Anbieter, document management vendor, DMS provider, d.velop,
DocuWare, ELO, enaio, M-Files, windream, Doxis, SER, agorum, Amagno, docuvita, OpenText`):

1. **Eigene Marken- und Produktnamen** des Auftraggebers (COI, BusinessFlow, PharmaSuite …).
2. **Eigene Kategorie-Anbieterbegriffe** — die „[Kategorie]-Anbieter / -vendor / -provider"-Wörter,
   die die **Angebotsseite** des eigenen Markts finden (`DMS-Anbieter`, `document management vendor`,
   `DMS provider`, `ECM-Anbieter`).
3. **Direkte Wettbewerber** namentlich (d.velop, DocuWare, ELO, enaio, M-Files …).

Zweck: Wettbewerber, Reseller und die gesamte **Angebotsseite des eigenen Markts** herausfiltern,
sodass nur **echte Käufer** übrig bleiben. Alles, was den Käufer-oder-Anbieter-Test als „Anbieter"
besteht, landet hier.

---

## Ablauf

1. **Kontext & Playbook laden.** Nutze vorhandenen Chat-Kontext. Liegt ein Amplifa-Playbook vor,
   lies es über die Amplifa-MCP (`playbook_read` mit exaktem `organization_name`) — daraus kommen
   Produkt, Value Proposition, Personae/Pains, Use Cases und Proof Points. Fehlt ein Playbook,
   nutze Website + gelieferte Materialien. Fehlende Angaben kurz benennen statt erfinden.

2. **Auftraggeber-Typ bestimmen** (entscheidet die Keyword-Quelle, siehe Regel 1 Sonderfall):
   Software/Lösung · Komponente/Zulieferer · Lohnfertigung/Category · Dienstleistung.

3. **ICPs/Personae übernehmen.** Pro ICP ein eigener Filter (wie COI: „ICP 5", „ICP 6" …).
   Jobtitel = das Buying Center des ICP aus dem Playbook.

4. **Keywords (bedarfsorientiert) ableiten** — pro ICP entlang der fünf Bedarfsquellen,
   DE + EN, jeden Begriff durch den Käufer-oder-Anbieter-Test schicken.

5. **Ausschluss-Keywords bauen** — eigene Produkte + Kategorie-Anbieterbegriffe + Wettbewerber.
   (Wettbewerber ggf. via kurzer Recherche/`competitor-finder` ergänzen.)

6. **Firmografie setzen** — Industrie (breit), Mitarbeiter (mit Sweet Spot), Standort, Seniority.

7. **Ausgeben** im COI-Tabellenformat (siehe unten), pro ICP eine Tabelle.

---

## Firmografie-Zeilen (Defaults & Anpassung)

- **Jobtitel** — alle relevanten Rollen des Buying Centers, DE + EN. **Standard: kein C-Level**
  (COI schreibt „(jeweils nicht C-Level)"). **Ausnahme:** Ist die/der Entscheider:in laut ICP
  die/der Inhaber:in/Gründer:in (sehr kleine Zielfirmen, z. B. 1–25 MA D2C-Brands), dann
  Founder/Owner **bewusst einschließen** und das explizit vermerken.
- **Industrie** — breit fassen (Apollo-Industry-Tags), lieber mehrere verwandte Branchen als eine
  enge. Die Präzision kommt aus Keywords + Titel.
- **Mitarbeiter** — Range **mit Sweet Spot** angeben (COI: „200–500.000 (Sweet Spot 500–100.000)").
- **Standort** — Default DACH: `Germany, Austria, Switzerland`. Bei EU-/Global-Strang zusätzliche
  Länder ausweisen.
- **Seniority** — `manager, senior, director, head, lead, vp` (Default **nicht** `c_suite, owner,
  founder, partner`; bei der Founder-Ausnahme oben aber `owner, founder, c_suite` ergänzen).
- **Kontakte pro Firma** — Hinweis mitgeben: bewusst nur **3–5 Entscheider** pro Zielfirma;
  Firmenauswahl schlägt Kontaktmenge.

---

## Apollo-Feld-Mapping (zum 1:1-Einstellen)

| Tabellenzeile | Apollo-Feld (UI / API) |
|---|---|
| Jobtitel | Person Titles (`person_titles`) |
| Industrie | Industry (`organization_industries`) |
| Mitarbeiter | # Employees (`organization_num_employees_ranges`) |
| Standort | Company / Person Location (`organization_locations` / `person_locations`) |
| Seniority | Management Level (`person_seniorities`) |
| Keywords (bedarfsorientiert) | Company Keywords (`q_organization_keyword_tags`) |
| Ausschluss-Keywords | Excluded Company Keywords (`q_not_organization_keyword_tags`) |

Optionale Präzisierung als eigene, kleinere Runs: **Technographics** (z. B. `Shopify`),
**Job Postings**, **Latest Funding**, **Company Founded** als Timing-Trigger.

---

## Ausgabeformat (COI-Struktur, pro ICP eine Tabelle)

Default = saubere Markdown-Tabelle im Chat. Auf Wunsch als styled Navy-Header-Tabelle
(HTML/docx im amplifa-Stil) rendern.

```
### Filter für ICP <N>: <ICP-/Persona-Name>

| Kriterium | Werte |
|---|---|
| **Jobtitel** | <DE/EN-Titel des Buying Centers> (jeweils nicht C-Level) |
| **Industrie** | <breite Apollo-Industry-Tags, komma-separiert> |
| **Mitarbeiter** | <Range> (Sweet Spot <Range>) |
| **Standort** | Germany, Austria, Switzerland |
| **Keywords (bedarfsorientiert)** | <nur Bedarfssignale, DE + EN, komma-separiert> |
| **Ausschluss-Keywords** | <eigene Produkte, Kategorie-Anbieter, Wettbewerber> |
```

---

## Qualitäts-Checkliste (vor der Ausgabe abhaken)

- [ ] Zwei COI-Beispiele (`references/coi-examples.md`) als Maßstab gelesen
- [ ] Playbook/Website gelesen, Auftraggeber-Typ bestimmt
- [ ] **Jedes** Keyword hat den Käufer-oder-Anbieter-Test bestanden (kein Anbieterbegriff in den Keywords)
- [ ] Keywords entlang der 5 Bedarfsquellen, **DE + EN**, mit Synonymen — breit genug
- [ ] Ausschluss-Liste = eigene Produkt-/Markennamen **+** Kategorie-Anbieterbegriffe **+** Wettbewerber
- [ ] Jobtitel = Buying Center; C-Level-Regel bewusst gesetzt (Standard raus / Founder-Ausnahme dokumentiert)
- [ ] Industrie breit, Mitarbeiter mit Sweet Spot, Standort, Seniority gesetzt
- [ ] Pro ICP eine eigene Tabelle im COI-Format
- [ ] Hinweis „3–5 Entscheider pro Firma" ergänzt
- [ ] Compliance-Kurzhinweis (DACH: UWG §7 / DSGVO, nur geschäftliche Adressen, Opt-out) bei Bedarf

---

## Bezug zu anderen Skills

- **Input**: `icp-playbook-org` / `icp-playbook-generator` liefern das Playbook; `persona-definer`,
  `icp-definer`, `pain-identifier` liefern ICP/Personae/Pains.
- **Wettbewerber**: `competitor-finder` liefert Namen für die Ausschluss-Liste.
- **Danach**: `prospect-list` / `people-finder` / `bedarfsliste` für den eigentlichen Listenbau.
Dieser Skill ist die **Apollo-spezifische Filterlogik** und ergänzt die allgemeine
`apollo-keyword-logic` aus dem Playbook-Skill um den COI-Bedarfssignal- und Ausschluss-Standard.
