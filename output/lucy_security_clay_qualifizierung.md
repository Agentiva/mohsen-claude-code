# Lucy Security – Clay Sculptor / Claygent Qualifizierung (3 Playbooks)

Für jedes Playbook enthält dieses Dokument:

1. **Claygent-/Sculptor-Qualifizierungs-Prompt** – prüft pro Firma (`{{company_name}}` / `{{domain}}`) den echten Bedarf an Lucy Security gegen die Bedarfs-Signale und Ausschlusskriterien des jeweiligen Playbooks und gibt ein **striktes JSON-Verdict** zurück.
2. **~25 Jobtitel (Tier 1 + Tier 2)** – komma-separiert, direkt copy-paste-fähig in Clays „Find People"-Jobtitel-Feld.

**Einsatz in Clay:** Neue Spalte → *Claygent* (bzw. *Sculptor / AI-Formula*). Prompt einfügen, `{{company_name}}` und `{{domain}}` auf deine Spalten mappen. Modell mit Web-Zugriff wählen (Research). Output-Spalte auf JSON parsen und nach `qualifiziert = true` bzw. `bedarfs_score >= 7` filtern.

**Gemeinsames JSON-Output-Schema (alle Playbooks):**

```json
{
  "qualifiziert": true,
  "konfidenz": "hoch | mittel | niedrig",
  "bedarfs_score": 8,
  "segment_treffer": "kurze Einordnung, welcher Sub-Sektor",
  "belege": [
    {"signal": "welches Bedarfs-Signal erfüllt", "quelle_url": "https://..."}
  ],
  "ausschluss_grund": null,
  "empfohlene_ansprache": "1 Satz: bester Angle für die Erstansprache"
}
```

Regeln für alle Prompts: Nur belegbare Aussagen (mit `quelle_url`). Wenn kein Beleg gefunden → `konfidenz: "niedrig"` und `bedarfs_score` konservativ. Bei erfülltem Ausschlusskriterium → `qualifiziert: false` und `ausschluss_grund` setzen. Kein Fließtext außerhalb des JSON.

---

## 1) Banking & Financial Services DACH

### Claygent-Qualifizierungs-Prompt

```
Du bist ein B2B-Sales-Research-Agent für Lucy Security (Phishing-Simulations- & Security-Awareness-Plattform, On-Premise / EU- bzw. Schweiz-Hosting, DORA-Art.-13-, BAIT-/VAIT-/MaRisk-konform, native Deepfake-Vishing-Simulation).

Firma: {{company_name}}
Domain: {{domain}}

AUFGABE: Recherchiere die Firma (Website, Impressum, LinkedIn, Register, Presse) und bewerte, wie hoch ihr Bedarf an einer regulierungskonformen Security-Awareness-/Phishing-Simulations-Plattform ist.

BEDARFS-SIGNALE (je erfülltem Signal steigt bedarfs_score):
1. Reguliertes Finanzunternehmen in DACH: Bank, Sparkasse, Volks-/Raiffeisenbank, Privat-/Landes-/Förderbank, Kantonalbank (CH), Bausparkasse, Versicherer/Rückversicherer, Asset Manager/KVG/Vermögensverwalter, Zahlungsinstitut/Fintech (ZAG), Leasing/Factoring, Börse/Marktinfrastruktur.
2. Fällt unter DORA (seit 17.01.2025), BAIT/VAIT/KAIT/ZAIT, MaRisk AT 7.2, FINMA RS 2023/1 oder FMA-Aufsicht → verpflichtende, evaluierte Awareness-Programme inkl. Board.
3. Aufsicht durch BaFin / FINMA / FMA / EZB (SREP); externe WP-Prüfung (IDW PS 951).
4. Sitz bzw. Datenhaltung in DE/AT/CH → Datensouveränität, US-Cloud-Awareness-Tools problematisch (Group-Compliance/CDO sagt Nein).
5. Exponiert für Deepfake-Vishing / CEO-Fraud / Payment- & Treasury-Betrug (Treasury, M&A-Teams, Trader-Floor, Zahlungsverkehr).
6. Hinweise auf M365-Rollout (Teams-/WhatsApp-Phishing-Fläche) oder laufende Security-/Compliance-Einstellungen.

AUSSCHLUSSKRITERIEN (→ qualifiziert=false):
- Kein Finanz-/Versicherungsbezug (reine Handels-, Industrie-, Beratungs- oder Marketingfirma ohne Regulierung).
- Sitz außerhalb DACH ohne relevante DACH-Einheit.
- Reine Marke/Website ohne eigenständige Gesellschaft; insolvent/eingestellt/vollständig fusioniert (Domain leitet auf Dritt-Konzern um).
- Kleinstvermittler ohne eigene IT/Belegschaft (< ~10 MA), reiner Ein-Personen-Assekuradeur.

Bewerte bedarfs_score 0–10 (10 = klar reguliert, exponiert, DACH, eigene IT). Gib NUR das JSON gemäß Schema zurück.
```

### Jobtitel für „Find People" (Tier 1 + Tier 2, komma-separiert)

```
Chief Information Security Officer, CISO, Head of Information Security, Leiter Informationssicherheit, Head of IT Security, IT-Sicherheitsbeauftragter, Information Security Officer, Deputy CISO, Head of IT, IT-Leiter, Chief Information Officer, CIO, DORA Officer, Head of Operational Resilience, Chief Risk Officer, Head of Cyber Security, Cyber Security Manager, Head of IT Governance Risk and Compliance, Compliance Officer, Head of Compliance, Datenschutzbeauftragter, Data Protection Officer, Chief Security Officer, Security Awareness Manager, IT Security Engineer
```

---

## 2) Stadtwerke & kommunale Versorger DACH

### Claygent-Qualifizierungs-Prompt

```
Du bist ein B2B-Sales-Research-Agent für Lucy Security (Phishing-Simulations- & Security-Awareness-Plattform, On-Premise im eigenen RZ / beim kommunalen IT-Dienstleister / Private Cloud DE-CH, §30-BSIG- und §11-EnWG-konform, KRITIS-tauglich).

Firma: {{company_name}}
Domain: {{domain}}

AUFGABE: Recherchiere die Firma und bewerte den Bedarf an einer KRITIS-konformen Awareness-/Phishing-Simulations-Plattform.

BEDARFS-SIGNALE:
1. Kommunaler Ver- oder Entsorger in DACH: Stadtwerk, Energieversorger (Strom/Gas/Wärme), regionales EVU, Wasser-/Abwasserbetrieb, Abfall-/Entsorgungsbetrieb, Verteilnetzbetreiber, Verkehrsbetrieb/ÖPNV, kommunaler IT-Dienstleister, Energiegenossenschaft.
2. KRITIS-Relevanz: fällt unter §30 BSIG (NIS2-Umsetzung), §11 EnWG / IT-Sicherheitskatalog, B3S Energie/Wasser, ISO 27001/27019 → Nachweispflicht für wirksame, dokumentierte Awareness.
3. Prüfdruck durch BNetzA / externe §30-BSIG-Auditoren / Wirtschaftsprüfer; persönliche Geschäftsleiter-Haftung.
4. Konzern-/Mandantenstruktur (Mutter-Stadtwerk, Netztochter, Vertriebs-GmbH, Beteiligungen) → getrennte Auswertung + Gruppen-Reporting.
5. Datenschutz-/Konzernvorgabe verbietet US-Cloud → On-Prem oder Hosting beim kommunalen IT-Dienstleister (AKDB, ekom21, Dataport, KRZN, Komm.ONE) gefragt.
6. Exponiert für Teams-Phishing, Smishing auf Diensthandys, Quishing, USB-Drops im Betriebsgelände/Umspannwerk.

AUSSCHLUSSKRITERIEN (→ qualifiziert=false):
- Kein Ver-/Entsorgungs-/kommunaler Infrastruktur-Bezug (reine Software-, Handels-, Beratungsfirma, die nur „Energie/Netz/Wasser" im Namen trägt).
- Sitz außerhalb DACH.
- Reiner Marken-/Tarifname ohne eigenständige Gesellschaft; Kundenzentrum/Verein ohne eigene IT-Verantwortung.
- Reiner Anlagenbauer/Contractor ohne Betrieb kritischer Infrastruktur (Einzelfall prüfen).

Bewerte bedarfs_score 0–10 (10 = klarer KRITIS-Versorger, eigene IT, DACH, Konzernstruktur). Gib NUR das JSON gemäß Schema zurück.
```

### Jobtitel für „Find People" (Tier 1 + Tier 2, komma-separiert)

```
Chief Information Security Officer, CISO, IT-Sicherheitsbeauftragter, Informationssicherheitsbeauftragter, Leiter Informationssicherheit, Head of IT Security, IT-Leiter, Leiter IT, Head of IT, Chief Information Officer, CIO, Leiter Digitalisierung, Leiter IT-Infrastruktur, KRITIS-Beauftragter, Compliance-Beauftragter, Datenschutzbeauftragter, Data Protection Officer, Leiter Governance Risk and Compliance, Geschäftsführer, Kaufmännischer Leiter, Technischer Leiter, IT Security Manager, IT-Administrator, Leiter Organisation und IT, Sicherheitsbeauftragter
```

---

## 3) Government / Öffentlicher Sektor / Military / Defense DACH

### Claygent-Qualifizierungs-Prompt

```
Du bist ein B2B-Sales-Research-Agent für Lucy Security (Phishing-Simulations- & Security-Awareness-Plattform, Air-Gapped / On-Premise beim Bundes-/Landes-RZ (ITZBund, BWI, Dataport) / dedizierte DE-CH-Cloud mit BSI C5, VS-NfD-tauglich, BSI-IT-Grundschutz ORP.3-konform).

Organisation: {{company_name}}
Domain: {{domain}}

AUFGABE: Recherchiere die Organisation und bewerte den Bedarf an einer Air-Gapped-/On-Prem-fähigen Awareness-/Phishing-Simulations-Plattform.

BEDARFS-SIGNALE:
1. Öffentlicher Sektor / Defense in DACH: Kommunalverwaltung (Stadt/Gemeinde/Landkreis), Bundes-/Landesbehörde, Ministerium, öffentlicher IT-Dienstleister, öffentliche Hochschule/Universität/Forschungseinrichtung, Polizei/Feuerwehr/Rettung, öffentlich-rechtlicher Sozialversicherungsträger/Krankenkasse, Verteidigungsindustrie/Defense-Contractor.
2. Prüf-/Nachweispflicht: BSI IT-Grundschutz ORP.3.A1–A8, UP Bund / Mindeststandards Bund, Bundes-/Landesrechnungshof (Wirtschaftlichkeit), DSGVO/BDSG bei personenbezogenen Klickdaten.
3. Cloud-Verbot / C5-Pflicht / VS-NfD-Einstufung → US-/Cloud-Tools (KnowBe4, Proofpoint, SoSafe, Hoxhunt) ausgeschlossen; Air-Gapped oder Hosting bei ITZBund/BWI/Dataport/Bundesrechenzentrum gefragt.
4. Föderale/nachgeordnete Struktur (Ministerium mit nachgeordnetem Bereich, Land mit Mittelbehörden) → Mandantentrennung + konsolidiertes Aufsichts-Reporting.
5. Exponiert für Spear-Phishing (Bewerbungs-/Pressekontakte), Teams-Phishing (M365 Government Cloud), Smishing auf Diensthandys, USB-Drops im Foyer.
6. Personalrat-/Mitbestimmung & Geheimschutz relevant → braucht DSFA-/Pseudonymisierungs-taugliches, on-prem-fähiges Tool.

AUSSCHLUSSKRITERIEN (→ qualifiziert=false):
- Keine öffentliche/behördliche/Defense-Organisation (reine Privatfirma ohne öffentlichen Auftrag, die nur „Stadt/Verwaltung/Amt" im Namen trägt).
- Sitz außerhalb DACH.
- Reiner Verein/Initiative ohne eigene IT-Verantwortung oder Beschäftigte; aufgelöste/fusionierte Einheit.

Bewerte bedarfs_score 0–10 (10 = klare Behörde/Defense mit VS-/C5-Anforderung, eigene IT, föderale Struktur). Gib NUR das JSON gemäß Schema zurück.
```

### Jobtitel für „Find People" (Tier 1 + Tier 2, komma-separiert)

```
IT-Sicherheitsbeauftragter, Informationssicherheitsbeauftragter, ISB, Chief Information Security Officer, CISO, Behördlicher Datenschutzbeauftragter, Data Protection Officer, Leiter IT, IT-Leiter, Leiter Informationstechnik, Head of IT, Chief Information Officer, CIO, Leiter Amt für Informationstechnik, Leiter Digitalisierung und IT, Geheimschutzbeauftragter, Leiter Organisation und IT, IT-Koordinator, Referatsleiter IT, Head of Cyber Security, Cyber Security Officer, IT Security Manager, Leiter Rechenzentrum, Systemadministrator, Compliance Manager, Sicherheitsbeauftragter
```

---

### Hinweise zur Nutzung

- **Reihenfolge in Clay:** erst „Find People" mit den Jobtiteln des passenden Playbooks (auf die bereits qualifizierten Firmen), dann optional den Firmen-Qualifizierungs-Prompt als Gate davor, um Streuung zu vermeiden.
- **Tier 1** (Budget-/Entscheider & direkte Bedarfsträger) steht in jeder Liste vorne, **Tier 2** (technische Ebene / Beeinflusser / Anwender) hinten – bei Bedarf die Liste kürzen, wenn Clays Titel-Limit greift.
- **Sprache:** DE-Titel dominieren (DACH-Zielmarkt), gängige EN-Entsprechungen (CISO, CIO, DPO) sind ergänzt, da viele Konzerne englische Titel führen.
- **Filter-Empfehlung:** `qualifiziert = true` UND `bedarfs_score >= 7` für die Erstansprache; `bedarfs_score 4–6` als zweite Welle mit leichterem Angle.
