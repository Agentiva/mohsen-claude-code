# Deep-Dive Market-Intelligence- & Onboarding-Report: Jobtiva (jobtiva.ai)

_Erstellt von amplifa · 05.08.2026 · Zielmarkt: Deutschland (DACH-Erweiterung) · Methodik: Multi-Source-Triangulation aus Produkt-Repository, internen Strategiedokumenten und öffentlichen Quellen_

> **Datenqualitäts-Hinweis:** `https://jobtiva.ai/` war aus dieser Session weder per WebFetch (HTTP 403, Bot-Schutz) noch per Direktabruf (Egress-Policy blockiert den Host) erreichbar; es existiert praktisch kein Suchmaschinen-Index zur Marke. Die Produkt- und Unternehmenswahrheit stammt deshalb **primär aus dem Quell-Repository `Agentiva/Jobtiva` (Stand 04.08.2026)** — `PRODUCT.md`, `src/lib/stripe.ts`, `src/lib/legal.ts`, `src/lib/plan-limits.ts`, `src/lib/addon-kits.ts` — plus fünf internen Strategie-PDFs (Business Plan, GTM B2C, GTM nach Maja Voje, Kooperationsstrategie öffentlicher Sektor, ElevaJobs-Vorgängerdokumente). Marktzahlen sind öffentlich belegt und, wo Quellen streuen, als Bandbreite ausgewiesen. **Wichtig: Die internen Strategiedokumente (Stand März 2026) und der Live-Code (Stand August 2026) widersprechen sich beim Preismodell, bei der Zielgruppe und bei der Hosting-Story.** Diese Divergenzen sind in Abschnitt 11 einzeln aufgeführt — sie sind das Wertvollste an diesem Report.

---

## 1. Management Summary

Jobtiva ist eine KI-gestützte Bewerbungsplattform für den deutschen Markt, betrieben vom Einzelunternehmen **Agentiva (Inh. Mohsen Ghulami, Wesseling/NRW)**. Das Produkt bündelt Stellensuche (BA-Jobsuche-API + JSearch), KI-Lebenslauf, Anschreiben nach DIN 5008, ATS-Check, Unternehmensrecherche, Interviewvorbereitung, Gehaltcheck, Berufscheck (RIASEC-basiert), KI-Bewerbungsfoto sowie einen automatischen Steuerbeleg nach § 9 EStG — in **19 Sprachen** plus Deutsch, mit Chrome-Extension für Auto-Fill.

Der Markt ist zyklisch im Rücken: Im **Juli 2026 waren 3,007 Mio. Menschen arbeitslos (Quote 6,4 %)** — der Januar 2026 markierte mit 6,6 % den höchsten Stand seit fast zehn Jahren ([BA](https://www.arbeitsagentur.de/presse/2026-05-arbeitsmarkt-im-januar-2026)). Gleichzeitig bewerben sich laut Stepstone bereits **61 % der Beschäftigten mit KI**, während **80 % der Recruiter die eingehenden Unterlagen als höchstens mittelmäßig** bewerten ([Stepstone-Studie 2025](https://www.stepstone.de/e-recruiting/hr-wissen/recruiting/stepstone-studie-2025-ki-und-jobsuche)). Genau in dieser Lücke — *KI ist Standard, Qualität ist es nicht* — liegt Jobtivas Kernversprechen.

**Zwei Linsen, zwei Zahlen:** Der adressierbare B2C-Markt (Linse A) liegt nach triangulierter Rechnung bei **€80–120 Mio./Jahr SAM**, mit einem realistischen 12-Monats-SOM von **€0,3–0,9 Mio.** Das für amplifa-Outbound relevante institutionelle Account-Universum (Linse B) umfasst **rund 6.000–8.000 Organisationen** in Deutschland (AZAV-Bildungsträger, Jobcenter, Agenturen, Hochschul-Career-Services, kommunale Integrations- und Wirtschaftsförderungsämter), davon **1.500–2.500 ICP-fit** und **400–700 in 12 Monaten bearbeitbar**. Das Base-Case-Ziel: **60–70 qualifizierte Erstgespräche pro Jahr** aus dem institutionellen Segment — genug, um bei 15–20 % Abschlussquote **10–13 Träger-/Standortverträge** und damit €15.000–58.000 MRR zu erzeugen.

Die Kernchance ist nicht die Technologie, sondern die **Kombination aus Deutschland-Spezifik (DIN 5008, Steuerbeleg, BA-API, 20 Sprachen für die Migrantenintegration) und institutionellem Vertrauens-Hebel**. Ein einziger BA-/Bildungsträger-Pilot ist gleichzeitig B2B-Umsatz und das stärkste denkbare B2C-Trust-Signal.

---

## 2. Unternehmens- & Produktüberblick (vollumfänglich)

### 2.1 Unternehmen — Steckbrief & Zusammenfassung

| Merkmal | Ausprägung | Quelle / Status |
|---|---|---|
| Firma / Rechtsform | **Agentiva** — Einzelunternehmen (ausdrücklich **keine** GmbH; Rechtsformzusatz im Code explizit verboten) | `src/lib/legal.ts` |
| Inhaber / Führung | Mohsen Ghulami (voll haftend) | `src/lib/legal.ts` |
| Sitz | Kastanienweg 7, 50389 Wesseling (NRW) | `src/lib/legal.ts` |
| USt-IdNr. | DE 364578579 | `src/lib/legal.ts` |
| Produktmarke | **Jobtiva** (jobtiva.ai); Vorgängermarke/Codebase: „ElevaJobs" | Repo-Struktur, Strategie-PDFs |
| Kontakt | hello@jobtiva.ai · alerts@jobtiva.ai (System) | `legal.ts`, Postfach-Alerts |
| Mitarbeiter | 1–2 (Gründer + Umfeld); Gründungsstipendium NRW ist auf ein 2-Personen-Team gerechnet | GTM Maja Voje |
| Umsatz | **Nicht öffentlich.** Interne Projektion (März 2026, altes Preismodell): Monat 12 ≈ €77.000/Monat, Monat 24 ≈ €275.000/Monat — *triangulierte Planzahl, nicht Ist* | Business Plan §9.5 |
| Aufsichtsbehörde | LDI NRW (Düsseldorf) | `legal.ts` |
| Rechtsstand | AGB/Datenschutz Version 2026-07, Stand 25.07.2026 | `legal.ts` |
| Verbundene Aktivität | Der Gründer ist parallel bei amplifa.ai beschäftigt — laut GTM-Doku ein **EXIST-Ausschlusskriterium** | GTM Maja Voje §7 |

**Zusammenfassung in Fließtext:** Jobtiva ist ein von einer Einzelperson getragenes, bootstrapped B2C-SaaS aus Nordrhein-Westfalen, das den kompletten deutschen Bewerbungsprozess in einer Anwendung abbildet — von der Stellensuche über Lebenslauf und Anschreiben bis zu Interviewvorbereitung, Gehaltseinordnung und Berufsorientierung. Die eigentliche Zielgruppe sind laut Produktdefinition **Berufseinsteiger:innen zwischen 20 und 28 Jahren** — Azubis, Studierende, frische Absolvent:innen und frühe Wechsler:innen —, also eine ausgesprochen preissensible, mobile-first sozialisierte Gruppe, die über TikTok, Instagram und Creator erreicht wird und von den institutionell wirkenden Platzhirschen (StepStone, Indeed, Arbeitsagentur) schlecht bedient wird. Verdient wird wiederkehrend über ein dreistufiges Abo (Free / Standard €14,95 / Premium €27,95, jeweils auch als 3-Monats-Bündel) plus Einmalkäufe von „Bewerbungskit"-Paketen; ein 7-Tage-Trial ohne Kreditkarte führt in die Bezahlschranke. Technisch läuft die Plattform auf Next.js/Node mit Supabase, Stripe und einem Multi-Provider-KI-Wasserfall (OpenAI, Anthropic, Google), rechtlich sauber flankiert durch Impressum, AGB, Widerruf und ein vollständiges Auftragsverarbeiter-Verzeichnis. Der Reifegrad ist **früh** — das Produkt ist funktional breit und rechtlich ordentlich aufgesetzt, aber ohne belegbare Nutzerzahlen, ohne öffentliche Sichtbarkeit und mit einer Preisstruktur, die sich seit dem Business Plan grundlegend geändert hat. Die Besonderheit gegenüber allen Wettbewerbern ist die Kombination aus Deutschland-Spezifik (DIN-5008-Formatierung, § 9 EStG-Steuerbeleg, BA-Jobsuche-API) und einer Mehrsprachigkeit von 20 Sprachen inklusive Arabisch, Persisch/Dari, Paschtu, Tigrinya, Somali, Kurdisch und Ukrainisch — ein Alleinstellungsmerkmal, das direkt auf die Arbeitsmarktintegration von Migrant:innen zielt.

### 2.2 Produkte & Produktgruppen (Aufschlüsselung)

| Produktgruppe | Konkrete Leistungen (Live im Repo) | Zielkunde / Use Case | Erlösmodell | Outbound-Türöffner-Eignung |
|---|---|---|---|---|
| **Bewerbungserstellung (Kern)** | CV-Builder, Anschreiben (DIN 5008), KI-Textvorschläge, Vorlagen (5/10/alle), PDF-Export, `translate-document` | Jede:r Bewerber:in | Abo + Bewerbungskit-Pakete | ★★★ — universeller Einstieg |
| **Job-Discovery & Matching** | Jobsuche über **BA-Jobsuche-API zuerst, JSearch/RapidAPI ergänzend**, `jobmatching`, gespeicherte Jobs, tägl. Matching-Cron | Aktive Suchende | Abo (Free = kein Dashboard) | ★★ — Nutzen, aber generisch |
| **Bewerbungsintelligenz** | ATS-Score (Quick frei, KI-Analyse ab Standard), Unternehmensrecherche/-Enrichment, Bewertungs-Enrichment, Interview-Prep | Qualitätsbewusste Bewerber | Abo-Kontingente | ★★★ — echtes Differenzmerkmal |
| **Karriere-Orientierung** | **Berufscheck** (RIASEC-basiertes Quiz → Job-Empfehlungen, Premium-only), Personality-Check | Unentschlossene, Quereinsteiger, Schüler | Premium | ★★★ — bester Lead-Magnet für Schulen/Bildungsträger |
| **Gehalt & Verhandlung** | Gehaltcheck, Gehaltsrechner, Gehaltsschätzung | Wechsler, Verhandlungssituation | Standard/Premium | ★★★ — höchste Share-Rate, SEO-stark |
| **Steuer-Layer** | `bewerbungskosten`-Modul, automatischer Beleg nach § 9 EStG | Alle Zahlenden | Conversion-Treiber (kein eigener Umsatz) | ★★★ — einzigartig, PR-fähig |
| **Bild & Auftritt** | KI-Bewerbungsfoto (`generate-headshot`) + Verfeinerung, Gesichtserkennung | Bewerber ohne Fotoshooting | Premium | ★★ — sichtbarer „Wow"-Moment |
| **Mehrsprachigkeit / Integration** | 19 Zielsprachen (ar, fa, ps, ti, so, ku, uk, ru, tr, pl, ro, bg, zh, es, pt, it, fr, nl …) + DE, `translate-strings`, `translate-document` | Migrant:innen mit Arbeitserlaubnis, Institutionen | B2B-Lizenz / öffentliche Förderung | ★★★ — **der institutionelle Türöffner** |
| **Distribution** | Chrome-Extension (Auto-Fill auf Bewerbungsformularen, ATS-kompatibel) | Massenbewerber | Bindung/Retention | ★★ — Produkt-Hook, kein Verkaufsargument |
| **B2B / White-Label** *(geplant)* | Träger-Lizenz, Standortlizenz, AVGS-Abrechnung | Bildungsträger, Jobcenter, Kommunen | Setup + Lizenz + Pro-Nutzer-Gebühr | ★★★ — **amplifa-relevantes Segment** |

### 2.3 Positionierung

- **Zielbranchen/-gruppen:** B2C — Berufseinsteiger:innen 20–28 (Produktdefinition) bzw. Quereinsteiger 25–40 (GTM-Empfehlung, siehe Konflikt in §11). B2B — Bildungsträger, Jobcenter/Agenturen, Kommunen, Hochschul-Career-Services.
- **Positionierung & USP:** „Expert-grade Bewerbungsqualität zu einem Preis, den ein Berufseinsteiger stemmen kann" — mit vier Bausteinen, die im Wettbewerb **kein** Anbieter kombiniert: (1) automatischer § 9 EStG-Steuerbeleg, (2) Berufscheck als Quiz-basierte Orientierung, (3) Gehaltcheck **im** Bewerbungs-Workflow, (4) 20-Sprachen-Brücke für Migrant:innen. Markenhaltung laut `PRODUCT.md`: „confident, refined, energetic" — premium-zurückhaltend, bewusst **nicht** verspielt/gamifiziert, ausdrücklich abgegrenzt vom „grauen Behörden-Look" von StepStone/Arbeitsagentur.
- **Bestehende Vertriebskanäle:** Bislang keine belegbaren. Vorgesehen: SEO (Priorität 1), TikTok/Instagram Reels, LinkedIn des Gründers (~4.000 Follower), Referral-Programm, selektive Google Ads. Kein Cold-Email-Outreach im B2C.

---

## 3. Markt & Segment (Deutschland) — validiert

### 3.1 Marktgröße & Dynamik

| Marktebene | Größe (Bandbreite) | Wachstum | Quelle |
|---|---|---|---|
| HR-Software DACH (Top-25-Anbieter, Umsatz) | **€2,65 Mrd. (2024)** | +11 % ggü. Vj.; 2023: +13,5 % | [Haufe HR-Software-Ranking](https://www.haufe.de/personal/hr-management/hr-software-die-groessten-anbieter_80_437646.html) |
| HR-Tech-Unternehmen DACH | **535 aktive Unternehmen (Q1 2025)** | +7,4 % ggü. Okt. 2023 | [Haufe HR-Tech-Markt](https://www.haufe.de/personal/hr-management/hr-tech-markt-fuer-hr-software-ist-in-bewegung_80_643304.html) |
| HR-Tech Deutschland gesamt | €1,0–2,8 Mrd. (Abgrenzungsbedingt streuend) | 7,6–10,4 % CAGR; KI-Segment ~15 % | Interner Business Plan §3.1 (triangulierte Sekundärquellen) — **als Annahme markiert** |
| **Bewerberseite (B2C) — hier relevant** | siehe TAM-Modell §4.1 | — | Eigenberechnung, Basis Destatis/BA/BIBB |

> **Abgrenzungs-Hinweis:** Alle großen HR-Tech-Zahlen messen den **Arbeitgeber-seitigen** Markt (ATS, HRIS, Payroll). Jobtiva verkauft an die **Bewerberseite** — ein Markt, für den keine belastbare kommerzielle Marktstudie existiert. Deshalb wird der TAM in §4 konsequent **bottom-up** aus amtlichen Bevölkerungs- und Arbeitsmarktzahlen hergeleitet, nicht aus HR-Tech-Reports abgeleitet.

**Nachfragebasis Deutschland (amtlich belegt):**

| Kennzahl | Wert | Quelle |
|---|---|---|
| Arbeitslose (Juli 2026) | **3.007.000**, Quote 6,4 % (+71.000 ggü. Vormonat) | [BA-Monatsbericht](https://www.arbeitsagentur.de/news/arbeitsmarkt) |
| Arbeitslose (Januar 2026) | 3.085.000, Quote 6,6 % — höchster Stand seit ~10 Jahren | [BA](https://www.arbeitsagentur.de/presse/2026-05-arbeitsmarkt-im-januar-2026) |
| Erwerbstätige Wechselwillige (Schätzung) | 1,7–3,2 Mio. | IAB-Schätzung, via internem Business Plan — *Annahme* |
| Studierende (WS 2025/26) | **2,87 Mio.** (+0,4 %) | [Destatis PM 426/2025](https://www.destatis.de/DE/Presse/Pressemitteilungen/2025/11/PD25_426_21.html) |
| Studienanfänger:innen (Studienjahr 2025) | **491.700** (+0,3 %, vierter Anstieg in Folge) | Destatis |
| Hochschulabschlüsse (Prüfungsjahr 2024) | **511.600** (+1,9 %) | Destatis |
| Neue duale Ausbildungsverträge (2025) | **476.000** (−2,1 %); Angebot 530.300 Stellen (−4,6 %) | [BIBB](https://www.bibb.de/de/215234.php) |
| Unversorgte Bewerber:innen (30.09.2025) | **40.000** (+9.000 ggü. Vj.) = 9 % der gemeldeten Bewerber | [BA-Ausbildungsmarktbilanz](https://www.arbeitsagentur.de/presse/2025-45-ausbildungsmarktbilanz-2024-2025) |
| Bewerbungen pro Suchprozess | 30–50 | Branchenübliche Spanne, via internem Business Plan — *Annahme* |
| Kosten Bewerbungscoaching | **80–200 €/Std.**, Ø 125 €/Std.; Komplettpakete **200–1.500 €** | [Karrierebibel](https://karrierebibel.de/bewerbungscoaching/), [Trustlocal](https://trustlocal.de/kosten/coaching-kosten/bewerbungscoaching-kosten/) |

### 3.2 Strukturelle Treiber (langfristig positiv)

1. **KI-Bewerbung ist Mainstream geworden.** 61 % der Beschäftigten nutzen KI bei Jobsuche und Bewerbung (Stepstone 2025). Die Kategorie muss nicht mehr erklärt werden — nur noch die Qualität.
2. **Qualitätslücke als Geschäftsmodell.** 69 % der Recruiter bemängeln fehlende Individualisierung, 73 % fehlende Authentizität, 75 % übertriebene Qualifikationsdarstellung (Stepstone). Jobtivas Enrichment-Pipeline ist die direkte Antwort auf genau diesen Vorwurf.
3. **Demografisch stabiler Zustrom.** ~490.000 Studienanfänger und ~512.000 Absolvent:innen pro Jahr plus ~476.000 neue Ausbildungsverhältnisse — die 20–28-Kohorte erneuert sich jährlich in Millionenhöhe.
4. **Migration & Integration.** Hunderttausende Menschen mit Arbeitserlaubnis scheitern am deutschen Anschreiben (in vielen Herkunftsländern unüblich). 20 Sprachen sind hier kein Feature, sondern ein Marktzugang.
5. **Öffentliche Finanzierungsinfrastruktur.** AVGS nach § 45 SGB III, Bildungsgutscheine, ESF+, IQ-Netzwerk, Landesprogramme — ein staatlich finanzierter Nachfragepool, der nicht auf Konsumentenbudgets angewiesen ist.

### 3.3 Zyklischer Rückenwind (aktuell — Timing-relevant fürs Messaging)

Anders als in klassischen Industrie-Mandaten wirkt die **Konjunkturschwäche hier zugunsten** des Kunden:

- Arbeitslosigkeit über 3 Mio. (Juli 2026) und Januar-Höchststand seit einem Jahrzehnt → mehr Suchende, mehr Absagen, mehr Frust.
- Ausbildungsangebot −4,6 %, 40.000 unversorgte Jugendliche → wachsende Orientierungslücke, exakt der Berufscheck-Use-Case.
- Betriebe reduzieren Ausbildungs- und Einstiegsangebote → höherer Wettbewerbsdruck pro Stelle → höhere Zahlungsbereitschaft für Differenzierung.
- **Institutionelle Konsequenz:** Steigende Fallzahlen bei gleichbleibenden Beraterkapazitäten (1 Berater : 150–300 Klienten) erhöhen den Druck auf Jobcenter und Träger, zu skalieren. Das ist das Timing-Argument im B2B-Messaging.

### 3.4 Regulatorik / Normen als Türöffner (und als Risiko)

| Regelwerk | Relevanz für Jobtiva | Bewertung |
|---|---|---|
| **EU AI Act Art. 50** — Transparenzpflichten, **anwendbar seit 02.08.2026** ([AI Act](https://artificialintelligenceact.eu/article/50/)) | KI-generierte Inhalte müssen maschinenlesbar gekennzeichnet sein | **Akut.** Seit drei Tagen scharf. Kennzeichnung in PDF-Metadaten ist zu verifizieren. Umgekehrt: „AI-Act-konform" ist gegenüber Institutionen ein Verkaufsargument |
| **§ 9 EStG** Werbungskosten, Pauschbetrag €1.230/Jahr | Automatischer Bewerbungskosten-Beleg | Einzigartiges Conversion- und PR-Asset |
| **§ 45 SGB III / AZAV** (Zertifizierung durch TÜV/DEKRA/certqua, 2–4 Monate, €3.000–8.000) | Voraussetzung für direkte AVGS-Abrechnung (30–80 €/Einheit; Standard-Vermittlungsgutschein €2.000 brutto) | Mittelfristiger Hebel; kurzfristig über bereits zertifizierte Träger abkürzbar ([BA zum AVGS](https://www.arbeitsagentur.de/arbeitslos-arbeit-finden/aktivierungs-vermittlungsgutschein-avgs)) |
| **DSGVO / Drittlandtransfer** | Verarbeiter außerhalb EU/EWR: Vercel (US), OpenAI (US), Anthropic (US), Resend (US), RapidAPI (US) | **Konflikt mit der „gehostet in Deutschland"-Story** — siehe §11 |
| **BFSG** (Barrierefreiheit, seit Juni 2025) | Kostenpflichtiger B2C-Dienst → WCAG 2.1 AA als Pflichtbaseline | In `PRODUCT.md` erkannt; Umsetzungsgrad offen |
| **AI Act, Hochrisiko-Einstufung** | Recruiting-Systeme sind Hochrisiko — Jobtiva ist **bewerberseitig** und trifft keine Einstellungsentscheidungen | Argumentativ sauber, sollte aber dokumentiert vorliegen |

### 3.5 Outbound-Eignung des Segments

**B2C: nicht outbound-fähig.** Cold-Outreach an Privatpersonen ist nach § 7 UWG unzulässig und passt weder zur Zielgruppe noch zum Preispunkt. Hier gilt ausschließlich PLG + SEO + Social.

**B2B/institutionell: sehr gut outbound-fähig — mit Einschränkungen.** Das Segment ist endlich (6.000–8.000 Organisationen), namentlich recherchierbar (KURSNET, Trägerverzeichnisse, Hochschul-Career-Service-Verzeichnisse, Jobcenter-Standortlisten), hat klar benennbare Funktionsrollen und einen unmittelbaren, quantifizierbaren Schmerz. Einschränkungen: lange Entscheidungszyklen, Vergabe-/Beschaffungsregeln bei Kommunen und BA, hohe Formalitätserwartung (Telefon und schriftliches Anschreiben schlagen Sequenz-Automatisierung), und AI-Voice ist gegenüber Behörden ein Reputationsrisiko.

---

## 4. TAM / SAM / SOM — zwei Linsen

### 4.1 Linse A — Produktmarkt (B2C-Umsatzpotenzial Jobtiva)

Modelliert auf das **aktuelle** Preismodell (Abo €14,95/€27,95 + Kit-Pakete), nicht auf das im Business Plan dokumentierte €2,50-pro-Download-Modell.

| Ebene | Definition | Größe | Herleitung |
|---|---|---|---|
| **TAM** | Jährliche Ausgabebereitschaft aller aktiven Jobsuchenden in DE für Bewerbungshilfe | **€180–450 Mio./Jahr** | 4,5–6,0 Mio. aktive Suchende (3,0 Mio. Arbeitslose + 1,7–3,2 Mio. erwerbstätige Wechselwillige, Überschneidungen bereinigt) × Ø-Zahlungsbereitschaft €40–75 pro Suchprozess. Plausibilitätsanker: ein einzelnes Coaching-Paket kostet bereits €200–1.500 — die Zahlungsbereitschaft existiert, sie ist nur ungleich verteilt |
| **SAM** | Digital-affine Kernzielgruppe mit Abo-Zahlungsbereitschaft (18–35) | **€80–120 Mio./Jahr** | ~2,0–2,6 Mio. Personen/Jahr im Bewerbungsprozess (512k Absolvent:innen + ~430k Ausbildungsplatzbewerber + junge Arbeitslose + junge Wechsler) × Ø €45 pro Suchprozess (≈ 2,5 Monate × Ø €18 Mischpreis Standard/Premium) |
| **SOM (12 Mon.)** | Über PLG/SEO/Social realistisch erreichbarer Anteil | **€0,3–0,9 Mio./Jahr** | 0,3–0,8 % SAM-Personendurchdringung ≈ 6.000–20.000 zahlende Nutzer × Ø €45 LTV |

> **Abweichung zum internen Business Plan:** Dort steht TAM €900 Mio. (4,5 Mio. × 80 Bewerbungen × €2,50) und SAM €45 Mio. Diese Rechnung unterstellt, dass jede:r Suchende **jede** Bewerbung einzeln bezahlt — bei 80 Bewerbungen wären das €200 pro Person, oberhalb dessen, was ein Bewerbungscoaching-Komplettpaket kostet. Die hier verwendete Herleitung ist konservativer und robuster. Beim aktuellen Abo-Modell ist die €2,50-Rechnung ohnehin gegenstandslos.

### 4.2 Linse B — Account-Universum (amplifa-relevant, bottom-up)

| Ebene | Definition | Anzahl Accounts (DE) | Herleitung |
|---|---|---|---|
| **TAM** | Alle Organisationen, die Bewerbungsunterstützung für Dritte organisieren | **~6.000–8.000** | ≥2.500 geprüfte AZAV-Bildungsträger ([GenauMeinKurs](https://www.genaumeinkurs.de/ratgeber/gefoerderte-weiterbildungen/richtige-weiterbildung-finden/)), realistisch 3.000–5.000 zertifizierte **Standorte** (KURSNET; kein zentrales Register, daher Bandbreite) + ~400 Jobcenter + ~150 Agenturen für Arbeit mit ~600 Standorten + ~420 Hochschulen mit Career Service (CSND) + ~400 Kreise/kreisfreie Städte mit Integrations-/Wirtschaftsförderungsämtern + private Outplacement-/Bewerbungsdienstleister |
| **SAM** | Träger mit aktivem Bewerbungstraining/AVGS-MAT-Portfolio, Career Services mit Tool-Budget, Jobcenter mit Digitalisierungsmandat | **~1.500–2.500** | Nur Standorte mit Coaching-/Bewerbungstrainings-Angebot (Schätzung 50–60 % der Träger) + alle Hochschul-Career-Services + Jobcenter in Digitalisierungspilotregionen |
| **SOM (12 Mon.)** | Mit 1 FTE Outbound + Gründer-Selling in 12 Monaten wirklich bearbeitbar | **400–700 Accounts** | Regionaler Start NRW (Pilotstandort Düsseldorf/Wesseling), dann Bundesland-weise Ausrollung; ~35–60 neue Accounts/Monat inkl. Recherche und Mehrfachkontakt |

### 4.3 SOM → Meeting-Forecast (das amplifa-Lieferversprechen)

Institutionelles Nischen-Outbound; Ø 2,5–3 relevante Personen pro Account.

| Szenario | Kontaktierte Personen | Meeting-Rate | Qualifizierte Erstgespräche / Jahr |
|---|---|---|---|
| Konservativ | 1.500 | 1,5 % | **~23** |
| **Base** | 3.000 | 2,2 % | **~66** |
| Optimistisch | 4.500 | 3,0 % | **~135** |

**Wirtschaftlichkeit (Base Case):** 66 Erstgespräche × 15–20 % Abschlussquote = **10–13 Verträge**. Bei den in der Kooperationsstrategie hinterlegten €50–150 pro Teilnehmer und Monat und angenommen 30 aktiven Teilnehmenden je Träger entspricht das **€1.500–4.500 MRR pro Account**, in Summe **€15.000–58.000 MRR** nach 12 Monaten — plus Setup-Gebühren. Zum Vergleich: der B2C-SOM-Basisfall liegt bei €25.000–75.000 Monatsumsatz. Das institutionelle Segment ist damit **umsatzseitig gleichwertig, aber mit deutlich weniger Marketingbudget erreichbar** — und liefert obendrein das Trust-Signal für B2C.

> **Zu verifizierende Annahmen:** Abschlussquote (15–20 %), Teilnehmerzahl pro Träger (30), Preis pro Teilnehmer (€50–150 — bislang nur intern gesetzt, nie am Markt getestet), Vertragslaufzeit. Alle vier gehören in den Kickoff (§10).

---

## 5. Wettbewerbslandschaft (mit validierten Eckdaten)

| Wettbewerber | Größe / Eckdaten | Positionierung | Stärke | Angriffsfläche für Jobtiva |
|---|---|---|---|---|
| **Jobstep.io** (CH) | Start Okt. 2025; **>2.500 zahlende Kunden bis Jan. 2026**; €8,95/Mo im Quartalsabo; ETH-/Stanford-Umfeld, Nähe zu Taxfix/Smallpdf ([ETH SPH](https://sph.ethz.ch/projects/jobstep-io)) | Bewerbungs-Cockpit mit Tracking + Video-Interview | Sehr schnelle Traktion, günstiger Preis, sauberes Produkt, deutschsprachig | **Der gefährlichste Wettbewerber.** Kein Steuernachweis, kein Berufscheck, kein Gehaltcheck im Workflow, Schweizer Hosting, keine 20-Sprachen-Integration, keine BA-API |
| **Bewerbung2Go (b2go)** | Angebot von Jobware; 520+ Vorlagen; kostenlos | Kostenloser Lebenslauf-Generator | Reichweite über Jobware, Bekanntheit, Preis €0 | Keine echte KI, kein Tracking, keine Recherche/Interview-Prep — Substitut nur für den CV-Teilschritt |
| **CVMaker.de** | Pro-Version €19,99; 20+ ATS-Vorlagen, KI-Textoptimierung | CV-Builder mit Zusatznutzen | Etabliert, gute Vorlagenqualität, SEO-stark | Kein Bewerbungs-Workflow, keine Jobsuche, keine Steuer-/Gehalts-/Berufsfunktionen |
| **careerboom.ai / Jobloo** | 2026 als „bestes KI-Bewerbungstool" in Vergleichsportalen platziert; Agenten-/Swipe-Auto-Apply | Auto-Apply-Automatisierung | Aggressives Content-Marketing, moderne UX | Auto-Apply erzeugt genau die Massen-Qualität, die Recruiter ablehnen — Jobtiva kann sich als Gegenentwurf positionieren |
| **Internationale Tools** (LazyApply, JobCopilot, Teal, Kickresume, LoopCV, Massive) | $38–79/Mo bzw. $99–249 einmalig; teils schwache Bewertungen (LazyApply Trustpilot 2,1/5) | US-zentrierte Massenbewerbung | Bekanntheit, Feature-Tiefe | Null DE-Lokalisierung: kein DIN 5008, kein Anschreiben-Verständnis, kein Foto, keine BA-Integration, keine Steuerlogik |
| **ChatGPT & Co.** | Kostenlos bzw. €20/Mo | Universalwerkzeug | Kostenlos, allgegenwärtig, „gut genug"-Wahrnehmung | **Der eigentliche Hauptwettbewerber.** Liefert Text, aber keine Formatierung, kein Unternehmens-Enrichment, keinen Beleg, keine Ablage, keine Interviewvorbereitung — genau das Substanz-Delta, das im Messaging stehen muss |
| **Bewerbungscoaches / -services** | 80–200 €/Std., Ø 125 €; Pakete 200–1.500 € | Persönliche Dienstleistung | Vertrauen, Individualität | Preis (Faktor 10–50), Verfügbarkeit, Skalierung — und über AVGS teilweise selbst Jobtivas B2B-Kunde statt Gegner |

**Wettbewerbsfazit:** Der Markt ist jung, fragmentiert und ohne dominanten deutschen Anbieter — aber das Zeitfenster schließt sich. Jobstep.io hat in sieben Monaten den Sprung geschafft, den Jobtiva noch vor sich hat, und besetzt exakt dieselbe Nische ohne die deutschen Tiefenfeatures. **Der Verteidigungsgraben ist nicht die Technologie, sondern Positionierung + Steuer-Story + institutionelle Verankerung.**

---

## 6. Ideal Customer Profile (ICP) — mit Tier-Priorisierung

### 6.1 B2C-ICP

| Kriterium | Tier 1 (Sweet Spot) | Tier 2 | Ausschluss |
|---|---|---|---|
| Situation | Absolvent:in/Azubi-Abgänger:in im aktiven Bewerbungsprozess, mehrere Absagen | Quereinsteiger:in 25–40, angestellt, wechselwillig | Führungskräfte ab Senior-Level (andere Kanäle, andere Erwartung) |
| Alter | 20–28 | 25–40 | 50+ (geringe Tool-Affinität, hohe Beratungserwartung) |
| Zahlungsbereitschaft | Niedrig-mittel, aber vorhanden (€15–30/Monat für 1–3 Monate) | Mittel-hoch (angestellt, investiert in Wechsel) | Ohne Budget und ohne AVGS-Anspruch |
| Kanal | TikTok, Instagram, Hochschul-Career-Services | LinkedIn, Google Ads, SEO | — |
| Signal | Erste Bewerbungsrunde, Studienabschluss, Ausbildungsende, Absagenserie | Jobwechsel-Recherche, Gehaltsvergleich, Restrukturierung im Arbeitgeber | — |
| Sprache | Deutsch | Deutsch | — |
| **Spezial-Tier** | **Migrant:in mit Arbeitserlaubnis, Deutsch ≤ B1** — höchster Schmerz, geringste Alternative, meist institutionell finanziert | — | — |

### 6.2 B2B-ICP (das amplifa-Zielsegment)

| Kriterium | Tier 1 (Sweet Spot) | Tier 2 | Ausschluss |
|---|---|---|---|
| Organisationstyp | **AZAV-zertifizierte Bildungsträger mit AVGS-MAT-/Bewerbungstrainings-Portfolio** (VHS, DAA, WBS, bfz, SBB, GFN, private Träger) | Hochschul-Career-Services; kommunale Integrations-/Migrationsämter; Wirtschaftsförderungen | Reine ATS-/HR-Software-Anbieter (Arbeitgeberseite = falsche Marktseite) |
| Größe | 3–30 Standorte, 200–3.000 Teilnehmende/Jahr | 1–2 Standorte bzw. einzelne Hochschule | Ein-Personen-Coaches ohne AZAV |
| Setup | Bereits zertifiziert (kein Zertifizierungsprojekt nötig), Bewerbungstraining im Kursportfolio, veraltete Tools/Word-Vorlagen im Einsatz | Career Service mit eigenem Tool-Budget | Träger ohne AVGS-/Bildungsgutschein-Zulassung |
| Region | **NRW zuerst** (Nähe, Pilotstandort Düsseldorf, Landesprogramme), danach BY/BW/NDS/HE | Bundesweit | DACH-Ausland (zunächst — AVGS ist DE-spezifisch) |
| Signal | Hoher Migrant:innen-Anteil in Maßnahmen; ausgeschriebene Stellen „Dozent:in Bewerbungstraining"; laufende ESF+/IQ-Projekte; Digitalisierungs-/Förderprojekte | Neuer Career-Service-Leitung; Uni-Kooperationsprogramme | — |

---

## 7. Buying Center & Personas (B2B)

| Persona | Titel (Beispiele) | Rolle im Kauf | Hauptmotivation | Haupteinwand |
|---|---|---|---|---|
| **Fachbereichsleitung Bewerbungstraining** | Fachbereichsleiter:in Bewerbung/Coaching, Maßnahmenleitung AVGS, Bildungsmanager:in | **Champion / Initiator** — spürt den Schmerz täglich | Dozent:innen sollen coachen statt formatieren; bessere Teilnehmerergebnisse; weniger Vorbereitungsaufwand | „Unsere Teilnehmenden sind digital nicht fit" |
| **Standort- / Niederlassungsleitung** | Standortleiter:in, Niederlassungsleiter:in, Regionalleitung | **Entscheider** bei Träger-Verträgen | Höhere Integrationsquoten = bessere Trägerbewertung und Folgeaufträge | Budget; „Was, wenn die BA das nicht anerkennt?" |
| **Geschäftsführung Bildungsträger** | GF, Vorstand, Prokurist:in | **Freigabe** bei mehrjährigen/mehrstandortigen Verträgen | Differenzierung gegenüber anderen Trägern in der Vergabe | Vertragsbindung, Datenschutz, Anbieterrisiko (Einzelunternehmen) |
| **Qualitäts- / AZAV-Beauftragte:r** | QM-Beauftragte:r, AZAV-Koordination | **Blocker/Prüfer** | Zertifizierungssicherheit, prüfungsfeste Dokumentation | AI Act, DSGVO, Nachweisführung gegenüber der fachkundigen Stelle |
| **BCA / Arbeitgeber-Service (BA)** | Beauftragte:r für Chancengleichheit am Arbeitsmarkt, Teamleitung Arbeitgeber-Service | **Türöffner** in die Agentur | Integrationsquote, Verweildauer, Aktivierungsquote | „Wir dürfen keine Produkte empfehlen" |
| **Career-Service-Leitung Hochschule** | Leiter:in Career Service, Career Center Manager:in | **Entscheider** im Uni-Kanal | Employability-Kennzahlen, Rankings, Angebot ohne Eigenaufwand | Vergaberecht, Werbeverbot auf dem Campus, Datenschutz für Studierende |
| **Amtsleitung Migration/Integration** | Amtsleiter:in, Integrationsbeauftragte:r | **Entscheider** im kommunalen Kanal | Messbare Arbeitsmarktintegration, Fördermittelverwendung | Vergabeverfahren, Nachhaltigkeit des Anbieters |
| **Datenschutzbeauftragte:r** | DSB (intern/extern) | **Blocker** | Rechtssicherheit | Drittlandtransfer (US-KI-Anbieter), AVV, Löschkonzept |

**Empfohlene Outbound-Reihenfolge:** Fachbereichsleitung Bewerbungstraining (Champion, niedrigste Hürde, sofortiger Schmerz) → Standortleitung (Entscheider) → parallel Career Services als volumenstarker, unkritischer Zweitkanal → Geschäftsführung erst bei Multi-Standort-Ausbau → QM/DSB **proaktiv** früh mit fertigen Unterlagen (AVV-Muster, AI-Act-Notiz, Verarbeiterliste) bedienen, statt sie am Ende als Blocker zu treffen → BA/Agentur zuletzt, nach vorzeigbarem Pilotergebnis.

---

## 8. Pain Points & Buying-Signals

### 8.1 Top-Pains

**B2C:**
- Absagen ohne Begründung — kein Lernprozess, wachsende Selbstzweifel.
- Der deutsche Bewerbungsapparat (Lebenslauf, Anschreiben, Foto, „richtiger" Ton) ist für Berufseinsteiger:innen undurchsichtig und einschüchternd.
- Professionelle Hilfe kostet €150–500 — mit dem ersten eigenen Einkommen unerreichbar.
- ChatGPT liefert generischen Text, der von Recruitern erkannt und abgewertet wird (69 % bemängeln fehlende Individualisierung).
- Keine belastbare Vorstellung vom eigenen Marktwert (Gehalt) und vom passenden Berufsfeld.
- Für Migrant:innen: Sprachbarriere + kulturell unbekanntes Anschreiben-Format.

**B2B/institutionell:**
- 1 Berater:in betreut 150–300 Klient:innen — individuelle Bewerbungshilfe ist im Tagesgeschäft nicht leistbar.
- Veraltete Word-Vorlagen ohne Wirkung; Dozent:innen verbringen Kurszeit mit Formatierung statt Coaching.
- Sprachbarrieren in Integrationsmaßnahmen ohne skalierbares Werkzeug.
- Harter Kennzahlendruck: Integrationsquote, Verweildauer, Aktivierungsquote, Kosten pro Vermittlung.
- 1 Monat ALG I kostet den Staat €1.200–1.800 — jede Verkürzung ist unmittelbar monetarisierbar.

### 8.2 Observable Buying-Signals (für Clay/Apollo-Trigger)

| Signal | Wo beobachtbar | Warum es kauft |
|---|---|---|
| Stellenausschreibung „Dozent:in / Trainer:in Bewerbungstraining", „Jobcoach", „Integrationscoach" | Träger-Karriereseiten, Indeed, BA-Jobbörse | Kapazitätsengpass genau im Zielprozess |
| AZAV-Zertifizierung neu erteilt / erneuert | KURSNET, Trägerwebsites, Zertifizierer-Listen | Portfolio wird gerade überarbeitet |
| Neue AVGS-MAT-Maßnahme im Kursportfolio | KURSNET, GenauMeinKurs | Aktives Angebot, das ein Tool braucht |
| Laufendes ESF+/IQ-Netzwerk-/Landesprojekt | Förderdatenbanken, Projektseiten, Pressemitteilungen | Budget vorhanden, Digitalisierungsauftrag im Projekt |
| Hoher Anteil Integrations-/Sprachkursangebote | Trägerwebsite, BAMF-Trägerlisten | 20-Sprachen-USP greift unmittelbar |
| Wechsel in der Career-Service-Leitung | LinkedIn, Hochschul-Pressemitteilungen | Neue Leitung will sichtbare Neuerung |
| Kommunale Digitalisierungs-/Integrationsstrategie veröffentlicht | Ratsinformationssysteme, Kommunalportale | Politisch gesetzter Handlungsauftrag |
| Trägerausschreibung/Vergabe für Bewerbungscoaching | Vergabeportale (z. B. eVergabe, DTVP) | Konkreter Beschaffungsanlass mit Frist |

---

## 9. Go-to-Market- und Outbound-Empfehlung

### 9.1 Value Proposition

**B2C:** „Deine Bewerbung wird auf die Stelle zugeschnitten, nicht auf ChatGPT-Durchschnitt — Lebenslauf, Anschreiben, Interviewvorbereitung und ein realistischer Gehaltsrahmen in einer Anwendung, zum Preis eines Streaming-Abos."

**B2B:** „Ihre Dozent:innen coachen wieder, statt zu formatieren. Jobtiva erstellt jedem Teilnehmenden in 5 Minuten eine individuelle, DIN-5008-konforme Bewerbung — in 20 Sprachen, DSGVO-konform, mit Reporting auf Ihre Integrations- und Verweildauerkennzahlen."

### 9.2 Top-Hooks / Angles (priorisiert)

1. **Der Qualitäts-Gegenentwurf (stärkster Hook, sofort belegbar).** „61 % bewerben sich schon mit KI — 80 % der Recruiter finden das Ergebnis höchstens mittelmäßig." Jobtiva ist die Antwort auf den zweiten Teil des Satzes. Funktioniert in B2C-Content **und** im institutionellen Anschreiben, weil es eine unabhängige Fremdquelle ist.
2. **Kapazitäts-Hook (B2B, primär).** „1 Berater:in : 150–300 Klient:innen. Wir machen die Bewerbungserstellung skalierbar, damit Ihre Leute wieder beraten." Direkt an der Kernkennzahl der Zielgruppe.
3. **Sprach-/Integrations-Hook (B2B, differenzierendster).** 20 Sprachen inkl. AR, FA, PS, TI, SO, KU, UK. „Lebenslauf in der Muttersprache rein, deutsche Bewerbung raus." Kein Wettbewerber bietet das — und es passt exakt auf ESF+/IQ-/BAMF-Förderlogik.
4. **Fiskal-Hook (B2B).** „1 Monat ALG I = €1.200–1.800. Verkürzen wir bei 10 % Ihrer Teilnehmenden die Suche um einen Monat, ist der Business Case erledigt." Wirkt bei Kommunen und Agenturen.
5. **Steuer-Hook (B2C, saisonal Jan–Mai).** § 9 EStG, automatischer Beleg, Werbungskostenpauschbetrag €1.230. SEO-Keyword „Bewerbungskosten absetzen" ist laut interner Analyse gering umkämpft und kommerziell hochwertig — das ist die realistischste organische Traffic-Chance.
6. **Timing-Hook (beide).** Arbeitslosigkeit über 3 Mio., Ausbildungsangebot −4,6 %, 40.000 unversorgte Jugendliche. Der Bedarf ist gerade jetzt am größten.

### 9.3 Kanal-Mix und Begründung

| Kanal | Einsatz | Begründung |
|---|---|---|
| **E-Mail-Outbound (B2B)** | **Primär.** Personalisierte Sequenzen an Fachbereichs- und Standortleitungen von Bildungsträgern; separate Sequenz für Career Services | Segment ist endlich, adressierbar und geschäftlich per E-Mail erreichbar; § 7 UWG-konform bei B2B mit sachlichem Bezug |
| **LinkedIn (B2B)** | **Sekundär, parallel.** Vernetzung + Nachfassen bei Champion-Personas; Gründer-Content zu Arbeitsmarkt-/Integrationsthemen | Bildungsträger- und Career-Service-Rollen sind auf LinkedIn gut vertreten; Gründerprofil (~4.000 Follower) ist ein vorhandenes Asset |
| **Telefon (B2B)** | **Pflicht bei Kommunen/Agenturen.** Erstkontakt lokal (Agentur Düsseldorf, Arbeitgeber-Service, BCA), nicht die Zentrale in Nürnberg | Öffentlicher Sektor entscheidet über persönliche Beziehungen, nicht über Sequenzen |
| **AI-Voice** | **Nicht einsetzen** gegenüber Behörden und Trägern | Reputations- und Compliance-Risiko übersteigt den Effizienzgewinn deutlich |
| **SEO (B2C)** | **Primär, langfristig.** Cluster „KI Bewerbung" (2.000–6.000/Mo, geringer Wettbewerb) und „Bewerbungskosten absetzen" zuerst | Höchster ROI für bootstrapped B2C; Wirkung ab Monat 6–9 |
| **TikTok/Instagram (B2C)** | **Primär, kurzfristig.** 2–3 Videos/Woche, Formate: Live-Demo, Preisvergleich, Steuerhack, Recruiter-Reaction | Zielgruppe 20–28 ist dort; DE-Engagement 3,85–4,1 %, ca. 8× Instagram |
| **Cold E-Mail an Privatpersonen** | **Nie** | § 7 UWG; zerstört zudem die Seriositätspositionierung |

**Sprache:** Outbound durchgängig Deutsch, formell (Sie) im institutionellen Segment. B2C-Content Deutsch, Du-Ansprache. Produktoberfläche mehrsprachig — das ist Verkaufsargument, nicht Kommunikationssprache.

### 9.4 Erste Kampagnen-Hypothese

**Kampagne „Trainer statt Formatierer" — NRW-Bildungsträger.**
Zielliste: 250–400 AZAV-zertifizierte Trägerstandorte in NRW mit Bewerbungstrainings-/AVGS-MAT-Angebot (Quelle: KURSNET + GenauMeinKurs + Trägerwebsites). Persona 1: Fachbereichsleitung Bewerbungstraining. Persona 2: Standortleitung. Hook 2 (Kapazität) als Einstieg, Hook 3 (Sprachen) als Differenzierung im Follow-up, Hook 4 (Fiskal) als Argument für die Freigabeebene. Angebot: **kostenloser 3-Monats-Pilot mit 100–200 Teilnehmenden**, ein Tag Schulung, monatliches Reporting — Kosten trägt Jobtiva. Zielgröße: 60–70 Erstgespräche im ersten Jahr, davon 10–13 Verträge.

**Switch-Segment:** Träger, die aktuell Word-Vorlagen oder Einzelcoaching einsetzen und gleichzeitig hohe Migrant:innen-Anteile in Maßnahmen haben — dort ist die 20-Sprachen-Funktion nicht ein Vorteil, sondern die Lösung eines akuten Betriebsproblems.

**Parallelkanal (geringerer Aufwand, schnellere Zyklen):** 20–30 NRW-Hochschulen mit Career Service. Angebot: kostenloser Basic-Zugang für alle Studierenden + Workshop. Kostet Jobtiva fast nichts, liefert Testimonials, Nutzungsdaten und Logos — und ist die Brücke zum institutionellen Vertrauen.

---

## 10. Onboarding-Fragenkatalog (für den Kickoff-Call)

**A. Angebot & Fokus**
- Starten wir Outbound auf **Bildungsträger** oder auf **Hochschul-Career-Services** zuerst? *(Annahme: Bildungsträger primär — höherer Deal-Wert; Career Services als schneller Parallelkanal)*
- Was ist der geplante Listenpreis pro Träger? Setup + monatliche Lizenz + Pro-Nutzer-Gebühr — welche Zahlen gelten? *(Annahme aus Kooperationsstrategie: €50–150 pro Teilnehmer/Monat — nie am Markt getestet)*
- Ist der kostenlose 3-Monats-Pilot (100–200 Teilnehmende, Kosten bei Jobtiva) das offizielle Einstiegsangebot? *(Annahme: ja, laut Pilotkonzept)*
- Wie lang ist der erwartete Sales-Cycle bei Trägern — und bei Kommunen? *(unbekannt)*

**B. ICP & Zielmarkt**
- NRW zuerst, dann bundesweit — bestätigt? *(Annahme: ja, Pilotstandort Düsseldorf)*
- Mindestgröße eines Trägers (Standorte / Teilnehmende pro Jahr)? Gibt es Ausschlusskriterien (z. B. keine reinen Sprachkursträger)?
- Sind Kommunen/Jobcenter im ersten Jahr wirklich in Scope, oder erst nach dem Pilotnachweis? *(Empfehlung: erst nach Pilot — Vergaberecht bremst)*
- DACH-Ausland (AT/CH) im ersten Jahr? *(Empfehlung: nein — AVGS-Logik ist DE-spezifisch)*

**C. Persona & Buying Center**
- Wer entscheidet bei euren bisherigen Gesprächen tatsächlich — Fachbereichs- oder Standortleitung? *(Annahme: Fachbereich initiiert, Standort entscheidet)*
- Gibt es bereits Kontakte in die Agentur für Arbeit Düsseldorf (Arbeitgeber-Service / BCA) oder zur Wirtschaftsförderung? *(Aktionsplan sieht das als „Sofort"-Maßnahme vor — Status?)*

**D. Proof & Differenzierung**
- Gibt es **irgendeine** referenzierbare Nutzung — Beta-User, Testimonials, ein laufender Pilot? *(Kritisch: ohne Proof ist institutionelles Outbound deutlich schwerer)*
- Dürfen wir konkrete Nutzerzahlen nennen — oder gilt weiter die Vorgabe „keine Nutzerzahlen, keine erfundenen Statistiken" aus den Markenfakten? *(Annahme: strikt keine Zahlen)*
- Was sind die Top-3-Einwände aus bisherigen Gesprächen und die beste Antwort darauf?
- Liegt eine AI-Act-Kennzeichnung (maschinenlesbare Markierung in generierten PDFs) vor? *(Seit 02.08.2026 anwendbar — QM-Beauftragte werden danach fragen)*

**E. Ziele & KPIs**
- Ziel: wie viele qualifizierte Erstgespräche pro Monat? *(Base-Case-Vorschlag: 5–6/Monat)*
- Definition eines qualifizierten Termins (SQL): AZAV-zertifiziert + Bewerbungstraining im Portfolio + Entscheider oder Champion am Tisch?
- Wer führt die Termine — Gründer allein? Reaktions-SLA auf Replies?

**F. Tech-Setup & Compliance**
- Sending-Domain: neue Outbound-Domain oder jobtiva.ai? *(Empfehlung: **separate** Domain — die Hauptdomain darf keinen Zustellungsschaden nehmen)*
- DNS-Zugang für SPF/DKIM/DMARC vorhanden?
- CRM: gibt es eines, oder läuft alles in der Sequenz-Software?
- Suppression: bestehende Kontakte, Pilotpartner, Investorengespräche — welche Liste ist auszuschließen?
- Ist ein AVV-Muster für Träger vorbereitet? Und eine Kurzdarstellung der Drittlandtransfers? *(Wird von jedem DSB abgefragt)*

**G. Material & Zugänge**
- Institutionelle Demo/Pitch-Deck (laut Aktionsplan „kurzfristig" geplant — Status?), Pilotkonzept auf 2–3 Seiten, Logos, Screenshots ohne Nutzerzahlen, Ansprechpartner + SLA.

---

## 11. Offene Annahmen & unklare Punkte (vor dem Call markiert)

| # | Annahme / Befund | Warum unsicher | Wie im Call klären |
|---|---|---|---|
| 1 | **Preismodell-Divergenz.** Strategiedokumente (März 2026): kostenlos erstellen + €2,50/Download + Abos €12/20/35. Live-Code (Aug. 2026): Free / €14,95 / €27,95 + 3-Monats-Bündel (€37,95/€69,95) + Bewerbungskit-Pakete (10/30/50 zu €9,99–44,99) + 7-Tage-Trial | Die gesamte GTM-Erzählung („€2,50 – weniger als ein Kaffee", „steuerlich absetzbar pro Bewerbung") hängt am alten Modell und ist im aktuellen Modell so nicht mehr wahr | Welches Modell gilt verbindlich? Muss das Messaging neu gebaut werden? Ist die Steuer-Story im Abo-Modell überhaupt noch tragfähig? |
| 2 | **Zielgruppen-Konflikt.** `PRODUCT.md`: Berufseinsteiger:innen 20–28. GTM nach Maja Voje: Beachhead = **Quereinsteiger 25–40** (Score 28/30), Berufseinsteiger nur sekundär (22/30) wegen geringer Zahlungsbereitschaft | Zwei gegensätzliche Beachheads bedeuten zwei verschiedene Produkte, Kanäle und Preispunkte | Verbindlich festlegen: Wer ist der erste zahlende Kunde? Alles Weitere hängt daran |
| 3 | **Hosting-/Datenschutz-Story.** Marketing-Behauptung: „Daten auf Hetzner-Servern in Deutschland, kein rechtliches Risiko". Verarbeiterverzeichnis: Vercel (US), OpenAI (US), Anthropic (US), Resend (US), RapidAPI (US) als Drittländer | Der Claim „gehostet in Deutschland" ist in dieser Absolutheit angreifbar (Wettbewerbsrecht) und wird von jedem DSB zerlegt | Wie lautet die belastbare Formulierung? Empfehlung: „Nutzerdaten in Deutschland, KI-Verarbeitung über AVV-gebundene Anbieter mit SCC" |
| 4 | **Scraping-Claim.** Business Plan: „kein Web-Scraping, ausschließlich offizielle APIs". Verarbeiterliste und Code: **Apify** für LinkedIn-/Xing-Profilextraktion | Widerspruch zwischen Außendarstellung und Ist-Zustand; ToS-Risiko bei LinkedIn/Xing | Was genau macht Apify? Ist die Extraktion nutzer-getriggert und auf eigene Profile beschränkt? Claim entsprechend anpassen |
| 5 | **Job-Datenquelle.** Plan nennt JSearch + Adzuna; Code nutzt **BA-Jobsuche-API zuerst**, JSearch ergänzend, Adzuna-Modul vorhanden | Die BA-Quelle ist ein Verkaufsargument gegenüber Institutionen („wir arbeiten auf Ihren Daten") — sie fehlt in jeder Außendarstellung | Bestätigen und ins Messaging heben |
| 6 | **Keine Traktionsdaten.** Weder im Repo noch in Dokumenten oder externen Quellen sind Nutzer-, Umsatz- oder Conversion-Zahlen belegt; Markenfakten verbieten ausdrücklich Nutzerzahlen und Erfolgsversprechen | Ohne Proof ist institutionelles Outbound erheblich schwerer, und der Umsatz-SOM ist reine Modellrechnung | Gibt es interne Zahlen (Signups, zahlende Nutzer, Trial-Conversion)? Falls ja: freigegeben für Vertrieb? |
| 7 | **B2B-Preis nie getestet.** €50–150/Teilnehmer/Monat stammt aus einer internen Setzung | Trägerbudgets sind über AVGS-Sätze (30–80 €/Einheit) und Ausschreibungen gedeckelt | Van-Westendorp-Kurzabfrage in den ersten 10 Trägergesprächen einbauen |
| 8 | **Abschlussquote 15–20 % und 30 Teilnehmende/Träger** im Meeting-Forecast | Reine Erfahrungswerte aus vergleichbaren institutionellen Mandaten, keine Jobtiva-Daten | Nach den ersten 10 Erstgesprächen neu kalibrieren |
| 9 | **Rechtsform Einzelunternehmen** bei Verträgen mit Kommunen/BA | Öffentliche Auftraggeber verlangen häufig Bonitäts-/Bestandsnachweise; volle persönliche Haftung | Ist eine UG/GmbH-Gründung vor den ersten Institutionsverträgen geplant? |
| 10 | **AI-Act-Kennzeichnung (Art. 50) seit 02.08.2026 anwendbar** | Aus dem Repo nicht ersichtlich, ob generierte PDFs maschinenlesbar markiert sind | Vor dem ersten institutionellen Gespräch verifizieren — QM-Beauftragte fragen danach |
| 11 | **HR-Tech-Marktzahlen (€1,0–2,8 Mrd., 7,6–10,4 % CAGR)** aus dem internen Business Plan | Quelle nicht nachvollziehbar; misst zudem den Arbeitgeber-, nicht den Bewerbermarkt | Für Außenkommunikation nicht verwenden; stattdessen Destatis-/BA-/BIBB-Zahlen aus §3.1 |
| 12 | **Jobstep.io-Zahlen** (>2.500 zahlende Kunden bis Jan. 2026) | Aus Sekundärquelle, nicht vom Unternehmen bestätigt; Stand Januar 2026, dürfte inzwischen höher liegen | Vor Wettbewerbsargumentation aktualisieren |
| 13 | **Website nicht auswertbar.** jobtiva.ai war aus dieser Umgebung nicht abrufbar (403 / Egress-Policy) | Die tatsächlich live kommunizierte Positionierung, Preisdarstellung und Trust-Elemente konnten nicht gegengeprüft werden | Screenshots oder Zugang bereitstellen; Abgleich Landing Page ↔ Code vor Kampagnenstart |

---

## 12. Quellen

**Unternehmen / Produkt (intern)**
- Repository `Agentiva/Jobtiva`, Stand 04.08.2026 — `PRODUCT.md`, `DESIGN.md`, `elevajobs/src/lib/stripe.ts`, `plan-limits.ts`, `addon-kits.ts`, `legal.ts`, `src/app/api/*`, `chrome-extension/`, `src/lib/i18n/generated/*`
- `Jobtiva Strategie/Jobtiva_Business_Plan_GTM_Strategie2.pdf` (März 2026)
- `Jobtiva Strategie/Jobtiva GTM Strategie B2C.pdf`
- `Jobtiva Strategie/Jobtiva Kooperationsstrategie Oeffentlicher Sektor.pdf`
- `Jobtiva Strategie/Jobtiva_GTM_Strategie_Maja_Voje.pdf`
- `Jobtiva Strategie/ElevaJobs_GTM_Strategie_Komplett_2026.pdf`

**Markt & Arbeitsmarkt**
- [Bundesagentur für Arbeit — Arbeitsmarkt aktuell](https://www.arbeitsagentur.de/news/arbeitsmarkt) · [Arbeitsmarkt im Januar 2026](https://www.arbeitsagentur.de/presse/2026-05-arbeitsmarkt-im-januar-2026)
- [Destatis — Wintersemester 2025/2026: 0,4 % mehr Studierende](https://www.destatis.de/DE/Presse/Pressemitteilungen/2025/11/PD25_426_21.html)
- [BIBB — Der Ausbildungsmarkt im Jahr 2025](https://www.bibb.de/de/215234.php) · [BA — Ausbildungsmarktbilanz 2024/25](https://www.arbeitsagentur.de/presse/2025-45-ausbildungsmarktbilanz-2024-2025)
- [Stepstone-Studie 2025 — KI und Jobsuche](https://www.stepstone.de/e-recruiting/hr-wissen/recruiting/stepstone-studie-2025-ki-und-jobsuche) · [Auswertung: 61 % bewerben sich mit KI](https://pressnetwork.de/61-prozent-bewerben-sich-mit-ki-doch-recruiter-bewerten-die-qualitaet-als-hoechstens-mittelmaessig-2/)
- [Haufe — HR-Software-Ranking, Top-25-Anbieter](https://www.haufe.de/personal/hr-management/hr-software-die-groessten-anbieter_80_437646.html) · [Haufe — HR-Tech-Markt in Bewegung](https://www.haufe.de/personal/hr-management/hr-tech-markt-fuer-hr-software-ist-in-bewegung_80_643304.html)

**Regulatorik & Förderung**
- [EU AI Act, Artikel 50 — Transparenzpflichten](https://artificialintelligenceact.eu/article/50/) · [Praxisleitfaden Art. 50](https://artificialintelligenceact.eu/transparency-rules-article-50/)
- [BA — Aktivierungs- und Vermittlungsgutschein (AVGS)](https://www.arbeitsagentur.de/arbeitslos-arbeit-finden/aktivierungs-vermittlungsgutschein-avgs) · [weiterbildung.nrw.de zum AVGS](https://www.weiterbildung.nrw.de/buergerinnen/finanzierung/angebote-der-bundesagentur-fuer-arbeit/aktivierungs-und-vermittlungsgutschein)
- [GenauMeinKurs — über 2.500 geprüfte AZAV-Bildungsträger](https://www.genaumeinkurs.de/ratgeber/gefoerderte-weiterbildungen/richtige-weiterbildung-finden/) · [DEKRA — AZAV-Zertifizierung](https://www.dekra-certification.de/de/azav-zertifizierung/)

**Wettbewerb**
- [Jobstep.io — ETH Student Project House](https://sph.ethz.ch/projects/jobstep-io) · [Trustpilot Jobstep](https://de.trustpilot.com/review/jobstep.io)
- [Bewerbung2Go (Jobware)](https://www.bewerbung2go.de/lebenslauf) · [CVMaker im Vergleich](https://www.2glory.de/lebenslauf-erstellen-beste-seite/)
- [careerboom.ai — Tool-Vergleich 2026](https://careerboom.ai/de/de/blog/tool-bewertung/beste-ki-job-bewerbung) · [Jobloo — KI-Tools Jobsuche 2026](https://jobloo.co/de/blog/beste-ki-tools-jobsuche/)
- [Karrierebibel — Bewerbungscoaching: Kosten](https://karrierebibel.de/bewerbungscoaching/) · [Trustlocal — Bewerbungscoaching-Kosten 2026](https://trustlocal.de/kosten/coaching-kosten/bewerbungscoaching-kosten/)

**amplifa**
- [amplifa.ai](https://amplifa.ai)

---

## Nächste Schritte

1. **Gebrandetes 16:9-Deck** — Übergabe dieses Inhalts an den Skill `amplifa-market-intelligence`, der den Report im amplifa-Designsystem als HTML-Präsentation rendert.
2. **Aktivierung** — Zielliste „NRW-Bildungsträger mit AVGS-MAT-Portfolio" (250–400 Standorte) über den Skill `firmen-deepresearch` bzw. `bedarfsliste` aufbauen und die Kampagne „Trainer statt Formatierer" mit `cold-email` sequenzieren.
