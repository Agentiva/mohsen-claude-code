---
name: onboarding-summary-mail
description: >
  Holt die Onboarding-Unterlagen zu einer Firma aus Fathom (Meeting-Recorder via
  MCP), zieht die eingeladenen Personen aus dem passenden Outlook-Kalender-Termin
  und schreibt eine deutsche Zusammenfassungs-Mail – die NACH Bestätigung
  über den Outlook-Account des Users an alle Teilnehmer rausgeht. IMMER nutzen,
  wenn der User sinngemäß sagt: "fetch onboarding zu Firma X und schick eine
  Zusammenfassung an alle aus dem Meeting", "Onboarding Firma X zusammenfassen und
  an die Eingeladenen mailen", "schick den Teilnehmern vom Kickoff eine Summary".
argument-hint: "<Firmenname> [optional: Terminbezeichnung/Datum]"
---

# Onboarding zusammenfassen & an Meeting-Teilnehmer senden

Workflow in 5 Schritten. Bei Mehrdeutigkeit (mehrere Termine, mehrere Onboarding-
Docs) **kurz rückfragen**, sonst durchziehen.

## 1. Onboarding-Material holen (Fathom)

- **Primärquelle Fathom (MCP):** das Onboarding-/Kickoff-Meeting zur Firma suchen
  (nach Firmenname bzw. Meeting-Titel). Aus dem Treffer Summary, Action Items und
  – wenn nötig – das Transkript ziehen. Das ist die Onboarding-Grundlage.
- Bei mehreren Treffern das passende nehmen (jüngstes Onboarding/Kickoff), im
  Zweifel kurz die Liste zeigen.
- Nichts erfinden. Wenn in Fathom nichts auffindbar: sagen, nicht halluzinieren.

## 2. Passenden Outlook-Termin finden

- Im Outlook-Kalender nach dem Termin suchen (Firmenname / "Onboarding" /
  "Kickoff"). Bei mehreren Treffern den vom User genannten bzw. den jüngsten
  relevanten nehmen – im Zweifel die Liste zeigen und fragen.
- **Teilnehmer/Eingeladene** des Termins extrahieren (Attendees).

## 3. Empfängerliste aufbereiten

- Standardmäßig **interne amplifa-Adressen (@amplifa.ai) ausschließen**, außer der
  User will sie drin haben. Externe Teilnehmer = primäre Empfänger.
- Liste dem User zeigen, bevor gesendet wird.

## 4. Zusammenfassungs-Mail schreiben (Deutsch)

Inhalt aus dem Onboarding-Material:
- kurzer Einstieg + Bezug auf den Termin
- Firmen-/Produkt-Kontext in 2–3 Sätzen
- vereinbarte Zielgruppe / ICP & Kanäle
- konkrete nächste Schritte / Action Items mit Verantwortlichen
- freundlicher Abschluss

Anrede: Default **Du**, wenn die bestehende Beziehung/der Thread schon auf Du
läuft (amplifa-Standard bei Kunden), sonst **Sie**. Im Zweifel Sie und anbieten,
auf Du umzustellen. Ton: amplifa, warm, knapp, professionell.

## 5. Senden – aber mit Bestätigungs-Gate

- **Nicht automatisch senden.** Erst Entwurf + Empfängerliste zeigen, dann auf das
  „OK / senden" des Users warten. Danach über den Outlook-Account des Users an
  alle Empfänger rausschicken.
- Grund: Client-facing Mails dürfen nie ungeprüft rausgehen. (Wenn der User
  ausdrücklich „direkt senden ohne Rückfrage" sagt, darf das Gate entfallen.)

## Benötigte Connectors / Rechte

Fathom (MCP, Meetings/Onboarding lesen), Microsoft 365 (Outlook-Kalender lesen für
die Teilnehmer + Mail senden). Lese-Tools dürfen pre-authorized sein; den
**Mail-Versand bewusst NICHT** vorab freigeben, damit das Bestätigungs-Gate greift.
(Exakte MCP-Tool-Namen ggf. an dein Claude-Code-Connector-Setup anpassen.)
