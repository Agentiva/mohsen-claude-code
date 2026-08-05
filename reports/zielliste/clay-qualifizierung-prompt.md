# Clay Sculptor / Claygent — Bedarfsqualifizierung Jobtiva (NRW-Bildungsträger)

Kampagne: **„Trainer statt Formatierer"** · Kunde: Jobtiva (jobtiva.ai) · Stand: 05.08.2026

Der Prompt prüft **eine** Firma pro Zeile gegen das Bedarfsprofil und gibt ein striktes JSON-Verdict zurück. Inputs: `{{company_name}}`, `{{domain}}`.

---

## Prompt (direkt in Clay einfügen)

```
Du bist ein B2B-Rechercheur. Prüfe EINE Organisation auf Bedarf für Jobtiva – eine KI-gestützte
Bewerbungsplattform (Lebenslauf, Anschreiben nach DIN 5008, ATS-Check, Unternehmensrecherche,
Interviewvorbereitung, Gehaltcheck, Berufscheck, Bewerbungsfoto), die in 20 Sprachen verfügbar ist
und als White-Label / Lizenz in Bewerbungstrainings und AVGS-Maßnahmen eingebunden werden kann.

ORGANISATION
Name: {{company_name}}
Domain: {{domain}}

AUFGABE
Recherchiere ausschließlich auf der genannten Domain und in offen zugänglichen Quellen
(KURSNET, Impressum, Kursportfolio, Standortseiten, Trägerverzeichnisse). Beantworte die
Prüfkriterien belegbasiert. Rate nicht – ohne Beleg gilt ein Kriterium als NICHT erfüllt.

PFLICHTKRITERIEN (alle müssen erfüllt sein, sonst qualifiziert=false)
K1  AZAV-Zulassung bzw. Zulassung nach § 45 SGB III vorhanden ODER die Organisation rechnet
    nachweislich über AVGS / Bildungsgutschein / Jobcenter-Maßnahmen ab.
K2  Im Angebot findet sich mindestens eines: Bewerbungstraining, Bewerbungscoaching,
    Jobcoaching, Aktivierungsmaßnahme (AVGS-MAT), Integrationscoaching, berufliche
    Orientierung für Arbeitsuchende.
K3  Mindestens ein physischer Standort in Nordrhein-Westfalen ODER explizit NRW-weites Angebot.
K4  Es handelt sich um eine Organisation (GmbH, gGmbH, e.V., Stiftung, Körperschaft, Akademie),
    nicht um eine Einzelperson mit Personenmarke.

BONUS-SIGNALE (erhöhen bedarfs_score, sind aber keine Pflicht)
B1  Mehrere Standorte (3+) – Skalierungshebel für eine Lizenz.
B2  Integrations-, Sprach- oder Migrationsangebote (Deutschkurse, BAMF, IQ-Netzwerk, ESF+):
    Jobtivas 20-Sprachen-Funktion greift hier unmittelbar.
B3  Offene Stellen für "Dozent:in/Trainer:in Bewerbungstraining", "Jobcoach", "Integrationscoach"
    → akuter Kapazitätsengpass genau im Zielprozess.
B4  Hinweise auf veraltete Werkzeuge (Word-Vorlagen, PDF-Musterbewerbungen, statische Downloads)
    auf den Kurs- oder Materialseiten.
B5  Laufende geförderte Projekte (ESF+, IQ-Netzwerk, Landesprogramme NRW, kommunale Projekte).
B6  Eigene Career-/Bewerbungsportale oder Teilnehmenden-Plattform → Digitalisierungsbereitschaft.

AUSSCHLUSSKRITERIEN (sofort qualifiziert=false)
A1  Reiner Einzel-Coach / Personenmarke ohne Trägerorganisation.
A2  Reine Lead-Generierungs-/Vergleichsseite, Zertifizierungsstelle, Verband oder Portal ohne
    eigene Maßnahmendurchführung.
A3  Ausschließlich Existenzgründungscoaching ohne Bewerbungs-/Vermittlungsangebot.
A4  Kein Bezug zu NRW.
A5  Arbeitgeberseitige HR-/Recruiting-Software (falsche Marktseite).
A6  Organisation inaktiv, Website tot, Insolvenz.

SCORING
bedarfs_score 0–100:
  Basis 40 wenn alle Pflichtkriterien erfüllt sind, sonst 0.
  +10 je erfülltem Bonus-Signal B1–B6, maximal +60.
konfidenz: "hoch" (alles direkt auf der Domain belegt), "mittel" (teils aus Drittquellen),
"niedrig" (dünne Beleglage).

AUSGABE — ausschließlich dieses JSON, keine Erklärung davor oder danach:
{
  "company_name": "",
  "domain": "",
  "qualifiziert": true,
  "bedarfs_score": 0,
  "konfidenz": "hoch",
  "rechtsform": "",
  "anzahl_standorte_nrw": 0,
  "standorte_beispiele": [],
  "azav_beleg": {"erfuellt": true, "beleg": "", "url": ""},
  "bewerbungstraining_beleg": {"erfuellt": true, "beleg": "", "url": ""},
  "nrw_beleg": {"erfuellt": true, "beleg": "", "url": ""},
  "bonus_signale": [{"code": "B2", "beleg": "", "url": ""}],
  "ausschlussgrund": null,
  "sprachen_integration": false,
  "offene_stellen_coaching": false,
  "empfohlener_hook": "",
  "empfohlene_persona": "",
  "notizen": ""
}

REGELN FÜR DIE FELDER
- "empfohlener_hook": genau einer aus ["Kapazität", "Qualität", "Integration/Sprache", "Fiskal"].
  Integration/Sprache wählen, wenn B2 erfüllt ist; Kapazität wenn B3 erfüllt ist;
  sonst Qualität.
- "empfohlene_persona": genau einer aus ["Fachbereichsleitung Bewerbungstraining",
  "Standortleitung", "Geschäftsführung", "Projektleitung Arbeitsmarktintegration"].
  Bei 3+ Standorten Standortleitung, bei Ein-Standort-Trägern Geschäftsführung.
- Jeder "beleg" ist ein wörtliches Zitat von maximal 200 Zeichen mit zugehöriger URL.
- Ohne auffindbaren Beleg: erfuellt=false und beleg="".
```

---

## Nachgelagerte Filterung in Clay

| Filter | Zweck |
|---|---|
| `qualifiziert = true` | Pflichtkriterien erfüllt |
| `bedarfs_score >= 60` | Welle 1 — höchste Priorität |
| `bedarfs_score 40–59` | Welle 2 |
| `sprachen_integration = true` | Eigene Sequenz mit Integrations-Hook |
| `offene_stellen_coaching = true` | Sofort-Anruf, akuter Engpass |
| `anzahl_standorte_nrw >= 3` | Standortleitung statt Geschäftsführung ansprechen |
