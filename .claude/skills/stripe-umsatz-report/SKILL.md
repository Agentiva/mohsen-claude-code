---
name: stripe-umsatz-report
description: Erstellt Umsatz-/Revenue-Reports aus Stripe. IMMER nutzen, wenn der User nach Umsatz, Revenue, Einnahmen, einem Stripe-Report, monatlichem/quartalsweisem Umsatz oder offenen Rechnungen fragt. Wendet automatisch die amplifa-Umsatzregel an: uncollectible-Rechnungen werden NIE angezeigt und NIE in den Umsatz gezählt.
argument-hint: [zeitraum, z. B. "Mai 2026" oder "Q1 2026"]
---

# Stripe-Umsatz-Report

Zieht Rechnungs-/Zahlungsdaten aus dem verbundenen Stripe-Connector und baut einen sauberen Umsatzreport für amplifa.

## Eiserne Regel (niemals abweichen)

- **Uncollectible-Rechnungen werden NIE angezeigt** und **NIE in Umsatzsummen eingerechnet.**
- Als Umsatz zählen **ausschließlich `paid` + `open`.**
- `void` und `draft` ebenfalls nicht als Umsatz zählen (nur paid + open ist Umsatz).

Diese Regel gilt für jede Summe, jede Zwischensumme und jede Tabelle im Report.

## Ablauf

1. Zeitraum bestimmen. Wenn keiner genannt ist, nachfragen oder den laufenden Monat annehmen (und das transparent machen).
2. Über den Stripe-Connector die Rechnungen/Invoices des Zeitraums abrufen. Status-Feld jeder Rechnung mitnehmen.
3. Filtern: alle `uncollectible` rauswerfen. Für die Umsatzsumme nur `paid` + `open` behalten.
4. Aggregieren:
   - **Umsatz gesamt** = Summe(paid) + Summe(open)
   - getrennt ausweisen: davon bereits bezahlt (paid) vs. noch offen (open)
   - optional nach Kunde aufschlüsseln, wenn gewünscht
5. Report ausgeben.

## Output-Format

Kurzer, klarer Report:

- **Zeitraum**
- **Umsatz gesamt (paid + open):** Betrag in EUR
- **davon bezahlt (paid):** Betrag
- **davon offen (open):** Betrag
- optional: Tabelle pro Kunde (Kunde | Status | Betrag), uncollectible nicht enthalten
- Eine Zeile Hinweis: "Uncollectible-Rechnungen sind ausgeschlossen."

Beträge in EUR mit zwei Nachkommastellen. Wenn Stripe in Cents liefert, vor der Ausgabe durch 100 teilen.
