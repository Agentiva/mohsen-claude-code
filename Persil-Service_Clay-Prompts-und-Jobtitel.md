# Persil Service – Clay-Sculptor-Prompts & Jobtitel je Playbook

Für jedes der 4 Persil-Service-Playbooks:
1. **Clay-Sculptor-/Claygent-Prompt** – prüft pro Firma (`{{company_name}}` / `{{domain}}`) den echten Bedarf und gibt ein striktes JSON-Verdict zurück (für die „AI /Claygent"-Spalte in Clay).
2. **25 Jobtitel** – komma-separiert, Tier 1 (Entscheider) zuerst, dann Tier 2 (Influencer/Anwender), direkt in Clays „Find People"-Jobtitel-Feld einfügbar.

> Einheitliches JSON-Ausgabeformat für alle Prompts:
> `{"qualifiziert": true|false, "konfidenz": 0.0-1.0, "bedarfs_score": 0-100, "begruendung": "1-2 Sätze", "belege": [{"fakt": "...", "url": "..."}], "playbook": "<Playbook-Name>"}`
> Nur echte, auf der Website belegbare Fakten nutzen. Nichts erfinden. Bei fehlender Website / kein Beleg → `qualifiziert: false`, `konfidenz` niedrig.

---

## 1) Apotheken-Wäscheservice

### Clay-Sculptor-Prompt
```
Du bist B2B-Qualifizierungs-Analyst für Persil Service (Henkel) – ein professioneller Textil-/Berufskleidungs-Wäscheservice. Prüfe, ob die Firma {{company_name}} (Domain: {{domain}}) eine passende Zielfirma für das Playbook "Apotheken-Wäscheservice" ist.

Öffne die Website {{domain}} (Startseite, Über-uns/Team, Leistungen, Impressum) und beantworte anhand belegbarer Fakten:

QUALIFIZIERT, wenn ALLE zutreffen:
- Es ist eine öffentliche Vor-Ort-Apotheke oder ein Apotheken-Filialverbund in Deutschland (Offizin mit Kundenverkehr), inkl. Versand-/Online-Apotheke mit eigenem Standort.
- Es gibt eigenes Apotheken-Personal (Apotheker, PTA, PKA), das Berufs-/Hygienekleidung (Kittel, Kasack) trägt.
- Die Firma betreibt keine eigene professionelle Wäscherei-Infrastruktur.

BEDARFS-SIGNALE (erhöhen bedarfs_score):
- Rezeptur/Defektur/Labor oder Sterilherstellung (höhere Hygiene-/Kittelanforderungen).
- Mehrere Filialen / Filialverbund (Skalierung, einheitliches Auftreten).
- Team-/Karriereseite, die auf Personalbindung / Mitarbeitergewinnung im PTA-/PKA-Fachkräftemangel hindeutet.

AUSSCHLUSS (qualifiziert = false):
- Reine Verzeichnisse/Portale, Apothekenkammern/-verbände, Pharmagroßhandel, Hersteller, Kooperations-Dachseiten ohne eigene Apotheke.
- Keine erreichbare Website oder kein Apothekenbezug belegbar.

Gib NUR dieses JSON zurück:
{"qualifiziert": true|false, "konfidenz": 0.0-1.0, "bedarfs_score": 0-100, "begruendung": "...", "belege": [{"fakt":"...","url":"..."}], "playbook": "Apotheken-Wäscheservice"}
```

### 25 Jobtitel (komma-separiert)
Apothekeninhaber, Apothekeninhaberin, Inhaber Apotheke, Apotheker, Apothekerin, approbierter Apotheker, Apothekenleiter, Apothekenleiterin, Leiter der Apotheke, selbstständiger Apotheker, Filialleiter Apotheke, Filialleiterin Apotheke, Filialapothekenleiter, Verbundleiter Apotheken, Standortleiter Apotheke, Pharmacy Owner, Pharmacist, Owner Pharmacy, Erste PTA, PTA-Teamleitung, Leitende PTA, Pharmazeutisch-technische Assistentin, PKA, Pharmazeutisch-kaufmännische Angestellte, QMB Apotheke

---

## 2) Arztpraxen-Wäscheservice

### Clay-Sculptor-Prompt
```
Du bist B2B-Qualifizierungs-Analyst für Persil Service (Henkel) – ein professioneller Textil-/Berufskleidungs-Wäscheservice. Prüfe, ob die Firma {{company_name}} (Domain: {{domain}}) eine passende Zielfirma für das Playbook "Arztpraxen-Wäscheservice" ist.

Öffne die Website {{domain}} (Startseite, Team, Leistungen/Fachgebiet, Impressum) und beantworte anhand belegbarer Fakten:

QUALIFIZIERT, wenn ALLE zutreffen:
- Es ist eine niedergelassene Arzt-/Facharztpraxis, Gemeinschaftspraxis oder ein MVZ in Deutschland (ambulant).
- Es gibt medizinisches Personal (Ärzte, MFA), das Berufs-/Bereichs-/Schutzkleidung (Kittel, Kasack) trägt.
- Die Praxis hat keine eigene validierte Wäscherei und wäscht Berufskleidung heute vermutlich privat/intern (TRBA 250: Heimwäsche kontaminierter Kleidung faktisch unzulässig).

BEDARFS-SIGNALE (erhöhen bedarfs_score):
- Fachrichtung mit hohem Wäscheaufkommen (Chirurgie, Dermatologie, Orthopädie, Gynäkologie, Innere/Hausarzt mit Eingriffen).
- Mehrere Standorte / MVZ-Struktur.
- Hinweise auf Hygiene-/QM-Anforderungen oder MFA-Recruiting (Fachkräftemangel, Benefits).

AUSSCHLUSS (qualifiziert = false):
- Kliniken/Krankenhäuser mit eigener Großwäscherei, reine Zahnlabore, Tierkliniken, Portale/Arztverzeichnisse, Ärztekammern/KV, Klinik-Konzern-Dachseiten.
- Keine erreichbare Website oder kein ambulanter Praxisbezug belegbar.

Gib NUR dieses JSON zurück:
{"qualifiziert": true|false, "konfidenz": 0.0-1.0, "bedarfs_score": 0-100, "begruendung": "...", "belege": [{"fakt":"...","url":"..."}], "playbook": "Arztpraxen-Wäscheservice"}
```

### 25 Jobtitel (komma-separiert)
Praxisinhaber, Praxisinhaberin, Niedergelassener Arzt, Niedergelassene Ärztin, Inhaber Arztpraxis, Facharzt, Fachärztin, Ärztlicher Leiter, Ärztliche Leitung, Praxismanager, Praxismanagerin, Praxismanagement, Leiter Praxismanagement, Erste MFA, Leitende MFA, Medizinische Fachangestellte, Praxiskoordinatorin, Verwaltungsleitung MVZ, Kaufmännische Leitung MVZ, Geschäftsführer MVZ, Standortleiter MVZ, Hygienebeauftragte, QM-Beauftragte, Practice Manager, Office Manager Praxis

---

## 3) Wäscheservice am Arbeitsplatz – Entsorgung & Gewerbebetriebe

### Clay-Sculptor-Prompt
```
Du bist B2B-Qualifizierungs-Analyst für Persil Service (Henkel) – ein professioneller Textil-/Berufskleidungs-Wäscheservice am Arbeitsplatz. Prüfe, ob die Firma {{company_name}} (Domain: {{domain}}) eine passende Zielfirma für das Playbook "Wäscheservice am Arbeitsplatz – Entsorgung & Gewerbebetriebe" ist.

Öffne die Website {{domain}} (Startseite, Leistungen, Über-uns, Karriere, Impressum) und beantworte anhand belegbarer Fakten:

QUALIFIZIERT, wenn ALLE zutreffen:
- Es ist ein operativ tätiger Entsorgungs-/Abfallwirtschafts-/Recycling- oder verwandter Gewerbebetrieb in Deutschland (z.B. Müllabfuhr, Containerdienst, Schrott/Metall, Sonderabfall, Bau-/Abbruchentsorgung, kommunaler Abfallbetrieb).
- Es gibt gewerbliches Personal (Fahrer, Lader, Müllwerker, Sortier-/Werkstattpersonal) mit stark verschmutzter Arbeits-/Warnschutzkleidung.
- Die Firma reinigt diese Kleidung nicht selbst professionell (kein eigener validierter Wäscherei-Betrieb).

BEDARFS-SIGNALE (erhöhen bedarfs_score):
- Eigener Fuhrpark / Sammel- & Tourenbetrieb, Warnschutz-/PSA-Pflicht.
- Hinweise auf Fahrer-/Personalmangel oder Recruiting gewerblicher Kräfte (Benefit-Argument).
- Kontaminierte Abfälle / Sonderabfall (GefStoffV: Arbeitgeber muss Reinigung sicherstellen, Heimwäsche verboten).

AUSSCHLUSS (qualifiziert = false):
- Reine Beratungs-/Planungs-/Software-Firmen ohne operatives Personal, Hersteller von Entsorgungstechnik/Behältern, Verbände/Ämter ohne eigenen Betrieb, Verzeichnisse.
- Keine erreichbare Website oder kein operativer Entsorgungsbezug belegbar.

Gib NUR dieses JSON zurück:
{"qualifiziert": true|false, "konfidenz": 0.0-1.0, "bedarfs_score": 0-100, "begruendung": "...", "belege": [{"fakt":"...","url":"..."}], "playbook": "Wäscheservice am Arbeitsplatz – Entsorgung & Gewerbebetriebe"}
```

### 25 Jobtitel (komma-separiert)
Geschäftsführer, Geschäftsführerin, Werkleiter, Werkleiterin, Betriebsleiter, Betriebsleiterin, Operations Manager, Standortleiter, Niederlassungsleiter, Inhaber, Prokurist, Personalleiter, Leiter Personal, HR-Leiter, Head of HR, Fuhrparkleiter, Leiter Fuhrpark, Disponent, Kraftverkehrsmeister, Schichtleiter, Werkstattleiter, Teamleiter Sammlung, Fachkraft für Arbeitssicherheit, Leiter Arbeitssicherheit, HSE Manager

---

## 4) Wäscheservice am Arbeitsplatz – Büro & Corporate-Benefit

### Clay-Sculptor-Prompt
```
Du bist B2B-Qualifizierungs-Analyst für Persil Service (Henkel) – ein Textil-/Wäscheservice am Arbeitsplatz, der Unternehmen als steuerfreier Mitarbeiter-Benefit (Sachbezug) angeboten wird. Prüfe, ob die Firma {{company_name}} (Domain: {{domain}}) eine passende Zielfirma für das Playbook "Wäscheservice am Arbeitsplatz – Büro & Corporate-Benefit" ist.

Öffne die Website {{domain}} (Startseite, Über-uns, Karriere/Benefits, Standorte, Impressum) und beantworte anhand belegbarer Fakten:

QUALIFIZIERT, wenn ALLE zutreffen:
- Es ist ein Unternehmen mit relevanter Büro-/Angestellten-Belegschaft in Deutschland (Richtwert ab ~250 Mitarbeitende an einem oder mehreren Bürostandorten).
- Die Belegschaft ist überwiegend Office/White-Collar (z.B. IT/Software, Versicherung, Banken/Finanzen, Beratung, Agentur/Medien, Ingenieurbüro, Industrie-Verwaltung).
- Das Unternehmen investiert erkennbar in Arbeitgeberattraktivität / Mitarbeiterbindung.

BEDARFS-SIGNALE (erhöhen bedarfs_score):
- Karriere-/Benefits-Seite mit vorhandenen Mitarbeiter-Benefits (Retention-Fokus, Employer Branding).
- Hybrid-/Zurück-ins-Büro-Konzept, mehrere Standorte, Wachstum/aktives Recruiting.
- Hinweise auf HR-/People-Funktion, ESG/Nachhaltigkeit.

AUSSCHLUSS (qualifiziert = false):
- Sehr kleine Firmen (< ~100 MA), reine Filial-/Retail-Ketten ohne relevante Büro-Belegschaft, Holdings-/Briefkasten-Gesellschaften, Verzeichnisse/Portale.
- Keine erreichbare Website oder keine Büro-Belegschaft belegbar.

Gib NUR dieses JSON zurück:
{"qualifiziert": true|false, "konfidenz": 0.0-1.0, "bedarfs_score": 0-100, "begruendung": "...", "belege": [{"fakt":"...","url":"..."}], "playbook": "Wäscheservice am Arbeitsplatz – Büro & Corporate-Benefit"}
```

### 25 Jobtitel (komma-separiert)
Head of People, HR-Leiter, HR-Leiterin, Leiter Personal, Personalleiter, People & Culture Manager, Head of People & Culture, Head of HR, HR Manager, People Operations Manager, HR Business Partner, Employer Branding Manager, Benefits Manager, Total Rewards Manager, Feelgood Manager, Office Manager, Workplace Manager, Teamassistenz, Facility Manager, Leiter Gebäudemanagement, Head of Facility Management, Geschäftsführer, CFO, Kaufmännische Leitung, COO
