# BACKUP — IAR Group Playbooks 136, 132, 131

**Gezogen am:** 2026-09-07, unmittelbar vor dem Überschreiben durch die Europa-Fassungen
**Quelle:** Amplifa Org 34 „IAR Group" · https://app.amplifa.ai/admin/organizations/34
**Stand der Daten:** `updated_at` 2026-08-19T15:22 (alle drei Playbooks)

Dies ist der vollständige, wiederherstellbare Zustand der drei Playbooks vor der
Europa-Optimierung. Jeder Block liegt als JSON vor, exakt so, wie ihn die Amplifa-API
zurückgegeben hat.

---

## Wiederherstellung

Pro Playbook und Subsection ein Aufruf von `playbook_update`:

```
playbook_update(
  organization_name = "IAR Group",
  playbook_id       = <136 | 132 | 131>,
  subsection        = "<value_proposition | personae | use_cases | proof_points | audience | product.description>",
  value             = <der JSON-Block aus diesem Dokument>
)
```

Reihenfolge ist beliebig, die Subsections sind voneinander unabhängig. `references` war bei
allen drei Playbooks bereits leer (`[]`) und muss nicht zurückgesetzt werden.

Unveränderte Felder, die nicht angefasst wurden und daher kein Backup brauchen:
`product.name`, `product.metadata` (leer), `status` (`approved`), `language` (`en`),
`created_at`, `ai_generation_notes`.

---
---

# Playbook 136 — Precision Metal Forming

`status: approved` · `language: en` · `references: []`

## product.description

```json
"IAR Group delivers end-to-end industrial automation and robotics integration services, helping manufacturers modernize their production lines, increase throughput, and reduce operational costs. With deep expertise in robotics systems design, deployment, and support, IAR Group enables companies to accelerate their digital transformation and achieve measurable competitive advantages on the factory floor."
```

## value_proposition

```json
"IAR Group provides automated inline inspection and sorting for precision metal forming — progressive stamping, deep drawing, springs and wire forms — running at 200+ parts per minute with 100% inspection, automatic good/bad sorting and tray packing. Vision systems catch burrs, cracks, dimensional deviations and surface defects in real time, replacing manual gauging and costly third-party sorting, with full traceability for IATF 16949 / PPAP and typical ROI under 18 months. Built on the proprietary Modular Automation Platform (MAP) with US-based engineering and service from Huntley, IL (reference customer: Paragon Medical, progressive-stamped drug-delivery components). Ideal targets: North American stamping, deep-draw, spring and wire-form manufacturers supplying automotive and medical, 50–1,000 employees; buyers in Quality, Engineering, Manufacturing, Operations and Owner/President. Not a fit: heavy machinery or casting, distributors, and HR / Facilities / Maintenance roles."
```

## personae

```json
[
  {
    "id": "8f86d636-9ea1-41ed-b2dc-3b03170be01c",
    "name": "Engineering Director Edward",
    "order": 1,
    "title": "Director / VP of Engineering",
    "pain_points": [
      "Manual inspection cannot keep pace with high-speed progressive stamping presses running hundreds of parts per minute",
      "Difficulty integrating inline inspection technology into existing stamping, deep drawing, or spring forming lines without disrupting production",
      "Evaluating vision system capabilities for detecting burrs, cracks, dimensional deviations, and surface defects across diverse part geometries",
      "Need for a modular, scalable inspection platform that grows with expanding product portfolios and new part introductions",
      "Lack of vendor partners who truly understand metalworking processes and the unique challenges of formed metal parts"
    ]
  },
  {
    "id": "05d00a55-f683-4abe-95ee-29b2f4892a67",
    "name": "Quality Director Quinn",
    "order": 2,
    "title": "Director of Quality / QA Manager",
    "pain_points": [
      "Customer complaints and costly returns caused by undetected burrs, cracks, or dimensional non-conformances escaping to the field",
      "Automotive and medical customers demanding 100% inspection, full traceability, and compliance with IATF 16949 and PPAP requirements",
      "Excessive spending on third-party sorting services after quality escapes, eroding margins on high-volume contracts",
      "Retiring experienced QA inspectors with no qualified replacements available in a tight labor market",
      "Inability to provide real-time defect data and statistical process insights to drive continuous improvement"
    ]
  },
  {
    "id": "8252004c-bb33-4c9c-a7ec-2244cb0eaaa1",
    "name": "Plant Manager Patricia",
    "order": 3,
    "title": "Director of Manufacturing / Plant Manager",
    "pain_points": [
      "Production throughput constrained by manual inspection bottlenecks downstream of high-speed stamping or forming equipment",
      "Rising labor costs and chronic difficulty recruiting reliable operators for repetitive visual inspection tasks",
      "Unplanned line stoppages and scrap spikes when defects are detected too late in the production process",
      "Pressure to reduce cost-per-part while simultaneously meeting stricter customer quality requirements",
      "Coordinating quality containment activities that pull resources away from core production operations"
    ]
  },
  {
    "id": "01afbd66-c4c3-4824-82fa-ce7046d374c2",
    "name": "Operations Director Oliver",
    "order": 4,
    "title": "Director of Operations / Production Manager",
    "pain_points": [
      "Balancing increasing production volume demands with the need for consistent outgoing quality on every part",
      "High internal and external failure costs eating into operational margins across multiple product lines",
      "Lack of automated data collection making it difficult to identify root causes of recurring defect patterns",
      "Need to demonstrate clear, quantifiable ROI to secure capital expenditure approval from ownership",
      "Managing multiple quality processes across stamping, forming, and secondary operations without a unified inspection platform"
    ]
  },
  {
    "id": "0c1507ed-0a6c-4265-a30a-78a3a1e008b7",
    "name": "Owner-Operator Oscar",
    "order": 5,
    "title": "Owner / President (SME Decision-Maker)",
    "pain_points": [
      "Every capital investment must show clear payback — typically under 18 months — to justify the expenditure",
      "Customer retention at risk when quality escapes lead to chargebacks, sorting charges, or loss of preferred supplier status",
      "Dependence on a small number of experienced inspectors who are approaching retirement with no succession plan",
      "Competitive pressure from larger shops that already have automated inspection and can guarantee 100% outgoing quality",
      "Concern about working with automation vendors who lack hands-on understanding of metal stamping and forming environments"
    ]
  }
]
```

## use_cases

```json
[
  {
    "id": "3df856df-9b84-4dc4-b896-b5c3343b6088",
    "order": 1,
    "title": "Inline High-Speed Inspection for Progressive Stamping Lines",
    "description": "IAR Group's vision systems integrate directly into progressive stamping lines, inspecting every part at speeds exceeding 200 parts per minute without slowing production. The system detects burrs, cracks, dimensional deviations, and surface defects in real time, automatically sorting reject parts and ensuring only conforming parts proceed to packaging or next-stage operations. This eliminates the manual inspection bottleneck and delivers 100% outgoing quality assurance."
  },
  {
    "id": "75b3d5ab-63f5-4ef9-887a-5a5c723f7ebe",
    "order": 2,
    "title": "Automated Defect Detection and Sorting for Deep Drawn Metal Parts",
    "description": "For deep drawing operations producing complex geometries, IAR Group provides dimensional measurement and surface inspection of critical features immediately after forming. The system identifies wrinkles, thinning, cracks, and out-of-tolerance conditions, automatically diverting defective parts. This dramatically reduces customer complaints and eliminates the need for expensive third-party sorting services after quality escapes."
  },
  {
    "id": "b76dd654-27e2-4fa3-8306-297b72dcc033",
    "order": 3,
    "title": "100% Inspection and Traceability for Automotive and Medical Compliance",
    "description": "IAR Group's platform enables manufacturers to meet the stringent 100% inspection and full traceability requirements demanded by automotive (IATF 16949 / PPAP) and medical device customers. Every part is inspected, measured, and logged with complete data records, providing auditable quality documentation. This use case is proven with reference customer Paragon Medical for progressive stamped drug delivery device components."
  },
  {
    "id": "b0fce725-f3ad-4120-a07a-ccc267e0f5c6",
    "order": 4,
    "title": "Spring and Wire Form Inspection with Automatic Tray Packing",
    "description": "IAR Group delivers inspection systems tailored for compression, extension, and torsion springs as well as wire formed and fourslide/multi-slide parts. The system verifies critical dimensions, detects material defects, and performs automatic good/bad sorting with optional tray packing for direct shipment to customers. This replaces labor-intensive manual gauging and reduces both inspection costs and cycle time."
  },
  {
    "id": "b55603db-e9f2-4f1a-802a-c90a86b8400b",
    "order": 5,
    "title": "Replacing Third-Party Sorting Services with In-House Automated Inspection",
    "description": "Many metal forming companies spend heavily on external sorting services after quality incidents. IAR Group's automated inspection and sorting systems bring this capability in-house, eliminating recurring sorting fees and providing permanent, consistent quality control. With typical ROI under 18 months and local support from IAR Group's facility in Huntley, IL, this investment pays for itself quickly while strengthening customer confidence in outgoing quality."
  }
]
```

## proof_points

```json
[
  {
    "id": "pp-136-1",
    "claim": "200+ ppm inline inspection with auto sort & tray packing",
    "order": 1,
    "description": "Detects burrs, cracks, dimensional deviations and surface defects in real time on progressive stamping, deep drawing, springs and wire forms — replacing manual gauging and third-party sorting."
  },
  {
    "id": "pp-136-2",
    "claim": "Reference customer: Paragon Medical",
    "order": 2,
    "description": "Deployed for 100% inspection and full traceability on progressive-stamped drug-delivery components — meeting automotive (IATF 16949 / PPAP) and medical requirements."
  },
  {
    "id": "pp-136-3",
    "claim": "Typical ROI under 18 months, US-based support",
    "order": 3,
    "description": "In-house automated inspection eliminates recurring third-party sorting fees and chargebacks, with local service from IAR's Huntley, IL facility."
  }
]
```

## audience

```json
{
  "summary": "US precision metal forming manufacturers — progressive stamping, deep drawing, springs, wire forms, fourslide — supplying automotive and medical OEMs (target 50–1,000 employees; the smallest size bucket starts at 51). Buying center: Owner/President, Quality, Engineering, Manufacturing and Operations. Exclude heavy machinery/casting/foundry, distributors, and HR/Facilities/Maintenance roles.",
  "target_market_companies": "4.000",
  "target_market_contacts": "12.000",
  "markets": ["US"],
  "company_sizes": ["51_200", "201_1000"],
  "industries": ["Metal Stamping", "Precision Metal Forming", "Spring Manufacturing", "Wire Forming", "Deep Drawing", "Automotive Components"],
  "seniority_levels": ["c_level", "vp_head_of", "manager", "specialist"],
  "roles": ["President/Owner", "Director of Quality", "VP of Manufacturing", "Director of Operations", "Plant Manager", "Quality Manager", "Manufacturing Engineer"],
  "required_keywords": ["stamping", "deep drawing", "springs", "wire form", "metal forming", "IATF 16949"],
  "excluded_keywords": ["casting", "foundry", "heavy machinery", "distributor", "staffing", "service center"]
}
```

---
---

# Playbook 132 — Micro Molding

`status: approved` · `language: en` · `references: []`

## product.description

```json
"IAR Group delivers end-to-end industrial automation and robotics integration services, helping manufacturers and industrial enterprises modernize their production lines, improve operational efficiency, and reduce costs. By combining deep engineering expertise with cutting-edge robotic technologies, IAR Group enables companies to accelerate their digital transformation and achieve measurable productivity gains on the factory floor."
```

## value_proposition

```json
"IAR Group builds automated inspection systems for micro-molded parts — plastic micro-injection-molded and metal-injection-molded (MIM) components — that are too small to gauge reliably with calipers or micrometers. High-resolution vision plus dimensional metrology detects flash, short shots, sink marks, knit lines and gate vestiges and measures sub-millimeter features at full press speed, with automatic good/bad sorting, tray packing and FDA 21 CFR Part 11 / ISO 13485-validated traceability. On the proprietary Modular Automation Platform (MAP) with US-based engineering and service from Huntley, IL, micro molders reach 100% inline inspection, cut scrap, and close the documentation gaps that trigger audit findings. Ideal targets: US micro-molding and MIM manufacturers serving medical, surgical and precision-industrial markets, 30–800 employees; buyers in Quality, Engineering, R&D, Manufacturing and Plant Management. Not a fit: high-volume commodity or packaging molders, distributors, and HR / Facilities / Maintenance roles."
```

## personae

```json
[
  {
    "id": "7602e3b3-f010-49c0-af57-d5a67da9e9cf",
    "name": "Engineering Director Edward",
    "order": 1,
    "title": "Director / VP of Engineering",
    "pain_points": [
      "Micro-molded parts with sub-millimeter features and complex geometries are impossible to measure reliably with calipers, micrometers, or manual gauging methods, forcing reliance on sampling-based inspection that misses critical defects",
      "Evaluating and selecting the right automated inspection technology from a confusing landscape of vision system vendors is extremely difficult without deep expertise in micro-scale metrology, leading to costly mismatches between system capabilities and actual part inspection requirements",
      "Designing inspection processes that can handle high-mix production with frequent changeovers between different micro part geometries without extensive re-engineering or prolonged downtime for each new product introduction",
      "Integrating new vision-based inspection systems with existing molding cell automation, PLCs, and data infrastructure that were never designed to accommodate high-resolution imaging and dimensional measurement at micro scale",
      "Ensuring inspection system accuracy and repeatability meet the stringent Gage R&R requirements demanded by medical device OEM customers and regulatory auditors for sub-millimeter part features"
    ]
  },
  {
    "id": "eef6436a-49ce-4f74-95be-91af7b53723a",
    "name": "Quality Director Quincy",
    "order": 2,
    "title": "Director of Quality / Quality Assurance",
    "pain_points": [
      "FDA 21 CFR Part 820 and ISO 13485 compliance requires complete, traceable inspection documentation for every lot of micro-molded surgical tools and medical components, but manual inspection methods cannot generate the data integrity and audit trails regulators demand",
      "Optical defects specific to micro molding — flash, short shots, sink marks, knit lines, and gate vestiges — are invisible to the naked eye and undetectable with mechanical measurement tools, creating unacceptable quality escape risks to customers",
      "High-volume production of micro parts at tens of thousands of units per run makes 100% inspection with manual methods physically impossible, forcing reliance on statistical sampling that exposes the company to costly field failures, customer complaints, and potential recalls",
      "Recruiting and retaining qualified QA inspectors who can reliably perform microscopic visual inspection is increasingly difficult and expensive, and human fatigue and subjectivity introduce unacceptable variability in pass/fail decisions",
      "Customer and regulatory audit findings repeatedly flag insufficient inspection capability and documentation gaps for micro-scale parts, putting key contracts and certifications at risk"
    ]
  },
  {
    "id": "791d58f3-60a3-4126-8ab7-6233c0c474b7",
    "name": "Manufacturing Director Dana",
    "order": 3,
    "title": "Director of Manufacturing / Production",
    "pain_points": [
      "Scrap rates and rework costs for micro-molded parts are disproportionately high because defective parts are not detected until downstream assembly or final inspection, wasting expensive materials and machine time on components that should have been caught at the press",
      "Production throughput is constrained by manual inspection bottlenecks — operators cannot keep pace with high-speed micro molding cycles, creating backlogs and forcing either slower cycle times or reduced inspection coverage that increases defect escapes",
      "Lack of real-time, part-by-part inspection data from the molding process makes it impossible to quickly identify process drift, tooling wear, or parameter shifts, resulting in extended runs of out-of-spec parts before problems are discovered",
      "Pressure to reduce cost-per-part while simultaneously meeting tighter quality specifications from medical and precision industrial customers creates an impossible tradeoff without automated inspection and sorting capabilities",
      "Manual sorting of good and defective micro parts is error-prone and labor-intensive, and the inability to automatically separate and tray-pack inspected parts slows downstream assembly and packaging operations"
    ]
  },
  {
    "id": "146540ad-beda-4594-9d69-b9ead54fc682",
    "name": "R&D Director Rachel",
    "order": 4,
    "title": "Director of R&D / Product Development",
    "pain_points": [
      "New micro-molded product designs are becoming increasingly complex with tighter tolerances and smaller feature sizes, but existing inspection infrastructure cannot validate whether production is capable of meeting these new specifications at volume",
      "Transitioning new micro parts from prototyping to full production is delayed because the quality team lacks automated inspection methods to perform first article inspection, process validation, and capability studies on sub-millimeter features efficiently",
      "Customer OEMs are demanding measurement data and SPC documentation for critical dimensions on micro components as a condition of design approval, but current gauging methods lack the resolution and repeatability to provide credible data",
      "Evaluating alternative materials, gate locations, and mold designs for micro parts requires rapid, high-resolution dimensional feedback that manual measurement cannot deliver with the speed or accuracy needed for iterative development cycles",
      "Developing inspection criteria and pass/fail specifications for novel micro part geometries requires close collaboration with an inspection technology partner who understands both molding process variation and vision-based metrology capabilities"
    ]
  },
  {
    "id": "cd12be49-db44-4d88-96fb-af54ecfc781d",
    "name": "Plant Manager Patrick",
    "order": 5,
    "title": "Plant Manager / Operations Director",
    "pain_points": [
      "Overall equipment effectiveness (OEE) for micro molding cells is undermined by the disconnect between high-speed press output and slow, unreliable manual inspection, creating a bottleneck that limits the plant's ability to take on new business and grow revenue",
      "Finding, training, and retaining workers willing and able to perform tedious microscopic inspection tasks under magnification for extended shifts is a persistent staffing challenge that drives up labor costs and creates production continuity risks",
      "Capital expenditure requests for automated inspection systems require clear ROI justification in terms of scrap reduction, labor savings, throughput improvement, and risk mitigation, but the plant lacks baseline inspection data to build a compelling business case",
      "Regulatory audit readiness is a constant concern because the plant's current inspection documentation for micro parts relies on paper-based records and manual entries that are vulnerable to errors, omissions, and data integrity questions",
      "The plant needs a U.S.-based equipment partner with local service and support capabilities who can deliver fast response times for system maintenance, troubleshooting, and production line changes without depending on overseas support with long lead times"
    ]
  }
]
```

## use_cases

```json
[
  {
    "id": "c6fde2ee-88e4-4e03-8742-4abceac7d109",
    "order": 1,
    "title": "Automated 100% Inspection for Micro Injection Molded Plastic Parts",
    "description": "IAR Group deploys high-resolution vision-based inspection systems directly integrated into micro injection molding production cells to perform 100% inline inspection of every plastic micro part at full production speed. The system simultaneously detects optical defects — flash, short shots, sink marks, and surface anomalies — while performing dimensional measurement of critical features down to sub-millimeter tolerances. Automatic good/bad sorting and tray packing are integrated, eliminating manual handling and ensuring only conforming parts proceed to downstream assembly or shipment, dramatically reducing scrap costs and customer quality escapes."
  },
  {
    "id": "24755324-4285-4796-bc52-78c2192813e8",
    "order": 2,
    "title": "Precision Inspection and Sorting for Metal Injection Molded (MIM) Components",
    "description": "Metal injection molded parts such as miniature gears for robotic surgery, micro tool blanks, and small motor housings require post-sintering dimensional verification and surface defect detection that mechanical gauges cannot reliably perform at volume. IAR Group's inspection platform combines 360-degree imaging with precision dimensional metrology to inspect MIM parts for dimensional conformance, surface porosity, cracks, and geometric distortion in a single automated cycle. Integrated sorting ensures only parts meeting specification are forwarded, while comprehensive inspection data is captured and stored for full traceability."
  },
  {
    "id": "c6fde123-92b0-464f-a877-2d0a20b432c4",
    "order": 3,
    "title": "FDA and ISO 13485 Compliant Inspection for Surgical Micro Tools and Medical Micro Components",
    "description": "Manufacturers of surgical micro instruments and medical micro components face stringent regulatory requirements for inspection documentation, data integrity, and process validation under FDA 21 CFR Part 820 and ISO 13485. IAR Group delivers inspection systems designed and validated for these regulated environments, providing tamper-proof electronic records, complete part-by-part traceability, statistical process control (SPC) reporting, and audit-ready documentation. This ensures manufacturers maintain continuous compliance, pass regulatory audits with confidence, and protect their ability to supply medical device OEM customers."
  },
  {
    "id": "c44df122-e589-4331-b3da-88408e3f7456",
    "order": 4,
    "title": "High-Mix Micro Part Inspection with Rapid Changeover Capability",
    "description": "Micro molding companies serving diverse markets often run dozens of different part numbers across multiple presses with frequent changeovers, making rigid, single-purpose inspection setups impractical. IAR Group's flexible inspection platform supports rapid recipe changes and product switchovers with minimal downtime, enabling high-mix manufacturers to maintain automated 100% inspection across their full product portfolio. Quick-change fixturing, stored inspection programs, and adaptive vision algorithms allow the system to accommodate a wide range of micro part geometries, materials, and tolerance requirements without re-engineering."
  },
  {
    "id": "85699c0b-570a-4c78-bcce-8b48dff4af3e",
    "order": 5,
    "title": "Inspection System Feasibility Study, ROI Analysis, and Validation Roadmap for Micro Molding Operations",
    "description": "Before investing in automated micro part inspection, manufacturers need rigorous clarity on which parts and processes will benefit most, what ROI to expect, and how the system will be validated for regulatory compliance. IAR Group conducts comprehensive feasibility assessments including part measurability studies, defect characterization, throughput modeling, and detailed ROI projections covering scrap reduction, labor savings, and risk mitigation. The engagement delivers a phased implementation roadmap with capital budget estimates, IQ/OQ/PQ validation plans, and technology recommendations tailored to the manufacturer's specific micro molding environment and regulatory requirements."
  }
]
```

## proof_points

```json
[
  {
    "id": "pp-132-1",
    "claim": "Measures what calipers can't",
    "order": 1,
    "description": "Sub-millimeter vision metrology with Gage R&R suited to micro features, giving OEMs and auditors credible dimensional data on parts that mechanical gauging cannot reliably measure."
  },
  {
    "id": "pp-132-2",
    "claim": "Catches micro-molding-specific defects at full speed",
    "order": 2,
    "description": "Detects flash, short shots, sink marks, knit lines and gate vestiges inline, with automatic sorting and tray packing that removes manual handling of tiny parts."
  },
  {
    "id": "pp-132-3",
    "claim": "FDA 21 CFR Part 11 / ISO 13485-validated traceability",
    "order": 3,
    "description": "Part-by-part electronic records and audit-ready documentation, supported locally from IAR's US site in Huntley, IL."
  }
]
```

## audience

```json
{
  "summary": "US micro-molding and metal-injection-molding (MIM) manufacturers making sub-millimeter plastic and metal parts for medical, surgical and precision-industrial markets (target 30–800 employees; smallest size bucket starts at 51, so include 30–50-employee shops via keywords). Buying center: Quality, Engineering, R&D, Manufacturing and Plant Management. Exclude high-volume commodity/packaging molders, distributors, and HR/Facilities roles.",
  "target_market_companies": "2.000",
  "target_market_contacts": "7.000",
  "markets": ["US"],
  "company_sizes": ["51_200", "201_1000"],
  "industries": ["Micro Molding", "Injection Molding", "Metal Injection Molding (MIM)", "Medical Device Manufacturing", "Precision Plastics"],
  "seniority_levels": ["c_level", "vp_head_of", "manager", "specialist"],
  "roles": ["Director of Engineering", "Director of Quality", "Director of Manufacturing", "R&D Director", "Plant Manager", "Quality Manager"],
  "required_keywords": ["micro molding", "injection molding", "MIM", "medical", "ISO 13485"],
  "excluded_keywords": ["packaging molder", "commodity molding", "distributor", "staffing"]
}
```

---
---

# Playbook 131 — Electrification & Precision Components

`status: approved` · `language: en` · `references: []`

## product.description

```json
"IAR Group delivers end-to-end industrial automation and robotics solutions that help manufacturers increase production efficiency, reduce operational costs, and modernize their factory floors. By combining deep engineering expertise with cutting-edge robotic systems, IAR Group enables industrial companies to achieve higher throughput, improved quality, and a faster return on their automation investments."
```

## value_proposition

```json
"IAR Group delivers turnkey high-speed inspection for electrified precision components — stamped contacts, terminals, interconnects, connectors and EV busbars — performing 100% inline visual and dimensional inspection at 200+ parts per minute with 2.5 µm repeatability, integrated directly at the progressive-stamping press exit with full per-part traceability into MES/ERP. Combined with assembly automation and tray packing on the proprietary Modular Automation Platform (MAP) and US-based engineering and service from Huntley, IL, it removes the manual-inspection bottleneck that caps line speed and secures EV-program and OEM (IATF 16949) compliance. Ideal targets: North American metal-stamping and connector/terminal manufacturers supplying automotive/EV and electronics, 50–1,000 employees; buyers in Quality, Engineering, Manufacturing and Operations. Not a fit: pure electronics OEMs without in-house stamping, distributors, defense-services primes, and HR / Facilities / Maintenance roles."
```

## personae

```json
[
  {
    "id": "026a92ed-36c7-42b4-8bc2-9f791fe246b2",
    "name": "Engineering Director Eduardo",
    "order": 1,
    "title": "Director / VP of Engineering",
    "pain_points": [
      "Current inspection systems cannot keep pace with progressive stamping lines running 120+ parts per minute, creating a throughput bottleneck that delays shipments of stamped contacts, terminals, and interconnects",
      "EV connector and terminal tolerances below ±125 µm demand micron-level measurement repeatability that legacy vision systems and manual gauging cannot consistently deliver across high-volume production",
      "The internal team lacks the combined high-speed vision, dimensional measurement, controls, and mechanical integration expertise needed to deploy inline 100% inspection without heavy reliance on outside resources",
      "Integrating inspection, assembly automation, and tray packing into existing progressive-stamping lines requires a turnkey partner who understands the full process chain from die exit to packed tray"
    ]
  },
  {
    "id": "2c6c464a-e3d0-49d2-98ad-69a6f5ba61f4",
    "name": "Quality Director Quinn",
    "order": 2,
    "title": "Director / VP of Quality Assurance",
    "pain_points": [
      "OEM customers mandate 100% visual and dimensional inspection on every stamped contact, terminal, and connector—failure to comply triggers containment actions, chargebacks, and potential loss of business",
      "Chronic shortage of skilled inspectors forces reliance on sampling plans that increase defect escape risk, especially on precision interconnects and EV battery contacts with tight dimensional tolerances",
      "Manual inspection introduces operator-dependent variability that undermines SPC data integrity and continuous improvement efforts",
      "Lack of complete part-level traceability data—including dimensional measurements, pass/fail status, and lot linkage—creates gaps that cause IATF 16949 audit findings and slow root-cause investigations"
    ]
  },
  {
    "id": "e618bd38-8408-45b0-b63f-c0188e808fae",
    "name": "Manufacturing Director Maria",
    "order": 3,
    "title": "Director of Manufacturing / Production",
    "pain_points": [
      "Downstream inspection and sorting—not the press—is the true line constraint above 120 parts per minute, preventing full utilization of existing stamping capacity",
      "Legacy inspection equipment requires excessive changeover time between connector and terminal variants, eroding OEE on shorter EV program runs",
      "Labor shortages on second and third shifts force a choice between reduced throughput and higher escape risk on high-precision stamped components",
      "Manual handling between inspection, assembly, and tray packing adds cycle time, increases damage risk on delicate contacts and interconnects, and consumes valuable floor space"
    ]
  },
  {
    "id": "bcd02185-aa11-4d4b-b09a-9461fdaf0f9e",
    "name": "Plant Manager Patrick",
    "order": 4,
    "title": "Director of Operations / Plant Manager",
    "pain_points": [
      "Relentless OEM cost-per-part pressure on electrified components demands automation of inspection, assembly, and packing to protect margins",
      "Aging inspection equipment causes unplanned downtime that cascades across the stamping line, triggering missed deliveries and expedited freight costs",
      "Lack of real-time part-level quality data delays detection of tooling wear and process drift, allowing defective stamped contacts and terminals to accumulate before anyone reacts",
      "Capital investment in new EV programs must scale with actual demand—rigid, monolithic inspection systems create financial risk when volumes ramp unpredictably"
    ]
  }
]
```

## use_cases

```json
[
  {
    "id": "2678707b-a44c-4b32-9b08-9637542c8464",
    "order": 1,
    "title": "High-Speed Inline 100% Visual & Dimensional Inspection",
    "description": "Deploy IAR Group's turnkey inspection systems directly at the progressive-stamping press exit to perform 100% visual and dimensional inspection of every stamped contact, terminal, interconnect, and connector at over 200 parts per minute with 2.5-micron repeatability. Non-conforming parts are rejected in real time, eliminating manual inspection bottlenecks and drastically reducing customer PPM defect rates."
  },
  {
    "id": "b6165824-d53c-4e50-b229-89e522be7b60",
    "order": 2,
    "title": "Integrated Inspection, Assembly Automation & Tray Packing",
    "description": "Combine high-speed inspection, assembly automation, and precision tray packing into a single integrated cell connected directly to your existing progressive-stamping line. This eliminates manual handling between process steps, reduces floor space, lowers labor dependency, and ensures every shipped EV busbar, battery contact, or connector is fully inspected, assembled, and traceable from die exit to packed tray."
  },
  {
    "id": "ab54da9c-559c-47d6-b049-ca5a9adb07f9",
    "order": 3,
    "title": "Complete Part-Level Traceability for Audit-Ready Quality Documentation",
    "description": "Automatically capture dimensional measurements, visual inspection results, pass/fail status, and lot data for every individual stamped part. Each inspected component receives full traceability records that integrate directly with MES/ERP systems, closing documentation gaps that cause IATF 16949 audit findings and enabling rapid root-cause investigations when quality events occur."
  },
  {
    "id": "9759bcd2-1117-4f7a-8b25-39d5f9b49f31",
    "order": 4,
    "title": "Unlocking Full Press Throughput on Electrified Precision Components",
    "description": "Replace manual or semi-automated inspection stations that cap your stamping line at a fraction of rated press speed. IAR Group's automated 200+ ppm inspection systems unlock existing press capacity for contacts, terminals, and interconnects without purchasing additional stamping equipment—delivering a significant capacity increase at a fraction of the cost of new presses."
  },
  {
    "id": "1232e031-b1d4-4d74-9cf9-9de1dc9d71cd",
    "order": 5,
    "title": "Modular Scale-Up for EV Program Launches",
    "description": "Start with a single inspection module for pilot runs of new electrified connector or terminal programs and add inspection, assembly, and tray-packing capacity on the same platform as volumes ramp—no re-engineering or re-qualification required. Capital spend stays aligned with actual OEM demand, reducing financial risk on new EV programs while maintaining 2.5-micron repeatability and full traceability from day one."
  }
]
```

## proof_points

```json
[
  {
    "id": "pp-131-1",
    "claim": "200+ ppm at 2.5 µm repeatability",
    "order": 1,
    "description": "100% inline visual and dimensional inspection directly at the progressive-stamping press exit, with no manual handling of delicate contacts and interconnects."
  },
  {
    "id": "pp-131-2",
    "claim": "Integrated inspection + assembly + tray packing (MAP)",
    "order": 2,
    "description": "A single cell from die exit to packed tray on the Modular Automation Platform, with complete per-part traceability into MES/ERP for gap-free IATF 16949 documentation."
  },
  {
    "id": "pp-131-3",
    "claim": "US-based engineering & service from Huntley, IL",
    "order": 3,
    "description": "Local North American commissioning and support that plugs into existing progressive-stamping lines without long overseas lead times."
  }
]
```

## audience

```json
{
  "summary": "US manufacturers of stamped electrical/electronic precision components — contacts, terminals, interconnects, connectors, EV busbars — running high-speed progressive stamping (target 50–1,000 employees). Buying center: Quality, Engineering, Manufacturing and Operations. Exclude pure electronics OEMs without in-house stamping, distributors, defense-services primes, and HR/Facilities/Maintenance roles.",
  "target_market_companies": "2.500",
  "target_market_contacts": "9.000",
  "markets": ["US"],
  "company_sizes": ["51_200", "201_1000"],
  "industries": ["Metal Stamping", "Electrical & Electronic Connectors", "EV Components", "Precision Metal Manufacturing", "Automotive Components"],
  "seniority_levels": ["c_level", "vp_head_of", "manager", "specialist"],
  "roles": ["Director of Quality", "VP of Engineering", "Director of Manufacturing", "Plant Manager", "Director of Operations", "Quality Manager", "Manufacturing Engineer"],
  "required_keywords": ["stamping", "connectors", "terminals", "progressive die", "EV", "busbar"],
  "excluded_keywords": ["distributor", "reseller", "staffing", "facilities management", "electronics OEM only"]
}
```
