---
name: html-signatur
description: >
  Baut aus einem Screenshot (oder bestehendem HTML) einer E-Mail-Signatur eine
  saubere, Outlook-feste HTML-Signatur 1:1 nach. IMMER nutzen, wenn der User ein
  Bild/Screenshot einer Signatur reinwirft und sagt "bau die nach", "Signatur als
  HTML", "mach mir die Signatur", "Kundensignatur nachbauen" oder ein bestehendes
  (oft Word-verseuchtes) Signatur-HTML bereinigen will. Auch nutzen, wenn nur grob
  "E-Mail-Signatur" + ein Bild im Spiel ist, selbst ohne das Wort "HTML".
argument-hint: "[Firma/Name optional] + Screenshot der Signatur"
---

# HTML-Signatur nachbauen

Ziel: aus einem Screenshot (oder Roh-HTML) eine **pixelnahe, in allen Mailclients
funktionierende** HTML-Signatur erzeugen, fertig zum Einfügen in die
Signatur-Einstellungen (Outlook, Gmail, Apple Mail).

## Ablauf

1. **Vorlage auslesen.** Aus dem Screenshot ALLE Elemente extrahieren:
   - Name, Titel/Rolle, Firma
   - Telefon, Mobil, Fax, E-Mail, Website
   - Adresse, Social-Links (LinkedIn, YouTube, Insta …)
   - Logo, Akzentfarben (Hex schätzen), Schriftart, Layout
     (Logo links vs. oben, Trennlinien, Spaltenaufbau).
   Wenn stattdessen Roh-HTML geliefert wird: erst entrümpeln (s. u.).

2. **Aufbau = table-based mit Inline-Styles.** Keine externen CSS-Klassen,
   kein `<div>`-Flexbox-Layout – Outlook rendert das nicht zuverlässig.
   Alles über `<table>`, `<td>`, `width`, `cellpadding`, `style="…"` inline.

3. **Alles klickbar machen:**
   - E-Mail → `mailto:`
   - Telefon/Mobil → `tel:` im Format `+49…` (Leerzeichen/Klammern raus)
   - Website → `https://…`
   - Social → direkte Profil-URLs.

4. **Logo:** möglichst **gehostete PNG-URL** verwenden (frag nach der URL, falls
   nicht geliefert). **SVG meiden** – wird in Outlook oft nicht angezeigt. Wenn
   keine URL da ist: Platzhalter-URL einsetzen und mit `[LOGO-URL EINSETZEN]`
   markieren. Base64-Einbettung nur als Fallback anbieten (sichtbar überall, aber
   bläht die Mailgröße auf).

5. **Pflichtangaben (DE GmbH):** wenn im Screenshot vorhanden oder geliefert,
   Geschäftsführer / HRB / USt-IdNr / Adresse als **kleinen, grauen** Footer
   (`font-size:11px; color:#888`). Nur einsetzen, was wirklich vorliegt – nichts
   erfinden. Fehlende Felder als `[PLATZHALTER]` kennzeichnen.

6. **Output:** eine einzelne, eigenständige `.html`-Datei in
   `/mnt/user-data/outputs/`, fertig zum Copy-Paste. Danach kurz die Felder
   nennen, die der User noch ersetzen muss (Platzhalter, Logo-URL).

## Roh-HTML bereinigen (falls Word/Outlook-Export geliefert)

Restlos entfernen: VML (`<v:…>`), conditional comments (`<!--[if …]>`),
`MsoNormal`, `o:p`, `mso-…`-Styles, leere `<span>`-Verschachtelungen. Häufiger
Bug: ein Markdown-Link `[text](url)` mitten im HTML – durch echtes
`<a href="url">text</a>` ersetzen.

## Regeln

- Layout treu nachbauen, nicht „verbessern", außer der User bittet darum.
- Maximale Breite ~600px, damit es im Mailfenster nicht bricht.
- Keine Platzhalter-Daten erfinden – lieber `[NAME]`, `[TEL]` etc. markieren und
  am Ende auflisten.
- Wenn mehrere Personen/Domains: pro Person eine Datei, klar benannt.
