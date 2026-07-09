# Clay Sculptor / Claygent – Bedarfs-Qualifizierung für photovest

In Clay auf die importierte Liste (`company_name` + `domain`) als Claygent-/Sculptor-Spalte anwenden.
Danach nach `fit_tier` ∈ {A, B} filtern und exportieren.

## Inputs (Clay-Spalten mappen)
- `{{company_name}}`
- `{{domain}}`

## Prompt

```
Du bist ein B2B-Sales-Researcher. Du bewertest, ob die unten genannte Firma einen ECHTEN Bedarf für das Angebot von photovest hat.

ANGEBOT photovest: Steueroptimiertes Photovoltaik-Investment ohne zusätzliches Eigenkapital. Zielkunde ist eine EINKOMMENSSTARKE PRIVATPERSON mit HOHER EINKOMMENSTEUERLAST (ab ca. 70.000 € Jahreseinkommen, besonders relevant ab >30.000 € Steuerzahlung pro Jahr) – abgebildet über ein Gewerbe. Der Bedarfsträger ist also nicht "die Firma" abstrakt, sondern der/die inhaber- bzw. gesellschaftergeführte, gut verdienende Eigentümer:in dahinter (Unternehmer, Freiberufler, Gesellschafter-Geschäftsführer).

ECHTER BEDARF (Tier A) besteht, wenn die Firma:
- in Deutschland sitzt, UND
- klar INHABER-/PARTNER-/GESELLSCHAFTERGEFÜHRT ist (kein Streubesitz), UND
- plausibel PROFITABEL bzw. etabliert ist, sodass der/die Eigentümer:in eine hohe persönliche Einkommensteuerlast trägt. Typische Fälle:
  * Freiberufler-Praxis/Kanzlei/Büro (Arzt, Zahnarzt, Rechtsanwalt, Steuerberater/WP, Architekt, Ingenieur, Unternehmensberater), ODER
  * inhabergeführtes, profitables Mittelstands-Unternehmen (GmbH / GmbH & Co. KG) im Handwerk, Handel, Fertigung, IT o. Ä.

Tier B: wahrscheinlich passend, aber Inhaberstruktur oder Profitabilität aus der Website nicht eindeutig belegbar.

KEIN Bedarf (Tier C):
- Börsennotierte / große Konzerne, AG/SE mit breitem Streubesitz (keine einzelne hohe Privatsteuerlast).
- Öffentliche Hand, Behörden, Stadtwerke, Kammern, Universitäten/Hochschulen, Kliniken/Krankenhäuser in öffentlicher/institutioneller Trägerschaft.
- Vereine (e.V.), gemeinnützige Organisationen (gGmbH), Stiftungen, Genossenschaften (eG), Banken/Sparkassen.
- Reine Holdings ohne operatives Einkommen, offensichtlich defizitäre Frühphasen-Startups.

VORGEHEN:
1. Besuche die Website https://{{domain}} (Startseite, "Über uns"/"Team"/"Kanzlei"/"Praxis", "Leistungen", "Impressum").
2. Bestimme Rechtsform & Eigentümerstruktur (Impressum/Über-uns): inhabergeführt vs. Konzern/öffentlich/gemeinnützig.
3. Achte auf Bedarfssignale: genannte Inhaber/Partner/Gesellschafter-Geschäftsführer als Namensträger, Freiberufler-Praxis/Kanzlei, etablierte Mittelstands-GmbH, mehrere Standorte/Mitarbeiter, hochwertige/gewinnstarke Leistungen.

GIB GENAU DIESES JSON ZURÜCK (nichts anderes):
{
  "fit_tier": "A | B | C",
  "owner_managed": "yes | no | unclear",
  "high_tax_owner_likely": "yes | no | unclear",
  "key_signal": "<stärkstes konkretes Signal in max. 10 Wörtern, oder 'none'>",
  "reason": "<1 knapper Satz, warum dieses Tier>"
}

Firma: {{company_name}}
Domain: {{domain}}
```

## Nachgelagert in Clay
- Filter: `fit_tier` ∈ {A, B} behalten, C entfernen.
- Optional A vor B priorisieren; zusätzlich `owner_managed=yes` + `high_tax_owner_likely=yes` als Hot-Segment.
- Export: `company_name`, `domain`, `playbook_name` (+ optional `fit_tier`, `key_signal`).
