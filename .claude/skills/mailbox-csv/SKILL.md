---
name: mailbox-csv
description: Generiert E-Mail-Postfach-CSVs für neue Sending-Domains. IMMER nutzen, wenn der User Mailboxen, Postfächer, E-Mail-Adressen oder Sending-Accounts für Domains anlegen will, oder Namen plus Domains in eine Adressliste umwandeln will – auch wenn das Wort "CSV" nicht explizit fällt. Erzeugt pro Domain EXAKT 5 Adressvarianten nach festen Mustern.
argument-hint: [pfad-zur-input-datei] oder Namen+Domains inline
allowed-tools: Bash(py *), Bash(python3 *), Bash(python *)
---

# Mailbox-CSV-Generator

Wandelt eine Liste aus Vor-/Nachnamen und Domains in eine sauber normalisierte E-Mail-CSV um. Für amplifa-Sending-Setups (Instantly etc.).

## Eiserne Regel (niemals abweichen)

Pro Domain werden **exakt 5** Adressen erzeugt – nicht 4, nicht 6. Immer dieselben fünf Muster, immer in dieser Reihenfolge:

1. `vorname.nachname`
2. `v.nachname`
3. `vnachname`
4. `nachname.vorname`
5. `nachname`

`v` = erster Buchstabe des Vornamens.

## Normalisierung (vor dem Bau jeder Adresse)

- Alles klein schreiben.
- Umlaute/ß transliterieren: ä→ae, ö→oe, ü→ue, ß→ss (auch Á/À/ Â etc. → Grundbuchstabe).
- Leerzeichen, Bindestriche und Apostrophe im Namen entfernen (z. B. "Jean-Luc" → "jeanluc", "O'Brien" → "obrien").
- Bei mehreren Vornamen nur den ersten verwenden; bei mehrteiligen Nachnamen alle Teile ohne Trenner zusammenziehen ("von der Heyde" → "vonderheyde").
- Domain unverändert übernehmen, nur trimmen und kleinschreiben.

## Ablauf

1. Input einlesen. Erwartetes Format pro Zeile: `Vorname, Nachname, Domain` (CSV oder lose Liste). Wenn der User die Daten inline gibt, schreibe sie zuerst in eine temporäre Datei.
2. Skript ausführen. Auf Windows ist der Python-Launcher `py` (nicht `python3`/`python`, das sind nur Microsoft-Store-Platzhalter):

```bash
py ${CLAUDE_SKILL_DIR}/scripts/generate_mailboxes.py <input-datei> > <ausgabe-datei>
```

3. Ergebnis kurz prüfen: Stimmt die Zeilenzahl? (Anzahl Personen × 5). Eventuell entstandene Leerzeilen entfernen. Bei Auffälligkeiten (fehlende Domain, leerer Name) melden statt still zu raten.
4. Pfad zur fertigen Datei ausgeben.

Das Skript erzwingt die 5-Varianten-Regel und die Normalisierung deterministisch – verlasse dich darauf statt die Adressen selbst zu tippen.

## Output: Benennung & Speicherort (immer)

- **Speicherort:** immer im Download-Ordner des Users (`%USERPROFILE%\Downloads` bzw. `~/Downloads`).
- **Dateiname:** `mailboxes_<domain>_<YYYY-MM-DD>.csv`.
  - Bei genau einer Domain: deren Name, z. B. `mailboxes_amplifa-mail.de_2026-06-21.csv`.
  - Bei mehreren Domains im selben Lauf: `mailboxes_multi_<YYYY-MM-DD>.csv`.
  - `<YYYY-MM-DD>` = heutiges Datum.
- Existiert die Datei bereits, einen Zähler anhängen (`..._2.csv`) statt zu überschreiben.

## Output-Format

CSV mit Header `email,first_name,last_name,domain`. Eine Zeile pro Adresse, Reihenfolge der 5 Muster wie oben. Keine Leerzeilen.
