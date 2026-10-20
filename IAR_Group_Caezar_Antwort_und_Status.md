# IAR Group — Antwort auf Caezars Fragen 1–3 + Status

Stand: 20.10.2026 · Amplifa Org 34 · https://app.amplifa.ai/admin/organizations/34

---

## Was ich geprüft habe

| Prüfpunkt | Befund |
|---|---|
| Sender in Org 34 | Caezar Ilaya (ID 44) war **noch aktiv** · Rita Sousa (ID 266) aktiv |
| Agents | 12 gesamt: 6 US-Kampagnen `paused`, 6 EU-Kampagnen `draft` |
| Konversationen | **657** insgesamt, alle aus den US-Kampagnen unter Caezars Identität |
| Davon positiv | **15** offen: 11 `interested`, 4 `meeting_request` |
| Versandadressen | Nie `caezar.ilaya@iargroup.com` — immer separate Sending-Domains |

## Durchgeführter Fix

**Sender Caezar Ilaya (ID 44) auf `inactive` gesetzt.** Damit kann er in keiner Kampagne
mehr als Absender ausgewählt werden. Verifiziert per Re-Read, `updated_at` 2026-10-20T07:55:53Z.

---

## Die Antworten im Detail

### Frage 1 — Kommt alles nur aus Ritas Postfächern?

Ja, und zwar schon strenger als gedacht: **Aus Caezars echtem Postfach ging nie etwas raus.**
Der Versand lief immer über eigene Cold-Email-Domains, die seinen Namen trugen:

- `iar-group-automation.com`
- `iargroup-automation.com`
- `iargroup-industrial.com` / `.net` / `.org`
- `iargroup-solutions.com`

Was ihn trotzdem sichtbar gemacht hat: In **jeder Signatur** standen sein Name, sein Titel,
seine Durchwahl (847) 946-2241 und seine echte Adresse `caezar.ilaya@iargroup.com`. Für den
Empfänger war es also eine Mail von Caezar — nur technisch nicht aus seinem Postfach.

Für den Relaunch: neue dedizierte Domains auf Ritas Namen, ihre Signatur, ihr Postfach in
Lissabon. Sein Sender-Profil ist jetzt deaktiviert.

### Frage 2 — Was passiert mit den laufenden Sequenzen aus seinem Postfach?

**Es läuft bereits nichts mehr.** Alle sechs US-Kampagnen stehen auf `paused`, seit dem
Stopp im August ist kein weiterer Sequenzschritt rausgegangen. Mit dem deaktivierten Sender
kann auch nichts versehentlich wieder anlaufen.

**Aber:** Unter den 657 Konversationen sind **15 offene positive** — 11 Interessenten und
**4 konkrete Meeting-Anfragen**. Die sind nicht verloren, werden aber auch nicht weiter
bespielt. Die sollten wir ihm nennen, bevor sie verfallen.

### Frage 3 — Englisch für die USA, Landessprache in Europa

Ist so konfiguriert:

| Kampagne | Sprache |
|---|---|
| Electrification / Micro Molding / Precision Metal Forming — USA | `en` |
| dieselben drei — DACH | `de` |
| dieselben drei — Spanien | `es` |

**Der Vorfall vom August ist erklärbar und behoben.** Am 12.08. ging eine Mail an Chris
Cassady bei Teleflex (USA) mit englischer Anrede und deutschem Fließtext raus — das kam aus
der gemeinsam genutzten US-Master-Sequenz. Die neuen EU-Kampagnen hängen an eigenen
Sequenzen pro Region (`Master Sequenz BS - EU - HUMAN` für DACH, `Master Sequenz Spanien - LIT`
für Spanien), damit ist die Sprache fest an die Region gebunden.

---

## Zwei offene Punkte vor dem Livegang

**1. Es gibt keine Portugal-Kampagne.** Angelegt sind nur DACH und Spanien. Caezar hatte
Portugal und Spanien als erste Priorität genannt — ohne PT-Agent haben die 553 portugiesischen
Firmen aus der Liste kein Ziel.

**2. Die Leads sind erst teilweise importiert.** In den sechs EU-Kampagnen liegen aktuell
2.655 Leads, die fertige Liste hat 4.637 Firmen.

| Kampagne | Leads |
|---|---|
| Precision Metal Forming — DACH | 1.253 |
| Precision Metal Forming — Spain | 744 |
| Micro Molding — DACH | 405 |
| Micro Molding — Spain | 52 |
| Electrification — DACH | 197 |
| Electrification — Spain | 4 |

Nebenbefund: Ritas Job-Titel steht im System auf „Communication Strategist". Caezar wollte im
Call vom 26.08. auf „Marketing Specialist" ändern. Habe ich nicht angefasst.

---
---

# E-Mail-Entwurf für Caezar (Englisch)

**Betreff:** IAR Group campaign relaunch — your three questions answered

---

Hi Caezar,

Thanks for the clear questions. We went through the full setup in the platform before answering, so here is exactly where things stand on all three.

**1. Sending will come only from Rita's addresses**

Confirmed. Your sender profile has been deactivated in the platform today, so it can no longer be selected for any campaign.

One clarification worth having on record: nothing was ever sent from your actual mailbox, caezar.ilaya@iargroup.com. All outbound ran on separate dedicated sending domains set up for deliverability — iar-group-automation.com, iargroup-automation.com, iargroup-industrial.com, and a few variants. Your real address and direct line appeared in the signature only, which is why it read as coming from you.

For the relaunch, the same principle applies with Rita: dedicated sending domains in her name, her signature, her Lisbon mailbox. Your name and contact details will not appear anywhere in the outbound.

**2. Existing conversations from the earlier campaigns**

All six US campaigns have been paused since August, so no further sequence steps have gone out, and with your sender now deactivated nothing can restart under your name. That is the stop you asked for.

There is one thing we do not want to lose quietly. Of the 657 conversations from those campaigns, 15 are still open and positive: 11 contacts marked interested and 4 who explicitly asked for a meeting. They will not be contacted again by the system. We would suggest either handing them to Rita to pick up, or you closing them out personally — your call, but they are real and currently sitting idle.

**3. Language**

Set up as you asked:

- United States: English
- Germany, Austria, Switzerland: German
- Spain: Spanish

On the mixed-language email you saw in August: that came from a shared US master sequence, where a European language variant could reach a US recipient. The new European campaigns run on their own sequences per region, so the language is now tied to the region and cannot cross over.

**Before we launch, two things we want to confirm with you**

First, we currently have campaigns for German-speaking Europe and for Spain, but not for Portugal. Since you named Portugal and Spain as the first markets, we would like to set up a Portuguese campaign as well — we have 553 Portuguese companies ready for it. Shall we?

Second, we are still importing the remaining target companies. 2,655 are loaded across the six European campaigns; the full qualified list is 4,637 companies across the three playbooks.

Separately, we have also reworked the three playbooks for the European launch: all US-specific wording is gone, IAR Group is now positioned through its actual European presence — Zofingen, IAR Deutschland, Mafra, Porto, Valencia — and all reference customers have been removed as you instructed.

Let us know on Portugal and we will get everything live.

Best regards,
