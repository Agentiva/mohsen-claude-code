#!/usr/bin/env python3
"""Build, per playbook, ONE comma-separated job-title line per country group.
Group A (Nordics+England): en, da, no, sv, fi, is
Group B (Eastern Europe+England): en, ru, bg, ro, pl, sk, cs, hu, et, lv, lt, sq, bcs, mk, sl
Core buying-center titles per language + playbook-specific English specialist titles.
"""
import os

CORE = {
"en":["Managing Director","CEO","General Manager","Owner","Founder","Plant Manager","Site Manager","Works Manager","Technical Director","Head of Technology","Technical Manager","Operations Manager","Production Manager","Head of Production","Maintenance Manager"],
"da":["Administrerende direktør","Adm. direktør","Ejer","Indehaver","Fabrikschef","Værkschef","Driftsleder","Teknisk direktør","Teknisk chef","Driftschef","Produktionschef","Produktionsleder","Vedligeholdelseschef"],
"no":["Administrerende direktør","Daglig leder","Eier","Gründer","Fabrikksjef","Verksleder","Driftsleder","Teknisk direktør","Teknisk sjef","Driftssjef","Produksjonssjef","Produksjonsleder","Vedlikeholdssjef"],
"sv":["Verkställande direktör","VD","Ägare","Grundare","Fabrikschef","Platschef","Anläggningschef","Teknisk direktör","Teknisk chef","Driftschef","Produktionschef","Produktionsledare","Underhållschef"],
"fi":["Toimitusjohtaja","Omistaja","Yrittäjä","Tehtaanjohtaja","Laitospäällikkö","Toimipaikan johtaja","Tekninen johtaja","Teknologiajohtaja","Käyttöpäällikkö","Tuotantojohtaja","Tuotantopäällikkö","Kunnossapitopäällikkö"],
"is":["Framkvæmdastjóri","Forstjóri","Eigandi","Verksmiðjustjóri","Stöðvarstjóri","Rekstrarstjóri","Tæknistjóri","Framleiðslustjóri","Viðhaldsstjóri"],
"ru":["Генеральный директор","Управляющий директор","Директор","Владелец","Собственник","Директор завода","Директор предприятия","Руководитель предприятия","Технический директор","Главный инженер","Директор по производству","Начальник производства","Операционный директор","Главный механик","Начальник технического обслуживания"],
"bg":["Управител","Изпълнителен директор","Генерален директор","Собственик","Директор на завод","Ръководител на завод","Мениджър на завода","Технически директор","Технически ръководител","Производствен директор","Ръководител производство","Мениджър операции","Ръководител поддръжка"],
"ro":["Director General","Administrator","Proprietar","Asociat","Director de fabrică","Șef de uzină","Manager de fabrică","Director Tehnic","Șef tehnic","Director de producție","Șef producție","Manager operațiuni","Șef mentenanță","Manager mentenanță"],
"pl":["Prezes Zarządu","Dyrektor Zarządzający","Dyrektor Generalny","Właściciel","Kierownik Zakładu","Dyrektor Zakładu","Kierownik Fabryki","Dyrektor Techniczny","Kierownik Techniczny","Kierownik Produkcji","Dyrektor Produkcji","Kierownik Operacyjny","Kierownik Utrzymania Ruchu"],
"sk":["Konateľ","Generálny riaditeľ","Výkonný riaditeľ","Majiteľ","Vlastník","Vedúci závodu","Riaditeľ závodu","Vedúci prevádzky","Technický riaditeľ","Technický vedúci","Vedúci výroby","Výrobný riaditeľ","Prevádzkový riaditeľ","Vedúci údržby"],
"cs":["Jednatel","Generální ředitel","Výkonný ředitel","Majitel","Vlastník","Vedoucí závodu","Ředitel závodu","Vedoucí provozu","Technický ředitel","Technický vedoucí","Vedoucí výroby","Výrobní ředitel","Provozní ředitel","Vedoucí údržby"],
"hu":["Ügyvezető igazgató","Ügyvezető","Vezérigazgató","Tulajdonos","Üzemvezető","Gyárigazgató","Telephelyvezető","Műszaki igazgató","Műszaki vezető","Termelésvezető","Gyártásvezető","Üzemeltetési vezető","Karbantartási vezető"],
"et":["Tegevjuht","Juhatuse esimees","Peadirektor","Omanik","Tehasejuht","Ettevõtte juht","Tehnikajuht","Tehniline direktor","Tootmisjuht","Operatsioonijuht","Hooldusjuht"],
"lv":["Valdes priekšsēdētājs","Izpilddirektors","Ģenerāldirektors","Īpašnieks","Rūpnīcas vadītājs","Ražotnes vadītājs","Tehniskais direktors","Tehniskais vadītājs","Ražošanas vadītājs","Operāciju vadītājs","Uzturēšanas vadītājs","Tehniskās apkopes vadītājs"],
"lt":["Generalinis direktorius","Vadovas","Direktorius","Savininkas","Gamyklos vadovas","Įmonės vadovas","Padalinio vadovas","Techninis direktorius","Technikos vadovas","Gamybos vadovas","Operacijų vadovas","Priežiūros vadovas","Techninės priežiūros vadovas"],
"sq":["Drejtor i Përgjithshëm","Administrator","Drejtor Ekzekutiv","Pronar","Menaxher i fabrikës","Drejtor fabrike","Menaxher i uzinës","Drejtor Teknik","Menaxher Teknik","Menaxher i Prodhimit","Drejtor prodhimi","Menaxher operacionesh","Menaxher i Mirëmbajtjes"],
"bcs":["Direktor","Generalni direktor","Izvršni direktor","Vlasnik","Direktor pogona","Rukovodilac pogona","Voditelj pogona","Direktor fabrike","Direktor tvornice","Tehnički direktor","Tehnički rukovodilac","Direktor proizvodnje","Rukovodilac proizvodnje","Voditelj proizvodnje","Menadžer operacija","Rukovodilac održavanja","Voditelj održavanja"],
"mk":["Генерален директор","Извршен директор","Управител","Сопственик","Директор на фабрика","Раководител на погон","Технички директор","Технички раководител","Директор на производство","Раководител на производство","Раководител на одржување"],
"sl":["Direktor","Generalni direktor","Izvršni direktor","Lastnik","Vodja obrata","Direktor obrata","Obratovodja","Tehnični direktor","Tehnični vodja","Vodja proizvodnje","Vodja operacij","Vodja vzdrževanja"],
}

GROUP_A = ["en","da","no","sv","fi","is"]                 # Nordics + England
GROUP_B = ["en","ru","bg","ro","pl","sk","cs","hu","et","lv","lt","sq","bcs","mk","sl"]  # Eastern Europe + England

# Playbook-specific specialist titles (English — commonly English-tagged on
# LinkedIn even in local markets; appended to both groups).
PB_EXTRA = {
"Private Recyclers & Reprocessors": ["Head of Recycling","Recycling Manager","Head of Processing","Plant Director"],
"Municipal & Public Waste Operators": ["Head of Waste Management","Waste Manager","Head of Environmental Services","Plant Director"],
"Cement, Energy & RDF Off-takers": ["Alternative Fuels Manager","Head of Alternative Fuels","Kiln Manager","Process Manager","Energy Manager","RDF Manager","Plant Director"],
"Wood & Biomass Recyclers": ["Head of Biomass","Biomass Manager","Sawmill Manager","Head of Wood Processing","Plant Director"],
}

def line(langs, extra):
    seen, out = set(), []
    for lg in langs:
        for t in CORE[lg]:
            k=t.lower()
            if k not in seen: seen.add(k); out.append(t)
    for t in extra:
        if t.lower() not in seen: seen.add(t.lower()); out.append(t)
    return ", ".join(out)

BASE=os.path.dirname(os.path.abspath(__file__))
lines=["# Lindner – Jobtitel pro Playbook x Laendergruppe (Clay Find People)",
"",
"Gruppe A = England, Dänemark, Norwegen, Schweden, Finnland, Island.",
"Gruppe B = Belarus, Bulgarien, Moldau, Polen, Rumänien, Slowakei, Tschechien, Ungarn, Estland, Lettland, Litauen, Albanien, Bosnien-H., Kosovo, Kroatien, Montenegro, Nordmazedonien, Serbien, Slowenien, England.",
"Kern-Titel identisch je Gruppe; pro Playbook zusätzlich Fachrollen (englisch). Jede Zeile copy-paste-fertig.",
""]
for pb, extra in PB_EXTRA.items():
    lines.append(f"## {pb}")
    lines.append("**Gruppe A — England + Nordics:**")
    lines.append("```")
    lines.append(line(GROUP_A, extra))
    lines.append("```")
    lines.append("**Gruppe B — England + Osteuropa:**")
    lines.append("```")
    lines.append(line(GROUP_B, extra))
    lines.append("```")
    lines.append("")

open(os.path.join(BASE,"find_people_titles_by_playbook.md"),"w",encoding="utf-8").write("\n".join(lines))
# also print counts
for pb,extra in PB_EXTRA.items():
    a=line(GROUP_A,extra).count(",")+1; b=line(GROUP_B,extra).count(",")+1
    print(f"{pb}: GroupA {a} titles | GroupB {b} titles")
