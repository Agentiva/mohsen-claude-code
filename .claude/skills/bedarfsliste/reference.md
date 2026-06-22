# Bedarfsliste Referenz

## Bedarfsprofil (Schritt 1) – Format

Kurz festhalten, bevor gesucht wird:

```
Kunde / Produkt: {…}
Problem, das es löst: {…}
=> Wer hat dieses Problem konkret?

Ziel-Branchen / Sub-Sektoren:  {Liste}
Firmengröße (MA / Umsatz):     {Band}
Region / Land:                 {…}
Bedarfs-Signale (Indizien):    {z. B. eigener Maschinenpark, Exportquote,
                                Schichtbetrieb, ERP-System, Zertifizierungen,
                                Wachstum, Standortausbau, Hiring …}
Ausschlusskriterien:           {wer hat definitiv keinen Bedarf}
```

### Beispiel
Kunde verkauft Schmierstoffe für Metallbearbeitung →
- Bedarf haben Firmen mit **eigener spanender Fertigung** (Zerspanung, CNC).
- Branchen: Maschinenbau, Metallverarbeitung, Automotive-Zulieferer, Werkzeugbau.
- Größe: ab ~20 MA (eigene Fertigung), bis Konzern.
- Signal: CNC-/Bearbeitungszentren, Lohnfertigung, ISO-9001/IATF.
- Ausschluss: reine Handelsfirmen, Dienstleister ohne Fertigung, Büro-/IT-Firmen.

→ daraus werden die Teilsuchen: „Maschinenbau {Land}", „Werkzeugbau {Land}",
„CNC Lohnfertigung {Land}", „Automotive-Zulieferer {Land}" usw.

## Apollo / Clay – Filter-Mapping

**Apollo Organization Search** (Bulk-Discovery): Filter nach
- Branche/Keywords (pro Teilsuche eine Branche/ein Sub-Sektor – nicht alles in eine Query)
- Mitarbeiterzahl (Größenbänder, z. B. 11–50, 51–200, 201–500 …)
- Land/Region

Tipps:
- Spezifische Branchen-/Keyword-Begriffe statt Oberbegriffen (sonst zu breit).
- Größe in Bänder splitten → mehr Treffer, da Apollo pro Query begrenzt liefert.
- Über Seiten paginieren, bis ein Segment ausgeschöpft ist, dann nächstes Segment.

**Clay** (Verifizierung/Anreicherung von Grenzfällen): nur einsetzen, wenn
zweifelhaft ist, ob echter Bedarf vorliegt (z. B. unklar, ob Firma eigene
Fertigung hat) – kostet Credits.

## Domain-Handling
- Domain immer normalisiert (ohne www./Schema/Pfad). Das Dedup-Skript macht das.
- Firma ohne auffindbare Domain: verifizieren oder rauslassen, nie raten.

## Zielzahl realistisch einordnen
Wenn der Markt kleiner ist als die Wunschzahl, das offen sagen. Eine ehrliche
1300er-Liste mit echtem Bedarf ist mehr wert als eine 2000er mit 700 Blindgängern.
