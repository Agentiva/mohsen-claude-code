# Lindner – Playbook-Überarbeitung: E-Mobilität / Fuhrpark & Off-Topic entfernen

**Problem (aus dem Strategie-Call 07.07.):** Die KI hat Nachrichten generiert, die anboten, den „Fuhrpark der E-Mobilität" zu übernehmen – komplett außerhalb von Lindners Produkten. Ursache: In den Playbooks steht zwar **kein** E-Mobilitäts-Text, aber die Produktsprache rund um die mobilen Schredder (**„diesel or 100% electric, tracked"**, **„off-grid / without transformer station"**, **„energy consumption"**) lässt das Modell zu EV/Fuhrpark/Energie abdriften.

**Fix (zweistufig):**
1. **Scope-Guardrail** (harte Negativ-Regel) in jedes Playbook UND in die Agenten-Nachrichten-Prompts.
2. **Reframing** der zweideutigen Antriebs-Sprache: „electric/diesel" = Antrieb der SCHREDDER-Maschine, kein Fahrzeug.

Dieser Guardrail ist zusätzlich zur bereits umgesetzten Wettbewerber-/Zulieferer-Prüfung (kein Konkurrent, kein Verkäufer an Lindner).

---

## 🔒 SCOPE GUARDRAIL (in JEDES Playbook + in die Agenten-Prompts einsetzen)

```
SCOPE GUARDRAIL — STRICT. Lindner manufactures and sells ONLY: industrial
shredders (single-shaft, twin-shaft, primary and secondary) and turnkey
shredding, sorting and RDF/SRF & wood-processing systems for waste, recycling
and alternative-fuel production — plus the related service (original spare
parts, maintenance, shaft reconditioning, Nexus performance monitoring).

Every message MUST stay strictly inside this scope. NEVER mention, offer,
imply, ask about, or connect Lindner to any OUT-OF-SCOPE topic, including:
- e-mobility, electric vehicles / EVs, EV charging or charging infrastructure
- vehicle fleets ("Fuhrpark"), fleet management, fleet electrification, telematics
- "mobility solutions", logistics or transport services
- energy supply, electricity/gas utility services, power trading, grid services
- photovoltaics/solar, wind, or ANY product Lindner does not manufacture

CLARIFICATION: when a Lindner machine is called "electric" or "diesel", this
refers ONLY to the drive of the SHREDDER itself (a stationary or tracked
processing machine) — it is NOT a vehicle and has nothing to do with
e-mobility, fleets or charging. "Off-grid / no transformer station" means the
shredder runs without a fixed on-site power connection — again nothing to do
with EVs.

If a prospect ALSO operates in e-mobility, energy, transport or any unrelated
field, IGNORE those activities entirely and address ONLY their waste /
recycling / shredding / RDF / wood-processing operations. If you cannot tie the
prospect to a genuine shredding/processing need, do NOT invent an offering —
skip the prospect rather than stray off-topic.
```

---

## Playbook 264 — Private Recyclers & Reprocessors

**Reframe (Use Case „Mobile on-site crushing"):**
- ALT: „The mobile Urraco series (diesel or 100% electric, tracked) enables on-site shredding…"
- NEU: „The mobile Urraco **shredder (with diesel or 100%-electric drive, tracked chassis)** enables on-site shredding with high throughput, FX quick-change and low energy consumption per tonne. *(The drive powers the shredding machine itself — it is not a vehicle.)*"

**Ergänzen:** Scope-Guardrail (oben) am Ende der Product Description.
Übrige Abschnitte (Value Proposition, Personae, Proof Points) bleiben unverändert – sie enthalten keinen Off-Topic-Inhalt.

---

## Playbook 263 — Municipal & Public Waste Operators

**Keine zweideutige Antriebs-Sprache** in diesem Playbook. **Ergänzen:** nur den Scope-Guardrail (oben) am Ende der Product Description.
Hinweis für die Personae: „Fuhrpark" NIE als Thema – Zielrolle ist Abfallbehandlung/Anlagenbetrieb, nicht der kommunale Fuhrpark.

---

## Playbook 262 — Cement, Energy & RDF Off-takers

**Wichtige Klarstellung im Guardrail-Kontext:** „Energy" kommt hier nur als **Kunde** vor (Kraftwerke/Zementwerke, die RDF verbrennen und dafür Lindner-Anlagen KAUFEN) — Lindner verkauft selbst KEINE Energie/Strom/Mobilität. **Ergänzen:** Scope-Guardrail (oben) am Ende der Product Description.
Übrige Abschnitte bleiben unverändert.

---

## Playbook 261 — Wood & Biomass Recyclers

**Reframe (Use Case „Mobile contract shredding"):**
- ALT: „The Urraco EVO mobile series (diesel or 100% electric, tracked) allows on-site shredding…"
- NEU: „The Urraco EVO mobile **shredder (diesel or 100%-electric drive, tracked chassis)** allows on-site shredding with high throughput, FX quick-change and low energy consumption per tonne. *(Drive of the shredding machine — not a vehicle.)*"

**Ergänzen:** Scope-Guardrail (oben) am Ende der Product Description.
Übrige Abschnitte bleiben unverändert.

---

## Agenten-Nachrichten-Prompts (dort entsteht die eigentliche Nachricht)

Denselben Scope-Guardrail-Block **oben in jeden System-/Step-Prompt** der 8 Agenten (Eastern Europe & Scandinavia × 4 Playbooks) einsetzen. Das war im 07.07.-Call der vereinbarte Hebel („wir müssen an eure System-Prompts für die Nachrichten ran"). Zusätzlich als eiserne Regel je Prompt:

```
Hard rule: If drafting this message would require referencing e-mobility,
vehicle fleets, charging, mobility or energy-supply services, STOP — those are
out of scope. Write only about shredding / recycling / RDF / wood-processing
needs. Keep the message short and specific to the prospect's processing operation.
```
