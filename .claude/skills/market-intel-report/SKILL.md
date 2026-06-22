---
name: market-intel-report
description: Erstellt Market-Intelligence- und Onboarding-Reports für neue amplifa-Kunden. IMMER nutzen, wenn der User einen Marktbericht, Onboarding-Report, eine Markt-/Wettbewerbsanalyse oder Kundenrecherche für ein neues B2B-Mandat braucht oder sich auf ein Onboarding/Kickoff-Gespräch vorbereiten will – auch bei Formulierungen wie "recherchier mal Firma X", "bau mir das Onboarding für Kunde Y" oder "bereite mein Onboarding mit Z vor". Liefert eine konsistente DACH-fokussierte Struktur mit validierten Marktdaten und TAM/SAM/SOM PLUS einer vollumfänglichen Unternehmens-Zusammenfassung, Produkt-/Produktgruppen-Aufschlüsselung, geschärften ICP & Personas und einem fertigen Onboarding-Fragenkatalog (offene/unklare Punkte), damit der User bestmöglich vorbereitet in den Call geht.
argument-hint: [kundenname oder domain]
allowed-tools: Bash(*), WebSearch, WebFetch
---

# Market-Intelligence-Report (amplifa Onboarding)

Erzeugt einen einheitlichen, **deep-recherchierten** Markt-/Onboarding-Report für ein neues amplifa-Mandat. Zielmarkt ist DACH-Industrie-Mittelstand (Maschinenbau, Chemie, Medizintechnik, Automotive u. ä.); Geschäftsmodell ist Pay-per-Meeting-Outbound über Clay/Apollo/Instantly.

**Qualitätsanspruch (nicht verhandelbar):** Jeder Report enthält validierte, mehrfach belegte Marktzahlen, ein nachvollziehbares TAM/SAM/SOM-Modell und einen Meeting-Forecast. Keine reinen Schätzungen ohne Beleg; jede Zahl bekommt eine Quelle oder ist klar als triangulierte Annahme markiert.

## Ablauf

### 1. Kunde fixieren
Name, Domain, Branche, Angebot. Bei Lücken kurz nachfragen statt raten. Produktmarke und Kernprodukt identifizieren (das adressierte Marktsegment hängt daran).

### 2. Deep Research — Pflicht, nicht optional
Mindestens **8–12 Web-Suchen** in mehreren parallelen Batches (Tool-Calls in einer Message bündeln). Tiefer gehen, bis jede Report-Sektion belegt ist. Pflicht-Rechercheblöcke:

- **Unternehmensprofil & Produktüberblick:** Größe (MA, Umsatz via North Data/DDW/Companyhouse), Standorte, Gründung, Eigentümer, Hauptansprechpartner, Positionierung, Referenzen/Zertifizierungen. Firmen-Website per `WebFetch` **vollständig** auswerten: alle Leistungen einsammeln und in **Produktgruppen clustern** (was hängt zusammen, was eignet sich als Outbound-Türöffner). Reicht für eine vollumfängliche Unternehmens-Zusammenfassung (Fließtext) + Produktgruppen-Tabelle.
- **Marktgröße (TAM):** Globale + DACH-Marktzahlen für das **konkrete Produktsegment** (nicht den Oberbegriff). Marktdaten von kommerziellen Research-Häusern **triangulieren** — sie streuen je nach Abgrenzung um Faktor 2–5. Immer ≥2 unabhängige Quellen pro Kernzahl, Bandbreite + CAGR angeben.
- **Marktdynamik:** Strukturelle Treiber (langfristig) UND zyklische Lage (aktuell, z. B. Branchenverbände wie VDW/VDMA/ZVEI) — das Timing-Argument fürs Messaging.
- **Bottom-up Account-Universum:** Anzahl Zielfirmen in DACH (Statista/Destatis/Branchenverbände/Handwerkszahlen) für die SAM/SOM-Account-Linse.
- **Regulatorik/Normen:** relevante Zertifizierungen als Türöffner (IATF/EN9100/ISO13485 etc.).
- **Wettbewerb:** 4–6 DACH-Wettbewerber **mit validierten Eckdaten** (MA/Umsatz/Eigentümer/aktuelle Lage). Aktuelle Schwächephasen (Insolvenz/Kurzarbeit/Übernahme) sind Switch-Hebel — gezielt suchen.
- **ICP, Buying Center, Pains, Buying-Signals** des Zielmarkts.

### 3. TAM / SAM / SOM modellieren (zwei Linsen)
- **Linse A – Produktmarkt:** Königs/Kunden Umsatzpotenzial. TAM (global/DACH Segment) → SAM (DACH adressierbar, Nische × Anteil) → SOM (über Outbound neu erschließbarer Jahres-Auftragswert).
- **Linse B – Account-Universum (amplifa-relevant):** TAM (alle Zielbetriebe DACH) → SAM (ICP-fit Accounts) → SOM (in 12 Monaten bearbeitbare Accounts).
- **Meeting-Forecast:** SOM-Accounts → kontaktierte Personen → Meeting-Rate (industrielles Nischen-Outbound ~1,5–3 %) → qualifizierte Erstgespräche/Jahr in 3 Szenarien (konservativ/base/optimistisch).
- Jede Herleitung als Formel/Logik offenlegen. Annahmen kennzeichnen.

### 4. Outbound-Winkel ableiten
Value Proposition, 4–6 priorisierte Hooks (zyklische Lage berücksichtigen!), Kanal-Mix (E-Mail/LinkedIn/AI-Voice) mit Begründung, Sprache, erste Kampagnen-Hypothese + ggf. Switch-Segment gegen geschwächte Wettbewerber.

### 5. Report füllen
Nach der Struktur in `report-template.md`. Jede Sektion belegen; keine Sektion leer lassen — bei Unsicherheit als Annahme markieren. **Pflicht-Mehrwert für die Onboarding-Vorbereitung:**
- **Vollumfängliche Unternehmens-Zusammenfassung** (Steckbrief-Tabelle + Fließtext-Absatz, der den Kunden in 6–10 Sätzen erklärbar macht).
- **Produkte & Produktgruppen** als geclusterte Tabelle (mit Erlösmodell & Türöffner-Eignung).
- **ICP mit Tier-Priorisierung** und **Personas/Buying Center** konkret ausfüllen (echte Jobtitel, keine Platzhalter).
- **Onboarding-Fragenkatalog** (Sektion 10): gruppierte, sofort vorlesbare Fragen. Wo möglich die recherchierte Annahme in Klammern mitliefern, sodass der Call zur **Bestätigung** statt zur Datensammlung wird.
- **Offene Annahmen/unklare Punkte** (Sektion 11) explizit auflisten: Annahme → warum unsicher → wie im Call klären.

### 6. Quellen
Vollständige Quellenliste mit klickbaren Markdown-Links, gruppiert (Unternehmen / Markt / Wettbewerb). Für Aussagen über amplifa https://amplifa.ai nutzen.

## Output

Zusammenhängender Report in Markdown nach `report-template.md`. Am Ende immer zwei nächste Schritte anbieten:
1. **Gebrandetes PDF:** Übergabe an den Skill `[[amplifa-report-design]]`, der den Inhalt 1:1 ins amplifa-Hausdesign (20–30 Seiten, Querformat) rendert.
2. **Aktivierung:** Prospect-Liste + Outbound-Sequenz aus der ersten Kampagnen-Hypothese.

Wenn der User ein PDF/eine Präsi/„so einen Report wie die Vorlage" will, direkt `amplifa-report-design` mit diesem Inhalt aufrufen.

## Hinweise

- **Validiert vor schön:** Sachlich und belegt, keine Marketing-Floskeln. Lieber Bandbreite mit Quelle als präzise wirkende erfundene Zahl.
- **Datenqualitäts-Hinweis** an den Report-Anfang stellen, wenn Marktzahlen stark streuen oder Kundenfinanzen nicht öffentlich sind.
- DACH-Fokus: Wettbewerber und Marktzahlen auf den deutschsprachigen Raum beziehen, sofern nicht anders gewünscht.
- Annahmen klar markieren, damit sie im Onboarding-Call verifiziert werden können (Sektion "Offene Annahmen").
- Umsatz/Marge/Win-Rate des Kunden sind oft nicht öffentlich → als triangulierte Schätzung (z. B. MA × Branchen-Umsatz/MA) ausweisen und explizit zur Verifikation flaggen.
