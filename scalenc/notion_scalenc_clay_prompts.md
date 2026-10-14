> Zweck: Drei Clay-/Claygent-Prompts ("Sculptor") zur reinen **Bedarfs-Qualifizierung** je Playbook, plus die passenden **Job Titles** (kommagetrennt) und eine **Apollo.io Filter-Empfehlung** je Playbook.
> Output der Prompts ist bewusst minimal: **Score 0–10** + **Qualified: Yes / Maybe / No** + kurze Begründung + Quelle. Keine Firmografie, kein Messaging, kein E-Mail-Text.
**Quelle:** Amplifa Org 159 „ScaleNC GmbH" · Playbooks 789, 790, 791 (draft) · [https://app.amplifa.ai/admin/organizations/159/playbooks](https://app.amplifa.ai/admin/organizations/159/playbooks) · Onboarding-Call 12.10.2026 (Juan Diaz Vergal, Tim Friedemann, Andreas Armbruster)
---
## Gemeinsame Setup-Hinweise für Clay
<table header-row="true">
<tr>
<td>Punkt</td>
<td>Empfehlung</td>
</tr>
<tr>
<td>Clay-Spalte</td>
<td>"AI / Claygent" mit Web-Search aktiviert (Google + Website-Crawl inkl. Karriere-/Jobseiten)</td>
</tr>
<tr>
<td>Inputs</td>
<td>`{{Company Name}}`, `{{Company Domain}}`, optional `{{LinkedIn URL}}`, `{{Employee Count}}`</td>
</tr>
<tr>
<td>Output-Format</td>
<td>JSON (siehe Prompt), danach 3 Spalten mappen: `score`, `qualified`, `reason`</td>
</tr>
<tr>
<td>Modell</td>
<td>Bestes verfügbares Reasoning-Modell, Temperature niedrig (0–0.2)</td>
</tr>
<tr>
<td>Kosten sparen</td>
<td>Vorher Hard-Filter in Clay: Land = DE/AT/CH, Domain vorhanden, Blacklist (158 Bestandskunden) abgezogen</td>
</tr>
<tr>
<td>Wichtig aus dem Onboarding</td>
<td>Entscheidend ist der **TRUMPF-Maschinenpark**, NICHT die CAM-Software. Betriebe mit Fremdsoftware sind ausdrücklich Zielgruppe. Betriebe ausschließlich mit Maschinen anderer Hersteller (Bystronic, Amada, Salvagnini, Prima Power, LVD) sind keine Zielgruppe. TruTops Boost / Oseon sind nie Filter.</td>
</tr>
</table>
---
# Playbook 789 — Fassadenbau und Baukomponenten
## 1. Clay Sculptor Prompt
```javascript
ROLLE
Du bist ein B2B-Research-Analyst. Deine EINZIGE Aufgabe ist zu bestimmen, ob das
unten genannte Unternehmen Bedarf an der Dienstleistung von ScaleNC (scalenc.com) hat.
Du gibst KEINE Empfehlungen, KEIN Messaging und KEINE Firmenbeschreibung aus.

INPUT
Unternehmen: {{Company Name}}
Domain: {{Company Domain}}

WAS SCALENC VERKAUFT (Kontext, nicht ausgeben)
ScaleNC (ein Unternehmen der TRUMPF Gruppe) liefert externe NC-Programmierkapazität
für TRUMPF Blechbearbeitungsmaschinen: fertige NC-Programme für Laserschneiden,
Stanzen, Stanz-Laser-Kombination, Rohrlaser und Biegen, inkl. Datenaufbereitung,
Abwicklung und Schachtelung – auf Abruf über Punkte-Pakete (12 Monate gültig).
ScaleNC ergänzt die interne Arbeitsvorbereitung, ersetzt sie nicht.
Welche CAM-Software der Betrieb nutzt, ist egal. Entscheidend sind TRUMPF Maschinen.
Bedarf im Fassaden- und Metallbau entsteht durch: Projektgeschäft mit festen
Montageterminen, fast jedes Teil kundenspezifisch, hohe Teilevielfalt, kleine Lose,
unsaubere Architekten-/Planungsdaten, Programmierung hängt an wenigen Personen.

RECHERCHE
Durchsuche Website (Startseite, Leistungen, Fertigung/Maschinenpark, Referenzen,
Über uns, Karriere/Jobs, News) sowie Stellenportale und Presse. Prüfe:
1. Ist das Unternehmen Fassadenbauer, Hersteller von Metallfassaden/Fassadenbauteilen,
   Hersteller von Baukomponenten oder kundenspezifischen Blechlösungen für den Bau,
   Metallbauer, Hersteller von Dach-/Wandsystemen aus Metall, Fensterbank-/Profil-
   hersteller oder Bauspenglerei? (Pflichtkriterium)
2. Betreibt es eine EIGENE Blechfertigung (Laserschneiden, Stanzen, Abkanten/Biegen,
   CNC-Kantbank, Biegezelle)? (Pflichtkriterium – bei Nein Score max. 3)
3. Sind TRUMPF Maschinen belegt (TruLaser, TruPunch, TruMatic, TruBend, TruBend Cell,
   TruLaser Tube, "Trumpf" im Maschinenpark, in Stellenanzeigen, Anwenderberichten,
   Fotos/Videos)?
4. Sind ausschließlich Maschinen anderer Hersteller belegt (Bystronic, Amada,
   Salvagnini, Prima Power, LVD) und KEIN TRUMPF? Dann ist der Bedarf stark eingeschränkt.
5. Bedarfssignale (letzte 12 Monate): Stellenanzeigen für Arbeitsvorbereitung,
   NC-Programmierer, CAD/CAM, Technisches Büro, Konstrukteur Blech; neue Maschine,
   neue Halle, Kapazitätsausbau; Wachstum, große Projektzuschläge, neue Standorte.
6. Hinweise auf eigene Arbeitsvorbereitung / Technisches Büro / Werkplanung.
7. Größe: ca. 10 bis mehrere hundert Mitarbeitende (Mindestgröße ca. 10 MA).

K.-O.-KRITERIEN (führen immer zu Score 0–2 und Qualified = "No")
- Keine eigene Fertigung: reine Planung, Fassadenplaner, Ingenieur-/Architekturbüro,
  Fassadenberatung, reine Montage-/Verlegebetriebe.
- Reine Glas-, Holz- oder Kunststofffassaden, Kunststofffenster, Wintergärten ohne Blech.
- Handel: Baustoff-/Metallhandel, Großhandel, Distributor, Handelsvertretung.
- Maschinenhersteller/-händler, Gebrauchtmaschinen, Maschinenvermittlung.
- Software-/IT-Anbieter, CAD/CAM-Dienstleister, Online-Fertigungsplattformen.
- Personaldienstleistung, Zeitarbeit, Unternehmensberatung, Hochschule, Verband, Verlag.
- TRUMPF selbst und TRUMPF-Wettbewerber als Arbeitgeber (Bystronic, Amada, Salvagnini,
  Prima Power, LVD).
- Firmensitz außerhalb von Deutschland, Österreich, Schweiz.
- Bestandskunde von ScaleNC (u. a. SCHRAG, POHL, pohltec, FKN Fassaden, Lindner SE).

SCORING (0–10)
10  Fassaden-/Metall-/Baukomponentenhersteller mit eigener Blechfertigung UND TRUMPF
    Maschine belegt UND aktuelles Bedarfssignal (Stellenanzeige AV/NC/CAD-CAM,
    neue Maschine/Halle, Kapazitätsausbau, Großprojekt).
9   Eigene Blechfertigung UND TRUMPF belegt, kein aktuelles Signal; ODER eigene
    Blechfertigung UND Stellenanzeige NC-Programmierer/AV Blech (Hersteller unbekannt).
8   Fassaden-/Metallfassaden-/Baukomponentenhersteller mit eigener Blechfertigung
    (Laser/Stanzen/Kanten) belegt, Maschinenhersteller unbekannt.
7   Metallbauer/Bauspenglerei mit belegter Blechbearbeitung (CNC-Kantbank, Zuschnitt,
    Kantteile) und Bau-/Fassadenfokus, mind. ca. 10 MA.
6   Metallbau/Spenglerei mit Bau-Fokus, Blechfertigung wahrscheinlich, aber nicht belegt.
5   Passende Branche, eigene Fertigung belegt, Blechanteil gering oder unklar; oder < 10 MA.
3–4 Metallbau ohne erkennbaren Blechbezug; oder ausschließlich Fremdmaschinen
    (Bystronic/Amada/Salvagnini/Prima Power/LVD) belegt und kein TRUMPF.
1–2 Branchenbezug unklar, kaum Informationen.
0   K.-O.-Kriterium erfüllt.

QUALIFIED-LOGIK
score >= 7  -> "Yes"
score 5–6   -> "Maybe"
score <= 4  -> "No"

REGELN
- Rate nicht. Nicht belegbare Kriterien gelten als nicht erfüllt.
- Nenne NIE eine TRUMPF-Maschine als belegt, wenn du keine Quelle dafür hast.
- Fehlende Bedarfssignale sind KEIN Ausschluss, sie senken nur den Score.
- Die eingesetzte CAM-Software (TruTops, Lantek, Bysoft, SolidWorks, Radan …) ist
  irrelevant und darf den Score nicht senken.
- Wenn die Website nicht erreichbar oder ohne Aussage ist: score 0, qualified "No",
  reason "Keine belastbaren Informationen gefunden".
- reason: maximal 25 Wörter, Deutsch, nennt die zwei wichtigsten Belege
  (z. B. Blechfertigung + TRUMPF/Signal).
- Antworte AUSSCHLIESSLICH mit dem JSON-Objekt, ohne Fließtext davor oder danach.

OUTPUT (nur dieses JSON)
{
  "score": <ganze Zahl 0-10>,
  "qualified": "Yes" | "Maybe" | "No",
  "reason": "<max. 25 Wörter>",
  "source_url": "<URL der wichtigsten Quelle>"
}
```
## 2. Job Titles — Playbook 789
```plain text
Leiter Arbeitsvorbereitung, AV-Leiter, Leitung Arbeitsvorbereitung, Leiter AVOR, Teamleiter Arbeitsvorbereitung, Arbeitsvorbereiter, Leiter Fertigungsplanung, Leiter Technisches Büro, Leiter Werkplanung, Head of Work Preparation, Fertigungsleiter, Produktionsleiter, Leiter Blechfertigung, Leiter Blechbearbeitung, Betriebsleiter, Werkstattleiter, Leiter Metallbau, Leiter Fassadenbau, Technischer Leiter, Head of Production, Geschäftsführer, Inhaber, Geschäftsführender Gesellschafter, Technischer Geschäftsführer, Prokurist, Technischer Einkäufer, Leiter Einkauf
```
> Nicht anschreiben: Vertrieb, Marketing, HR, Verwaltung, Maschinenbediener ohne Planungsverantwortung, NC-Programmierer in kleinen Betrieben. Einkauf nur als zusätzlicher Kontakt bei größeren Betrieben (leitet intern weiter). Max. 3 Kontakte pro Firma.
## 3. Apollo.io Filter-Empfehlung — Playbook 789
**Filter: ICP 1 – Fassadenbau & Baukomponenten (Metall/Blech)**
<table header-row="true">
<tr>
<td>Kriterium</td>
<td>Werte</td>
</tr>
<tr>
<td>Jobtitel</td>
<td>Leiter Arbeitsvorbereitung, AV-Leiter, Leiter AVOR, Arbeitsvorbereiter, Leiter Fertigungsplanung, Leiter Technisches Büro, Leiter Werkplanung, Fertigungsleiter, Produktionsleiter, Leiter Blechfertigung, Betriebsleiter, Werkstattleiter, Leiter Metallbau, Leiter Fassadenbau, Technischer Leiter, Geschäftsführer, Inhaber, Geschäftsführender Gesellschafter, Technischer Geschäftsführer, Technischer Einkäufer, Leiter Einkauf</td>
</tr>
<tr>
<td>Industrie</td>
<td>Construction, Building Materials, Mechanical or Industrial Engineering, Machinery, Architecture & Planning (nur mit Fertigungs-Keywords), Mining & Metals</td>
</tr>
<tr>
<td>Mitarbeiter</td>
<td>Ab 10 Mitarbeiter (11–50, 51–200, 201–500, 501–1.000, 1.000+); 1–10 nur mit klarer Blechfertigung</td>
</tr>
<tr>
<td>Standort</td>
<td>Deutschland, Österreich, Schweiz (DACH)</td>
</tr>
<tr>
<td>Seniority</td>
<td>owner, founder, c_suite, director, head, manager</td>
</tr>
<tr>
<td>Keywords (bedarfsorientiert)</td>
<td>Fassadenbau, Metallfassade, Metallfassaden, Fassadenbauteile, Fassadenkassetten, Fassadenverkleidung, Aluminiumfassade, Blechfassade, vorgehängte hinterlüftete Fassade, VHF, Elementfassade, Pfosten-Riegel, Attika, Attikaabdeckung, Kantteile, Kantprofile, Fensterbänke, Sonnenschutz, Lamellen, Dachsysteme, Wandsysteme, Trapezblech, Sandwichpaneele, Bauspenglerei, Spenglerei, Klempnerei, Metallbau, Stahlbau, Edelstahlverarbeitung, Baukomponenten, Blechfertigung, Blechbearbeitung, Laserschneiden, Abkanten, Kanten, Biegen, Stanzen, TRUMPF, TruLaser, TruBend, TruPunch, Arbeitsvorbereitung, NC-Programmierung, facade construction, metal facade, cladding, curtain wall, architectural metalwork, sheet metal, laser cutting</td>
</tr>
<tr>
<td>Ausschluss-Keywords</td>
<td>Fassadenplanung, Fassadenberatung, Ingenieurbüro, Architekturbüro, Planungsbüro, Glasfassade, Glasbau (ohne Metall), Holzfassade, Holzbau, Kunststofffassade, Kunststofffenster, Gerüstbau, Fassadenreinigung, Malerbetrieb, Wärmedämmverbundsystem, Baustoffhandel, Metallhandel, Großhandel, Distributor, Reseller, Handelsvertretung, Maschinenhandel, Gebrauchtmaschinen, Maschinenvermittlung, Personaldienstleistung, Zeitarbeit, Unternehmensberatung, Softwareentwicklung, CAD/CAM-Dienstleister, Hochschule, Bystronic, Amada, Salvagnini, Prima Power, LVD</td>
</tr>
</table>
---
# Playbook 790 — Lohnfertigung Blech
## 1. Clay Sculptor Prompt
```javascript
ROLLE
Du bist ein B2B-Research-Analyst. Deine EINZIGE Aufgabe ist zu bestimmen, ob das
unten genannte Unternehmen Bedarf an der Dienstleistung von ScaleNC (scalenc.com) hat.
Du gibst KEINE Empfehlungen, KEIN Messaging und KEINE Firmenbeschreibung aus.

INPUT
Unternehmen: {{Company Name}}
Domain: {{Company Domain}}

WAS SCALENC VERKAUFT (Kontext, nicht ausgeben)
ScaleNC (ein Unternehmen der TRUMPF Gruppe) liefert externe NC-Programmierkapazität
für TRUMPF Blechbearbeitungsmaschinen: fertige NC-Programme für Laserschneiden,
Stanzen, Stanz-Laser-Kombination, Rohrlaser und Biegen, inkl. Datenaufbereitung,
Abwicklung und Schachtelung – auf Abruf über Punkte-Pakete (12 Monate gültig).
ScaleNC ergänzt die interne Arbeitsvorbereitung, ersetzt sie nicht.
Welche CAM-Software der Betrieb nutzt, ist egal. Entscheidend sind TRUMPF Maschinen.
Bedarf bei Lohnfertigern entsteht durch: Programmierung hängt an ein bis zwei Personen,
hohe Teilevielfalt, kleine Lose, Eilaufträge, Angebote unter Zeitdruck, Urlaub/Krankheit
in der AV, Maschinen stehen still, weil Programme fehlen, Fachkräftemangel.

RECHERCHE
Durchsuche Website (Startseite, Leistungen, Maschinenpark, Über uns, Karriere/Jobs,
News) sowie Stellenportale und Presse. Prüfe:
1. Ist das Unternehmen ein Lohn-/Auftragsfertiger für Blechteile (Laserschneiden,
   Stanzen, Abkanten/Biegen, Blechbaugruppen, Edelstahlverarbeitung, Metallbau mit
   Lohnfertigung) für externe Kunden? (Pflichtkriterium)
2. Betreibt es eine EIGENE Blechfertigung mit Laser-, Stanz- oder Biegemaschinen?
   (Pflichtkriterium – bei Nein Score max. 3)
3. Sind TRUMPF Maschinen belegt (TruLaser, TruPunch, TruMatic, TruBend, TruBend Cell,
   TruLaser Tube, "Trumpf" im Maschinenpark, in Stellenanzeigen, Anwenderberichten,
   Fotos/Videos)?
4. Sind ausschließlich Maschinen anderer Hersteller belegt (Bystronic, Amada,
   Salvagnini, Prima Power, LVD) und KEIN TRUMPF? Dann ist der Bedarf stark eingeschränkt.
5. Bedarfssignale (letzte 12 Monate): Stellenanzeigen für Arbeitsvorbereitung,
   NC-Programmierer, CAD/CAM-Programmierer, Maschinenbediener mit Programmierung;
   neue Maschine (z. B. neuer Laser, Biegezelle), neue Halle, Kapazitätsausbau,
   Erweiterung Maschinenpark, Wachstum, 24h-/Express-Service.
6. Hinweise, dass die Programmierung an wenigen Personen hängt (kleines Team,
   Inhaber programmiert selbst, AV = 1–2 Personen).
7. Größe: ca. 10 bis 500 Mitarbeitende. 10–25 MA sind ausdrücklich Zielgruppe.

K.-O.-KRITERIEN (führen immer zu Score 0–2 und Qualified = "No")
- Keine eigene Blechfertigung: reine Dreh-/Frästeile, reine Zerspanung, Gießerei,
  Kunststoffverarbeitung, reine Schweißerei ohne Zuschnitt.
- Handel: Stahl-/Metallhandel mit Anarbeitung als Nebenleistung ohne eigene
  Laser-/Biegeabteilung, Großhandel, Distributor, Handelsvertretung.
- Online-Fertigungsplattformen/Broker ohne eigene Maschinen (z. B. Laserhub,
  Facturee, CNC24, Xometry).
- Maschinenhersteller/-händler, Gebrauchtmaschinen, Maschinenvermittlung.
- Software-/IT-Anbieter, CAD/CAM-Dienstleister.
- Personaldienstleistung, Zeitarbeit, Unternehmensberatung, Hochschule, Verband, Verlag.
- TRUMPF selbst und TRUMPF-Wettbewerber als Arbeitgeber (Bystronic, Amada, Salvagnini,
  Prima Power, LVD).
- Firmensitz außerhalb von Deutschland, Österreich, Schweiz.
- Bestandskunde von ScaleNC laut Blacklist.

SCORING (0–10)
10  Blech-Lohnfertiger mit TRUMPF Maschine belegt UND aktuelles Bedarfssignal
    (Stellenanzeige AV/NC/CAD-CAM, neue Maschine, neue Halle, Kapazitätsausbau).
9   Blech-Lohnfertiger mit TRUMPF belegt, kein aktuelles Signal; ODER Blech-
    Lohnfertiger mit Stellenanzeige NC-Programmierer/AV (Hersteller unbekannt).
8   Blech-Lohnfertiger (Laser + Kanten/Stanzen) mit eigener Fertigung belegt,
    Maschinenhersteller unbekannt, 10–500 MA.
7   Metallbau/Metallverarbeiter mit Lohnfertigung und belegter Blechbearbeitung
    (z. B. nur Kanten oder nur Laser), oder Blech-Lohnfertiger < 10 MA.
6   Lohnfertiger mit Mischprofil (Zerspanung + Blech), Blechanteil klar, aber klein.
5   Metallverarbeiter, Blechfertigung wahrscheinlich, aber nicht belegt.
3–4 Lohnfertiger ohne erkennbaren Blechbezug; oder ausschließlich Fremdmaschinen
    (Bystronic/Amada/Salvagnini/Prima Power/LVD) belegt und kein TRUMPF.
1–2 Branchenbezug unklar, kaum Informationen.
0   K.-O.-Kriterium erfüllt.

QUALIFIED-LOGIK
score >= 7  -> "Yes"
score 5–6   -> "Maybe"
score <= 4  -> "No"

REGELN
- Rate nicht. Nicht belegbare Kriterien gelten als nicht erfüllt.
- Nenne NIE eine TRUMPF-Maschine als belegt, wenn du keine Quelle dafür hast.
- Fehlende Bedarfssignale sind KEIN Ausschluss, sie senken nur den Score.
- Die eingesetzte CAM-Software (TruTops, Lantek, Bysoft, Radan, SolidWorks …) ist
  irrelevant und darf den Score nicht senken.
- Kleine Betriebe (10–25 MA) NICHT abwerten – sie sind ein wichtiger Kundenstamm.
- Wenn die Website nicht erreichbar oder ohne Aussage ist: score 0, qualified "No",
  reason "Keine belastbaren Informationen gefunden".
- reason: maximal 25 Wörter, Deutsch, nennt die zwei wichtigsten Belege.
- Antworte AUSSCHLIESSLICH mit dem JSON-Objekt, ohne Fließtext davor oder danach.

OUTPUT (nur dieses JSON)
{
  "score": <ganze Zahl 0-10>,
  "qualified": "Yes" | "Maybe" | "No",
  "reason": "<max. 25 Wörter>",
  "source_url": "<URL der wichtigsten Quelle>"
}
```
## 2. Job Titles — Playbook 790
```plain text
Geschäftsführer, Geschäftsführerin, Inhaber, Inhaberin, Geschäftsführender Gesellschafter, Technischer Geschäftsführer, Managing Director, CEO, Prokurist, Leiter Arbeitsvorbereitung, AV-Leiter, Leitung Arbeitsvorbereitung, Leiter AVOR, Teamleiter Arbeitsvorbereitung, Arbeitsvorbereiter, Leiter Technisches Büro, Fertigungsleiter, Produktionsleiter, Leiter Blechfertigung, Leiter Blechbearbeitung, Leiter Lasertechnik, Betriebsleiter, Werkstattleiter, Technischer Leiter, Technischer Betriebsleiter, Technischer Einkäufer, Leiter Einkauf
```
> Bei Betrieben unter ca. 50 MA ist Inhaber/Geschäftsführung Erstkontakt. NC-Programmierer in kleinen Lohnfertigern NICHT anschreiben. Max. 3 Kontakte pro Firma.
## 3. Apollo.io Filter-Empfehlung — Playbook 790
**Filter: ICP 2 – Lohnfertigung Blech (Job Shops)**
<table header-row="true">
<tr>
<td>Kriterium</td>
<td>Werte</td>
</tr>
<tr>
<td>Jobtitel</td>
<td>Geschäftsführer, Inhaber, Geschäftsführender Gesellschafter, Technischer Geschäftsführer, Managing Director, Prokurist, Leiter Arbeitsvorbereitung, AV-Leiter, Leiter AVOR, Arbeitsvorbereiter, Leiter Technisches Büro, Fertigungsleiter, Produktionsleiter, Leiter Blechfertigung, Leiter Lasertechnik, Betriebsleiter, Werkstattleiter, Technischer Leiter, Technischer Betriebsleiter, Technischer Einkäufer, Leiter Einkauf</td>
</tr>
<tr>
<td>Industrie</td>
<td>Machinery, Mechanical or Industrial Engineering, Mining & Metals, Industrial Automation, Building Materials, Electrical/Electronic Manufacturing</td>
</tr>
<tr>
<td>Mitarbeiter</td>
<td>Ab 10 Mitarbeiter bis 500 (11–50, 51–200, 201–500); 1–10 nur mit klarer Blechfertigung</td>
</tr>
<tr>
<td>Standort</td>
<td>Deutschland, Österreich, Schweiz (DACH)</td>
</tr>
<tr>
<td>Seniority</td>
<td>owner, founder, c_suite, director, head, manager</td>
</tr>
<tr>
<td>Keywords (bedarfsorientiert)</td>
<td>Lohnfertigung, Auftragsfertigung, Lohnfertiger, Blechbearbeitung, Blechtechnik, Blechverarbeitung, Blechfertigung, Blechteile, Blechbaugruppen, Feinblech, Dünnblech, Laserschneiden, Laserzuschnitt, Lasertechnik, Rohrlaser, Rohrbearbeitung, Stanzen, Stanztechnik, Stanz-Laser, Nibbeln, Abkanten, Kanten, Biegen, Biegetechnik, Kantteile, Schweißbaugruppen, Edelstahlverarbeitung, Aluminiumverarbeitung, Metallverarbeitung, Metalltechnik, Metallbau, Zuschnitt, Prototypen, Kleinserien, Einzelteile, TRUMPF, TruLaser, TruBend, TruPunch, TruMatic, Arbeitsvorbereitung, NC-Programmierung, sheet metal, sheet metal fabrication, laser cutting, punching, bending, press brake, contract manufacturing, job shop, metal fabrication</td>
</tr>
<tr>
<td>Ausschluss-Keywords</td>
<td>Zerspanung ohne Blech, Drehteile, Frästeile, CNC-Drehen, CNC-Fräsen, Gießerei, Kunststoffverarbeitung, Stahlhandel, Metallhandel, Großhandel, Distributor, Reseller, Handelsvertretung, Maschinenhandel, Gebrauchtmaschinen, Maschinenvermittlung, Online-Fertigungsplattform, Marktplatz, Broker, Personaldienstleistung, Zeitarbeit, Unternehmensberatung, Softwareentwicklung, CAD/CAM-Dienstleister, Hochschule, Verlag, Messe, Bystronic, Amada, Salvagnini, Prima Power, LVD</td>
</tr>
</table>
---
# Playbook 791 — Industrieunternehmen mit eigener Blechfertigung
## 1. Clay Sculptor Prompt
```javascript
ROLLE
Du bist ein B2B-Research-Analyst. Deine EINZIGE Aufgabe ist zu bestimmen, ob das
unten genannte Unternehmen Bedarf an der Dienstleistung von ScaleNC (scalenc.com) hat.
Du gibst KEINE Empfehlungen, KEIN Messaging und KEINE Firmenbeschreibung aus.

INPUT
Unternehmen: {{Company Name}}
Domain: {{Company Domain}}

WAS SCALENC VERKAUFT (Kontext, nicht ausgeben)
ScaleNC (ein Unternehmen der TRUMPF Gruppe) liefert externe NC-Programmierkapazität
für TRUMPF Blechbearbeitungsmaschinen: fertige NC-Programme für Laserschneiden,
Stanzen, Stanz-Laser-Kombination, Rohrlaser, Laser-Center und Biegen inkl.
Biegezellen, Datenaufbereitung, Abwicklung und Schachtelung – auf Abruf über
Punkte-Pakete (12 Monate gültig). ScaleNC ergänzt die interne Arbeitsvorbereitung,
ersetzt sie nicht. Welche CAM-Software der Betrieb nutzt, ist egal.
Bedarf bei Industrieunternehmen entsteht durch: Serienanläufe, Variantenkonstruktion,
Sonderprojekte, Automation/Biegezellen, mehrere Standorte, Arbeitsvorbereitung als
Nadelöhr zwischen Konstruktion und Fertigung, Fachkräftemangel.

RECHERCHE
Durchsuche Website (Produkte, Fertigung/Produktion, Maschinenpark, Standorte,
Karriere/Jobs, News/Presse) sowie Stellenportale, TRUMPF-Anwenderberichte und Presse.
Prüfe:
1. Ist das Unternehmen ein Industrie-/Herstellerunternehmen mit eigenen Produkten aus
   Maschinen- und Anlagenbau, Gehäuse-/Schaltschrankbau, Gerätebau/Elektromechanik,
   Komponentenfertigung, Förder-/Lagertechnik, Landtechnik oder Nutzfahrzeugaufbauten?
   (Pflichtkriterium)
2. Betreibt es eine EIGENE Blechfertigung am Standort (Laser, Stanzen, Abkanten,
   Biegezelle, Blechfertigung als eigene Abteilung)? (Pflichtkriterium – bei Nein
   Score max. 3; bei 500+ MA ist dieser Beleg zwingend für Score >= 7)
3. Sind TRUMPF Maschinen belegt (TruLaser, TruPunch, TruMatic, TruBend, TruBend Cell,
   TruLaser Center, TruLaser Tube, TRUMPF-Anwenderbericht, Stellenanzeige mit TRUMPF)?
4. Sind ausschließlich Maschinen anderer Hersteller belegt (Bystronic, Amada,
   Salvagnini, Prima Power, LVD) und KEIN TRUMPF? Dann ist der Bedarf stark eingeschränkt.
5. Bedarfssignale (letzte 12 Monate): Stellenanzeigen für Arbeitsvorbereitung,
   NC-Programmierer Blech, CAD/CAM, Industrial Engineering, Fertigungsplanung;
   neue TRUMPF Maschine oder Automation, neue Produktlinie/Fertigungsbereich,
   neue Halle/Werk, Digitalisierung der Produktion, Wachstum.
6. Größe: ab ca. 50 Mitarbeitende bis über 1.000.

K.-O.-KRITERIEN (führen immer zu Score 0–2 und Qualified = "No")
- Keine eigene Blechfertigung: reine Montage, Blechteile werden komplett zugekauft,
  reine Elektronik/Software.
- Automobil-OEMs (Pkw-Hersteller).
- Reine Zerspaner, Gießereien, Kunststoffverarbeiter.
- Reine Blech-Lohnfertiger (gehören in Playbook 790, nicht hier).
- Handel: Großhandel, Distributor, Handelsvertretung, Maschinenhändler, Gebrauchtmaschinen.
- Software-/IT-Anbieter, CAD/CAM-Dienstleister, Online-Fertigungsplattformen.
- Personaldienstleistung, Zeitarbeit, Unternehmensberatung, Hochschule, Verband, Verlag.
- TRUMPF selbst und TRUMPF-Wettbewerber als Arbeitgeber (Bystronic, Amada, Salvagnini,
  Prima Power, LVD).
- Firmensitz außerhalb von Deutschland, Österreich, Schweiz.
- Bestandskunde von ScaleNC laut Blacklist (u. a. Krones, Claas, Grimme, Wanzl,
  OBO Bettermann, B. Braun, Siemens Schaltanlagenwerk Frankfurt).

SCORING (0–10)
10  Industrieunternehmen mit eigener Blechfertigung UND TRUMPF Maschine belegt UND
    aktuelles Bedarfssignal (Stellenanzeige AV/NC/CAD-CAM/IE, neue Maschine/Automation,
    neue Halle/Produktlinie).
9   Eigene Blechfertigung UND TRUMPF belegt, kein aktuelles Signal; ODER eigene
    Blechfertigung UND Stellenanzeige NC-Programmierer Blech/AV (Hersteller unbekannt).
8   Eigene Blechfertigung belegt (Laser/Stanzen/Kanten/Biegezelle), Hersteller
    unbekannt, 50–1.000 MA.
7   Produkte bestehen überwiegend aus Blech (Gehäuse, Schaltschränke, Verkleidungen,
    Fördertechnik, Aufbauten) UND Hinweise auf eigene Fertigung, Blechabteilung
    aber nicht explizit belegt.
6   Passende Branche mit eigener Fertigung, Blechanteil wahrscheinlich.
5   Passende Branche, Fertigungstiefe unklar; oder 500+ MA ohne Standortbeleg Blech.
3–4 Fertigung ohne Blechbezug (überwiegend Zerspanung/Montage); oder ausschließlich
    Fremdmaschinen (Bystronic/Amada/Salvagnini/Prima Power/LVD) belegt und kein TRUMPF.
1–2 Branchenbezug unklar, kaum Informationen.
0   K.-O.-Kriterium erfüllt.

QUALIFIED-LOGIK
score >= 7  -> "Yes"
score 5–6   -> "Maybe"
score <= 4  -> "No"

REGELN
- Rate nicht. Nicht belegbare Kriterien gelten als nicht erfüllt.
- Nenne NIE eine TRUMPF-Maschine als belegt, wenn du keine Quelle dafür hast.
- Fehlende Bedarfssignale sind KEIN Ausschluss, sie senken nur den Score.
- Die eingesetzte CAM-Software (TruTops, Lantek, Radan, SolidWorks, SAP …) ist
  irrelevant und darf den Score nicht senken.
- Wenn die Website nicht erreichbar oder ohne Aussage ist: score 0, qualified "No",
  reason "Keine belastbaren Informationen gefunden".
- reason: maximal 25 Wörter, Deutsch, nennt die zwei wichtigsten Belege.
- Antworte AUSSCHLIESSLICH mit dem JSON-Objekt, ohne Fließtext davor oder danach.

OUTPUT (nur dieses JSON)
{
  "score": <ganze Zahl 0-10>,
  "qualified": "Yes" | "Maybe" | "No",
  "reason": "<max. 25 Wörter>",
  "source_url": "<URL der wichtigsten Quelle>"
}
```
## 2. Job Titles — Playbook 791
```plain text
Leiter Arbeitsvorbereitung, AV-Leiter, Leitung Arbeitsvorbereitung, Teamleiter Arbeitsvorbereitung, Leiter Fertigungsplanung, Leiter Produktionsplanung, Leiter Industrial Engineering, Head of Industrial Engineering, Head of Manufacturing Engineering, Werkleiter, Werksleiter, Plant Manager, Leiter Produktion, Produktionsleiter, Fertigungsleiter, Leiter Blechfertigung, Leiter Blechbearbeitung, Head of Production, Director Operations, Technischer Geschäftsführer, COO, Technischer Leiter, Leiter NC-Programmierung, Leiter CAD/CAM, Technischer Einkäufer, Leiter Einkauf, Strategischer Einkäufer
```
> Leiter NC-Programmierung / CAD/CAM und Produktions-IT nur als Zweitkontakt. Nicht anschreiben: Vertrieb, Marketing, HR, Verwaltung, Qualitätsmanagement, Maschinenbediener. Max. 3 Kontakte pro Firma.
## 3. Apollo.io Filter-Empfehlung — Playbook 791
**Filter: ICP 3 – Industrie / OEM mit eigener Blechfertigung**
<table header-row="true">
<tr>
<td>Kriterium</td>
<td>Werte</td>
</tr>
<tr>
<td>Jobtitel</td>
<td>Leiter Arbeitsvorbereitung, AV-Leiter, Leiter Fertigungsplanung, Leiter Produktionsplanung, Leiter Industrial Engineering, Head of Manufacturing Engineering, Werkleiter, Werksleiter, Plant Manager, Leiter Produktion, Produktionsleiter, Fertigungsleiter, Leiter Blechfertigung, Head of Production, Technischer Geschäftsführer, COO, Technischer Leiter, Leiter NC-Programmierung, Leiter CAD/CAM, Technischer Einkäufer, Leiter Einkauf</td>
</tr>
<tr>
<td>Industrie</td>
<td>Machinery, Mechanical or Industrial Engineering, Industrial Automation, Electrical/Electronic Manufacturing, Medical Devices, Environmental Services (Anlagenbau), Farming (Landtechnik-Hersteller), Transportation/Trucking/Railroad (nur Fahrzeug-/Aufbautenhersteller), Food Production (nur Maschinen-/Anlagenhersteller)</td>
</tr>
<tr>
<td>Mitarbeiter</td>
<td>Ab 50 Mitarbeiter (51–200, 201–500, 501–1.000, 1.000+); ab 500 nur mit Blechfertigung am Standort</td>
</tr>
<tr>
<td>Standort</td>
<td>Deutschland, Österreich, Schweiz (DACH)</td>
</tr>
<tr>
<td>Seniority</td>
<td>c_suite, vp, director, head, manager</td>
</tr>
<tr>
<td>Keywords (bedarfsorientiert)</td>
<td>eigene Blechfertigung, Blechfertigung, Blechbearbeitung, Blechteile, Blechgehäuse, Gehäusebau, Schaltschrankbau, Schaltanlagenbau, Verteilerbau, Maschinenbau, Sondermaschinenbau, Anlagenbau, Gerätebau, Elektromechanik, Komponentenfertigung, Fördertechnik, Fördersysteme, Lagertechnik, Intralogistik, Regalbau, Landtechnik, Landmaschinen, Fahrzeugbau, Nutzfahrzeugaufbauten, Aufbauten, Anhängerbau, Kältetechnik, Klimatechnik, Lüftungstechnik, Großküchentechnik, Ladenbau, Medizintechnik, Labortechnik, Verpackungsmaschinen, Lebensmittelmaschinen, Filteranlagen, Recyclinganlagen, Laserschneiden, Abkanten, Biegezelle, Automation, TRUMPF, TruLaser, TruBend, TruPunch, TruMatic, Arbeitsvorbereitung, NC-Programmierung, Industrial Engineering, Fertigungsplanung, sheet metal, sheet metal fabrication, enclosures, switchgear, machine building, special purpose machinery, conveyor systems, agricultural machinery, vehicle bodies</td>
</tr>
<tr>
<td>Ausschluss-Keywords</td>
<td>Automobilhersteller, OEM Automotive, Pkw, reine Montage, Zerspanung, Drehteile, Frästeile, Gießerei, Kunststoffverarbeitung, Lohnfertigung (→ Playbook 790), Maschinenhandel, Gebrauchtmaschinen, Maschinenvermittlung, Großhandel, Distributor, Reseller, Handelsvertretung, Personaldienstleistung, Zeitarbeit, Unternehmensberatung, Softwareentwicklung, IT-Dienstleister, CAD/CAM-Dienstleister, Hochschule, Bystronic, Amada, Salvagnini, Prima Power, LVD</td>
</tr>
</table>
---
## Nächste Schritte
- [ ] Prompts in Clay als Claygent-Spalte je Playbook anlegen, `score` / `qualified` / `reason` als eigene Spalten mappen
- [ ] Testlauf über 50 Zeilen je Playbook aus der Firmenliste (CSV `scalenc_playbooks_789_790_791.csv`), `Yes`-Trefferquote manuell gegenprüfen
- [ ] Schwellwerte (7 / 5) nach Testlauf justieren
- [ ] Nur `Yes` (+ optional `Maybe`) an Apollo/Clay People-Search mit den Job Titles weitergeben
- [ ] Blacklist (158 Bestandskunden, DACH) vor dem Upload in Amplifa erneut abgleichen
