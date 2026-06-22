---
name: playbook-generator
description: Erstellt komplette amplifa-Kampagnen-Playbooks pro Kunde/Produktgruppe – exakt in der Block-Struktur der amplifa-App. IMMER nutzen, wenn der User ein Playbook, Personas, Use Cases, Reference Customers, Proof Points oder Product Descriptions für einen Kunden/eine Branche braucht. Zieht IMMER zuerst den Onboarding/Kickoff-Call aus Fathom, recherchiert dann Firma + Produktgruppen und liefert jeden Block einzeln, copy-paste-fertig.
argument-hint: <Kunde/Firma> [optional: Produktgruppe(n), Sprache]
---

# Playbook-Generator (amplifa)

Baut für einen amplifa-Kunden ein oder mehrere **Outbound-Playbooks**. Ein Playbook ist die Inhalts-Grundlage,
aus der die amplifa-AI später die Mails generiert – es muss daher **sitzen und exakt der App-Block-Struktur
entsprechen**. Output = pro Playbook **jeder Block einzeln, fertig zum Kopieren** in die App-Felder.

Die exakte Block-Struktur, das Format jedes Blocks und ein vollständiger Goldstandard (GBN Systems) stehen in
**`playbook-template.md`** (gleicher Ordner). **Diese Datei vor dem Bauen lesen** und Format/Länge/Ton 1:1 treffen.

## Pflicht-Reihenfolge (nicht überspringen)

### 1. Onboarding/Kickoff-Call aus Fathom ziehen — IMMER zuerst
Der **Fathom-MCP** ist die primäre Wahrheitsquelle für Angebot, Produktgruppen, Zielkunden, ICP, Sprache,
Personas, Value Proposition, Referenzen und Proof Points. Konkreter Ablauf mit den Fathom-Tools:

1. **Call suchen:** `search_meetings` mit `query = <Kundenname>` und `recorded_by = "anyone"`
   (org-weit, nicht nur eigene Aufnahmen). Liefert Titel, Datum, `recording_id`, `url` + Summary-Snippet.
   - Falls der MCP-Server-Name als UUID erscheint (`mcp__<uuid>__search_meetings`): das ist Fathom – Tool an der
     Funktion (`search_meetings`/`get_meeting_summary`/`get_meeting_transcript`/`list_meetings`) erkennen, nicht am UUID.
   - Tool nicht sichtbar? Erst `ToolSearch "+fathom"` bzw. „meeting transcript summary"; wenn weiterhin nichts:
     Fathom ist nicht verbunden → **sagen, nicht halluzinieren**, und Call-Notizen vom User erfragen.
2. **Richtigen Call wählen:** das **Onboarding/Kickoff** nehmen (Titel enthält „Onboarding"/„Kickoff", jüngstes).
   Bei mehreren relevanten Calls (z. B. zusätzlich Pitch/Pre-Sales) kurz die Liste zeigen. Der **Pitch-/Pre-Sales-Call
   enthält oft die Service→Playbook-Segmentierung** und lohnt sich als Zweitquelle.
3. **Inhalte ziehen:** `get_meeting_summary(recording_id)` für Überblick + Action Items, dann
   `get_meeting_transcript(recording_id, url)` für die Detail-Wahrheiten (exakte Value Prop, In-/Out-of-Scope,
   Pains, Personas, Geo/Industrie-Targeting). Transkripte sind groß → max. ~3 pro Lauf.
4. **Scope extrahieren:** explizit **In-Scope-Services** (= Playbooks) und **Out-of-Scope** (nie bespielen),
   Zielregion/PLZ, Zielbranchen, Personas/Rollen, Kernbotschaft. Out-of-Scope auch dann ausschließen, wenn es
   auf der Website steht.

### 2. Firma & Produktgruppen recherchieren
- Auf Basis des Calls die Firma **per Web** recherchieren: Website, Leistungen, Produkte/**Produktgruppen**,
  Branchen, Referenzen, Kundenstimmen, Zahlen/Jahre, Zielmärkte, Sprache des Zielmarkts.
- Ziel: belegbare Fakten für Product Description, Use Cases, Reference Customers und Proof Points sammeln.
- Nichts erfinden. Unbelegtes später mit `(zu verifizieren)` markieren.

### 3. Playbook-Schnitt festlegen
- Aus Call + Recherche ableiten, **welche Playbooks** sinnvoll sind. Faustregel: **ein Playbook pro Produktgruppe /
  Angebot / klar abgegrenztem Zielsegment** (so wie GBN „Mechatronische Entwicklung und Konstruktion" als ein
  Playbook von mehreren führt).
- Dem User **kurz die vorgeschlagene Playbook-Liste mit Titeln zeigen** (1 Zeile je Playbook, Titel = Produktgruppe,
  nicht Firmenname) und bestätigen lassen, bevor alle Blöcke ausformuliert werden. Bei klarem Auftrag direkt bauen.

### 4. Pro Playbook alle 6 Blöcke bauen
Exakt nach `playbook-template.md`, in dieser Reihenfolge:
1. **Product Description** (3 Absätze + `INDUSTRY:` + `USPs:` durchnummeriert)
2. **Value Proposition** (1 Absatz, Outcome)
3. **Target Personas (N)** (je Karte: Name, Titel-Zeile, `Pain Points:` mit 4–6 Bullets aus Sicht der Person)
4. **Use Cases (N)** (je: fetter Titel + 1 Absatz Ausgangslage→Lösung→Ergebnis)
5. **Reference Customers (N)** (je: Firma + `Name, Rolle` + 1 Absatz Kundenstimme)
6. **Proof Points (N)** (je: fetter Titel/Behauptung + 1 Absatz Beleg)

### 5. Copy-paste-fertig ausgeben
- **Jeder Block als eigener, klar abgegrenzter Abschnitt** mit Überschrift `=== <Block-Name> ===`, darunter der reine
  Inhalt zum Kopieren (kein Meta-Kommentar im Inhalt).
- Bei mehreren Playbooks: pro Playbook ein Abschnitt mit `Playbook-Titel` + `Language` (z. B. `de`), darunter die 6 Blöcke.
- So formatieren, dass der User jeden Block ohne Nacharbeit in das passende App-Feld einfügen kann.

## Qualitätsregeln
- **Sprache = Sprache des Zielmarkts** des Kunden (DACH → Deutsch). Gilt für alle Blöcke und Beispiele.
- Inhalte **aus Call + Recherche belegt**, branchen-/firmenspezifisch – keine generischen Platzhalter, keine erfundenen
  Zahlen/Referenzen. Unbelegtes klar mit `(zu verifizieren)` kennzeichnen.
- Personas mit **echten Titeln, echten Schmerzen** des realen Buying-Centers (technisch + regulatorisch + operativ +
  kaufmännisch), Pain Points aus Ich-/Er-Sie-Perspektive.
- Format, Länge und Ton **am Goldstandard in `playbook-template.md` kalibrieren** (nicht kürzer/abstrakter werden).
- `N` (Anzahl Personas/Use Cases/Referenzen/Proof Points) aus der tatsächlichen Substanz ableiten; Orientierung:
  4–6 Personas, 4–6 Use Cases, 3–5 Reference Customers, 4–6 Proof Points.

## Connectors / Rechte
Fathom (MCP, Onboarding/Kickoff lesen) – **Pflicht-Erstquelle**. Web-Recherche für Firma/Produktgruppen. Reine
Lese-Tools dürfen vorab freigegeben sein.
