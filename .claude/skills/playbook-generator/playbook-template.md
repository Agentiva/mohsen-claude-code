# amplifa Playbook – Block-Struktur (Goldstandard)

Dies ist die **exakte Block-Struktur**, wie sie in der amplifa-App (`/admin/organizations/.../playbooks/...`)
existiert. Ein Playbook = die Inhalts-Grundlage, aus der die AI später die Outbound-Mails generiert.
**Jeder Block unten wird einzeln in ein Feld der App kopiert.** Deshalb muss der Generator pro Playbook
**jeden Block getrennt und copy-paste-fertig** ausgeben – exakt in dieser Reihenfolge, in dieser Form,
in **derselben Sprache wie der Zielmarkt des Kunden** (DACH = Deutsch).

> Die App setzt selbst: `Status` (Draft), `Language`, `Created`, `Last updated`, `Discussion`.
> Diese sind **kein** generierter Inhalt. Nur `Language` muss der Generator kennen (z. B. `de`).

Pro Playbook gibt es **genau diese 6 Inhalts-Blöcke** in dieser Reihenfolge:

1. Product Description
2. Value Proposition
3. Target Personas (N)
4. Use Cases (N)
5. Reference Customers (N)
6. Proof Points (N)

Der **Playbook-Titel** ist der Name der Produktgruppe / des Angebots (z. B. „Mechatronische Entwicklung
und Konstruktion"), **nicht** der Firmenname.

---

## Block 1 — Product Description

Format: **3 Fließtext-Absätze**, danach zwei Strukturzeilen `INDUSTRY:` und `USPs:`.

- **Absatz 1:** Wer ist die Firma, Kernpositionierung, Erfahrung/Jahre, für wen sie arbeitet. Wenn eine
  Angabe (z. B. Mitarbeiterzahl) nicht belegt ist → ehrlich so schreiben („wird auf der Website nicht genannt"),
  nicht erfinden.
- **Absatz 2:** Was ist die Kernleistung dieser Produktgruppe konkret (Prozess, Leistungstiefe, Einstiegspunkte).
- **Absatz 3:** Marktpositionierung & Differenzierung (was unterscheidet sie vom Wettbewerb).
- `INDUSTRY:` komma-separierte Branchen/Sub-Sektoren.
- `USPs:` durchnummeriert `1. … 2. … 3. …` (5–8 USPs), je ein prägnanter Satz.

**Goldstandard (GBN Systems / „Mechatronische Entwicklung und Konstruktion"):**

> GBN Systems ist ein bayerischer B2B-Partner für mechatronischen Gerätebau mit über 35 Jahren Erfahrung. Das
> Unternehmen arbeitet für anspruchsvolle Technologieunternehmen, Start-ups, Spin-offs, Forschungsorganisationen
> und industrielle Hightech-Anbieter, die komplexe technische Produktideen in marktfähige Geräte überführen wollen.
> Die genaue Unternehmensgröße wird auf der Website nicht genannt; positioniert wird GBN Systems als erfahrener
> One-Stop-Shop für „leistungsstarke Mechatronik – Made in Bavaria".
>
> Kernleistung ist die mechatronische Entwicklung und Konstruktion inklusive Gerätebau, Feinmechanik, Montage,
> Fertigung sowie Überführung von Prototypen in Vorserie und Serie. GBN Systems verbindet mechanische Konstruktion,
> Präzisionsfertigung, Steuerungstechnik, Sensorik, Programmierung und Montage in einem durchgängigen
> Umsetzungsprozess. Kunden können bereits in frühen Entwicklungsphasen einsteigen – etwa bei der Übersetzung einer
> technischen Vision in Zeichnungen, funktionsfähige Prototypen, produktionsnahe Baugruppen oder serienfähige Geräte.
>
> Im Markt positioniert sich GBN Systems über die Kombination aus Entwicklungskompetenz, Fertigungstiefe,
> regulatorischem Verständnis und regionaler Lieferfähigkeit. Besonders differenzierend sind der One-Stop-Shop-Ansatz
> mit weniger Schnittstellen, die nachgewiesene Erfahrung in regulierten Bereichen wie Medizintechnik, Biotechnologie,
> Radiopharmazeutik und GMP-nahen Anwendungen sowie die Fähigkeit, Spezialwerkstoffe wie Wolfram und Blei zu handhaben.
>
> INDUSTRY: Mechatronischer Gerätebau, Medizintechnik, Hightech-Fertigung, Präzisionstechnik, Auftragsfertigung
>
> USPs: 1. Entwicklung, Konstruktion, Gerätebau, Feinmechanik, Montage und Serienüberführung aus einer Hand.
> 2. Über 35 Jahre Erfahrung mit komplexen mechatronischen Produkten. 3. Nachgewiesene Projektpraxis in regulierten
> Umfeldern wie GMP-naher radiopharmazeutischer Herstellung. 4. Fähigkeit zur Überführung von Prototypen in Vorserie
> und Serienfertigung. 5. Lokales bayerisches Netzwerk mit kurzen Lieferwegen. 6. Erfahrung mit Spezialwerkstoffen
> wie Wolfram und Blei. 7. One-Face-to-the-Customer-Ansatz mit pragmatischer Projektabwicklung.

---

## Block 2 — Value Proposition

Format: **1 kompakter Absatz** (2–4 Sätze). Was erreicht der Kunde des Kunden konkret – Outcome, nicht Feature.

**Goldstandard:**

> GBN Systems unterstützt anspruchsvolle Tech-Unternehmen dabei, komplexe mechatronische Geräte schneller und sicherer
> von der Idee über Prototyp und Vorserie bis zur Serienfertigung zu bringen. Durch Entwicklung, Konstruktion,
> Feinmechanik, Gerätebau, Montage und Fertigung aus einer Hand reduziert GBN Systems Schnittstellen, Abstimmungsaufwand
> und Umsetzungsrisiken – besonders in regulierten und präzisionskritischen Märkten.

---

## Block 3 — Target Personas (N)

`N` Persona-Karten (Beispiel hatte 5). Jede Karte hat **genau** diese drei Teile:

1. **Name:** Rolle + Vorname, z. B. `Entwicklungsleiter Thomas`. (Rolle als Archetyp + ein menschlicher Vorname.)
2. **Titel-Zeile:** komma-separierte alternative Jobtitel (DE + EN gemischt, wie sie real vorkommen).
3. **`Pain Points:`** — **4–6 Bullets**, jeweils aus Sicht der Person formuliert (`Er muss …`, `Sie steht unter Druck …`,
   `Er benötigt …`). Konkrete, kaufrelevante Schmerzen dieser Rolle in genau diesem Markt – keine Floskeln.

**Goldstandard (eine Karte):**

> **Entwicklungsleiter Thomas**
> Leiter Entwicklung, Head of R&D, Entwicklungsleiter Mechatronik, Technischer Leiter, Director Engineering
>
> Pain Points:
> - Er muss komplexe mechatronische Entwicklungen in belastbare, serienfähige Geräte überführen, ohne intern alle
>   Fertigungs- und Montagekompetenzen vorzuhalten.
> - Er steht unter Druck, Prototypen nicht nur funktionsfähig, sondern frühzeitig serienreif, montierbar und marktfähig
>   auszulegen.
> - Er muss entscheiden, wann teure Investitionen in Werkzeuge, Fertigungsmittel oder Serienprozesse ausgelöst werden.
> - Er benötigt einen Partner, der die technische Vision in Zeichnungen, Prototypen, Vorserien und serienfähige Geräte
>   übersetzt, ohne dass an jeder Schnittstelle Information verloren geht.

Weitere Beispiel-Personas aus demselben Playbook (zur Kalibrierung der Bandbreite): `Medizintechnik-Produktmanagerin Anna`,
`Operations-Direktor Jens`, `Fertigungsleiterin Sabine`, `Herstellungsleiter Dr. Markus`.
→ Mix aus technischen, regulatorischen, operativen und kaufmännischen Rollen entlang des realen Buying-Centers.

---

## Block 4 — Use Cases (N)

`N` Use Cases (Beispiel hatte 6). Jeder Use Case = **fetter Titel** + **1 Absatz** nach Logik
**Ausgangslage → Lösung → Ergebnis** (in Fließtext, nicht als Labels).

**Goldstandard (zwei Beispiele):**

> **Vom HealthTech-Prototyp zur marktfähigen Vorserie**
> Junge HealthTech-Unternehmen müssen technische Visionen schnell in funktionsfähige und investorenfähige Geräte
> überführen, verfügen intern aber oft nicht über alle Entwicklungs- und Fertigungskapazitäten. GBN Systems übernimmt
> Konstruktion, Prototypenbau, Montage und Vorbereitung der Vorserie aus einer Hand. Dadurch sind die Produktideen zum
> richtigen Zeitpunkt prüf- und finanzierbar, ohne dass das Team alle Kompetenzen selbst aufbauen muss.

> **Serienüberführung komplexer mechatronischer Geräte**
> Entwicklungsteams stehen häufig vor dem Problem, dass ein Prototyp zwar technisch funktioniert, aber noch nicht
> serienreif konstruiert, montierbar oder wirtschaftlich produzierbar ist. GBN Systems verbindet mechatronische
> Entwicklung mit serienreifer Konstruktion und Fertigung und führt das Gerät kontrolliert in Vorserie und Serie über.
> Das konkrete Ergebnis ist ein wirtschaftlich produzierbares Gerät mit weniger Schnittstellen und geringerem Risiko.

Weitere Beispiel-Titel: „Regulatorisch anspruchsvolle Baugruppen für Biotechnologie und Pharma", „Präzisionsfertigung
für Halbleitergeräte und Drahtbonder", „Mechatronische Speziallösungen für Nuklearmedizintechnik und Radiopharmazeutik",
„Strategischer Lieferantenwechsel für präzise Hightech-Komponenten".

---

## Block 5 — Reference Customers (N)

`N` Referenzkunden (Beispiel hatte 4). Jeder Eintrag:

1. **Firmenname** (z. B. `Logitogo GmbH`)
2. **Kontaktperson:** `Name, Rolle` (z. B. `Andreas Beck, Geschäftsführer`)
3. **1 Absatz** Beschreibung der Zusammenarbeit / Kundenstimme (warum/wie lange/was geschätzt wird).

> Nur Referenzen aufnehmen, die in Onboarding/Recherche **belegt** sind. Wenn keine belegten Referenzen vorliegen:
> Block leer lassen bzw. mit `(zu verifizieren – aus Onboarding ergänzen)` markieren, **nicht erfinden.**

**Goldstandard (ein Eintrag):**

> **Logitogo GmbH**
> Andreas Beck, Geschäftsführer
> Andreas Beck, Geschäftsführer der Logitogo GmbH, arbeitet seit 2001 mit GBN Systems zusammen. Er hebt die
> langjährige, vertrauensvolle Partnerschaft, unbürokratische Unterstützung und pragmatische, projektgetriebene
> Lösungen hervor.

---

## Block 6 — Proof Points (N)

`N` Proof Points (Beispiel hatte 5). Jeder Proof Point = **fetter Titel (die Behauptung)** + **1 Absatz**, der sie belegt
(Quelle/Kundenstimme/Kennzahl). Proof Points sollen Personas/Use Cases stützen.

> Belegbar halten. Unbelegtes mit `(zu verifizieren)` markieren statt zu erfinden.

**Goldstandard (zwei Beispiele):**

> **Über 35 Jahre Erfahrung im mechatronischen Gerätebau**
> Die Website nennt ausdrücklich „über 35 Jahre Erfahrung im Gerätebau" und beschreibt, dass GBN Systems seit Jahrzehnten
> komplexe mechatronische Produkte für Medizintechnik, additive Fertigung, Halbleiterindustrie und weitere
> anspruchsvolle Anwendungsfelder realisiert.

> **Reibungsloser Übergang von Prototypenfertigung in Serienfertigung bei ITM Medical Isotopes**
> In der Kundenstimme von ITM Medical Isotopes wird der Übergang von der Prototypenfertigung in die Serienfertigung von
> Generatorsäulen und Generatorbodies ausdrücklich als reibungslos beschrieben.

Weitere Beispiel-Titel: „Kundenpartnerschaft seit 2001 mit Logitogo", „Über 10 Jahre gemeinsame Projektlösungen mit
ITM Medical Isotopes", „Kontinuierlich gewachsenes Volumen und Produktportfolio bei Repligen".
