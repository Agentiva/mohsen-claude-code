# DISC-System

DISC ist der Hebel, der eine Mail von generisch zu personalisiert macht. Es
steuert nicht nur Wortwahl, sondern **Länge, Rhythmus, Format und CTA-Frame**.
Die Profilblöcke kommen direkt nach dem DISC-Header (siehe Bausteine).

## Inhalt
1. Profil-Bausteine D / I / S / C (Voll-Variante, DISC-SALES)
2. Profil-Kurzfassung für AUGENHÖHE-Familie
3. Kombinationen
4. Wortzahl-Matrix pro Sequenz-Position
5. Default-Regel

---

## 1. Profil-Bausteine (DISC-SALES, Voll-Variante)

`«LEN»` = Wortzahl aus der Matrix (Abschnitt 4) für die jeweilige Position.

```
**PROFIL D (Dominant) — Macher, ergebnisorientiert, ungeduldig**
LÄNGE: «LEN-D» (kürzer als andere Profile)
STRUKTUR: kurze Absätze; Hook → Pain+Lösung kombiniert → CTA
SATZRHYTHMUS: Kurze Sätze. Punkt. Punkt. Selten Nebensätze.
EMPFOHLENE VERBEN: liefern, gewinnen, sichern, beschleunigen, durchsetzen, skalieren, sparen
EMPFOHLENE NOMEN: Ergebnis, Marktanteil, Wettbewerbsvorteil, ROI, Geschwindigkeit, Pipeline, Hebel
VERBOTENE WÖRTER: vielleicht, eventuell, gemeinsam, behutsam, sorgfältig, harmonisch
PAIN-FRAMING: verlorenes Geschäft, verpasste Chance, Wettbewerber-Vorsprung
CTA-STIL: selbstbewusst, direkt (Stil-Beispiel auf Deutsch — in {{locale}} formulieren)

**PROFIL I (Influent) — beziehungsorientiert, enthusiastisch, visuell**
LÄNGE: «LEN-I»
STRUKTUR: persönlicher Hook → Vision/Pain → Lösung als Story → einladender CTA
SATZRHYTHMUS: variabel; längere Sätze mit Bildern; rhetorische Fragen wirken.
EMPFOHLENE VERBEN: gestalten, bewegen, inspirieren, sichtbar machen, gemeinsam entwickeln, prägen
EMPFOHLENE NOMEN: Vision, Wirkung, Sichtbarkeit, Marke, Bühne, Impact, Resonanz
VERBOTENE WÖRTER: Auditierung, Methodik, KPI, Spezifikation, prozessual, normiert
PAIN-FRAMING: verpasste Anerkennung, Stillstand der Marke, ungenutztes Potenzial
CTA-STIL: einladend, persönlich

**PROFIL S (Stetig) — beziehungstreu, harmoniebedürftig, risikoavers**
LÄNGE: «LEN-S»
STRUKTUR: wertschätzender Hook → sanfter Pain → ruhige Lösung mit Sicherheit → niedrigschwelliger CTA
SATZRHYTHMUS: ruhig, gleichmäßig, keine Druck-Sprache; Wir-Formulierungen.
EMPFOHLENE VERBEN: unterstützen, begleiten, sichern, bewahren, schrittweise verbessern
EMPFOHLENE NOMEN: Partnerschaft, Verlässlichkeit, Sicherheit, Kontinuität, Erfahrung, Vertrauen
VERBOTENE WÖRTER: aggressiv, disruptiv, sofort, durchbrechen, attackieren, kämpfen, dominant
PAIN-FRAMING: sanft, "vielleicht kennen Sie das" — nie Vorwurf, nie Drohung
CTA-STIL: niedrigschwellig, unverbindlich

**PROFIL C (Gewissenhaft) — analytisch, faktenorientiert, skeptisch**
LÄNGE: «LEN-C»
STRUKTUR: faktenbasierter Hook → präziser Pain mit Ursache-Wirkung → Mechanismus + Proof Point → konkreter CTA
SATZRHYTHMUS: strukturiert, präzise, substanziell; Branchenvokabular sauber.
EMPFOHLENE VERBEN: validieren, dokumentieren, verifizieren, optimieren, messen, nachweisen, quantifizieren
EMPFOHLENE NOMEN: Mechanismus, Methodik, Spezifikation, Toleranz, KPI, Datenbasis, Nachweis
VERBOTENE WÖRTER: spannend, aufregend, fantastisch, leidenschaftlich, gemeinsam (emotional)
PAIN-FRAMING: Effizienz-/Qualitätsproblem mit Ursache-Wirkung, belegt mit Zahlen
CTA-STIL: konkret, mit Mechanismus
```

## 2. Profil-Kurzfassung (AUGENHÖHE-Familie)

In dieser Familie steuert DISC Ton/Satzbau/Anker — aber innerhalb der
zurückhaltenden Grundhaltung (kein Marketing-Druck). Kurzform:

```
### D — Dominant (CEO, GF, Head of)
Direkt, kurze Sätze (~15 Wörter), kein Konjunktiv. Implikation zuerst, Zahlen vor
Erläuterung. Anker: frischestes strategisches Signal aus {{lead.buying_signals}}.
Vermeide Smalltalk/weiche Formulierungen. Wortzahl «LEN-D».

### I — Initiativ (Marketing, Sales, BD, Creative)
Lebendig, dialogisch; eine echte (nicht-werbliche) Frage erlaubt. Entwicklung/Vision
zuerst, dann Detail; Bezug auf {{lead.linkedin_posts}}/{{lead.linkedin_summary}}.
Vermeide trockene Faktenlisten. Wortzahl «LEN-I».

### S — Stetig (HR, Operations, Teamleitung, Familienunternehmen)
Ruhig, vertrauensbildend, mittellange Sätze; Konjunktiv ok. Stabilität/Risiko-
minimierung vor Wachstum; Referenz aus {{playbook.references}}. Anker: strukturelles
Signal. Vermeide Druck/Dringlichkeit. Wortzahl «LEN-S».

### C — Gewissenhaft (R&D, Engineering, Qualität, Technik, Einkauf-technisch)
Sachlich, präzise; Fachbegriffe/Kennzahlen erwünscht. Logik & Belege vor Nutzen-
versprechen. Anker: technisch konkretes Signal aus {{lead.buying_signals}} +
Proof-Point aus {{playbook.proof_points}}. Vermeide vage Behauptungen. Wortzahl «LEN-C».

Leer/unklar → C als Default. Mischprofil → dominantes Profil führt (~70/30).
```

## 3. Kombinationen
```
**KOMBINATIONEN (DC, IS, CD, DI, SC etc.)**
- Struktur, Länge und CTA-Frame des dominanten Profils (erster Buchstabe, 70%)
- 30% Wortwahl/Tönung des zweiten Profils einweben
- Beispiel "DC": D-Struktur (kurz), aber Faktenhärte/Proof-Point-Tiefe (C)
- Beispiel "IS": I-Struktur (bildhaft), aber Wir-Formulierungen/Partnerschaft (S)
- Beispiel "CD": C-Struktur (fakten), aber Hook/CTA etwas direkter (D)
- WICHTIG bei S-Anteil (Pattern-Interrupt/Provokation): Provokationsgrad runter,
  reflexive statt aggressive Frage.
```

## 4. Wortzahl-Matrix pro Sequenz-Position

Längen schrumpfen über die Sequenz (späterer Touch = höhere Dichte pro Wort).
Werte sind Body-Wortzahl (P.S. separat). Setze sie als `«LEN-D/I/S/C»` ein.

| Position | D | I | S | C |
|---|---|---|---|---|
| **E1 Cold-Open (DISC-SALES)** | 130–160 | 170–200 | 170–200 | 180–200 |
| **E1/Basis (AUGENHÖHE)** | 110–130 | 125–145 | 120–140 | 120–145 |
| **E2 Follow-up (Bullets)** | 130–150 | 160–180 | 160–180 | 170–190 |
| **E2 Follow-up (30-Min-Variante)** | 130–150 | 160–180 | 160–180 | 170–190 |
| **E2 Augenhöhe-Follow-up** | 100–130 (alle Profile, knapp) |||
| **E3 kompakt** | 110–150 (kürzer als E1/E2) |||
| **E4 ultrakurz** | 90–110 | 110–130 | 110–130 | 110–130 |
| **E5 P.S.-Recovery** | 130–145 + P.S.≤25 | 150–160 + P.S.≤30 | 150–160 + P.S.≤30 | 145–160 + P.S.≤30 |
| **E6 Perspektivwechsel** | 100–140 (DISC-abhängig) |||
| **E7 Story** | 140–160 | 160–175 | 160–175 | 160–175 |
| **E8 Pattern-Interrupt** | 130–150 | 150–165 | 150–165 | 145–165 |
| **E9 radikale Transparenz** | 120–140 | 135–155 | 135–155 | 130–150 |
| **Augenhöhe kurz-Variante** | 85–105 | 100–120 | 95–115 | 100–120 |
| **Augenhöhe mit P.S.** | 110–130 | 125–145 | 120–140 (kein P.S. bei S) | 120–145 |

Wenn eine gewünschte Position nicht in der Tabelle steht: nächstgelegene nehmen
und im Zweifel kürzer als länger.

## 5. Default-Regel
`{{lead.disc_profile}}` bleibt im Prompt; der im Prompt verankerte Fallback ist
immer **C** (sachlich, zurückhaltend) — nie raten, welches Profil der konkrete
Lead hat. Der Prompt beschreibt alle Profile; die Engine wählt zur Laufzeit.
