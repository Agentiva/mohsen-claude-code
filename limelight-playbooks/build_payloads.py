import json, uuid
U = lambda: str(uuid.uuid4())

def persona(name, title, pains):
    return {"id": U(), "name": name, "title": title, "pain_points": pains}
def uc(t, d): return {"id": U(), "title": t, "description": d}
def ref(c, d): return {"id": U(), "customer_name": c, "description": d}
def pp(claim, d): return {"id": U(), "claim": claim, "description": d}

def order(items):
    for i, it in enumerate(items, 1): it["order"] = i
    return items

# ---------------- PLAYBOOK 33 : B2B Kunden (de) ----------------
p33_desc = """LIMELIGHT ist ein Münchner Full-Service-Dienstleister für Veranstaltungstechnik und Live-Kommunikation. Das Unternehmen arbeitet für Marken, Konzerne, Agenturen und Institutionen, die bei Corporate Events, Kongressen, Jahreskonferenzen, Galas und Jubiläen professionell in Szene gesetzt werden wollen. Gründungsjahr und genaue Mitarbeiterzahl werden auf der Website nicht ausgewiesen (zu verifizieren); positioniert wird LIMELIGHT ausdrücklich als Technikpartner, der die Marke versteht – nicht als reiner Gerätevermieter.

Kernleistung ist die ganzheitliche technische Eventproduktion aus einer Hand: Lichtdesign, Tontechnik, Video- und Medientechnik, hochauflösende LED-Wände, Event-IT (WLAN, Netzwerk, Zugangskontrolle) sowie Rigging, Bühnen- und Sonderbau. Von Beratung und Konzeption über Aufbau und Durchführung bis zum Abbau übernimmt LIMELIGHT den kompletten technischen Part – inklusive Livestreaming und hybriden Formaten. Der Kunde bucht einen einzigen Partner statt mehrere Gewerke einzeln zu koordinieren.

Im Markt differenziert sich LIMELIGHT über echte Single-Source-Verantwortung, einen eigenen großen Gerätepark mit Lager in München (kurzfristige Lieferfähigkeit) und nachgewiesene Projekte mit anspruchsvollen Marken. Set- und Sonderbau auf TV-/Film-Niveau (etwa zum 100-jährigen ARRI-Jubiläum), eine bis 8.000+ Teilnehmer skalierbare Event-IT und seit der Pandemie intensiv ausgebaute Hybrid-Kompetenz heben LIMELIGHT von klassischen Technikdienstleistern ab.

INDUSTRY: Veranstaltungstechnik, Live-Kommunikation, Corporate Events, Kongresse & Tagungen, Markeninszenierung/Brand Experience

USPs: 1. Licht, Ton, Video, LED, Event-IT und Bühnen-/Sonderbau aus einer Hand – ein Ansprechpartner statt vieler Gewerke. 2. Eigener großer Gerätepark und Lager in München für kurzfristige Projekte. 3. Hochauflösende LED-Wände mit variablem Pixel-Pitch für jede Betrachtungsdistanz. 4. Event-IT skalierbar von 20 bis 8.000+ Teilnehmer unter höchsten Sicherheitsstandards. 5. Hybrid-Event- und Livestreaming-Kompetenz, seit der Pandemie intensiv ausgebaut. 6. Set- und Sonderbau auf TV-/Film-Niveau (u. a. ARRI-Jubiläum). 7. Referenzprojekte mit Porsche, Volkswagen, Telefónica und TEDx München. 8. Partner, der die Marke inszeniert, statt nur Technik zu liefern."""

p33 = {
 "language":"de","status":"draft",
 "product":{"name":"B2B Kunden","metadata":{},"description":p33_desc},
 "value_proposition":"LIMELIGHT nimmt Marketing- und Event-Verantwortlichen die gesamte technische Verantwortung für ihre Veranstaltung ab – von Licht, Ton, Video und Bühne bis Event-IT und Livestream, koordiniert aus einer Hand. So entfällt das Jonglieren mehrerer Technikgewerke, Schnittstellen- und Pannenrisiken sinken deutlich, und Marketing und Management können sich auf das Wesentliche konzentrieren: den markenwirksamen Auftritt selbst.",
 "personae":order([
   persona("Head of Events Julia","Head of Events, Eventmanager:in, Leiter:in Veranstaltungen, Event Marketing Manager, Manager Corporate Events",
     ["Sie muss für ein einzelnes Event mehrere Technikgewerke – Licht, Ton, Video, IT – koordinieren und verliert Zeit an Abstimmung und Schnittstellen.",
      "Sie trägt das Risiko, dass eine technische Panne live vor Gästen den Markenauftritt beschädigt.",
      "Sie braucht einen Partner, der mitdenkt und kreative Vorschläge einbringt, statt nur abzuarbeiten, was bestellt wurde.",
      "Sie steht unter Druck, hybride Formate und Besuchervernetzung sauber umzusetzen, ohne dafür zusätzliche Dienstleister zu suchen.",
      "Sie muss Qualität, Nachhaltigkeit und Budget gleichzeitig gegenüber der Geschäftsführung rechtfertigen."]),
   persona("Agentur-Producer Laura","Producer Eventagentur, Projektleiter:in Live-Marketing, Head of Production (Eventagentur), Senior Projektmanager:in Live-Kommunikation, Executive Producer Agentur",
     ["Sie produziert Events für Markenkunden und braucht einen Technikpartner, der unter ihrem Namen fehlerfrei abliefert.",
      "Sie muss kurzfristige Kundenwünsche und Last-Minute-Änderungen technisch umsetzen, ohne den Zeitplan zu sprengen.",
      "Sie will einen verlässlichen Full-Service-Partner mit eigenem Gerätepark, statt mehrere Gewerke einzeln zu steuern.",
      "Sie trägt gegenüber ihrem Kunden die Verantwortung, wenn Technik live nicht funktioniert.",
      "Sie braucht einen Partner, der kreative Mehrwerte einbringt und die Marke ihres Kunden versteht."]),
   persona("Marketingleiterin Sandra","Marketingleiter:in, Head of Marketing, Head of Brand, Leiter:in Marktkommunikation, Brand Experience Manager",
     ["Sie verantwortet, dass Marke und Botschaft auf der Bühne konsistent und hochwertig erlebbar sind.",
      "Sie fürchtet einen technisch mittelmäßigen Auftritt, der die Positionierung der Marke unterläuft.",
      "Sie braucht eine Displaylösung (LED), die spontane Content-Änderungen während der Veranstaltung erlaubt.",
      "Sie will einen Partner mit vorzeigbaren Marken-Referenzen, den sie intern verantworten kann."]),
   persona("Event-Projektmanager Tim","Event-Projektmanager, Projektleiter Events, Veranstaltungskoordinator, Event Operations Manager, Assistenz Eventmanagement",
     ["Er koordiniert Auf- und Abbau, Zeitpläne und Gewerke operativ und haftet, wenn ein Gewerk kippt.",
      "Er braucht verlässliche Ansprechpartner, die auch kurzfristig und unter Zeitdruck liefern.",
      "Er will einen technischen Ablauf ohne Überraschungen und sauber dokumentierte Prozesse.",
      "Er muss mehrere parallele Veranstaltungen stemmen und sucht Entlastung durch einen Full-Service-Partner."]),
   persona("Leiterin Interne Kommunikation Katrin","Leiter:in Interne Kommunikation, Head of Internal Communications, Corporate Communications Manager, Referent:in Unternehmenskommunikation",
     ["Sie inszeniert Kick-offs, Townhalls und Hauptversammlungen, die on- und offline gleichzeitig funktionieren müssen.",
      "Sie braucht sichere Event-IT und stabilen Livestream, damit verteilte Belegschaften zuverlässig teilnehmen.",
      "Sie will interaktive Formate wie Live-Abstimmungen und Besuchervernetzung, ohne separate Anbieter zu steuern.",
      "Sie steht in der Verantwortung, wenn ein unternehmensweites Format technisch nicht sauber läuft."]),
   persona("Geschäftsführer Michael","Geschäftsführer, CEO, Inhaber, Vorstand, Managing Director",
     ["Er will bei Jubiläen und Galas einen Auftritt, der dem Unternehmen und den Gästen gerecht wird, ohne sich selbst um Technik zu kümmern.",
      "Er erwartet Budgettransparenz und einen Partner, der echte Verantwortung übernimmt.",
      "Er trägt das Reputationsrisiko, wenn ein Großereignis technisch scheitert."]),
 ]),
 "use_cases":order([
   uc("Ganzheitliche technische Eventproduktion für Corporate Events und Kongresse","Große Unternehmen brauchen für Jahreskonferenzen, Kongresse oder Jubiläen einen einzigen Technikpartner, der Licht, Ton, Video, Bühne und Event-IT koordiniert liefert. LIMELIGHT übernimmt die gesamte technische Produktion aus einer Hand – von Beratung und Konzeption über Aufbau und Durchführung bis zum Abbau. Der Kunde spart Koordinationsaufwand, reduziert Schnittstellenrisiken und erhält ein konsistentes, professionelles Ergebnis."),
   uc("Event-IT und Besuchervernetzung für Kongresse und Messestände","Aussteller und Kongressveranstalter wollen Gäste digital vernetzen – untereinander und mit der Technik im Saal oder am Stand. LIMELIGHT stellt professionelle WLAN-Infrastruktur, Netzwerke und interaktive Anwendungen bereit, mit denen Besucher sich mit eigenen oder gestellten Devices verbinden, an Abstimmungen teilnehmen und Inhalte interaktiv erleben. Höchste Sicherheitsstandards und Skalierung von 20 bis 8.000+ Teilnehmern sichern den reibungslosen Betrieb."),
   uc("LED-Wand-Lösungen für Corporate-Präsentationen und Produktlaunches","Unternehmen suchen eine hochauflösende Displaylösung, die Besucher beeindruckt und die Marke optimal in Szene setzt. LIMELIGHT liefert LED-Wände in variablen Größen und Pixel-Pitches, die sich nahtlos in Bühnen- und Eventdesign einfügen, mehrere Bildquellen gleichzeitig darstellen und spontane Content-Änderungen während des Events erlauben. Das Ergebnis ist ein flexibler, visuell herausragender Markenauftritt."),
   uc("Hybrid-Events und Livestreaming für verteilte Zielgruppen","Unternehmen und Verbände wollen Veranstaltungen nicht nur vor Ort, sondern auch für ein virtuelles Publikum zugänglich machen. LIMELIGHT kombiniert Live-Event-Technik mit professionellem Livestreaming und interaktiven Online-Features und bindet physische wie digitale Teilnehmer nahtlos ein. Diese Hybrid-Kompetenz wurde seit der Pandemie intensiv ausgebaut und sorgt für ein konsistentes Erlebnis über alle Kanäle."),
   uc("Jubiläums-Galas und Festveranstaltungen in großem Maßstab","Zu Firmenjubiläen und Galas erwarten Unternehmen einen Auftritt, der Anlass und Gästen gerecht wird. LIMELIGHT verantwortet Licht, Ton, Video, Bühne und Sonderbau für Gala-Dinner und Corporate Events in großem Maßstab – bis hin zu mehrtägigen Formaten. Das Ergebnis ist eine durchgängig inszenierte Veranstaltung ohne technische Brüche."),
 ]),
 "references":order([
   ref("Porsche","Technische Produktion des Porsche-Panamera-Spots mit komplexer Licht- und Videotechnik für eine hochwertige Fahrzeug-Inszenierung."),
   ref("Volkswagen","Mehrwöchiges VW-Sales-Event in Saragossa mit extravaganten Shows und Meetingreihen – ein Großprojekt mit umfangreicher Licht-, Video- und Bühnentechnik."),
   ref("Telefónica","Event-IT und technische Gesamtproduktion für Telefónica-Kick-off und Hauptversammlung."),
   ref("TEDx München","Ganzheitliche Veranstaltungstechnik für die TEDx-München-Konferenz – Licht, Ton, Video und Bühne aus einer Hand."),
   ref("Hamberger","Technische Produktion der Jubiläums-Gala zum 150-jährigen Bestehen – Gala-Dinner und Corporate Event in großem Maßstab."),
 ]),
 "proof_points":order([
   pp("Markeninszenierung auf Werbespot-Niveau für Porsche","Für den Porsche-Panamera-Spot verantwortete LIMELIGHT die komplexe Licht- und Videotechnik einer hochwertigen Fahrzeug-Inszenierung – Beleg für Bild- und Lichtqualität auf Produktions-Niveau."),
   pp("Ganzheitliche Technik für TEDx München aus einer Hand","Für die TEDx-München-Konferenz lieferte LIMELIGHT Licht, Ton, Video und Bühne gebündelt – Beleg für echte Single-Source-Eventproduktion."),
   pp("Großprojektfähigkeit beim mehrwöchigen VW-Sales-Event in Saragossa","Das mehrwöchige Volkswagen-Sales-Event mit Shows und Meetingreihen zeigt, dass LIMELIGHT auch umfangreiche, länderübergreifende Großprojekte technisch stemmt."),
   pp("Event-IT skalierbar von 20 bis 8.000+ Teilnehmer","LIMELIGHTs Event-IT deckt WLAN, Netzwerke, Zugangskontrolle und Datenverkehrssteuerung unter höchsten Sicherheitsstandards ab – skalierbar von kleinen Runden bis über 8.000 Teilnehmer, u. a. umgesetzt für Telefónica."),
   pp("Jubiläumskompetenz in großem Maßstab bei Hamberger","Die Jubiläums-Gala zum 150-jährigen Bestehen von Hamberger belegt die Fähigkeit, große Gala- und Festformate durchgängig technisch zu inszenieren."),
 ]),
}
json.dump(p33, open("p33.json","w"), ensure_ascii=False)
print("p33 ok personae", len(p33["personae"]), "uc", len(p33["use_cases"]), "ref", len(p33["references"]), "pp", len(p33["proof_points"]))
