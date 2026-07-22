# Lindner – Clay-Assets pro Playbook

Zwei Dinge pro Playbook:
1. **Clay-Sculptor / Claygent-Prompt** – auf die importierte Liste (`company_name` + `domain`) anwenden, um jede Firma auf ECHTEN Bedarf zu prüfen. Danach in Clay nach `fit_tier` ∈ {A, B} filtern und exportieren.
2. **„Find People"-Jobtitel-Zeile** – copy-paste-fertig in das Clay-Titelfeld. Tier 1 = Entscheider/Economic Buyer, Tier 2 = technisch/operativ. Bewusst OHNE Einkauf und OHNE Nachhaltigkeitsmanager (so im Kickoff bestätigt).

Inputs in allen Prompts: `{{company_name}}`, `{{domain}}`.

> **In JEDEM Sculptor-Prompt ist eine Pflicht-Doppelprüfung eingebaut:** (a) hat die Firma wirklich Bedarf an Lindners Produkten/Dienstleistungen (Schredder/Zerkleinerung/Aufbereitungsanlagen) und (b) ist sie **kein Wettbewerber** (Maschinenbauer/-händler) und **kein Zulieferer**, der etwas AN Lindner verkaufen will. Trifft (b) zu → immer `fit_tier = C`. Diese Doppelprüfung ist die zweite, intelligente Verifizierungsstufe nach dem deterministischen `verify_screen.py`.

---

## Playbook 264 – Private Recyclers & Reprocessors

### Clay-Sculptor-Prompt
```
Du bist ein B2B-Sales-Researcher. Du bewertest, ob die unten genannte Firma einen ECHTEN Bedarf für die Industrieschredder von LINDNER (lindner.com) hat.

PRODUKT LINDNER: Stationäre und mobile Ein-/Zweiwellen-Schredder plus schlüsselfertige Zerkleinerungs-/Sortieranlagen für Abfall und Recycling. Löst: Verschleiß, ungeplante Stillstände und schwankende Output-Qualität bei der Zerkleinerung kontaminierter Materialströme.

ECHTER BEDARF besteht NUR, wenn die Firma:
- ein PRIVATES Entsorgungs-/Recyclingunternehmen ist, das selbst Material AUFBEREITET (nicht nur einsammelt/transportiert), UND
- physische Stoffströme zerkleinert/sortiert: Gewerbeabfall, Sperrmüll, Kunststoff, Papier/Kartonage, Bau-/Abbruchabfall, Schrott/Metall, Elektroaltgeräte (WEEE) oder eine eigene Sortier-/MRF-Anlage betreibt.

KEIN Bedarf (Tier C): Hersteller/Händler/Vermieter von Schredder-, Sortier- oder Recyclingmaschinen (Wettbewerber wie UNTHA, Vecoplan, Komptech, Doppstadt, Weima usw.); reine Berater/Ingenieurbüros; Software/IT; reine Transport-/Logistikfirmen ohne eigene Aufbereitung; reine Händler ohne Verarbeitung; Behörden ohne Anlage.

ZUSÄTZLICHE PFLICHTPRÜFUNG (immer durchführen):
(a) BEDARF BESTÄTIGEN: Belege konkret, dass die Firma Lindners Produkte/Dienstleistungen (Schredder/Zerkleinerung/Aufbereitung) tatsächlich brauchen könnte – nicht nur vage „irgendwas mit Abfall". Kein belegbarer eigener Aufbereitungsprozess → höchstens Tier B, im Zweifel C.
(b) WETTBEWERBER/ZULIEFERER AUSSCHLIESSEN: Prüfe, ob die Firma (i) ein WETTBEWERBER ist – Hersteller/Händler/Vermieter von Schredder-, Zerkleinerungs-, Sortier- oder Recyclingmaschinen – ODER (ii) ein ZULIEFERER, der etwas AN Lindner verkaufen will (Maschinen-/Anlagenbau, Engineering/Ingenieurbüro, Hydraulik, Antriebe, Fördertechnik, Stahl-/Metallbau, Automatisierung, Verschleiß-/Ersatzteile, Waagen). Trifft (i) ODER (ii) zu → IMMER fit_tier C, egal wie gut der Fit sonst wäre.

VORGEHEN:
1. Besuche https://{{domain}} (Startseite, „Leistungen"/„Anlagen"/„Standorte", „Über uns").
2. Bestimme, ob die Firma selbst Material aufbereitet und welche Stoffströme.
3. Achte auf Bedarfssignale: eigene Aufbereitungs-/Sortieranlage, Nennung von Schreddern/Zerkleinerung, mehrere Standorte/Werkstoffhöfe, Investitionen/Anlagenausbau, Zertifizierung als Entsorgungsfachbetrieb, Durchsatz in t/Jahr.
4. Prüfe die Doppelprüfung (a)+(b) oben.

GIB GENAU DIESES JSON ZURÜCK (nichts anderes):
{
  "fit_tier": "A | B | C",
  "has_need": "yes | no | unclear",
  "operates_processing": "yes | no | unclear",
  "is_competitor": "yes | no | unclear",
  "sells_to_lindner": "yes | no | unclear",
  "key_signal": "<stärkstes konkretes Bedarfssignal, max 10 Wörter, oder 'none'>",
  "reason": "<1 knapper Satz>"
}
Regel: Wenn is_competitor = yes ODER sells_to_lindner = yes, dann fit_tier = C.

Firma: {{company_name}}
Domain: {{domain}}
```

### Find-People-Jobtitel (eine Zeile → Clay)
```
Geschäftsführer, Managing Director, Inhaber, Owner, Geschäftsführender Gesellschafter, General Manager, Werkleiter, Standortleiter, Plant Manager, Betriebsleiter, Operations Manager, Head of Operations, Technischer Leiter, Technical Director, Technischer Geschäftsführer, Head of Technology, Produktionsleiter, Production Manager, Anlagenleiter, Leiter Aufbereitung, Prozessleiter, Leiter Instandhaltung, Maintenance Manager, Leiter Technik, Head of Recycling
```
Tier 1 (Entscheider): Geschäftsführer/Managing Director, Inhaber/Owner, Geschäftsführender Gesellschafter, Werkleiter, Standortleiter. — Tier 2 (technisch/operativ): Technischer Leiter, Betriebsleiter, Produktionsleiter, Anlagenleiter, Leiter Aufbereitung/Instandhaltung.

---

## Playbook 263 – Municipal & Public Waste Operators

### Clay-Sculptor-Prompt
```
Du bist ein B2B-Sales-Researcher. Du bewertest, ob die unten genannte Firma einen ECHTEN Bedarf für die Industrieschredder und schlüsselfertigen Anlagen von LINDNER (lindner.com) hat.

PRODUKT LINDNER: Robuste, störstoffresistente Schredder für Siedlungs- und Sperrmüll inkl. FPS-Brandschutzsystem (Li-Ionen-Risiko) sowie schlüsselfertige Behandlungsanlagen (Vorzerkleinerung, Metallabscheidung, Siebung, Sortierung).

ECHTER BEDARF besteht NUR, wenn die Firma:
- ein KOMMUNALES/ÖFFENTLICHES Entsorgungsunternehmen, Abfallwirtschaftsbetrieb, Zweckverband, Stadtwerk mit Abfallsparte oder eine öffentliche Versorgungsgesellschaft mit Abfallbehandlung ist, UND
- Siedlungs-/Sperr-/Bulkabfall selbst behandelt, sortiert oder zerkleinert (nicht nur Verwaltung/Gebühren).

KEIN Bedarf (Tier C): Maschinenhersteller/-händler (Wettbewerber); reine Berater; reine Wasser-/Abwasserbetriebe ohne Abfallsparte; reiner ÖPNV/Personentransport; reine Post/Bahn; reine Verwaltung/Behörde ohne eigene Anlage; Software/IT; Fach-Zweckverbände ohne Abfallbezug (KiTa, Schule/VHS, Tourismus, Wasser).

ZUSÄTZLICHE PFLICHTPRÜFUNG (immer durchführen):
(a) BEDARF BESTÄTIGEN: Belege, dass die Firma Siedlungsabfall SELBST behandelt/sortiert/zerkleinert (eigene Anlage, MBA, Umschlag, Sperrmüllaufbereitung) – nicht nur einsammelt oder verwaltet. Kein belegbarer Behandlungsprozess → höchstens Tier B, im Zweifel C.
(b) WETTBEWERBER/ZULIEFERER AUSSCHLIESSEN: Prüfe, ob die Firma (i) ein WETTBEWERBER ist (Hersteller/Händler von Schredder-/Sortier-/Recyclingmaschinen) ODER (ii) ein ZULIEFERER, der etwas AN Lindner verkaufen will (Maschinen-/Anlagenbau, Engineering/Ingenieurbüro, Hydraulik, Antriebe, Fördertechnik, Stahl-/Metallbau, Automatisierung, Verschleiß-/Ersatzteile). Trifft (i) ODER (ii) zu → IMMER fit_tier C.

VORGEHEN:
1. Besuche https://{{domain}} (Startseite, „Abfallwirtschaft"/„Entsorgung"/„Anlagen"/„Über uns").
2. Bestimme, ob die Firma Siedlungsabfall SELBST behandelt (nicht nur einsammelt/verwaltet).
3. Achte auf Bedarfssignale: eigene MBA/Sortier-/Umladeanlage, Sperrmüllaufbereitung, Nennung von Zerkleinerung/Schredder, Brandvorfälle/Li-Ionen-Thema, Ausschreibungen/Investitionen, kommunaler Entsorgungsauftrag.
4. Prüfe die Doppelprüfung (a)+(b) oben.

GIB GENAU DIESES JSON ZURÜCK (nichts anderes):
{
  "fit_tier": "A | B | C",
  "has_need": "yes | no | unclear",
  "operates_treatment": "yes | no | unclear",
  "is_competitor": "yes | no | unclear",
  "sells_to_lindner": "yes | no | unclear",
  "key_signal": "<stärkstes konkretes Bedarfssignal, max 10 Wörter, oder 'none'>",
  "reason": "<1 knapper Satz>"
}
Regel: Wenn is_competitor = yes ODER sells_to_lindner = yes, dann fit_tier = C.

Firma: {{company_name}}
Domain: {{domain}}
```

### Find-People-Jobtitel (eine Zeile → Clay)
```
Geschäftsführer, Managing Director, Werkleiter, Standortleiter, Betriebsleiter, Betriebsleiter Abfallwirtschaft, Leiter Abfallwirtschaft, Head of Waste Management, Technischer Leiter, Technical Director, Technischer Geschäftsführer, Head of Technology, Werksleiter, Plant Manager, Operations Manager, Head of Operations, Anlagenleiter, Leiter Technik, Leiter Entsorgung, Produktionsleiter, Prozessleiter, Leiter Instandhaltung, Maintenance Manager, Bereichsleiter Entsorgung, Amtsleiter Abfallwirtschaft
```
Tier 1 (Entscheider): Geschäftsführer/Managing Director, Werkleiter, Standortleiter, Leiter Abfallwirtschaft, Technischer Geschäftsführer. — Tier 2 (technisch/operativ): Technischer Leiter, Betriebsleiter (Abfallwirtschaft), Anlagenleiter, Leiter Technik/Entsorgung, Instandhaltung.

---

## Playbook 262 – Cement, Energy & RDF Off-takers

### Clay-Sculptor-Prompt
```
Du bist ein B2B-Sales-Researcher. Du bewertest, ob die unten genannte Firma einen ECHTEN Bedarf für die mehrstufigen EBS/RDF-Aufbereitungsanlagen und Schredder von LINDNER (lindner.com) hat.

PRODUKT LINDNER: Mehrstufige Ersatzbrennstoff-Anlagen (Vor-/Nachzerkleinerung, Metall-/Schwerstoffabscheidung, NIR-Sortierung, Inline-Qualitätsmonitoring) für kalibrierten Premium-RDF/SRF – für Zement-, Kalk- und Energieabnehmer sowie EBS-Produzenten.

ECHTER BEDARF besteht NUR, wenn die Firma:
- Ersatzbrennstoff (RDF/SRF) VERBRENNT oder PRODUZIERT – d.h. Zementwerk, Kalkwerk, Waste-to-Energy-/thermisches Kraftwerk, Heiz(kraft)werk/Fernwärme mit RDF-/Biomasse-Mitverbrennung, ODER dedizierter EBS/SRF-Produzent.

KEIN Bedarf (Tier C): Maschinenhersteller/EPC-Berater ohne eigenes Werk; reine Transportbeton-/Zuschlagstoff-Betriebe ohne Zementofen; reine Solar-/Windentwickler ohne thermische RDF-Nutzung; Software/IT; reiner Öl-/Gashandel; reine Vertriebs-/Logistikarme ohne eigenes Werk.

ZUSÄTZLICHE PFLICHTPRÜFUNG (immer durchführen):
(a) BEDARF BESTÄTIGEN: Belege, dass die Firma tatsächlich einen Zement-/Kalkofen, eine WtE-/Kraftwerksfeuerung oder eine EBS/SRF-Produktion BETREIBT (nicht nur handelt/vertreibt). Kein belegbarer Ofen/Feuerung/EBS-Prozess → höchstens Tier B, im Zweifel C.
(b) WETTBEWERBER/ZULIEFERER AUSSCHLIESSEN: Prüfe, ob die Firma (i) ein WETTBEWERBER ist (Hersteller/Händler von Schredder-/Aufbereitungsmaschinen) ODER (ii) ein ZULIEFERER, der etwas AN Lindner verkaufen will (Anlagenbau/EPC/Engineering-Ingenieurbüro, Hydraulik, Antriebe, Fördertechnik, Stahlbau, Automatisierung, Ersatzteile). Trifft (i) ODER (ii) zu → IMMER fit_tier C.

VORGEHEN:
1. Besuche https://{{domain}} (Startseite, „Werke/Standorte", „Alternative Brennstoffe"/„Nachhaltigkeit"/„Produkte").
2. Bestimme, ob ein Zement-/Kalkofen, eine WtE-/Kraftwerksfeuerung oder eine EBS-Produktion betrieben wird.
3. Achte auf Bedarfssignale: Nennung alternativer/ Ersatzbrennstoffe, Substitutionsrate, Klinker/Ofenlinie, EBS/SRF-Output, CO2-/Dekarbonisierungsziele, Kessel/Rostfeuerung.
4. Prüfe die Doppelprüfung (a)+(b) oben.

GIB GENAU DIESES JSON ZURÜCK (nichts anderes):
{
  "fit_tier": "A | B | C",
  "has_need": "yes | no | unclear",
  "burns_or_makes_rdf": "yes | no | unclear",
  "is_competitor": "yes | no | unclear",
  "sells_to_lindner": "yes | no | unclear",
  "key_signal": "<stärkstes konkretes Bedarfssignal, max 10 Wörter, oder 'none'>",
  "reason": "<1 knapper Satz>"
}
Regel: Wenn is_competitor = yes ODER sells_to_lindner = yes, dann fit_tier = C.

Firma: {{company_name}}
Domain: {{domain}}
```

### Find-People-Jobtitel (eine Zeile → Clay)
```
Geschäftsführer, Managing Director, Werkleiter, Plant Manager, Plant Director, Standortleiter, Technischer Leiter, Technical Director, Head of Technology, Technischer Geschäftsführer, Production Manager, Produktionsleiter, Head of Production, Alternative Fuels Manager, Leiter Alternative Brennstoffe, Kiln Manager, Leiter Verfahrenstechnik, Process Manager, Operations Manager, Head of Operations, Betriebsleiter, Anlagenleiter, Leiter Instandhaltung, Maintenance Manager, Energy Manager
```
Tier 1 (Entscheider): Geschäftsführer/Managing Director, Werkleiter/Plant Manager, Standortleiter, Technischer Geschäftsführer. — Tier 2 (technisch/operativ): Technischer Leiter, Alternative Fuels Manager / Leiter Alternative Brennstoffe, Leiter Verfahrenstechnik, Kiln/Process Manager, Produktionsleiter, Instandhaltung.

---

## Playbook 261 – Wood & Biomass Recyclers

### Clay-Sculptor-Prompt
```
Du bist ein B2B-Sales-Researcher. Du bewertest, ob die unten genannte Firma einen ECHTEN Bedarf für die Holz-/Biomasse-Schredder und Schneidsysteme von LINDNER (lindner.com) hat.

PRODUKT LINDNER: Schredder und wechselbare Schneidsysteme für Altholz-Vorzerkleinerung und Feinzerkleinerung sowie Biomasse (mobile Urraco EVO, stationäre Polaris/Jupiter). Definierte Endkorngröße je Verwertungsweg, störstoffresistent, energieeffizient.

ECHTER BEDARF besteht NUR, wenn die Firma:
- Altholz oder holzartige Biomasse AUFBEREITET/ZERKLEINERT, d.h. Altholzrecycler/-aufbereiter, Spanplatten-/MDF-/Holzwerkstoffhersteller (Recyclingholz als Rohstoff), Biomasse-Heiz(kraft)werk/Bioenergie mit Holzbrennstoff, Pellet-/Hackschnitzelproduzent, Sägewerk/Holzverarbeitung mit Rest-/Altholzzerkleinerung, oder Grün-/Gartenabfall-Holzrecycler.

KEIN Bedarf (Tier C): Hersteller/Händler von Zerkleinerern/Hackern (Wettbewerber); reine Möbel-/Fenster-/Türen-/Parkett-/Bodenbelag-Hersteller und Holzbau/Zimmerei (Fertighaus) – das sind Holz-VERWENDER, keine -Zerkleinerer; reine Holzhändler/-importeure; reine Forst-/Logging-Betriebe ohne Zerkleinerung; Software/IT; reine Solar-/Windentwickler.

ZUSÄTZLICHE PFLICHTPRÜFUNG (immer durchführen):
(a) BEDARF BESTÄTIGEN: Belege, dass die Firma Holz/Biomasse SELBST zerkleinert/aufbereitet ODER Recyclingholz/Holzbrennstoff im Prozess einsetzt (Altholz, Hackschnitzel, Spanplatte, Biomassekessel). Reiner Holz-Endprodukt-Hersteller (Möbel/Fenster/Türen/Parkett/Fertighaus) oder Holzhändler → Tier C. Kein belegbarer Zerkleinerungs-/Aufbereitungsbezug → höchstens Tier B, im Zweifel C.
(b) WETTBEWERBER/ZULIEFERER AUSSCHLIESSEN: Prüfe, ob die Firma (i) ein WETTBEWERBER ist (Hersteller/Händler von Schredder-, Hacker-, Zerkleinerungs- oder Holzbearbeitungsmaschinen – z. B. Ledinek, Springer Maschinenfabrik, Uniforest) ODER (ii) ein ZULIEFERER, der etwas AN Lindner verkaufen will (Maschinen-/Anlagenbau, Engineering/Ingenieurbüro, Krantechnik, Hydraulik, Antriebe, Fördertechnik, Stahlbau, Ersatzteile). Trifft (i) ODER (ii) zu → IMMER fit_tier C.

VORGEHEN:
1. Besuche https://{{domain}} (Startseite, „Produkte/Leistungen", „Altholz"/„Biomasse"/„Anlagen", „Über uns").
2. Bestimme, ob die Firma Holz/Biomasse SELBST zerkleinert/aufbereitet oder als Brennstoff/Rohstoff einsetzt.
3. Achte auf Bedarfssignale: Altholzklassen A1–A4, eigene Zerkleinerung/Schredder, Spanplatten-/Werkstoffproduktion, Biomassekessel/Heizkraftwerk, Pellet-/Hackschnitzeloutput, ENplus, Durchsatz in t/Jahr.
4. Prüfe die Doppelprüfung (a)+(b) oben.

GIB GENAU DIESES JSON ZURÜCK (nichts anderes):
{
  "fit_tier": "A | B | C",
  "has_need": "yes | no | unclear",
  "processes_wood_biomass": "yes | no | unclear",
  "is_competitor": "yes | no | unclear",
  "sells_to_lindner": "yes | no | unclear",
  "key_signal": "<stärkstes konkretes Bedarfssignal, max 10 Wörter, oder 'none'>",
  "reason": "<1 knapper Satz>"
}
Regel: Wenn is_competitor = yes ODER sells_to_lindner = yes, dann fit_tier = C.

Firma: {{company_name}}
Domain: {{domain}}
```

### Find-People-Jobtitel (eine Zeile → Clay)
```
Geschäftsführer, Managing Director, Inhaber, Owner, Werkleiter, Standortleiter, Plant Manager, Betriebsleiter, Operations Manager, Head of Operations, Technischer Leiter, Technical Director, Head of Technology, Technischer Geschäftsführer, Produktionsleiter, Production Manager, Anlagenleiter, Leiter Aufbereitung, Leiter Holzaufbereitung, Prozessleiter, Leiter Instandhaltung, Maintenance Manager, Leiter Technik, Head of Biomass, Werksleiter Sägewerk
```
Tier 1 (Entscheider): Geschäftsführer/Managing Director, Inhaber/Owner, Werkleiter, Standortleiter. — Tier 2 (technisch/operativ): Technischer Leiter, Betriebsleiter, Produktionsleiter, Anlagenleiter, Leiter (Holz-)Aufbereitung, Instandhaltung.
