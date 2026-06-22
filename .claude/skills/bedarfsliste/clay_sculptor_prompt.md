# Clay Sculptor / Claygent – Bedarfs-Qualifizierungs-Prompt (Vorlage)

Diese Vorlage IMMER mit der Bedarfsliste mitliefern. Platzhalter `[...]` durch das konkrete Kundenprodukt + Bedarfsprofil (aus Schritt 1) ersetzen. In Clay als Claygent-/Sculptor-Spalte auf die importierte Liste (`company_name` + `domain`) anwenden.

## Inputs (Clay-Spalten mappen)
- `{{company_name}}`
- `{{domain}}`

## Prompt (an Kundenprodukt anpassen)

```
Du bist ein B2B-Sales-Researcher. Du bewertest, ob die unten genannte Firma einen ECHTEN Bedarf für das Produkt von [KUNDE] hat.

PRODUKT [KUNDE]: [1–2 Sätze: was es ist, welches Problem es löst].

ECHTER BEDARF besteht NUR, wenn die Firma:
- [Pflichtkriterium 1 aus dem Bedarfsprofil], UND
- [Pflichtkriterium 2 aus dem Bedarfsprofil].

KEIN Bedarf (Tier C): [harte Ausschlüsse aus dem Bedarfsprofil – z. B. reine Dienstleister/Software/Beratung/Holdings ohne den relevanten Prozess].

VORGEHEN:
1. Besuche die Website https://{{domain}} (Startseite, „Produkte"/„Leistungen", „Über uns", ggf. „Karriere").
2. Bestimme, was die Firma tut und ob die Pflichtkriterien erfüllt sind.
3. Achte auf Bedarfssignale: [3–5 konkrete, beobachtbare Signale aus dem Bedarfsprofil].

GIB GENAU DIESES JSON ZURÜCK (nichts anderes):
{
  "fit_tier": "A | B | C",          // A = Kriterien klar erfüllt; B = wahrscheinlich, aber unsicher; C = kein echter Bedarf
  "has_need": "yes | no | unclear",
  "key_signal": "<stärkstes konkretes Bedarfssignal in max. 10 Wörtern, oder 'none'>",
  "reason": "<1 knapper Satz, warum dieses Tier>"
}

Firma: {{company_name}}
Domain: {{domain}}
```

## Nachgelagert in Clay
- Filter: `fit_tier` ∈ {A, B} behalten, C entfernen.
- Optional A vor B priorisieren.
- Export: `company_name`, `domain` (+ optional `fit_tier`, `key_signal`) → fertige, bedarfsqualifizierte Liste.
