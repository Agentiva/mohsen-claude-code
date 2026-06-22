---
name: amplifa-market-intelligence
description: >
  Erstellt einen Market-Intelligence- & Outbound-GTM-Report im amplifa-Design als
  16:9-HTML-Deck (1920×1080) für eine beliebige Auftraggeber-Firma. Nimm die
  recherchierten Firmen-/Markt-/GTM-Daten (z. B. aus einem Research-Skill) und
  setze sie in das feste amplifa-Designsystem ein: gleiche Typografie, Farben und
  Slide-Komponenten wie bei ErgoPack/GBN/REMIRA, aber Inhalt, Reihenfolge und
  Slide-Anzahl passen sich der jeweiligen Firma an. Nutze diesen Skill, wann immer
  ein neuer "<Firma> Market Intelligence"-Report im amplifa-Look gebaut werden soll.
---

# amplifa Market Intelligence Report — Skill

Du baust einen **Market-Intelligence- & Outbound-GTM-Report** im amplifa-Design.
Das **Design ist fix**, die **Inhalte sind variabel**. Deine Aufgabe ist es, die
gelieferten Recherche-Daten *intelligent* in den passenden Slide-Komponenten zu
platzieren — nicht ein starres Template Feld-für-Feld auszufüllen.

> Bestehende Beispiele desselben Systems: ErgoPack (22 Slides), GBN Systems (24),
> REMIRA (30). Gleiche CSS-Basis, unterschiedliche Story-Länge.

---

## 1. Was du bekommst (Input)

Ein Daten-Payload zu **einer Firma** (Auftraggeber von amplifa), typischerweise:

- Firmenprofil: Name, Standort, Gründung, Eigentümer, Kennzahlen (Umsatz, MA, HRB …)
- Produkt/Leistung + Portfolio-Linien
- Eine zentrale **Klarstellung/Korrektur** (häufiger Briefing-Fehler, der zu fixen ist)
- Wettbewerb & Positionierung
- Marktgröße & Wachstum (mit Quellen), strukturelle Treiber
- TAM/SAM/SOM (als Bandbreiten)
- Zielvertikalen / ICPs, Buying Committee (Personas), Trigger-Events
- GTM: Hook-Lines je Persona, Kanal-Mix, Phasenplan, Empfehlungen, Vorbehalte

Nicht jede Firma hat jeden Block. **Lass Slides weg, die keine Substanz haben.**
Erfinde keine Zahlen — kennzeichne Schätzungen als illustrativ.

---

## 2. Workflow

1. **Daten sichten** und in die 4 Erzähl-Teile gruppieren (siehe §3).
2. **Slide-Plan** aufstellen: Liste der Sections in Reihenfolge, jeweils mit der
   gewählten Komponente aus `reference/COMPONENTS.md`. Plane Total-Slide-Zahl.
3. **Shell kopieren:** Starte von `assets/report-shell.html`. Sie enthält den
   kompletten `<head>` + das **gesamte CSS** (nicht ändern!) + `deck-stage.js`.
   Kopiere `assets/amplifa-logo.png` und `assets/amplifa-logo-white.png` neben
   die Ausgabedatei (Ordner `assets/`) sowie `deck-stage.js` ins selbe Verzeichnis.
4. **Slides bauen:** Für jede geplante Section das HTML-Pattern aus
   `COMPONENTS.md` kopieren und mit den Firmendaten füllen.
5. **Nummerierung:** Jede Section hat `data-screen-label="NN Titel"` und im
   `.chrome` einen `.chrome-pages` Zähler `NN / TOTAL`. Durchnummerieren, TOTAL
   überall gleich setzen.
6. **Render-Check:** Deck öffnen, prüfen dass kein Slide-Inhalt unten abgeschnitten
   ist (1080px Höhe, 88px Padding). Bei Überfüllung → §6 Density-Fixes.
7. **Dateiname:** `<Firma> Market Intelligence.html`.

---

## 3. Die Erzähl-Architektur (4 Teile)

Jeder Report folgt grob diesem Bogen. Cover + 4 dunkle Divider + Closing sind das
Skelett; dazwischen variabel viele Inhalts-Slides.

| Teil | Inhalt | Typische Slides |
|---|---|---|
| **00 Rahmen** | Cover (`s-title`) | 01 |
| **Teil 01 — Executive Summary** | Divider + Top-5-Insights | 2–3 |
| **Teil 02 — Unternehmen & Produkt** | Divider, Snapshot-Kennzahlen, Produktlinien, **Klarstellung/Korrektur**, Wettbewerb | 4–7 |
| **Teil 03 — Markt & Zielgruppe** | Divider, Marktanalyse (Bars), Treiber, TAM/SAM/SOM, Zielvertikalen, Buying Committee, Trigger-Events | 6–9 |
| **Teil 04 — Go-to-Market** | Divider, Hook-Lines, Kanal-Strategie, Phasenplan, Empfehlungen, Vorbehalte | 5–7 |
| **Abschluss** | Closing (`s-close`) | 01 |

**Pflicht-Slides** (immer dabei): Cover, die 4 Teil-Divider, Executive-Insights,
Snapshot, Marktanalyse, TAM/SAM/SOM, Buying Committee, Trigger, Kanal-Strategie,
Phasenplan, Empfehlungen, Vorbehalte (Caveats), Closing.

**Optionale Slides** (nur bei genug Substanz): zusätzliche Produkt-/Portfolio-Slides,
mehrere ICP-Detailslides, Geografie, Treiber/Inhibitoren-Spalten, Referenzwand,
Risiken, Materialwechsel-/Sonder-Hooks.

Die **Klarstellung/Korrektur** (`correction` + `myth-real`, siehe COMPONENTS) ist ein
Signature-Element: fast jede Firma hat einen verbreiteten Irrtum (falscher
Eigentümer, falsches Geschäftsmodell, falsche Marktkategorie). Finde ihn und gib ihm
einen eigenen Slide — das schafft Glaubwürdigkeit im Kickoff.

---

## 4. Designsystem (NICHT verändern)

Vollständig in `assets/report-shell.html`. Kurz:

- **Canvas:** `1920×1080`, Padding `88px 112px`, Sprache `de`.
- **Fonts:** `Inter` (400–800) für Text, `JetBrains Mono` für Labels/Zahlen/Kicker.
- **Hintergrund:** warmes Off-White `--bg #f6f5f1`; dunkle Slides `--ink #0a0a0f`.
- **Akzentfarben** (sparsam, semantisch — nicht dekorativ):
  `--accent-grn #1f8a5b` (positiv/primär), `--accent-red #ff3b30` (Warnung/Krise),
  `--accent-blu #2a6ffd`, `--accent-pur #7b3aed`, `--accent-yel #ffb800`.
- **Rhythmus:** helle Inhalts-Slides, dunkle Divider/Closing als Zäsuren.
  Pro Inhalts-Block höchstens 1 dunkle Karte als Kontrast-Akzent.
- **Chrome:** jede Section hat oben die Kopfzeile (Logo links, Kontext + Seitenzahl
  rechts). Dunkle Slides nutzen `amplifa-logo-white.png`, helle `amplifa-logo.png`.

**Typo-Klassen:** `h1.display` (Cover), `h2.title`/`h2.title-md` (Slide-Titel),
`h3.sub` (Subline), `.eyebrow` (Label über Titel, `.warn` = roter Strich),
`.body-text`, `.mono`. Inhalts-Slides beginnen mit `.pad-top` (180px) damit der Titel
unter der Chrome sitzt.

---

## 5. Inhaltsregeln

- **Mindest-Schriftgröße 24px** im Fließtext — das ist ein 1920er Deck, keine Webseite.
- **Keine Slop-Füllung:** jeder Slide trägt eine These. Lieber 18 dichte Slides als 30 dünne.
- **Zahlen = Beweis:** jede Kennzahl mit Quelle/Stand in der `.note`/`small`/`.alt`.
  Unsichere Werte als „illustrativ"/„Größenordnung" kennzeichnen (siehe Caveats-Slide).
- **Compliance-Linie** (Kanal-Strategie): Telefon-/LinkedIn-first, dokumentierte
  Einwilligung VOR Cold-E-Mail/KI-Voice (UWG §7 / BVerwG 6 C 3.23). Diese Haltung
  bleibt firmenübergreifend gleich — Formulierung an Branche anpassen.
- **Ton:** sachlich, beraterisch, deutsch. Anführungszeichen „…" (deutsch).
- **CTA** ist firmenspezifisch, zielt aber immer auf den stärksten Conversion-Hebel
  der Firma (bei ErgoPack: kostenlose Vor-Ort-Demo).

---

## 6. Layout / Density

Jeder Slide muss **innerhalb 1080px** passen, kein Scrollen, kein Abschnitt.

- Standard-Titel `.title-md` (72px). Bei langem Titel auf 2 Zeilen umbrechen (`<br>`).
- Grids haben feste Spaltenzahl — halte dich an die in COMPONENTS angegebene Anzahl
  (5 Insights, 3 brand-cols, 4 snap, 3 funnel, 6 personas …). Mehr Items → kleinere
  `min-height`/`padding` per Slide-Override, nicht globales CSS ändern.
- **Per-Slide-Overrides** (wie in REMIRA) gehören in einen zusätzlichen `<style>`
  am Ende des `<head>`, selektiert über das Label, z. B.:
  ```css
  section[data-screen-label="23 Personas"] .pcard { min-height: 268px; }
  section[data-screen-label="23 Personas"] .pad-top { padding-top: 110px; }
  ```
  So bleibt das Basis-CSS unangetastet und nur der volle Slide wird verdichtet.

- **Bekannter Engpass — `brand-cols`-Slides (Produktlinien/Wettbewerb/Zielvertikalen):**
  Mit 2-zeiligem `.title-md` + `desc` + 3 `ul`-Zeilen reichen die Karten
  (`min-height:480px`) bis an die 1080px-Kante → untere Kartenreihe wird abgeschnitten.
  **Fix = Karten in voller Größe lassen, nur den ganzen Block nach oben schieben**
  (NICHT die Karten verkleinern). Für jeden betroffenen `brand-cols`-Slide:
  ```css
  section[data-screen-label="NN Label"] .pad-top { padding-top: 128px; }
  section[data-screen-label="NN Label"] .brand-cols { margin-top: 44px; }
  ```

- **Render zu PDF:** Chrome/Edge headless mit Wartebudget, sonst leeres PDF (Print vor
  JS/Font-Init): `--headless=new --disable-gpu --run-all-compositor-stages-before-draw
  --virtual-time-budget=8000 --no-pdf-header-footer --print-to-pdf=...`. Danach Seiten
  als PNG prüfen (Density/Abschnitt), v. a. die `brand-cols`-Slides.

---

## 7. Referenzen in diesem Skill

- `assets/report-shell.html` — Start-Skelett: kompletter Head + CSS + leere Stage
  mit Beispiel-Cover. **Hier anfangen.**
- `assets/deck-stage.js` — die Deck-Engine (neben die Ausgabe kopieren).
- `assets/amplifa-logo*.png` — Logos (in `assets/` neben die Ausgabe kopieren).
- `reference/COMPONENTS.md` — **der Baukasten**: jede Slide-Komponente mit fertigem
  HTML-Pattern, wann man sie nutzt und welche Daten hineingehören.
- `reference/example-ergopack.html` — vollständiger, fertiger Report als Goldstandard.
  Bei Unsicherheit über Markup/Stil hier nachschauen.

**Reihenfolge beim Bauen:** report-shell.html kopieren → COMPONENTS.md je Section →
example-ergopack.html als visuelle Referenz gegenchecken.
