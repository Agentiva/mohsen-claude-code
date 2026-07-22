# ProContur – DACH Bedarfsliste

Bedarfsqualifizierte B2B-Firmenliste (DE/AT/CH) für **ProContur** (Feinblech-/Kunststoff-**Systemlieferant**, komplette Baugruppen & anschlussfertige Turnkey-Geräte aus einer Hand).

- **Playbook:** `Systemlieferant: Baugruppen & Turnkey-Geräte`
  (https://app.amplifa.ai/admin/organizations/69/playbooks/471)
- **Firmen in `procontur_dach_bedarfsliste.csv`:** **6.609** (Ziel war 5.000 – übererfüllt)
- **Spalten:** `company_name, domain, playbook_name`

## Bedarfsprofil (Zielkunde)
- **Echter Bedarf:** B2B-**Hersteller** mit eigenem Gerät/Maschine/Anlage, der **kundenspezifische Gehäuse / Baugruppen / komplette Systeme** (Blech + Kunststoff + Elektronikverbau) braucht statt Standardkomponenten.
- **Zielbranchen:** Maschinen-/Anlagenbau, Sondermaschinenbau, Elektrotechnik/Elektronik, Medizintechnik, Luft-/Raumfahrt, Wehr-/Verteidigungstechnik, Energie-/Umwelttechnik.
- **Größe:** ab ~50 Mitarbeiter. **Region:** DACH-Standort.
- **Harte Ausschlüsse:** Automotive; reine Dienstleister/Beratung/Software/Handel; reine Blech-/Kunststoff-Lohnfertiger (= Wettbewerb); Klinik/Uni/Behörde.

## Methodik
1. **Website Deep Research** – ICP/Positionierung über procontur.de + öffentliche Quellen und Meeting-Kontext (Fathom) bestätigt; Zielbranchen-Taxonomie abgeleitet. Direkte Firmen-Extraktion aus Branchenverzeichnissen (BDSV, chemie.de) war durch Bot-Schutz (HTTP 403) blockiert → planmäßiger Übergang zu Apollo für die skalierte, domain-verifizierte Discovery.
2. **Apollo.io Organization Search** – segmentiert über **DE/AT/CH**, Mitarbeiter **51+**, **Automotive ausgeschlossen** (NAICS 3361–3363). Zwei komplementäre Filterlinien:
   - **NAICS-Familien** (hohe Präzision): 332–339 (Maschinenbau, Elektronik, Elektrotechnik, Medizintechnik, Luft-/Raumfahrt, Wehrtechnik).
   - **Branchen-Keyword-Tags** (hohe Recall-Abdeckung, da NAICS EU-Firmen unvollständig taggt): *mechanical or industrial engineering, machinery, electrical/electronic manufacturing, industrial automation, medical device, defense & space, renewables & environment*.
3. **Firmographische Vorfilterung + Dedupe** – Name-/Domain-basierte Ausschlüsse (Nicht-Hersteller, Dienstleister, Automotive), Dedupe nach normalisierter Domain.

> Hinweis: Der Keyword-Tag-Ansatz maximiert die Abdeckung, lässt aber vereinzelt Nicht-Passer durch. Die **intelligente Pro-Firma-Bedarfsprüfung** erfolgt bewusst NICHT hier, sondern in **Clay** (siehe unten) – token-/kostengünstig und skalierbar.

## Nächste Schritte in Clay
1. `procontur_dach_bedarfsliste.csv` in Clay importieren (Spalten `company_name`, `domain`).
2. **`clay_qualifizierung_prompt.md`** als Claygent-/Sculptor-Spalte anwenden → pro Firma `fit_tier` (A/B/C) bestimmen. Danach `fit_tier ∈ {A, B}` behalten.
3. Auf die qualifizierten Firmen **„Find People"** mit den Titeln aus **`jobtitles_find_people.txt`** anwenden (Tier 1 = Entscheider, Tier 2 = operative Ebene/Influencer).

## Dateien
| Datei | Inhalt |
|---|---|
| `procontur_dach_bedarfsliste.csv` | 6.609 Firmen – `company_name, domain, playbook_name` |
| `clay_qualifizierung_prompt.md` | Auf ProContur zugeschnittener Clay-Bedarfs-Qualifizierungs-Prompt |
| `jobtitles_find_people.txt` | ~25 Tier-1/Tier-2 Jobtitel für „Find People" in Clay |
