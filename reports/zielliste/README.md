# Zielliste — Kampagne „Trainer statt Formatierer" (Jobtiva · NRW-Bildungsträger)

Stand: 05.08.2026 · Methode: Deep Research per Websuche (kein Apollo/Clay) · Artefakte: `liste.csv`, `clay-qualifizierung-prompt.md`, `jobtitles-clay.txt`

---

## 1. Bedarfsprofil

```
Kunde / Produkt:    Jobtiva (jobtiva.ai) — KI-Bewerbungsplattform: Lebenslauf, Anschreiben
                    (DIN 5008), ATS-Check, Unternehmensrecherche, Interviewvorbereitung,
                    Gehaltcheck, Berufscheck (RIASEC), KI-Bewerbungsfoto; 20 Sprachen;
                    Chrome-Extension; White-Label/Lizenz für Träger geplant.

Problem, das es     Bildungsträger und Jobcenter betreuen 150–300 Klient:innen je Berater:in.
löst:               Individuelle Bewerbungshilfe ist im Tagesgeschäft nicht leistbar; Dozent:innen
                    verbringen Kurszeit mit Formatierung statt Coaching. Migrant:innen scheitern
                    am deutschen Anschreiben. Bestehende Werkzeuge sind Word-Vorlagen.

Ziel-Branchen /     Tier 1: AZAV-zertifizierte Bildungsträger mit AVGS-MAT- bzw.
Sub-Sektoren:       Bewerbungstrainings-Portfolio (private Träger, Wohlfahrts- und
                    Wirtschafts-Bildungswerke, Kammer-Akademien).
                    Tier 2: kommunale Beschäftigungs-/Qualifizierungsgesellschaften,
                    Volkshochschulen mit Jobcenter-Maßnahmen, Berufsförderungswerke.

Größe:              3–30 Standorte, 200–3.000 Teilnehmende/Jahr. Ein-Standort-Träger nur,
                    wenn Bewerbungstraining Kernangebot ist.

Region:             Nordrhein-Westfalen (Pilotregion; Gründersitz Wesseling, Pilotstandort
                    Düsseldorf). Bundesweite Träger nur mit belegtem NRW-Standort.

Bedarfs-Signale:    AZAV-Zulassung / AVGS-Abrechnung · Bewerbungstraining oder Jobcoaching im
                    Kursportfolio · Integrations- und Sprachangebote (BAMF, IQ, ESF+) ·
                    offene Stellen „Dozent:in/Trainer:in Bewerbungstraining" · Word-Vorlagen
                    und statische PDF-Musterbewerbungen auf den Kursseiten · laufende
                    Förderprojekte · mehrere Standorte.

Ausschluss:         Einzel-Coaches mit Personenmarke · Lead-Gen-/Vergleichsportale ·
                    Zertifizierungsstellen und Verbände ohne eigene Maßnahmen · reines
                    Gründungscoaching · arbeitgeberseitige HR-/Recruiting-Software ·
                    kein NRW-Bezug.
```

---

## 2. Was in `liste.csv` steht

**55 Organisationen** mit `company_name,domain`. Jede Domain stammt aus einer realen Suchtreffer-URL, in der Titel und Snippet die Organisation eindeutig benennen — keine geratene Domain.

Zusammensetzung:

| Gruppe | Anzahl (ca.) | Beispiele |
|---|---|---|
| Bundesweite Träger mit NRW-Standorten | 20 | WBS TRAINING, Grone, COMCAVE, DAA, IBB, SBH West, DEKRA Akademie, TÜV Rheinland Akademie, Kolping |
| NRW-regionale Träger & Institute | 20 | Weststadt Akademie (Essen), Bildungsinstitut Vogel (Bochum/Herne), BRW (Köln/Krefeld), Rheindenker-Akademie, Domstadt-Akademie, BSG Bildungsinstitut |
| Kommunale / öffentlich-nahe Träger | 8 | dobeq (Dortmund), Werkstatt im Kreis Unna, REGE mbH (Bielefeld), BFW Dortmund, BFW Düren, VHS Köln, VHS Essen |
| Kammer- und Wirtschafts-Akademien | 7 | HWK Dortmund, HWK Düsseldorf, HWK Köln, IHK Nord Westfalen, BWNRW, Arbeit und Leben NRW |

---

## 3. Ehrliche Einordnung — was diese Liste ist und was nicht

**Sie ist eine belastbare Startliste, nicht die vollständige Zielliste.** Der Report veranschlagt für die Kampagne 250–400 NRW-Trägerstandorte. Erreicht sind 55 Organisationen. Zwei Gründe:

1. **Kein Seitenabruf möglich.** In dieser Umgebung ist der direkte Abruf von Webseiten blockiert (HTTP 403 bzw. Netzwerk-Policy). Schritt 3.2 des Verfahrens — Verzeichnisseiten abrufen und Firmenlisten extrahieren — konnte nicht ausgeführt werden. Verwendbar war ausschließlich die Suche, und eine Suchanfrage liefert acht bis zehn Treffer, keine Trägerliste.
2. **Kein zentrales AZAV-Register.** Ein öffentliches Gesamtverzeichnis zertifizierter Träger existiert nicht; die Daten liegen verteilt in KURSNET und bei den Zertifizierern.

**Ebenfalls offen:** die im Verfahren vorgesehene Einzelprüfung jeder Firmenwebsite. Sie ist bewusst in den Clay-Sculptor-Prompt verlagert — der prüft dieselben Kriterien pro Firma und liefert ein belegtes JSON-Verdict. Die 55 Einträge sind also **vorqualifiziert, nicht endqualifiziert**.

### Wie die Liste auf 250–400 wächst

| Weg | Quelle | Erwarteter Zugewinn |
|---|---|---|
| **KURSNET-Extraktion** (Weiterbildungsdatenbank der BA) — Filter: NRW × Maßnahmeart AVGS-MAT | `arbeitsagentur.de` / KURSNET | 150–250 Standorte |
| **GenauMeinKurs Träger-A–Z** — über 2.500 geprüfte AZAV-Träger, nach NRW filtern | `genaumeinkurs.de/bildungstraeger-a-z/` | 80–150 |
| **Mitgliederliste Bildungsverband (BBB)** — über 170 Träger, NRW-Anteil extrahieren | `bildungsverband.info/mitglieder` | 40–70 |
| **Regionale Weiterbildungsanbieter der BA** je Agenturbezirk (16 Bezirke in NRW) | `arbeitsagentur.de/vor-ort/…/regionaleweiterbildungsanbieter` | 100–200 |
| **IHK-Übersicht Bildungsträger mittleres Ruhrgebiet** (PDF-Verzeichnis) | `ihk.de` | 30–60 |
| **Freie Wohlfahrtspflege NRW** — Mitgliedsverbände und deren Bildungswerke | `freiewohlfahrtspflege-nrw.de` | 30–50 |
| **Alternativ per Datenbank** | Skill `bedarfsliste` über Apollo/Clay, Branche „Professional Training & Coaching" × NRW | 300–600 roh, danach Sculptor-Filter |

Alle Zugewinne über dasselbe Dedup-Skript auf `liste.csv` mergen:

```bash
python3 .claude/skills/firmen-deepresearch/scripts/merge_dedupe.py \
  reports/zielliste/liste.csv batch2.csv > reports/zielliste/liste.csv
```

---

## 4. Nicht aufgenommen (und warum)

| Ausgeschlossen | Grund |
|---|---|
| `avgs-coaching.de`, `avgs-coaching.team`, `avgs-bewerbungscoaching.com`, `avgs-job-coaching.de`, `avgs-karrierecoaching.de`, `online-avgs-coaching.de`, `avgs-coaching.jetzt` | SEO-/Lead-Gen-Landingpages, kein erkennbarer eigener Trägerbetrieb (A2) |
| `azavo.de`, `azav-wissen.de`, `azav-zertifikat.de`, `genaumeinkurs.de`, `careertune.de` | Portale und Zertifizierungs-Ratgeber — als Quelle wertvoll, als Zielkunde falsch (A2) |
| `avgs-gruendungscoaching.de`, `selbststaendigkeit.de` | Fokus Existenzgründung, kein Bewerbungs-/Vermittlungsangebot (A3) |
| `gina-friedrich.com`, `anjafuchs-coaching.de`, `christian-b-rahe.de`, `praxis-duru.de` | Einzel-Coaches mit Personenmarke (A1) |
| `bildungsverband.info`, `bv-bfw.de`, `wbk-nrw.de`, `freiewohlfahrtspflege-nrw.de`, `dwf-do.de` | Verbände und Netzwerke — Multiplikatoren für einen eigenen Kanal, keine Maßnahmenträger (A2) |
| Berger Bildungsinstitut GmbH (Bochum) | Real und passend, aber es war keine eigene Domain auffindbar — Domains werden nicht geraten |

---

## 5. Nächster Schritt

1. `liste.csv` in Clay importieren, den Sculptor aus `clay-qualifizierung-prompt.md` über alle Zeilen laufen lassen.
2. Nach `bedarfs_score >= 60` in Welle 1 und `40–59` in Welle 2 segmentieren.
3. „Find People" mit den 25 Jobtiteln aus `jobtitles-clay.txt` auf die qualifizierten Accounts.
4. Sequenz nach dem im Report empfohlenen Kanal-Mix: LinkedIn → Telefon → Consent → E-Mail, über eine **separate Sending-Domain**, nicht über jobtiva.ai.
