---
name: onboarding-summary-mail
description: >
  Holt die Onboarding-Unterlagen zu einer Firma aus Fathom (Meeting-Recorder via
  MCP), zieht die eingeladenen Personen aus dem passenden Outlook-Kalender-Termin
  und schreibt eine deutsche Zusammenfassungs-Mail – die standardmäßig als
  Outlook-Draft an alle Teilnehmer angelegt wird (der User prüft & sendet selbst
  in Outlook). IMMER nutzen, wenn der User sinngemäß sagt: "fetch onboarding zu
  Firma X und schick/erstell eine Zusammenfassung an alle aus dem Meeting",
  "Onboarding Firma X zusammenfassen und an die Eingeladenen mailen", "schick den
  Teilnehmern vom Kickoff eine Summary", "erstelle einen Draft in Outlook an alle
  aus dem Call".
argument-hint: "<Firmenname> [optional: Terminbezeichnung/Datum]"
---

# Onboarding zusammenfassen & als Outlook-Draft an Meeting-Teilnehmer anlegen

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
- **Echte E-Mail-Adressen** der Empfänger aus dem Outlook-Termin (Attendees-Feld)
  ziehen – nicht nur Namen. Fathom liefert nur Namen; die Adressen kommen aus dem
  Kalender-Event.
- Liste dem User zeigen, bevor der Draft angelegt wird.

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

## 5. Outlook-Draft anlegen (Standard) – nicht automatisch senden

- **Standard-Output ist ein Outlook-Draft**, adressiert an alle Empfänger aus
  Schritt 3 (To = externe Teilnehmer; amplifa-Kollegen optional auf CC, wenn der
  User das will). Betreff + formatierter Body aus Schritt 4. So bleibt die finale
  Kontrolle (Prüfen & Senden) beim User direkt in Outlook.
- **Niemals automatisch senden.** Den Draft anlegen und Empfängerliste + Inhalt im
  Chat zeigen. Nur wenn der User ausdrücklich „direkt senden" sagt UND ein
  Sende-Tool verfügbar ist, darf gesendet werden.
- **Draft-Tool:** das Outlook-/Microsoft-365-Tool zum Erstellen eines Mail-Entwurfs
  nutzen (Graph `createDraft` bzw. das entsprechende MCP-Write-Tool). Tool-Namen an
  das jeweilige Connector-Setup anpassen.
- **Fallback bei read-only Connector:** Ist nur ein lesender Microsoft-365-Connector
  verbunden (nur Suche/Lesen von Mail/Kalender, kein Draft-/Send-Tool), kann der
  Draft NICHT direkt in Outlook geschrieben werden. Dann: das ehrlich sagen, die
  echten Empfänger-Adressen + den versandfertigen Entwurf (Betreff + Body) im Chat
  liefern, sodass der User ihn 1:1 in Outlook einfügen kann. Optional als Alternative
  einen Slack-Entwurf im Kundenchannel anbieten.

## Benötigte Connectors / Rechte

Fathom (MCP, Meetings/Onboarding lesen), Microsoft 365 (Outlook-Kalender + -Mail).
Für den Standard-Workflow wird ein **Outlook-Write-Tool zum Draft-Anlegen** benötigt;
Lese-Tools (Kalender/Teilnehmer) dürfen pre-authorized sein. Den **Mail-Versand**
bewusst NICHT vorab freigeben – Standard ist Draft, nicht Send. Ist nur ein
read-only Microsoft-365-Connector vorhanden, greift der Fallback aus Schritt 5.
(Exakte MCP-Tool-Namen ggf. an dein Claude-Code-Connector-Setup anpassen.)
