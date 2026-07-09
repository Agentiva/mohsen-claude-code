# photovest – Bedarfsqualifizierte Zielfirmenliste (DE, 5.000)

Bedarfsliste für **photovest** (steueroptimiertes Photovoltaik-Investment ohne Eigenkapital).
Playbook: **Photovoltaik-Investment ohne Eigenkapital**.

## Deliverables
- `photovest_prospects.csv` – **5.000 Firmen**, Spalten: `company_name, domain, playbook_name`.
- `clay_sculptor_prompt.md` – Pro-Firma-Bedarfsprüfung (Claygent/Sculptor) in Clay.
- `find_people_jobtitles.md` – ~25 Tier-1/Tier-2-Jobtitel für "Find People" in Clay.

## Bedarfslogik
photovest verkauft an **einkommensstarke Privatpersonen mit hoher Einkommensteuerlast**
(ab ~70 T€ Jahreseinkommen, besonders ab >30 T€ Steuer/Jahr), abgebildet über ein Gewerbe.
Da Zielobjekte **Firmen** sind, ist der Bedarfsträger das inhaber-/gesellschaftergeführte,
profitable Unternehmen, hinter dem ein/e hoch besteuerte/r Eigentümer:in steht
(Personas: Unternehmer Michael, Freiberuflerin Sabine, Investor Thomas, Steueroptimierer Andreas).

## Methode
1. **Website/Deep Research** zur Validierung der Segmentgrößen (Freiberufler-Universum in DE
   allein >300.000 Einheiten → 5.000 klar tragbar).
2. **Apollo.io Organization Search** als Skalier-Engine (Deep-Research-Limit für 5.000 saubere
   Name+Domain-Paare schnell erreicht), segmentweise nach NAICS × Mitarbeiterband × Deutschland.
3. **Dedupe** nach normalisierter Domain + **firmographische Vorqualifizierung**
   (Ausschluss von AG/SE/Streubesitz, öffentlicher Hand, Kliniken/Uni, e.V./gGmbH/Stiftung,
   Genossenschaften/Banken).
4. Intelligente Pro-Firma-Prüfung bewusst **an Clay ausgelagert** (siehe Sculptor-Prompt),
   nicht token-teuer pro Website durch das Modell.

## Segment-Mix (Tier-A-gewichtet, höchste Steuerlast-Wahrscheinlichkeit)
Rechtsanwalts-Kanzleien, Steuerberater/WP, Architektur-/Ingenieurbüros, Arztpraxen,
Unternehmensberatung, Maschinenbau/Fertigung, IT-Dienstleister, Bau/Handwerk (Elektro/SHK),
Zahnarztpraxen, Großhandel, Autohäuser.
