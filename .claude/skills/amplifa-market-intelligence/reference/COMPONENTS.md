# COMPONENTS — amplifa Market Intelligence Baukasten

Jede Slide ist ein direktes `<section>`-Kind von `<deck-stage>`. Kopiere das
Pattern, fülle die Daten, setze `data-screen-label="NN …"` und den `.chrome-pages`
Zähler `NN / TOTAL`. Helle Slides → `amplifa-logo.png`, dunkle → `amplifa-logo-white.png`.

Alle Klassen sind in `assets/report-shell.html` definiert — **CSS nicht ändern**,
nur per-Slide-Overrides am Head-Ende (siehe SKILL §6).

Standard-Chrome (oben in jeder hellen Section):
```html
<div class="chrome">
  <div class="mark"><img src="assets/amplifa-logo.png" alt="amplifa"></div>
  <div class="meta"><span>KONTEXT-LABEL</span><span class="chrome-pages">NN / TOTAL</span></div>
</div>
```
Inhalts-Slides wickeln den Body in `<div class="pad-top"> … </div>` (Titel sitzt
unter der Chrome). Aufbau fast immer: `eyebrow` → `h2.title-md` → Komponente.

---

## 1 · COVER — `s-title`  (immer Slide 01)
Headline = die zentrale Story in 2–3 kurzen Zeilen, letztes Wort farbig (`pop-red`).
```html
<section data-screen-label="01 Cover" class="s-title">
  <div class="chrome">
    <div class="mark"><img src="assets/amplifa-logo.png" alt="amplifa"></div>
    <div class="meta"><span><span class="dot"></span>Vertraulich · für COMPANY</span><span class="chrome-pages">01 / TOTAL</span></div>
  </div>
  <div class="hero">
    <div class="kicker">MARKT-INTELLIGENZ &amp; OUTBOUND-GTM-ANALYSE · DE / DACH · MONAT JAHR</div>
    <h1 class="display">Erste<br>Zeile<br><span class="pop-red">Pointe.</span></h1>
    <div class="underline"><span></span><span></span><span></span><span></span><span></span></div>
  </div>
  <div class="footnote" style="margin-top:96px">
    <div><strong>Auftraggeber</strong>COMPANY · Standort<br>Kurzcharakterisierung · GF Name</div>
    <div><strong>Gegenstand &amp; Zweck</strong>Produkt/Leistung<br>KI-gestützte Outbound-Neukundenakquise via amplifa</div>
    <div><strong>Stand</strong>Datum<br>v1.0 · DE · amplifa</div>
  </div>
</section>
```

## 2 · DIVIDER — `s-divider`  (dunkel; 1× pro Teil, 4×)
Große Teil-Überschrift + erklärender `sub`-Absatz, was dieser Teil leistet.
```html
<section data-screen-label="NN Divider Titel" class="s-divider">
  <div class="chrome"><div class="mark"><img src="assets/amplifa-logo-white.png" alt="amplifa"></div><div class="meta"><span>Teil 0X</span><span class="chrome-pages">NN / TOTAL</span></div></div>
  <div class="core">
    <div class="num">— TEIL 0X</div>
    <h2>Teil-<br>Titel.</h2>
    <p class="sub">Ein Satz, der genau benennt, was dieser Abschnitt liefert und warum er für die Akquise zählt.</p>
    <div class="stripe"><span></span><span></span><span></span><span></span></div>
  </div>
  <div class="foot"><span>Linker Fußnoten-Tag</span><span>Rechter Kontext-Tag</span></div>
</section>
```

## 3 · TOP-5 INSIGHTS — `insights`  (genau 5 Karten)
Die 5 strategischen Kernaussagen des Reports. `bar`-Farben sind fix (grn/blu/yel/pur/red).
```html
<section data-screen-label="NN Top 5 Insights">
  <div class="chrome">…</div>
  <div class="pad-top">
    <span class="eyebrow">Top 5</span>
    <h2 class="title-md" style="margin-top:24px">Die&nbsp;fünf&nbsp;Insights<br>für die Akquise-Story.</h2>
    <div class="insights">
      <div class="insight">
        <span class="bar"></span><span class="idx">01</span>
        <h4>Kurze These-Überschrift</h4>
        <p>2–3 Sätze Beleg mit konkreten Zahlen/Quellen.</p>
        <div class="tag">→ Kategorie</div>
      </div>
      <!-- … insgesamt 5 .insight … -->
    </div>
  </div>
</section>
```

## 4 · SNAPSHOT-KENNZAHLEN — `snap-grid`  (4 Spalten, meist 8 Kacheln)
Verifizierte Firmen-KPIs. Eine Kachel als `snap dark` für Hauptsitz/Highlight.
Lange Werte: `style="font-size:38px"` o. ä. am `.val` reduzieren.
```html
<section data-screen-label="NN Snapshot">
  <div class="chrome">…</div>
  <div class="pad-top">
    <span class="eyebrow">Account at a glance</span>
    <h2 class="title-md" style="margin-top:24px">Die Firma<br>in Zahlen.</h2>
    <div class="snap-grid">
      <div class="snap"><div class="lbl">Label</div><div class="val">Wert<span class="unit">Einheit</span></div><div class="note">Kontext · Quelle</div></div>
      <div class="snap dark"><div class="lbl">Hauptsitz</div><div class="val" style="font-size:40px">Ort</div><div class="note">Adresse</div></div>
      <!-- … 4er-Raster, i. d. R. 8 Kacheln … -->
    </div>
  </div>
</section>
```

## 5 · DREI-SÄULEN-KARTEN — `brand-cols` / `brand-card`  (genau 3)
Mehrzweck: Produktlinien, Wettbewerbsgruppen, ODER Zielvertikalen. Die mittlere/
wichtigste Karte `v-a` (schwarzer Rahmen = Hervorhebung); andere `v-b`/`v-c`/`v-d`.
```html
<section data-screen-label="NN Produktlinien">
  <div class="chrome">…</div>
  <div class="pad-top">
    <span class="eyebrow">Drei Linien — ein roter Faden</span>
    <h2 class="title-md" style="margin-top:24px">Linie A, B<br>und C.</h2>
    <div class="brand-cols">
      <div class="brand-card v-a">
        <div class="accent-bar"></div>
        <div class="lvl">LINIE 01 / EINSTIEG</div>
        <h3>Name</h3>
        <div class="tag">Modell-/Typencodes</div>
        <p class="desc">Was es ist und für wen — 2 Sätze.</p>
        <ul>
          <li>Merkmal <span>Wert</span></li>
          <li>Preis <span>Spanne</span></li>
          <li>Hook <span>Verkaufsargument</span></li>
        </ul>
      </div>
      <!-- v-b, v-c … -->
    </div>
  </div>
</section>
```
> Für die wichtigste Mittel-Position (z. B. „die Nische dazwischen") `v-a` verwenden.
> ⚠️ **Density-Pflicht:** Bei 2-zeiligem Titel + `desc` + 3 `ul`-Zeilen reichen die Karten
> bis an die 1080px-Kante (untere Reihe abgeschnitten). Karten in voller Größe lassen und
> per Slide-Override nur den Block nach oben schieben (`.pad-top:128px`, `.brand-cols margin-top:44px`,
> siehe SKILL §6) — NICHT die Karten verkleinern.

## 6 · KLARSTELLUNG / KORREKTUR — `correction` + `myth-real`  (Signature-Slide)
Links Erklärung, rechts Mythos-Karte (hell, durchgestrichene Tags) über Verifiziert-
Karte (dunkel). `eyebrow warn` für den roten Strich. Optional graue Mono-Box als Beleg.
```html
<section data-screen-label="NN Klarstellung">
  <div class="chrome">…</div>
  <div class="correction">
    <div>
      <span class="eyebrow warn">Wichtig fürs Kickoff</span>
      <h2 class="title-md" style="margin-top:24px">Korrekt —<br>nicht Irrtum.</h2>
      <p class="lede">Worum es geht und was im Markt falsch kursiert; verifizierte Lage in 3–4 Sätzen.</p>
      <div style="margin-top:36px;padding:24px 28px;background:var(--bg-2);border:1px solid var(--line);border-radius:14px;font-family:'JetBrains Mono',monospace;font-size:15px;color:var(--ink-2);line-height:1.6">Zusatz-Beleg / Quelle als Mono-Box.</div>
    </div>
    <div class="myth-real">
      <div class="mr-card myth">
        <div class="mr-lbl">Mythos · zu korrigieren</div>
        <div class="mr-head">„Falsche Annahme"</div>
        <div class="mr-body">Warum das falsch ist.</div>
        <div class="mr-tags"><span>Falsch-Tag</span><span>Falsch-Tag</span></div>
      </div>
      <div class="mr-card real">
        <div class="mr-lbl">Verifiziert</div>
        <div class="mr-head">Korrekte Lage</div>
        <div class="mr-body">Beleg mit Quelle/Datum.</div>
        <div class="mr-tags"><span>Fakt</span><span>Fakt</span></div>
      </div>
    </div>
  </div>
</section>
```

## 7 · MARKTANALYSE mit Balken — `crisis` + `bars-chart`  (2-spaltig)
Links Story + farbige Akzent-Box; rechts Balkendiagramm + 2 KPI-Kacheln.
`fill width:%` proportional setzen; Krisenjahr `crisis-y`, Zukunft `future`.
```html
<section data-screen-label="NN Marktanalyse">
  <div class="chrome">…</div>
  <div class="crisis">
    <div>
      <span class="eyebrow">Markt-Kontext</span>
      <h2 class="title-md">Markt mit<br>Rückenwind.</h2>
      <p class="lede">Marktgröße, CAGR, Region — mit Quelle.</p>
      <div style="margin-top:32px;padding:22px 28px;background:var(--accent-red);color:#fff;border-radius:14px;font-size:17px;line-height:1.5">Zugespitzter Treiber-Fakt mit Zahl.</div>
    </div>
    <div>
      <div style="font-family:'JetBrains Mono',monospace;font-size:13px;letter-spacing:0.1em;text-transform:uppercase;color:var(--muted);margin-bottom:18px">Chart-Titel · Einheit (Quelle)</div>
      <div class="bars-chart">
        <div class="bar-line"><span class="yr">2024</span><div class="track"><div class="fill" style="width:66%">5,43</div></div><span class="delta pos">Basis</span></div>
        <div class="bar-line future"><span class="yr">2032</span><div class="track"><div class="fill" style="width:100%">8,25</div></div><span class="delta pos">CAGR</span></div>
      </div>
      <div style="margin-top:44px;display:grid;grid-template-columns:1fr 1fr;gap:16px">
        <div style="background:var(--bg-2);border:1px solid var(--line);border-radius:16px;padding:26px 28px">… KPI hell …</div>
        <div style="background:var(--ink);color:#fff;border-radius:16px;padding:26px 28px">… KPI dunkel …</div>
      </div>
    </div>
  </div>
</section>
```

## 8 · TREIBER- / ZIEL-TABELLE — `trg-table`  (3 Spalten)
Treiber / Vendor-Liste / Account-Liste. `tw urgent` (schwarz) = höchste Relevanz,
`tw` = mittel, `tw opp` (grau) = Kontext.
```html
<div class="trg-table">
  <div class="trg-row head"><div>Treiber / Markt</div><div>Kennzahl &amp; Status</div><div style="text-align:center">Relevanz</div></div>
  <div class="trg-row"><div class="tname">Name<small>Sub-Label</small></div><div class="tsrc">Beleg mit Zahl &amp; Quelle</div><div class="tw urgent">Kern</div></div>
  <!-- weitere Zeilen … -->
</div>
```

## 9 · TREIBER & HEMMNISSE — `di-grid` / `di-col`  (2 Spalten)
Links helle „Treiber"-Spalte (grüner Punkt), rechts dunkle „Hemmnisse"-Spalte (roter Punkt).
```html
<div class="di-grid">
  <div class="di-col">
    <div class="head"><span class="dot"></span><h4>Treiber</h4></div>
    <ul><li><span class="ico">↑</span><span class="txt">Treiber-Text</span><span class="val pos">+X %</span></li></ul>
  </div>
  <div class="di-col dark">
    <div class="head"><span class="dot"></span><h4>Hemmnisse</h4></div>
    <ul><li><span class="ico">↓</span><span class="txt">Hemmnis-Text</span><span class="val down">−X</span></li></ul>
  </div>
</div>
```

## 10 · USP / PLATTFORMEN — `usp-grid`  (3 Spalten, 3–6 Karten)
`ico-block`-Farben rotieren automatisch per `:nth-child` (grn/blu/ink/pur/yel/red).
```html
<div class="usp-grid">
  <div class="usp"><div class="ico-block">01</div><div class="nm">USP-Name</div><div class="desc">Nutzen in 1–2 Sätzen.</div></div>
  <!-- … -->
</div>
```

## 11 · TAM / SAM / SOM — `funnel`  (genau 3, SOM dunkel)
Transparente Bandbreiten, keine Punktprognosen. SOM-Karte `fn som` (dunkel).
Danach optional Hinweis-Leiste (dunkel) mit „illustrativ".
```html
<div class="funnel">
  <div class="fn"><div class="lbl">TAM · MARKTPOTENZIAL</div><h4>Definition</h4><p class="desc">Was zählt dazu.</p><div class="bignum" style="font-size:60px">Wert<span class="unit">Einheit</span></div><div class="alt">Annahme · <strong>Hervorhebung</strong></div></div>
  <div class="fn"><div class="lbl">SAM · ERREICHBAR</div>…</div>
  <div class="fn som"><div class="lbl">SOM · 12–24 MONATE</div>…</div>
</div>
<div style="margin-top:22px;padding:24px 36px;background:var(--ink);color:#fff;border-radius:16px;display:flex;align-items:center;gap:8px;flex-wrap:wrap"><span style="font-family:'JetBrains Mono',monospace;font-size:13px;color:var(--accent-yel);letter-spacing:0.1em;text-transform:uppercase;margin-right:18px">Hinweis</span><span style="font-size:20px;line-height:1.4;color:rgba(255,255,255,0.9)">Illustrative Größenordnungen, mit CRM-/Pipeline-Daten zu kalibrieren.</span></div>
```

## 12 · BUYING COMMITTEE — `persona-grid` / `pcard`  (3 Spalten, meist 6)
`ch primary` = empfohlener Erstkanal. Sub-Label = Rolle im Kaufprozess.
```html
<div class="persona-grid">
  <div class="pcard">
    <div class="role">Rolle / Titel<small>Funktion im Buying-Prozess</small></div>
    <div class="kpis">FOKUS · Stichworte</div>
    <div class="channels"><span class="ch primary">Telefon*</span><span class="ch">LinkedIn</span></div>
    <div class="trig"><strong>Hebel</strong>Wodurch man diese Person gewinnt.</div>
  </div>
  <!-- … 6 Karten … -->
</div>
```

## 13 · TRIGGER-EVENTS — `signals-list` / `sig`  (Liste, meist 6)
Nach Kaufabsicht sortiert. Top-Trigger `.when` schwarz hervorheben.
```html
<div class="signals-list">
  <div class="sig"><div class="num">01</div><div class="nm">Trigger-Name<small>warum er Kaufabsicht signalisiert</small></div><div class="src">Datenquelle</div><div class="when" style="background:var(--ink);color:#fff;border-color:var(--ink)">Top-Trigger</div></div>
  <div class="sig"><div class="num">02</div><div class="nm">…<small>…</small></div><div class="src">…</div><div class="when">sehr hoch</div></div>
</div>
```

## 14 · HOOK-LINES — `hooks-grid` / `hook`  (3 Spalten, meist 6)
Je Persona ein Zitat-Hook. Optional darunter dunkle CTA-Leiste mit General-Pitch.
```html
<div class="hooks-grid">
  <div class="hook"><span class="idx">01 · Persona</span><q>Wörtlicher Gesprächsaufhänger mit Zahl/Nutzen.</q><div class="ctx">Thema · Tag</div></div>
  <!-- … 6 … -->
</div>
<div style="margin-top:26px;padding:22px 30px;background:var(--ink);color:#fff;border-radius:14px;display:flex;gap:24px;align-items:center"><span style="font-family:'JetBrains Mono',monospace;font-size:13px;color:var(--accent-yel);letter-spacing:0.1em;text-transform:uppercase;white-space:nowrap">Genereller CTA</span><span style="font-size:19px;line-height:1.4;color:rgba(255,255,255,0.9)">Der eine Pitch-Satz, der auf den Conversion-Hebel zielt.</span></div>
```

## 15 · KANAL-STRATEGIE — `cmx`  (Compliance-Matrix)
Pro Persona: Telefon-Level, LinkedIn-Level, empfohlene Sequenz. Level-Klassen:
`primar` (grün, voll), `sek` (schwarz, 58%), `consent` (34%), `none` (leer).
Darunter Legende + UWG/DSGVO-Hinweis-Absatz (Mono).
```html
<div class="cmx">
  <div class="cmx-row head"><div>Persona</div><div>Telefon*</div><div>LinkedIn</div><div>Empfohlene Sequenz</div></div>
  <div class="cmx-row">
    <div class="pn">Persona<small>Sub</small></div>
    <div class="lv primar"><span class="badge">Primär</span><span class="meter"><i></i></span></div>
    <div class="lv sek"><span class="badge">Sekundär</span><span class="meter"><i></i></span></div>
    <div class="seq"><b>1</b>LinkedIn → <b>2</b>Telefon → <b>3</b>Consent → E-Mail</div>
  </div>
</div>
<div class="cmx-legend"><span><i style="background:var(--accent-grn)"></i>Primär</span><span><i style="background:var(--ink)"></i>Sekundär</span></div>
<div style="margin-top:28px;font-family:'JetBrains Mono',monospace;font-size:14px;color:var(--muted);line-height:1.6">§ 7 UWG / BVerwG 6 C 3.23: Cold-E-Mail &amp; KI-Voice nur NACH dokumentierter Einwilligung; Branchen-/Sachbezug je Account festhalten.</div>
```

## 16 · REFERENZWAND — `ref-cols`  (3 Spalten)
Belegte Referenzkunden gruppiert (z. B. nach Vertikale). `accent-bar` grn/blu/pur.
```html
<div class="ref-cols">
  <div class="ref-col"><div class="accent-bar"></div><div class="rh">GRUPPE</div><h3>Titel</h3><ul><li>Kunde <small>Kontext</small></li></ul></div>
</div>
```

## 17 · RISIKEN — `risk-grid`  (3 Spalten)
Roter Links-Balken; je Karte Risiko + Mitigation (grün, Mono).
```html
<div class="risk-grid">
  <div class="risk"><div class="nm">Risiko</div><div class="desc">Beschreibung.</div><div class="mit"><strong>Mitigation</strong>Gegenmaßnahme.</div></div>
</div>
```

## 18 · PHASENPLAN — `phases`  (genau 3, Timeline)
3-Stufen-Vorgehen mit verbundener Linie. Erste Node `nd` schwarz. `bench` = Schwelle.
```html
<div class="phases">
  <div class="phase"><div class="nd">01</div><div class="wk">Monat 1–3</div><h4>Phasen-Titel</h4><ul><li><span>Maßnahme</span></li></ul><div class="bench">→ Threshold: messbares Ziel</div></div>
  <div class="phase"><div class="nd">02</div>…</div>
  <div class="phase"><div class="nd">03</div>…</div>
</div>
```

## 19 · EMPFEHLUNGEN — `recs`  (2 Spalten, meist 4–5)
Nummerierte Handlungsempfehlungen.
```html
<div class="recs">
  <div class="rec"><div class="num">01</div><div><h5>Empfehlung</h5><p>Begründung.</p></div></div>
</div>
```

## 20 · VORBEHALTE — `caveats`  (2 Spalten, meist 6) — fast immer vorletzter Slide
`eyebrow warn`. Ehrliche Datenlage: was unsicher/illustrativ/Herstellerangabe ist.
```html
<div class="caveats">
  <div class="cv"><div class="i">01</div><div class="t">Vorbehalt mit konkretem Bezug.</div></div>
</div>
```

## 21 · CLOSING — `s-close`  (dunkel; immer letzter Slide)
Empfehlung als große Headline (`accent` = grün), CTA-Buttons, Swatches, Footer.
```html
<section data-screen-label="NN Closing" class="s-close">
  <div class="chrome"><div class="mark"><img src="assets/amplifa-logo-white.png" alt="amplifa"></div><div class="meta"><span>Empfehlung &amp; nächste Schritte</span><span class="chrome-pages">NN / TOTAL</span></div></div>
  <div class="core">
    <span class="eyebrow">Empfehlung</span>
    <h2>Kernempfehlung mit <span class="accent">Akzent</span>.<br>Zweite Zeile.</h2>
    <p class="sub-cta" style="margin-top:32px">Zusammenfassung des empfohlenen Vorgehens in 2–3 Sätzen.</p>
    <div class="actions" style="margin-top:40px">
      <a class="btn" href="#">Primäre Aktion <span class="arr">↗</span></a>
      <a class="btn ghost" href="#">Sekundäre Aktion <span class="arr">→</span></a>
    </div>
    <div class="swatches" style="margin-top:36px"><span style="background:var(--accent-grn)"></span><span style="background:var(--accent-blu)"></span><span style="background:var(--accent-yel)"></span><span style="background:var(--accent-pur)"></span></div>
  </div>
  <div class="foot">
    <div><strong>amplifa</strong>Outbound-Akquise · COMPANY</div>
    <div style="text-align:right"><strong>Report v1.0 · Datum</strong>für COMPANY · vertraulich</div>
  </div>
</section>
```

---

### Farb-Semantik (einheitlich verwenden)
- **grn** `#1f8a5b` — positiv, primär, „verifiziert", Erfolg
- **red** `#ff3b30` — Warnung, Krise, Mythos, Vorbehalt
- **blu** `#2a6ffd` · **pur** `#7b3aed` · **yel** `#ffb800` — neutrale Akzent-Rotation
- **ink** `#0a0a0f` — Divider, Closing, je 1 Kontrast-Karte pro Slide

### Checkliste je Slide
- [ ] `data-screen-label="NN …"` gesetzt, `chrome-pages` `NN / TOTAL` korrekt
- [ ] richtiges Logo (hell/dunkel) für den Hintergrund
- [ ] Inhalt passt in 1080px (sonst per-Slide-Override, §6 SKILL)
- [ ] jede Zahl mit Quelle/Stand; Unsicheres als „illustrativ" markiert
