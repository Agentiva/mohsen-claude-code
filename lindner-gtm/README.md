# Lindner – Bedarfsqualifizierte Zielfirmenlisten (4 Playbooks)

Kunde: **Lindner** (https://www.lindner.com/de/) – österreichischer Hersteller von Industrieschreddern und schlüsselfertigen Zerkleinerungs-/Sortieranlagen für Abfall, RDF/EBS und Holz.

Auftrag: pro Playbook Richtung 2.000 bedarfsstarke Firmen aus 27 Ländern (DACH, Nordics, Baltikum, CEE, Balkan). Erst Website-Deep-Research, dann Apollo. Output: CSV mit **company name, company domain, playbook name**.

## Ergebnis (nach Dedupe + Ausschlussprüfung)

| Playbook | Firmen | Ziel 2.000? |
|---|---:|---|
| Private Recyclers & Reprocessors | **1.995** | ✅ erreicht (aus >2.400 qualifizierten gecappt) |
| Wood & Biomass Recyclers | **1.997** | ✅ erreicht |
| Municipal & Public Waste Operators | **619** | ⚠️ realistische Marktobergrenze (s. u.) |
| Cement, Energy & RDF Off-takers | **219** | ⚠️ bewusst eng gehalten (s. u.) |
| **Kombiniert (playbook-getaggt)** | **4.830 Zeilen / 4.493 Unternehmen** | |

## Dateien
- `lindner_target_companies.csv` — **Hauptdeliverable**: `company_name, domain, playbook` (alle 4 Playbooks).
- `clean/pbXXX_*.csv` — je Playbook eine saubere Liste `company_name, domain` (Import-fertig).
- `clay_assets.md` — pro Playbook: Clay-Sculptor-Qualifizierungsprompt + „Find People"-Jobtitel-Zeile.
- `raw/pbXXX_*.csv` — Rohoutput der 4 Discovery-Agenten (vor finalem Dedupe/Ausschluss).
- `review/excluded.csv` — jede entfernte Zeile inkl. Grund (nichts wird still gedroppt).
- `assemble.py` — Dedupe-, Ausschluss- und Tagging-Pipeline (reproduzierbar).

## Methode
1. **Website-Deep-Research** (WebSearch) für benannte, verifizierte Firmen aus Verbands-/Mitglieder-/Messelisten.
2. **Apollo Organization Search** zum Skalieren: Segmentierung nach Branche/Keyword × NAICS × Land × Größenband, paginiert.
3. **Firmographische Vorqualifizierung** (günstig, ohne Pro-Firma-Webscan): NAICS/Branche-Fit, Namens-/Domain-Ausschluss, Land/Größe.
4. **Finaler Ausschlusspass** (`assemble.py`): Wettbewerber (Maschinenbauer wie UNTHA, Vecoplan, Komptech, Doppstadt, Weima …), generische Nicht-Passer (Beratung, Software, Agentur, Versicherung, Immobilien, Recruiting, Mobilität …), Referenz-Exemplare (REMONDIS, Veolia, FCC, Holcim, Heidelberg, Cemex, Saubermacher, LINZ AG …), Dedupe je Playbook.
5. **Intelligente Pro-Firma-Bedarfsprüfung → Clay** (nicht Claude): mit den Sculptor-Prompts in `clay_assets.md`; danach `fit_tier ∈ {A,B}` filtern und exportieren.

## Verifizierungs-Pass (Konkurrenz / Zulieferer / Nicht-Betreiber entfernt)

Auf ausdrücklichen Wunsch geprüft: Sind die Firmen echte potenzielle **Käufer** – und keine **Wettbewerber** oder Firmen, die **an Lindner verkaufen** wollen? Script: `verify_screen.py`. Ergebnis:

| Playbook | vorher | verifiziert | entfernt |
|---|---:|---:|---:|
| Private Recyclers & Reprocessors | 1.995 | **1.973** | 22 |
| Wood & Biomass Recyclers | 1.997 | **1.844** | 153 |
| Municipal & Public Waste Operators | 619 | **540** | 79 |
| Cement, Energy & RDF Off-takers | 219 | **219** | 0 |
| **Gesamt** | 4.830 | **4.576** | 254 |

Entfernt (alle nachvollziehbar in `review/flagged_suspects.csv`): **38 Zulieferer** (Maschinenbau/Anlagenbau/Engineering/Ingenieurbüros, Hydraulik/Antriebe/Fördertechnik, Stahl-/Metallbau, Kran-/Wägetechnik – z. B. Ledinek, Springer Maschinenfabrik, Wessel-Hydraulik, KÜHNEZUG), **3 Wettbewerber** (Forsttechnik-Hersteller Uniforest u. a.), **95 Nicht-Betreiber** (v. a. Fach-/Zweckverbände ohne Abfallbezug wie KiTa-, ÖPNV-, Wasser-, VHS-, IT-Zweckverbände, dazu Verbände/Institute/Akademien/Verlage/Beratungen) und **118 Falsch-Segment im Wood-Playbook** (Holz-VERWENDER statt -Zerkleinerer: Fenster-, Türen-, Parkett-/Bodenbelag-, Möbelhersteller, Holzbau/Zimmerei, Holzhändler). Fehl-Flags wurden korrigiert (echte Abfall-Zweckverbände wie Müllverwertung Schwandorf, KVA Thurgau blieben drin).

### Stichproben-Audit (WebSearch, 45 Firmen, risikogewichtet)
Echte-Käufer-Quote im Sample **≈ 67 %** vor dem Wood-Falsch-Segment-Filter; danach deutlich höher. Nach Playbook: **Cement/Energy/RDF ~93 %** (stärkstes), **Municipal ~78 %**, **Private ~60 %**, **Wood ~33 %** (schwächstes → daher der zusätzliche Falsch-Segment-Filter, der 118 Holz-Endprodukt-Hersteller entfernt hat). Reststreuung (z. B. reine Händler, Grenzfälle) wird final vom Clay-Sculptor-Pass gefiltert.

**Verifizierte Hauptdatei:** `lindner_target_companies_verified.csv` · verifizierte Einzellisten unter `verified/`.

> Hinweis: Der Screen entfernt Konkurrenz/Zulieferer/Nicht-Betreiber deterministisch über Name+Domain (kein Website-Besuch, da WebFetch geblockt). Die **positive Pro-Firma-Bedarfsbestätigung** (betreibt die Firma wirklich eine Zerkleinerung / verbrennt RDF / verarbeitet Altholz) ist der Clay-Sculptor-Schritt in `clay_assets.md`. Ein Rest-Long-Tail an Falsch-Segment-Treffern (z. B. Fensterbauer in Wood) bleibt möglich und wird dort final gefiltert.

## Ehrliche Einordnung / Caveats
- **WebFetch war umgebungsseitig geblockt (403 auf allen Hosts)** – Verbands-Mitgliederverzeichnisse (Avfall Sverige/Norge, Dansk Affaldsforening, KIVO, Schweizer KVA, österreichische Abfallverbände, EPF, ENplus, bvse) konnten NICHT gescraped werden. Skalierung lief daher überwiegend über Apollo mit landessprachlicher Keyword-Segmentierung; WebSearch nur zur Orientierung.
- **Municipal (619):** öffentlich/kommunale MSW-Betreiber mit eigener, in Apollo auffindbarer Domain sind ein endlicher Satz (~600–800, Deutschland-dominiert). Über ~620 hinaus hieße mit privaten Fuhrunternehmen/bloßen Gemeinden auffüllen – das vermeidet das Playbook bewusst. **Upside:** der geblockte Verzeichnis-Kanal (Abfallverbände AT ~50–80, KVA CH ~30, KIVO FI ~30, volle Nordic-Mitgliederlisten) könnte in einer nicht geblockten Umgebung einige Hundert ergänzen.
- **Cement/Energy/RDF (219):** bewusst eng („eng halten"). Da die Exemplar-Majors (Holcim, Heidelberg, CRH, Cemex) per Definition ausgeschlossen sind und diese einen Großteil der regionalen Zement-/Kalköfen betreiben, ist das adressierbare Nicht-Exemplar-Universum klein (~220–260). Kern: ~60 hochsichere Zement-/Kalk-/Energie-Abnehmer; der Rest sind WtE-/RDF-fähige (oft kommunale) Betreiber, die der Clay-Sculptor-Gate final qualifiziert.
- **Long-Tail:** In den Keyword/NAICS-gebauten Listen bleibt ein kleiner Rand marginaler Treffer (z. B. Fenster-/Möbelhersteller in Wood, reine Sammelbetriebe in Cement). Genau dafür ist der Clay-Sculptor-Pass gedacht – die zweistufige Logik (günstige Firmographie durch Claude, intelligente Bedarfsprüfung durch Clay).
- **Überschneidung:** 279 Domains (~6 %) erscheinen in >1 Playbook – reale Mehrfachbedarfe (z. B. kommunale Abfallwirtschaft mit MVA = Municipal + RDF-Off-taker + Gewerbeabfall). Beim Import je Playbook über die Blacklist/Dedupe der Plattform handhaben.
