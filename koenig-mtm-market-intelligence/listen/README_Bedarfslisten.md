# König MTM — Bedarfsqualifizierte Zielfirmen-Listen (Apollo + Web)

Primärmarkt **Europa (ohne UK)**. Quelle: Apollo.io Organization Search, firmographisch gefiltert
(Branche/NAICS × Mitarbeiterband 50–5.000 × Land), UK/Irland ausgeschlossen, dann bereinigt
(offensichtliche Nicht-Passer wie Consulting/Software/Versicherung/Uni/Hotel etc. raus) und dedupliziert.

## Artefakt 1 — CSVs (Spalten: `company_name,domain`)

| Playbook | Datei | Firmen | Ziel |
|---|---|---|---|
| Luft- & Raumfahrt / Defense | `aerospace_clean.csv` | **2.137** | 2.000 ✓ |
| Antrieb & E-Mobilität | `antrieb_emobilitaet_clean.csv` | **587** | 500 ✓ |
| Medizintechnik | `medizintechnik_clean.csv` | **681** | 500 ✓ |
| Maschinen- & Werkzeugbau | `maschinenbau_clean.csv` | **765** | 500 ✓ |
| Robotik & Antriebstechnik | `robotik_antriebstechnik_clean.csv` | **543** | 500 ✓ |
| Windkraft & Schwerindustrie | `windkraft_schwerindustrie_clean.csv` | **566** | 500 ✓ |
| **Master (cross-dedupliziert, + Spalte `playbook`)** | `master_alle_segmente.csv` | **4.790 unique** | — |

> Hinweis: Das ist der **firmographische Pool** (richtige Branche/Größe/Region). Die intelligente
> Pro-Firma-Bedarfsprüfung läuft günstig in Clay über den Prompt unten — danach in Clay nach
> `fit_tier ∈ {A,B}` filtern und in die Kampagne exportieren.

---

## Artefakt 2 — Clay-Sculptor/Claygent-Qualifizierungs-Prompt

Inputs: `{{company_name}}`, `{{domain}}`

```
Du bewertest, ob das Unternehmen {{company_name}} ({{domain}}) einen ECHTEN Bedarf an
hochpräziser Sonder-Spanntechnik von WILHELM KÖNIG MTM hat (hydraulische/mechanische
Spanndorne "Königdorn", Rundlauf < 0,003 mm, kundenspezifisch konstruiert, Engineering-to-Order).

KÖNIG MTM löst: prozesssichere, rundlaufgenaue Aufnahme ROTATIONSSYMMETRISCHER Präzisionsteile
(Wellen, Zahnräder/Verzahnung, Rotoren, Turbinenscheiben, Implantate, Spindeln) beim
DREHEN, SCHLEIFEN, VERZAHNUNGSSCHLEIFEN/-FRÄSEN, Honen, Wuchten, Messen — dort, wo
Katalog-Spannmittel (Hainbuch/Schunk/Röhm/Emuge) nicht ausreichen.

VORGEHEN:
1. Besuche {{domain}} (Startseite, "Produkte/Leistungen", "Fertigung/Maschinenpark", "Branchen").
2. Prüfe auf konkrete Bedarfssignale:
   - EIGENE spanende Fertigung (CNC-Drehen, -Schleifen, Verzahnungsbearbeitung) im Haus?
   - Rotationssymmetrische Präzisionsteile / Verzahnungs- / Wellen- / Turbinen- / Implantatteile?
   - Verzahnungsmaschinen-Hinweise (Kapp, Reishauer, Liebherr, Gleason, Höfler) oder Schleifmaschinen?
   - Branche: Aerospace/Triebwerk, Antrieb/E-Mobility, Medizintechnik, Maschinenbau, Robotik/Antrieb, Windkraft/Schwerindustrie?
   - Zertifizierungen (AS9100, IATF 16949, ISO 13485, ISO 9001) als Präzisions-/Serienindikator?
3. HARTE AUSSCHLÜSSE (fit_tier = C): reiner Händler/Reseller ohne Fertigung; nur Blech/Guss/Schweißen/
   Montage ohne rotationssymmetrische Zerspanung; reine Dienstleistung/Engineering-Büro ohne eigene
   Maschinen; Software/IT; Betreiber/Entwickler ohne Fertigung (z. B. Windpark-Betreiber, Airline).

OUTPUT (striktes JSON):
{
  "fit_tier": "A | B | C",            // A = klarer Bedarf (eigene Präzisions-Zerspanung rotationssym. Teile);
                                       // B = plausibel/teilweise; C = kein Bedarf/Ausschluss
  "does_precision_rotational_machining": "yes | no | unclear",
  "key_signal": "kürzester Beleg von der Website (z. B. 'Verzahnungsschleifen, AS9100, eigene CNC-Dreherei')",
  "reason": "1 Satz Begründung"
}
```

In Clay: Spalten anlegen, nach `fit_tier` ∈ {A,B} filtern, dann „Find People" (Titel unten) anwenden und exportieren.

---

## Artefakt 3 — ~25 Jobtitel für „Find People" in Clay (copy-paste, eine Zeile)

```
Geschäftsführer, CEO, Inhaber, Managing Director, Werkleiter, Plant Manager, Fertigungsleiter, Produktionsleiter, Head of Production, Head of Manufacturing, Technischer Leiter, Leiter Zerspanung, Head of Machining, Leiter Dreherei, Meister Zerspanung, Arbeitsvorbereitung, Fertigungsplaner, Prozessingenieur, Industrial Engineer, REFA-Techniker, Technischer Einkauf, Einkaufsleiter, Head of Purchasing, Strategischer Einkäufer, Leiter Qualitätssicherung, Head of Quality, QS-Leiter
```

- **Tier 1 (Entscheider / Economic Buyer):** Geschäftsführer / CEO / Inhaber / Werkleiter / Plant Manager, Fertigungs-/Produktionsleiter, Head of Production/Manufacturing, Technischer Leiter, Technischer Einkauf / Einkaufsleiter / Head of Purchasing / Strategischer Einkäufer.
- **Tier 2 (Champion / Anwender / Influencer):** Leiter Zerspanung / Head of Machining / Leiter Dreherei / Meister Zerspanung, Arbeitsvorbereitung / Fertigungsplaner / Prozessingenieur / Industrial Engineer / REFA, Leiter Qualitätssicherung / Head of Quality / QS-Leiter.
