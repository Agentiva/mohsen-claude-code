# Platzhalter-Katalog (kanonisch)

Dies ist die **einzige Wahrheit** für Platzhalter. Verwende nur Strings aus
dieser Liste, **wörtlich** und in doppelten geschweiften Klammern `{{...}}`.
Sie bleiben im erzeugten Prompt unausgefüllt — amplifa ersetzt sie zur Laufzeit
pro Lead. Erfinde keine neuen Platzhalter.

## Inhalt
1. Lead-Stammdaten
2. Lead-Recherche
3. Organisation (Absender = amplifa bzw. der Kunde)
4. Playbook (wird aus den Playbook-Detailseiten gefüllt)
5. Persona
6. Sequenz-/Sprachsteuerung
7. Playbook-Screenshot → Platzhalter-Mapping
8. Auswahlregeln (welcher Platzhalter wofür)

---

## 1. Lead-Stammdaten
| Platzhalter | Bedeutung |
|---|---|
| `{{first_name}}` | Vorname |
| `{{last_name}}` | Nachname (für Anrede) |
| `{{full_name}}` | Voller Name (Geschlecht für Anrede ableiten) |
| `{{job_title}}` | Position → bestimmt ICP-/Persona-Zuordnung |
| `{{company}}` | Firmenname |
| `{{company_domain}}` | Firmendomain |
| `{{company_website}}` | Firmen-Website-URL |
| `{{email}}` | E-Mail des Leads |
| `{{linkedin_url}}` | LinkedIn-Profil-URL |
| `{{location}}` | Standort des Leads |

## 2. Lead-Recherche (Personalisierungs-Rohstoff)
| Platzhalter | Bedeutung |
|---|---|
| `{{lead.disc_profile}}` | DISC-Profil (D/I/S/C oder Kombi) — steuert den Schreibstil |
| `{{lead.linkedin_headline}}` | LinkedIn-Headline |
| `{{lead.linkedin_summary}}` | LinkedIn-Summary/About |
| `{{lead.linkedin_scraped}}` | Komplettes gescraptes Profil |
| `{{lead.linkedin_posts}}` | Letzte Posts (für Zitate) |
| `{{lead.company_website_scraped}}` | Gescrapte Firmen-Website |
| `{{lead.buying_signals}}` | Buying Signals (Funding, Hiring, Launch, Award, Expansion, Patent, Messe …) — Hook-Quelle bei „mit Signale" |

> Hinweis: In manchen Alt-Prompts steht zusätzlich `{{company_website}}` als
> Recherche-Quelle. Für Body-Scrape immer `{{lead.company_website_scraped}}`
> bevorzugen; `{{company_website}}` ist nur die URL.

## 3. Organisation (Absender)
| Platzhalter | Bedeutung |
|---|---|
| `{{organization.website_url}}` | Website des Absenders (amplifa bzw. Kunde) |
| `{{organization.description}}` | Beschreibung des Absenders |

## 4. Playbook (aus den Playbook-Detailseiten)
| Platzhalter | Bedeutung |
|---|---|
| `{{playbook.product.name}}` | Produktname |
| `{{playbook.product.description}}` | Produktbeschreibung |
| `{{playbook.value_proposition}}` | Wertversprechen |
| `{{playbook.full_context}}` | Voller Kontext (Sammelfeld) |
| `{{playbook.icps}}` | ICP-Liste (mit Nummern; Lead per `{{job_title}}` zuordnen) |
| `{{playbook.use_cases}}` | Anwendungsfälle |
| `{{playbook.references}}` | Referenzkunden |
| `{{playbook.proof_points}}` | Beweispunkte (Pflicht-Material für Bullets/Proof) |
| `{{playbook.knowledge_base}}` | Wissensbasis (Hintergrund) |

## 5. Persona
| Platzhalter | Bedeutung |
|---|---|
| `{{persona.name}}` | Persona-Name (z. B. „Einkaufsleiter Robert") |
| `{{persona.title}}` | Persona-Titel/Rolle |
| `{{persona.pain_points}}` | Pain Points der Persona — Fundament des Pain-Absatzes |

## 6. Sequenz-/Sprachsteuerung
| Platzhalter | Bedeutung |
|---|---|
| `{{locale}}` | Zielsprache (de/en/fr) — bei locale-gesteuerten Prompts maßgeblich |
| `{{previous_email_body}}` | Vorherige Mail der Sequenz (ab Email 2; NICHT zitieren/wiederholen) |
| `{{lead.country}}` / `{{company.country}}` | Land (bei länder-gesteuerter Sprachregel) |

---

## 7. Playbook-Screenshot → Platzhalter-Mapping

Die Playbook-Detailseite (Beispiel „ErgoPack Palettenumreifungssystem") füllt die
`{{playbook.*}}`- und `{{persona.*}}`-Platzhalter. So hängen die Felder zusammen —
genau so „logisch gefüllt" muss der Prompt sie referenzieren:

| Playbook-Seite (UI-Block) | Platzhalter im Prompt |
|---|---|
| **Product Description** | `{{playbook.product.description}}` (Name → `{{playbook.product.name}}`) |
| **Value Proposition** | `{{playbook.value_proposition}}` |
| **Target Personae (n)** → je Persona Name/Titel | `{{persona.name}}`, `{{persona.title}}` |
| **Target Personae** → „Pain Points" je Persona | `{{persona.pain_points}}` |
| **Use Cases (n)** | `{{playbook.use_cases}}` |
| **Reference Customers (n)** | `{{playbook.references}}` |
| **Proof Points (n)** | `{{playbook.proof_points}}` |
| **Industry / USPs / sonstiger Kontext** | `{{playbook.full_context}}`, `{{playbook.knowledge_base}}` |

Konsequenzen für den Prompt-Bau:
- **Bullets/Proof** ziehen IMMER aus `{{playbook.proof_points}}` (+ optional
  `{{playbook.references}}`). Nie Zahlen erfinden — der Prompt verweist auf diese
  Felder, die Engine liefert die echten.
- **Pain-Absatz** baut auf `{{persona.pain_points}}` (Fundament) + ggf.
  `{{playbook.icps}}` als Fallback, wenn Persona nicht zur `{{job_title}}` passt.
- **Story/Use-Case-Brücke** zieht aus `{{playbook.use_cases}}` /
  `{{playbook.references}}`.
- **Relevanz/Mechanismus** aus `{{playbook.value_proposition}}` +
  `{{playbook.product.description}}`.

---

## 8. Auswahlregeln (welcher Platzhalter wofür)

- **Hook bei „mit Signale"** → `{{lead.buying_signals}}` (Priorität 1), dann
  `{{lead.linkedin_posts}}` → `{{lead.linkedin_headline}}`/`{{lead.linkedin_summary}}`.
- **Hook bei „ohne Signale"** → `{{persona.pain_points}}` + `{{playbook.icps}}`
  (ICP-Pain-Hypothese), gestützt durch `{{lead.linkedin_summary}}`/
  `{{lead.linkedin_scraped}}`/`{{lead.company_website_scraped}}` + Peer-Proof aus
  `{{playbook.references}}`.
- **Anrede-Geschlecht** → aus `{{full_name}}` ableiten; Nachname `{{last_name}}`.
- **ICP-Zuordnung** → `{{job_title}}` gegen `{{playbook.icps}}` matchen.
- **Sprache** → je nach Prompt-Typ über `{{locale}}` ODER über Land
  (`{{lead.country}}`/`{{location}}`); siehe Sprach-Regel-Bausteine.
- **Absender-Identität** → `{{organization.description}}` +
  `{{organization.website_url}}`.

Wenn ein gewünschter Inhalt keinen passenden Platzhalter hat: NICHT erfinden —
den nächstliegenden vorhandenen nutzen oder Anthony fragen, ob ein neues
Playbook-Feld nötig ist.
