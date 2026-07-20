import json, uuid
U=lambda:str(uuid.uuid4())
def persona(n,t,p): return {"id":U(),"name":n,"title":t,"pain_points":p}
def uc(t,d): return {"id":U(),"title":t,"description":d}
def ref(c,d): return {"id":U(),"customer_name":c,"description":d}
def pp(c,d): return {"id":U(),"claim":c,"description":d}
def order(x):
    for i,it in enumerate(x,1): it["order"]=i
    return x

# ---------- PLAYBOOK 30 : Producer US/CA (en) ----------
p30_desc="""LIMELIGHT is a Munich-based full-service provider for event and production technology, bringing Hollywood-level production infrastructure to European shoots and events. The company works for international producers, studios, agencies and brands that shoot or stage in Germany and Central Europe and need a reliable local partner who speaks the language of creative vision and executes flawlessly. Founding year and exact headcount are not stated on the website (to be verified); LIMELIGHT positions itself as a full-service technical partner rather than a pure equipment renter.

The core offering for this segment is end-to-end production support from a single source: state-of-the-art LED walls for virtual production, custom set and scenic construction, lighting design, sound engineering, camera and video systems, live broadcast infrastructure and event IT. LIMELIGHT covers concept, build, on-set operation and strike, and can supply either a full technical crew or dry-hire equipment from its own large Munich inventory – ideal for US and Canadian productions on the ground in Central Europe.

LIMELIGHT differentiates through single-source responsibility, a deep in-house equipment stock (especially LED walls and advanced AV), and proven high-end craftsmanship – from bespoke sets for ARRI's 100th anniversary to Porsche commercial productions. English-fluent coordination, local expertise on venue, power and rigging standards, and an extensive partner network for dry hire remove the friction international producers usually face when working across time zones and regulations.

INDUSTRY: Film & TV Production, Virtual Production, Live Events & Corporate Production, Broadcast, Event Technology

USPs: 1. Full technical package from one source: LED walls, custom sets, lighting, audio, video and broadcast. 2. High-resolution LED walls with variable pixel pitch for virtual production and live stages. 3. Custom set and scenic construction at TV/film level (e.g. ARRI 100th anniversary). 4. Large in-house Munich inventory plus a broad dry-hire partner network. 5. English-fluent crew familiar with US-standard workflows. 6. Local expertise on European venue, power and rigging standards. 7. Proven work for demanding brands such as Porsche and ARRI. 8. One reliable partner on the ground – no juggling multiple local vendors."""
p30={"language":"en","status":"draft",
 "product":{"name":"Producer US/CA","metadata":{},"description":p30_desc},
 "value_proposition":"LIMELIGHT gives international producers a reliable European partner who delivers US-level production value without them having to be on-site for every step. With state-of-the-art LED-wall technology, custom set construction and a full-service technical crew that speaks fluent English and understands US workflows, LIMELIGHT removes the language, time-zone and local-standard friction of shooting or staging in Central Europe.",
 "personae":order([
  persona("Executive Producer Mark","Executive Producer, Event Producer, Show Producer, Head of Production",
   ["He needs a reliable local production partner in Europe who understands US-standard workflows and communicates fluently in English.",
    "He has to guarantee his clients the same production value they expect in the US – without being on-site for every step.",
    "He worries about time-zone gaps and language barriers during critical load-in and rehearsal phases.",
    "He needs high-quality LED walls and advanced AV from a single supplier on the ground, not a patchwork of vendors."]),
  persona("Agency Producer Chris","Agency Executive Producer, Experiential Producer, Head of Production (Creative/Experiential Agency), Brand Experience Producer, Senior Event Producer",
   ["He produces brand experiences for clients in Europe and needs a local partner who delivers flawlessly under his agency's name.",
    "He must hit US client expectations on production value while managing a foreign crew remotely.",
    "He needs one English-speaking partner for LED, sets, lighting and crew instead of sourcing multiple European vendors.",
    "He carries the client relationship and cannot afford local surprises on rigging, power or permits.",
    "He wants a partner with proven brand references he can present to his client."]),
  persona("Line Producer Rachel","Line Producer, Production Manager, Production Supervisor",
   ["She is accountable for budget, schedule and load-in and cannot afford local surprises on power, rigging or permits.",
    "She needs a partner who flags European venue-specific requirements early instead of on the day.",
    "She wants one point of contact who can supply both crew and equipment to keep the call sheet tight.",
    "She has to keep quality consistent while managing costs across a foreign production."]),
  persona("Director of Photography Dave","Director of Photography, Technical Director, Virtual Production Supervisor",
   ["He needs LED walls and camera systems that deliver full creative control over dynamic backdrops on set.",
    "He wants real-time content adjustments without costly location travel.",
    "He depends on a technical partner who understands virtual production and matches the look he is after.",
    "He cannot risk image quality or color fidelity on a high-end shoot."]),
  persona("Production Coordinator Emily","Production Coordinator, Production Manager (Logistics), Production Office Coordinator",
   ["She coordinates logistics, gear and crew across borders and needs a dependable local counterpart.",
    "She needs clear, English-language communication and documentation to keep the production office aligned.",
    "She has to solve equipment and dry-hire needs fast when plans change on short notice.",
    "She is the one chasing loose ends when a local vendor drops the ball."]),
  persona("VP of Production Steven","VP of Production, Head of Production, Managing Director (Studio/Agency)",
   ["He selects vendors and carries the risk if a European partner underdelivers on a flagship project.",
    "He wants a partner with proven high-end references he can stand behind internally.",
    "He needs consistent, seamless execution across multiple productions without micromanaging each one.",
    "He values a single accountable partner over a fragmented local supply chain."]),
 ]),
 "use_cases":order([
  uc("Virtual Production with LED Walls for Film & Commercials","Productions want full creative control over dynamic backdrops without costly location travel. LIMELIGHT provides high-resolution LED walls for virtual production sets, giving directors and DoPs real-time content control on set. The result is flexible, high-fidelity backdrops that cut travel and location cost while keeping creative options open."),
  uc("Custom Set & Scenic Construction for TV Studios and Film Shoots","High-end shoots need bespoke sets that combine structural craftsmanship with integrated media technology. From ARRI's 100th anniversary to Porsche commercial productions, LIMELIGHT builds custom sets and scenic environments to a TV/film standard. Producers get a single partner for both construction and media integration, reducing coordination risk."),
  uc("Full Technical Package: Lighting, Audio, Video for Production","Multi-day shoots require a complete technical crew and equipment supply rather than separate rentals. LIMELIGHT delivers lighting design, sound engineering, camera systems and live broadcast infrastructure as one package. The production runs on one accountable crew, keeping quality and communication consistent throughout."),
  uc("Hybrid Production Studio Setup","Some productions need both physical and digital outputs from the same environment. LIMELIGHT builds temporary and permanent studio setups including stage construction, rigging and full media technology. The client gets a purpose-built studio that serves live and streamed formats without compromise."),
  uc("Equipment Rental & Dry Hire for International Productions","US and Canadian productions shooting in Central Europe often need reliable local gear on short notice. LIMELIGHT offers extensive in-house stock plus access to a broad partner network for dry hire. Producers get dependable equipment locally without shipping their own kit across the Atlantic."),
 ]),
 "references":order([
  ref("ARRI","Set and scenic construction for the ARRI Lighting Showreel marking the company's 100th anniversary – a bespoke build combining structural and media-technology expertise."),
  ref("Porsche","Technical production of the Porsche Panamera spot with complex lighting and video technology for a high-end vehicle staging."),
  ref("Telefónica","Event IT and full technical production for Telefónica kick-off and annual general meeting – evidence of large-scale, secure production capability."),
 ]),
 "proof_points":order([
  pp("Bespoke set build for ARRI's 100th anniversary","LIMELIGHT delivered the custom set and scenic construction for the ARRI Lighting Showreel marking the company's 100th anniversary – proof of film-grade set craftsmanship for one of the industry's most demanding names."),
  pp("High-end commercial production for Porsche","LIMELIGHT handled the complex lighting and video technology for the Porsche Panamera spot – evidence of image and lighting quality at commercial-production level."),
  pp("Extensive in-house LED and AV inventory in Munich","LIMELIGHT maintains a large in-house equipment stock, especially LED walls and advanced AV, plus a broad dry-hire partner network – so international productions get high-end gear locally without shipping their own."),
  pp("Single-source crew and equipment for multi-day shoots","LIMELIGHT supplies lighting, sound, camera and live-broadcast infrastructure as one package with its own crew, keeping quality and communication consistent across a full production."),
  pp("Local expertise on European venue, power and rigging standards","LIMELIGHT provides on-the-ground knowledge of European venue requirements, power and rigging standards, removing the local-compliance risk producers cannot manage from North America."),
 ]),
}
json.dump(p30,open("p30.json","w"),ensure_ascii=False)

# ---------- PLAYBOOK 29 : Messebauer & Messearchitekten (de) ----------
p29_desc="""LIMELIGHT ist ein Münchner Full-Service-Dienstleister für Veranstaltungstechnik und liefert die Technik, die Messestände zum Blickfang macht. Als Partner von Messebauern und Messearchitekten übernimmt LIMELIGHT die komplette technische Integration in bestehende Standarchitekturen – LED-Wände, Lichtdesign, Ton- und Medientechnik, Event-IT sowie Rigging und Sonderbau. Gründungsjahr und Mitarbeiterzahl werden auf der Website nicht ausgewiesen (zu verifizieren); positioniert wird LIMELIGHT als technischer Integrationspartner, nicht als reiner Verleiher.

Kernleistung für dieses Segment ist die technische Ausstattung und Integration am Messestand: hochauflösende LED-Wände in variablen Größen und Pixel-Pitches, Lichtdesign und Videoprojektion abgestimmt auf CI und Standarchitektur, interaktive Medientechnik sowie die komplette technische Logistik von Transport über Auf- und Abbau bis Betrieb während der Messelaufzeit. Durch einen eigenen großen Lagerbestand in München ist LIMELIGHT auch bei kurzfristigen Projekten und parallelen Aufträgen lieferfähig – inklusive Dry-Hire für Kollegen- und Partnerfirmen.

Im Markt differenziert sich LIMELIGHT über die nahtlose Integration von Technik in Standarchitektur, den eigenen Gerätepark mit Münchner Lager für kurzfristige Bedarfe und die Erfahrung mit anspruchsvollen Marken und Formaten. Set- und Sonderbau auf TV-/Film-Niveau, interaktive Digital-Lösungen und ein belastbares Partnernetzwerk für Dry-Hire machen LIMELIGHT zu einem Technikpartner, der auch unter engen Auf- und Abbauzeiten liefert.

INDUSTRY: Messebau, Messearchitektur, Veranstaltungstechnik, Live-Kommunikation, Digital Signage / Medientechnik

USPs: 1. Komplette technische Integration in bestehende Standarchitekturen aus einer Hand. 2. Hochauflösende LED-Wände mit variablem Pixel-Pitch, nahtlos in Standdesign integrierbar. 3. Eigener großer Lagerbestand in München für kurzfristige und parallele Projekte. 4. Dry-Hire für Kollegen- und Partnerfirmen inklusive Venue-Service. 5. Interaktive Medientechnik (Touch-Displays, Live-Demos, Content-Steuerung) für mehr Verweildauer am Stand. 6. Technische Logistik inklusive Auf-/Abbau und Betrieb während der Messelaufzeit. 7. Set- und Sonderbau auf TV-/Film-Niveau. 8. Zuverlässige Lieferfähigkeit auch unter engen Auf- und Abbauzeiten."""
p29={"language":"de","status":"draft",
 "product":{"name":"Messebauer & Messearchitekten","metadata":{},"description":p29_desc},
 "value_proposition":"Auf Messen zählt der erste Eindruck. LIMELIGHT liefert Messebauern und Messearchitekten die Technik, die Stände zum Blickfang macht – LED-Wände mit maximaler Auflösung, professionelles Lichtdesign, Tontechnik und interaktive Medientechnik – und übernimmt die komplette technische Integration in bestehende Standarchitekturen. Flexibel, schnell und mit eigenem Lagerbestand, sodass Messebauer ihr Leistungsportfolio erweitern, ohne selbst in Technik und Personal zu investieren.",
 "personae":order([
  persona("Geschäftsführer Messebau Andreas","Geschäftsführer Messebau, Inhaber Messebauunternehmen, Managing Director Exhibition, Geschäftsführung Standbau",
   ["Er muss zuverlässige Technikpartner finden, die auch kurzfristig verfügbar sind und unter Zeitdruck Qualität liefern.",
    "Er will das Leistungsportfolio um Technik erweitern, ohne selbst in teuren Gerätepark und Personal zu investieren.",
    "Er trägt das Risiko, wenn bei mehreren parallelen Projekten Material knapp wird.",
    "Er braucht einen Partner, der steigende Kundenerwartungen an interaktive und digitale Standelemente abdeckt."]),
  persona("Roadshow-Projektleiter Daniel","Projektleiter Roadshows, Leiter:in Wanderausstellungen, Projektmanager:in Mobile Messe, Tour-/Event-Logistikleiter:in, Head of Roadshow",
   ["Er bespielt mehrere Standorte nacheinander und braucht robuste, wiederverwendbare Technik plus zuverlässige Logistik.",
    "Er ist auf einen Partner mit eigenem Lagerbestand und Dry-Hire angewiesen, um Material-Engpässe über die Tour zu vermeiden.",
    "Er hat an jedem Standort enge Auf- und Abbauzeiten und kann sich keine technischen Verzögerungen leisten.",
    "Er will einen festen Ansprechpartner für die gesamte Tour statt wechselnder lokaler Dienstleister."]),
  persona("Projektleiter Messebau Stefan","Projektleiter Messebau, Projektmanager Messe, Bauleiter Messe, Standbauleiter",
   ["Er arbeitet mit extrem knappen Auf- und Abbauzeiten – jede technische Verzögerung gefährdet den gesamten Zeitplan.",
    "Er braucht einen Technikpartner, der termintreu liefert und auf der Fläche mitdenkt.",
    "Er muss Technik, Standbau und Gewerke sauber takten, ohne dass Schnittstellen zu Reibung führen.",
    "Er will einen festen Ansprechpartner statt wechselnder Subunternehmer."]),
  persona("Messearchitektin Nina","Messearchitekt:in, Kreativdirektor:in, Head of Design, Standdesigner:in, Szenograf:in",
   ["Sie muss Licht, Video und Audio so integrieren, dass sie das architektonische Konzept stärken statt zu stören.",
    "Sie will LED-Flächen, die sich nahtlos in Standdesign, CI und Besucherführung einfügen.",
    "Sie braucht einen Partner, der Design versteht und technische Machbarkeit früh einbringt.",
    "Sie steht unter Druck, jeden Stand visuell vom Wettbewerb abzuheben."]),
  persona("Technischer Leiter Frank","Technischer Leiter, Head of Technical, Leiter Technik/Werkstatt, Technische Projektleitung",
   ["Er muss technische Machbarkeit, Rigging, Strom und Sicherheit am Stand verantworten.",
    "Er braucht verlässliche Technik und Dokumentation, damit unter Zeitdruck nichts kippt.",
    "Er will einen Partner, der Sonderkonstruktionen und komplexe Integrationen sicher umsetzt.",
    "Er haftet, wenn Technik am Messetag ausfällt."]),
  persona("Strategischer Einkauf Petra","Strategischer Einkauf, Einkaufsleiter:in, Procurement Manager, Leiter:in Beschaffung",
   ["Sie sucht einen Technikpartner mit eigenem Lagerbestand, um Material-Engpässe bei parallelen Projekten zu vermeiden.",
    "Sie will planbare Konditionen und Dry-Hire-Optionen statt teurer Einzelbeschaffung.",
    "Sie braucht einen verlässlichen, skalierbaren Lieferanten für wiederkehrende Messeprojekte.",
    "Sie muss Qualität und Budget in Einklang bringen."]),
 ]),
 "use_cases":order([
  uc("LED-Wand-Inszenierungen für Messeauftritte und Produktlaunches","Messebauer und Unternehmen suchen eine hochauflösende Displaylösung, die Besucher fesselt und die Marke abhebt. LIMELIGHT stattet Messestände und Produktpräsentationen mit LED-Wänden aus, deren Inhalte flexibel anpassbar sind und dynamische Präsentationen ermöglichen. Das Ergebnis ist ein Stand mit maximaler visueller Wirkung, der sich vom Wettbewerb absetzt."),
  uc("Licht- und Medientechnik-Integration in Standarchitektur","Anspruchsvolle Standkonzepte verlangen, dass Technik das Design stärkt statt zu stören. LIMELIGHT integriert Lichtdesign, Videoprojektion und Audiosysteme in maßgefertigte Standarchitekturen – abgestimmt auf CI, Raumkonzept und Besucherführung. So entsteht ein stimmiger Auftritt, in dem Architektur und Technik als Einheit wirken."),
  uc("Interaktive Medientechnik und Digital Interaction am Messestand","Kunden erwarten zunehmend interaktive Standelemente, die über das eigene Portfolio des Messebauers hinausgehen. LIMELIGHT integriert Touch-Displays, Live-Demos und interaktive Content-Steuerung, die Standbesucher aktiv einbinden. Das erhöht Verweildauer und Interaktion am Stand messbar."),
  uc("Technische Logistik und Auf-/Abbauservice für Messeauftritte","Auf- und Abbauzeiten sind extrem knapp, und Materialengpässe gefährden parallele Projekte. LIMELIGHT übernimmt Transport, Aufbau, technischen Betrieb und Abbau während der gesamten Messelaufzeit – mit eigenem Lagerbestand und Partnernetzwerk für Dry-Hire. Der Messebauer erhält einen termintreuen Technikpartner ohne eigenes Investitionsrisiko."),
  uc("Festinstallation von Medientechnik in Showrooms und Konferenzräumen","Unternehmen mit dauerhaften Ausstellungsräumen brauchen verlässliche, fest installierte Medientechnik. LIMELIGHT plant und installiert Medientechnik inklusive Wartung und Service. So bleibt der Showroom dauerhaft auf technisch aktuellem Stand, ohne dass der Kunde eigene Technikkompetenz aufbauen muss."),
 ]),
 "references":order([
  ref("Porsche","Technische Produktion des Porsche-Panamera-Spots mit komplexer Licht- und Videotechnik – Beleg für Markeninszenierung auf höchstem visuellen Niveau."),
  ref("Telefónica","Event-IT und technische Gesamtproduktion für Telefónica-Kick-off und Hauptversammlung – Beleg für sichere, skalierbare Technikintegration."),
  ref("TEDx München","Ganzheitliche Veranstaltungstechnik für die TEDx-München-Konferenz – Licht, Ton, Video und Bühne aus einer Hand."),
 ]),
 "proof_points":order([
  pp("Eigener großer Lagerbestand in München für kurzfristige Projekte","LIMELIGHT verfügt über einen großen eigenen Gerätepark mit Lager in München und bietet Dry-Hire für Kollegen- und Partnerfirmen – so ist LIMELIGHT auch bei kurzfristigen und parallelen Messeprojekten lieferfähig."),
  pp("LED-Wände mit variablem Pixel-Pitch für nahtlose Standintegration","LIMELIGHT liefert hochauflösende LED-Wände in variablen Größen und Pixel-Pitches, die sich passgenau in Standarchitektur und Betrachtungsdistanz einfügen und mehrere Bildquellen gleichzeitig darstellen."),
  pp("Markeninszenierung auf Produktions-Niveau für Porsche","Für den Porsche-Panamera-Spot verantwortete LIMELIGHT die komplexe Licht- und Videotechnik – Beleg für die visuelle Qualität, die auch anspruchsvolle Messeauftritte verlangen."),
  pp("Sichere, skalierbare Event-IT bis 8.000+ Teilnehmer","LIMELIGHTs Event-IT deckt WLAN, Netzwerke und Zugangskontrolle unter höchsten Sicherheitsstandards ab und skaliert bis über 8.000 Teilnehmer – umgesetzt u. a. für Telefónica, relevant für Kongress- und Messeflächen."),
  pp("Termintreue Technik unter engen Auf- und Abbauzeiten","LIMELIGHT übernimmt Transport, Aufbau, Betrieb und Abbau während der Messelaufzeit mit eigenem Lager und Partnernetzwerk – ausgelegt auf die knappen Zeitfenster im Messebau."),
 ]),
}
json.dump(p29,open("p29.json","w"),ensure_ascii=False)
print("p30 personae",len(p30["personae"]),"| p29 personae",len(p29["personae"]))
