# -*- coding: utf-8 -*-
from docx import Document
from docx.shared import Pt, RGBColor, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

INK = RGBColor(0x0A, 0x0A, 0x0F)
GRN = RGBColor(0x1F, 0x8A, 0x5B)
MUT = RGBColor(0x6B, 0x6B, 0x75)

doc = Document()

# Base style
st = doc.styles['Normal']
st.font.name = 'Calibri'
st.font.size = Pt(11)
st.paragraph_format.space_after = Pt(6)
st.paragraph_format.line_spacing = 1.15

def shade(par, hexfill):
    pPr = par._p.get_or_add_pPr()
    shd = OxmlElement('w:shd')
    shd.set(qn('w:val'), 'clear'); shd.set(qn('w:color'), 'auto'); shd.set(qn('w:fill'), hexfill)
    pPr.append(shd)

def title(text):
    p = doc.add_paragraph()
    r = p.add_run(text); r.bold = True; r.font.size = Pt(24); r.font.color.rgb = INK
    p.space_after = Pt(4)
    return p

def subtitle(text):
    p = doc.add_paragraph()
    r = p.add_run(text); r.font.size = Pt(12); r.font.color.rgb = MUT
    return p

def block_header(text):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(14)
    r = p.add_run('  ' + text + '  ')
    r.bold = True; r.font.size = Pt(13); r.font.color.rgb = RGBColor(0xFF,0xFF,0xFF)
    shade(p, '0A0A0F')
    return p

def h_field(label):
    p = doc.add_paragraph()
    r = p.add_run(label); r.bold = True; r.font.size = Pt(11); r.font.color.rgb = GRN
    return p

def para(text, italic=False, color=None, size=11, bold=False):
    p = doc.add_paragraph()
    r = p.add_run(text); r.italic = italic; r.bold = bold; r.font.size = Pt(size)
    if color: r.font.color.rgb = color
    return p

def persona(name, titles, pains):
    p = doc.add_paragraph(); r = p.add_run(name); r.bold = True; r.font.size = Pt(13)
    p.paragraph_format.space_before = Pt(8)
    para(titles, italic=True, color=MUT)
    hp = doc.add_paragraph(); rr = hp.add_run('Pain Points:'); rr.bold = True
    for b in pains:
        bp = doc.add_paragraph(b, style='List Bullet'); bp.paragraph_format.space_after = Pt(2)

def named(titletext, body):
    p = doc.add_paragraph(); r = p.add_run(titletext); r.bold = True; r.font.size = Pt(12)
    p.paragraph_format.space_before = Pt(8); p.paragraph_format.space_after = Pt(2)
    para(body)

# ============ COVER / HEADER ============
title('Playbook: 360°-Video-Booth für Messen & Brand Activation')
subtitle('360°PhotoBoothMieten (Threesixtymedia) · Kampagnen-Playbook · Sprache: de · erstellt von amplifa')
note = doc.add_paragraph()
nr = note.add_run('Hinweis: Kein Onboarding-/Kickoff-Call in Fathom auffindbar – Inhalte sind aus Website-Recherche + '
                  'Market-Intelligence-Report belegt; Unbelegtes ist mit „(zu verifizieren)" markiert und im Kickoff zu bestätigen.')
nr.italic = True; nr.font.size = Pt(9.5); nr.font.color.rgb = MUT

# ============ BLOCK 1 ============
block_header('Block 1 — Product Description')
para('360°PhotoBoothMieten (Marke „360° Company", rechtlich Threesixtymedia) ist ein inhabergeführter Spezialist für die '
     'Vermietung von 360°-Video-Booths mit Sitz in Stolberg (Rheinland/NRW). Anders als klassische Fotobox-Anbieter '
     'positioniert sich das Unternehmen bewusst B2B: als Partner für strategische Markenaktivierung und teilbaren, gebrandeten '
     'User-Generated-Content auf Messen, Roadshows, Corporate Events und am Point of Sale. Inhaber ist Youssef Ismail; die genaue '
     'Mitarbeiterzahl wird auf der Website nicht genannt – gearbeitet wird projektbasiert mit Event-Assistenten vor Ort. Die '
     'Website ist zweisprachig (DE/EN) und richtet sich primär an den deutschsprachigen Raum mit Schwerpunkt West-DACH.')
para('Kernleistung ist die schlüsselfertige Vermietung eines 360°-Video-Booths inklusive Plattform für bis zu 5 Personen '
     'gleichzeitig, professioneller Kamera mit 120 fps, gebrandeten Videoclips von bis zu 25 Sekunden, sofortigem Download per '
     'QR-Code, Live-Gadgets (z. B. Konfetti, Bubbles), Event-Assistent sowie Auf- und Abbau. Der Booth wird im Corporate Design '
     'des Kunden gebrandet – von Logo über Farben bis zur Botschaft – sodass jedes Video zu teilbarem Marken-Content wird. '
     'Ergänzend bietet das Unternehmen professionelle Event-Foto- und -Videografie als „visuelles Kapital" für PR, Social Media '
     'und künftige Kampagnen sowie (zu verifizieren) DSGVO-konforme Lead-/Kontaktdatenerfassung am Booth.')
para('Im Markt differenziert sich 360°PhotoBoothMieten über die konsequente Ausrichtung auf messbares Live-Marketing statt '
     'austauschbaren „Fotospaß". Während der Großteil der DACH-Wettbewerber im preisgetriebenen Consumer-/Hochzeitssegment '
     '(449–800 €) konkurriert, verkauft das Unternehmen den Booth als Werkzeug für Standfrequenz, Verweildauer, Social-Reichweite '
     'und Leadgenerierung – also für Marketing-Wirkung mit Wow-Effekt. Genau das trifft den steigenden ROI-Druck auf Live-Budgets '
     'und den Bedarf an nativem, teilbarem Video-Content.')
p = doc.add_paragraph(); r = p.add_run('INDUSTRY: '); r.bold = True
p.add_run('Messe- & Eventservice, Live-Marketing, Brand Activation, Experiential Marketing, Eventagenturen, Veranstaltungstechnik')
p = doc.add_paragraph(); r = p.add_run('USPs: '); r.bold = True
p.add_run('1. 360°-Video-Booth schlüsselfertig inklusive Personal, Auf-/Abbau und Anfahrt – ein Ansprechpartner, kein '
          'Organisationsaufwand. 2. Vollständiges Branding im Corporate Design des Kunden für konsistenten Markenauftritt auf '
          'jedem Clip. 3. Bis zu 5 Personen gleichzeitig, 120 fps und Clips bis 25 Sekunden für hochwertige, dynamische '
          'Aufnahmen. 4. Sofortiger Download per QR-Code – Gäste teilen den gebrandeten Content selbst und sofort auf Social '
          'Media. 5. Live-Gadgets (Konfetti, Bubbles u. a.) inklusive für zusätzlichen Wow- und Aufmerksamkeitseffekt. '
          '6. Konsequente B2B-Ausrichtung auf Markenaktivierung und UGC statt reiner Hochzeits-Fotobox. 7. Optionale '
          'Event-Foto-/Videografie als zusätzliches visuelles Kapital für PR und Marketing. 8. (zu verifizieren) DSGVO-konforme '
          'Datenerfassung am Booth für messbare Leadgenerierung.')

# ============ BLOCK 2 ============
block_header('Block 2 — Value Proposition')
para('360°PhotoBoothMieten verwandelt Messestände und Events in eine Social-Bühne: mehr Besucherfrequenz und Verweildauer am '
     'Stand, teilbarer gebrandeter Video-Content und – richtig aufgesetzt – qualifizierte Leads. Statt eines austauschbaren '
     'Gimmicks erhalten Marken und Aussteller ein schlüsselfertiges Live-Marketing-Werkzeug inklusive Personal, das messbare '
     'Aufmerksamkeit und Reichweite erzeugt, ohne dass das eigene Team Aufwand oder Risiko trägt.')

# ============ BLOCK 3 ============
block_header('Block 3 — Target Personas (5)')
persona('Eventmanagerin Lena',
        'Eventmanager, Messeverantwortlicher, Trade-Fair Manager, Live-Communication Manager, Projektleiter Events',
        ['Sie muss dafür sorgen, dass der Messestand aus der Masse heraussticht und Besucher anzieht – die Standfläche ist teuer und darf nicht leer wirken.',
         'Sie steht unter Druck, die Verweildauer am Stand und die Zahl der Standkontakte messbar zu erhöhen.',
         'Sie braucht eine Attraktion, die reibungslos läuft, ohne dass sie sich am Eventtag noch um Technik und Auf-/Abbau kümmern muss.',
         'Sie will dem Management nach der Messe belegbare Ergebnisse zeigen, nicht nur „war ein schöner Stand".',
         'Sie sucht nach etwas Neuem jenseits der klassischen Fotobox, die viele Stände schon hatten.'])
persona('Brand-Manager Daniel',
        'Marketing Manager, Brand Manager, Brand-Activation Manager, Head of Marketing, Marketingleiter',
        ['Er muss sein Live-/Eventbudget gegenüber der Geschäftsführung mit messbarer Wirkung (Reichweite, Leads) rechtfertigen.',
         'Er braucht laufend frischen, teilbaren Video-Content für Social Media, ohne jedes Mal eine teure Produktion aufzusetzen.',
         'Er will, dass jede Aktivierung konsequent im Corporate Design auftritt und die Markenbotschaft transportiert.',
         'Er sucht Aktivierungsformate, die Aufmerksamkeit erzeugen und gleichzeitig Daten/Leads für den Vertrieb liefern.',
         'Er steht unter Druck, mit begrenztem Budget mehr Marken-Wirkung pro Event herauszuholen.'])
persona('Agentur-Producer Mark',
        'Projektleiter Live-Kommunikation, Producer, Account Director Eventagentur, Senior Projektmanager Brand Experience',
        ['Er muss für seine Markenkunden verlässliche Subdienstleister finden, die Qualität und Timing zu 100 % halten.',
         'Er trägt das Risiko, wenn ein Modul am Eventtag nicht funktioniert – ein Ausfall fällt direkt auf die Agentur zurück.',
         'Er braucht Partner, die white-label-fähig sind und sich nahtlos ins CI seiner Kunden einfügen.',
         'Er will Module, die er kalkulierbar wiederverwenden und über mehrere Kundenprojekte hinweg einsetzen kann.',
         'Er muss bei Pitches mit innovativen, social-tauglichen Formaten überzeugen, ohne alles selbst aufzubauen.'])
persona('Social-Media-Managerin Jana',
        'Social Media Manager, Content Manager, Online-Marketing Manager, Content Creator',
        ['Sie braucht eine konstante Pipeline an authentischem, vertikalem Video-Content für Instagram, TikTok & Co.',
         'Sie will, dass Besucher selbst Content erstellen und teilen, statt alles selbst produzieren zu müssen.',
         'Sie steht unter Druck, Reichweite und Engagement rund um Events nachzuweisen.',
         'Sie benötigt Material, das sofort verfügbar ist – nicht erst Wochen nach dem Event nach langer Postproduktion.'])
persona('Geschäftsführer Stefan (KMU-Aussteller)',
        'Geschäftsführer, Inhaber, Vertriebsleiter (kleinerer Aussteller), Geschäftsführender Gesellschafter',
        ['Er muss mit begrenztem Messebudget einen Auftritt hinbekommen, der gegen größere Wettbewerber besteht.',
         'Er will einen klaren Kosten-Nutzen-Effekt und einen Ansprechpartner, der alles übernimmt.',
         'Er braucht eine Außenwirkung, die seinen Stand modern und attraktiv erscheinen lässt.',
         'Er hat keine Marketingabteilung, die sich um zusätzliche Technik und Logistik kümmern kann.'])

# ============ BLOCK 4 ============
block_header('Block 4 — Use Cases (6)')
named('Standmagnet auf der Leitmesse',
      'Aussteller zahlen viel für Standfläche, kämpfen aber darum, Besucher anzuziehen und länger zu halten. '
      '360°PhotoBoothMieten stellt einen im CI gebrandeten 360°-Video-Booth schlüsselfertig auf den Stand – inklusive Personal, '
      'Auf- und Abbau. Das Ergebnis ist spürbar höhere Standfrequenz, längere Verweildauer und Gesprächsanlässe, weil Besucher '
      'anstehen, um ihren eigenen gebrandeten Clip aufzunehmen und sofort zu teilen.')
named('DSGVO-konforme Leadgenerierung am Messestand',
      'Marketing- und Vertriebsverantwortliche brauchen aus teuren Messeauftritten verwertbare Leads, nicht nur Sichtkontakte. '
      'Der Booth lässt sich (zu verifizieren) mit einer Opt-in-Datenerfassung kombinieren, sodass Besucher ihren Clip gegen '
      'Hinterlassen ihrer Kontaktdaten erhalten. So entsteht aus der Attraktion eine messbare, DSGVO-konforme Liste interessierter '
      'Kontakte, die das Live-Budget belegbar rechtfertigt.')
named('Roadshow & Produktlaunch mit reproduzierbarem Marken-Content',
      'Bei Roadshows und Launches muss dieselbe Markeninszenierung über mehrere Termine hinweg verlässlich funktionieren. '
      '360°PhotoBoothMieten liefert ein standardisiertes, gebrandetes Booth-Setup, das an jedem Stopp identisch hochwertige '
      '360°-Clips produziert. Das Ergebnis ist ein konsistenter Markenauftritt und ein wiederverwendbarer Strom an teilbarem '
      'Content über die gesamte Tour.')
named('White-Label-Modul für Eventagenturen',
      'Eventagenturen brauchen verlässliche, CI-treue Module für ihre Markenkunden, ohne eigene Technik vorzuhalten. '
      '360°PhotoBoothMieten agiert als white-label-fähiger Subdienstleister mit termintreuer Umsetzung und Personal vor Ort. Die '
      'Agentur kann das 360°-Modul kalkulierbar in Pitches und Projekten einsetzen und trägt deutlich weniger Umsetzungsrisiko.')
named('Pop-up- und Point-of-Sale-Aktivierung im Retail',
      'Handels- und Konsumgütermarken wollen an Pop-up-Flächen und am PoS Aufmerksamkeit erzeugen und Laufkundschaft in '
      'Markenkontakte verwandeln. Der 360°-Video-Booth wird im Markendesign aufgebaut und lädt Passanten ein, sich filmen zu '
      'lassen und den gebrandeten Clip sofort zu teilen. Das Ergebnis ist erhöhte Standzeit am PoS, organische Social-Reichweite '
      'und ein modernes, erlebbares Markenbild direkt am Verkaufsort.')
named('Corporate Event mit Social-Reichweite und Wow-Effekt',
      'Bei Firmenfeiern, Mitarbeiter- und Kundenevents soll ein bleibender Eindruck entstehen und gleichzeitig teilbarer Content '
      'für die Außenwirkung produziert werden. 360°PhotoBoothMieten bringt den Booth schlüsselfertig inklusive Event-Assistent und '
      'Live-Gadgets mit. Gäste werden zu Akteuren ihrer eigenen gebrandeten Clips, was Stimmung erzeugt und dem Unternehmen sofort '
      'verfügbares Video-Material für Social Media und Employer Branding liefert.')

# ============ BLOCK 5 ============
block_header('Block 5 — Reference Customers (zu verifizieren)')
para('(zu verifizieren – aus Onboarding ergänzen) Auf der Website und in öffentlich recherchierbaren Quellen ließen sich keine '
     'belegten, namentlich nennbaren Referenzkunden mit Kundenstimme identifizieren. Im Kickoff 2–3 nennbare Referenzprojekte mit '
     'Marke, Eventtyp, Ansprechpartner und – idealerweise – Kennzahlen (z. B. Anzahl erstellter Clips, Reichweite, generierte '
     'Leads) sowie Logo-/Case-Freigabe einsammeln. Bis dahin Block leer lassen, nicht erfinden.', italic=True, color=MUT)

# ============ BLOCK 6 ============
block_header('Block 6 — Proof Points (6)')
named('Bis zu 5 Personen, 120 fps und Clips bis 25 Sekunden',
      'Die technische Ausstattung ist auf der Website ausgewiesen: Die Plattform fasst bis zu fünf Personen gleichzeitig, die '
      'Kamera nimmt mit 120 fps auf und erzeugt Videos von bis zu 25 Sekunden Länge – Grundlage für hochwertige, dynamische '
      '360°-Clips statt einfacher Schnappschüsse.')
named('Vollständiges Branding im Corporate Design des Kunden',
      'Laut Eigenbeschreibung wird der 360°-Video-Booth individuell auf das Corporate Design abgestimmt – von Logo über Farben bis '
      'zur Botschaft. Jeder erzeugte Clip transportiert damit konsistent die Marke des Kunden auf Events, Messen und in Social Media.')
named('Schlüsselfertig inklusive Personal, Auf-/Abbau und Anfahrt',
      'Das Angebot umfasst einen persönlichen Event-Assistenten vor Ort sowie Auf- und Abbau; die Anfahrt wird deutschlandweit '
      'beworben. Der Kunde muss sich am Eventtag um nichts kümmern – ein zentrales Argument für reibungslose Messe- und Eventeinsätze.')
named('Sofortiges Teilen per QR-Code für organische Reichweite',
      'Aufnahmen stehen unmittelbar per QR-Code zum Download bereit, sodass Gäste ihren gebrandeten Clip direkt auf Instagram, '
      'TikTok & Co. teilen. Aus jeder Aufnahme wird so potenziell organische, markengetriebene Social-Reichweite.')
named('Konsequente B2B-Positionierung als Brand-Activation-Tool',
      '360°PhotoBoothMieten beschreibt sich selbst als Anbieter strategischer Markenaktivierung und branded User-Generated-Content '
      'für Messen, Roadshows, Corporate Events und Point of Sale – und grenzt sich damit klar vom austauschbaren '
      'Consumer-/Hochzeits-Fotoboxmarkt ab.')
named('Marktrückenwind für Live-Marketing und UGC',
      'Der Bedarf ist strukturell belegt: Experiential Marketing macht rund 28–35 % der Marketingbudgets aus, 97 % der '
      'B2B-Marketer halten Vor-Ort-Events für maßgeblich, und die deutsche Messewirtschaft zählte 2025 rund 190.000 Aussteller auf '
      '304 Messen (AUMA). Ein 360°-Booth bedient genau die Nachfrage nach aufmerksamkeitsstarken, social-tauglichen Aktivierungen.')

out = '/home/user/mohsen-claude-code/reports/360photoboothmieten/360PhotoBoothMieten Playbook.docx'
doc.save(out)
print('saved', out)
