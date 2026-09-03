# photovest – Bedarfsqualifizierte Zielfirmenliste (DE) · net-new

Bedarfsliste für **photovest** (steueroptimiertes Photovoltaik-Investment ohne Eigenkapital).
Amplifa Org 60 · Playbook 321 „Photovoltaik-Investment ohne Eigenkapital".

## Finale Deliverables
- `photovest_prospects_final.csv` – **5.000 net-new Firmen**, Spalten:
  `company_name, company_domain, playbook_name`.
- Notion: **photovest – Clay Sculptor Prompt & Job Titles (Playbook 321)**
  (Score 0–10 + Qualified Yes/Maybe/No + reason + source_url) unter „photovest GmbH".

## Ausschluss (wichtig)
Alle Firmen aus den 4 hochgeladenen Kontaktlisten (CEOs Germany SMBs, Manufacturing
Leadership Germany, Finance & Management Executives Germany, Geschäftsführer –
zusammen 13.435 unique Domains) wurden **hart entfernt**. Overlap der finalen CSV mit
diesen Listen = **0**. Zusätzlich sind alle bereits in der ersten 5.000er-Liste
enthaltenen Domains als „schon vorhanden" behandelt, sodass die Topup-Firmen echt net-new sind.

## Methode
1. **Website/Deep Research** zur Segmentvalidierung (Freiberufler-Universum DE >300k Einheiten).
2. **Apollo.io Organization Search** als Skalier-Engine (NAICS × Mitarbeiterband × DE),
   segmentweise paginiert.
3. **Dedupe** (normalisierte Domain) + **firmographische Bereinigung** (AG/SE/Streubesitz,
   öffentliche Hand, Kliniken/Uni, e.V./gGmbH/Stiftung, Genossenschaften/Banken raus).
4. **Exklusion** der 4 Kundenlisten → 4.005 net-new, danach per Apollo auf 5.000 aufgefüllt.
5. Intelligente Pro-Firma-Prüfung → Clay Sculptor Prompt (Notion), nicht token-teuer im Modell.

## Bedarfslogik
photovest-Kunde = einkommensstarke Privatperson mit hoher Einkommensteuerlast
(ab ~70 T€ Einkommen, >30 T€ Steuer/Jahr), über Gewerbe. Als Firma abgebildet =
inhaber-/gesellschaftergeführtes, profitables Unternehmen mit hoch besteuertem Eigner.

Hinweis: Die Ausschluss-/Zwischen­dateien (Kunden-Kontaktlisten, kombinierte Exclude-Sets)
werden bewusst NICHT ins Repo committet (proprietäre Kontaktdaten).
