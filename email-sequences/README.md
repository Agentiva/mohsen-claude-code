# amplifa Master-Email-Sequenzen — Index

14 Master-Sequenzen (fertige System-Prompts mit `{{...}}`-Platzhaltern für app.amplifa.ai → Playbook → Sequence → Email-Step). Gebaut nach dem Hausstil-Skill `.claude/skills/amplifa-email-prompt-builder`.

## Entscheidungsbaum (Miro-Logik)

```
Signale?
 ├─ Mit Signale   → Familie AUGENHÖHE (zurückhaltend, Signal-Hook)        → 10 Mails je Master
 └─ Ohne Signale  → Familie DISC-SALES (offensiv, ICP-Pain-Hook)          →  9 Mails je Master
        │
   Welche Länder?
     ├─ DACH        → Deutsch (Hochdeutsch, CH nie Schweizerdeutsch)
     ├─ EU          → Land-Routing: DE/AT/CH = Deutsch, alle anderen = Englisch
     └─ Asien-USA   → durchgehend Englisch, Wortzahlen etwas kürzer (~110–145)
        │
   Welche CTA?
     ├─ 15-Min digital
     ├─ 30-Min digital   (Anti-Deliverable-Regel zwingend)
     └─ Vor-Ort-Termin   (NUR DACH — bei EU/Asien-USA nicht sinnvoll)
```

## Matrix (14 Master)

| Familie / Region | 15-Min digital | 30-Min digital | Vor-Ort |
|---|---|---|---|
| **MIT · DACH** | `mit-signale_dach_15min-digital.md` | `mit-signale_dach_30min-digital.md` | `mit-signale_dach_vorort.md` |
| **MIT · EU** | `mit-signale_eu_15min-digital.md` | `mit-signale_eu_30min-digital.md` | — |
| **MIT · Asien-USA** | `mit-signale_asien-usa_15min-digital.md` | `mit-signale_asien-usa_30min-digital.md` | — |
| **OHNE · DACH** | `ohne-signale_dach_15min-digital.md` | `ohne-signale_dach_30min-digital.md` | `ohne-signale_dach_vorort.md` |
| **OHNE · EU** | `ohne-signale_eu_15min-digital.md` | `ohne-signale_eu_30min-digital.md` | — |
| **OHNE · Asien-USA** | `ohne-signale_asien-usa_15min-digital.md` | `ohne-signale_asien-usa_30min-digital.md` | — |

→ 2 Signale × (DACH 3 + EU 2 + Asien-USA 2 CTA) = **14 Master**.
Vor-Ort nur bei DACH (Skill-Guardrail: bei USA/Asien Vor-Ort unrealistisch → nur digital).

## Sequenz-Positionen

**MIT Signale (AUGENHÖHE, 10 Mails):** E1 Cold-Open · E2 Cold-Open-Variante · E3 Follow-up · E4 Kurzvariante · E5 mit P.S. · E6 Follow-up neuer Blickwinkel · E7 Storytelling · E8 Pattern-Interrupt · E9 radikale Transparenz · E10 mutiger Reframe.

**OHNE Signale (DISC-SALES, 9 Mails):** E1 Cold-Open · E2 Follow-up (Bullets) · E3 kompakt · E4 ultrakurz · E5 P.S.-Recovery · E6 Perspektivwechsel · E7 Story · E8 Pattern-Interrupt · E9 radikale Transparenz.

## Globale Regeln (in jedem Prompt verankert)

- **Output-Zeichen-Regel:** im fertigen E-Mail-Text keine der Zeichen `— – * # +`. Reiner Fließtext mit Komma/Punkt/Klammern. Normale Wort-Bindestriche (`Vor-Ort-Termin`, `15-minütig`, `800-VDC`) erlaubt.
- **Anti-Deliverable-Regel:** keine erfundenen Pseudo-Angebote („48h-Audit", „Quick-Check", „Marktradar", „ROI-Vergleich").
- **DISC-Schreibstil** (`{{lead.disc_profile}}`: D/I/S/C + Kombis) steuert Ton, Länge, Format, CTA-Frame; Wortzahlen aus der DISC-Matrix des Skills, schrumpfen über die Sequenz.
- **Platzhalter bleiben Platzhalter** — `{{...}}` werden zur Laufzeit von amplifa pro Lead gefüllt, nie im Prompt ausfüllen.

## Achsen-Code je Master

`E«n» · «MIT/OHNE» · «REGION» · «CTA» · «FAMILIE»` — steht oben in jeder Datei als Variant-Code.
