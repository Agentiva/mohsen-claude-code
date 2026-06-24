# Sequenz-Blueprints + Achsen

Was jede Position leisten muss, plus die Achsen Signale / Region-Locale / CTA.
Pro Position: Job, Struktur, CTA-Minuten, harte Verbote. Wortzahlen in
`disc-system.md` (Matrix).

## Inhalt
1. Positions-Blueprints (E1–E9 + Sondervarianten)
2. Achse: Signale (mit/ohne)
3. Achse: Region → Locale
4. Achse: CTA (15D / Vorort / 30D) + Guardrails
5. Schnell-Mapping zur Miro-Logik

---

## 1. Positions-Blueprints

### E1 — Cold-Open (Erstkontakt)
- **Job:** Aufmerksamkeit + Relevanz herstellen, ein echter Aufhänger.
- **Struktur (DISC-SALES):** Anrede → Hook → fachliche Bridge → (Bullets je nach
  Variante) → 1 CTA → Schluss. Mind. 1 Proof Point.
- **Struktur (AUGENHÖHE):** Anrede → beobachtender Signal-Hook (neutral, keine
  Verkaufsfrage) → neutrale technische Einordnung → Relevanz von
  `{{playbook.product.name}}` als möglicher Gesprächspartner → offener Dialog-CTA.
- **CTA:** 15D (Default).
- **Verbote:** keine Floskeln („ich hoffe, diese Mail erreicht Sie gut"); keine
  generische Personalisierung; AUGENHÖHE zusätzlich: dem Empfänger nicht seine
  eigene Rolle erklären („Sie kennen das…").

### E2 — Follow-up (neuer Winkel)
- **Job:** an E1 anknüpfen OHNE Wiederholung; neuer Hook/Winkel, tiefer (Zahlen,
  Proof). Leichter/kürzer als E1.
- **Struktur:** kurzer Anschluss an `{{previous_email_body}}` + EIN vertiefender
  Gedanke; DISC-SALES-Variante mit 3 Bullets (2/3 mit Proof Point aus
  `{{playbook.proof_points}}`).
- **CTA:** 15D oder 20-Min; **30-Min-Variante** existiert (dann CTA = nur Bitte um
  30 Minuten, Anti-Deliverable-Regel zwingend einbauen).
- **Verbote:** „Ich wollte nachfassen", „Falls meine Mail untergegangen ist";
  gleicher Hook wie E1; erfundene Deliverables/Fristen.

### E3 — kompakt
- **Job:** dichter dritter Touch, kürzer als E1/E2, reiner Fließtext, KEINE
  Bullets. Neuer Mini-Case/Proof/zweites Signal. Soft-Re-Engagement ohne Bettel-Ton.
- **CTA:** 15–20-Min Termin-Ask.
- **Verbote:** „Haben Sie meine Mail erhalten?", Entschuldigungen, Bullet-Listen,
  Material-Versand.

### E4 — ultrakurz
- **Job:** letzter sanfter Touch vor Pause; ein starker Gedanke. Pain + Value
  verschmolzen (nicht getrennt), genau 1 Proof Point, Mikro-CTA (1 Satz).
- **CTA:** 10-Min Mikro-Termin-Ask.
- **Verbote:** Bullets, Pain-Dump, langer CTA, Material-Versand.

### E5 — P.S.-Recovery
- **Job:** Body (Personalisierung → Pain → Value → Termin-CTA → Schluss) + **P.S.**
  als zweiter Hook (neuer Hebel, NIE passiv „Details im Call"). P.S. DISC-spezifisch
  (D: Wettbewerb, I: Story, S: Sicherheit, C: Datenpunkt).
- **CTA:** 15–20-Min; **Output endet mit der P.S.-Zeile**.
- **Verbote:** passives P.S., Bullets, Material-Versand.

### E6 — Perspektivwechsel
- **Job:** echter Pivot — anderer Pain / anderer Use Case / Markttrigger als in
  E1–E5; NEUER Proof Point (nicht aus `{{previous_email_body}}`). Sanftes Opening.
- **CTA:** 15–20-Min Termin-Ask (kein vages „freue mich über Rückmeldung").
- **Verbote:** Wiederholung der bisherigen Argumente, Bettel-Sprache, Bullets.

### E7 — Story
- **Job:** Mini-Case mit 4 Elementen — Protagonist (echte Referenz aus
  `{{playbook.references}}` oder anonymisiert mit Branche/Größe) → Problem (=
  Persona-Pain) → Wendepunkt (aus `{{playbook.value_proposition}}`) → Resultat MIT
  Zahl aus `{{playbook.proof_points}}`. Dann explizite Brücke zu `{{company}}`.
- **CTA:** Termin-Ask mit Slot-Vorschlag.
- **Verbote:** abstrakte Story ohne konkreten Protagonisten/Zahl; Zahl erfinden.

### E8 — Pattern-Interrupt
- **Job:** 1 aufmerksamkeitsstarker Satz (DISC-konform: D/C härter, I bildhafter,
  **S reflexiv statt aggressiv** — sonst Conversion-Killer) → Untermauerung +
  sanfter Reframe → Value mit Proof Point → Termin-CTA mit Slot.
- **CTA:** 15–20-Min Termin-Ask mit Slot.
- **Verbote:** Klickbait ohne Substanz, aggressive Provokation bei S, Bullets.

### E9 — radikale Transparenz
- **Job:** offen zugeben, dass recherchiert wurde + SPEZIFISCHES, nicht-offensichtliches
  Detail (Zahl/Datum/Zitat) → ehrliche Brücke → Value in 1 Zeile mit Proof Point →
  Termin-CTA mit konkreten Slots (Tag/Uhrzeit). Menschlich, KEIN Corporate-Speak.
- **CTA:** 15–20-Min mit konkreten Slot-Vorschlägen.
- **Verbote:** Corporate-Speak/Buzzwords, generische Recherche-Behauptung, schmierige
  Verkaufstransparenz.

### Sondervarianten
- **AUGENHÖHE-Basis / -Follow-up / -kurz / -mit-P.S.** — zurückhaltende Familie,
  Hook = neutrale Signal-Beobachtung, weicher Dialog-CTA. Bei P.S.-Variante: **kein
  P.S. bei S-Profil** (kann als Druck wirken). Siehe `tonalitaet-familien.md`.

---

## 2. Achse: Signale (mit/ohne)
- **mit Signale:** Hook hängt direkt am `{{lead.buying_signals}}` (Auslöser
  benennen, nie raten). Personalisierungs-Hierarchie 7a. Höhere Direktheit, CTA darf
  früher kommen.
- **ohne Signale:** kein Auslöser → Relevanz über ICP-Pain-Hypothese
  (`{{persona.pain_points}}` + `{{playbook.icps}}`) + Peer-Proof
  (`{{playbook.references}}`). Personalisierungs-Hierarchie 7b. 1–2 zusätzliche
  Wert-Touches vor dem CTA, langsamere Eskalation. KEIN Buying Signal behaupten,
  das nicht da ist.

Das ist der zentrale Unterschied der „ohne-Signale-Master"-Sequenz: gleiche
Positionen, aber Hook-Quelle und Hierarchie verschieben sich von Signal → ICP-Pain.

## 3. Achse: Region → Locale
| Region | Locale | Sprach-Regel-Variante | Tonalität |
|---|---|---|---|
| DACH | de | 4a oder 4c | Sie, Understatement, kein Hype, DSGVO/NIS2-sensibel |
| EU (Rest) | en | 4a/4b | klar, etwas direkter als DACH, kulturneutral |
| USA | en | 4a | direkt, Outcome-/ROI-forward, schneller CTA, casual |
| Asien | en | 4a | wie USA (EN, direkt); Zeitzonen/Seniorität beachten |
| FR | fr | 4b oder 4c | „Cher/Chère…", „Cordialement," |

## 4. Achse: CTA + Guardrails
- **15D** (15-Min digital): Default, niedrigste Hürde, früh/kalt/ohne Signal.
- **VORORT:** höchstes Commitment, persönlich. Nur DACH/EU sinnvoll. CTA-Block auf
  Vor-Ort-Termin umformulieren.
- **30D** (30-Min digital): substanzieller, für wärmere/qualifizierte Kontakte; bei
  30-Min-Variante Anti-Deliverable-Regel zwingend.

**Guardrails (zwingend prüfen):**
1. `VORORT` + Region ∈ {USA, Asien} → automatisch auf `30D` digital drehen (Hinweis
   im Output ausweisen).
2. `ohne Signale` + 30-Min im ersten Touch → zu großer Ask; ersten CTA auf 15-Min.
3. `ohne Signale` → 1–2 Wert-Touches vor dem CTA.
4. DACH → keine US-Superlative, keine erfundenen ROI-Zahlen.
5. Späte Position (E3+) → CTA-Minuten tendenziell kürzer (E4 = 10 Min).

## 5. Schnell-Mapping zur Miro-Logik
Die Miro-Entscheidung `Signale → Region → CTA` mappt 1:1:
`SIGNALE(mit/ohne) × REGION(DACH/EU/USA) × CTA(15D/VORORT/30D)` = die Achsen 2–4.
Achse 1 (Position) und Achse 5 (Familie) kommen hinzu. Ein vollständiger Variant-Code
für einen Prompt: `E«n»-«MIT/OHNE»-«REGION»-«CTA»-«FAMILIE»`,
z. B. `E1-OHNE-DACH-15D-AUGENHOEHE`.
