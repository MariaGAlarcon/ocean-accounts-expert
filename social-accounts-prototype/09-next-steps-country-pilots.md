# Next Steps: Country Pilot Examples

This document outlines the plan for testing the social accounts prototype with real, open-access data. The goal is to select two countries, identify five representative ecosystem services, and build worked examples that trace flows from ecosystem assets through to household-level social conditions.

---

## Country selection

### Australia

**Rationale:** Australia has among the most comprehensive open environmental and socioeconomic data systems globally. The Great Barrier Reef has decades of monitoring data with socioeconomic surveys. The Australian Bureau of Statistics (ABS) produces detailed household surveys with industry-level disaggregation.

**Key data sources (to be verified for current access):**

| Data need | Likely source | Resolution | Household disagg? |
|---|---|---|---|
| Fisheries catch and value | ABARES Fisheries Statistics, Australian Fisheries Management Authority | State, fishery level | No (industry level) |
| Fishing employment | ABS Labour Force Survey, Census (ISIC/ANZSIC) | State, SA2 level | By industry, gender, formality |
| Household fish consumption | ABS Household Expenditure Survey | National, state | By income quintile |
| Reef/mangrove extent | AIMS Long-Term Monitoring Program, Allen Coral Atlas, Global Mangrove Watch | Reef-level, 10m resolution | N/A (spatial) |
| Coastal protection | Geoscience Australia coastal risk data, Bureau of Meteorology | Local government area | Can overlay with census |
| Marine tourism | Tourism Research Australia, Tourism Satellite Account (ABS) | State, tourism region | Employment by gender |
| Aquaculture production | ABARES Aquaculture Statistics | State, species level | No |
| Indigenous marine use | AIATSIS, Native Title records, Indigenous ranger programs | Varies, often community-level | Sensitive data, access restrictions likely |
| Time-use survey | ABS Time Use Survey (2020-21 most recent) | National, state | By gender, household type |
| GBR socioeconomic monitoring | GBRMPA Social and Economic Long-Term Monitoring Program (SELTMP) | GBR regions | By community, income, age |

**Strengths:** Very strong on fisheries economics, tourism employment, household expenditure, and reef condition monitoring. SELTMP is one of the few programs globally that tracks community perceptions of reef dependence over time.

**Gaps:** Indigenous marine use data may have access restrictions. Linking household surveys to specific ecosystem assets (BSU-level) requires custom geospatial analysis. Subsistence fishing is small relative to Pacific Island nations, limiting the test of E10 non-market pathways.

### Fiji

**Rationale:** Fiji is a Pacific Island nation where subsistence fishing is a major food security pathway, customary marine tenure (qoliqoli) is legally recognized, and the social dimensions of ocean use are central to livelihoods. This makes Fiji the stronger test case for non-market social flows (E10), the subsistence boundary question (File 07), and cultural services.

**Key data sources (to be verified for current access):**

| Data need | Likely source | Resolution | Household disagg? |
|---|---|---|---|
| Fisheries catch (commercial) | Fiji Ministry of Fisheries, FAO FishStatJ | National, some by species | No |
| Subsistence fishing | Fiji HIES (fish consumption module), SPC PROCFish surveys | National, provincial, some community | By income, location, gender |
| Household income and expenditure | Fiji Bureau of Statistics HIES (2019-20 most recent) | National, urban/rural, provincial | By income quintile, location |
| Census (fishing communities) | Fiji Bureau of Statistics Census (2017) | Tikina/district level | By occupation, location, ethnicity |
| Reef/mangrove extent | Allen Coral Atlas, Global Mangrove Watch, MACBIO project | Reef-level spatial data | N/A (spatial) |
| Marine ecosystem services valuation | MACBIO project outputs (GIZ/IUCN/SPREP) | National, some by province | N/A (aggregate values) |
| Tourism | Fiji Bureau of Statistics, Tourism Fiji | National | Employment by sector |
| Aquaculture | FAO, Ministry of Fisheries | National | Limited |
| Customary marine tenure (qoliqoli) | iTaukei Affairs Board, published research | By qoliqoli area | Community-level |
| Coastal fisheries monitoring | SPC PROCFish/C, community-based monitoring | Site-level | By community, gender |

**Strengths:** Fiji's HIES includes detailed fish consumption data that can be disaggregated by income and location. The MACBIO project produced ecosystem service valuations. SPC PROCFish provides community-level fisheries data. Customary tenure (qoliqoli) provides a natural spatial unit for linking social and ecosystem data. Subsistence fishing is large and well-documented relative to other countries.

**Gaps:** Microdata from HIES and census may require formal data request from Fiji Bureau of Statistics. Time-use survey data may not exist in the form needed for social activity tables. Aquaculture data is limited. Tourism employment data may lack the disaggregation needed.

---

## Recommended five ecosystem services for pilot

These five were selected for data richness and coverage of both market (E9) and non-market (E10) pathways:

| # | Ecosystem service | Type | Primary pathway | Why this service |
|---|---|---|---|---|
| 1 | Fish provisioning (capture fisheries) | Provisioning | Market (E9) + Non-market (E10 for subsistence) | Most data-rich; tests the subsistence boundary question; affects material wellbeing, employment, food security |
| 2 | Coastal protection (reefs and mangroves) | Regulating | Non-market (E10) | Tests spatial distribution of benefits; strongly linked to vulnerability and equity; can overlay with household census data |
| 3 | Marine recreation/tourism | Cultural | Market (E9) + Non-market (E10) | Tests both market (tourism employment) and non-market (resident recreation) pathways; good employment data |
| 4 | Subsistence gleaning (shellfish, seaweed) | Provisioning | Non-market (E10) | Strongly gendered; tests E10 pathway; central to food security for poorest households; best tested with Fiji data |
| 5 | Cultural/spiritual services (traditional practices) | Cultural | Non-market (E10) | Tests the most challenging social flows; linked to customary governance and knowledge transmission; unique to Fiji's qoliqoli system |

### What the pilot would trace for each service

For each of the five services, the pilot would attempt to populate:
1. The ecosystem asset baseline (extent and condition from ecosystem accounts or proxies)
2. The ecosystem service flow (physical quantity from services data)
3. The household disaggregation of service use (from HIES, census, or survey data)
4. The social condition indicators affected (from social stock tables)
5. The social activity flows involved (from time-use or community survey data)

---

## Questions to explore through examples

### Double counting

Fish provisioning is the primary test case. The same fish cannot appear as both E9 (market) and E10 (non-market) flow. The pilot should:
- Split total catch into commercial and subsistence components using HIES or fisheries census data
- Verify that the split is exhaustive (all fish accounted for) and exclusive (no fish counted twice)
- Test whether the "product in E9, activity in E10" resolution from File 07 works in practice
- Check whether household-level consumption data (from HIES) reconciles with total catch data (from fisheries statistics)

Coastal protection is the second test case. Protection benefits are non-rival (all buildings in the zone benefit), but the distributional table allocates benefits to household groups. Does the sum of household-level benefits exceed total service supply? It should not, but the allocation method matters.

### Spatial resolution and BSU

The pilot should test whether available data supports BSU-level analysis:
- For Australia: Can ABS Census SA2 areas serve as proxies for BSUs? Can reef monitoring sites be mapped to SA2s?
- For Fiji: Can qoliqoli boundaries serve as BSUs for social accounts? Can provincial-level HIES data be mapped to coastal ecosystem types?

The spatial question is whether household data and ecosystem data can be joined at a meaningful geographic unit. If the finest household data is provincial but the ecosystem data is reef-level, the analysis loses the spatial precision needed to say "households near this reef receive these services."

---

## Proposed sequence of work

1. **Data audit (both countries):** Verify access to each data source listed above. Download or request what is available. Identify gaps that block specific tables.

2. **Australia pilot -- fish provisioning worked example:** Start with the most data-rich service in the most data-rich country. Populate the distributional supply-use table (File 05 format) for fish provisioning by income quintile using ABARES catch data and ABS household expenditure data.

3. **Fiji pilot -- subsistence fisheries and food security:** Build the non-market pathway example using Fiji HIES fish consumption data disaggregated by income and location. Test the subsistence boundary resolution from File 07.

4. **Fiji pilot -- coastal protection and vulnerability:** Overlay reef/mangrove extent data with census population data to estimate which communities are protected. Test the spatial BSU question.

5. **Cross-service integration:** For one accounting area in each country, attempt to populate all five services simultaneously. Test whether the accounting identities hold when multiple services flow to the same households.

6. **Double counting and consistency checks:** Run the tests outlined above. Document what works and what breaks.

---

## Open questions

1. **Which country first?** Australia is more data-rich but Fiji better tests the non-market pathways that make social accounts distinctive. Starting with Fiji may be more valuable conceptually even if the data is harder to obtain.

2. **Synthetic vs. real data:** If microdata access requires formal requests, should the pilot use synthetic data calibrated to published aggregates? This enables table design testing while data requests are processed.

3. **Scope of "worked example":** Should each example be a fully populated table or a narrative walkthrough showing how the table would be populated with available data? The latter is faster and more useful for methodology development; the former proves feasibility.

4. **Time period:** What accounting period should the pilots use? The most recent HIES (Fiji 2019-20) and census data (Fiji 2017, Australia 2021) may not align with the most recent ecosystem monitoring data.
