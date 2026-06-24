---
name: amplifa-email-prompt-builder
description: >-
  Baut neue amplifa-Cold-Email-Prompts im exakten Hausstil — fertige
  System-Prompts (mit {{...}}-Platzhaltern, NICHT ausgefüllt), die Anthony in
  app.amplifa.ai unter Playbooks/Sequences einsetzt. Der Skill kalibriert jeden
  Prompt über fünf Achsen: Sequenz-Position (Email 1–9 / Follow-up / Breakup),
  Signale mit/ohne, Region→Locale (DACH=de, EU=en, USA=en, FR=fr), CTA
  (15-Min digital / Vorort / 30-Min digital) und Tonalitäts-Familie (DISC-Sales
  vs. Augenhöhe/zurückhaltend) — plus DISC-Schreibstil (D/I/S/C + Kombis).
  Nutze diesen Skill IMMER, wenn Anthony einen Email-Prompt, eine Mastersequenz,
  einen Sequenz-Prompt, ein Email-Template oder eine Prompt-Variante bauen,
  anpassen oder „nachziehen" will — auch wenn er nur sagt „bau mir den Prompt für
  Email 3", „neuer prompt ohne signals für USA", „mach die 30-Min-Variante", „pass
  die mastersequenz an" oder „erstell den prompt für [Position]". Greift auch,
  wenn er nur die Achsen-Kürzel nennt (z. B. „Email 5, ohne Signale, DACH, Vorort").
---

# amplifa Email-Prompt-Builder

Generator für amplifa-Cold-Email-Prompts. **Output ist ein fertiger
System-Prompt** im Hausstil — kein Email-Text. Anthony fügt ihn in
app.amplifa.ai (Playbook → Sequence → Email-Step) ein; die `{{...}}`-Platzhalter
werden dort zur Laufzeit pro Lead aus Lead- und Playbook-Daten gefüllt.

## Goldene Regel: Platzhalter bleiben Platzhalter

Der erzeugte Prompt enthält `{{...}}`-Platzhalter **wörtlich und unverändert**.
NIEMALS einen Platzhalter mit echten Werten ersetzen (kein „Festo", kein „ABM
Greiffenberger", keine erfundene Zahl). Die amplifa-Engine substituiert sie
später. Erfundene Inhalte im Prompt = der schwerste Fehler hier, weil sie sich
über jede generierte Mail vervielfältigen. Bei Platzhalter-Auswahl ist
`reference/platzhalter.md` die einzige Wahrheit — keine Namen raten.

## Die fünf Achsen (so wird ein Prompt bestimmt)

Jeder Prompt ist eine Kombination aus:

1. **Sequenz-Position** — welche Mail im Ablauf (Email 1 Cold-Open, 2 Follow-up,
   3 kompakt, 4 ultrakurz, 5 P.S.-Recovery, 6 Perspektivwechsel, 7 Story,
   8 Pattern-Interrupt, 9 radikale Transparenz; + Sondervarianten wie 30-Min).
   Jede Position hat einen eigenen strategischen Job, eigene Länge, eigenes
   Format. → `reference/sequenz-blueprints.md`
2. **Signale** — `mit` (Hook hängt direkt am Buying Signal) oder `ohne` (kein
   Auslöser → Relevanz über ICP-Pain-Hypothese + Peer-Proof). Ändert vor allem
   Hook-Quelle und Personalisierungs-Hierarchie. → `reference/sequenz-blueprints.md`
3. **Region → Locale** — DACH→`de`, EU(Rest)→`en`, USA→`en`, FR→`fr`.
   Steuert Sprache + Tonalität + erlaubte CTA. Asien wird wie USA behandelt
   (EN, direkt). → `reference/sequenz-blueprints.md`
4. **CTA** — `15D` (15-Min digital), `VORORT` (Vor-Ort-Termin), `30D` (30-Min
   digital). Achtung Guardrails (z. B. Vorort nur DACH/EU sinnvoll).
   → `reference/sequenz-blueprints.md`
5. **Tonalitäts-Familie** — `DISC-SALES` (offensiv: Termin-CTA, Bullets/P.S./
   Story/Pattern-Interrupt, Box-Header, 4 Stil-Referenzen) ODER `AUGENHÖHE`
   (zurückhaltend: „fachlicher Austausch auf Augenhöhe", beobachtend-neutral,
   weicher Dialog-CTA, kein Bullet-/P.S.-Druck). → `reference/tonalitaet-familien.md`

Quer dazu liegt immer **DISC** (`{{lead.disc_profile}}`): D/I/S/C + Kombis
steuern Wortwahl, Länge, Rhythmus, CTA-Frame innerhalb der gewählten Familie.
→ `reference/disc-system.md`

## Workflow

### 1. Spec aufnehmen
Lies zuerst, was Anthony schon gesagt hat. Fehlt eine der fünf Achsen und lässt
sie sich nicht sinnvoll defaulten, frag **kompakt mit Auswahl-Buttons**
(`ask_user_input_v0`) — eine Frage pro fehlender Achse, nie mehr als nötig.
Sensible Defaults, wenn Anthony nur grob spezifiziert:
- Familie: `AUGENHÖHE` für DACH-Technik-Entscheider (R&D/Einkauf/Technik),
  sonst `DISC-SALES`.
- Region/Locale: `DACH`/`de`, wenn nichts gesagt.
- CTA: `15D`.
- Signale: `mit`, wenn das Playbook/der Kontext Signale nahelegt, sonst `ohne`.
- DISC: bleibt als `{{lead.disc_profile}}` im Prompt; Default-Fallback im Prompt
  ist immer `C`.

Wenn Anthony eine **ganze Sequenz** will („alle 9", „die EU-ohne-Signale-Master"),
generiere die Positionen der Reihe nach, jede als eigenen vollständigen Prompt.

### 2. Bausteine + Blueprint laden
- `reference/sequenz-blueprints.md` → Job, Länge, Format, CTA-Minuten, Verbote
  der Position; Signale-Delta; Region/CTA-Guardrails.
- `reference/disc-system.md` → DISC-Profile + Wortzahl-Matrix für genau diese
  Position (Längen schrumpfen über die Sequenz!).
- `reference/hausstil-bausteine.md` → die wörtlichen Block-Vorlagen
  (Output-Regel, Sprach-Regel, CTA-Regel, DISC-Header, Kontext-Blöcke,
  Qualitäts-Check, Finaler Reminder).
- `reference/platzhalter.md` → exakte Platzhalter + welches Playbook-Feld sie füllt.
- `reference/tonalitaet-familien.md` → Familien-Unterschiede + welche Blöcke je
  Familie rein/raus.

### 3. Prompt zusammenbauen (fixe Reihenfolge)
Halte diese Abschnittsreihenfolge ein — sie ist der Hausstil:

```
1.  ABSOLUTE OUTPUT-REGEL           (immer; wörtlich aus Bausteinen)
2.  CTA-KERNREGEL                   (ab Email 2 / immer bei DISC-SALES)
3.  SPRACH-REGEL                    (immer; Locale-Logik je Region)
4.  DISC-SCHREIBSTIL                (immer; Profile + Kombis + Normalisierung)
5.  ROLLE (intern)                  (immer)
6.  PERSONA-ZUORDNUNG (intern)      (immer; {{persona.*}} + {{playbook.icps}})
7.  PRODUKT-/FIRMENKONTEXT (intern) ({{organization.*}} + {{playbook.*}})
8.  RECHERCHE-INPUTS (intern)       ({{lead.*}})
9.  SEQUENZ-KONTEXT                 (Position-Job; {{previous_email_body}} ab E2)
10. HIERARCHIE DER PERSONALISIERUNG (Signale-mit/ohne entscheidet Gewichtung)
11. AUFBAU DER E-MAIL               (Position-spezifische Struktur)
12. INTERNE QUALITÄTS-PRÜFUNG       (Checkliste)
13. FINALER REMINDER                (✅/❌-Liste)
14. STIL-REFERENZEN                 (nur DISC-SALES: 4 Beispiele, je 1 Profil/Kombi)
```
Bei `AUGENHÖHE` entfallen 1.-Block-Härte teils (siehe Familien-Datei): keine
Bullet-Pflicht, kein P.S.-Druck, weicher Dialog-CTA statt Termin-Zwang, oft nur
1 statt 4 Stil-Referenzen.

### 4. Validieren (vor Ausgabe)
- **Platzhalter exakt** gegen `reference/platzhalter.md`. Kein erfundener
  Platzhalter, kein ausgefüllter Wert, keine Tippfehler (`{{lead.buying_signals}}`
  nicht `{{buying_signals}}`).
- **Anti-Halluzination**: Prompt zwingt das Modell, nur Fakten aus Input zu
  nutzen; keine erfundenen Deliverables/Fristen (kein „48h-Audit/Quick-Check/
  Marktradar/ROI-Vergleich" als Köder — das ist verboten, siehe Bausteine).
- **CTA-Disziplin**: korrekte Minuten für die Position; bei DISC-SALES immer
  Termin-Ask; bei AUGENHÖHE offenes Gesprächsangebot. Region-Guardrail geprüft
  (Vorort → bei USA/Asien auf digital drehen).
- **Sprachkonsistenz**: Sprach-Regel zwingt EINE Sprache durchgängig inkl. CTA +
  Schlussgruß (häufigster Fehler: DE-Body / EN-CTA).
- **Länge/Format** passt zur Position und schrumpft sequenzgerecht.

### 5. Ausgeben
Gib den fertigen Prompt als sauberen Block aus (Anthony kopiert ihn 1:1 in
amplifa). Bei mehreren Positionen je einen klar betitelten Block
(`### EMAIL 3 · OHNE SIGNALE · DACH · 15D · AUGENHÖHE`). Kurz dazu: welche Achsen
gesetzt wurden und welche Defaults du angenommen hast — knapp, kein Roman.

## Was bewusst NICHT passiert
- Keine echten Mails schreiben (das macht amplifa zur Laufzeit).
- Keine Platzhalter füllen.
- Keine neuen Platzhalter erfinden, die amplifa nicht kennt.
- Kein Verbiegen der Sektionsreihenfolge — der Hausstil ist Teil des Produkts.

## Referenzdateien
- `reference/platzhalter.md` — kanonischer Platzhalter-Katalog + Playbook-Mapping
- `reference/hausstil-bausteine.md` — wörtliche, kopierbare Block-Vorlagen
- `reference/disc-system.md` — DISC-Profile, Kombis, Wortzahl-Matrix pro Position
- `reference/sequenz-blueprints.md` — die Positionen + Signale/Region/CTA-Achsen
- `reference/tonalitaet-familien.md` — DISC-SALES vs. AUGENHÖHE
