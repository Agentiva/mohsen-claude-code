# Persil Service – Playbook „Müllentsorgung": Clay-Sculptor-Prompt & 25 Jobtitel

Zielsegment: **Müllentsorgungs- & Abfallwirtschaftsbetriebe in Deutschland** (kommunal + privat) – der Segment mit hohem, unaufgefordertem Inbound-Bedarf laut Onboarding-Call.
Angebot: Persil Service = professionelle, hygienische Reinigung stark verschmutzter Arbeits-/Warnschutzkleidung + Textilservice „Am Arbeitsplatz" (Abhol-/Bringnetz), zugleich Mitarbeiter-Benefit.

> JSON-Ausgabeformat (für die „AI /Claygent"-Spalte in Clay):
> `{"qualifiziert": true|false, "konfidenz": 0.0-1.0, "bedarfs_score": 0-100, "begruendung": "1-2 Sätze", "belege": [{"fakt":"...","url":"..."}], "playbook": "Müllentsorgung"}`
> Nur belegbare Website-Fakten nutzen. Nichts erfinden. Keine Website / kein Beleg → `qualifiziert: false`, niedrige `konfidenz`.

---

## Clay-Sculptor-Prompt

```
Du bist B2B-Qualifizierungs-Analyst für Persil Service (Henkel) – ein professioneller Textil-/Berufskleidungs-Wäscheservice am Arbeitsplatz. Prüfe, ob die Firma {{company_name}} (Domain: {{domain}}) eine passende Zielfirma für das Playbook "Müllentsorgung" ist.

Öffne die Website {{domain}} (Startseite, Leistungen, Über-uns, Fuhrpark/Standorte, Karriere, Impressum) und beantworte ausschließlich anhand belegbarer Fakten.

QUALIFIZIERT, wenn ALLE zutreffen:
- Es ist ein operativ tätiger Müllentsorgungs- bzw. Abfallwirtschaftsbetrieb in Deutschland – z.B. Müllabfuhr, Abfallsammlung/-transport, kommunaler Abfallwirtschaftsbetrieb/Zweckverband/Stadtreinigung, privater Entsorger, Containerdienst, Wertstoff-/Recyclinghof-Betreiber, Sonderabfall-/Gewerbeabfallentsorger.
- Es gibt gewerbliches Betriebspersonal (Fahrer, Lader/Müllwerker, Sortier-, Wertstoffhof- oder Werkstattpersonal), das täglich stark verschmutzte Arbeits-/Warnschutzkleidung trägt.
- Die Firma reinigt diese Berufskleidung nicht selbst professionell (kein eigener validierter Wäscherei-Betrieb) – heute vermutlich Heimwäsche der Mitarbeitenden.

BEDARFS-SIGNALE (erhöhen bedarfs_score):
- Eigener Fuhrpark / Sammel- & Tourenbetrieb, Sammelfahrzeuge, Warnschutz-/PSA-Pflicht (DIN EN ISO 20471).
- Kontakt mit kontaminierten Abfällen / biologischen Arbeitsstoffen oder Sonderabfall (GefStoffV/TRBA 500: Arbeitgeber muss Reinigung sicherstellen, Heimwäsche kontaminierter Kleidung ist unzulässig).
- Hinweise auf Fahrer-/Fachkräftemangel oder aktives Recruiting gewerblicher Kräfte (Wäscheservice als sichtbarer Mitarbeiter-Benefit / Retention-Hebel).
- Mehrere Standorte / größere Belegschaft (Skalierung).

AUSSCHLUSS (qualifiziert = false):
- Reine Beratungs-, Planungs-, Software- oder Ingenieurfirmen der Abfallbranche ohne eigenes operatives Personal.
- Hersteller/Händler von Entsorgungstechnik, Müllfahrzeugen, Behältern oder Tonnen.
- Verbände, Ämter/Behörden ohne eigenen Sammel-/Betriebsdienst, Branchenverzeichnisse/Portale.
- Keine erreichbare Website oder kein operativer Müllentsorgungs-Bezug belegbar.

Gib NUR dieses JSON zurück:
{"qualifiziert": true|false, "konfidenz": 0.0-1.0, "bedarfs_score": 0-100, "begruendung": "...", "belege": [{"fakt":"...","url":"..."}], "playbook": "Müllentsorgung"}
```

---

## 25 Jobtitel (komma-separiert, Tier 1 → Tier 2)

Geschäftsführer, Geschäftsführerin, Werkleiter, Werkleiterin, Betriebsleiter, Betriebsleiterin, Operations Manager, Standortleiter, Niederlassungsleiter, Inhaber, Prokurist, Personalleiter, Leiter Personal, HR-Leiter, Head of HR, Fuhrparkleiter, Leiter Fuhrpark, Disponent, Kraftverkehrsmeister, Schichtleiter, Werkstattleiter, Teamleiter Sammlung, Fachkraft für Arbeitssicherheit, Leiter Arbeitssicherheit, HSE Manager

**Tier 1 (Entscheider/Budget & Champion):** Geschäftsführer, Werkleiter, Betriebsleiter/Operations Manager, Standort-/Niederlassungsleiter, Inhaber, Prokurist, Personalleiter/HR-Leiter.
**Tier 2 (operative Bedarfsträger/Influencer):** Fuhrparkleiter, Disponent, Kraftverkehrsmeister, Schicht-/Werkstattleiter, Teamleiter Sammlung, Fachkraft für Arbeitssicherheit / HSE.
