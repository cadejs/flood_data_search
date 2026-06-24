# Twenty-Country Flood Data Readiness Review

This document is generated from verified, versioned JSON artifacts. Do not edit it directly.

> **Dataset-resolved links.** A source is confirmed only when the authoritative flood dataset is identifiable and usable through a working service, download, viewer, map document, or dataset-specific page. Generic portals and agency homepages are retained only as investigation leads. This report describes what exists and how usable it is; it does not assign an overall readiness grade.

## How to use this report

Every country section has the same shape. Work through it top to bottom:

1. **What we have** — a snapshot of how many sources have confirmed dataset access, how many are leads, and which flood-hazard families (fluvial, coastal, surface water) are actually confirmed.
2. **Source tables**, which sort every candidate into three tiers:
   - **Confirmed dataset access** — the link reaches a usable flood dataset (service, API, download, viewer, map document, or dataset page). Start here.
   - **Reachable investigation leads** — the link works but lands on a generic portal, catalogue, or ambiguous/restricted product; the dataset still has to be located by hand.
   - **Unavailable candidates** — the link did not resolve (shown as non-clickable text).
3. **Access column** — distinguishes machine-readable endpoints (Service / API / Direct download) from things that need a person (Interactive viewer, Map document, Dataset page).
4. **Portal search guide** — website roots plus the exact native-language search terms to paste into each portal to turn a lead into a confirmed source.
5. **What comes next** — the concrete actions still outstanding for that country.

**Evaluating a source further.** When you open a candidate, judge it on the same factors used throughout:

- **Geographic completeness** — national, or only some regions?
- **Scenario richness** — multiple return periods (e.g., 10 / 100 / 500-year) and depth/velocity, or a single layer?
- **Technical accessibility** — a service or download you can pull, or a viewer you can only look at?
- **Documentation currency** — when was it last updated?
- **Licensing** — is reuse permitted? Many licences are still marked "verify".
- **Integration effort** — format, coordinate system, and language barriers to actually using it.

## Country overview

One row per country. The hazard columns show whether a **confirmed** dataset exists for each family (confirmed / unconfirmed / none); "unconfirmed" means a candidate exists but its dataset is not yet confirmed. "Needs review" counts material sources that are not yet confirmed (leads plus broken links). Provisional pilots cover only the top five regions and are flagged in each country section.

| Country | Fluvial | Coastal | Surface water | Confirmed sources | Leads | Needs review | Coverage model |
|---|---|---|---|---:|---:|---:|---|
| Brazil * | unconfirmed | unconfirmed | unconfirmed | 0 | 5 | 8 | mixed national and regional |
| India * | confirmed | unconfirmed | confirmed | 2 | 2 | 6 | mixed national and regional |
| Germany * | confirmed | confirmed | confirmed | 7 | 2 | 2 | national catalogue with regional publishers |
| China * | unconfirmed | unconfirmed | confirmed | 1 | 5 | 7 | primarily regional |
| Canada * | confirmed | confirmed | confirmed | 3 | 1 | 4 | national catalogue with regional publishers |
| France * | confirmed | confirmed | unconfirmed | 2 | 2 | 6 | national catalogue with regional publishers |
| Mexico * | confirmed | unconfirmed | confirmed | 1 | 4 | 7 | mixed national and regional |
| Malaysia * | unconfirmed | unconfirmed | unconfirmed | 0 | 5 | 8 | mixed national and regional |
| Poland | confirmed | confirmed | none | 3 | 2 | 1 | nationally unified |
| Japan * | confirmed | confirmed | confirmed | 4 | 0 | 4 | national catalogue with regional publishers |
| Belgium | confirmed | confirmed | confirmed | 3 | 2 | 3 | primarily regional |
| Italy * | confirmed | confirmed | unconfirmed | 3 | 1 | 5 | national catalogue with regional publishers |
| Switzerland * | confirmed | none | confirmed | 2 | 4 | 5 | national catalogue with regional publishers |
| Ireland | confirmed | confirmed | confirmed | 4 | 2 | 1 | nationally unified |
| Thailand * | unconfirmed | unconfirmed | unconfirmed | 0 | 3 | 8 | mixed national and regional |
| Sweden | confirmed | confirmed | confirmed | 4 | 0 | 1 | nationally unified |
| Austria | confirmed | none | confirmed | 4 | 1 | 0 | nationally unified |
| United Arab Emirates * | unconfirmed | unconfirmed | unconfirmed | 0 | 3 | 6 | primarily regional |
| South Africa * | unconfirmed | unconfirmed | unconfirmed | 0 | 6 | 8 | mixed national and regional |
| Republic of Korea | confirmed | unconfirmed | confirmed | 1 | 3 | 4 | nationally unified |

\* Provisional — coverage assessed on a top-five-region pilot.

## Link coverage and caveats

Across the 20 countries, **154 candidate sources** were audited: **44 have confirmed dataset access**, **53 are reachable investigation leads**, and **57 are unavailable** (including 17 confirmed HTTP 404s). Confirmed access includes **1 service/API/download endpoint(s)** and **43 usable viewers, map documents, or dataset-specific pages**.

## Brazil (BR)

**Coverage model:** mixed national and regional · **Scope:** provisional — top-five-region pilot · **Confidence in completeness:** low

ANA/SNIRH and SGB provide national flood-vulnerability, risk-sector and monitoring entry points, while detailed hazard mapping is commonly published through state environmental and water geoportals. The top-five-state pilot therefore combines national candidates with São Paulo, Minas Gerais, Rio de Janeiro, Bahia and Paraná portals.

### What we have

- **Confirmed dataset access:** 0 source(s) (0 direct service/API/download, 0 viewer / map document / dataset page).
- **Investigation leads:** 5 reachable portal(s) that still need the dataset located by hand.
- **Unavailable:** 4 broken or unreachable candidate(s).
- **Hazard families confirmed:** none. **Not yet confirmed:** Fluvial (river), Coastal, Surface water (pluvial).
- **Best confirmed access:** No confirmed dataset access.


### Population-priority regions

| Rank | Region | Population | Year | Source |
|---:|---|---:|---:|---|
| 1 | São Paulo | 44,411,238 | 2022 | [IBGE Censo Demográfico 2022](https://censo2022.ibge.gov.br/panorama/) |
| 2 | Minas Gerais | 20,539,989 | 2022 | [IBGE Censo Demográfico 2022](https://censo2022.ibge.gov.br/panorama/) |
| 3 | Rio de Janeiro | 16,055,174 | 2022 | [IBGE Censo Demográfico 2022](https://censo2022.ibge.gov.br/panorama/) |
| 4 | Bahia | 14,141,626 | 2022 | [IBGE Censo Demográfico 2022](https://censo2022.ibge.gov.br/panorama/) |
| 5 | Paraná | 11,444,380 | 2022 | [IBGE Censo Demográfico 2022](https://censo2022.ibge.gov.br/panorama/) |

**Deferred regions:** Acre, Alagoas, Amapá, Amazonas, Ceará, Distrito Federal, Espírito Santo, Goiás, Maranhão, Mato Grosso, Mato Grosso do Sul, Pará, Paraíba, Pernambuco, Piauí, Rio Grande do Norte, Rio Grande do Sul, Rondônia, Roraima, Santa Catarina, Sergipe, Tocantins

### Portal search guide and website roots

Use the exact dataset names in the directory first. If that fails, try the local-language flood terms below in the site's search box, map-layer catalogue, or metadata search. Website-root links are navigation aids; they are not themselves confirmation that a dataset is available.

**Portal languages:** Portuguese

**Country search phrases:** `mapa de inundação` · `perigo de inundação` · `mancha de inundação` · `profundidade` · `velocidade` · `tempo de retorno` · `inundação costeira` · `cota de inundação litoral` · `coastal flood hazard` · `mapa de risco costeiro`

**Native-language term guide:** `mapa de inundação` — flood / inundation map · `perigo de inundação` — flood hazard · `mancha de inundação` — inundation extent · `profundidade` — depth · `velocidade` — velocity · `tempo de retorno` — return period · `inundação costeira` — coastal flooding · `cota de inundação litoral` — coastal flood elevation · `mapa de risco costeiro` — coastal risk map. Paste the native term into the portal; the English text is only a meaning guide.

| Website root | Related source IDs | Publisher(s) | Search this site for | Link roles | Current classification |
|---|---|---|---|---|---|
| [censo2022.ibge.gov.br](https://censo2022.ibge.gov.br/) | population: São Paulo, population: Minas Gerais, population: Rio de Janeiro, population: Bahia, population: Paraná | IBGE Censo Demográfico 2022 | `São Paulo population`<br>`Minas Gerais population`<br>`Rio de Janeiro population`<br>`Bahia population`<br>`Paraná population` | population source | supporting citation |
| [data.jrc.ec.europa.eu](https://data.jrc.ec.europa.eu/) | BR-JRC-001 | European Commission Joint Research Centre | `Global River Flood Hazard Maps` | primary, verification final, selected access | investigation lead |
| [datageo.ambiente.sp.gov.br](https://datageo.ambiente.sp.gov.br/) | BR-SP-001, BR-SP-002 | Secretaria de Meio Ambiente, Infraestrutura e Logística / DataGEO; Instituto de Pesquisas Ambientais (IPA) / SEMIL - DataGEO | `DataGEO - Áreas de risco e inundação`<br>`Mapa de Risco de Erosão Costeira Crônica e Inundação Costeira - Orla Oceânica de São Paulo` | primary, verification final, selected access, service | investigation lead |
| [geobahia.inema.ba.gov.br](https://geobahia.inema.ba.gov.br/) | BR-BA-001 | Instituto do Meio Ambiente e Recursos Hídricos (INEMA) | `GeoBahia` | primary | unavailable candidate |
| [geoportal.inea.rj.gov.br](https://geoportal.inea.rj.gov.br/) | BR-RJ-001 | Instituto Estadual do Ambiente (INEA) | `GeoINEA - Risco de Inundação` | primary | unavailable candidate |
| [geoportal.meioambiente.mg.gov.br](https://geoportal.meioambiente.mg.gov.br/) | BR-MG-001 | SEMAD / IDE-Sisema | `IDE-Sisema - Inundação e áreas de risco` | verification final, selected access | investigation lead |
| [geoportal.sgb.gov.br](https://geoportal.sgb.gov.br/) | BR-SGB-001 | Serviço Geológico do Brasil (SGB/CPRM) | `GeoSGB / Cartografia de Risco Geológico` | primary, verification final, selected access | investigation lead |
| [idesisema.meioambiente.mg.gov.br](https://idesisema.meioambiente.mg.gov.br/) | BR-MG-001 | SEMAD / IDE-Sisema | `IDE-Sisema - Inundação e áreas de risco` | primary | investigation lead |
| [www.geopr.pr.gov.br](https://www.geopr.pr.gov.br/) | BR-PR-001 | Governo do Paraná / GeoPR | `GeoPR - Dados geoespaciais de risco e inundação` | primary | unavailable candidate |
| [www.snirh.gov.br](https://www.snirh.gov.br/) | BR-ANA-001 | Agência Nacional de Águas e Saneamento Básico (ANA) | `Atlas de Vulnerabilidade a Inundações` | primary, verification final | unavailable candidate |

### Confirmed dataset access

Each clickable link below was confirmed to identify an authoritative flood dataset and provide a usable service, download, viewer, map document, or dataset-specific page.

| ID | Jurisdiction / agency | Dataset | Confirmed flood type | Confirmed scenarios | Confirmed coverage | Confirmed formats | Confirmed licence | Access | Link | Verified | Flags | Evidence |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| _none_ | — | — | — | — | — | — | — | — | — | — | — | — |

### Reachable investigation leads

These links resolve, but they are generic portals, catalogue searches, restricted/request-only paths, ambiguous products, or otherwise lack confirmed dataset-specific access. They are clickable for investigation but excluded from scoring.

| ID | Jurisdiction / agency | Candidate | Access | Link | Reason | Tracking |
|---|---|---|---|---|---|---|
| BR-SGB-001 | National<br>Serviço Geológico do Brasil (SGB/CPRM) | GeoSGB / Cartografia de Risco Geológico | Generic portal | [Open](https://geoportal.sgb.gov.br/portal/home/) | The link is a generic agency or geoportal entry point; the named dataset was not resolved. | human review |
| BR-SP-001 | São Paulo<br>Secretaria de Meio Ambiente, Infraestrutura e Logística / DataGEO | DataGEO - Áreas de risco e inundação | Catalogue search | [Open](https://datageo.ambiente.sp.gov.br/) | The link is a catalogue/search entry point rather than a dataset-specific record. | human review |
| BR-MG-001 | Minas Gerais<br>SEMAD / IDE-Sisema | IDE-Sisema - Inundação e áreas de risco | Catalogue search | [Open](https://geoportal.meioambiente.mg.gov.br/) | The link is a catalogue/search entry point rather than a dataset-specific record. | human review |
| BR-JRC-001 | National fallback<br>European Commission Joint Research Centre | Global River Flood Hazard Maps | Restricted | [Open](https://data.jrc.ec.europa.eu/collection/id-0054) | The JRC collection resolves to a login surface; unauthenticated dataset access was not confirmed. | non-material candidate |
| BR-SP-002 | São Paulo<br>Instituto de Pesquisas Ambientais (IPA) / SEMIL - DataGEO | Mapa de Risco de Erosão Costeira Crônica e Inundação Costeira - Orla Oceânica de São Paulo | Service (OGC) | [Open](https://datageo.ambiente.sp.gov.br/geoserver/datageo/ows?SERVICE=WMS&REQUEST=GetCapabilities) | service exposes no recognizably flood-related layers | human review |

### Unavailable candidates

These links did not resolve. URLs are plain text and non-clickable.

| ID | Jurisdiction / agency | Candidate | Status | Candidate URL | Tracking |
|---|---|---|---|---|---|
| BR-ANA-001 | National<br>Agência Nacional de Águas e Saneamento Básico (ANA) | Atlas de Vulnerabilidade a Inundações | failed (HTTP 404): No candidate link resolved successfully during the strict audit. | `https://www.snirh.gov.br/portal/snirh/snirh-1/atlas-de-vulnerabilidade-a-inundacoes` | human review |
| BR-RJ-001 | Rio de Janeiro<br>Instituto Estadual do Ambiente (INEA) | GeoINEA - Risco de Inundação | failed (unreachable): No candidate link resolved successfully during the strict audit. | `https://geoportal.inea.rj.gov.br/portal/apps/sites/#/geoinea` | human review |
| BR-BA-001 | Bahia<br>Instituto do Meio Ambiente e Recursos Hídricos (INEMA) | GeoBahia | failed (unreachable): No candidate link resolved successfully during the strict audit. | `https://geobahia.inema.ba.gov.br/` | human review |
| BR-PR-001 | Paraná<br>Governo do Paraná / GeoPR | GeoPR - Dados geoespaciais de risco e inundação | failed (unreachable): No candidate link resolved successfully during the strict audit. | `https://www.geopr.pr.gov.br/` | human review |

### What comes next

1. Confirm Fluvial (river), Coastal, Surface water (pluvial) coverage — a candidate exists but its dataset is not yet confirmed.
2. Work the 5 investigation lead(s): use the portal search guide below to locate the dataset behind each portal, then confirm a usable service, download, viewer, or dataset page.
3. Resolve 4 broken or unreachable material source(s) flagged for human review (see the Unavailable table and the Human review required section).
4. Extend beyond the 5-region pilot to the 22 deferred region(s).

## India (IN)

**Coverage model:** mixed national and regional · **Scope:** provisional — top-five-region pilot · **Confidence in completeness:** medium

National remote-sensing and water-information systems expose flood inundation, hazard-atlas and forecasting products, but authoritative static hazard coverage is assembled unevenly by state and event. The pilot covers Uttar Pradesh, Maharashtra, Bihar, West Bengal and Madhya Pradesh.

### What we have

- **Confirmed dataset access:** 2 source(s) (0 direct service/API/download, 2 viewer / map document / dataset page).
- **Investigation leads:** 2 reachable portal(s) that still need the dataset located by hand.
- **Unavailable:** 5 broken or unreachable candidate(s).
- **Hazard families confirmed:** Fluvial (river), Surface water (pluvial). **Not yet confirmed:** Coastal.
- **Best confirmed access:** Interactive viewer, Dataset page.


### Population-priority regions

| Rank | Region | Population | Year | Source |
|---:|---|---:|---:|---|
| 1 | Uttar Pradesh | 199,812,341 | 2011 | [Census of India 2011](https://censusindia.gov.in/census.website/data/census-tables) |
| 2 | Maharashtra | 112,374,333 | 2011 | [Census of India 2011](https://censusindia.gov.in/census.website/data/census-tables) |
| 3 | Bihar | 104,099,452 | 2011 | [Census of India 2011](https://censusindia.gov.in/census.website/data/census-tables) |
| 4 | West Bengal | 91,276,115 | 2011 | [Census of India 2011](https://censusindia.gov.in/census.website/data/census-tables) |
| 5 | Madhya Pradesh | 72,626,809 | 2011 | [Census of India 2011](https://censusindia.gov.in/census.website/data/census-tables) |

**Deferred regions:** Andhra Pradesh, Arunachal Pradesh, Assam, Chhattisgarh, Goa, Gujarat, Haryana, Himachal Pradesh, Jharkhand, Karnataka, Kerala, Manipur, Meghalaya, Mizoram, Nagaland, Odisha, Punjab, Rajasthan, Sikkim, Tamil Nadu, Telangana, Tripura, Uttarakhand, Union territories

### Portal search guide and website roots

Use the exact dataset names in the directory first. If that fails, try the local-language flood terms below in the site's search box, map-layer catalogue, or metadata search. Website-root links are navigation aids; they are not themselves confirmation that a dataset is available.

**Portal languages:** Hindi, English

**Country search phrases:** `flood hazard map` · `inundation map` · `flood depth` · `flood velocity` · `return period` · `बाढ़ मानचित्र` · `बाढ़ जोखिम`

**Native-language term guide:** `बाढ़ मानचित्र` — flood map · `बाढ़ जोखिम` — flood risk. Paste the native term into the portal; the English text is only a meaning guide.

| Website root | Related source IDs | Publisher(s) | Search this site for | Link roles | Current classification |
|---|---|---|---|---|---|
| [aff.india-water.gov.in](https://aff.india-water.gov.in/) | IN-CWC-001 | Central Water Commission | `भारत बाढ़ पूर्वानुमान / Flood Forecasting Portal` | primary | unavailable candidate |
| [bhuvan-app1.nrsc.gov.in](https://bhuvan-app1.nrsc.gov.in/) | IN-NRSC-001 | National Remote Sensing Centre / ISRO | `Bhuvan Disaster Services - Flood` | primary, verification final, selected access | confirmed dataset access |
| [censusindia.gov.in](https://censusindia.gov.in/) | population: Uttar Pradesh, population: Maharashtra, population: Bihar, population: West Bengal, population: Madhya Pradesh | Census of India 2011 | `Uttar Pradesh population`<br>`Maharashtra population`<br>`Bihar population`<br>`West Bengal population`<br>`Madhya Pradesh population` | population source | supporting citation |
| [data.jrc.ec.europa.eu](https://data.jrc.ec.europa.eu/) | IN-JRC-001 | European Commission Joint Research Centre | `Global River Flood Hazard Maps` | primary, verification final, selected access | investigation lead |
| [indiawris.gov.in](https://indiawris.gov.in/) | IN-WRIS-001 | National Water Informatics Centre | `India-WRIS` | primary | unavailable candidate |
| [mpwrd.gov.in](https://mpwrd.gov.in/) | IN-MP-001 | Water Resources Department, Madhya Pradesh | `Water Resources GIS and Flood Studies` | primary | unavailable candidate |
| [sdma.maharashtra.gov.in](https://sdma.maharashtra.gov.in/) | IN-MH-001 | Maharashtra State Disaster Management Authority | `Maharashtra Flood Hazard and Risk Resources` | primary, verification final, selected access | investigation lead |
| [upsdma.up.nic.in](https://upsdma.up.nic.in/) | IN-UP-001 | Uttar Pradesh State Disaster Management Authority | `उत्तर प्रदेश बाढ़ जोखिम / Flood Hazard Resources` | primary | unavailable candidate |
| [wbiwd.gov.in](https://wbiwd.gov.in/) | IN-WB-001 | Irrigation & Waterways Department, West Bengal | `Flood Management and GIS Resources` | primary | unavailable candidate |
| [www.fmiscwrdbihar.gov.in](https://www.fmiscwrdbihar.gov.in/) | IN-BR-001 | Water Resources Department, Bihar / FMIS | `Flood Management Information System` | primary, verification final, selected access | confirmed dataset access |

### Confirmed dataset access

Each clickable link below was confirmed to identify an authoritative flood dataset and provide a usable service, download, viewer, map document, or dataset-specific page.

| ID | Jurisdiction / agency | Dataset | Confirmed flood type | Confirmed scenarios | Confirmed coverage | Confirmed formats | Confirmed licence | Access | Link | Verified | Flags | Evidence |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| IN-BR-001 | Bihar<br>Water Resources Department, Bihar / FMIS | Flood Management Information System<br>_Bihar Flood Management Information System_ | fluvial | unknown | Bihar | Dataset-specific page | unknown | Dataset page | [Primary](https://www.fmiscwrdbihar.gov.in/) | 2026-06-24 | verified | Official dataset-specific page or viewer confirmed during bounded page review. |
| IN-NRSC-001 | National<br>National Remote Sensing Centre / ISRO | Bhuvan Disaster Services - Flood<br>_Bhuvan Flood Disaster Services_ | fluvial, surface_water | unknown | India; event and project dependent | Interactive viewer | unknown | Interactive viewer | [Primary](https://bhuvan-app1.nrsc.gov.in/disaster/disaster.php) | 2026-06-24 | verified | Official dataset-specific page or viewer confirmed during bounded page review. |

### Reachable investigation leads

These links resolve, but they are generic portals, catalogue searches, restricted/request-only paths, ambiguous products, or otherwise lack confirmed dataset-specific access. They are clickable for investigation but excluded from scoring.

| ID | Jurisdiction / agency | Candidate | Access | Link | Reason | Tracking |
|---|---|---|---|---|---|---|
| IN-MH-001 | Maharashtra<br>Maharashtra State Disaster Management Authority | Maharashtra Flood Hazard and Risk Resources | Generic portal | [Open](https://sdma.maharashtra.gov.in/) | The link is a generic agency or geoportal entry point; the named dataset was not resolved. | human review |
| IN-JRC-001 | National fallback<br>European Commission Joint Research Centre | Global River Flood Hazard Maps | Restricted | [Open](https://data.jrc.ec.europa.eu/collection/id-0054) | The JRC collection resolves to a login surface; unauthenticated dataset access was not confirmed. | non-material candidate |

### Unavailable candidates

These links did not resolve. URLs are plain text and non-clickable.

| ID | Jurisdiction / agency | Candidate | Status | Candidate URL | Tracking |
|---|---|---|---|---|---|
| IN-CWC-001 | National<br>Central Water Commission | भारत बाढ़ पूर्वानुमान / Flood Forecasting Portal | failed (unreachable): No candidate link resolved successfully during the strict audit. | `https://aff.india-water.gov.in/` | human review |
| IN-WRIS-001 | National<br>National Water Informatics Centre | India-WRIS | failed (unreachable): No candidate link resolved successfully during the strict audit. | `https://indiawris.gov.in/wris/` | human review |
| IN-UP-001 | Uttar Pradesh<br>Uttar Pradesh State Disaster Management Authority | उत्तर प्रदेश बाढ़ जोखिम / Flood Hazard Resources | failed (unreachable): No candidate link resolved successfully during the strict audit. | `https://upsdma.up.nic.in/` | human review |
| IN-WB-001 | West Bengal<br>Irrigation & Waterways Department, West Bengal | Flood Management and GIS Resources | failed (unreachable): No candidate link resolved successfully during the strict audit. | `https://wbiwd.gov.in/` | human review |
| IN-MP-001 | Madhya Pradesh<br>Water Resources Department, Madhya Pradesh | Water Resources GIS and Flood Studies | failed (unreachable): No candidate link resolved successfully during the strict audit. | `https://mpwrd.gov.in/` | human review |

### What comes next

1. Confirm Coastal coverage — a candidate exists but its dataset is not yet confirmed.
2. Work the 2 investigation lead(s): use the portal search guide below to locate the dataset behind each portal, then confirm a usable service, download, viewer, or dataset page.
3. Resolve 5 broken or unreachable material source(s) flagged for human review (see the Unavailable table and the Human review required section).
4. Extend beyond the 5-region pilot to the 24 deferred region(s).
5. Confirm licensing for 2 confirmed source(s) whose licence is still marked "verify".

## Germany (DE)

**Coverage model:** national catalogue with regional publishers · **Scope:** provisional — top-five-region pilot · **Confidence in completeness:** high

Floods Directive products are coordinated nationally through WasserBLIcK/BfG, while authoritative high-resolution hazard and risk maps are published by the Länder. The pilot includes Nordrhein-Westfalen, Bayern, Baden-Württemberg, Niedersachsen and Hessen.

### What we have

- **Confirmed dataset access:** 7 source(s) (1 direct service/API/download, 6 viewer / map document / dataset page).
- **Investigation leads:** 2 reachable portal(s) that still need the dataset located by hand.
- **Unavailable:** 0 broken or unreachable candidate(s).
- **Hazard families confirmed:** Fluvial (river), Coastal, Surface water (pluvial).
- **Best confirmed access:** Dataset page, Interactive viewer, Service (OGC).


### Population-priority regions

| Rank | Region | Population | Year | Source |
|---:|---|---:|---:|---|
| 1 | Nordrhein-Westfalen | 18,034,600 | 2024 | [Destatis population by Länder](https://www.destatis.de/EN/Themes/Society-Environment/Population/Current-Population/Tables/population-by-laender.html) |
| 2 | Bayern | 13,248,928 | 2024 | [Destatis population by Länder](https://www.destatis.de/EN/Themes/Society-Environment/Population/Current-Population/Tables/population-by-laender.html) |
| 3 | Baden-Württemberg | 11,246,000 | 2024 | [Destatis population by Länder](https://www.destatis.de/EN/Themes/Society-Environment/Population/Current-Population/Tables/population-by-laender.html) |
| 4 | Niedersachsen | 8,005,000 | 2024 | [Destatis population by Länder](https://www.destatis.de/EN/Themes/Society-Environment/Population/Current-Population/Tables/population-by-laender.html) |
| 5 | Hessen | 6,280,000 | 2024 | [Destatis population by Länder](https://www.destatis.de/EN/Themes/Society-Environment/Population/Current-Population/Tables/population-by-laender.html) |

**Deferred regions:** Berlin, Brandenburg, Bremen, Hamburg, Mecklenburg-Vorpommern, Rheinland-Pfalz, Saarland, Sachsen, Sachsen-Anhalt, Schleswig-Holstein, Thüringen

### Portal search guide and website roots

Use the exact dataset names in the directory first. If that fails, try the local-language flood terms below in the site's search box, map-layer catalogue, or metadata search. Website-root links are navigation aids; they are not themselves confirmation that a dataset is available.

**Portal languages:** German

**Country search phrases:** `Hochwassergefahrenkarte` · `Überschwemmungsgebiet` · `Überflutungstiefe` · `Fließgeschwindigkeit` · `Wiederkehrintervall` · `Starkregengefahrenkarte` · `Starkregen Hinweiskarte` · `urban pluvial flood map` · `Oberflächenwasser Überflutung`

**Native-language term guide:** `Hochwassergefahrenkarte` — flood-hazard map · `Überschwemmungsgebiet` — flood / inundation zone · `Überflutungstiefe` — inundation depth · `Fließgeschwindigkeit` — flow velocity · `Wiederkehrintervall` — return interval · `Starkregengefahrenkarte` — heavy-rain hazard map · `Starkregen Hinweiskarte` — heavy-rain advisory map · `Oberflächenwasser Überflutung` — surface-water flooding. Paste the native term into the portal; the English text is only a meaning guide.

| Website root | Related source IDs | Publisher(s) | Search this site for | Link roles | Current classification |
|---|---|---|---|---|---|
| [geoportal.bafg.de](https://geoportal.bafg.de/) | DE-BFG-001 | Bundesanstalt für Gewässerkunde (BfG) | `Geoportal der BfG` | primary, verification final, selected access | investigation lead |
| [hochwasser.hessen.de](https://hochwasser.hessen.de/) | DE-HE-001 | Hessisches Landesamt für Naturschutz, Umwelt und Geologie | `Hochwasserrisikomanagement Hessen` | verification final, selected access | confirmed dataset access |
| [sgx.geodatenzentrum.de](https://sgx.geodatenzentrum.de/) | DE-BKG-001 | Bundesamt für Kartographie und Geodäsie (BKG) | `Hinweiskarte Starkregengefahren` | service, verification final, selected access | confirmed dataset access |
| [udo.lubw.baden-wuerttemberg.de](https://udo.lubw.baden-wuerttemberg.de/) | DE-BW-001 | Landesanstalt für Umwelt Baden-Württemberg | `Hochwassergefahrenkarten (UDO)` | primary, verification final, selected access | confirmed dataset access |
| [water.europa.eu](https://water.europa.eu/) | DE-EEA-001 | European Environment Agency | `WISE Floods Directive` | primary, verification final, selected access | confirmed dataset access |
| [www.bkg.bund.de](https://www.bkg.bund.de/) | DE-BKG-001 | Bundesamt für Kartographie und Geodäsie (BKG) | `Hinweiskarte Starkregengefahren` | primary | confirmed dataset access |
| [www.destatis.de](https://www.destatis.de/) | population: Nordrhein-Westfalen, population: Bayern, population: Baden-Württemberg, population: Niedersachsen, population: Hessen | Destatis population by Länder | `Nordrhein-Westfalen population`<br>`Bayern population`<br>`Baden-Württemberg population`<br>`Niedersachsen population`<br>`Hessen population` | population source | supporting citation |
| [www.flussgebiete.nrw.de](https://www.flussgebiete.nrw.de/) | DE-NW-001 | Ministerium für Umwelt, Naturschutz und Verkehr NRW | `Hochwassergefahrenkarten und Hochwasserrisikokarten` | primary, verification final, selected access | confirmed dataset access |
| [www.hochwasser-hessen.de](https://www.hochwasser-hessen.de/) | DE-HE-001 | Hessisches Landesamt für Naturschutz, Umwelt und Geologie | `Hochwasserrisikomanagement Hessen` | primary | confirmed dataset access |
| [www.umweltatlas.bayern.de](https://www.umweltatlas.bayern.de/) | DE-BY-001 | Bayerisches Landesamt für Umwelt | `UmweltAtlas Bayern - Naturgefahren Hochwasser` | primary, verification final, selected access | confirmed dataset access |
| [www.umweltkarten-niedersachsen.de](https://www.umweltkarten-niedersachsen.de/) | DE-NI-001 | Niedersächsischer Landesbetrieb für Wasserwirtschaft, Küsten- und Naturschutz | `Umweltkarten Niedersachsen - Hochwasser` | primary, verification final, selected access | investigation lead |
| [www.wasserblick.net](https://www.wasserblick.net/) | DE-WBL-001 | Bund/Länder-Arbeitsgemeinschaft Wasser / WasserBLIcK | `Hochwassergefahren- und Hochwasserrisikokarten` | primary, verification final, selected access | confirmed dataset access |

### Confirmed dataset access

Each clickable link below was confirmed to identify an authoritative flood dataset and provide a usable service, download, viewer, map document, or dataset-specific page.

| ID | Jurisdiction / agency | Dataset | Confirmed flood type | Confirmed scenarios | Confirmed coverage | Confirmed formats | Confirmed licence | Access | Link | Verified | Flags | Evidence |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| DE-BKG-001 | National<br>Bundesamt für Kartographie und Geodäsie (BKG) | Hinweiskarte Starkregengefahren<br>_Heavy-Rain (Pluvial) Hazard Advisory Map_ | surface_water | unknown | Germany; Länder coverage expanding (11 Länder live early 2026, nationwide completion targeted end 2026) | OGC service | unknown | Service (OGC) | [Service](https://sgx.geodatenzentrum.de/wms_starkregen?request=GetCapabilities&service=WMS) | 2026-06-24 | verified | Direct dataset endpoint selected for bounded validation. |
| DE-BW-001 | Baden-Württemberg<br>Landesanstalt für Umwelt Baden-Württemberg | Hochwassergefahrenkarten (UDO)<br>_Flood Hazard Maps Baden-Württemberg_ | fluvial | HQ10, HQ50, HQ100, HQextrem, depth | Baden-Württemberg | Interactive viewer | unknown | Interactive viewer | [Primary](https://udo.lubw.baden-wuerttemberg.de/public/) | 2026-06-24 | verified | Official dataset-specific page or viewer confirmed during bounded page review. |
| DE-BY-001 | Bayern<br>Bayerisches Landesamt für Umwelt | UmweltAtlas Bayern - Naturgefahren Hochwasser<br>_Bavaria Environmental Atlas - Flood Hazards_ | fluvial, flash_flood | HQhäufig, HQ100, HQextrem, depth candidates | Bayern | Interactive viewer | unknown | Interactive viewer | [Primary](https://www.umweltatlas.bayern.de/mapapps/resources/apps/umweltatlas/index.html?lang=de) | 2026-06-24 | verified | Official dataset-specific page or viewer confirmed during bounded page review. |
| DE-EEA-001 | National fallback<br>European Environment Agency | WISE Floods Directive | fluvial, coastal | unknown | Germany | Dataset-specific page | EEA reuse policy | Dataset page | [Primary](https://water.europa.eu/freshwater/europe-freshwater/floods-directive) | 2026-06-24 | fallback, non-material, verified | Official dataset-specific page or viewer confirmed during bounded page review. |
| DE-HE-001 | Hessen<br>Hessisches Landesamt für Naturschutz, Umwelt und Geologie | Hochwasserrisikomanagement Hessen<br>_Hesse Flood Risk Management Maps_ | fluvial | HQ10, HQ100, HQextrem, depth candidates | Hessen | Dataset-specific page | unknown | Dataset page | [Primary](https://hochwasser.hessen.de/) | 2026-06-24 | verified | Official dataset-specific page or viewer confirmed during bounded page review. |
| DE-NW-001 | Nordrhein-Westfalen<br>Ministerium für Umwelt, Naturschutz und Verkehr NRW | Hochwassergefahrenkarten und Hochwasserrisikokarten<br>_Flood Hazard and Flood Risk Maps NRW_ | fluvial | high, medium, low probability | Nordrhein-Westfalen | Dataset-specific page | unknown | Dataset page | [Primary](https://www.flussgebiete.nrw.de/hochwassergefahrenkarten-und-hochwasserrisikokarten) | 2026-06-24 | verified | Official dataset-specific page or viewer confirmed during bounded page review. |
| DE-WBL-001 | National<br>Bund/Länder-Arbeitsgemeinschaft Wasser / WasserBLIcK | Hochwassergefahren- und Hochwasserrisikokarten<br>_Flood Hazard and Flood Risk Maps_ | fluvial, coastal | high/medium/low probability, Floods Directive cycles | Germany by river-basin district and Land | Dataset-specific page | unknown | Dataset page | [Primary](https://www.wasserblick.net/servlet/is/1/) | 2026-06-24 | verified | Official dataset-specific page or viewer confirmed during bounded page review. |

### Reachable investigation leads

These links resolve, but they are generic portals, catalogue searches, restricted/request-only paths, ambiguous products, or otherwise lack confirmed dataset-specific access. They are clickable for investigation but excluded from scoring.

| ID | Jurisdiction / agency | Candidate | Access | Link | Reason | Tracking |
|---|---|---|---|---|---|---|
| DE-BFG-001 | National<br>Bundesanstalt für Gewässerkunde (BfG) | Geoportal der BfG | Catalogue search | [Open](https://geoportal.bafg.de/) | The link is a catalogue/search entry point rather than a dataset-specific record. | human review |
| DE-NI-001 | Niedersachsen<br>Niedersächsischer Landesbetrieb für Wasserwirtschaft, Küsten- und Naturschutz | Umweltkarten Niedersachsen - Hochwasser | Generic portal | [Open](https://www.umweltkarten-niedersachsen.de/) | The link is a generic agency or geoportal entry point; the named dataset was not resolved. | human review |

### What comes next

1. Work the 2 investigation lead(s): use the portal search guide below to locate the dataset behind each portal, then confirm a usable service, download, viewer, or dataset page.
2. Extend beyond the 5-region pilot to the 11 deferred region(s).
3. Confirm licensing for 6 confirmed source(s) whose licence is still marked "verify".

## China (CN)

**Coverage model:** primarily regional · **Scope:** provisional — top-five-region pilot · **Confidence in completeness:** low

China has a national flood-risk-map programme and technical standards, but public machine-readable hazard datasets are difficult to locate. Candidate access is concentrated in Ministry of Water Resources and provincial water-resources portals; the top-five-province pilot covers Guangdong, Shandong, Henan, Jiangsu and Sichuan.

### What we have

- **Confirmed dataset access:** 1 source(s) (0 direct service/API/download, 1 viewer / map document / dataset page).
- **Investigation leads:** 5 reachable portal(s) that still need the dataset located by hand.
- **Unavailable:** 3 broken or unreachable candidate(s).
- **Hazard families confirmed:** Surface water (pluvial). **Not yet confirmed:** Fluvial (river), Coastal.
- **Best confirmed access:** Map document.


### Population-priority regions

| Rank | Region | Population | Year | Source |
|---:|---|---:|---:|---|
| 1 | Guangdong | 126,012,510 | 2020 | [Seventh National Population Census](https://www.stats.gov.cn/english/PressRelease/202105/t20210510_1817185.html) |
| 2 | Shandong | 101,527,453 | 2020 | [Seventh National Population Census](https://www.stats.gov.cn/english/PressRelease/202105/t20210510_1817185.html) |
| 3 | Henan | 99,365,519 | 2020 | [Seventh National Population Census](https://www.stats.gov.cn/english/PressRelease/202105/t20210510_1817185.html) |
| 4 | Jiangsu | 84,748,016 | 2020 | [Seventh National Population Census](https://www.stats.gov.cn/english/PressRelease/202105/t20210510_1817185.html) |
| 5 | Sichuan | 83,674,866 | 2020 | [Seventh National Population Census](https://www.stats.gov.cn/english/PressRelease/202105/t20210510_1817185.html) |

**Deferred regions:** Anhui, Beijing, Chongqing, Fujian, Gansu, Guangxi, Guizhou, Hainan, Hebei, Heilongjiang, Hubei, Hunan, Inner Mongolia, Jiangxi, Jilin, Liaoning, Ningxia, Qinghai, Shaanxi, Shanghai, Shanxi, Tianjin, Tibet, Xinjiang, Yunnan, Zhejiang

### Portal search guide and website roots

Use the exact dataset names in the directory first. If that fails, try the local-language flood terms below in the site's search box, map-layer catalogue, or metadata search. Website-root links are navigation aids; they are not themselves confirmation that a dataset is available.

**Portal languages:** Chinese

**Country search phrases:** `洪水风险图` · `洪水淹没图` · `淹没深度` · `流速` · `重现期` · `城市内涝风险图` · `内涝` · `urban waterlogging map` · `surface water flood`

**Native-language term guide:** `洪水风险图` — flood-risk map · `洪水淹没图` — flood-inundation map · `淹没深度` — inundation depth · `流速` — flow velocity · `重现期` — return period · `城市内涝风险图` — urban-waterlogging risk map · `内涝` — urban waterlogging. Paste the native term into the portal; the English text is only a meaning guide.

| Website root | Related source IDs | Publisher(s) | Search this site for | Link roles | Current classification |
|---|---|---|---|---|---|
| [jssslt.jiangsu.gov.cn](http://jssslt.jiangsu.gov.cn/) | CN-JS-001 | 江苏省水利厅 | `江苏省洪水风险图` | primary | unavailable candidate |
| [slt.sc.gov.cn](http://slt.sc.gov.cn/) | CN-SC-001 | 四川省水利厅 | `四川省洪水风险图与山洪灾害危险区` | primary, verification final, selected access | investigation lead |
| [wr.shandong.gov.cn](http://wr.shandong.gov.cn/) | CN-SD-001 | 山东省水利厅 | `山东省洪水风险图` | primary, verification final, selected access | investigation lead |
| [www.mwr.gov.cn](http://www.mwr.gov.cn/) | CN-MWR-001 | 中华人民共和国水利部 / Ministry of Water Resources | `全国洪水风险图编制与应用` | primary, verification final, selected access | investigation lead |
| [data.jrc.ec.europa.eu](https://data.jrc.ec.europa.eu/) | CN-JRC-001 | European Commission Joint Research Centre | `Global River Flood Hazard Maps` | primary, verification final, selected access | investigation lead |
| [slt.gd.gov.cn](https://slt.gd.gov.cn/) | CN-GD-001 | 广东省水利厅 | `广东省洪水风险图 / 山洪灾害风险图` | primary, verification final | unavailable candidate |
| [slt.henan.gov.cn](https://slt.henan.gov.cn/) | CN-HA-001 | 河南省水利厅 | `河南省洪水风险图` | primary, verification final | unavailable candidate |
| [swj.beijing.gov.cn](https://swj.beijing.gov.cn/) | CN-BJ-001 | 北京市水务局 (Beijing Municipal Water Authority) | `北京城市积水内涝风险地图` | primary, verification final, selected access | confirmed dataset access |
| [www.mem.gov.cn](https://www.mem.gov.cn/) | CN-MEM-001 | 中华人民共和国应急管理部 / Ministry of Emergency Management | `第一次全国自然灾害综合风险普查` | primary, verification final, selected access | investigation lead |
| [www.stats.gov.cn](https://www.stats.gov.cn/) | population: Guangdong, population: Shandong, population: Henan, population: Jiangsu, population: Sichuan | Seventh National Population Census | `Guangdong population`<br>`Shandong population`<br>`Henan population`<br>`Jiangsu population`<br>`Sichuan population` | population source | supporting citation |

### Confirmed dataset access

Each clickable link below was confirmed to identify an authoritative flood dataset and provide a usable service, download, viewer, map document, or dataset-specific page.

| ID | Jurisdiction / agency | Dataset | Confirmed flood type | Confirmed scenarios | Confirmed coverage | Confirmed formats | Confirmed licence | Access | Link | Verified | Flags | Evidence |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| CN-BJ-001 | Beijing Municipality<br>北京市水务局 (Beijing Municipal Water Authority) | 北京城市积水内涝风险地图<br>_Beijing Urban Waterlogging (Ponding) Risk Map_ | surface_water | unknown | Beijing Municipality (central city, sub-centre, and 11 suburban districts) | Map document | unknown | Map document | [Primary](https://swj.beijing.gov.cn/swdt/tzgg/202207/t20220707_2766190.html) | 2026-06-24 | verified | Official dataset-specific page or viewer confirmed during bounded page review. |

### Reachable investigation leads

These links resolve, but they are generic portals, catalogue searches, restricted/request-only paths, ambiguous products, or otherwise lack confirmed dataset-specific access. They are clickable for investigation but excluded from scoring.

| ID | Jurisdiction / agency | Candidate | Access | Link | Reason | Tracking |
|---|---|---|---|---|---|---|
| CN-MWR-001 | National<br>中华人民共和国水利部 / Ministry of Water Resources | 全国洪水风险图编制与应用 | Restricted | [Open](http://www.mwr.gov.cn/) | Access is restricted and no public dataset path was confirmed. | human review |
| CN-MEM-001 | National<br>中华人民共和国应急管理部 / Ministry of Emergency Management | 第一次全国自然灾害综合风险普查 | Restricted | [Open](https://www.mem.gov.cn/) | Access is restricted and no public dataset path was confirmed. | human review |
| CN-SD-001 | Shandong<br>山东省水利厅 | 山东省洪水风险图 | Restricted | [Open](http://wr.shandong.gov.cn/) | Access is restricted and no public dataset path was confirmed. | human review |
| CN-SC-001 | Sichuan<br>四川省水利厅 | 四川省洪水风险图与山洪灾害危险区 | Restricted | [Open](http://slt.sc.gov.cn/) | Access is restricted and no public dataset path was confirmed. | human review |
| CN-JRC-001 | National fallback<br>European Commission Joint Research Centre | Global River Flood Hazard Maps | Restricted | [Open](https://data.jrc.ec.europa.eu/collection/id-0054) | The JRC collection resolves to a login surface; unauthenticated dataset access was not confirmed. | non-material candidate |

### Unavailable candidates

These links did not resolve. URLs are plain text and non-clickable.

| ID | Jurisdiction / agency | Candidate | Status | Candidate URL | Tracking |
|---|---|---|---|---|---|
| CN-GD-001 | Guangdong<br>广东省水利厅 | 广东省洪水风险图 / 山洪灾害风险图 | failed (HTTP 500): No candidate link resolved successfully during the strict audit. | `https://slt.gd.gov.cn/` | human review |
| CN-HA-001 | Henan<br>河南省水利厅 | 河南省洪水风险图 | failed (HTTP 403): The official page returned HTTP 403; public dataset usability could not be confirmed. | `https://slt.henan.gov.cn/` | human review |
| CN-JS-001 | Jiangsu<br>江苏省水利厅 | 江苏省洪水风险图 | failed (unreachable): No candidate link resolved successfully during the strict audit. | `http://jssslt.jiangsu.gov.cn/` | human review |

### What comes next

1. Confirm Fluvial (river), Coastal coverage — a candidate exists but its dataset is not yet confirmed.
2. Work the 5 investigation lead(s): use the portal search guide below to locate the dataset behind each portal, then confirm a usable service, download, viewer, or dataset page.
3. Resolve 3 broken or unreachable material source(s) flagged for human review (see the Unavailable table and the Human review required section).
4. Extend beyond the 5-region pilot to the 26 deferred region(s).
5. Confirm licensing for 1 confirmed source(s) whose licence is still marked "verify".

## Canada (CA)

**Coverage model:** national catalogue with regional publishers · **Scope:** provisional — top-five-region pilot · **Confidence in completeness:** medium

Natural Resources Canada coordinates national flood-hazard identification and provides federal discovery products, while provinces, territories and conservation authorities remain the authoritative publishers for detailed floodplain mapping. The pilot covers Ontario, Quebec, British Columbia, Alberta and Manitoba.

### What we have

- **Confirmed dataset access:** 3 source(s) (0 direct service/API/download, 3 viewer / map document / dataset page).
- **Investigation leads:** 1 reachable portal(s) that still need the dataset located by hand.
- **Unavailable:** 4 broken or unreachable candidate(s).
- **Hazard families confirmed:** Fluvial (river), Coastal, Surface water (pluvial).
- **Best confirmed access:** Interactive viewer, Dataset page.


### Population-priority regions

| Rank | Region | Population | Year | Source |
|---:|---|---:|---:|---|
| 1 | Ontario | 14,223,942 | 2021 | [Statistics Canada 2021 Census](https://www12.statcan.gc.ca/census-recensement/2021/dp-pd/index-eng.cfm) |
| 2 | Quebec | 8,501,833 | 2021 | [Statistics Canada 2021 Census](https://www12.statcan.gc.ca/census-recensement/2021/dp-pd/index-eng.cfm) |
| 3 | British Columbia | 5,000,879 | 2021 | [Statistics Canada 2021 Census](https://www12.statcan.gc.ca/census-recensement/2021/dp-pd/index-eng.cfm) |
| 4 | Alberta | 4,262,635 | 2021 | [Statistics Canada 2021 Census](https://www12.statcan.gc.ca/census-recensement/2021/dp-pd/index-eng.cfm) |
| 5 | Manitoba | 1,342,153 | 2021 | [Statistics Canada 2021 Census](https://www12.statcan.gc.ca/census-recensement/2021/dp-pd/index-eng.cfm) |

**Deferred regions:** New Brunswick, Newfoundland and Labrador, Northwest Territories, Nova Scotia, Nunavut, Prince Edward Island, Saskatchewan, Yukon

### Portal search guide and website roots

Use the exact dataset names in the directory first. If that fails, try the local-language flood terms below in the site's search box, map-layer catalogue, or metadata search. Website-root links are navigation aids; they are not themselves confirmation that a dataset is available.

**Portal languages:** English, French

**Country search phrases:** `flood hazard map` · `floodplain mapping` · `inundation depth` · `return period` · `carte des zones inondables` · `profondeur d'inondation` · `période de retour`

**Native-language term guide:** `carte des zones inondables` — flood-zone map · `profondeur d'inondation` — inundation depth · `période de retour` — return period. Paste the native term into the portal; the English text is only a meaning guide.

| Website root | Related source IDs | Publisher(s) | Search this site for | Link roles | Current classification |
|---|---|---|---|---|---|
| [data.jrc.ec.europa.eu](https://data.jrc.ec.europa.eu/) | CA-JRC-001 | European Commission Joint Research Centre | `Global River Flood Hazard Maps` | primary, verification final, selected access | investigation lead |
| [floods.alberta.ca](https://floods.alberta.ca/) | CA-AB-001 | Government of Alberta | `Alberta Flood Awareness Map Application` | primary, verification final, selected access | confirmed dataset access |
| [geoinondations.gouv.qc.ca](https://geoinondations.gouv.qc.ca/) | CA-QC-001 | Gouvernement du Québec | `Géo-Inondations` | primary | confirmed dataset access |
| [natural-resources.canada.ca](https://natural-resources.canada.ca/) | CA-NRCAN-001 | Natural Resources Canada | `Flood Hazard Identification and Mapping Program` | primary, verification final | unavailable candidate |
| [search.open.canada.ca](https://search.open.canada.ca/) | CA-OPENMAPS-001 | Government of Canada | `Open Maps / Flood-related geospatial datasets` | primary | unavailable candidate |
| [www.gov.mb.ca](https://www.gov.mb.ca/) | CA-MB-001 | Government of Manitoba | `Flood information and maps` | primary, verification final, selected access | confirmed dataset access |
| [www.ontario.ca](https://www.ontario.ca/) | CA-ON-001 | Government of Ontario / Ministry of Natural Resources | `Floodplain mapping` | primary, verification final | unavailable candidate |
| [www12.statcan.gc.ca](https://www12.statcan.gc.ca/) | population: Ontario, population: Quebec, population: British Columbia, population: Alberta, population: Manitoba | Statistics Canada 2021 Census | `Ontario population`<br>`Quebec population`<br>`British Columbia population`<br>`Alberta population`<br>`Manitoba population` | population source | supporting citation |
| [www2.gov.bc.ca](https://www2.gov.bc.ca/) | CA-BC-001 | Government of British Columbia | `Floodplain Mapping` | primary, verification final | unavailable candidate |
| [zonesinondables.mrnf.gouv.qc.ca:443](https://zonesinondables.mrnf.gouv.qc.ca:443/) | CA-QC-001 | Gouvernement du Québec | `Géo-Inondations` | verification final, selected access | confirmed dataset access |

### Confirmed dataset access

Each clickable link below was confirmed to identify an authoritative flood dataset and provide a usable service, download, viewer, map document, or dataset-specific page.

| ID | Jurisdiction / agency | Dataset | Confirmed flood type | Confirmed scenarios | Confirmed coverage | Confirmed formats | Confirmed licence | Access | Link | Verified | Flags | Evidence |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| CA-AB-001 | Alberta<br>Government of Alberta | Alberta Flood Awareness Map Application<br>_Alberta Flood Awareness Map_ | fluvial | 1% design flood and other study scenarios vary | Mapped Alberta communities and river reaches | Interactive viewer | unknown | Interactive viewer | [Primary](https://floods.alberta.ca/) | 2026-06-24 | verified | Official dataset-specific page or viewer confirmed during bounded page review. |
| CA-MB-001 | Manitoba<br>Government of Manitoba | Flood information and maps<br>_Manitoba Flood Information and Maps_ | fluvial, surface_water | unknown | Manitoba; strongest in major river corridors | Dataset-specific page | unknown | Dataset page | [Primary](https://www.gov.mb.ca/mti/) | 2026-06-24 | verified | Official dataset-specific page or viewer confirmed during bounded page review. |
| CA-QC-001 | Quebec<br>Gouvernement du Québec | Géo-Inondations<br>_Geo-Floods Quebec_ | fluvial, coastal | unknown | Quebec | Interactive viewer | unknown | Interactive viewer | [Primary](https://zonesinondables.mrnf.gouv.qc.ca:443/) | 2026-06-24 | verified | Official dataset-specific page or viewer confirmed during bounded page review. |

### Reachable investigation leads

These links resolve, but they are generic portals, catalogue searches, restricted/request-only paths, ambiguous products, or otherwise lack confirmed dataset-specific access. They are clickable for investigation but excluded from scoring.

| ID | Jurisdiction / agency | Candidate | Access | Link | Reason | Tracking |
|---|---|---|---|---|---|---|
| CA-JRC-001 | National fallback<br>European Commission Joint Research Centre | Global River Flood Hazard Maps | Restricted | [Open](https://data.jrc.ec.europa.eu/collection/id-0054) | The JRC collection resolves to a login surface; unauthenticated dataset access was not confirmed. | non-material candidate |

### Unavailable candidates

These links did not resolve. URLs are plain text and non-clickable.

| ID | Jurisdiction / agency | Candidate | Status | Candidate URL | Tracking |
|---|---|---|---|---|---|
| CA-NRCAN-001 | National<br>Natural Resources Canada | Flood Hazard Identification and Mapping Program | failed (HTTP 404): No candidate link resolved successfully during the strict audit. | `https://natural-resources.canada.ca/science-and-data/science-and-research/natural-hazards/flood-hazard-identification-and-mapping-program` | human review |
| CA-OPENMAPS-001 | National<br>Government of Canada | Open Maps / Flood-related geospatial datasets | failed (unreachable): The link is a catalogue/search entry point rather than a dataset-specific record. | `https://search.open.canada.ca/openmap/` | human review |
| CA-ON-001 | Ontario<br>Government of Ontario / Ministry of Natural Resources | Floodplain mapping | failed (HTTP 404): No candidate link resolved successfully during the strict audit. | `https://www.ontario.ca/page/floodplain-mapping` | human review |
| CA-BC-001 | British Columbia<br>Government of British Columbia | Floodplain Mapping | failed (HTTP 404): No candidate link resolved successfully during the strict audit. | `https://www2.gov.bc.ca/gov/content/environment/air-land-water/water/drought-flooding-dikes-dams/integrated-flood-hazard-management/flood-hazard-land-use-management/floodplain-mapping` | human review |

### What comes next

1. Work the 1 investigation lead(s): use the portal search guide below to locate the dataset behind each portal, then confirm a usable service, download, viewer, or dataset page.
2. Resolve 4 broken or unreachable material source(s) flagged for human review (see the Unavailable table and the Human review required section).
3. Extend beyond the 5-region pilot to the 8 deferred region(s).
4. Confirm licensing for 3 confirmed source(s) whose licence is still marked "verify".

## France (FR)

**Coverage model:** national catalogue with regional publishers · **Scope:** provisional — top-five-region pilot · **Confidence in completeness:** medium

Géorisques provides national discovery and standardized regulatory/risk layers, while detailed Floods Directive TRI maps, PPRI products and hydraulic depth/velocity layers are published through regional DREAL/DDT services. The pilot covers Île-de-France, Auvergne-Rhône-Alpes, Nouvelle-Aquitaine, Occitanie and Hauts-de-France.

### What we have

- **Confirmed dataset access:** 2 source(s) (0 direct service/API/download, 2 viewer / map document / dataset page).
- **Investigation leads:** 2 reachable portal(s) that still need the dataset located by hand.
- **Unavailable:** 4 broken or unreachable candidate(s).
- **Hazard families confirmed:** Fluvial (river), Coastal. **Not yet confirmed:** Surface water (pluvial).
- **Best confirmed access:** Dataset page.


### Population-priority regions

| Rank | Region | Population | Year | Source |
|---:|---|---:|---:|---|
| 1 | Île-de-France | 12,395,000 | 2024 | [INSEE regional population estimates](https://www.insee.fr/fr/statistiques/7728784) |
| 2 | Auvergne-Rhône-Alpes | 8,169,000 | 2024 | [INSEE regional population estimates](https://www.insee.fr/fr/statistiques/7728784) |
| 3 | Nouvelle-Aquitaine | 6,154,000 | 2024 | [INSEE regional population estimates](https://www.insee.fr/fr/statistiques/7728784) |
| 4 | Occitanie | 6,080,000 | 2024 | [INSEE regional population estimates](https://www.insee.fr/fr/statistiques/7728784) |
| 5 | Hauts-de-France | 5,995,000 | 2024 | [INSEE regional population estimates](https://www.insee.fr/fr/statistiques/7728784) |

**Deferred regions:** Bourgogne-Franche-Comté, Bretagne, Centre-Val de Loire, Corse, Grand Est, Normandie, Pays de la Loire, Provence-Alpes-Côte d'Azur, Guadeloupe, Guyane, La Réunion, Martinique, Mayotte

### Portal search guide and website roots

Use the exact dataset names in the directory first. If that fails, try the local-language flood terms below in the site's search box, map-layer catalogue, or metadata search. Website-root links are navigation aids; they are not themselves confirmation that a dataset is available.

**Portal languages:** French

**Country search phrases:** `carte aléa inondation` · `zone inondable` · `hauteur d'eau` · `vitesse d'écoulement` · `période de retour`

**Native-language term guide:** `carte aléa inondation` — flood-hazard map · `zone inondable` — flood-prone zone · `hauteur d'eau` — water depth · `vitesse d'écoulement` — flow velocity · `période de retour` — return period. Paste the native term into the portal; the English text is only a meaning guide.

| Website root | Related source IDs | Publisher(s) | Search this site for | Link roles | Current classification |
|---|---|---|---|---|---|
| [water.europa.eu](https://water.europa.eu/) | FR-EEA-001 | European Environment Agency | `WISE Floods Directive` | primary, verification final, selected access | confirmed dataset access |
| [www.auvergne-rhone-alpes.developpement-durable.gouv.fr](https://www.auvergne-rhone-alpes.developpement-durable.gouv.fr/) | FR-ARA-001 | DREAL Auvergne-Rhône-Alpes | `Directive inondation - cartographies des TRI` | primary, verification final | unavailable candidate |
| [www.drieat.ile-de-france.developpement-durable.gouv.fr](https://www.drieat.ile-de-france.developpement-durable.gouv.fr/) | FR-IDF-001 | DRIEAT Île-de-France | `Cartographie des territoires à risque important d'inondation` | primary, verification final | unavailable candidate |
| [www.geoportail-urbanisme.gouv.fr](https://www.geoportail-urbanisme.gouv.fr/) | FR-GPU-001 | Ministère de la Transition écologique | `Géoportail de l'Urbanisme - Plans de prévention des risques` | primary, verification final, selected access | investigation lead |
| [www.georisques.gouv.fr](https://www.georisques.gouv.fr/) | FR-GEORISQUES-001 | Ministère de la Transition écologique / BRGM | `Géorisques - Inondation` | primary, verification final, selected access | investigation lead |
| [www.hauts-de-france.developpement-durable.gouv.fr](https://www.hauts-de-france.developpement-durable.gouv.fr/) | FR-HDF-001 | DREAL Hauts-de-France | `Cartographies des territoires à risques importants d'inondation` | primary, verification final | unavailable candidate |
| [www.insee.fr](https://www.insee.fr/) | population: Île-de-France, population: Auvergne-Rhône-Alpes, population: Nouvelle-Aquitaine, population: Occitanie, population: Hauts-de-France | INSEE regional population estimates | `Île-de-France population`<br>`Auvergne-Rhône-Alpes population`<br>`Nouvelle-Aquitaine population`<br>`Occitanie population`<br>`Hauts-de-France population` | population source | supporting citation |
| [www.nouvelle-aquitaine.developpement-durable.gouv.fr](https://www.nouvelle-aquitaine.developpement-durable.gouv.fr/) | FR-NAQ-001 | DREAL Nouvelle-Aquitaine | `Cartographie des risques d'inondation` | primary, verification final, selected access | confirmed dataset access |
| [www.occitanie.developpement-durable.gouv.fr](https://www.occitanie.developpement-durable.gouv.fr/) | FR-OCC-001 | DREAL Occitanie | `Cartographie des surfaces inondables et des risques` | primary, verification final | unavailable candidate |

### Confirmed dataset access

Each clickable link below was confirmed to identify an authoritative flood dataset and provide a usable service, download, viewer, map document, or dataset-specific page.

| ID | Jurisdiction / agency | Dataset | Confirmed flood type | Confirmed scenarios | Confirmed coverage | Confirmed formats | Confirmed licence | Access | Link | Verified | Flags | Evidence |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| FR-EEA-001 | National fallback<br>European Environment Agency | WISE Floods Directive | fluvial, coastal | unknown | France | Dataset-specific page | EEA reuse policy | Dataset page | [Primary](https://water.europa.eu/freshwater/europe-freshwater/floods-directive) | 2026-06-24 | fallback, non-material, verified | Official dataset-specific page or viewer confirmed during bounded page review. |
| FR-NAQ-001 | Nouvelle-Aquitaine<br>DREAL Nouvelle-Aquitaine | Cartographie des risques d'inondation<br>_Nouvelle-Aquitaine Flood-Risk Maps_ | fluvial, coastal | unknown | Nouvelle-Aquitaine TRI areas | Dataset-specific page | unknown | Dataset page | [Primary](https://www.nouvelle-aquitaine.developpement-durable.gouv.fr/directive-inondation-r740.html) | 2026-06-24 | verified | Official dataset-specific page or viewer confirmed during bounded page review. |

### Reachable investigation leads

These links resolve, but they are generic portals, catalogue searches, restricted/request-only paths, ambiguous products, or otherwise lack confirmed dataset-specific access. They are clickable for investigation but excluded from scoring.

| ID | Jurisdiction / agency | Candidate | Access | Link | Reason | Tracking |
|---|---|---|---|---|---|---|
| FR-GEORISQUES-001 | National<br>Ministère de la Transition écologique / BRGM | Géorisques - Inondation | Catalogue search | [Open](https://www.georisques.gouv.fr/donnees/bases-de-donnees) | The link is a catalogue/search entry point rather than a dataset-specific record. | human review |
| FR-GPU-001 | National<br>Ministère de la Transition écologique | Géoportail de l'Urbanisme - Plans de prévention des risques | Generic portal | [Open](https://www.geoportail-urbanisme.gouv.fr/) | The link is a generic agency or geoportal entry point; the named dataset was not resolved. | human review |

### Unavailable candidates

These links did not resolve. URLs are plain text and non-clickable.

| ID | Jurisdiction / agency | Candidate | Status | Candidate URL | Tracking |
|---|---|---|---|---|---|
| FR-IDF-001 | Île-de-France<br>DRIEAT Île-de-France | Cartographie des territoires à risque important d'inondation | failed (HTTP 404): No candidate link resolved successfully during the strict audit. | `https://www.drieat.ile-de-france.developpement-durable.gouv.fr/cartographie-des-risques-d-inondation-r677.html` | human review |
| FR-ARA-001 | Auvergne-Rhône-Alpes<br>DREAL Auvergne-Rhône-Alpes | Directive inondation - cartographies des TRI | failed (HTTP 404): No candidate link resolved successfully during the strict audit. | `https://www.auvergne-rhone-alpes.developpement-durable.gouv.fr/directive-inondation-r3414.html` | human review |
| FR-OCC-001 | Occitanie<br>DREAL Occitanie | Cartographie des surfaces inondables et des risques | failed (HTTP 404): No candidate link resolved successfully during the strict audit. | `https://www.occitanie.developpement-durable.gouv.fr/la-directive-inondation-r7214.html` | human review |
| FR-HDF-001 | Hauts-de-France<br>DREAL Hauts-de-France | Cartographies des territoires à risques importants d'inondation | failed (HTTP 404): No candidate link resolved successfully during the strict audit. | `https://www.hauts-de-france.developpement-durable.gouv.fr/?Cartographie-des-risques-d-inondation` | human review |

### What comes next

1. Confirm Surface water (pluvial) coverage — a candidate exists but its dataset is not yet confirmed.
2. Work the 2 investigation lead(s): use the portal search guide below to locate the dataset behind each portal, then confirm a usable service, download, viewer, or dataset page.
3. Resolve 4 broken or unreachable material source(s) flagged for human review (see the Unavailable table and the Human review required section).
4. Extend beyond the 5-region pilot to the 13 deferred region(s).
5. Confirm licensing for 1 confirmed source(s) whose licence is still marked "verify".

## Mexico (MX)

**Coverage model:** mixed national and regional · **Scope:** provisional — top-five-region pilot · **Confidence in completeness:** medium

CENAPRED's Atlas Nacional de Riesgos provides the main national viewer and inventories state/municipal atlases, while CONAGUA and INEGI provide hydrographic and flood-related layers. Detailed hazard maps vary by state and municipality; the pilot covers Estado de México, Ciudad de México, Jalisco, Veracruz and Puebla.

### What we have

- **Confirmed dataset access:** 1 source(s) (0 direct service/API/download, 1 viewer / map document / dataset page).
- **Investigation leads:** 4 reachable portal(s) that still need the dataset located by hand.
- **Unavailable:** 4 broken or unreachable candidate(s).
- **Hazard families confirmed:** Fluvial (river), Surface water (pluvial). **Not yet confirmed:** Coastal.
- **Best confirmed access:** Interactive viewer.


### Population-priority regions

| Rank | Region | Population | Year | Source |
|---:|---|---:|---:|---|
| 1 | Estado de México | 16,992,418 | 2020 | [INEGI Censo de Población y Vivienda 2020](https://www.inegi.org.mx/programas/ccpv/2020/) |
| 2 | Ciudad de México | 9,209,944 | 2020 | [INEGI Censo de Población y Vivienda 2020](https://www.inegi.org.mx/programas/ccpv/2020/) |
| 3 | Jalisco | 8,348,151 | 2020 | [INEGI Censo de Población y Vivienda 2020](https://www.inegi.org.mx/programas/ccpv/2020/) |
| 4 | Veracruz | 8,062,579 | 2020 | [INEGI Censo de Población y Vivienda 2020](https://www.inegi.org.mx/programas/ccpv/2020/) |
| 5 | Puebla | 6,583,278 | 2020 | [INEGI Censo de Población y Vivienda 2020](https://www.inegi.org.mx/programas/ccpv/2020/) |

**Deferred regions:** Aguascalientes, Baja California, Baja California Sur, Campeche, Chiapas, Chihuahua, Coahuila, Colima, Durango, Guanajuato, Guerrero, Hidalgo, Michoacán, Morelos, Nayarit, Nuevo León, Oaxaca, Querétaro, Quintana Roo, San Luis Potosí, Sinaloa, Sonora, Tabasco, Tamaulipas, Tlaxcala, Yucatán, Zacatecas

### Portal search guide and website roots

Use the exact dataset names in the directory first. If that fails, try the local-language flood terms below in the site's search box, map-layer catalogue, or metadata search. Website-root links are navigation aids; they are not themselves confirmation that a dataset is available.

**Portal languages:** Spanish

**Country search phrases:** `mapa de peligro de inundación` · `zona inundable` · `profundidad de inundación` · `velocidad` · `periodo de retorno`

**Native-language term guide:** `mapa de peligro de inundación` — flood-hazard map · `zona inundable` — flood-prone zone · `profundidad de inundación` — inundation depth · `velocidad` — velocity · `periodo de retorno` — return period. Paste the native term into the portal; the English text is only a meaning guide.

| Website root | Related source IDs | Publisher(s) | Search this site for | Link roles | Current classification |
|---|---|---|---|---|---|
| [www.veracruz.gob.mx](http://www.veracruz.gob.mx/) | MX-VER-001 | Secretaría de Protección Civil de Veracruz | `Atlas de Riesgos del Estado de Veracruz` | primary | unavailable candidate |
| [antares.inegi.org.mx](https://antares.inegi.org.mx/) | MX-INEGI-001 | Instituto Nacional de Estadística y Geografía | `SIATL - Simulador de Flujos de Agua de Cuencas Hidrográficas` | primary, verification final, selected access | investigation lead |
| [atlasderiesgo.edomex.gob.mx](https://atlasderiesgo.edomex.gob.mx/) | MX-EM-001 | Coordinación General de Protección Civil del Estado de México | `Atlas de Riesgos del Estado de México` | primary | unavailable candidate |
| [atlasderiesgos.puebla.gob.mx](https://atlasderiesgos.puebla.gob.mx/) | MX-PUE-001 | Coordinación General de Protección Civil del Estado de Puebla | `Atlas de Riesgos del Estado de Puebla` | primary | unavailable candidate |
| [data.jrc.ec.europa.eu](https://data.jrc.ec.europa.eu/) | MX-JRC-001 | European Commission Joint Research Centre | `Global River Flood Hazard Maps` | primary, verification final, selected access | investigation lead |
| [proteccioncivil.jalisco.gob.mx](https://proteccioncivil.jalisco.gob.mx/) | MX-JAL-001 | Unidad Estatal de Protección Civil y Bomberos Jalisco | `Atlas Estatal de Riesgos de Jalisco` | primary, verification final, selected access | investigation lead |
| [sina.conagua.gob.mx](https://sina.conagua.gob.mx/) | MX-CONAGUA-001 | Comisión Nacional del Agua | `Sistema Nacional de Información del Agua` | primary | investigation lead |
| [www.atlas.cdmx.gob.mx](https://www.atlas.cdmx.gob.mx/) | MX-CMX-001 | Secretaría de Gestión Integral de Riesgos y Protección Civil | `Atlas de Riesgos de la Ciudad de México` | primary, verification final, selected access | confirmed dataset access |
| [www.atlasnacionalderiesgos.gob.mx](https://www.atlasnacionalderiesgos.gob.mx/) | MX-CENAPRED-001 | Centro Nacional de Prevención de Desastres | `Atlas Nacional de Riesgos` | primary | unavailable candidate |
| [www.gob.mx](https://www.gob.mx/) | MX-CONAGUA-001 | Comisión Nacional del Agua | `Sistema Nacional de Información del Agua` | verification final, selected access | investigation lead |
| [www.inegi.org.mx](https://www.inegi.org.mx/) | population: Estado de México, population: Ciudad de México, population: Jalisco, population: Veracruz, population: Puebla | INEGI Censo de Población y Vivienda 2020 | `Estado de México population`<br>`Ciudad de México population`<br>`Jalisco population`<br>`Veracruz population`<br>`Puebla population` | population source | supporting citation |

### Confirmed dataset access

Each clickable link below was confirmed to identify an authoritative flood dataset and provide a usable service, download, viewer, map document, or dataset-specific page.

| ID | Jurisdiction / agency | Dataset | Confirmed flood type | Confirmed scenarios | Confirmed coverage | Confirmed formats | Confirmed licence | Access | Link | Verified | Flags | Evidence |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| MX-CMX-001 | Ciudad de México<br>Secretaría de Gestión Integral de Riesgos y Protección Civil | Atlas de Riesgos de la Ciudad de México<br>_Mexico City Risk Atlas_ | surface_water, fluvial | unknown | Ciudad de México | Interactive viewer | unknown | Interactive viewer | [Primary](https://www.atlas.cdmx.gob.mx/) | 2026-06-24 | verified | Official dataset-specific page or viewer confirmed during bounded page review. |

### Reachable investigation leads

These links resolve, but they are generic portals, catalogue searches, restricted/request-only paths, ambiguous products, or otherwise lack confirmed dataset-specific access. They are clickable for investigation but excluded from scoring.

| ID | Jurisdiction / agency | Candidate | Access | Link | Reason | Tracking |
|---|---|---|---|---|---|---|
| MX-CONAGUA-001 | National<br>Comisión Nacional del Agua | Sistema Nacional de Información del Agua | Catalogue search | [Open](https://www.gob.mx/conagua) | The link is a catalogue/search entry point rather than a dataset-specific record. | human review |
| MX-INEGI-001 | National<br>Instituto Nacional de Estadística y Geografía | SIATL - Simulador de Flujos de Agua de Cuencas Hidrográficas | Ambiguous | [Open](https://antares.inegi.org.mx/analisis/red_hidro/siatl/) | The page resolves, but dataset identity or usable access could not be confirmed. | human review |
| MX-JAL-001 | Jalisco<br>Unidad Estatal de Protección Civil y Bomberos Jalisco | Atlas Estatal de Riesgos de Jalisco | Generic portal | [Open](https://proteccioncivil.jalisco.gob.mx/) | The link is a generic agency or geoportal entry point; the named dataset was not resolved. | human review |
| MX-JRC-001 | National fallback<br>European Commission Joint Research Centre | Global River Flood Hazard Maps | Restricted | [Open](https://data.jrc.ec.europa.eu/collection/id-0054) | The JRC collection resolves to a login surface; unauthenticated dataset access was not confirmed. | non-material candidate |

### Unavailable candidates

These links did not resolve. URLs are plain text and non-clickable.

| ID | Jurisdiction / agency | Candidate | Status | Candidate URL | Tracking |
|---|---|---|---|---|---|
| MX-CENAPRED-001 | National<br>Centro Nacional de Prevención de Desastres | Atlas Nacional de Riesgos | failed (unreachable): No candidate link resolved successfully during the strict audit. | `https://www.atlasnacionalderiesgos.gob.mx/` | human review |
| MX-EM-001 | Estado de México<br>Coordinación General de Protección Civil del Estado de México | Atlas de Riesgos del Estado de México | failed (unreachable): No candidate link resolved successfully during the strict audit. | `https://atlasderiesgo.edomex.gob.mx/` | human review |
| MX-VER-001 | Veracruz<br>Secretaría de Protección Civil de Veracruz | Atlas de Riesgos del Estado de Veracruz | failed (unreachable): No candidate link resolved successfully during the strict audit. | `http://www.veracruz.gob.mx/proteccioncivil/atlas-de-riesgos/` | human review |
| MX-PUE-001 | Puebla<br>Coordinación General de Protección Civil del Estado de Puebla | Atlas de Riesgos del Estado de Puebla | failed (unreachable): No candidate link resolved successfully during the strict audit. | `https://atlasderiesgos.puebla.gob.mx/` | human review |

### What comes next

1. Confirm Coastal coverage — a candidate exists but its dataset is not yet confirmed.
2. Work the 4 investigation lead(s): use the portal search guide below to locate the dataset behind each portal, then confirm a usable service, download, viewer, or dataset page.
3. Resolve 4 broken or unreachable material source(s) flagged for human review (see the Unavailable table and the Human review required section).
4. Extend beyond the 5-region pilot to the 27 deferred region(s).
5. Confirm licensing for 1 confirmed source(s) whose licence is still marked "verify".

## Malaysia (MY)

**Coverage model:** mixed national and regional · **Scope:** provisional — top-five-region pilot · **Confidence in completeness:** low

The Department of Irrigation and Drainage operates national flood-information and geospatial systems, but detailed flood-hazard maps are commonly organized by river basin, state or study project. The top-five-state pilot covers Selangor, Johor, Sabah, Perak and Sarawak.

### What we have

- **Confirmed dataset access:** 0 source(s) (0 direct service/API/download, 0 viewer / map document / dataset page).
- **Investigation leads:** 5 reachable portal(s) that still need the dataset located by hand.
- **Unavailable:** 4 broken or unreachable candidate(s).
- **Hazard families confirmed:** none. **Not yet confirmed:** Fluvial (river), Coastal, Surface water (pluvial).
- **Best confirmed access:** No confirmed dataset access.


### Population-priority regions

| Rank | Region | Population | Year | Source |
|---:|---|---:|---:|---|
| 1 | Selangor | 6,994,233 | 2020 | [Department of Statistics Malaysia Census 2020](https://www.dosm.gov.my/portal-main/release-content/key-findings-population-and-housing-census-of-malaysia-2020) |
| 2 | Johor | 4,009,000 | 2020 | [Department of Statistics Malaysia Census 2020](https://www.dosm.gov.my/portal-main/release-content/key-findings-population-and-housing-census-of-malaysia-2020) |
| 3 | Sabah | 3,418,785 | 2020 | [Department of Statistics Malaysia Census 2020](https://www.dosm.gov.my/portal-main/release-content/key-findings-population-and-housing-census-of-malaysia-2020) |
| 4 | Perak | 2,496,700 | 2020 | [Department of Statistics Malaysia Census 2020](https://www.dosm.gov.my/portal-main/release-content/key-findings-population-and-housing-census-of-malaysia-2020) |
| 5 | Sarawak | 2,453,900 | 2020 | [Department of Statistics Malaysia Census 2020](https://www.dosm.gov.my/portal-main/release-content/key-findings-population-and-housing-census-of-malaysia-2020) |

**Deferred regions:** Kedah, Kelantan, Melaka, Negeri Sembilan, Pahang, Penang, Perlis, Terengganu, Federal Territories

### Portal search guide and website roots

Use the exact dataset names in the directory first. If that fails, try the local-language flood terms below in the site's search box, map-layer catalogue, or metadata search. Website-root links are navigation aids; they are not themselves confirmation that a dataset is available.

**Portal languages:** Malay

**Country search phrases:** `peta bahaya banjir` · `peta genangan banjir` · `kedalaman banjir` · `halaju banjir` · `tempoh ulangan`

**Native-language term guide:** `peta bahaya banjir` — flood-hazard map · `peta genangan banjir` — flood-inundation map · `kedalaman banjir` — flood depth · `halaju banjir` — flood velocity · `tempoh ulangan` — return period. Paste the native term into the portal; the English text is only a meaning guide.

| Website root | Related source IDs | Publisher(s) | Search this site for | Link roles | Current classification |
|---|---|---|---|---|---|
| [data.jrc.ec.europa.eu](https://data.jrc.ec.europa.eu/) | MY-JRC-001 | European Commission Joint Research Centre | `Global River Flood Hazard Maps` | primary, verification final, selected access | investigation lead |
| [did.sabah.gov.my](https://did.sabah.gov.my/) | MY-SBH-001 | Jabatan Pengairan dan Saliran Sabah | `Peta Bahaya Banjir Sabah` | primary, verification final, selected access | investigation lead |
| [did.sarawak.gov.my](https://did.sarawak.gov.my/) | MY-SWK-001 | Department of Irrigation and Drainage Sarawak | `Flood Hazard and Drainage Maps Sarawak` | primary, verification final, selected access | investigation lead |
| [jpsgeo.water.gov.my](https://jpsgeo.water.gov.my/) | MY-JPS-002, MY-SEL-001, MY-JHR-001, MY-PRK-001 | Jabatan Pengairan dan Saliran Malaysia; JPS Malaysia / JPS Selangor; JPS Malaysia / JPS Johor; JPS Malaysia / JPS Perak | `JPS Geospatial / Peta Bahaya Banjir`<br>`Peta Bahaya Banjir Selangor`<br>`Peta Bahaya Banjir Johor`<br>`Peta Bahaya Banjir Perak` | primary | unavailable candidate |
| [publicinfobanjir.water.gov.my](https://publicinfobanjir.water.gov.my/) | MY-JPS-001 | Jabatan Pengairan dan Saliran Malaysia / Department of Irrigation and Drainage | `Public Infobanjir` | primary, verification final, selected access | investigation lead |
| [www.dosm.gov.my](https://www.dosm.gov.my/) | population: Selangor, population: Johor, population: Sabah, population: Perak, population: Sarawak | Department of Statistics Malaysia Census 2020 | `Selangor population`<br>`Johor population`<br>`Sabah population`<br>`Perak population`<br>`Sarawak population` | population source | supporting citation |
| [www.nahrim.gov.my](https://www.nahrim.gov.my/) | MY-NAHRIM-001 | National Water Research Institute of Malaysia (NAHRIM) | `Flood and Climate Risk Research Products` | primary, verification final, selected access | investigation lead |

### Confirmed dataset access

Each clickable link below was confirmed to identify an authoritative flood dataset and provide a usable service, download, viewer, map document, or dataset-specific page.

| ID | Jurisdiction / agency | Dataset | Confirmed flood type | Confirmed scenarios | Confirmed coverage | Confirmed formats | Confirmed licence | Access | Link | Verified | Flags | Evidence |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| _none_ | — | — | — | — | — | — | — | — | — | — | — | — |

### Reachable investigation leads

These links resolve, but they are generic portals, catalogue searches, restricted/request-only paths, ambiguous products, or otherwise lack confirmed dataset-specific access. They are clickable for investigation but excluded from scoring.

| ID | Jurisdiction / agency | Candidate | Access | Link | Reason | Tracking |
|---|---|---|---|---|---|---|
| MY-JPS-001 | National<br>Jabatan Pengairan dan Saliran Malaysia / Department of Irrigation and Drainage | Public Infobanjir | Wrong product | [Open](https://publicinfobanjir.water.gov.my/) | The reachable product is operational or observational, not a confirmed flood-hazard dataset. | human review |
| MY-NAHRIM-001 | National<br>National Water Research Institute of Malaysia (NAHRIM) | Flood and Climate Risk Research Products | Generic portal | [Open](https://www.nahrim.gov.my/) | The link is a generic agency or geoportal entry point; the named dataset was not resolved. | human review |
| MY-SBH-001 | Sabah<br>Jabatan Pengairan dan Saliran Sabah | Peta Bahaya Banjir Sabah | Generic portal | [Open](https://did.sabah.gov.my/) | The link is a generic agency or geoportal entry point; the named dataset was not resolved. | human review |
| MY-SWK-001 | Sarawak<br>Department of Irrigation and Drainage Sarawak | Flood Hazard and Drainage Maps Sarawak | Generic portal | [Open](https://did.sarawak.gov.my/web/home/index/) | The link is a generic agency or geoportal entry point; the named dataset was not resolved. | human review |
| MY-JRC-001 | National fallback<br>European Commission Joint Research Centre | Global River Flood Hazard Maps | Restricted | [Open](https://data.jrc.ec.europa.eu/collection/id-0054) | The JRC collection resolves to a login surface; unauthenticated dataset access was not confirmed. | non-material candidate |

### Unavailable candidates

These links did not resolve. URLs are plain text and non-clickable.

| ID | Jurisdiction / agency | Candidate | Status | Candidate URL | Tracking |
|---|---|---|---|---|---|
| MY-JPS-002 | National<br>Jabatan Pengairan dan Saliran Malaysia | JPS Geospatial / Peta Bahaya Banjir | failed (unreachable): No candidate link resolved successfully during the strict audit. | `https://jpsgeo.water.gov.my/` | human review |
| MY-SEL-001 | Selangor<br>JPS Malaysia / JPS Selangor | Peta Bahaya Banjir Selangor | failed (unreachable): No candidate link resolved successfully during the strict audit. | `https://jpsgeo.water.gov.my/` | human review |
| MY-JHR-001 | Johor<br>JPS Malaysia / JPS Johor | Peta Bahaya Banjir Johor | failed (unreachable): No candidate link resolved successfully during the strict audit. | `https://jpsgeo.water.gov.my/` | human review |
| MY-PRK-001 | Perak<br>JPS Malaysia / JPS Perak | Peta Bahaya Banjir Perak | failed (unreachable): No candidate link resolved successfully during the strict audit. | `https://jpsgeo.water.gov.my/` | human review |

### What comes next

1. Confirm Fluvial (river), Coastal, Surface water (pluvial) coverage — a candidate exists but its dataset is not yet confirmed.
2. Work the 5 investigation lead(s): use the portal search guide below to locate the dataset behind each portal, then confirm a usable service, download, viewer, or dataset page.
3. Resolve 4 broken or unreachable material source(s) flagged for human review (see the Unavailable table and the Human review required section).
4. Extend beyond the 5-region pilot to the 9 deferred region(s).

## Poland (PL)

**Coverage model:** nationally unified · **Confidence in completeness:** medium

Państwowe Gospodarstwo Wodne Wody Polskie publishes nationally standardized Floods Directive hazard and risk maps through the ISOK Hydroportal. Products are organized by river basin and planning cycle but are available through a unified national interface. Surface-water (pluvial / powódź opadowa) hazard: no authoritative national or major-city product exists - the statutory ISOK/Wody Polskie Floods Directive maps explicitly exclude rainfall/stormwater flooding, and only academic case studies were found (verified June 2026).

### What we have

- **Confirmed dataset access:** 3 source(s) (0 direct service/API/download, 3 viewer / map document / dataset page).
- **Investigation leads:** 2 reachable portal(s) that still need the dataset located by hand.
- **Unavailable:** 0 broken or unreachable candidate(s).
- **Hazard families confirmed:** Fluvial (river), Coastal. **Not yet confirmed:** Surface water (pluvial).
- **Best confirmed access:** Interactive viewer, Dataset page.


### Portal search guide and website roots

Use the exact dataset names in the directory first. If that fails, try the local-language flood terms below in the site's search box, map-layer catalogue, or metadata search. Website-root links are navigation aids; they are not themselves confirmation that a dataset is available.

**Portal languages:** Polish

**Country search phrases:** `mapa zagrożenia powodziowego` · `obszar zalewowy` · `głębokość wody` · `prędkość przepływu` · `okres powtarzalności` · `mapa zagrożenia powodzią opadową` · `powódź miejska` · `surface water flood map` · `pluvial flood`

**Native-language term guide:** `mapa zagrożenia powodziowego` — flood-hazard map · `obszar zalewowy` — inundation area · `głębokość wody` — water depth · `prędkość przepływu` — flow velocity · `okres powtarzalności` — return period · `mapa zagrożenia powodzią opadową` — rainfall-flood hazard map · `powódź miejska` — urban flooding. Paste the native term into the portal; the English text is only a meaning guide.

| Website root | Related source IDs | Publisher(s) | Search this site for | Link roles | Current classification |
|---|---|---|---|---|---|
| [hydro.imgw.pl](https://hydro.imgw.pl/) | PL-IMGW-001 | Instytut Meteorologii i Gospodarki Wodnej | `Hydro IMGW-PIB` | primary, verification final, selected access | investigation lead |
| [mapy.geoportal.gov.pl](https://mapy.geoportal.gov.pl/) | PL-GUGIK-001 | Główny Urząd Geodezji i Kartografii | `Geoportal Krajowy - zagrożenie powodziowe` | primary, verification final, selected access | investigation lead |
| [water.europa.eu](https://water.europa.eu/) | PL-EEA-001 | European Environment Agency | `WISE Floods Directive` | primary, verification final, selected access | confirmed dataset access |
| [wody.isok.gov.pl](https://wody.isok.gov.pl/) | PL-WP-001 | Państwowe Gospodarstwo Wodne Wody Polskie | `Hydroportal ISOK - Mapy zagrożenia powodziowego` | primary, verification final, selected access | confirmed dataset access |
| [www.gov.pl](https://www.gov.pl/) | PL-WP-002 | Państwowe Gospodarstwo Wodne Wody Polskie | `Mapy zagrożenia powodziowego i mapy ryzyka powodziowego` | primary, verification final, selected access | confirmed dataset access |

### Confirmed dataset access

Each clickable link below was confirmed to identify an authoritative flood dataset and provide a usable service, download, viewer, map document, or dataset-specific page.

| ID | Jurisdiction / agency | Dataset | Confirmed flood type | Confirmed scenarios | Confirmed coverage | Confirmed formats | Confirmed licence | Access | Link | Verified | Flags | Evidence |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| PL-EEA-001 | National fallback<br>European Environment Agency | WISE Floods Directive | fluvial, coastal | unknown | Poland | Dataset-specific page | EEA reuse policy | Dataset page | [Primary](https://water.europa.eu/freshwater/europe-freshwater/floods-directive) | 2026-06-24 | fallback, non-material, verified | Official dataset-specific page or viewer confirmed during bounded page review. |
| PL-WP-001 | National<br>Państwowe Gospodarstwo Wodne Wody Polskie | Hydroportal ISOK - Mapy zagrożenia powodziowego<br>_ISOK Hydroportal Flood Hazard Maps_ | fluvial, coastal | high probability, medium probability, low probability/extreme, depth, velocity candidates | Poland | Interactive viewer | unknown | Interactive viewer | [Primary](https://wody.isok.gov.pl/imap_kzgw/?gpmap=gpMZP) | 2026-06-24 | verified | Official dataset-specific page or viewer confirmed during bounded page review. |
| PL-WP-002 | National<br>Państwowe Gospodarstwo Wodne Wody Polskie | Mapy zagrożenia powodziowego i mapy ryzyka powodziowego<br>_Flood Hazard and Flood Risk Maps_ | fluvial, coastal | 10-year/100-year/500-year equivalents vary by product cycle | Poland | Dataset-specific page | unknown | Dataset page | [Primary](https://www.gov.pl/web/wody-polskie/mapy-zagrozenia-powodziowego-i-mapy-ryzyka-powodziowego) | 2026-06-24 | verified | Official dataset-specific page or viewer confirmed during bounded page review. |

### Reachable investigation leads

These links resolve, but they are generic portals, catalogue searches, restricted/request-only paths, ambiguous products, or otherwise lack confirmed dataset-specific access. They are clickable for investigation but excluded from scoring.

| ID | Jurisdiction / agency | Candidate | Access | Link | Reason | Tracking |
|---|---|---|---|---|---|---|
| PL-GUGIK-001 | National<br>Główny Urząd Geodezji i Kartografii | Geoportal Krajowy - zagrożenie powodziowe | Ambiguous | [Open](https://mapy.geoportal.gov.pl/imap/Imgp_2.html) | The page resolves, but dataset identity or usable access could not be confirmed. | human review |
| PL-IMGW-001 | National supporting<br>Instytut Meteorologii i Gospodarki Wodnej | Hydro IMGW-PIB | Wrong product | [Open](https://hydro.imgw.pl/) | The reachable product is operational or observational, not a confirmed flood-hazard dataset. | non-material candidate |

### What comes next

1. Find Surface water (pluvial) coverage, or document in the summary above why the family does not apply.
2. Work the 2 investigation lead(s): use the portal search guide below to locate the dataset behind each portal, then confirm a usable service, download, viewer, or dataset page.
3. Confirm licensing for 2 confirmed source(s) whose licence is still marked "verify".

## Japan (JP)

**Coverage model:** national catalogue with regional publishers · **Scope:** provisional — top-five-region pilot · **Confidence in completeness:** high

MLIT and GSI provide a unified national hazard-map portal and downloadable national land numerical information, while legally designated inundation-assumption zones and local hazard maps are maintained by prefectures, river offices and municipalities. The pilot covers Tokyo, Kanagawa, Osaka, Aichi and Saitama.

### What we have

- **Confirmed dataset access:** 4 source(s) (0 direct service/API/download, 4 viewer / map document / dataset page).
- **Investigation leads:** 0 reachable portal(s) that still need the dataset located by hand.
- **Unavailable:** 4 broken or unreachable candidate(s).
- **Hazard families confirmed:** Fluvial (river), Coastal, Surface water (pluvial).
- **Best confirmed access:** Interactive viewer, Dataset page.


### Population-priority regions

| Rank | Region | Population | Year | Source |
|---:|---|---:|---:|---|
| 1 | Tokyo | 14,047,594 | 2020 | [Statistics Bureau of Japan 2020 Census](https://www.stat.go.jp/english/data/kokusei/2020/summary.html) |
| 2 | Kanagawa | 9,237,337 | 2020 | [Statistics Bureau of Japan 2020 Census](https://www.stat.go.jp/english/data/kokusei/2020/summary.html) |
| 3 | Osaka | 8,837,685 | 2020 | [Statistics Bureau of Japan 2020 Census](https://www.stat.go.jp/english/data/kokusei/2020/summary.html) |
| 4 | Aichi | 7,542,415 | 2020 | [Statistics Bureau of Japan 2020 Census](https://www.stat.go.jp/english/data/kokusei/2020/summary.html) |
| 5 | Saitama | 7,344,765 | 2020 | [Statistics Bureau of Japan 2020 Census](https://www.stat.go.jp/english/data/kokusei/2020/summary.html) |

**Deferred regions:** Hokkaido, Aomori, Iwate, Miyagi, Akita, Yamagata, Fukushima, Ibaraki, Tochigi, Gunma, Chiba, Niigata, Toyama, Ishikawa, Fukui, Yamanashi, Nagano, Gifu, Shizuoka, Mie, Shiga, Kyoto, Hyogo, Nara, Wakayama, Tottori, Shimane, Okayama, Hiroshima, Yamaguchi, Tokushima, Kagawa, Ehime, Kochi, Fukuoka, Saga, Nagasaki, Kumamoto, Oita, Miyazaki, Kagoshima, Okinawa

### Portal search guide and website roots

Use the exact dataset names in the directory first. If that fails, try the local-language flood terms below in the site's search box, map-layer catalogue, or metadata search. Website-root links are navigation aids; they are not themselves confirmation that a dataset is available.

**Portal languages:** Japanese

**Country search phrases:** `洪水ハザードマップ` · `浸水想定区域` · `浸水深` · `流速` · `再現期間`

**Native-language term guide:** `洪水ハザードマップ` — flood-hazard map · `浸水想定区域` — designated inundation area · `浸水深` — inundation depth · `流速` — flow velocity · `再現期間` — return period. Paste the native term into the portal; the English text is only a meaning guide.

| Website root | Related source IDs | Publisher(s) | Search this site for | Link roles | Current classification |
|---|---|---|---|---|---|
| [disaportal.gsi.go.jp](https://disaportal.gsi.go.jp/) | JP-MLIT-001 | 国土交通省 / Ministry of Land, Infrastructure, Transport and Tourism | `ハザードマップポータルサイト` | primary, verification final, selected access | confirmed dataset access |
| [nlftp.mlit.go.jp](https://nlftp.mlit.go.jp/) | JP-MLIT-002 | 国土交通省 国土数値情報 | `洪水浸水想定区域データ` | primary, verification final, selected access | confirmed dataset access |
| [www.kensetsu.metro.tokyo.lg.jp](https://www.kensetsu.metro.tokyo.lg.jp/) | JP-TKY-001 | 東京都建設局 | `洪水浸水想定区域図` | primary, verification final | unavailable candidate |
| [www.pref.aichi.jp](https://www.pref.aichi.jp/) | JP-AIC-001 | 愛知県 | `洪水浸水想定区域図` | primary, verification final | unavailable candidate |
| [www.pref.kanagawa.jp](https://www.pref.kanagawa.jp/) | JP-KNG-001 | 神奈川県 | `洪水浸水想定区域図` | primary, verification final, selected access | confirmed dataset access |
| [www.pref.osaka.lg.jp](https://www.pref.osaka.lg.jp/) | JP-OSK-001 | 大阪府 | `洪水浸水想定区域図` | primary, verification final | unavailable candidate |
| [www.pref.saitama.lg.jp](https://www.pref.saitama.lg.jp/) | JP-SAI-001 | 埼玉県 | `洪水浸水想定区域図` | primary, verification final | unavailable candidate |
| [www.river.go.jp](https://www.river.go.jp/) | JP-MLIT-003 | 国土交通省 | `川の防災情報` | primary, verification final, selected access | confirmed dataset access |
| [www.stat.go.jp](https://www.stat.go.jp/) | population: Tokyo, population: Kanagawa, population: Osaka, population: Aichi, population: Saitama | Statistics Bureau of Japan 2020 Census | `Tokyo population`<br>`Kanagawa population`<br>`Osaka population`<br>`Aichi population`<br>`Saitama population` | population source | supporting citation |

### Confirmed dataset access

Each clickable link below was confirmed to identify an authoritative flood dataset and provide a usable service, download, viewer, map document, or dataset-specific page.

| ID | Jurisdiction / agency | Dataset | Confirmed flood type | Confirmed scenarios | Confirmed coverage | Confirmed formats | Confirmed licence | Access | Link | Verified | Flags | Evidence |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| JP-KNG-001 | Kanagawa<br>神奈川県 | 洪水浸水想定区域図<br>_Kanagawa Flood Inundation Assumption Maps_ | fluvial | unknown | Kanagawa Prefecture | Dataset-specific page | unknown | Dataset page | [Primary](https://www.pref.kanagawa.jp/docs/f4i/cnt/f3747/) | 2026-06-24 | verified | Official dataset-specific page or viewer confirmed during bounded page review. |
| JP-MLIT-001 | National<br>国土交通省 / Ministry of Land, Infrastructure, Transport and Tourism | ハザードマップポータルサイト<br>_Hazard Map Portal Site_ | fluvial, coastal, surface_water, tsunami | unknown | Japan | Interactive viewer | unknown | Interactive viewer | [Primary](https://disaportal.gsi.go.jp/) | 2026-06-24 | verified | Official dataset-specific page or viewer confirmed during bounded page review. |
| JP-MLIT-002 | National<br>国土交通省 国土数値情報 | 洪水浸水想定区域データ<br>_Flood Inundation Assumption Area Data_ | fluvial | unknown | Japan; compiled prefectural/national river designations | Dataset-specific page | unknown | Dataset page | [Primary](https://nlftp.mlit.go.jp/ksj/gml/datalist/KsjTmplt-A31-v3_0.html) | 2026-06-24 | verified | Official dataset-specific page or viewer confirmed during bounded page review. |
| JP-MLIT-003 | National supporting<br>国土交通省 | 川の防災情報<br>_River Disaster Prevention Information_ | fluvial | unknown | Japan | Interactive viewer | unknown | Interactive viewer | [Primary](https://www.river.go.jp/) | 2026-06-24 | non-material, verified | Official dataset-specific page or viewer confirmed during bounded page review. |

### Unavailable candidates

These links did not resolve. URLs are plain text and non-clickable.

| ID | Jurisdiction / agency | Candidate | Status | Candidate URL | Tracking |
|---|---|---|---|---|---|
| JP-TKY-001 | Tokyo<br>東京都建設局 | 洪水浸水想定区域図 | failed (HTTP 404): No candidate link resolved successfully during the strict audit. | `https://www.kensetsu.metro.tokyo.lg.jp/jigyo/river/chusho_seibi/index/menu03-01.html` | human review |
| JP-OSK-001 | Osaka<br>大阪府 | 洪水浸水想定区域図 | failed (HTTP 404): No candidate link resolved successfully during the strict audit. | `https://www.pref.osaka.lg.jp/o130350/kasenkankyo/hazardmap/index.html` | human review |
| JP-AIC-001 | Aichi<br>愛知県 | 洪水浸水想定区域図 | failed (HTTP 404): No candidate link resolved successfully during the strict audit. | `https://www.pref.aichi.jp/soshiki/kasen/shinsuisoutei.html` | human review |
| JP-SAI-001 | Saitama<br>埼玉県 | 洪水浸水想定区域図 | failed (HTTP 404): No candidate link resolved successfully during the strict audit. | `https://www.pref.saitama.lg.jp/a1007/kouzui-sinsuisouteikuiki.html` | human review |

### What comes next

1. Resolve 4 broken or unreachable material source(s) flagged for human review (see the Unavailable table and the Human review required section).
2. Extend beyond the 5-region pilot to the 42 deferred region(s).
3. Confirm licensing for 4 confirmed source(s) whose licence is still marked "verify".

## Belgium (BE)

**Coverage model:** primarily regional · **Confidence in completeness:** medium

Flood-hazard authority is regional. Flanders publishes through Waterinfo and Geopunt, Wallonia through the flood-risk geoportal/WalOnMap, and Brussels through Bruxelles Environnement/BruGIS. All three regions are included; no regional deferral is required.

### What we have

- **Confirmed dataset access:** 3 source(s) (0 direct service/API/download, 3 viewer / map document / dataset page).
- **Investigation leads:** 2 reachable portal(s) that still need the dataset located by hand.
- **Unavailable:** 1 broken or unreachable candidate(s).
- **Hazard families confirmed:** Fluvial (river), Coastal, Surface water (pluvial).
- **Best confirmed access:** Interactive viewer, Dataset page.


### Population-priority regions

| Rank | Region | Population | Year | Source |
|---:|---|---:|---:|---|
| 1 | Flemish Region | 6,774,000 | 2024 | [Statbel population structure](https://statbel.fgov.be/en/themes/population/structure-population) |
| 2 | Walloon Region | 3,693,000 | 2024 | [Statbel population structure](https://statbel.fgov.be/en/themes/population/structure-population) |
| 3 | Brussels-Capital Region | 1,249,000 | 2024 | [Statbel population structure](https://statbel.fgov.be/en/themes/population/structure-population) |

### Portal search guide and website roots

Use the exact dataset names in the directory first. If that fails, try the local-language flood terms below in the site's search box, map-layer catalogue, or metadata search. Website-root links are navigation aids; they are not themselves confirmation that a dataset is available.

**Portal languages:** Dutch, French, German

**Country search phrases:** `overstromingsgevaarkaart` · `overstromingsdiepte` · `carte aléa inondation` · `hauteur d'eau` · `Hochwassergefahrenkarte`

**Native-language term guide:** `overstromingsgevaarkaart` — flood-hazard map · `overstromingsdiepte` — flood depth · `carte aléa inondation` — flood-hazard map · `hauteur d'eau` — water depth · `Hochwassergefahrenkarte` — flood-hazard map. Paste the native term into the portal; the English text is only a meaning guide.

| Website root | Related source IDs | Publisher(s) | Search this site for | Link roles | Current classification |
|---|---|---|---|---|---|
| [environnement.brussels](https://environnement.brussels/) | BE-BRU-001 | Bruxelles Environnement | `Carte d'aléa et de risque d'inondation` | primary, verification final | unavailable candidate |
| [environnement.wallonie.be](https://environnement.wallonie.be/) | BE-WAL-002 | Service public de Wallonie | `Portail Inondations en Wallonie` | verification final, selected access | confirmed dataset access |
| [geoportail.wallonie.be](https://geoportail.wallonie.be/) | BE-WAL-001 | Service public de Wallonie | `Cartographie de l'aléa d'inondation` | primary, verification final, selected access | investigation lead |
| [inondations.wallonie.be](https://inondations.wallonie.be/) | BE-WAL-002 | Service public de Wallonie | `Portail Inondations en Wallonie` | primary | confirmed dataset access |
| [statbel.fgov.be](https://statbel.fgov.be/) | population: Flemish Region, population: Walloon Region, population: Brussels-Capital Region | Statbel population structure | `Flemish Region population`<br>`Walloon Region population`<br>`Brussels-Capital Region population` | population source | supporting citation |
| [water.europa.eu](https://water.europa.eu/) | BE-EEA-001 | European Environment Agency | `WISE Floods Directive` | primary, verification final, selected access | confirmed dataset access |
| [waterinfo.vlaanderen.be](https://waterinfo.vlaanderen.be/) | BE-VLG-001 | Vlaamse Milieumaatschappij | `Overstromingskaarten Waterinfo` | verification final, selected access | confirmed dataset access |
| [www.geopunt.be](https://www.geopunt.be/) | BE-VLG-002 | Digitaal Vlaanderen | `Geopunt - Overstromingsgevoelige gebieden` | primary, verification final, selected access | investigation lead |
| [www.waterinfo.be](https://www.waterinfo.be/) | BE-VLG-001 | Vlaamse Milieumaatschappij | `Overstromingskaarten Waterinfo` | primary | confirmed dataset access |

### Confirmed dataset access

Each clickable link below was confirmed to identify an authoritative flood dataset and provide a usable service, download, viewer, map document, or dataset-specific page.

| ID | Jurisdiction / agency | Dataset | Confirmed flood type | Confirmed scenarios | Confirmed coverage | Confirmed formats | Confirmed licence | Access | Link | Verified | Flags | Evidence |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| BE-EEA-001 | National fallback<br>European Environment Agency | WISE Floods Directive | fluvial, coastal | unknown | Belgium | Dataset-specific page | EEA reuse policy | Dataset page | [Primary](https://water.europa.eu/freshwater/europe-freshwater/floods-directive) | 2026-06-24 | fallback, non-material, verified | Official dataset-specific page or viewer confirmed during bounded page review. |
| BE-VLG-001 | Flemish Region<br>Vlaamse Milieumaatschappij | Overstromingskaarten Waterinfo<br>_Flanders Flood Maps_ | fluvial, coastal, surface_water | small/medium/large probability, climate scenarios, depth candidates | Flemish Region | Interactive viewer | unknown | Interactive viewer | [Primary](https://waterinfo.vlaanderen.be/overstromingsrichtlijn) | 2026-06-24 | verified | Official dataset-specific page or viewer confirmed during bounded page review. |
| BE-WAL-002 | Walloon Region<br>Service public de Wallonie | Portail Inondations en Wallonie<br>_Wallonia Flood Portal_ | fluvial, surface_water | unknown | Walloon Region | Dataset-specific page | unknown | Dataset page | [Primary](https://environnement.wallonie.be/home/gestion-environnementale/risques-climatiques/inondations.html) | 2026-06-24 | verified | Official dataset-specific page or viewer confirmed during bounded page review. |

### Reachable investigation leads

These links resolve, but they are generic portals, catalogue searches, restricted/request-only paths, ambiguous products, or otherwise lack confirmed dataset-specific access. They are clickable for investigation but excluded from scoring.

| ID | Jurisdiction / agency | Candidate | Access | Link | Reason | Tracking |
|---|---|---|---|---|---|---|
| BE-VLG-002 | Flemish Region<br>Digitaal Vlaanderen | Geopunt - Overstromingsgevoelige gebieden | Catalogue search | [Open](https://www.geopunt.be/) | The link is a catalogue/search entry point rather than a dataset-specific record. | human review |
| BE-WAL-001 | Walloon Region<br>Service public de Wallonie | Cartographie de l'aléa d'inondation | Catalogue search | [Open](https://geoportail.wallonie.be/walonmap) | The link is a catalogue/search entry point rather than a dataset-specific record. | human review |

### Unavailable candidates

These links did not resolve. URLs are plain text and non-clickable.

| ID | Jurisdiction / agency | Candidate | Status | Candidate URL | Tracking |
|---|---|---|---|---|---|
| BE-BRU-001 | Brussels-Capital Region<br>Bruxelles Environnement | Carte d'aléa et de risque d'inondation | failed (HTTP 404): No candidate link resolved successfully during the strict audit. | `https://environnement.brussels/citoyen/outils-et-donnees/cartes/les-cartes-relatives-aux-inondations-pour-la-region-bruxelloise` | human review |

### What comes next

1. Work the 2 investigation lead(s): use the portal search guide below to locate the dataset behind each portal, then confirm a usable service, download, viewer, or dataset page.
2. Resolve 1 broken or unreachable material source(s) flagged for human review (see the Unavailable table and the Human review required section).
3. Confirm licensing for 2 confirmed source(s) whose licence is still marked "verify".

## Italy (IT)

**Coverage model:** national catalogue with regional publishers · **Scope:** provisional — top-five-region pilot · **Confidence in completeness:** medium

ISPRA's IdroGEO provides national harmonized flood-hazard and risk viewing, while authoritative Floods Directive mapping is produced by district basin authorities and regions. The top-five-region pilot maps Lombardia to the Po district, Lazio to Central Apennines, Campania to Southern Apennines, Veneto to Eastern Alps and Sicilia to the Sicilian district authority.

### What we have

- **Confirmed dataset access:** 3 source(s) (0 direct service/API/download, 3 viewer / map document / dataset page).
- **Investigation leads:** 1 reachable portal(s) that still need the dataset located by hand.
- **Unavailable:** 4 broken or unreachable candidate(s).
- **Hazard families confirmed:** Fluvial (river), Coastal. **Not yet confirmed:** Surface water (pluvial).
- **Best confirmed access:** Interactive viewer, Dataset page.


### Population-priority regions

| Rank | Region | Population | Year | Source |
|---:|---|---:|---:|---|
| 1 | Lombardia | 10,020,000 | 2024 | [ISTAT resident population](https://demo.istat.it/) |
| 2 | Lazio | 5,720,000 | 2024 | [ISTAT resident population](https://demo.istat.it/) |
| 3 | Campania | 5,590,000 | 2024 | [ISTAT resident population](https://demo.istat.it/) |
| 4 | Veneto | 4,850,000 | 2024 | [ISTAT resident population](https://demo.istat.it/) |
| 5 | Sicilia | 4,790,000 | 2024 | [ISTAT resident population](https://demo.istat.it/) |

**Deferred regions:** Abruzzo, Basilicata, Calabria, Emilia-Romagna, Friuli-Venezia Giulia, Liguria, Marche, Molise, Piemonte, Puglia, Sardegna, Toscana, Trentino-Alto Adige, Umbria, Valle d'Aosta

### Portal search guide and website roots

Use the exact dataset names in the directory first. If that fails, try the local-language flood terms below in the site's search box, map-layer catalogue, or metadata search. Website-root links are navigation aids; they are not themselves confirmation that a dataset is available.

**Portal languages:** Italian

**Country search phrases:** `mappa pericolosità alluvioni` · `area allagabile` · `tirante idrico` · `velocità` · `tempo di ritorno` · `allagamento urbano` · `pericolosità da pioggia intensa` · `pluvial flood map` · `rischio allagamenti`

**Native-language term guide:** `mappa pericolosità alluvioni` — flood-hazard map · `area allagabile` — floodable area · `tirante idrico` — water depth · `velocità` — velocity · `tempo di ritorno` — return period · `allagamento urbano` — urban flooding · `pericolosità da pioggia intensa` — heavy-rain hazard · `rischio allagamenti` — flooding risk. Paste the native term into the portal; the English text is only a meaning guide.

| Website root | Related source IDs | Publisher(s) | Search this site for | Link roles | Current classification |
|---|---|---|---|---|---|
| [demo.istat.it](https://demo.istat.it/) | population: Lombardia, population: Lazio, population: Campania, population: Veneto, population: Sicilia | ISTAT resident population | `Lombardia population`<br>`Lazio population`<br>`Campania population`<br>`Veneto population`<br>`Sicilia population` | population source | supporting citation |
| [distrettoalpiorientali.it](https://distrettoalpiorientali.it/) | IT-AO-001 | Autorità di bacino distrettuale delle Alpi Orientali | `PGRA - Mappe della pericolosità e del rischio` | primary | unavailable candidate |
| [idrogeo.isprambiente.it](https://idrogeo.isprambiente.it/) | IT-ISPRA-001 | Istituto Superiore per la Protezione e la Ricerca Ambientale | `IdroGEO - Piattaforma italiana sul dissesto idrogeologico` | primary, verification final, selected access | confirmed dataset access |
| [pgt.comune.milano.it](https://pgt.comune.milano.it/) | IT-MI-001 | Comune di Milano - PGT Componente Geologica | `Documento Semplificato del Rischio Idraulico / Carta del Rischio Idraulico` | primary, verification final | unavailable candidate |
| [water.europa.eu](https://water.europa.eu/) | IT-EEA-001 | European Environment Agency | `WISE Floods Directive` | primary, verification final, selected access | confirmed dataset access |
| [www.adbpo.it](https://www.adbpo.it/) | IT-ADBPO-001 | Autorità di bacino distrettuale del fiume Po | `PGRA - Mappe della pericolosità e del rischio di alluvioni` | primary, verification final, selected access | confirmed dataset access |
| [www.autoritadistrettoac.it](https://www.autoritadistrettoac.it/) | IT-AC-001 | Autorità di bacino distrettuale dell'Appennino Centrale | `PGRAAC - Mappe di pericolosità e rischio` | primary | unavailable candidate |
| [www.distrettoappenninomeridionale.it](https://www.distrettoappenninomeridionale.it/) | IT-AM-001 | Autorità di bacino distrettuale dell'Appennino Meridionale | `PGRA - Piano di Gestione del Rischio di Alluvioni` | primary, verification final | unavailable candidate |
| [www.regione.sicilia.it](https://www.regione.sicilia.it/) | IT-SIC-001 | Autorità di bacino del Distretto Idrografico della Sicilia | `Piano di Gestione del Rischio di Alluvioni` | primary, verification final, selected access | investigation lead |

### Confirmed dataset access

Each clickable link below was confirmed to identify an authoritative flood dataset and provide a usable service, download, viewer, map document, or dataset-specific page.

| ID | Jurisdiction / agency | Dataset | Confirmed flood type | Confirmed scenarios | Confirmed coverage | Confirmed formats | Confirmed licence | Access | Link | Verified | Flags | Evidence |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| IT-ADBPO-001 | Lombardia / Po basin<br>Autorità di bacino distrettuale del fiume Po | PGRA - Mappe della pericolosità e del rischio di alluvioni<br>_Po District Flood Hazard and Risk Maps_ | fluvial | unknown | Po River district including Lombardia | Dataset-specific page | unknown | Dataset page | [Primary](https://www.adbpo.it/) | 2026-06-24 | verified | Official dataset-specific page or viewer confirmed during bounded page review. |
| IT-EEA-001 | National fallback<br>European Environment Agency | WISE Floods Directive | fluvial, coastal | unknown | Italy | Dataset-specific page | EEA reuse policy | Dataset page | [Primary](https://water.europa.eu/freshwater/europe-freshwater/floods-directive) | 2026-06-24 | fallback, non-material, verified | Official dataset-specific page or viewer confirmed during bounded page review. |
| IT-ISPRA-001 | National<br>Istituto Superiore per la Protezione e la Ricerca Ambientale | IdroGEO - Piattaforma italiana sul dissesto idrogeologico<br>_IdroGEO National Hydrogeological Hazard Platform_ | fluvial, coastal | unknown | Italy | Interactive viewer | unknown | Interactive viewer | [Primary](https://idrogeo.isprambiente.it/app/) | 2026-06-24 | verified | Official dataset-specific page or viewer confirmed during bounded page review. |

### Reachable investigation leads

These links resolve, but they are generic portals, catalogue searches, restricted/request-only paths, ambiguous products, or otherwise lack confirmed dataset-specific access. They are clickable for investigation but excluded from scoring.

| ID | Jurisdiction / agency | Candidate | Access | Link | Reason | Tracking |
|---|---|---|---|---|---|---|
| IT-SIC-001 | Sicilia<br>Autorità di bacino del Distretto Idrografico della Sicilia | Piano di Gestione del Rischio di Alluvioni | Ambiguous | [Open](https://www.regione.sicilia.it/istituzioni/regione/strutture-regionali/presidenza-regione/autorita-bacino-distretto-idrografico-sicilia) | The page resolves, but dataset identity or usable access could not be confirmed. | human review |

### Unavailable candidates

These links did not resolve. URLs are plain text and non-clickable.

| ID | Jurisdiction / agency | Candidate | Status | Candidate URL | Tracking |
|---|---|---|---|---|---|
| IT-AC-001 | Lazio / Central Apennines<br>Autorità di bacino distrettuale dell'Appennino Centrale | PGRAAC - Mappe di pericolosità e rischio | failed (unreachable): No candidate link resolved successfully during the strict audit. | `https://www.autoritadistrettoac.it/pianificazione/pianificazione-distrettuale/pgra/` | human review |
| IT-AM-001 | Campania / Southern Apennines<br>Autorità di bacino distrettuale dell'Appennino Meridionale | PGRA - Piano di Gestione del Rischio di Alluvioni | failed (HTTP 404): No candidate link resolved successfully during the strict audit. | `https://www.distrettoappenninomeridionale.it/index.php/pgra` | human review |
| IT-AO-001 | Veneto / Eastern Alps<br>Autorità di bacino distrettuale delle Alpi Orientali | PGRA - Mappe della pericolosità e del rischio | failed (unreachable): No candidate link resolved successfully during the strict audit. | `https://distrettoalpiorientali.it/piano-gestione-rischio-alluvioni/` | human review |
| IT-MI-001 | Comune di Milano (Lombardia)<br>Comune di Milano - PGT Componente Geologica | Documento Semplificato del Rischio Idraulico / Carta del Rischio Idraulico | failed (HTTP 403): The official page returned HTTP 403; public dataset usability could not be confirmed. | `https://pgt.comune.milano.it/gall08-documento-semplificato-del-rischio-idraulico` | human review |

### What comes next

1. Confirm Surface water (pluvial) coverage — a candidate exists but its dataset is not yet confirmed.
2. Work the 1 investigation lead(s): use the portal search guide below to locate the dataset behind each portal, then confirm a usable service, download, viewer, or dataset page.
3. Resolve 4 broken or unreachable material source(s) flagged for human review (see the Unavailable table and the Human review required section).
4. Extend beyond the 5-region pilot to the 15 deferred region(s).
5. Confirm licensing for 2 confirmed source(s) whose licence is still marked "verify".

## Switzerland (CH)

**Coverage model:** national catalogue with regional publishers · **Scope:** provisional — top-five-region pilot · **Confidence in completeness:** medium

Switzerland combines federal national hazard layers with canton-level statutory natural-hazard maps. Surface-water runoff has a national federal layer, while detailed fluvial hazard maps remain cantonal. Coastal flood hazard is N/A because Switzerland is landlocked.

### What we have

- **Confirmed dataset access:** 2 source(s) (0 direct service/API/download, 2 viewer / map document / dataset page).
- **Investigation leads:** 4 reachable portal(s) that still need the dataset located by hand.
- **Unavailable:** 1 broken or unreachable candidate(s).
- **Hazard families confirmed:** Fluvial (river), Surface water (pluvial). **Not yet confirmed:** Coastal.
- **Best confirmed access:** Interactive viewer, Dataset page.


### Population-priority regions

| Rank | Region | Population | Year | Source |
|---:|---|---:|---:|---|
| 1 | Zürich | 1,601,434 | 2023 | [Swiss Federal Statistical Office population by canton](https://www.bfs.admin.ch/bfs/en/home/statistics/population/effectif-change.html) |
| 2 | Bern | 1,063,533 | 2023 | [Swiss Federal Statistical Office population by canton](https://www.bfs.admin.ch/bfs/en/home/statistics/population/effectif-change.html) |
| 3 | Vaud | 846,300 | 2023 | [Swiss Federal Statistical Office population by canton](https://www.bfs.admin.ch/bfs/en/home/statistics/population/effectif-change.html) |
| 4 | Aargau | 727,235 | 2023 | [Swiss Federal Statistical Office population by canton](https://www.bfs.admin.ch/bfs/en/home/statistics/population/effectif-change.html) |
| 5 | St. Gallen | 526,792 | 2023 | [Swiss Federal Statistical Office population by canton](https://www.bfs.admin.ch/bfs/en/home/statistics/population/effectif-change.html) |

**Deferred regions:** Appenzell Ausserrhoden, Appenzell Innerrhoden, Basel-Landschaft, Basel-Stadt, Fribourg, Geneva, Glarus, Graubünden, Jura, Luzern, Neuchâtel, Nidwalden, Obwalden, Schaffhausen, Schwyz, Solothurn, Thurgau, Ticino, Uri, Valais, Zug

### Portal search guide and website roots

Use the exact dataset names in the directory first. If that fails, try the local-language flood terms below in the site's search box, map-layer catalogue, or metadata search. Website-root links are navigation aids; they are not themselves confirmation that a dataset is available.

**Portal languages:** German, French, Italian, Romansh

**Country search phrases:** `Hochwassergefahrenkarte` · `Überflutungstiefe` · `carte des dangers crues` · `mappa pericolo alluvione` · `Wiederkehrperiode`

**Native-language term guide:** `Hochwassergefahrenkarte` — flood-hazard map · `Überflutungstiefe` — inundation depth · `carte des dangers crues` — river-flood hazard map · `mappa pericolo alluvione` — flood-hazard map · `Wiederkehrperiode` — return period. Paste the native term into the portal; the English text is only a meaning guide.

| Website root | Related source IDs | Publisher(s) | Search this site for | Link roles | Current classification |
|---|---|---|---|---|---|
| [map.geo.admin.ch](https://map.geo.admin.ch/) | CH-BAFU-001 | Bundesamt für Umwelt (BAFU) | `Gefährdungskarte Oberflächenabfluss` | primary, verification final, selected access | confirmed dataset access |
| [maps.zh.ch](https://maps.zh.ch/) | CH-ZH-001 | Kanton Zürich | `Naturgefahrenkarte Hochwasser` | primary, verification final, selected access | investigation lead |
| [www.ag.ch](https://www.ag.ch/) | CH-AG-001 | Kanton Aargau | `Gefahrenkarte Hochwasser` | primary, verification final, selected access | investigation lead |
| [www.bafu.admin.ch](https://www.bafu.admin.ch/) | CH-BAFU-002 | Bundesamt für Umwelt (BAFU) | `Gefahrenkarten, Intensitätskarten und Gefahrenhinweiskarten` | primary, verification final, selected access | confirmed dataset access |
| [www.bfs.admin.ch](https://www.bfs.admin.ch/) | population: Zürich, population: Bern, population: Vaud, population: Aargau, population: St. Gallen | Swiss Federal Statistical Office population by canton | `Zürich population`<br>`Bern population`<br>`Vaud population`<br>`Aargau population`<br>`St. Gallen population` | population source | supporting citation |
| [www.geo.apps.be.ch](https://www.geo.apps.be.ch/) | CH-BE-001 | Kanton Bern | `Gefahrenkarte Naturgefahren - Hochwasser` | primary | unavailable candidate |
| [www.geo.vd.ch](https://www.geo.vd.ch/) | CH-VD-001 | État de Vaud | `Cartes de dangers naturels - inondations` | primary, verification final, selected access | investigation lead |
| [www.geoportal.ch](https://www.geoportal.ch/) | CH-SG-001 | Kanton St. Gallen | `Naturgefahrenkarte Wasser` | primary, verification final, selected access | investigation lead |

### Confirmed dataset access

Each clickable link below was confirmed to identify an authoritative flood dataset and provide a usable service, download, viewer, map document, or dataset-specific page.

| ID | Jurisdiction / agency | Dataset | Confirmed flood type | Confirmed scenarios | Confirmed coverage | Confirmed formats | Confirmed licence | Access | Link | Verified | Flags | Evidence |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| CH-BAFU-001 | National<br>Bundesamt für Umwelt (BAFU) | Gefährdungskarte Oberflächenabfluss<br>_Surface Runoff Hazard Map_ | surface_water | unknown | Switzerland | Interactive viewer | unknown | Interactive viewer | [Primary](https://map.geo.admin.ch/?layers=ch.bafu.gefaehrdungskarte-oberflaechenabfluss) | 2026-06-24 | verified | Official dataset-specific page or viewer confirmed during bounded page review. |
| CH-BAFU-002 | National<br>Bundesamt für Umwelt (BAFU) | Gefahrenkarten, Intensitätskarten und Gefahrenhinweiskarten<br>_Hazard, Intensity and Hazard-Indication Maps_ | fluvial, flash_flood, other | unknown | Switzerland; authoritative detailed maps are cantonal | Dataset-specific page | unknown | Dataset page | [Primary](https://www.bafu.admin.ch/de/naturgefahren) | 2026-06-24 | verified | Official dataset-specific page or viewer confirmed during bounded page review. |

### Reachable investigation leads

These links resolve, but they are generic portals, catalogue searches, restricted/request-only paths, ambiguous products, or otherwise lack confirmed dataset-specific access. They are clickable for investigation but excluded from scoring.

| ID | Jurisdiction / agency | Candidate | Access | Link | Reason | Tracking |
|---|---|---|---|---|---|---|
| CH-ZH-001 | Zürich<br>Kanton Zürich | Naturgefahrenkarte Hochwasser | Generic portal | [Open](https://maps.zh.ch/) | The link is a generic agency or geoportal entry point; the named dataset was not resolved. | human review |
| CH-VD-001 | Vaud<br>État de Vaud | Cartes de dangers naturels - inondations | Generic portal | [Open](https://www.geo.vd.ch/) | The link is a generic agency or geoportal entry point; the named dataset was not resolved. | human review |
| CH-AG-001 | Aargau<br>Kanton Aargau | Gefahrenkarte Hochwasser | Ambiguous | [Open](https://www.ag.ch/geoportal/apps/onlinekarten/?welcome) | The page resolves, but dataset identity or usable access could not be confirmed. | human review |
| CH-SG-001 | St. Gallen<br>Kanton St. Gallen | Naturgefahrenkarte Wasser | Generic portal | [Open](https://www.geoportal.ch/) | The link is a generic agency or geoportal entry point; the named dataset was not resolved. | human review |

### Unavailable candidates

These links did not resolve. URLs are plain text and non-clickable.

| ID | Jurisdiction / agency | Candidate | Status | Candidate URL | Tracking |
|---|---|---|---|---|---|
| CH-BE-001 | Bern<br>Kanton Bern | Gefahrenkarte Naturgefahren - Hochwasser | failed (unreachable): No candidate link resolved successfully during the strict audit. | `https://www.geo.apps.be.ch/` | human review |

### What comes next

1. Find Coastal coverage, or document in the summary above why the family does not apply.
2. Work the 4 investigation lead(s): use the portal search guide below to locate the dataset behind each portal, then confirm a usable service, download, viewer, or dataset page.
3. Resolve 1 broken or unreachable material source(s) flagged for human review (see the Unavailable table and the Human review required section).
4. Extend beyond the 5-region pilot to the 21 deferred region(s).
5. Confirm licensing for 2 confirmed source(s) whose licence is still marked "verify".

## Ireland (IE)

**Coverage model:** nationally unified · **Confidence in completeness:** medium

The Office of Public Works publishes nationally coordinated CFRAM predictive flood maps and historical flood records through Floodinfo.ie. Detailed mapping is catchment- and area-based but uses a unified national portal and common scenario framework.

### What we have

- **Confirmed dataset access:** 4 source(s) (0 direct service/API/download, 4 viewer / map document / dataset page).
- **Investigation leads:** 2 reachable portal(s) that still need the dataset located by hand.
- **Unavailable:** 0 broken or unreachable candidate(s).
- **Hazard families confirmed:** Fluvial (river), Coastal, Surface water (pluvial).
- **Best confirmed access:** Interactive viewer.


### Portal search guide and website roots

Use the exact dataset names in the directory first. If that fails, try the local-language flood terms below in the site's search box, map-layer catalogue, or metadata search. Website-root links are navigation aids; they are not themselves confirmation that a dataset is available.

**Portal languages:** Irish, English

**Country search phrases:** `flood hazard map` · `flood extent` · `flood depth` · `return period` · `léarscáil tuilte` · `pluvial flood map` · `surface water flood` · `rainfall flood map`

**Native-language term guide:** `léarscáil tuilte` — flood map. Paste the native term into the portal; the English text is only a meaning guide.

| Website root | Related source IDs | Publisher(s) | Search this site for | Link roles | Current classification |
|---|---|---|---|---|---|
| [data.gov.ie](https://data.gov.ie/) | IE-DATA-001 | Office of Public Works / data.gov.ie | `Flood Maps datasets` | primary, verification final, selected access | investigation lead |
| [gis.epa.ie](https://gis.epa.ie/) | IE-EPA-001 | Environmental Protection Agency Ireland | `Geoportal - Flood and water layers` | primary, verification final, selected access | investigation lead |
| [water.europa.eu](https://water.europa.eu/) | IE-EEA-001 | European Environment Agency | `WISE Floods Directive` | primary, verification final, selected access | confirmed dataset access |
| [www.floodinfo.ie](https://www.floodinfo.ie/) | IE-OPW-001, IE-OPW-002, IE-OPW-003 | Office of Public Works; Office of Public Works (OPW) | `CFRAM Flood Maps`<br>`National Flood Hazard Mapping`<br>`OPW Flood Maps - CFRAM Rainfall (Pluvial) Flood Extents` | primary, verification final, selected access | confirmed dataset access |

### Confirmed dataset access

Each clickable link below was confirmed to identify an authoritative flood dataset and provide a usable service, download, viewer, map document, or dataset-specific page.

| ID | Jurisdiction / agency | Dataset | Confirmed flood type | Confirmed scenarios | Confirmed coverage | Confirmed formats | Confirmed licence | Access | Link | Verified | Flags | Evidence |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| IE-EEA-001 | National fallback<br>European Environment Agency | WISE Floods Directive | fluvial, coastal | unknown | Ireland | Dataset-specific page | EEA reuse policy | Dataset page | [Primary](https://water.europa.eu/freshwater/europe-freshwater/floods-directive) | 2026-06-24 | fallback, non-material, verified | Official dataset-specific page or viewer confirmed during bounded page review. |
| IE-OPW-001 | National<br>Office of Public Works | CFRAM Flood Maps<br>_CFRAM Predictive Flood Maps_ | fluvial, coastal | 10% AEP, 1% AEP, 0.1% AEP fluvial, 10%/0.5%/0.1% coastal candidates, climate scenarios, depth candidate | Republic of Ireland; modelled areas and APSFRs | Interactive viewer | unknown | Interactive viewer | [Primary](https://www.floodinfo.ie/map/floodmaps/) | 2026-06-24 | verified | Official dataset-specific page or viewer confirmed during bounded page review. |
| IE-OPW-002 | National<br>Office of Public Works | National Flood Hazard Mapping<br>_National Flood Hazard Mapping Archive_ | historic, fluvial, coastal, surface_water | unknown | Republic of Ireland | Interactive viewer | unknown | Interactive viewer | [Primary](https://www.floodinfo.ie/map/floodmaps/) | 2026-06-24 | non-material, verified | Official dataset-specific page or viewer confirmed during bounded page review. |
| IE-OPW-003 | National<br>Office of Public Works (OPW) | OPW Flood Maps - CFRAM Rainfall (Pluvial) Flood Extents<br>_OPW Pluvial / Rainfall Flood Maps_ | surface_water | 10% AEP, 1% AEP, 0.1% AEP, present-day and future rainfall (+20%/+30%) climate scenarios | Republic of Ireland; pluvial mapping for selected AFAs/urban areas (e.g. Dublin) plus CFRAM rainfall flood extents in the national viewer | Interactive viewer | unknown | Interactive viewer | [Primary](https://www.floodinfo.ie/map/floodmaps/) | 2026-06-24 | verified | Official dataset-specific page or viewer confirmed during bounded page review. |

### Reachable investigation leads

These links resolve, but they are generic portals, catalogue searches, restricted/request-only paths, ambiguous products, or otherwise lack confirmed dataset-specific access. They are clickable for investigation but excluded from scoring.

| ID | Jurisdiction / agency | Candidate | Access | Link | Reason | Tracking |
|---|---|---|---|---|---|---|
| IE-DATA-001 | National<br>Office of Public Works / data.gov.ie | Flood Maps datasets | Catalogue search | [Open](https://data.gov.ie/dataset/?q=flood+maps) | The link is a catalogue/search entry point rather than a dataset-specific record. | human review |
| IE-EPA-001 | National supporting<br>Environmental Protection Agency Ireland | Geoportal - Flood and water layers | Ambiguous | [Open](https://gis.epa.ie/EPAMaps/) | The page resolves, but dataset identity or usable access could not be confirmed. | non-material candidate |

### What comes next

1. Work the 2 investigation lead(s): use the portal search guide below to locate the dataset behind each portal, then confirm a usable service, download, viewer, or dataset page.
2. Confirm licensing for 3 confirmed source(s) whose licence is still marked "verify".

## Thailand (TH)

**Coverage model:** mixed national and regional · **Scope:** provisional — top-five-region pilot · **Confidence in completeness:** low

National agencies publish monitoring, satellite inundation and water-resource risk information, while static hazard maps are spread across Department of Water Resources projects, GISTDA products, Bangkok systems and provincial disaster plans. The pilot covers Bangkok, Nakhon Ratchasima, Ubon Ratchathani, Chiang Mai and Khon Kaen.

### What we have

- **Confirmed dataset access:** 0 source(s) (0 direct service/API/download, 0 viewer / map document / dataset page).
- **Investigation leads:** 3 reachable portal(s) that still need the dataset located by hand.
- **Unavailable:** 7 broken or unreachable candidate(s).
- **Hazard families confirmed:** none. **Not yet confirmed:** Fluvial (river), Coastal, Surface water (pluvial).
- **Best confirmed access:** No confirmed dataset access.


### Population-priority regions

| Rank | Region | Population | Year | Source |
|---:|---|---:|---:|---|
| 1 | Bangkok | 5,494,000 | 2023 | [Thailand official registration statistics / NSO](https://www.nso.go.th/nsoweb/nso/statistical_system) |
| 2 | Nakhon Ratchasima | 2,630,000 | 2023 | [Thailand official registration statistics / NSO](https://www.nso.go.th/nsoweb/nso/statistical_system) |
| 3 | Ubon Ratchathani | 1,870,000 | 2023 | [Thailand official registration statistics / NSO](https://www.nso.go.th/nsoweb/nso/statistical_system) |
| 4 | Chiang Mai | 1,790,000 | 2023 | [Thailand official registration statistics / NSO](https://www.nso.go.th/nsoweb/nso/statistical_system) |
| 5 | Khon Kaen | 1,780,000 | 2023 | [Thailand official registration statistics / NSO](https://www.nso.go.th/nsoweb/nso/statistical_system) |

**Deferred regions:** Remaining provinces outside the top-five population pilot

### Portal search guide and website roots

Use the exact dataset names in the directory first. If that fails, try the local-language flood terms below in the site's search box, map-layer catalogue, or metadata search. Website-root links are navigation aids; they are not themselves confirmation that a dataset is available.

**Portal languages:** Thai

**Country search phrases:** `แผนที่เสี่ยงน้ำท่วม` · `พื้นที่น้ำท่วม` · `ความลึกน้ำท่วม` · `ความเร็วการไหล` · `คาบอุบัติซ้ำ` · `coastal flood map` · `storm surge map` · `แผนที่น้ำท่วมชายฝั่ง` · `coastal inundation`

**Native-language term guide:** `แผนที่เสี่ยงน้ำท่วม` — flood-risk map · `พื้นที่น้ำท่วม` — flooded / inundation area · `ความลึกน้ำท่วม` — flood depth · `ความเร็วการไหล` — flow velocity · `คาบอุบัติซ้ำ` — return period · `แผนที่น้ำท่วมชายฝั่ง` — coastal-flood map. Paste the native term into the portal; the English text is only a meaning guide.

| Website root | Related source IDs | Publisher(s) | Search this site for | Link roles | Current classification |
|---|---|---|---|---|---|
| [data.jrc.ec.europa.eu](https://data.jrc.ec.europa.eu/) | TH-JRC-001 | European Commission Joint Research Centre | `Global River Flood Hazard Maps` | primary, verification final, selected access | investigation lead |
| [disaster.gistda.or.th](https://disaster.gistda.or.th/) | TH-GISTDA-001 | สำนักงานพัฒนาเทคโนโลยีอวกาศและภูมิสารสนเทศ | `ระบบติดตามสถานการณ์ภัยพิบัติ - น้ำท่วม` | primary | unavailable candidate |
| [mekhala.dwr.go.th](https://mekhala.dwr.go.th/) | TH-DWR-001 | กรมทรัพยากรน้ำ / Department of Water Resources | `ระบบภูมิสารสนเทศทรัพยากรน้ำและแผนที่เสี่ยงน้ำท่วม` | primary, verification final, selected access | investigation lead |
| [tcs.dmcr.go.th](https://tcs.dmcr.go.th/) | TH-DMCR-001 | Department of Marine and Coastal Resources (DMCR) | `ระบบฐานข้อมูลเชิงพื้นที่การเปลี่ยนแปลงพื้นที่ชายฝั่งทะเลไทย` | primary, verification final | unavailable candidate |
| [weather.bangkok.go.th](https://weather.bangkok.go.th/) | TH-BKK-001 | Bangkok Metropolitan Administration | `ระบบตรวจวัดและเตือนภัยน้ำท่วมกรุงเทพมหานคร` | primary | unavailable candidate |
| [www.disaster.go.th](https://www.disaster.go.th/) | TH-NMA-001, TH-UBN-001, TH-CMI-001, TH-KKN-001 | Department of Disaster Prevention and Mitigation / provincial authorities | `แผนที่เสี่ยงอุทกภัย จังหวัดนครราชสีมา`<br>`แผนที่เสี่ยงอุทกภัย จังหวัดอุบลราชธานี`<br>`แผนที่เสี่ยงอุทกภัย จังหวัดเชียงใหม่`<br>`แผนที่เสี่ยงอุทกภัย จังหวัดขอนแก่น` | primary, verification final | unavailable candidate |
| [www.nso.go.th](https://www.nso.go.th/) | population: Bangkok, population: Nakhon Ratchasima, population: Ubon Ratchathani, population: Chiang Mai, population: Khon Kaen | Thailand official registration statistics / NSO | `Bangkok population`<br>`Nakhon Ratchasima population`<br>`Ubon Ratchathani population`<br>`Chiang Mai population`<br>`Khon Kaen population` | population source | supporting citation |
| [www.thaiwater.net](https://www.thaiwater.net/) | TH-THAIWATER-001 | Hydro-Informatics Institute | `ThaiWater` | primary, verification final, selected access | investigation lead |

### Confirmed dataset access

Each clickable link below was confirmed to identify an authoritative flood dataset and provide a usable service, download, viewer, map document, or dataset-specific page.

| ID | Jurisdiction / agency | Dataset | Confirmed flood type | Confirmed scenarios | Confirmed coverage | Confirmed formats | Confirmed licence | Access | Link | Verified | Flags | Evidence |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| _none_ | — | — | — | — | — | — | — | — | — | — | — | — |

### Reachable investigation leads

These links resolve, but they are generic portals, catalogue searches, restricted/request-only paths, ambiguous products, or otherwise lack confirmed dataset-specific access. They are clickable for investigation but excluded from scoring.

| ID | Jurisdiction / agency | Candidate | Access | Link | Reason | Tracking |
|---|---|---|---|---|---|---|
| TH-DWR-001 | National<br>กรมทรัพยากรน้ำ / Department of Water Resources | ระบบภูมิสารสนเทศทรัพยากรน้ำและแผนที่เสี่ยงน้ำท่วม | Catalogue search | [Open](https://mekhala.dwr.go.th/) | The link is a catalogue/search entry point rather than a dataset-specific record. | human review |
| TH-THAIWATER-001 | National supporting<br>Hydro-Informatics Institute | ThaiWater | Wrong product | [Open](https://www.thaiwater.net/) | The reachable product is operational or observational, not a confirmed flood-hazard dataset. | non-material candidate |
| TH-JRC-001 | National fallback<br>European Commission Joint Research Centre | Global River Flood Hazard Maps | Restricted | [Open](https://data.jrc.ec.europa.eu/collection/id-0054) | The JRC collection resolves to a login surface; unauthenticated dataset access was not confirmed. | non-material candidate |

### Unavailable candidates

These links did not resolve. URLs are plain text and non-clickable.

| ID | Jurisdiction / agency | Candidate | Status | Candidate URL | Tracking |
|---|---|---|---|---|---|
| TH-GISTDA-001 | National<br>สำนักงานพัฒนาเทคโนโลยีอวกาศและภูมิสารสนเทศ | ระบบติดตามสถานการณ์ภัยพิบัติ - น้ำท่วม | failed (unreachable): No candidate link resolved successfully during the strict audit. | `https://disaster.gistda.or.th/` | human review |
| TH-BKK-001 | Bangkok<br>Bangkok Metropolitan Administration | ระบบตรวจวัดและเตือนภัยน้ำท่วมกรุงเทพมหานคร | failed (unreachable): No candidate link resolved successfully during the strict audit. | `https://weather.bangkok.go.th/` | human review |
| TH-NMA-001 | Nakhon Ratchasima<br>Department of Disaster Prevention and Mitigation / provincial authorities | แผนที่เสี่ยงอุทกภัย จังหวัดนครราชสีมา | failed (HTTP 403): The official page returned HTTP 403; public dataset usability could not be confirmed. | `https://www.disaster.go.th/` | human review |
| TH-UBN-001 | Ubon Ratchathani<br>Department of Disaster Prevention and Mitigation / provincial authorities | แผนที่เสี่ยงอุทกภัย จังหวัดอุบลราชธานี | failed (HTTP 403): The official page returned HTTP 403; public dataset usability could not be confirmed. | `https://www.disaster.go.th/` | human review |
| TH-CMI-001 | Chiang Mai<br>Department of Disaster Prevention and Mitigation / provincial authorities | แผนที่เสี่ยงอุทกภัย จังหวัดเชียงใหม่ | failed (HTTP 403): The official page returned HTTP 403; public dataset usability could not be confirmed. | `https://www.disaster.go.th/` | human review |
| TH-KKN-001 | Khon Kaen<br>Department of Disaster Prevention and Mitigation / provincial authorities | แผนที่เสี่ยงอุทกภัย จังหวัดขอนแก่น | failed (HTTP 403): The official page returned HTTP 403; public dataset usability could not be confirmed. | `https://www.disaster.go.th/` | human review |
| TH-DMCR-001 | National<br>Department of Marine and Coastal Resources (DMCR) | ระบบฐานข้อมูลเชิงพื้นที่การเปลี่ยนแปลงพื้นที่ชายฝั่งทะเลไทย | failed (HTTP 200): No candidate link resolved successfully during the strict audit. | `https://tcs.dmcr.go.th/dmcr/v2/router?page=home` | human review |

### What comes next

1. Confirm Fluvial (river), Coastal, Surface water (pluvial) coverage — a candidate exists but its dataset is not yet confirmed.
2. Work the 3 investigation lead(s): use the portal search guide below to locate the dataset behind each portal, then confirm a usable service, download, viewer, or dataset page.
3. Resolve 7 broken or unreachable material source(s) flagged for human review (see the Unavailable table and the Human review required section).
4. Extend beyond the 5-region pilot to the 1 deferred region(s).

## Sweden (SE)

**Coverage model:** nationally unified · **Confidence in completeness:** medium

The Swedish Civil Contingencies Agency publishes nationally coordinated flood inundation mapping and Floods Directive products through Översvämningsportalen. Coverage is reach- and locality-based rather than wall-to-wall, but discovery and downloads are nationally standardized.

### What we have

- **Confirmed dataset access:** 4 source(s) (0 direct service/API/download, 4 viewer / map document / dataset page).
- **Investigation leads:** 0 reachable portal(s) that still need the dataset located by hand.
- **Unavailable:** 2 broken or unreachable candidate(s).
- **Hazard families confirmed:** Fluvial (river), Coastal, Surface water (pluvial).
- **Best confirmed access:** Interactive viewer, Dataset page.


### Portal search guide and website roots

Use the exact dataset names in the directory first. If that fails, try the local-language flood terms below in the site's search box, map-layer catalogue, or metadata search. Website-root links are navigation aids; they are not themselves confirmation that a dataset is available.

**Portal languages:** Swedish

**Country search phrases:** `översvämningskarta` · `översvämningsrisk` · `vattendjup` · `flödeshastighet` · `återkomsttid` · `skyfallskartering` · `skyfall översvämning` · `pluvial flood` · `surface water flood`

**Native-language term guide:** `översvämningskarta` — flood map · `översvämningsrisk` — flood risk · `vattendjup` — water depth · `flödeshastighet` — flow velocity · `återkomsttid` — return period · `skyfallskartering` — cloudburst mapping · `skyfall översvämning` — cloudburst flooding. Paste the native term into the portal; the English text is only a meaning guide.

| Website root | Related source IDs | Publisher(s) | Search this site for | Link roles | Current classification |
|---|---|---|---|---|---|
| [gisapp.msb.se](https://gisapp.msb.se/) | SE-MSB-001, SE-MSB-004 | Myndigheten för samhällsskydd och beredskap; Myndigheten för samhällsskydd och beredskap (MSB) | `Översvämningsportalen`<br>`Skyfallskartering / Lågpunktskartering (Översvämningsportalen)` | primary, verification final, selected access | confirmed dataset access |
| [water.europa.eu](https://water.europa.eu/) | SE-EEA-001 | European Environment Agency | `WISE Floods Directive` | primary, verification final, selected access | confirmed dataset access |
| [www.lantmateriet.se](https://www.lantmateriet.se/) | SE-LANT-001 | Lantmäteriet | `Nationell höjdmodell` | primary, verification final | unavailable candidate |
| [www.mcf.se](https://www.mcf.se/) | SE-MSB-002, SE-MSB-003 | Myndigheten för samhällsskydd och beredskap | `Översvämningskarteringar`<br>`Kartor enligt översvämningsdirektivet` | verification final, selected access | unavailable candidate, confirmed dataset access |
| [www.msb.se](https://www.msb.se/) | SE-MSB-002, SE-MSB-003 | Myndigheten för samhällsskydd och beredskap | `Översvämningskarteringar`<br>`Kartor enligt översvämningsdirektivet` | primary | unavailable candidate, confirmed dataset access |

### Confirmed dataset access

Each clickable link below was confirmed to identify an authoritative flood dataset and provide a usable service, download, viewer, map document, or dataset-specific page.

| ID | Jurisdiction / agency | Dataset | Confirmed flood type | Confirmed scenarios | Confirmed coverage | Confirmed formats | Confirmed licence | Access | Link | Verified | Flags | Evidence |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| SE-EEA-001 | National fallback<br>European Environment Agency | WISE Floods Directive | fluvial, coastal | unknown | Sweden | Dataset-specific page | EEA reuse policy | Dataset page | [Primary](https://water.europa.eu/freshwater/europe-freshwater/floods-directive) | 2026-06-24 | fallback, non-material, verified | Official dataset-specific page or viewer confirmed during bounded page review. |
| SE-MSB-001 | National<br>Myndigheten för samhällsskydd och beredskap | Översvämningsportalen<br>_Swedish Flood Portal_ | fluvial, coastal | 100-year, 200-year, highest calculated flow, climate-adjusted scenarios, depth/velocity candidates | Mapped Swedish watercourses and significant flood-risk areas | Interactive viewer | unknown | Interactive viewer | [Primary](https://gisapp.msb.se/apps/oversvamningsportal/index.html) | 2026-06-24 | verified | Official dataset-specific page or viewer confirmed during bounded page review. |
| SE-MSB-003 | Floods Directive areas<br>Myndigheten för samhällsskydd och beredskap | Kartor enligt översvämningsdirektivet<br>_Floods Directive Hazard and Risk Maps_ | fluvial, coastal | high/medium/low probability | Swedish areas of potential significant flood risk | Dataset-specific page | unknown | Dataset page | [Primary](https://www.mcf.se/sv/amnesomraden/skydd-mot-olyckor-och-farliga-amnen/naturolyckor-och-klimat/oversvamning/oversvamningsdirektivet/) | 2026-06-24 | verified | Official dataset-specific page or viewer confirmed during bounded page review. |
| SE-MSB-004 | National<br>Myndigheten för samhällsskydd och beredskap (MSB) | Skyfallskartering / Lågpunktskartering (Översvämningsportalen)<br>_Cloudburst / Low-point (surface-water) flood mapping_ | surface_water | 100-year rainfall national cloudburst overview (2023), low-point / surface-runoff accumulation (2x2 m DTM) | Sweden; national cloudburst overview plus detailed low-point mapping in selected municipalities | Interactive viewer | unknown | Interactive viewer | [Primary](https://gisapp.msb.se/Apps/oversvamningsportal/index.html) | 2026-06-24 | verified | Official dataset-specific page or viewer confirmed during bounded page review. |

### Unavailable candidates

These links did not resolve. URLs are plain text and non-clickable.

| ID | Jurisdiction / agency | Candidate | Status | Candidate URL | Tracking |
|---|---|---|---|---|---|
| SE-MSB-002 | National<br>Myndigheten för samhällsskydd och beredskap | Översvämningskarteringar | failed (HTTP 404): No candidate link resolved successfully during the strict audit. | `https://www.msb.se/sv/verktyg--tjanster/oversvamningsportalen/oversvamningskarteringar/` | human review |
| SE-LANT-001 | National supporting<br>Lantmäteriet | Nationell höjdmodell | failed (HTTP 404): No candidate link resolved successfully during the strict audit. | `https://www.lantmateriet.se/sv/geodata/vara-produkter/produktlista/markhojdmodell-nedladdning-grid-1/` | non-material candidate |

### What comes next

1. Resolve 1 broken or unreachable material source(s) flagged for human review (see the Unavailable table and the Human review required section).
2. Confirm licensing for 3 confirmed source(s) whose licence is still marked "verify".

## Austria (AT)

**Coverage model:** nationally unified · **Confidence in completeness:** medium

Austria provides nationally unified public viewing through HORA and WISA, combining federal and Länder flood-hazard information. Detailed planning layers may still originate with provincial authorities and river-basin planning, but discovery is centralized. Coastal flood hazard is N/A because Austria is landlocked.

### What we have

- **Confirmed dataset access:** 4 source(s) (0 direct service/API/download, 4 viewer / map document / dataset page).
- **Investigation leads:** 1 reachable portal(s) that still need the dataset located by hand.
- **Unavailable:** 0 broken or unreachable candidate(s).
- **Hazard families confirmed:** Fluvial (river), Surface water (pluvial). **Not yet confirmed:** Coastal.
- **Best confirmed access:** Interactive viewer, Dataset page.


### Portal search guide and website roots

Use the exact dataset names in the directory first. If that fails, try the local-language flood terms below in the site's search box, map-layer catalogue, or metadata search. Website-root links are navigation aids; they are not themselves confirmation that a dataset is available.

**Portal languages:** German

**Country search phrases:** `Hochwassergefahrenkarte` · `Überflutungsfläche` · `Wassertiefe` · `Fließgeschwindigkeit` · `Jährlichkeit`

**Native-language term guide:** `Hochwassergefahrenkarte` — flood-hazard map · `Überflutungsfläche` — inundation extent · `Wassertiefe` — water depth · `Fließgeschwindigkeit` — flow velocity · `Jährlichkeit` — annual exceedance / return frequency. Paste the native term into the portal; the English text is only a meaning guide.

| Website root | Related source IDs | Publisher(s) | Search this site for | Link roles | Current classification |
|---|---|---|---|---|---|
| [ehyd.gv.at](https://ehyd.gv.at/) | AT-EHYD-001 | Hydrographischer Dienst Österreich | `eHYD` | primary, verification final, selected access | investigation lead |
| [hora.gv.at](https://hora.gv.at/) | AT-HORA-001 | Bundesministerium für Land- und Forstwirtschaft, Klima- und Umweltschutz, Regionen und Wasserwirtschaft | `HORA - Natural Hazard Overview & Risk Assessment Austria` | verification final, selected access | confirmed dataset access |
| [info.bml.gv.at](https://info.bml.gv.at/) | AT-BML-001 | Bundesministerium | `Hochwasserrisikomanagement in Österreich` | primary | confirmed dataset access |
| [maps.wisa.bml.gv.at](https://maps.wisa.bml.gv.at/) | AT-WISA-001 | Bundesministerium / Wasser Informationssystem Austria | `WISA Hochwasser - Gefahren- und Risikokarten` | primary | confirmed dataset access |
| [maps.wisa.bmluk.gv.at](https://maps.wisa.bmluk.gv.at/) | AT-WISA-001 | Bundesministerium / Wasser Informationssystem Austria | `WISA Hochwasser - Gefahren- und Risikokarten` | verification final, selected access | confirmed dataset access |
| [water.europa.eu](https://water.europa.eu/) | AT-EEA-001 | European Environment Agency | `WISE Floods Directive` | primary, verification final, selected access | confirmed dataset access |
| [www.bmluk.gv.at](https://www.bmluk.gv.at/) | AT-BML-001 | Bundesministerium | `Hochwasserrisikomanagement in Österreich` | verification final, selected access | confirmed dataset access |
| [www.hora.gv.at](https://www.hora.gv.at/) | AT-HORA-001 | Bundesministerium für Land- und Forstwirtschaft, Klima- und Umweltschutz, Regionen und Wasserwirtschaft | `HORA - Natural Hazard Overview & Risk Assessment Austria` | primary | confirmed dataset access |

### Confirmed dataset access

Each clickable link below was confirmed to identify an authoritative flood dataset and provide a usable service, download, viewer, map document, or dataset-specific page.

| ID | Jurisdiction / agency | Dataset | Confirmed flood type | Confirmed scenarios | Confirmed coverage | Confirmed formats | Confirmed licence | Access | Link | Verified | Flags | Evidence |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| AT-BML-001 | National<br>Bundesministerium | Hochwasserrisikomanagement in Österreich<br>_Flood Risk Management in Austria_ | fluvial, surface_water | unknown | Austria | Dataset-specific page | unknown | Dataset page | [Primary](https://www.bmluk.gv.at/themen/wasser/wisa/hochwasserrisiko.html) | 2026-06-24 | verified | Official dataset-specific page or viewer confirmed during bounded page review. |
| AT-EEA-001 | National fallback<br>European Environment Agency | WISE Floods Directive | fluvial | unknown | Austria | Dataset-specific page | EEA reuse policy | Dataset page | [Primary](https://water.europa.eu/freshwater/europe-freshwater/floods-directive) | 2026-06-24 | fallback, non-material, verified | Official dataset-specific page or viewer confirmed during bounded page review. |
| AT-HORA-001 | National<br>Bundesministerium für Land- und Forstwirtschaft, Klima- und Umweltschutz, Regionen und Wasserwirtschaft | HORA - Natural Hazard Overview & Risk Assessment Austria<br>_HORA Natural Hazard Map_ | fluvial, surface_water, flash_flood | HQ30, HQ100, HQ300 candidates, surface runoff, address risk | Austria | Interactive viewer | unknown | Interactive viewer | [Primary](https://hora.gv.at/) | 2026-06-24 | address_only, verified | Official dataset-specific page or viewer confirmed during bounded page review. |
| AT-WISA-001 | National<br>Bundesministerium / Wasser Informationssystem Austria | WISA Hochwasser - Gefahren- und Risikokarten<br>_WISA Flood Hazard and Risk Maps_ | fluvial | high/medium/low probability, Floods Directive cycles, depth candidate | Austria | Interactive viewer | unknown | Interactive viewer | [Primary](https://maps.wisa.bmluk.gv.at/hochwasser) | 2026-06-24 | verified | Official dataset-specific page or viewer confirmed during bounded page review. |

### Reachable investigation leads

These links resolve, but they are generic portals, catalogue searches, restricted/request-only paths, ambiguous products, or otherwise lack confirmed dataset-specific access. They are clickable for investigation but excluded from scoring.

| ID | Jurisdiction / agency | Candidate | Access | Link | Reason | Tracking |
|---|---|---|---|---|---|---|
| AT-EHYD-001 | National supporting<br>Hydrographischer Dienst Österreich | eHYD | Wrong product | [Open](https://ehyd.gv.at/) | The reachable product is operational or observational, not a confirmed flood-hazard dataset. | non-material candidate |

### What comes next

1. Find Coastal coverage, or document in the summary above why the family does not apply.
2. Work the 1 investigation lead(s): use the portal search guide below to locate the dataset behind each portal, then confirm a usable service, download, viewer, or dataset page.
3. Confirm licensing for 3 confirmed source(s) whose licence is still marked "verify".

## United Arab Emirates (AE)

**Coverage model:** primarily regional · **Scope:** provisional — top-five-region pilot · **Confidence in completeness:** low

No single public national flood-hazard dataset was identified during bounded discovery. Flood and drainage modelling appears to be held by federal infrastructure bodies and emirate/municipal geospatial authorities, with public access often limited to general geoportals, planning systems or operational warnings. The pilot covers Abu Dhabi, Dubai, Sharjah, Ajman and Ras Al Khaimah.

### What we have

- **Confirmed dataset access:** 0 source(s) (0 direct service/API/download, 0 viewer / map document / dataset page).
- **Investigation leads:** 3 reachable portal(s) that still need the dataset located by hand.
- **Unavailable:** 5 broken or unreachable candidate(s).
- **Hazard families confirmed:** none. **Not yet confirmed:** Fluvial (river), Coastal, Surface water (pluvial).
- **Best confirmed access:** No confirmed dataset access.


### Population-priority regions

| Rank | Region | Population | Year | Source |
|---:|---|---:|---:|---|
| 1 | Abu Dhabi | 3,789,000 | 2023 | [Federal Competitiveness and Statistics Centre / emirate statistics](https://fcsc.gov.ae/en-us/Pages/Statistics/Statistics-by-Subject.aspx) |
| 2 | Dubai | 3,655,000 | 2023 | [Federal Competitiveness and Statistics Centre / emirate statistics](https://fcsc.gov.ae/en-us/Pages/Statistics/Statistics-by-Subject.aspx) |
| 3 | Sharjah | 1,800,000 | 2022 | [Federal Competitiveness and Statistics Centre / emirate statistics](https://fcsc.gov.ae/en-us/Pages/Statistics/Statistics-by-Subject.aspx) |
| 4 | Ajman | 505,000 | 2022 | [Federal Competitiveness and Statistics Centre / emirate statistics](https://fcsc.gov.ae/en-us/Pages/Statistics/Statistics-by-Subject.aspx) |
| 5 | Ras Al Khaimah | 400,000 | 2022 | [Federal Competitiveness and Statistics Centre / emirate statistics](https://fcsc.gov.ae/en-us/Pages/Statistics/Statistics-by-Subject.aspx) |

**Deferred regions:** Fujairah, Umm Al Quwain

### Portal search guide and website roots

Use the exact dataset names in the directory first. If that fails, try the local-language flood terms below in the site's search box, map-layer catalogue, or metadata search. Website-root links are navigation aids; they are not themselves confirmation that a dataset is available.

**Portal languages:** Arabic

**Country search phrases:** `خريطة مخاطر الفيضانات` · `مناطق الغمر` · `عمق الفيضان` · `سرعة الجريان` · `فترة التكرار`

**Native-language term guide:** `خريطة مخاطر الفيضانات` — flood-risk map · `مناطق الغمر` — inundation zones · `عمق الفيضان` — flood depth · `سرعة الجريان` — flow velocity · `فترة التكرار` — return period. Paste the native term into the portal; the English text is only a meaning guide.

| Website root | Related source IDs | Publisher(s) | Search this site for | Link roles | Current classification |
|---|---|---|---|---|---|
| [data.jrc.ec.europa.eu](https://data.jrc.ec.europa.eu/) | AE-JRC-001 | European Commission Joint Research Centre | `Global River Flood Hazard Maps` | primary, verification final, selected access | investigation lead |
| [fcsc.gov.ae](https://fcsc.gov.ae/) | population: Abu Dhabi, population: Dubai, population: Sharjah, population: Ajman, population: Ras Al Khaimah | Federal Competitiveness and Statistics Centre / emirate statistics | `Abu Dhabi population`<br>`Dubai population`<br>`Sharjah population`<br>`Ajman population`<br>`Ras Al Khaimah population` | population source | supporting citation |
| [gis.abudhabi.ae](https://gis.abudhabi.ae/) | AE-AUH-001 | Department of Municipalities and Transport / Abu Dhabi Spatial Data Infrastructure | `Abu Dhabi GeoSpatial Portal - flood and drainage layers` | primary | unavailable candidate |
| [gis.ajman.ae](https://gis.ajman.ae/) | AE-AJM-001 | Ajman Municipality and Planning Department | `Ajman GIS` | primary | unavailable candidate |
| [mun.rak.ae](https://mun.rak.ae/) | AE-RAK-001 | Ras Al Khaimah Municipality | `RAK GIS / Geoportal` | primary, verification final, selected access | investigation lead |
| [sdi.shj.ae](https://sdi.shj.ae/) | AE-SHJ-001 | Sharjah Department of Town Planning and Survey / Sharjah SDI | `Sharjah Spatial Data Infrastructure` | primary | unavailable candidate |
| [www.dubaihere.ae](https://www.dubaihere.ae/) | AE-DXB-001 | Dubai Municipality | `Dubai Municipality GIS / Dubai Here` | primary | unavailable candidate |
| [www.moei.gov.ae](https://www.moei.gov.ae/) | AE-MOEI-001 | Ministry of Energy and Infrastructure | `National infrastructure and stormwater/flood studies` | primary | unavailable candidate |
| [www.ncm.ae](https://www.ncm.ae/) | AE-NCM-001 | National Center of Meteorology | `Warnings Map and Radar/Satellite Products` | primary | investigation lead |
| [www.ncm.gov.ae](https://www.ncm.gov.ae/) | AE-NCM-001 | National Center of Meteorology | `Warnings Map and Radar/Satellite Products` | verification final, selected access | investigation lead |

### Confirmed dataset access

Each clickable link below was confirmed to identify an authoritative flood dataset and provide a usable service, download, viewer, map document, or dataset-specific page.

| ID | Jurisdiction / agency | Dataset | Confirmed flood type | Confirmed scenarios | Confirmed coverage | Confirmed formats | Confirmed licence | Access | Link | Verified | Flags | Evidence |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| _none_ | — | — | — | — | — | — | — | — | — | — | — | — |

### Reachable investigation leads

These links resolve, but they are generic portals, catalogue searches, restricted/request-only paths, ambiguous products, or otherwise lack confirmed dataset-specific access. They are clickable for investigation but excluded from scoring.

| ID | Jurisdiction / agency | Candidate | Access | Link | Reason | Tracking |
|---|---|---|---|---|---|---|
| AE-NCM-001 | National supporting<br>National Center of Meteorology | Warnings Map and Radar/Satellite Products | Wrong product | [Open](https://www.ncm.gov.ae/) | The reachable product is operational or observational, not a confirmed flood-hazard dataset. | non-material candidate |
| AE-RAK-001 | Ras Al Khaimah<br>Ras Al Khaimah Municipality | RAK GIS / Geoportal | Request only | [Open](https://mun.rak.ae/) | Access requires a data request; no public dataset path was confirmed. | human review |
| AE-JRC-001 | National fallback<br>European Commission Joint Research Centre | Global River Flood Hazard Maps | Restricted | [Open](https://data.jrc.ec.europa.eu/collection/id-0054) | The JRC collection resolves to a login surface; unauthenticated dataset access was not confirmed. | non-material candidate |

### Unavailable candidates

These links did not resolve. URLs are plain text and non-clickable.

| ID | Jurisdiction / agency | Candidate | Status | Candidate URL | Tracking |
|---|---|---|---|---|---|
| AE-MOEI-001 | National<br>Ministry of Energy and Infrastructure | National infrastructure and stormwater/flood studies | failed (unreachable): No candidate link resolved successfully during the strict audit. | `https://www.moei.gov.ae/` | human review |
| AE-AUH-001 | Abu Dhabi<br>Department of Municipalities and Transport / Abu Dhabi Spatial Data Infrastructure | Abu Dhabi GeoSpatial Portal - flood and drainage layers | failed (unreachable): No candidate link resolved successfully during the strict audit. | `https://gis.abudhabi.ae/` | human review |
| AE-DXB-001 | Dubai<br>Dubai Municipality | Dubai Municipality GIS / Dubai Here | failed (unreachable): No candidate link resolved successfully during the strict audit. | `https://www.dubaihere.ae/` | human review |
| AE-SHJ-001 | Sharjah<br>Sharjah Department of Town Planning and Survey / Sharjah SDI | Sharjah Spatial Data Infrastructure | failed (unreachable): No candidate link resolved successfully during the strict audit. | `https://sdi.shj.ae/` | human review |
| AE-AJM-001 | Ajman<br>Ajman Municipality and Planning Department | Ajman GIS | failed (unreachable): No candidate link resolved successfully during the strict audit. | `https://gis.ajman.ae/` | human review |

### What comes next

1. Confirm Fluvial (river), Coastal, Surface water (pluvial) coverage — a candidate exists but its dataset is not yet confirmed.
2. Work the 3 investigation lead(s): use the portal search guide below to locate the dataset behind each portal, then confirm a usable service, download, viewer, or dataset page.
3. Resolve 5 broken or unreachable material source(s) flagged for human review (see the Unavailable table and the Human review required section).
4. Extend beyond the 5-region pilot to the 2 deferred region(s).

## South Africa (ZA)

**Coverage model:** mixed national and regional · **Scope:** provisional — top-five-region pilot · **Confidence in completeness:** low

National risk, hydrology and geospatial platforms provide broad susceptibility, event and water-resource context, while regulatory floodlines and detailed hydraulic maps are mainly produced by provinces and municipalities. The pilot covers Gauteng, KwaZulu-Natal, Western Cape, Eastern Cape and Limpopo.

### What we have

- **Confirmed dataset access:** 0 source(s) (0 direct service/API/download, 0 viewer / map document / dataset page).
- **Investigation leads:** 6 reachable portal(s) that still need the dataset located by hand.
- **Unavailable:** 3 broken or unreachable candidate(s).
- **Hazard families confirmed:** none. **Not yet confirmed:** Fluvial (river), Coastal, Surface water (pluvial).
- **Best confirmed access:** No confirmed dataset access.


### Population-priority regions

| Rank | Region | Population | Year | Source |
|---:|---|---:|---:|---|
| 1 | Gauteng | 15,100,000 | 2022 | [Statistics South Africa Census 2022](https://census.statssa.gov.za/) |
| 2 | KwaZulu-Natal | 12,420,000 | 2022 | [Statistics South Africa Census 2022](https://census.statssa.gov.za/) |
| 3 | Western Cape | 7,430,000 | 2022 | [Statistics South Africa Census 2022](https://census.statssa.gov.za/) |
| 4 | Eastern Cape | 7,230,000 | 2022 | [Statistics South Africa Census 2022](https://census.statssa.gov.za/) |
| 5 | Limpopo | 6,570,000 | 2022 | [Statistics South Africa Census 2022](https://census.statssa.gov.za/) |

**Deferred regions:** Free State, Mpumalanga, North West, Northern Cape

### Portal search guide and website roots

Use the exact dataset names in the directory first. If that fails, try the local-language flood terms below in the site's search box, map-layer catalogue, or metadata search. Website-root links are navigation aids; they are not themselves confirmation that a dataset is available.

**Portal languages:** English, Afrikaans

**Country search phrases:** `flood hazard map` · `floodline` · `inundation depth` · `return period` · `oorstromingskaart` · `vloedlyn`

**Native-language term guide:** `oorstromingskaart` — flood map · `vloedlyn` — floodline. Paste the native term into the portal; the English text is only a meaning guide.

| Website root | Related source IDs | Publisher(s) | Search this site for | Link roles | Current classification |
|---|---|---|---|---|---|
| [census.statssa.gov.za](https://census.statssa.gov.za/) | population: Gauteng, population: KwaZulu-Natal, population: Western Cape, population: Eastern Cape, population: Limpopo | Statistics South Africa Census 2022 | `Gauteng population`<br>`KwaZulu-Natal population`<br>`Western Cape population`<br>`Eastern Cape population`<br>`Limpopo population` | population source | supporting citation |
| [data.jrc.ec.europa.eu](https://data.jrc.ec.europa.eu/) | ZA-JRC-001 | European Commission Joint Research Centre | `Global River Flood Hazard Maps` | primary, verification final, selected access | investigation lead |
| [gis.gauteng.gov.za](https://gis.gauteng.gov.za/) | ZA-GP-001 | Gauteng Provincial Government / municipalities | `Gauteng GIS floodline and risk layers` | primary | unavailable candidate |
| [sarva.saeon.ac.za](https://sarva.saeon.ac.za/) | ZA-SARVA-001 | South African Environmental Observation Network / government partners | `South African Risk and Vulnerability Atlas` | primary, verification final, selected access | investigation lead |
| [www.coghsta.limpopo.gov.za](https://www.coghsta.limpopo.gov.za/) | ZA-LP-001 | Limpopo Provincial Disaster Management Centre | `Limpopo Disaster Risk Profile and Flood Maps` | primary, verification final, selected access | investigation lead |
| [www.dws.gov.za](https://www.dws.gov.za/) | ZA-DWS-001 | Department of Water and Sanitation | `Hydrological Services and Flood Studies` | primary, verification final | unavailable candidate |
| [www.eccogta.gov.za](https://www.eccogta.gov.za/) | ZA-EC-001 | Eastern Cape Provincial Disaster Management Centre | `Eastern Cape Disaster Risk Profile and Flood Maps` | primary, verification final, selected access | investigation lead |
| [www.kzncogta.gov.za](https://www.kzncogta.gov.za/) | ZA-KZN-001 | KwaZulu-Natal Provincial Disaster Management Centre / eThekwini Municipality | `KwaZulu-Natal flood risk and floodline maps` | primary, verification final, selected access | investigation lead |
| [www.ndmc.gov.za](https://www.ndmc.gov.za/) | ZA-NDMC-001 | National Disaster Management Centre | `NDMC GIS Portal / Risk Information` | primary, verification final, selected access | investigation lead |
| [www.westerncape.gov.za](https://www.westerncape.gov.za/) | ZA-WC-001 | Western Cape Government / Department of Local Government | `Western Cape Disaster Risk and Flood Mapping` | primary, verification final | unavailable candidate |

### Confirmed dataset access

Each clickable link below was confirmed to identify an authoritative flood dataset and provide a usable service, download, viewer, map document, or dataset-specific page.

| ID | Jurisdiction / agency | Dataset | Confirmed flood type | Confirmed scenarios | Confirmed coverage | Confirmed formats | Confirmed licence | Access | Link | Verified | Flags | Evidence |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| _none_ | — | — | — | — | — | — | — | — | — | — | — | — |

### Reachable investigation leads

These links resolve, but they are generic portals, catalogue searches, restricted/request-only paths, ambiguous products, or otherwise lack confirmed dataset-specific access. They are clickable for investigation but excluded from scoring.

| ID | Jurisdiction / agency | Candidate | Access | Link | Reason | Tracking |
|---|---|---|---|---|---|---|
| ZA-SARVA-001 | National<br>South African Environmental Observation Network / government partners | South African Risk and Vulnerability Atlas | Generic portal | [Open](https://sarva.saeon.ac.za/) | The link is a generic agency or geoportal entry point; the named dataset was not resolved. | human review |
| ZA-NDMC-001 | National<br>National Disaster Management Centre | NDMC GIS Portal / Risk Information | Generic portal | [Open](https://www.ndmc.gov.za/) | The link is a generic agency or geoportal entry point; the named dataset was not resolved. | human review |
| ZA-KZN-001 | KwaZulu-Natal<br>KwaZulu-Natal Provincial Disaster Management Centre / eThekwini Municipality | KwaZulu-Natal flood risk and floodline maps | Request only | [Open](https://www.kzncogta.gov.za/) | Access requires a data request; no public dataset path was confirmed. | human review |
| ZA-EC-001 | Eastern Cape<br>Eastern Cape Provincial Disaster Management Centre | Eastern Cape Disaster Risk Profile and Flood Maps | Request only | [Open](https://www.eccogta.gov.za/) | Access requires a data request; no public dataset path was confirmed. | human review |
| ZA-LP-001 | Limpopo<br>Limpopo Provincial Disaster Management Centre | Limpopo Disaster Risk Profile and Flood Maps | Request only | [Open](https://www.coghsta.limpopo.gov.za/) | Access requires a data request; no public dataset path was confirmed. | human review |
| ZA-JRC-001 | National fallback<br>European Commission Joint Research Centre | Global River Flood Hazard Maps | Restricted | [Open](https://data.jrc.ec.europa.eu/collection/id-0054) | The JRC collection resolves to a login surface; unauthenticated dataset access was not confirmed. | non-material candidate |

### Unavailable candidates

These links did not resolve. URLs are plain text and non-clickable.

| ID | Jurisdiction / agency | Candidate | Status | Candidate URL | Tracking |
|---|---|---|---|---|---|
| ZA-DWS-001 | National<br>Department of Water and Sanitation | Hydrological Services and Flood Studies | failed (HTTP 403): The official page returned HTTP 403; public dataset usability could not be confirmed. | `https://www.dws.gov.za/Hydrology/` | human review |
| ZA-GP-001 | Gauteng<br>Gauteng Provincial Government / municipalities | Gauteng GIS floodline and risk layers | failed (unreachable): No candidate link resolved successfully during the strict audit. | `https://gis.gauteng.gov.za/` | human review |
| ZA-WC-001 | Western Cape<br>Western Cape Government / Department of Local Government | Western Cape Disaster Risk and Flood Mapping | failed (HTTP 404): No candidate link resolved successfully during the strict audit. | `https://www.westerncape.gov.za/general-publication/disaster-management` | human review |

### What comes next

1. Confirm Fluvial (river), Coastal, Surface water (pluvial) coverage — a candidate exists but its dataset is not yet confirmed.
2. Work the 6 investigation lead(s): use the portal search guide below to locate the dataset behind each portal, then confirm a usable service, download, viewer, or dataset page.
3. Resolve 3 broken or unreachable material source(s) flagged for human review (see the Unavailable table and the Human review required section).
4. Extend beyond the 5-region pilot to the 4 deferred region(s).

## Republic of Korea (KR)

**Coverage model:** nationally unified · **Confidence in completeness:** medium

The Ministry of Environment operates a national Flood Risk Map Information System, supported by national water-information and safety-map platforms. Products include river-flood hazard maps and urban-inundation maps, with some access or download functions potentially restricted.

### What we have

- **Confirmed dataset access:** 1 source(s) (0 direct service/API/download, 1 viewer / map document / dataset page).
- **Investigation leads:** 3 reachable portal(s) that still need the dataset located by hand.
- **Unavailable:** 2 broken or unreachable candidate(s).
- **Hazard families confirmed:** Fluvial (river), Surface water (pluvial). **Not yet confirmed:** Coastal.
- **Best confirmed access:** Interactive viewer.


### Portal search guide and website roots

Use the exact dataset names in the directory first. If that fails, try the local-language flood terms below in the site's search box, map-layer catalogue, or metadata search. Website-root links are navigation aids; they are not themselves confirmation that a dataset is available.

**Portal languages:** Korean

**Country search phrases:** `홍수위험지도` · `침수예상도` · `침수심` · `유속` · `재현기간`

**Native-language term guide:** `홍수위험지도` — flood-risk map · `침수예상도` — expected-inundation map · `침수심` — inundation depth · `유속` — flow velocity · `재현기간` — return period. Paste the native term into the portal; the English text is only a meaning guide.

| Website root | Related source IDs | Publisher(s) | Search this site for | Link roles | Current classification |
|---|---|---|---|---|---|
| [www.wamis.go.kr](http://www.wamis.go.kr/) | KR-WAMIS-001 | 국가수자원관리종합정보시스템 | `WAMIS 국가수자원관리종합정보시스템` | primary | unavailable candidate |
| [data.jrc.ec.europa.eu](https://data.jrc.ec.europa.eu/) | KR-JRC-001 | European Commission Joint Research Centre | `Global River Flood Hazard Maps` | primary, verification final, selected access | investigation lead |
| [floodmap.go.kr](https://floodmap.go.kr/) | KR-MOE-001 | 환경부 / Ministry of Environment | `홍수위험지도 정보시스템` | primary, verification final, selected access | confirmed dataset access |
| [www.data.go.kr](https://www.data.go.kr/) | KR-DATA-001 | 공공데이터포털 | `공공데이터포털 홍수위험지도 데이터` | primary, verification final, selected access | investigation lead |
| [www.safemap.go.kr](https://www.safemap.go.kr/) | KR-SAFEMAP-001 | 행정안전부 | `생활안전지도 - 침수 및 재난안전` | primary, verification final, selected access | investigation lead |
| [www.vworld.kr](https://www.vworld.kr/) | KR-VWORLD-001 | 국토교통부 / VWorld | `국가공간정보 오픈플랫폼 VWorld` | primary | unavailable candidate |

### Confirmed dataset access

Each clickable link below was confirmed to identify an authoritative flood dataset and provide a usable service, download, viewer, map document, or dataset-specific page.

| ID | Jurisdiction / agency | Dataset | Confirmed flood type | Confirmed scenarios | Confirmed coverage | Confirmed formats | Confirmed licence | Access | Link | Verified | Flags | Evidence |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| KR-MOE-001 | National<br>환경부 / Ministry of Environment | 홍수위험지도 정보시스템<br>_Flood Risk Map Information System_ | fluvial, surface_water | river flooding scenarios, urban inundation scenarios, depth candidates | Republic of Korea | Interactive viewer | unknown | Interactive viewer | [Primary](https://floodmap.go.kr/intro) | 2026-06-24 | verified | Official dataset-specific page or viewer confirmed during bounded page review. |

### Reachable investigation leads

These links resolve, but they are generic portals, catalogue searches, restricted/request-only paths, ambiguous products, or otherwise lack confirmed dataset-specific access. They are clickable for investigation but excluded from scoring.

| ID | Jurisdiction / agency | Candidate | Access | Link | Reason | Tracking |
|---|---|---|---|---|---|---|
| KR-SAFEMAP-001 | National<br>행정안전부 | 생활안전지도 - 침수 및 재난안전 | Generic portal | [Open](https://www.safemap.go.kr/) | The link is a generic agency or geoportal entry point; the named dataset was not resolved. | human review |
| KR-DATA-001 | National<br>공공데이터포털 | 공공데이터포털 홍수위험지도 데이터 | Catalogue search | [Open](https://www.data.go.kr/) | The link is a catalogue/search entry point rather than a dataset-specific record. | human review |
| KR-JRC-001 | National fallback<br>European Commission Joint Research Centre | Global River Flood Hazard Maps | Restricted | [Open](https://data.jrc.ec.europa.eu/collection/id-0054) | The JRC collection resolves to a login surface; unauthenticated dataset access was not confirmed. | non-material candidate |

### Unavailable candidates

These links did not resolve. URLs are plain text and non-clickable.

| ID | Jurisdiction / agency | Candidate | Status | Candidate URL | Tracking |
|---|---|---|---|---|---|
| KR-WAMIS-001 | National<br>국가수자원관리종합정보시스템 | WAMIS 국가수자원관리종합정보시스템 | failed (unreachable): No candidate link resolved successfully during the strict audit. | `http://www.wamis.go.kr/` | human review |
| KR-VWORLD-001 | National<br>국토교통부 / VWorld | 국가공간정보 오픈플랫폼 VWorld | failed (unreachable): No candidate link resolved successfully during the strict audit. | `https://www.vworld.kr/` | human review |

### What comes next

1. Confirm Coastal coverage — a candidate exists but its dataset is not yet confirmed.
2. Work the 3 investigation lead(s): use the portal search guide below to locate the dataset behind each portal, then confirm a usable service, download, viewer, or dataset page.
3. Resolve 2 broken or unreachable material source(s) flagged for human review (see the Unavailable table and the Human review required section).
4. Confirm licensing for 1 confirmed source(s) whose licence is still marked "verify".

## Human review required

These items remained unresolved after the single permitted rediscovery round.

| Country | Source | Problem | Requested review |
|---|---|---|---|
| BR | BR-ANA-001 | Dataset-resolved verification did not confirm usable access for BR-ANA-001 (Agência Nacional de Águas e Saneamento Básico (ANA) — Flood Vulnerability Atlas). Classification: unavailable / unavailable. No candidate link resolved successfully during the strict audit. | Human review: provide a current authoritative dataset-specific viewer, document, service, API, or download as a superseding candidate, or accept this coverage/access gap in the readiness score. |
| BR | BR-RJ-001 | Dataset-resolved verification did not confirm usable access for BR-RJ-001 (Instituto Estadual do Ambiente (INEA) — GeoINEA Flood-Risk Mapping). Classification: unavailable / unavailable. No candidate link resolved successfully during the strict audit. | Human review: provide a current authoritative dataset-specific viewer, document, service, API, or download as a superseding candidate, or accept this coverage/access gap in the readiness score. |
| BR | BR-BA-001 | Dataset-resolved verification did not confirm usable access for BR-BA-001 (Instituto do Meio Ambiente e Recursos Hídricos (INEMA) — GeoBahia Environmental Geoportal). Classification: unavailable / unavailable. No candidate link resolved successfully during the strict audit. | Human review: provide a current authoritative dataset-specific viewer, document, service, API, or download as a superseding candidate, or accept this coverage/access gap in the readiness score. |
| BR | BR-PR-001 | Dataset-resolved verification did not confirm usable access for BR-PR-001 (Governo do Paraná / GeoPR — GeoPR Flood and Risk Geodata). Classification: unavailable / unavailable. No candidate link resolved successfully during the strict audit. | Human review: provide a current authoritative dataset-specific viewer, document, service, API, or download as a superseding candidate, or accept this coverage/access gap in the readiness score. |
| IN | IN-CWC-001 | Dataset-resolved verification did not confirm usable access for IN-CWC-001 (Central Water Commission — CWC Flood Forecasting Portal). Classification: unavailable / unavailable. No candidate link resolved successfully during the strict audit. | Human review: provide a current authoritative dataset-specific viewer, document, service, API, or download as a superseding candidate, or accept this coverage/access gap in the readiness score. |
| IN | IN-WRIS-001 | Dataset-resolved verification did not confirm usable access for IN-WRIS-001 (National Water Informatics Centre — India Water Resources Information System). Classification: unavailable / unavailable. No candidate link resolved successfully during the strict audit. | Human review: provide a current authoritative dataset-specific viewer, document, service, API, or download as a superseding candidate, or accept this coverage/access gap in the readiness score. |
| IN | IN-UP-001 | Dataset-resolved verification did not confirm usable access for IN-UP-001 (Uttar Pradesh State Disaster Management Authority — Uttar Pradesh Flood Hazard Resources). Classification: unavailable / unavailable. No candidate link resolved successfully during the strict audit. | Human review: provide a current authoritative dataset-specific viewer, document, service, API, or download as a superseding candidate, or accept this coverage/access gap in the readiness score. |
| IN | IN-WB-001 | Dataset-resolved verification did not confirm usable access for IN-WB-001 (Irrigation & Waterways Department, West Bengal — West Bengal Flood Management and GIS Resources). Classification: unavailable / unavailable. No candidate link resolved successfully during the strict audit. | Human review: provide a current authoritative dataset-specific viewer, document, service, API, or download as a superseding candidate, or accept this coverage/access gap in the readiness score. |
| IN | IN-MP-001 | Dataset-resolved verification did not confirm usable access for IN-MP-001 (Water Resources Department, Madhya Pradesh — Madhya Pradesh Water Resources GIS and Flood Studies). Classification: unavailable / unavailable. No candidate link resolved successfully during the strict audit. | Human review: provide a current authoritative dataset-specific viewer, document, service, API, or download as a superseding candidate, or accept this coverage/access gap in the readiness score. |
| CN | CN-GD-001 | Dataset-resolved verification did not confirm usable access for CN-GD-001 (广东省水利厅 — Guangdong Flood and Flash-Flood Risk Maps). Classification: unavailable / unavailable. No candidate link resolved successfully during the strict audit. | Human review: provide a current authoritative dataset-specific viewer, document, service, API, or download as a superseding candidate, or accept this coverage/access gap in the readiness score. |
| CN | CN-HA-001 | Dataset-resolved verification did not confirm usable access for CN-HA-001 (河南省水利厅 — Henan Flood Risk Maps). Classification: unavailable / unavailable. The official page returned HTTP 403; public dataset usability could not be confirmed. | Human review: provide a current authoritative dataset-specific viewer, document, service, API, or download as a superseding candidate, or accept this coverage/access gap in the readiness score. |
| CN | CN-JS-001 | Dataset-resolved verification did not confirm usable access for CN-JS-001 (江苏省水利厅 — Jiangsu Flood Risk Maps). Classification: unavailable / unavailable. No candidate link resolved successfully during the strict audit. | Human review: provide a current authoritative dataset-specific viewer, document, service, API, or download as a superseding candidate, or accept this coverage/access gap in the readiness score. |
| CA | CA-NRCAN-001 | Dataset-resolved verification did not confirm usable access for CA-NRCAN-001 (Natural Resources Canada — Flood Hazard Identification and Mapping Program). Classification: unavailable / unavailable. No candidate link resolved successfully during the strict audit. | Human review: provide a current authoritative dataset-specific viewer, document, service, API, or download as a superseding candidate, or accept this coverage/access gap in the readiness score. |
| CA | CA-ON-001 | Dataset-resolved verification did not confirm usable access for CA-ON-001 (Government of Ontario / Ministry of Natural Resources — Ontario Floodplain Mapping). Classification: unavailable / unavailable. No candidate link resolved successfully during the strict audit. | Human review: provide a current authoritative dataset-specific viewer, document, service, API, or download as a superseding candidate, or accept this coverage/access gap in the readiness score. |
| CA | CA-BC-001 | Dataset-resolved verification did not confirm usable access for CA-BC-001 (Government of British Columbia — British Columbia Floodplain Mapping). Classification: unavailable / unavailable. No candidate link resolved successfully during the strict audit. | Human review: provide a current authoritative dataset-specific viewer, document, service, API, or download as a superseding candidate, or accept this coverage/access gap in the readiness score. |
| FR | FR-IDF-001 | Dataset-resolved verification did not confirm usable access for FR-IDF-001 (DRIEAT Île-de-France — Île-de-France TRI Flood Maps). Classification: unavailable / unavailable. No candidate link resolved successfully during the strict audit. | Human review: provide a current authoritative dataset-specific viewer, document, service, API, or download as a superseding candidate, or accept this coverage/access gap in the readiness score. |
| FR | FR-ARA-001 | Dataset-resolved verification did not confirm usable access for FR-ARA-001 (DREAL Auvergne-Rhône-Alpes — Auvergne-Rhône-Alpes TRI Flood Maps). Classification: unavailable / unavailable. No candidate link resolved successfully during the strict audit. | Human review: provide a current authoritative dataset-specific viewer, document, service, API, or download as a superseding candidate, or accept this coverage/access gap in the readiness score. |
| FR | FR-OCC-001 | Dataset-resolved verification did not confirm usable access for FR-OCC-001 (DREAL Occitanie — Occitanie Flood Hazard and Risk Maps). Classification: unavailable / unavailable. No candidate link resolved successfully during the strict audit. | Human review: provide a current authoritative dataset-specific viewer, document, service, API, or download as a superseding candidate, or accept this coverage/access gap in the readiness score. |
| FR | FR-HDF-001 | Dataset-resolved verification did not confirm usable access for FR-HDF-001 (DREAL Hauts-de-France — Hauts-de-France TRI Flood Maps). Classification: unavailable / unavailable. No candidate link resolved successfully during the strict audit. | Human review: provide a current authoritative dataset-specific viewer, document, service, API, or download as a superseding candidate, or accept this coverage/access gap in the readiness score. |
| MX | MX-CENAPRED-001 | Dataset-resolved verification did not confirm usable access for MX-CENAPRED-001 (Centro Nacional de Prevención de Desastres — National Risk Atlas). Classification: unavailable / unavailable. No candidate link resolved successfully during the strict audit. | Human review: provide a current authoritative dataset-specific viewer, document, service, API, or download as a superseding candidate, or accept this coverage/access gap in the readiness score. |
| MX | MX-EM-001 | Dataset-resolved verification did not confirm usable access for MX-EM-001 (Coordinación General de Protección Civil del Estado de México — State of Mexico Risk Atlas). Classification: unavailable / unavailable. No candidate link resolved successfully during the strict audit. | Human review: provide a current authoritative dataset-specific viewer, document, service, API, or download as a superseding candidate, or accept this coverage/access gap in the readiness score. |
| MX | MX-VER-001 | Dataset-resolved verification did not confirm usable access for MX-VER-001 (Secretaría de Protección Civil de Veracruz — Veracruz State Risk Atlas). Classification: unavailable / unavailable. No candidate link resolved successfully during the strict audit. | Human review: provide a current authoritative dataset-specific viewer, document, service, API, or download as a superseding candidate, or accept this coverage/access gap in the readiness score. |
| MX | MX-PUE-001 | Dataset-resolved verification did not confirm usable access for MX-PUE-001 (Coordinación General de Protección Civil del Estado de Puebla — Puebla State Risk Atlas). Classification: unavailable / unavailable. No candidate link resolved successfully during the strict audit. | Human review: provide a current authoritative dataset-specific viewer, document, service, API, or download as a superseding candidate, or accept this coverage/access gap in the readiness score. |
| MY | MY-JPS-002 | Dataset-resolved verification did not confirm usable access for MY-JPS-002 (Jabatan Pengairan dan Saliran Malaysia — DID Geospatial Flood Hazard Maps). Classification: unavailable / unavailable. No candidate link resolved successfully during the strict audit. | Human review: provide a current authoritative dataset-specific viewer, document, service, API, or download as a superseding candidate, or accept this coverage/access gap in the readiness score. |
| MY | MY-SEL-001 | Dataset-resolved verification did not confirm usable access for MY-SEL-001 (JPS Malaysia / JPS Selangor — Selangor Flood Hazard Maps). Classification: unavailable / unavailable. No candidate link resolved successfully during the strict audit. | Human review: provide a current authoritative dataset-specific viewer, document, service, API, or download as a superseding candidate, or accept this coverage/access gap in the readiness score. |
| MY | MY-JHR-001 | Dataset-resolved verification did not confirm usable access for MY-JHR-001 (JPS Malaysia / JPS Johor — Johor Flood Hazard Maps). Classification: unavailable / unavailable. No candidate link resolved successfully during the strict audit. | Human review: provide a current authoritative dataset-specific viewer, document, service, API, or download as a superseding candidate, or accept this coverage/access gap in the readiness score. |
| MY | MY-PRK-001 | Dataset-resolved verification did not confirm usable access for MY-PRK-001 (JPS Malaysia / JPS Perak — Perak Flood Hazard Maps). Classification: unavailable / unavailable. No candidate link resolved successfully during the strict audit. | Human review: provide a current authoritative dataset-specific viewer, document, service, API, or download as a superseding candidate, or accept this coverage/access gap in the readiness score. |
| JP | JP-TKY-001 | Dataset-resolved verification did not confirm usable access for JP-TKY-001 (東京都建設局 — Tokyo Flood Inundation Assumption Maps). Classification: unavailable / unavailable. No candidate link resolved successfully during the strict audit. | Human review: provide a current authoritative dataset-specific viewer, document, service, API, or download as a superseding candidate, or accept this coverage/access gap in the readiness score. |
| JP | JP-OSK-001 | Dataset-resolved verification did not confirm usable access for JP-OSK-001 (大阪府 — Osaka Flood Inundation Assumption Maps). Classification: unavailable / unavailable. No candidate link resolved successfully during the strict audit. | Human review: provide a current authoritative dataset-specific viewer, document, service, API, or download as a superseding candidate, or accept this coverage/access gap in the readiness score. |
| JP | JP-AIC-001 | Dataset-resolved verification did not confirm usable access for JP-AIC-001 (愛知県 — Aichi Flood Inundation Assumption Maps). Classification: unavailable / unavailable. No candidate link resolved successfully during the strict audit. | Human review: provide a current authoritative dataset-specific viewer, document, service, API, or download as a superseding candidate, or accept this coverage/access gap in the readiness score. |
| JP | JP-SAI-001 | Dataset-resolved verification did not confirm usable access for JP-SAI-001 (埼玉県 — Saitama Flood Inundation Assumption Maps). Classification: unavailable / unavailable. No candidate link resolved successfully during the strict audit. | Human review: provide a current authoritative dataset-specific viewer, document, service, API, or download as a superseding candidate, or accept this coverage/access gap in the readiness score. |
| BE | BE-BRU-001 | Dataset-resolved verification did not confirm usable access for BE-BRU-001 (Bruxelles Environnement — Brussels Flood Hazard and Risk Map). Classification: unavailable / unavailable. No candidate link resolved successfully during the strict audit. | Human review: provide a current authoritative dataset-specific viewer, document, service, API, or download as a superseding candidate, or accept this coverage/access gap in the readiness score. |
| IT | IT-AC-001 | Dataset-resolved verification did not confirm usable access for IT-AC-001 (Autorità di bacino distrettuale dell'Appennino Centrale — Central Apennines Flood Hazard and Risk Maps). Classification: unavailable / unavailable. No candidate link resolved successfully during the strict audit. | Human review: provide a current authoritative dataset-specific viewer, document, service, API, or download as a superseding candidate, or accept this coverage/access gap in the readiness score. |
| IT | IT-AM-001 | Dataset-resolved verification did not confirm usable access for IT-AM-001 (Autorità di bacino distrettuale dell'Appennino Meridionale — Southern Apennines Flood Risk Management Maps). Classification: unavailable / unavailable. No candidate link resolved successfully during the strict audit. | Human review: provide a current authoritative dataset-specific viewer, document, service, API, or download as a superseding candidate, or accept this coverage/access gap in the readiness score. |
| IT | IT-AO-001 | Dataset-resolved verification did not confirm usable access for IT-AO-001 (Autorità di bacino distrettuale delle Alpi Orientali — Eastern Alps Flood Hazard and Risk Maps). Classification: unavailable / unavailable. No candidate link resolved successfully during the strict audit. | Human review: provide a current authoritative dataset-specific viewer, document, service, API, or download as a superseding candidate, or accept this coverage/access gap in the readiness score. |
| CH | CH-BE-001 | Dataset-resolved verification did not confirm usable access for CH-BE-001 (Kanton Bern — Bern Natural-Hazard Flood Map). Classification: unavailable / unavailable. No candidate link resolved successfully during the strict audit. | Human review: provide a current authoritative dataset-specific viewer, document, service, API, or download as a superseding candidate, or accept this coverage/access gap in the readiness score. |
| TH | TH-GISTDA-001 | Dataset-resolved verification did not confirm usable access for TH-GISTDA-001 (สำนักงานพัฒนาเทคโนโลยีอวกาศและภูมิสารสนเทศ — GISTDA Disaster Flood Monitoring). Classification: unavailable / unavailable. No candidate link resolved successfully during the strict audit. | Human review: provide a current authoritative dataset-specific viewer, document, service, API, or download as a superseding candidate, or accept this coverage/access gap in the readiness score. |
| TH | TH-BKK-001 | Dataset-resolved verification did not confirm usable access for TH-BKK-001 (Bangkok Metropolitan Administration — Bangkok Flood Monitoring and Risk Maps). Classification: unavailable / unavailable. No candidate link resolved successfully during the strict audit. | Human review: provide a current authoritative dataset-specific viewer, document, service, API, or download as a superseding candidate, or accept this coverage/access gap in the readiness score. |
| TH | TH-NMA-001 | Dataset-resolved verification did not confirm usable access for TH-NMA-001 (Department of Disaster Prevention and Mitigation / provincial authorities — Nakhon Ratchasima Flood-Risk Maps). Classification: unavailable / unavailable. The official page returned HTTP 403; public dataset usability could not be confirmed. | Human review: provide a current authoritative dataset-specific viewer, document, service, API, or download as a superseding candidate, or accept this coverage/access gap in the readiness score. |
| TH | TH-UBN-001 | Dataset-resolved verification did not confirm usable access for TH-UBN-001 (Department of Disaster Prevention and Mitigation / provincial authorities — Ubon Ratchathani Flood-Risk Maps). Classification: unavailable / unavailable. The official page returned HTTP 403; public dataset usability could not be confirmed. | Human review: provide a current authoritative dataset-specific viewer, document, service, API, or download as a superseding candidate, or accept this coverage/access gap in the readiness score. |
| TH | TH-CMI-001 | Dataset-resolved verification did not confirm usable access for TH-CMI-001 (Department of Disaster Prevention and Mitigation / provincial authorities — Chiang Mai Flood-Risk Maps). Classification: unavailable / unavailable. The official page returned HTTP 403; public dataset usability could not be confirmed. | Human review: provide a current authoritative dataset-specific viewer, document, service, API, or download as a superseding candidate, or accept this coverage/access gap in the readiness score. |
| TH | TH-KKN-001 | Dataset-resolved verification did not confirm usable access for TH-KKN-001 (Department of Disaster Prevention and Mitigation / provincial authorities — Khon Kaen Flood-Risk Maps). Classification: unavailable / unavailable. The official page returned HTTP 403; public dataset usability could not be confirmed. | Human review: provide a current authoritative dataset-specific viewer, document, service, API, or download as a superseding candidate, or accept this coverage/access gap in the readiness score. |
| SE | SE-MSB-002 | Dataset-resolved verification did not confirm usable access for SE-MSB-002 (Myndigheten för samhällsskydd och beredskap — Flood Inundation Mapping Downloads). Classification: unavailable / unavailable. No candidate link resolved successfully during the strict audit. | Human review: provide a current authoritative dataset-specific viewer, document, service, API, or download as a superseding candidate, or accept this coverage/access gap in the readiness score. |
| AE | AE-MOEI-001 | Dataset-resolved verification did not confirm usable access for AE-MOEI-001 (Ministry of Energy and Infrastructure — Federal Flood and Stormwater Studies). Classification: unavailable / unavailable. No candidate link resolved successfully during the strict audit. | Human review: provide a current authoritative dataset-specific viewer, document, service, API, or download as a superseding candidate, or accept this coverage/access gap in the readiness score. |
| AE | AE-AUH-001 | Dataset-resolved verification did not confirm usable access for AE-AUH-001 (Department of Municipalities and Transport / Abu Dhabi Spatial Data Infrastructure — Abu Dhabi Flood and Drainage Geodata). Classification: unavailable / unavailable. No candidate link resolved successfully during the strict audit. | Human review: provide a current authoritative dataset-specific viewer, document, service, API, or download as a superseding candidate, or accept this coverage/access gap in the readiness score. |
| AE | AE-DXB-001 | Dataset-resolved verification did not confirm usable access for AE-DXB-001 (Dubai Municipality — Dubai Flood and Drainage Geodata). Classification: unavailable / unavailable. No candidate link resolved successfully during the strict audit. | Human review: provide a current authoritative dataset-specific viewer, document, service, API, or download as a superseding candidate, or accept this coverage/access gap in the readiness score. |
| AE | AE-SHJ-001 | Dataset-resolved verification did not confirm usable access for AE-SHJ-001 (Sharjah Department of Town Planning and Survey / Sharjah SDI — Sharjah Flood and Drainage Geodata). Classification: unavailable / unavailable. No candidate link resolved successfully during the strict audit. | Human review: provide a current authoritative dataset-specific viewer, document, service, API, or download as a superseding candidate, or accept this coverage/access gap in the readiness score. |
| AE | AE-AJM-001 | Dataset-resolved verification did not confirm usable access for AE-AJM-001 (Ajman Municipality and Planning Department — Ajman Flood and Drainage Geodata). Classification: unavailable / unavailable. No candidate link resolved successfully during the strict audit. | Human review: provide a current authoritative dataset-specific viewer, document, service, API, or download as a superseding candidate, or accept this coverage/access gap in the readiness score. |
| ZA | ZA-DWS-001 | Dataset-resolved verification did not confirm usable access for ZA-DWS-001 (Department of Water and Sanitation — DWS Hydrological and Flood Studies). Classification: unavailable / unavailable. The official page returned HTTP 403; public dataset usability could not be confirmed. | Human review: provide a current authoritative dataset-specific viewer, document, service, API, or download as a superseding candidate, or accept this coverage/access gap in the readiness score. |
| ZA | ZA-GP-001 | Dataset-resolved verification did not confirm usable access for ZA-GP-001 (Gauteng Provincial Government / municipalities — Gauteng Floodline and Risk Geodata). Classification: unavailable / unavailable. No candidate link resolved successfully during the strict audit. | Human review: provide a current authoritative dataset-specific viewer, document, service, API, or download as a superseding candidate, or accept this coverage/access gap in the readiness score. |
| ZA | ZA-WC-001 | Dataset-resolved verification did not confirm usable access for ZA-WC-001 (Western Cape Government / Department of Local Government — Western Cape Flood Risk Mapping). Classification: unavailable / unavailable. No candidate link resolved successfully during the strict audit. | Human review: provide a current authoritative dataset-specific viewer, document, service, API, or download as a superseding candidate, or accept this coverage/access gap in the readiness score. |
| KR | KR-WAMIS-001 | Dataset-resolved verification did not confirm usable access for KR-WAMIS-001 (국가수자원관리종합정보시스템 — Water Resources Management Information System). Classification: unavailable / unavailable. No candidate link resolved successfully during the strict audit. | Human review: provide a current authoritative dataset-specific viewer, document, service, API, or download as a superseding candidate, or accept this coverage/access gap in the readiness score. |
| KR | KR-VWORLD-001 | Dataset-resolved verification did not confirm usable access for KR-VWORLD-001 (국토교통부 / VWorld — VWorld National Spatial Information Platform). Classification: unavailable / unavailable. No candidate link resolved successfully during the strict audit. | Human review: provide a current authoritative dataset-specific viewer, document, service, API, or download as a superseding candidate, or accept this coverage/access gap in the readiness score. |
| IT | IT-MI-001 | Dataset-resolved verification did not confirm usable access for IT-MI-001 (Comune di Milano - PGT Componente Geologica — Milan Simplified Hydraulic-Risk Document and Map). Classification: unavailable / unavailable. The official page returned HTTP 403; public dataset usability could not be confirmed. | Human review: provide a current authoritative dataset-specific viewer, document, service, API, or download as a superseding candidate, or accept this coverage/access gap in the readiness score. |
| TH | TH-DMCR-001 | Dataset-resolved verification did not confirm usable access for TH-DMCR-001 (Department of Marine and Coastal Resources (DMCR) — Thailand Coastal Spatial Database (TCS) - Coastal Change / Erosion). Classification: unavailable / unavailable. No candidate link resolved successfully during the strict audit. | Human review: provide a current authoritative dataset-specific viewer, document, service, API, or download as a superseding candidate, or accept this coverage/access gap in the readiness score. |
| BR | BR-SGB-001 | Dataset-resolved verification did not confirm usable access for BR-SGB-001 (Serviço Geológico do Brasil (SGB/CPRM) — GeoSGB Geological Risk Mapping). Classification: lead / generic_portal. The link is a generic agency or geoportal entry point; the named dataset was not resolved. | Human review: provide a current authoritative dataset-specific viewer, document, service, API, or download as a superseding candidate, or accept this coverage/access gap in the readiness score. |
| BR | BR-SP-001 | Dataset-resolved verification did not confirm usable access for BR-SP-001 (Secretaria de Meio Ambiente, Infraestrutura e Logística / DataGEO — DataGEO Flood and Risk Layers). Classification: lead / catalogue_search. The link is a catalogue/search entry point rather than a dataset-specific record. | Human review: provide a current authoritative dataset-specific viewer, document, service, API, or download as a superseding candidate, or accept this coverage/access gap in the readiness score. |
| BR | BR-MG-001 | Dataset-resolved verification did not confirm usable access for BR-MG-001 (SEMAD / IDE-Sisema — IDE-Sisema Flood and Risk Layers). Classification: lead / catalogue_search. The link is a catalogue/search entry point rather than a dataset-specific record. | Human review: provide a current authoritative dataset-specific viewer, document, service, API, or download as a superseding candidate, or accept this coverage/access gap in the readiness score. |
| BR | BR-SP-002 | Dataset-resolved verification did not confirm usable access for BR-SP-002 (Instituto de Pesquisas Ambientais (IPA) / SEMIL - DataGEO — São Paulo Coastal Erosion and Coastal Flooding Risk Map). Classification: lead / service. service exposes no recognizably flood-related layers | Human review: provide a current authoritative dataset-specific viewer, document, service, API, or download as a superseding candidate, or accept this coverage/access gap in the readiness score. |
| IN | IN-MH-001 | Dataset-resolved verification did not confirm usable access for IN-MH-001 (Maharashtra State Disaster Management Authority — Maharashtra Flood Hazard and Risk Resources). Classification: lead / generic_portal. The link is a generic agency or geoportal entry point; the named dataset was not resolved. | Human review: provide a current authoritative dataset-specific viewer, document, service, API, or download as a superseding candidate, or accept this coverage/access gap in the readiness score. |
| DE | DE-BFG-001 | Dataset-resolved verification did not confirm usable access for DE-BFG-001 (Bundesanstalt für Gewässerkunde (BfG) — BfG Geoportal). Classification: lead / catalogue_search. The link is a catalogue/search entry point rather than a dataset-specific record. | Human review: provide a current authoritative dataset-specific viewer, document, service, API, or download as a superseding candidate, or accept this coverage/access gap in the readiness score. |
| DE | DE-NI-001 | Dataset-resolved verification did not confirm usable access for DE-NI-001 (Niedersächsischer Landesbetrieb für Wasserwirtschaft, Küsten- und Naturschutz — Lower Saxony Environmental Maps - Flood). Classification: lead / generic_portal. The link is a generic agency or geoportal entry point; the named dataset was not resolved. | Human review: provide a current authoritative dataset-specific viewer, document, service, API, or download as a superseding candidate, or accept this coverage/access gap in the readiness score. |
| CN | CN-MWR-001 | Dataset-resolved verification did not confirm usable access for CN-MWR-001 (中华人民共和国水利部 / Ministry of Water Resources — National Flood Risk Map Programme). Classification: lead / restricted. Access is restricted and no public dataset path was confirmed. | Human review: provide a current authoritative dataset-specific viewer, document, service, API, or download as a superseding candidate, or accept this coverage/access gap in the readiness score. |
| CN | CN-MEM-001 | Dataset-resolved verification did not confirm usable access for CN-MEM-001 (中华人民共和国应急管理部 / Ministry of Emergency Management — First National Comprehensive Natural Disaster Risk Survey). Classification: lead / restricted. Access is restricted and no public dataset path was confirmed. | Human review: provide a current authoritative dataset-specific viewer, document, service, API, or download as a superseding candidate, or accept this coverage/access gap in the readiness score. |
| CN | CN-SD-001 | Dataset-resolved verification did not confirm usable access for CN-SD-001 (山东省水利厅 — Shandong Flood Risk Maps). Classification: lead / restricted. Access is restricted and no public dataset path was confirmed. | Human review: provide a current authoritative dataset-specific viewer, document, service, API, or download as a superseding candidate, or accept this coverage/access gap in the readiness score. |
| CN | CN-SC-001 | Dataset-resolved verification did not confirm usable access for CN-SC-001 (四川省水利厅 — Sichuan Flood and Flash-Flood Risk Maps). Classification: lead / restricted. Access is restricted and no public dataset path was confirmed. | Human review: provide a current authoritative dataset-specific viewer, document, service, API, or download as a superseding candidate, or accept this coverage/access gap in the readiness score. |
| CA | CA-OPENMAPS-001 | Dataset-resolved verification did not confirm usable access for CA-OPENMAPS-001 (Government of Canada — Open Maps Flood Geospatial Catalogue). Classification: unavailable / unavailable. The link is a catalogue/search entry point rather than a dataset-specific record. | Human review: provide a current authoritative dataset-specific viewer, document, service, API, or download as a superseding candidate, or accept this coverage/access gap in the readiness score. |
| FR | FR-GEORISQUES-001 | Dataset-resolved verification did not confirm usable access for FR-GEORISQUES-001 (Ministère de la Transition écologique / BRGM — Georisques Flood Data). Classification: lead / catalogue_search. The link is a catalogue/search entry point rather than a dataset-specific record. | Human review: provide a current authoritative dataset-specific viewer, document, service, API, or download as a superseding candidate, or accept this coverage/access gap in the readiness score. |
| FR | FR-GPU-001 | Dataset-resolved verification did not confirm usable access for FR-GPU-001 (Ministère de la Transition écologique — Urban Planning Geoportal - Risk Prevention Plans). Classification: lead / generic_portal. The link is a generic agency or geoportal entry point; the named dataset was not resolved. | Human review: provide a current authoritative dataset-specific viewer, document, service, API, or download as a superseding candidate, or accept this coverage/access gap in the readiness score. |
| MX | MX-CONAGUA-001 | Dataset-resolved verification did not confirm usable access for MX-CONAGUA-001 (Comisión Nacional del Agua — National Water Information System). Classification: lead / catalogue_search. The link is a catalogue/search entry point rather than a dataset-specific record. | Human review: provide a current authoritative dataset-specific viewer, document, service, API, or download as a superseding candidate, or accept this coverage/access gap in the readiness score. |
| MX | MX-INEGI-001 | Dataset-resolved verification did not confirm usable access for MX-INEGI-001 (Instituto Nacional de Estadística y Geografía — SIATL Watershed Flow Simulator). Classification: lead / ambiguous. The page resolves, but dataset identity or usable access could not be confirmed. | Human review: provide a current authoritative dataset-specific viewer, document, service, API, or download as a superseding candidate, or accept this coverage/access gap in the readiness score. |
| MX | MX-JAL-001 | Dataset-resolved verification did not confirm usable access for MX-JAL-001 (Unidad Estatal de Protección Civil y Bomberos Jalisco — Jalisco State Risk Atlas). Classification: lead / generic_portal. The link is a generic agency or geoportal entry point; the named dataset was not resolved. | Human review: provide a current authoritative dataset-specific viewer, document, service, API, or download as a superseding candidate, or accept this coverage/access gap in the readiness score. |
| MY | MY-JPS-001 | Dataset-resolved verification did not confirm usable access for MY-JPS-001 (Jabatan Pengairan dan Saliran Malaysia / Department of Irrigation and Drainage — Public Flood Information Portal). Classification: lead / wrong_product. The reachable product is operational or observational, not a confirmed flood-hazard dataset. | Human review: provide a current authoritative dataset-specific viewer, document, service, API, or download as a superseding candidate, or accept this coverage/access gap in the readiness score. |
| MY | MY-NAHRIM-001 | Dataset-resolved verification did not confirm usable access for MY-NAHRIM-001 (National Water Research Institute of Malaysia (NAHRIM) — NAHRIM Flood and Climate Risk Products). Classification: lead / generic_portal. The link is a generic agency or geoportal entry point; the named dataset was not resolved. | Human review: provide a current authoritative dataset-specific viewer, document, service, API, or download as a superseding candidate, or accept this coverage/access gap in the readiness score. |
| MY | MY-SBH-001 | Dataset-resolved verification did not confirm usable access for MY-SBH-001 (Jabatan Pengairan dan Saliran Sabah — Sabah Flood Hazard Maps). Classification: lead / generic_portal. The link is a generic agency or geoportal entry point; the named dataset was not resolved. | Human review: provide a current authoritative dataset-specific viewer, document, service, API, or download as a superseding candidate, or accept this coverage/access gap in the readiness score. |
| MY | MY-SWK-001 | Dataset-resolved verification did not confirm usable access for MY-SWK-001 (Department of Irrigation and Drainage Sarawak — Sarawak Flood Hazard and Drainage Maps). Classification: lead / generic_portal. The link is a generic agency or geoportal entry point; the named dataset was not resolved. | Human review: provide a current authoritative dataset-specific viewer, document, service, API, or download as a superseding candidate, or accept this coverage/access gap in the readiness score. |
| PL | PL-GUGIK-001 | Dataset-resolved verification did not confirm usable access for PL-GUGIK-001 (Główny Urząd Geodezji i Kartografii — National Geoportal Flood Hazard Layers). Classification: lead / ambiguous. The page resolves, but dataset identity or usable access could not be confirmed. | Human review: provide a current authoritative dataset-specific viewer, document, service, API, or download as a superseding candidate, or accept this coverage/access gap in the readiness score. |
| BE | BE-VLG-002 | Dataset-resolved verification did not confirm usable access for BE-VLG-002 (Digitaal Vlaanderen — Geopunt Flood-Susceptibility Layers). Classification: lead / catalogue_search. The link is a catalogue/search entry point rather than a dataset-specific record. | Human review: provide a current authoritative dataset-specific viewer, document, service, API, or download as a superseding candidate, or accept this coverage/access gap in the readiness score. |
| BE | BE-WAL-001 | Dataset-resolved verification did not confirm usable access for BE-WAL-001 (Service public de Wallonie — Wallonia Flood Hazard Maps). Classification: lead / catalogue_search. The link is a catalogue/search entry point rather than a dataset-specific record. | Human review: provide a current authoritative dataset-specific viewer, document, service, API, or download as a superseding candidate, or accept this coverage/access gap in the readiness score. |
| IT | IT-SIC-001 | Dataset-resolved verification did not confirm usable access for IT-SIC-001 (Autorità di bacino del Distretto Idrografico della Sicilia — Sicily Flood Risk Management Plan Maps). Classification: lead / ambiguous. The page resolves, but dataset identity or usable access could not be confirmed. | Human review: provide a current authoritative dataset-specific viewer, document, service, API, or download as a superseding candidate, or accept this coverage/access gap in the readiness score. |
| CH | CH-ZH-001 | Dataset-resolved verification did not confirm usable access for CH-ZH-001 (Kanton Zürich — Zurich Flood Natural-Hazard Map). Classification: lead / generic_portal. The link is a generic agency or geoportal entry point; the named dataset was not resolved. | Human review: provide a current authoritative dataset-specific viewer, document, service, API, or download as a superseding candidate, or accept this coverage/access gap in the readiness score. |
| CH | CH-VD-001 | Dataset-resolved verification did not confirm usable access for CH-VD-001 (État de Vaud — Vaud Natural-Hazard Flood Maps). Classification: lead / generic_portal. The link is a generic agency or geoportal entry point; the named dataset was not resolved. | Human review: provide a current authoritative dataset-specific viewer, document, service, API, or download as a superseding candidate, or accept this coverage/access gap in the readiness score. |
| CH | CH-AG-001 | Dataset-resolved verification did not confirm usable access for CH-AG-001 (Kanton Aargau — Aargau Flood Hazard Map). Classification: lead / ambiguous. The page resolves, but dataset identity or usable access could not be confirmed. | Human review: provide a current authoritative dataset-specific viewer, document, service, API, or download as a superseding candidate, or accept this coverage/access gap in the readiness score. |
| CH | CH-SG-001 | Dataset-resolved verification did not confirm usable access for CH-SG-001 (Kanton St. Gallen — St. Gallen Water Natural-Hazard Map). Classification: lead / generic_portal. The link is a generic agency or geoportal entry point; the named dataset was not resolved. | Human review: provide a current authoritative dataset-specific viewer, document, service, API, or download as a superseding candidate, or accept this coverage/access gap in the readiness score. |
| IE | IE-DATA-001 | Dataset-resolved verification did not confirm usable access for IE-DATA-001 (Office of Public Works / data.gov.ie — Irish Flood Map Open Data). Classification: lead / catalogue_search. The link is a catalogue/search entry point rather than a dataset-specific record. | Human review: provide a current authoritative dataset-specific viewer, document, service, API, or download as a superseding candidate, or accept this coverage/access gap in the readiness score. |
| TH | TH-DWR-001 | Dataset-resolved verification did not confirm usable access for TH-DWR-001 (กรมทรัพยากรน้ำ / Department of Water Resources — Water Resources GIS and Flood-Risk Maps). Classification: lead / catalogue_search. The link is a catalogue/search entry point rather than a dataset-specific record. | Human review: provide a current authoritative dataset-specific viewer, document, service, API, or download as a superseding candidate, or accept this coverage/access gap in the readiness score. |
| AE | AE-RAK-001 | Dataset-resolved verification did not confirm usable access for AE-RAK-001 (Ras Al Khaimah Municipality — Ras Al Khaimah Flood and Drainage Geodata). Classification: lead / request_only. Access requires a data request; no public dataset path was confirmed. | Human review: provide a current authoritative dataset-specific viewer, document, service, API, or download as a superseding candidate, or accept this coverage/access gap in the readiness score. |
| ZA | ZA-SARVA-001 | Dataset-resolved verification did not confirm usable access for ZA-SARVA-001 (South African Environmental Observation Network / government partners — South African Risk and Vulnerability Atlas). Classification: lead / generic_portal. The link is a generic agency or geoportal entry point; the named dataset was not resolved. | Human review: provide a current authoritative dataset-specific viewer, document, service, API, or download as a superseding candidate, or accept this coverage/access gap in the readiness score. |
| ZA | ZA-NDMC-001 | Dataset-resolved verification did not confirm usable access for ZA-NDMC-001 (National Disaster Management Centre — National Disaster Risk GIS). Classification: lead / generic_portal. The link is a generic agency or geoportal entry point; the named dataset was not resolved. | Human review: provide a current authoritative dataset-specific viewer, document, service, API, or download as a superseding candidate, or accept this coverage/access gap in the readiness score. |
| ZA | ZA-KZN-001 | Dataset-resolved verification did not confirm usable access for ZA-KZN-001 (KwaZulu-Natal Provincial Disaster Management Centre / eThekwini Municipality — KwaZulu-Natal Flood Risk and Floodline Maps). Classification: lead / request_only. Access requires a data request; no public dataset path was confirmed. | Human review: provide a current authoritative dataset-specific viewer, document, service, API, or download as a superseding candidate, or accept this coverage/access gap in the readiness score. |
| ZA | ZA-EC-001 | Dataset-resolved verification did not confirm usable access for ZA-EC-001 (Eastern Cape Provincial Disaster Management Centre — Eastern Cape Flood Risk Maps). Classification: lead / request_only. Access requires a data request; no public dataset path was confirmed. | Human review: provide a current authoritative dataset-specific viewer, document, service, API, or download as a superseding candidate, or accept this coverage/access gap in the readiness score. |
| ZA | ZA-LP-001 | Dataset-resolved verification did not confirm usable access for ZA-LP-001 (Limpopo Provincial Disaster Management Centre — Limpopo Flood Risk Maps). Classification: lead / request_only. Access requires a data request; no public dataset path was confirmed. | Human review: provide a current authoritative dataset-specific viewer, document, service, API, or download as a superseding candidate, or accept this coverage/access gap in the readiness score. |
| KR | KR-SAFEMAP-001 | Dataset-resolved verification did not confirm usable access for KR-SAFEMAP-001 (행정안전부 — National Safety Map - Inundation and Disaster Safety). Classification: lead / generic_portal. The link is a generic agency or geoportal entry point; the named dataset was not resolved. | Human review: provide a current authoritative dataset-specific viewer, document, service, API, or download as a superseding candidate, or accept this coverage/access gap in the readiness score. |
| KR | KR-DATA-001 | Dataset-resolved verification did not confirm usable access for KR-DATA-001 (공공데이터포털 — Korea Public Data Portal Flood Map Datasets). Classification: lead / catalogue_search. The link is a catalogue/search entry point rather than a dataset-specific record. | Human review: provide a current authoritative dataset-specific viewer, document, service, API, or download as a superseding candidate, or accept this coverage/access gap in the readiness score. |

## How this table was generated (AI agentic search)

This review was produced by an AI agentic-search pipeline, not by manual literature review. The working brief given to the agents was:

> For each of twenty priority countries, identify the authoritative government (or official intergovernmental) sources that publish flood **hazard** mapping, prioritizing jurisdictions by population. Every country's source set must cover each applicable flood-hazard family — **fluvial** (river), **coastal**, and **surface water** (pluvial / stormwater) — or explicitly record why a family does not apply. For each source capture the publishing agency, dataset, flood types, scenarios (return periods), spatial coverage and resolution, formats, licence, and access/delivery mode, with a working link. Describe each country's data readiness and flag every source whose dataset cannot be confirmed.

The pipeline runs as two independent agent roles with a strict separation of duties, so that the agent making claims is never the agent that confirms them:

1. **Discovery.** A discovery agent runs bounded web search per country (capped numbers of searches, page reads, and service-capability probes) and emits *unverified* candidate sources covering the required hazard families. It may not assign scores or verification status.
2. **Verification.** A separate verification agent checks reachability, publisher authority, dataset identity, and human usability. Services are capability-probed for relevant flood layers; downloads must return a data response rather than HTML; dynamic viewers and dataset pages require a bounded browser audit. Generic portals, catalogue searches, restricted or request-only paths, and ambiguous products are retained as leads but are not verified. Raw service payloads are read only by dedicated validation tools and never enter model reasoning.
3. **Assessment.** Each country is described across six explicit factors — geographic completeness, scenario richness, technical accessibility, documentation currency, licensing, and integration effort — used as evaluation lenses (see "How to use this report") rather than collapsed into a single grade. The emphasis is on what exists and how usable it is.
4. **Findings and human review.** Any material source that fails verification generates a structured finding. One automated rediscovery round is permitted to find a replacement; anything still unresolved is escalated to the **Human review required** section rather than dropped or silently guessed.
5. **Build.** This report is rendered deterministically from versioned, schema-validated JSON artifacts; the prose is generated, the underlying facts are not.

Because discovery is automated and the live web changes, links can break between verification and reading. The **Verification** columns and the human-review section are the authoritative record of what was confirmed and when.
