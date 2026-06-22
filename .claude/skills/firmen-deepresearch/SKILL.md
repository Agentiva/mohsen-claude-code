---
name: firmen-deepresearch
description: Findet B2B-Unternehmen rein über Websuche/Deep Research (KEIN Apollo/Clay) und liefert eine bedarfsqualifizierte CSV mit Unternehmensname + Domain. IMMER nutzen, wenn der User Firmen per Websuche/Deep Research finden will, ausdrücklich kein Apollo/Clay nutzen will, Branchenverzeichnisse/Verbände/Messelisten durchsuchen lassen will, oder "finde mehr" zu einer per Websuche erstellten Liste sagt. Recherchiert IMMER zuerst das Kundenprodukt und nimmt nur Firmen mit echtem Bedarf auf. Liefert IMMER drei Artefakte: (1) saubere CSV Name+Domain, (2) fertigen Clay-Sculptor-/Claygent-Qualifizierungs-Prompt für die Pro-Firma-Bedarfsprüfung, (3) ~25 komma-separierte Tier-1/Tier-2-Jobtitel für "Find People" in Clay. Web-Tools sind vorab freigegeben – keine Domain-Bestätigung pro Seite nötig.
argument-hint: [kunde/produkt + anzahl + zielland]
allowed-tools: WebSearch, WebFetch, Bash(python3 *)
---

# Firmen-Deep-Research per Websuche (amplifa)

Findet Zielunternehmen ausschließlich über **Websuche und Deep Research** – ohne Apollo/Clay. Stark für Nischen, regionale Märkte und Branchen, die Datenbanken schlecht abdecken (Verbände, Messen, Verzeichnisse). Output: saubere CSV mit **Unternehmensname + Domain**, nur Firmen mit echtem Bedarf.

**Web-Zugriff ist über `allowed-tools` vorab freigegeben** – Suche und Seitenabruf laufen ohne Bestätigung pro Domain durch. (Falls dennoch ein Prompt kommt: `WebSearch` und `WebFetch` in `.claude/settings.json` unter `permissions.allow` ergänzen.)

## Schritt 1 – Produkt-/Bedarfsanalyse (IMMER zuerst)

Vor jeder Suche das Kundenprodukt recherchieren und das **Bedarfsprofil** ableiten: welche Branchen/Sub-Sektoren das Problem konkret haben, passende Firmengröße, Bedarfs-Signale, Ausschlusskriterien. Profil kurz festhalten und zeigen, bevor in die Masse gegangen wird. (Format/Beispiel: `reference.md`.)

## Schritt 2 – Quellen- & Query-Strategie

Aus dem Bedarfsprofil systematische Websuchen bauen – pro Sub-Sektor × Region eigene Queries. Quellen breit anlegen statt nur Google-Treffer:

- Branchenverzeichnisse (wlw, Europages, Kompass …)
- Verbands-Mitgliederlisten (z. B. VDMA, VCI, branchenspezifische Verbände)
- Messe-Ausstellerlisten (relevante Leitmessen der Branche)
- IHK-/Handelsregister-nahe Verzeichnisse, regionale Cluster
- Gezielte Suchanfragen: „Hersteller/Lieferant {Produkt} {Region}", „{Sub-Sektor} {Land} Liste"

Quellenliste & Query-Muster: `reference.md`.

## Schritt 3 – Deep Research & Extraktion

1. Listings/Verzeichnisseiten abrufen und Firmen + Domains extrahieren.
2. **In die Tiefe gehen:** je Kandidat die Firmenwebsite kurz prüfen, um (a) die korrekte Hauptdomain zu bestätigen und (b) den Bedarf zu verifizieren (passt das, was die Firma tut, wirklich zum Bedarfsprofil?).
3. Treffer laufend in eine Arbeits-CSV schreiben; über viele Queries/Quellen iterieren, bis die Zielzahl erreicht ist.

## Schritt 4 – Bedarfs-Qualifizierung

Bedarfsfremde Firmen entfernen (falscher Sub-Sektor, zu klein, Ausschlusskriterium). Im Zweifel die Website-Prüfung aus Schritt 3 entscheiden lassen. Lieber weniger, dafür echte Treffer.

## Schritt 5 – Dedupe & Output

```bash
python3 ${CLAUDE_SKILL_DIR}/scripts/merge_dedupe.py master.csv neuer_batch.csv > liste.csv
```

- Dedupe nach normalisierter Domain (www./Schema/Pfad egal).
- **CSV-Output: genau zwei Spalten – `company_name,domain`** (mehr nur auf Wunsch).
- Skript meldet Gesamtzahl + neue Treffer.

## Schritt 6 – Pflicht-Zusatzartefakte (IMMER mitliefern)

Jede Lieferung besteht aus **drei Artefakten** – nie nur die CSV abgeben:

1. **CSV** (`liste.csv`) – `company_name,domain`.
2. **Clay-/Claygent-Qualifizierungs-Prompt** – fertiger Pro-Firma-Bedarfsprüfungs-Prompt (Input `{{company_name}}`/`{{domain}}`), der gegen die Bedarfs-Signale + Ausschlusskriterien aus Schritt 1 prüft und ein striktes JSON-Verdict (`qualifiziert`, `konfidenz`, `bedarfs_score`, Belege+URL) ausgibt. Als eigene Datei `clay-qualifizierung-prompt.md` ablegen. (Konsistent mit `bedarfsliste`.)
3. **25 Jobtitel (Tier 1 + Tier 2), komma-separiert** – für „Find People" in Clay. Aus dem Kundenprodukt/Bedarfsprofil die kaufenden/beeinflussenden Rollen ableiten:
   - **Tier 1** = primäre Entscheider/Budgetträger & direkte Bedarfsträger (z. B. Leitung Fertigung/Produktion, Reinigungstechnik, Qualität/Technische Sauberkeit, Einkauf, Betriebsleitung).
   - **Tier 2** = Beeinflusser/Anwender/technische Ebene (z. B. Fertigungs-/Prozessplaner, Industrial Engineering, Teamleiter Reinigung, AV, Instandhaltung, QS-Ingenieure).
   - DE-Titel + gängige EN-Entsprechungen mischen, dedupliziert, **genau ~25 Stück, eine Zeile, komma-separiert**, direkt copy-paste-fähig in Clays „Find People"-Jobtitel-Feld. Als `jobtitles-clay.txt` ablegen und im Chat anzeigen.

## „Finde mehr" / „Finde 1000 mehr"

Bestehende `liste.csv` ist master. Neue Quellen/Queries anzapfen (bereits gefundene Domains ausgeschlossen), als Batch sammeln, draufmergen:

```bash
python3 ${CLAUDE_SKILL_DIR}/scripts/merge_dedupe.py liste.csv batch2.csv > liste.csv
```

## Qualitätsregeln (eisern)

- Erst Produkt verstehen, dann suchen – Schritt 1 nie überspringen.
- Nur Firmen mit nachvollziehbarem Bedarf; keine Auffüllung nur für die Zahl.
- Zielland/Region hart anwenden.
- **Domains nie raten** – jede Domain stammt aus einer real abgerufenen Quelle/Website. Unbestätigt → raus.
- Quellen sauber nutzen; offensichtlichen Verzeichnis-Spam/aggregierte Müllseiten meiden.
- Realistisch bleiben: ist der Markt kleiner als die Wunschzahl, das ehrlich melden.
- Deep Research per Websuche ist gründlicher, aber langsamer als Datenbank-Suche – bei sehr großen Zahlen in Etappen arbeiten und Zwischenstände sichern.
- Endausgabe immer durch das Dedup-Skript.
- **Immer alle drei Artefakte liefern** (Schritt 6): CSV + Qualifizierungs-Prompt + 25 Tier-1/Tier-2-Jobtitel. Nie nur die CSV.
