# byload – Firmen-Deep-Research (KMU / Süddeutschland-DACH)

Zielunternehmen für die Spedition **byload GmbH** (Mindelheim, Allgäu), recherchiert rein per Web Deep Research. Nur **klein- bis mittelständische Unternehmen (KMU)** – keine Konzerne/Großunternehmen. Zwei getrennte Bedarfslisten je Playbook, je Zielgröße **3.000 Firmen**.

## Kunde / Produkt
byload ist ein bayerischer Transport- & Logistikdienstleister mit eigenem Fuhrpark (>15 J. Erfahrung). Kern: Teil- & Komplettladungen, ergänzend Schwer-/Sondertransporte, Lagerlogistik, europaweit inkl. Zoll. Differenzierung: Tempo (Angebot ~10 Min.), starke Preise im FTL/LTL-Segment, Flexibilität, fester Ansprechpartner, eigenes Spezialequipment.

---

## Playbook 1 – Schwer- & Sondertransporte
**Bedarf:** KMU, die (auch nur gelegentlich) schwere, übergroße, sperrige oder nicht standardisierbare Güter national/europaweit bewegen müssen und kein eigenes Schwerlast-Equipment vorhalten.

- **Ziel-Sub-Sektoren:** Maschinen- & Anlagenbau / Sondermaschinenbau, Stahl-/Metallbau & Stahlkonstruktion, Betonfertigteile/Baustoffe-schwer/Fertighaus-Hallenbau, Landtechnik/Baumaschinen/Förder-/Hebetechnik/Krane, Behälter-/Apparate-/Kessel-/Tank-/Silobau, Fahrzeug-/Sonderaufbautenbau.
- **Firmengröße:** KMU (grob < 250 MA), mittelständisch/inhabergeführt.
- **Region:** Fokus Süddeutschland (Bayern, BW), ergänzend restl. DE + AT/CH.
- **Bedarfs-Signale:** übergroße/schwere Endprodukte, „Schwertransport nötig", eigene Fertigung großer Baugruppen, Projekt-/Anlagengeschäft, Maße jenseits Standardmaß.
- **Ausschluss:** Konzerne/Weltmarken/Konzerntöchter; reine Dienstleister ohne physische Güter; Sammelgut-/Kleinteil-Versender ohne Übermaß.

## Playbook 2 – Komplett- & Teilladungen (FTL/LTL, Planen-/Trockenware)
**Bedarf:** Verlader/KMU mit regelmäßigem, palettiertem Transportaufkommen oberhalb Sammelgut (ab ~3–4 Paletten bis Vollauslastung), Planen-/Trockenware – **kein** Frigo, **kein** Sammelgut.

- **Ziel-Sub-Sektoren:** Metallverarbeitung & Metallbau, produzierendes Gewerbe/Industrie, Futtermittel/Mühlen, Getränke/Brauereien, Lebensmittel-Trockenware/Non-Food-Konsumgüter, Automotive-Zulieferer, Baustoffe & Beton (palettiert), Kunststoffverarbeitung, Papier/Verpackung, Möbel/Holz, technischer Großhandel/Industriebedarf.
- **Firmengröße:** KMU (grob < 250 MA).
- **Region:** Fokus Süddeutschland (PLZ 7/8), ergänzend restl. DE + AT/CH; europaweite Relationen relevant.
- **Bedarfs-Signale:** wiederkehrendes Palettenaufkommen, eigene Produktion/Abfüllung, Versand an Handel/Industrie, mehrere Standorte/Relationen, Trockenware.
- **Ausschluss:** Konzerne/Weltmarken; reine Frigo-/Kühlgutversender; reine Kleinpaket-/Sammelgut-Versender; Dienstleister ohne physische Güter.

---

## Artefakte je Playbook
1. `pb1/liste.csv` bzw. `pb2/liste.csv` – `company_name,domain` (dedupliziert).
2. `pb1/clay-qualifizierung-prompt.md` / `pb2/clay-qualifizierung-prompt.md` – Claygent-Bedarfsprüfung.
3. `pb1/jobtitles-clay.txt` / `pb2/jobtitles-clay.txt` – ~25 Tier-1/Tier-2-Jobtitel für „Find People".

## Qualitätsregeln
Domains nie geraten (nur aus real abgerufenen Quellen). KMU-Filter hart. Region priorisiert Süddeutschland. Dedupe über `scripts/merge_dedupe.py`.

---

## Fortschritt (Web-only, über mehrere Sessions)

**Ziel:** 3.000 KMU je Playbook. **Methode:** reine Web-Recherche (Beschluss des Kunden).

| Stand | PB1 (Schwer/Sonder) | PB2 (FTL/LTL) |
|---|---|---|
| Session 1 (2026-07-17) | **328** | **347** |
| **Ziel** | 3.000 | 3.000 |

### Umgebungs-Limits (wichtig für die Planung)
Reine Web-Recherche ist in dieser Umgebung hart gedeckelt:
- **WebSearch:** ~200 Queries pro Session (sessionweit geteilt) – nach einer Welle erschöpft.
- **WebFetch/Egress:** Org-Policy blockt externe Firmen-/Verzeichnis-Websites (403). Domain-Verifikation per Fetch nicht möglich; Domains stammen aus Suchtreffer-URLs.

→ Pro Session realistisch **~600–700 neue verifizierte KMU** (beide Playbooks zusammen). Für 6.000 gesamt sind also ca. **9–10 Folge-Sessions** nötig.

### So geht es in einer neuen Session weiter ("finde mehr")
1. Bestehende `pb1/liste.csv` / `pb2/liste.csv` sind der **Master** (bereits gefundene Domains werden ausgeschlossen).
2. Neue Sub-Sektor × Region-Wellen recherchieren (noch nicht ausgeschöpfte Nischen siehe unten), pro Batch als eigene CSV ablegen.
3. Draufmergen:
   ```bash
   python3 .claude/skills/firmen-deepresearch/scripts/merge_dedupe.py \
     byload-research/pb1/liste.csv byload-research/pb1/<neuer_batch>.csv > byload-research/pb1/liste.new.csv \
     && mv byload-research/pb1/liste.new.csv byload-research/pb1/liste.csv
   ```
4. Zahl im Tracker oben fortschreiben.

### Noch nicht/kaum ausgeschöpfte Nischen (Backlog für Folge-Sessions)
- **PB1:** Gießereien/Schmieden, Pressen/Umformtechnik, Industrieöfen/Trocknung, Getränke-/Abfülltechnik-Maschinenbau, Windkraft-/Energiekomponenten, Textil-/Papiermaschinen, Pumpen-/Mischtechnik, Vorrichtungs-/Betriebsmittelbau, Bootsbau/Yachten, Modul-/Raumzellenbau, Trafo-/Schaltanlagenbau.
- **PB2:** Automotive-Zulieferer (palettiert), Möbel/Holzverarbeitung, technischer Großhandel/Industriebedarf, Agrarhandel/Sackware, Elektro-/Elektrotechnik-Produkte, Fliesen/Naturstein, Farben/Lacke (verpackt), Sanitär/Heizung-Produkte, Papierwaren/Hygiene, Tierfutter/Heimtierbedarf, Baumaschinen-Zubehör.
- **Regionen** je Nische einzeln durchgehen: Schwaben, Oberbayern, Niederbayern, Oberfranken/Mittelfranken/Unterfranken, Oberpfalz, BW (Stuttgart, Ostwürttemberg, Bodensee-Oberschwaben, Schwarzwald), dann NRW/Hessen/Niedersachsen/Sachsen/RLP + AT/CH.
