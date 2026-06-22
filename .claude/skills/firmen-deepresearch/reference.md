# Firmen-Deep-Research Referenz

## Bedarfsprofil (Schritt 1) – Format

```
Kunde / Produkt: {…}
Problem, das es löst: {…}
Ziel-Branchen / Sub-Sektoren:  {Liste}
Firmengröße (MA / Umsatz):     {Band}
Region / Land:                 {…}
Bedarfs-Signale:               {Indizien, die auf Bedarf hindeuten}
Ausschlusskriterien:           {wer definitiv keinen Bedarf hat}
```

## Quellenarten (breit anlegen)

| Quelle | Wofür | Beispiel-Sucheinstieg |
|---|---|---|
| Branchenverzeichnisse | breite Abdeckung, Domains direkt | wlw.de, europages, kompass |
| Verbands-Mitgliederlisten | hohe Qualität, klar abgegrenzt | „{Branche}verband Mitglieder {Land}" |
| Messe-Ausstellerlisten | aktuelle, aktive Firmen | „{Leitmesse} Aussteller {Jahr}" |
| Regionale Cluster / IHK | regionale Tiefe | „{Sub-Sektor} {Region} Unternehmen" |
| Ranglisten / Marktstudien | Marktführer/Mittelstand | „Top {Sub-Sektor} Hersteller {Land}" |
| Gezielte Web-Queries | Long-Tail/Nischen | siehe Query-Muster |

## Query-Muster (pro Sub-Sektor × Region variieren)

- `Hersteller {Produkt/Leistung} {Land}`
- `Lieferant {Produkt} {Region}`
- `{Sub-Sektor} Unternehmen {Land} Liste`
- `{Branchenverband} Mitgliederverzeichnis`
- `{Leitmesse} Ausstellerverzeichnis`
- `"{Sub-Sektor}" Standort {Bundesland/Kanton/Region}`

Tipp: pro Sub-Sektor mehrere Regionen einzeln durchgehen → mehr und gezieltere Treffer als eine breite Query.

## Extraktion & Verifizierung

1. Listing-Seite abrufen → Firmennamen + verlinkte Domains sammeln.
2. Pro Firma die Hauptdomain bestimmen (Startseite, nicht Unterseite/Tracking-Link).
3. Kurzer Website-Check: Macht die Firma wirklich das, was Bedarf erzeugt? → behalten/verwerfen.
4. Domain normalisiert ablegen (ohne www./Schema/Pfad – das Dedup-Skript erzwingt das).

## Abgrenzung zu `bedarfsliste`
- `bedarfsliste` = Bulk über Apollo/Clay (schnell, große Zahlen, Datenbank).
- `firmen-deepresearch` = reine Websuche (gründlich, Nischen/Verbände/Messen, kein MCP, langsamer).
Beide liefern dasselbe CSV-Format (`company_name,domain`) und nutzen dasselbe Dedup-Skript – Ergebnisse lassen sich also mergen.
