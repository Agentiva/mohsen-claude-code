# ProContur – Firmenlisten für Playbook 471, 616 & 617

Bedarfsorientierte Firmenlisten für die drei ProContur-Playbooks (Amplifa Org 69) in **einer** CSV.
Erstellt am 16.10.2026.

| Datei | Inhalt |
|---|---|
| `procontur_playbook_companies.csv` | **Ergebnis:** `Company Name, Company Domain, Playbook Name`, je Playbook nach Bedarfs-Rang sortiert (beste zuerst) |
| `procontur_playbook_companies_audit.csv` | Gleiche Firmen plus `playbook_id`, `rank_score`, `country`, `sources` zur Nachvollziehbarkeit |

Clay-Prompts, Job Titles und Apollo-Filter je Playbook stehen in Notion:
**ProContur – Clay Sculptor Prompts, Job Titles & Apollo Filter (Playbook 471, 616 & 617)** (unter „Mohsen - Kampagne").

## Ergebnis

| Playbook | Firmen | Länder | Hinweis |
|---|---|---|---|
| 471 Systemlieferant: Baugruppen & Turnkey-Geräte | **1.977** | DE 1.306 · AT 156 · CH 276 · .com ohne Länderzuordnung 239 | 23 unter Ziel: der Markt ist durch frühere Kampagnen bereits stark bearbeitet (1.424 Treffer waren schon Org-69-Leads) |
| 616 Turnkey Systems (BENELUX) | **1.347** | NL · BE · LU | Marktgrenze: Apollo und Prospeo zusammen liefern für das ICP (OEMs mit eigenem Produkt, 51–1.000 MA) nicht mehr passende Firmen; nicht mit Off-ICP-Firmen aufgefüllt |
| 617 Fertigungs- und Systempartner für Entwicklungs- und Konstruktionsbüros | **2.000** | DE 1.568 · AT/CH 430 | Die letzten 698 Zeilen sind Büros, die Apollo mit 1–10 MA führt (unter dem 11–200-Schwerpunkt) – erst nach den 1.302 Kernbüros nutzen |

**Summe: 5.324 Firmen**, keine Firma in zwei Playbooks, keine Dubletten.

## Vorgehen

1. **Website Deep Research (zuerst):** Mitglieder- und Ausstellerverzeichnisse (u. a. SPECTARIS, BDLI, Precision Fair, Design-Agentur-Listen). 104 Firmen mit belegter Domain; viele Verzeichnisse waren gesperrt (403, nur per JavaScript) → Grenze der Web-Recherche erreicht. Web-Funde erhalten den höchsten Rang.
2. **Apollo.io:** kostenlose Organisations-Suche (0 Credits, 400 Aufrufe/Stunde) mit bedarfsorientierten Keyword- und NAICS-Segmenten je Playbook; ergänzend die bezahlte Suche (69 Credits), bis das Team-Export-Kontingent erschöpft war (Reset 21.10.2026).
3. **Prospeo** (nach Erreichen des Apollo-Limits): Branchen- und Keyword-Segmente mit Firmenbeschreibung, 380 Credits.
4. **Triage:** offensichtliche Nicht-Passer je Playbook entfernt (Wettbewerb/Lohnfertiger/EMS, Handel, Software, Beratung, Bau/TGA, Pharma/Food, Hochschulen/Verbände, Vertriebsniederlassungen ausländischer Marken, Automotive u. a.) – bei Prospeo auf Basis der Firmenbeschreibung, sonst nach Name/Domain. Unklare Fälle bleiben drin; die eigentliche Bedarfsprüfung erfolgt per Clay-Prompt.
5. **Ausschlüsse:** alle 15.124 bereits importierten Leads von Org 69 (4.315 E-Mail-Domains + 3.815 Firmennamen) sowie die Domain-Blacklist (Notion-Blacklist, Blacklist-Ergänzung vom 13.10., pausierte Firmen Gerresheimer, Hitachi Energy, Miba, ProContur selbst).
6. **Ranking:** Treffer in mehreren unabhängigen Bedarfssegmenten und Quellen, Web-Fund, bedarfsnahe Keywords stärker als breite Branchen-Tags, DE vor AT vor CH (Schweiz-Pause bis KW46).

## Wichtige Hinweise

- **Schweiz:** Laut Status-Check vom 14.10. bis KW46 keine neuen CH-Importe. 471 enthält 276 CH-Firmen, 617 enthält 96 – erst nach Freigabe importieren.
- **Blacklist:** Die Original-Blacklist aus dem Onboarding (183 Einträge) war nur noch zu 50 Einträgen lesbar (Download-Link abgelaufen). Die restlichen sind sehr wahrscheinlich über die Org-69-Leads abgedeckt, sollten aber neu exportiert und gegengeprüft werden.
- **Qualität:** Die Liste ist vorqualifiziert, nicht endqualifiziert. Vor dem Import den Clay-Prompt des jeweiligen Playbooks laufen lassen und nur `Yes` (optional `Maybe`) übernehmen.
