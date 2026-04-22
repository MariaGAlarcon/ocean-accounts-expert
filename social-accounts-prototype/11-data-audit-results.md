# Data Audit Results: Australia and Fiji

Data audit conducted 2026-04-22 using web research. Access conditions should be re-verified before beginning data work, as portals change.

---

## Australia

### Summary

| # | Data need | Source | Downloadable? | Format | Resolution | Household disagg? | Access |
|---|---|---|---|---|---|---|---|
| 1 | Fisheries catch and value | ABARES Fisheries and Aquaculture Statistics | Yes | PDF reports, Excel tables, dashboard | By fishery, species, state | No (industry-level) | Free, open |
| 2 | Stock status | ABARES Fishery Status Reports 2025 + dashboard | Yes | Interactive dashboard, downloadable map data | By stock, species group, fishery | No | Free, open |
| 3 | Household fish consumption | ABS Household Expenditure Survey (2015-16, most recent) | Partial | Summary tables free; microdata via DataLab or CURF | National, state | By income quintile, household type | Summary: free. Microdata: registration required (free) |
| 4 | Household income distribution | ABS Distribution of Household Income, Consumption and Wealth (2021-22) | Yes | Excel tables | National | By income decile, wealth quintile | Free, open |
| 5 | Time use (unpaid labour) | ABS Time Use Survey (2020-21) | Yes | Excel tables | National, state | By gender, age, household type | Free, open |
| 6 | Reef condition | AIMS Long-Term Monitoring Program | Yes | Annual reports; reef-level data via Reef Dashboard | Individual reef, GBR regions | N/A (spatial) | Free, open |
| 7 | GBR socioeconomic | CSIRO SELTMP (2013, 2017, 2021, 2023) | Partial | 2013 data on CSIRO Data Portal; dashboards for 2023 | GBR communities/regions | By community, income, age | 2013 data: free. Later waves: check CSIRO portal |
| 8 | Tourism visitors | Tourism Research Australia (NVS ended Dec 2024; replaced by DoTS from Jan 2025) | Partial | TRA Online (subscription) for detailed tables; summary reports free | State, tourism region | Limited | Summaries: free. Detailed: subscription |
| 9 | Employment by industry | ABS Census 2021 via TableBuilder | Yes | Custom tables (ANZSIC x SA2 x demographics) | SA2 (fine-grained) | By industry, gender, age, income | Free registration required |
| 10 | Reef/mangrove extent | Allen Coral Atlas + Global Mangrove Watch | Yes | Raster (5m resolution), GIS layers | Reef-level, global | N/A (spatial) | Free, open |

### Source details

**1. ABARES Fisheries and Aquaculture Statistics**
- Annual report with production, trade, consumption, and employment data for all Australian fisheries.
- Fishery Status Reports 2025 cover stocks representing $403M GVP (25% of total wild-catch).
- Stock Status Dashboard: interactive, filterable data from 1992 to 2024.
- Source: [ABARES Fisheries Statistics](https://www.agriculture.gov.au/abares/research-topics/fisheries/fisheries-and-aquaculture-statistics)
- Source: [Fisheries Data](https://www.agriculture.gov.au/abares/research-topics/fisheries/fisheries-data)
- Source: [Stock Status Dashboard](https://www.agriculture.gov.au/abares/research-topics/fisheries/fishery-status/stock-status-dashboard)
- Evidence level: Tier 1 (government)

**3. ABS Household Expenditure Survey**
- Most recent: 2015-16 (collected every 6 years; 2021-22 collection likely but not yet released as of April 2026).
- Summary tables include expenditure on food by broad category. Fish-specific consumption by income quintile may require microdata access.
- Microdata available via DataLab (free registration) or CURF. Contact: microdata.access@abs.gov.au
- Source: [HES Summary](https://www.abs.gov.au/statistics/economy/finance/household-expenditure-survey-australia-summary-results/latest-release)
- Evidence level: Tier 1 (government)

**5. ABS Time Use Survey 2020-21**
- Covers daily activities of people aged 15+. Excel tables downloadable.
- Includes unpaid household labour by gender and household type -- directly relevant for social activity supply tables.
- Source: [How Australians Use Their Time 2020-21](https://www.abs.gov.au/statistics/people/people-and-communities/how-australians-use-their-time/2020-21)
- Evidence level: Tier 1 (government)

**7. CSIRO SELTMP**
- Tracks community perceptions, reef dependency, and socioeconomic conditions for GBR communities.
- 2013 data publicly available: [CSIRO Data Portal](https://data.csiro.au/collection/csiro:61731)
- 2023 data dashboards: [SELTMP Research](https://research.csiro.au/seltmp/)
- Publications: [SELTMP Publications](https://research.csiro.au/seltmp/publications/)
- Evidence level: Tier 1 (government research agency)

**8. Tourism Research Australia**
- NVS ended December 2024; replaced by Domestic Tourism Statistics (DoTS) from January 2025.
- Detailed data requires TRA Online subscription. Summary reports and trends freely available.
- Source: [TRA Data and Research](https://www.tra.gov.au/en/data-and-research)
- Evidence level: Tier 1 (government)

**9. ABS Census 2021 TableBuilder**
- Free tool (registration required) to build custom tables crossing industry (ANZSIC) with geography (SA2), demographics, income.
- Can extract: number of people employed in fishing (ANZSIC 0411) by SA2, gender, age, income bracket.
- Source: [Census TableBuilder](https://www.abs.gov.au/census/guide-census-data/about-census-tools/tablebuilder)
- Evidence level: Tier 1 (government)

### Australia: strengths and gaps

**Strengths:**
- Fisheries catch/value data is comprehensive and annually updated.
- Census TableBuilder gives fine-grained (SA2) employment data by industry, crossable with demographics.
- Time Use Survey provides unpaid labour data by gender -- critical for social activity tables.
- AIMS LTMP provides one of the best reef condition time series globally.
- SELTMP is one of few programs worldwide tracking community perceptions of reef dependence.

**Gaps:**
- HES fish consumption data is from 2015-16 -- 10 years old. Updated microdata may not yet be released.
- Tourism data transition (NVS to DoTS) creates a gap; marine-specific tourism disaggregation is limited.
- No direct link between household surveys and specific ecosystem assets (BSU-level join requires custom GIS work).
- Indigenous marine use data was not found in open-access form -- likely access-restricted.

---

## Fiji

### Summary

| # | Data need | Source | Downloadable? | Format | Resolution | Household disagg? | Access |
|---|---|---|---|---|---|---|---|
| 1 | Household income, expenditure, fish consumption | Fiji Bureau of Statistics HIES 2019-20 | Partial | Summary report published; microdata may require formal request | National, urban/rural, provincial | By income quintile, location | Summary: free. Microdata: contact FBS |
| 2 | Census (fishing communities) | Fiji Census 2017 | Partial | Population tables by tikina; agriculture/fishing module included | Tikina level (admin level 3) | By occupation, location, ethnicity | Summary tables: free. Detailed tables: contact FBS |
| 3 | Fisheries catch (commercial) | FAO FishStatJ | Yes | Queryable database | National, by species | No | Free, open |
| 4 | Coastal fisheries (community-level) | SPC PROCFish/C Fiji 2002-2003 | Yes | Darwin Core Archive via GBIF/Pacific Data Hub | Site-level (5 sites) | No (species/abundance data) | Free, open |
| 5 | Reef extent | Allen Coral Atlas | Yes | Raster (5m), GIS layers, statistics by EEZ/MPA | Reef-level | N/A (spatial) | Free, open |
| 6 | Mangrove extent | Global Mangrove Watch | Yes | Raster, GIS layers | Global, 25m resolution | N/A (spatial) | Free, open |
| 7 | Marine ecosystem service values | MACBIO Fiji National MESV (2017) | Yes | PDF report | National, some by service type | No | Free download |
| 8 | Qoliqoli boundaries | iTaukei Affairs Board / FLMMA / MACBIO Marine Atlas | Partial | GIS layers exist; access varies | Qoliqoli area (411 registered) | N/A (spatial) | Research use: check SPREP/MACBIO portals |
| 9 | Tourism | Fiji Bureau of Statistics | Partial | Summary tables | National | By sector | Contact FBS |
| 10 | Subnational admin boundaries | HDX / Pacific Data Hub | Yes | Shapefiles (division, province, tikina) | Tikina level | N/A (spatial) | Free, open |

### Source details

**1. Fiji HIES 2019-20**
- 6,000-household sample; conducted Feb 2019 to Feb 2020.
- Includes consumption module (food by source: purchased, own production, gifted).
- Key poverty finding: 258,000 people below Basic Needs Poverty Line.
- Summary report published. Microdata access may require formal request to FBS.
- Source: [Fiji HIES 2019-20](https://www.statsfiji.gov.fj/2019-20-hies/)
- SPC catalog: [SDD Collection](https://sdd.spc.int/collection/2019-Household-income-and-expenditure-survey-collection-fiji-0)
- Evidence level: Tier 1 (government)

**2. Fiji Census 2017**
- Includes Module H: Agriculture and Fishing (9 questions).
- Population data available at tikina level (admin level 3).
- Tikina dashboards being developed by FBS.
- Source: [Census of Population and Housing](https://www.statsfiji.gov.fj/census-surveys/census-of-population-and-housing/)
- Evidence level: Tier 1 (government)

**4. SPC PROCFish/C Fiji 2002-2003**
- Underwater Visual Census data: fish species, abundance, body length across 5 sites (Dromuna, Muaivuso, Mali, Lakeba, Labeka Island).
- 7,612 records in core data table.
- Also available: invertebrate observations from same sites.
- Source: [GBIF](https://www.gbif.org/dataset/806eae29-ea28-409f-9d95-f7b1f06f0448)
- Source: [Pacific Data Hub](https://pacificdata.org/data/dataset/806eae29-ea28-409f-9d95-f7b1f06f0448)
- Note: Data is from 2002-2003 -- over 20 years old. Useful as a baseline but not current.
- Evidence level: Tier 1 (intergovernmental: SPC)

**7. MACBIO Fiji National MESV**
- Marine ecosystem services valued at FJ$2.5 billion annually (2014 data).
- Covers fisheries, tourism, coastal protection, carbon, and other services.
- Prepared by University of the South Pacific under GIZ/IUCN/SPREP.
- Full report: [MACBIO Fiji MESV PDF](http://macbio-pacific.info/wp-content/uploads/2017/10/Fiji-MESV-Digital-LowRes.pdf)
- Evidence level: Tier 2 (university research under intergovernmental project)

**8. Qoliqoli boundaries**
- 411 registered qoliqoli areas covering approximately 30,011 km2.
- Boundaries loosely follow reef geomorphology (outer limits often defined by outer reef edges).
- GIS data exists (referenced in FLMMA maps and MACBIO Marine Atlas).
- Access: check [SPREP Pacific Environment Data Portal](https://pacific-data.sprep.org/data-dashboard/gis-spatial-data-dashboard) and MACBIO Marine Atlas.
- Evidence level: Tier 1 (government registry via iTaukei Affairs Board)

### Fiji: strengths and gaps

**Strengths:**
- HIES 2019-20 includes food consumption by source (purchased vs own production vs gifted) -- directly tests subsistence boundary question.
- Census 2017 includes agriculture/fishing module with tikina-level resolution.
- MACBIO provides aggregate ecosystem service values as a reference frame.
- Qoliqoli system provides a natural spatial unit linking marine tenure to communities (potentially usable as BSU proxy).
- Allen Coral Atlas provides current reef extent at 5m resolution.
- Subnational boundary shapefiles (tikina) available via HDX -- enables spatial joins.

**Gaps:**
- HIES microdata may require formal request. Fish consumption disaggregation by income quintile may not be in the published summary.
- PROCFish data is from 2002-2003 -- old. More recent coastal fisheries monitoring data may exist but was not found in open-access form.
- No time-use survey found for Fiji (limits ability to populate social activity supply tables).
- Aquaculture data is limited (FAO has national totals but no subnational or household-level data).
- Qoliqoli boundary GIS data access needs verification -- may require request to iTaukei Affairs Board or FLMMA.
- Tourism employment data lacks detailed disaggregation.

---

## Comparative assessment

| Criterion | Australia | Fiji |
|---|---|---|
| Fisheries catch data | Strong (annual, by fishery) | Moderate (FAO national; PROCFish old) |
| Household fish consumption | Moderate (HES 2015-16, aging) | Strong potential (HIES 2019-20 with subsistence split) |
| Employment by industry | Strong (Census SA2 x ANZSIC) | Moderate (Census tikina, fishing module) |
| Time-use data | Strong (TUS 2020-21) | Not available |
| Reef/mangrove extent | Strong (AIMS + Allen Atlas) | Strong (Allen Atlas) |
| Ecosystem service values | Moderate (SELTMP for GBR) | Strong (MACBIO national valuation) |
| Spatial units for BSU | Strong (SA2, reef monitoring regions) | Strong potential (qoliqoli + tikina) |
| Subsistence fishing | Weak (small share of economy) | Strong (major food pathway) |
| Cultural services data | Weak (access-restricted Indigenous data) | Moderate (qoliqoli system, but data access unclear) |
| Household disaggregation | Strong (ABS quintiles, demographics) | Moderate (HIES quintiles if microdata accessible) |

### Recommendation

Start with **Australia for fish provisioning** (Step 2 of workflow guide) because the data is most readily accessible and the distributional supply-use table can be populated using published ABARES + ABS data without formal data requests.

In parallel, **request Fiji HIES microdata** from FBS (contact: info@statsfiji.gov.fj) and begin the Fiji pilot when the data arrives. Fiji is the stronger test case for non-market pathways, subsistence boundary, and cultural services.

---

## Sources

### Australia
- [ABARES Fisheries and Aquaculture Statistics](https://www.agriculture.gov.au/abares/research-topics/fisheries/fisheries-and-aquaculture-statistics)
- [ABARES Fisheries Data](https://www.agriculture.gov.au/abares/research-topics/fisheries/fisheries-data)
- [ABARES Fishery Status Reports 2025](https://www.agriculture.gov.au/abares/research-topics/fisheries/fishery-status)
- [ABARES Stock Status Dashboard](https://www.agriculture.gov.au/abares/research-topics/fisheries/fishery-status/stock-status-dashboard)
- [ABS Household Expenditure Survey](https://www.abs.gov.au/statistics/economy/finance/household-expenditure-survey-australia-summary-results/latest-release)
- [ABS Distribution of Household Income, Consumption and Wealth](https://www.abs.gov.au/statistics/economy/national-accounts/australian-national-accounts-distribution-household-income-consumption-and-wealth/latest-release)
- [ABS How Australians Use Their Time 2020-21](https://www.abs.gov.au/statistics/people/people-and-communities/how-australians-use-their-time/2020-21)
- [ABS Census TableBuilder](https://www.abs.gov.au/census/guide-census-data/about-census-tools/tablebuilder)
- [AIMS Long-Term Monitoring Program](https://www.aims.gov.au/research-topics/monitoring-and-discovery/monitoring-great-barrier-reef/long-term-monitoring-program)
- [AIMS Reef Condition Summary 2024/25](https://www.aims.gov.au/monitoring-great-barrier-reef/gbr-condition-summary-2024-25)
- [CSIRO SELTMP](https://research.csiro.au/seltmp/)
- [CSIRO SELTMP 2013 Data](https://data.csiro.au/collection/csiro:61731)
- [Tourism Research Australia](https://www.tra.gov.au/en/data-and-research)
- [Allen Coral Atlas](https://allencoralatlas.org/)

### Fiji
- [Fiji Bureau of Statistics HIES 2019-20](https://www.statsfiji.gov.fj/2019-20-hies/)
- [Fiji Census of Population and Housing](https://www.statsfiji.gov.fj/census-surveys/census-of-population-and-housing/)
- [SPC PROCFish/C Fiji 2002-2003 (GBIF)](https://www.gbif.org/dataset/806eae29-ea28-409f-9d95-f7b1f06f0448)
- [SPC PROCFish/C Fiji 2002-2003 (Pacific Data Hub)](https://pacificdata.org/data/dataset/806eae29-ea28-409f-9d95-f7b1f06f0448)
- [FAO FishStatJ](https://www.fao.org/fishery/statistics/software/fishstatj/en)
- [MACBIO Fiji National MESV Report](http://macbio-pacific.info/wp-content/uploads/2017/10/Fiji-MESV-Digital-LowRes.pdf)
- [MACBIO Project](http://macbio-pacific.info/)
- [Allen Coral Atlas](https://allencoralatlas.org/)
- [SPREP Pacific Environment Data Portal](https://pacific-data.sprep.org/data-dashboard/gis-spatial-data-dashboard)
- [Fiji Subnational Boundaries (HDX)](https://data.humdata.org/dataset/cod-ab-fji)
- [SDD/SPC HIES Collection](https://sdd.spc.int/collection/2019-Household-income-and-expenditure-survey-collection-fiji-0)
