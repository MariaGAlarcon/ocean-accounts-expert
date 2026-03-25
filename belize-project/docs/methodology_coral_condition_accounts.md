# Coral Reef Condition Accounts for Belize: Methodology

## 1. Purpose and Scope

This document describes the methodology for producing SEEA EA coral reef condition accounts for Belize. It covers every step from field data through indicator calculation to the final condition account tables, written so that any analyst can replicate the process, review each decision, and verify the results.

The pilot account covers Ambergris Caye within the Northern Barrier Complex. The same methodology produces accounts for all marine protected areas and subregions where matched survey data exists for both the opening and closing years.

The intended audience includes statisticians at the Belize Statistical Institute, reef ecologists reviewing indicator choices, and international partners working on ocean accounts under the Global Ocean Accounts Partnership (GOAP).

## 2. Framework

### 2.1 SEEA EA Condition Accounting

The System of Environmental-Economic Accounting, Ecosystem Accounting (SEEA EA) provides a standardized structure for measuring ecosystem condition over time (United Nations et al. 2021). A condition account records the state of an ecosystem at an opening year and a closing year using measurable indicators. Each indicator value is normalized to a condition index between 0 and 1 by comparing the measured value against a reference level that represents a healthy or pre-degradation state. A condition index of 1.0 means the ecosystem meets or exceeds the reference condition; 0 means total degradation relative to that benchmark.

The condition account table reports, for each indicator: the raw measured value at both time points, the corresponding condition index, the standard error, and the change between periods. This structure makes condition comparable across ecosystems, indicators, and countries.

### 2.2 Ecosystem Type

The ecosystem type is photic coral reefs, classified as M1.3 under the IUCN Global Ecosystem Typology (Keith et al. 2020). In Belize, this encompasses the barrier reef system (the second largest in the world), three offshore atolls (Glover's Reef, Turneffe, and Lighthouse Reef), and patch reefs within the coastal lagoon. The barrier reef runs about 300 km along the coast and supports reef crest, fore-reef, back reef, and lagoon patch reef habitats.

### 2.3 Reporting Hierarchy

The accounts use a nested geographic hierarchy:

| Level | Unit | Example |
|---|---|---|
| 1 | National | Belize |
| 2 | Subregion | Northern Barrier Complex, Central Barrier Complex, Southern Barrier Complex, Glover's Reef Atoll, Turneffe Atoll, Lighthouse Reef |
| 3 | Marine Protected Area | Hol Chan Marine Reserve, Caye Caulker Marine Reserve, Glover's Reef Marine Reserve, Sapodilla Cayes Marine Reserve, Laughing Bird Caye National Park |
| 4 | Site | Individual AGRRA survey locations (e.g., BZHCCD01, Mexico Rocks) |

The pilot covers Ambergris Caye, which includes the Hol Chan Marine Reserve and surrounding sites within the Northern Barrier Complex. The same methodology produces accounts at every level where data allows.

## 3. Data Source

### 3.1 Field Survey Data

Field data come from the Atlantic and Gulf Rapid Reef Assessment (AGRRA) program, a standardized protocol for coral reef monitoring across the Caribbean (AGRRA 2024). AGRRA surveys record benthic cover using point-intercept transects, coral colony health through individual colony measurements, fish communities through visual census, and invertebrate populations through transect counts.

The Belize Fisheries Department provided four data files exported from the AGRRA platform, containing survey metadata, benthic cover observations, coral community records, and fish transect data. The dataset covers 169 survey sites with 105,800 benthic point-intercept observations, 5,021 individual coral colony measurements, 18,933 fish count records, and 753 coral recruit observations.

### 3.2 Accounting Period

Two survey campaigns define the accounting period:

| Period | Year | Collector | Surveys |
|---|---|---|---|
| Opening | 2023 | Healthy Reefs Initiative | 110 |
| Closing | 2025 | Belize Fisheries Department | 59 |

The accounting period spans 2 years. Both campaigns followed the standardized AGRRA protocol, which reduces inter-observer variability, though some variation between survey teams is expected.

### 3.3 Geographic Coverage

The two campaigns cover 169 sites across 6 subregions of the Belize Barrier Reef system. Not all subregions were surveyed in both years, which limits where full opening/closing accounts can be produced.

| Subregion | Sites in 2023 | Sites in 2025 | Sites with both years |
|---|---|---|---|
| Northern Barrier Complex | 13 | 11 | 11 |
| Central Barrier Complex | 28 | 8 | 8 |
| Southern Barrier Complex | 18 | 28 | 15 |
| Glover's Reef Atoll | 9 | 9 | 9 |
| Turneffe Atoll | 17 | 0 | 0 |
| Lighthouse Reef | 24 | 0 | 0 |

Only sites surveyed in both years contribute to the opening/closing change assessment. Sites with data in only one year contribute single-year condition snapshots.

### 3.4 Site-to-Marine Protected Area Assignment

The AGRRA metadata does not include an MPA field. Sites were assigned to their corresponding marine protected areas using three criteria: site code prefixes (e.g., BZHCCD for Hol Chan, BZPHMR for Port Honduras), explicit site names (e.g., "North of Hol Chan Marine Reserve"), and geographic coordinates compared against known MPA boundaries. This assignment should be verified with the Belize Fisheries Department.

| MPA | Sites with both years |
|---|---|
| Hol Chan Marine Reserve | 4 |
| Caye Caulker Marine Reserve | 3 |
| Glover's Reef Marine Reserve | 9 |
| Sapodilla Cayes Marine Reserve | 7 |
| Laughing Bird Caye National Park | 2 |
| South Water Caye Marine Reserve | 0 (2023 only) |
| Turneffe Atoll Marine Reserve | 0 (2023 only) |
| Lighthouse Reef / Half Moon Caye | 0 (2023 only) |

The Ambergris Caye pilot area includes the 4 Hol Chan MR sites plus 3 adjacent sites (Mexico Rocks, Tres Cocos, BZ1081), giving 7 sites with data in both years.

## 4. Methods

The methodology follows the SEEA EA condition account workflow as described in the GOAP condition measurement framework: data quality assurance, indicator calculation, normalization to condition indices, spatial aggregation, and change analysis. The indicator calculation step uses R scripts developed under the GOAP Belize coral condition account project (available at https://github.com/uberi-projects/GOAP-condition-account-belize).

### 4.1 Quality Assurance

Before calculating indicators, all field data pass through a quality assurance procedure that checks for completeness and consistency.

**Coordinate validation.** Survey site coordinates are checked against the Belize reef system boundary. Latitude values must fall within 15.9 to 18.5 degrees north; longitude values within -88.99 to -87.00 degrees west. Sites outside these bounds are flagged for review.

**Taxonomic standardization.** Each benthic organism observation is recorded as a numeric code in the AGRRA platform. These codes are resolved to scientific names and assigned to a functional category (e.g., "Calcifiers :: Coral", "Algae :: Macro :: Fleshy") using the taxonomy tables provided in the AGRRA metadata. Coral colony observations are resolved to genus level using the AGRRA CoralTaxonomy reference table, which contains 51 Caribbean coral species across 24 genera.

**Unit harmonization.** All cover values are expressed as percentages. Recruit counts are expressed per unit area. Reef relief is recorded in centimeters. Temperature is recorded in degrees Celsius, depth in meters.

**Range checks.** Numeric values are checked against expected bounds: depth 0 to 20 m, water temperature 25 to 35 C, transect numbers 1 to 6, relief 0 to 200 cm. Values outside these ranges are flagged.

**Completeness assessment.** Each dataset is checked for required fields. Missing or null values are counted per field and reported. The quality assurance step produces a validation report listing all checks with pass/fail status and counts of flagged records.

### 4.2 Indicator Selection

Six biotic condition indicators were selected based on their ecological relevance to coral reef function, their availability in the AGRRA dataset, and their alignment with the SEEA EA coral reef condition framework. The table below summarizes each indicator, what it measures, and how higher values should be interpreted.

| Indicator | What it measures | Ecological role | Direction |
|---|---|---|---|
| Live coral cover (%) | Proportion of reef substrate occupied by living hard coral | Primary reef-building organisms; structural foundation of the ecosystem | Higher is better |
| Fleshy macroalgae cover (%) | Proportion of reef substrate occupied by fleshy macroalgae | Competitive threat to coral; indicator of nutrient loading and reduced herbivory | Higher is worse |
| Coral recruit density | Number of juvenile corals per unit area | Reef recovery capacity; indicates whether new corals are settling and surviving | Higher is better |
| Coral diversity (Shannon H') | Diversity of coral species assemblage | Community resilience; more diverse assemblages are more resistant to disturbance | Higher is better |
| Reef relief (cm) | Maximum vertical height of reef structures | Structural complexity; provides habitat for fish and invertebrates | Higher is better |
| Coral bleaching prevalence (%) | Proportion of coral colonies showing bleaching or paling | Thermal stress response; early warning of mass mortality events | Higher is worse |

The AGRRA dataset contains additional variables that could support a broader set of condition indicators in future accounting periods. Fish biomass and abundance, recorded through visual census transects, are standard SEEA EA coral reef condition indicators and serve as direct inputs to fisheries provisioning service accounts. Dead coral cover, available in the benthic point-intercept data, tracks recent mortality and would complement the live coral cover indicator. Crustose coralline algae (CCA) cover, also recorded in the benthic surveys, indicates reef consolidation capacity and substrate availability for coral settlement. Coral disease prevalence, recorded at the colony level alongside bleaching data, tracks chronic stressors distinct from thermal bleaching. These indicators were not included in the current accounting period because the priority was to establish the core six indicators with complete spatial coverage. Adding fish biomass would require size-to-biomass conversion using published length-weight relationships (e.g., Bohnsack and Harper 1988), which introduces additional uncertainty. Fish biomass and bleaching prevalence should be prioritized for the next period because they connect directly to ecosystem service accounts: fish biomass feeds fisheries and recreation service valuations, and bleaching prevalence responds to climate pressures that affect all reef services.

### 4.3 Indicator Calculation

Each indicator is calculated from the AGRRA field data following a sequence of steps: raw observations are linked to site metadata and taxonomy, aggregated to the transect level, then averaged to the site level.

#### 4.3.1 Live Coral Cover

Live coral cover is calculated from the benthic point-intercept survey data.

**Step 1: Classify each observation.** Each point along a benthic transect records a primary organism and an optional secondary organism. Each organism code is matched to the AGRRA taxonomy to determine its functional category. Organisms in the "Calcifiers :: Coral" category that are not in a "Newly Dead" state count as live coral.

**Step 2: Assign coral presence weights.** At each point, coral presence is scored using a co-dominance weighting system that accounts for points where two organisms share the substrate:

| Primary organism | Secondary organism | Coral presence score |
|---|---|---|
| Live coral | Absent or live coral | 1.0 |
| Live coral | Not coral | 0.5 |
| Not coral | Live coral | 0.5 |
| Not coral | Not coral or absent | 0.0 |

**Step 3: Calculate transect-level cover.** For each transect, live coral cover (%) = 100 x (sum of coral presence scores) / (total number of points on the transect). Each transect typically has 100 points.

**Step 4: Calculate site-level cover.** For each site, coral cover is the arithmetic mean of the transect-level values. Sites typically have 6 benthic transects.

#### 4.3.2 Fleshy Macroalgae Cover

Fleshy macroalgae cover follows the same method as live coral cover, but the functional category used is "Algae :: Macro :: Fleshy" instead of "Calcifiers :: Coral". This category includes genera such as Dictyota, Lobophora, Sargassum, Caulerpa, and other fleshy macroalgae recorded in the AGRRA taxonomy. The same co-dominance weighting and aggregation steps apply.

#### 4.3.3 Coral Recruit Density

Coral recruit density is calculated from the quadrat recruit survey data.

**Step 1: Record recruit counts.** Along each benthic transect, quadrats are surveyed for coral recruits. Each recruit is identified to coral genus and classified by size: small recruits (2 cm or less in diameter) and large recruits (2 to 4 cm). Quadrats where no recruits were observed are recorded as zero.

**Step 2: Fill absent quadrats.** If a quadrat was not surveyed (missing from the data), it is filled with a count of zero to avoid inflating density estimates by excluding empty quadrats.

**Step 3: Calculate site-level density.** Total recruit counts across all quadrats and transects at a site are summed and divided by the total surveyed area to produce a density value (recruits per unit area).

#### 4.3.4 Coral Diversity

Coral species diversity is calculated from the coral community survey data, where individual colonies are identified to species.

**Step 1: Count colonies per species.** Within each transect, the number of colonies of each coral species is tallied. Records with missing or blank species identifiers are excluded.

**Step 2: Calculate Shannon diversity index.** For each transect, the relative abundance of each species is calculated as p_i = (count of species i) / (total colonies in the transect). The Shannon diversity index is then H' = -sum(p_i x ln(p_i)) across all species. Species richness (the count of distinct species) is also recorded.

**Step 3: Calculate site-level diversity.** Shannon H' and species richness are averaged across all transects at a site to produce site-level values.

#### 4.3.5 Reef Relief

Reef relief is calculated from the fish transect survey data.

**Step 1: Record maximum relief.** Each fish transect records the maximum vertical height (in cm) of reef structures along the transect. This measures the tallest reef feature, not average roughness.

**Step 2: Calculate site-level relief.** Maximum relief values are averaged across all transects at a site to produce a site-level mean relief value.

#### 4.3.6 Coral Bleaching Prevalence

Bleaching prevalence is calculated from the coral community belt transect data, where individual colonies are assessed for bleaching status.

**Step 1: Classify each colony.** Each coral colony record includes the percentage of the colony that is bleached and the percentage that is pale. A colony is classified as "showing bleaching signs" if either value is greater than zero.

**Step 2: Calculate site-level prevalence.** For each site, bleaching prevalence (%) = 100 x (number of colonies with bleaching signs) / (total number of colonies assessed). This is calculated across all transects at the site.

### 4.4 Reference Levels

#### 4.4.1 Approach

SEEA EA condition accounts normalize each measured indicator value to a condition index between 0 and 1 using a reference level. The reference level should represent a documented pre-degradation state or a scientifically established benchmark for ecosystem health. Three types of reference levels exist within the SEEA EA framework: Type 1 (global literature defaults), Type 2 (regional published benchmarks), and Type 3 (locally calibrated baselines from long-term monitoring). The reference levels used here are Type 2, drawing from peer-reviewed Caribbean reef science.

#### 4.4.2 Reference Level Selection

| Indicator | Reference level | Source | Type |
|---|---|---|---|
| Live coral cover | 50% | Caribbean pre-1980s baseline from meta-analysis of 263 sites (Gardner et al. 2003) and expert elicitation (Roff et al. 2018) | Peer-reviewed |
| Fleshy macroalgae cover | 50% | Algal dominance threshold; reefs exceeding 50% macroalgae cover are considered phase-shifted (Bruno et al. 2009) | Peer-reviewed |
| Coral recruit density | 15 recruits/m2 | Healthy Caribbean reef observations from Curacao long-term monitoring (Bak and Engel 1979, cited in subsequent studies) | Peer-reviewed (single location) |
| Coral diversity (H') | 2.0 | Upper range of Caribbean coral Shannon index at healthy sites; Caribbean assemblages are naturally less diverse than Indo-Pacific (about 65 species vs. 600) | Regional studies |
| Reef relief | 150 cm | Based on AGRRA maximum relief measurements; represents high structural complexity within the measurement range observed in Belize (11 to 175 cm) | Empirical (this dataset) |
| Coral bleaching prevalence | 100% | Theoretical maximum; a reef with 0% bleaching scores CI = 1.0 and a reef with 100% bleaching scores CI = 0.0 | Theoretical |

The reef relief reference level (150 cm) is derived from the empirical distribution of this dataset rather than from peer-reviewed literature. Caribbean reef rugosity has been documented using a chain-tape method (Alvarez-Filip et al. 2009), but these measurements use a different unit (rugosity index) than the AGRRA maximum relief in centimeters, and no reliable conversion exists. The 150 cm reference is provisional and carries more uncertainty than the literature-based references for coral cover, macroalgae, and recruit density. Within the SEEA EA reference level typology, it is closer to a Type 1 (ad-hoc) reference than the Type 2 (regional benchmark) references used for the other indicators.

All condition indices are capped at 1.0. Values exceeding the reference level are not scaled beyond 1.

#### 4.4.3 Normalization

For indicators where higher values indicate better condition (coral cover, recruit density, diversity, relief):

> Condition Index = min(Measured Value / Reference Level, 1.0)

For indicators where higher values indicate degradation (fleshy macroalgae cover, coral bleaching prevalence):

> Condition Index = max(1 - (Measured Value / Reference Level), 0.0)

Measurement uncertainty is propagated to the condition index using the formula SE_CI = SE_measured / Reference Level. The 95% confidence interval on each condition index is CI +/- 1.96 x SE_CI, capped at the range 0 to 1.

#### 4.4.4 Discussion of Reference Level Choices

**Live coral cover.** Gardner et al. (2003) conducted a meta-analysis of 263 Caribbean reef sites spanning 1977 to 2001 and documented a decline from about 50% coral cover in the late 1970s to about 10% by 2001. Roff et al. (2018) corroborated these estimates using expert elicitation, with Caribbean experts estimating pre-degradation baselines of 53% to 59%. Cramer et al. (2021) combined paleoecological, historical, and modern data to estimate pre-decline Caribbean coral cover at about 53%. The GCRMN Status of Coral Reefs of the World report (Souter et al. 2021) estimated about 35% for the earliest Caribbean monitoring period (1970 to 1983), though this was already post-decline for many sites.

Perry et al. (2013) identified 10% coral cover as the critical threshold below which Caribbean reefs shift from net carbonate accretion to net erosion. The Healthy Reefs Initiative considers 20% the minimum for a "healthy" Mesoamerican reef (McField and Kramer 2007), but this is a management target rather than a historical baseline.

The 50% reference used here reflects the best available estimate of Caribbean coral cover before the mass mortality events of the 1980s.

**Fleshy macroalgae.** Hughes (1994) documented the shift of Jamaican reefs from about 50% coral to over 90% macroalgae between 1977 and 1993. Bruno et al. (2009) found that only about 4% of Caribbean reef sites exceeded 50% macroalgae cover, and that macroalgae cover above 20% was negatively correlated with coral cover. The Healthy Reefs Initiative scores macroalgae cover as: Very Good (1% or less), Good (5% or less), Fair (12% or less), Poor (25% or less), Critical (above 25%). The 50% reference represents the threshold for near-total algal dominance; reefs near this level have shifted to an alternative stable state.

**Coral recruit density.** Long-term monitoring in Curacao recorded about 15.3 recruits/m2 in 1975, declining to about 6.9/m2 by 2005 (Bak and Engel, cited in subsequent Caribbean recruitment studies). This is the strongest historical Caribbean benchmark found, though it comes from a single location. Published Caribbean recruit density values range from about 5 to 22/m2 across sites and methods. This reference level carries more uncertainty than the coral cover or macroalgae references.

**Coral diversity.** No strong Caribbean-specific Shannon index benchmark was found in the published literature. Caribbean coral communities naturally support fewer species than Indo-Pacific reefs. Reported Shannon index values for Caribbean coral assemblages range from about 0.9 (degraded) to about 2.0 (healthy). The 2.0 reference represents a moderately diverse Caribbean assemblage.

**Reef relief.** Alvarez-Filip et al. (2009) documented that Caribbean reef rugosity (measured by chain-tape method) declined from about 2.5 in 1969 to about 1.2 by the mid-2000s. The AGRRA data records maximum reef relief height in centimeters rather than the chain-tape rugosity index, so these units are not directly comparable. The 150 cm reference is based on the empirical distribution of maximum relief values in the Belize AGRRA dataset, where the 90th percentile is about 119 cm and the maximum is 175 cm.

**Coral bleaching prevalence.** Bleaching prevalence is normalized against a theoretical maximum of 100%. This produces a linear scale where 0% bleaching scores CI = 1.0 and 100% bleaching scores CI = 0.0. Alternative approaches exist: the SEEA EA reference methodology for the Maldives used 50% as a "severe bleaching threshold," producing a steeper decline curve. The 100% reference was chosen here because it avoids imposing an arbitrary threshold and produces condition indices that are directly interpretable as the proportion of the reef community not showing bleaching signs. If future accounting periods coincide with mass bleaching events (such as those triggered by marine heatwaves), even the 100% scale will register large declines in condition.

### 4.5 Spatial Aggregation

For each geographic unit (MPA, subregion, or national):

**Step 1.** Calculate each indicator at the site level for each year, following the methods in Section 4.3.

**Step 2.** Calculate the arithmetic mean and standard error across all sites within the geographic unit for each indicator, separately for the opening and closing years.

**Step 3.** Normalize the mean to a condition index using the formulas in Section 4.4.3.

**Step 4.** Propagate uncertainty from the measured values to the condition index.

Only sites with data in both the opening and closing years contribute to the change assessment. Sites with data in only one year contribute to single-year condition snapshots for that geographic unit.

The aggregation uses simple arithmetic means (equal weight per site). The SEEA EA framework recommends area-weighted means when survey sites are purposively selected rather than randomly sampled. The AGRRA sites are not randomly distributed; they are concentrated in accessible reef areas and marine protected areas. Area-weighted aggregation was not applied because individual site catchment areas are not defined in the AGRRA metadata and because the survey protocol targets similar reef habitats (fore-reef at 5 to 15 m depth) across sites, limiting the extent of habitat-type bias. If future accounts incorporate site-level reef area estimates from satellite-derived extent maps, area-weighted aggregation should be used.

### 4.6 Change Analysis

For each indicator at each geographic level:

**Absolute change** in condition index = Closing CI - Opening CI.

**Percent change** = ((Closing CI - Opening CI) / Opening CI) x 100.

**Interpretation** is based on the magnitude of change relative to uncertainty. If the absolute change falls within one standard error of zero (using the mean of opening and closing SE), the change is classified as "Stable". Otherwise, positive change is classified as "Improving" and negative change as "Declining".

The 1-SE threshold is a pragmatic choice for a Tier 1 to 2 account. The SEEA EA reference methodology describes a more conservative approach based on 95% confidence interval overlap: if the 95% CIs of the opening and closing condition indices do not overlap, the change is classified as significant. The 1-SE threshold is more permissive (more likely to classify change as real) than the 95% CI overlap test. Some changes currently classified as Declining or Improving might not reach significance under the stricter test. Future accounting periods with larger sample sizes and longer time series could adopt formal hypothesis testing (paired t-test or Wilcoxon signed-rank test) for matched-site comparisons.

### 4.7 Computational Implementation

The indicator calculations were implemented in R using scripts developed under the GOAP Belize coral condition account project (https://github.com/uberi-projects/GOAP-condition-account-belize). These scripts read the AGRRA data files, join survey metadata with observation records, apply the taxonomy classification, and compute each indicator following the steps described in Section 4.3. The normalization, aggregation, and change analysis steps were implemented as an additional processing layer that takes the site-level indicator values and produces the final SEEA EA condition account tables for each geographic unit.

## 5. Condition Account Output

### 5.1 Table Format

The final SEEA EA condition account table has this structure, with one row per indicator per geographic unit:

| Ecosystem type | Indicator | Unit | Reference level | Opening year | Opening value (mean +/- SE) | Opening CI | Closing year | Closing value (mean +/- SE) | Closing CI | Change in CI | Interpretation | N sites | Data quality |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Coral reef (M1.3) | Live coral cover | % | 50% | 2023 | X +/- SE | CI | 2025 | Y +/- SE | CI | delta | status | n/n | rating |

Data quality is rated as "Good" (5 or more matched sites), "Moderate" (3 to 4 sites), or "Limited" (2 or fewer sites).

### 5.2 Accounts Produced

Full opening/closing accounts (2023 to 2025) were produced for nine geographic units with matched site data in both years:

| Geographic unit | Type | Matched sites |
|---|---|---|
| Ambergris Caye (pilot) | Subregion subset | 7 |
| Hol Chan Marine Reserve | MPA | 4 |
| Caye Caulker Marine Reserve | MPA | 3 |
| Glover's Reef Marine Reserve | MPA | 9 |
| Sapodilla Cayes Marine Reserve | MPA | 7 |
| Laughing Bird Caye National Park | MPA | 2 |
| Northern Barrier Complex | Subregion | 11 |
| Central Barrier Complex | Subregion | 8 |
| Southern Barrier Complex | Subregion | 15 |

Opening-year snapshots (2023 only) were produced for Turneffe Atoll Marine Reserve (17 sites), Lighthouse Reef (24 sites), and South Water Caye Marine Reserve (12+ sites). A national aggregate account was produced by combining all subregions with matched data.

## 6. Data Quality Assessment

### 6.1 Tiered Assessment

Following the SEEA EA tiered assessment framework, the condition account was evaluated across three dimensions:

| Dimension | Tier | Rationale |
|---|---|---|
| Feasibility | Tier 2 | 2 to 3 analysts; standard R computing environment; data provided by national agency |
| Accuracy | Tier 1 to 2 | Regional Caribbean benchmarks for reference levels (not locally calibrated); 169 sites but unequal coverage between years |
| Difficulty | Tier 1 to 2 | Standard statistical methods; data from two agencies; no advanced modelling required |

The binding constraint on accuracy is the reference level sub-procedure. The reference levels for coral cover and macroalgae are supported by peer-reviewed Caribbean-wide studies. The reference levels for recruit density and coral diversity rest on weaker published consensus. Advancing to Tier 3 would require locally calibrated reference levels derived from long-term Belize monitoring data (10+ years) or paleoecological records.

### 6.2 Limitations

| Issue | Impact | Mitigation |
|---|---|---|
| Different survey teams in 2023 and 2025 | Potential observer bias between opening and closing years | Both teams followed standardized AGRRA protocol |
| Not all sites resurveyed in 2025 | Turneffe and Lighthouse Reef lack closing-year data; reduces matched pairs for change detection | Report only matched sites for opening/closing accounts; present single-year snapshots for unmatched areas |
| No MPA field in AGRRA metadata | Sites assigned to MPAs by coordinate and name pattern | Document assignment logic; verify with Belize Fisheries Department |
| Coral transects absent from some subregions in 2023 | Recruit density and coral diversity not available for 2023 at most sites; limits opening/closing comparison | Report as "Closing only" where opening data is missing |
| Recruit density reference level weakly established | Published Caribbean consensus weaker than for coral cover | Flag uncertainty; interpret recruit density CI with caution |
| Reef relief measured in cm; historical reference in rugosity index | Units not directly comparable | Use empirical reference from this dataset (150 cm) rather than converting rugosity |

## 7. References

Alvarez-Filip L, Dulvy NK, Gill JA, Cote IM, Watkinson AR. 2009. Flattening of Caribbean coral reefs: region-wide declines in architectural complexity. Proceedings of the Royal Society B 276:3019-3025. DOI: 10.1098/rspb.2009.0339

AGRRA (Atlantic and Gulf Rapid Reef Assessment). 2024. Coral Reef Monitoring Protocol. https://www.agrra.org/

Bruno JF, Sweatman H, Precht WF, Selig ER, Schutte VGW. 2009. Assessing evidence of phase shifts from coral to macroalgal dominance on coral reefs. Ecology 90:1478-1484. DOI: 10.1890/08-1781.1

Cramer KL, Donovan MK, Jackson JBC et al. 2021. The transformation of Caribbean coral communities since humans. Ecology and Evolution 11:10098-10118. DOI: 10.1002/ece3.7808

Gardner TA, Cote IM, Gill JA, Grant A, Watkinson AR. 2003. Long-term region-wide declines in Caribbean corals. Science 301:958-960. DOI: 10.1126/science.1086050

GCRMN. 2025. Status and Trends of Caribbean Coral Reefs: 1970-2024. Global Coral Reef Monitoring Network / International Coral Reef Initiative. https://gcrmn.net/caribbean-2025/

Hughes TP. 1994. Catastrophes, phase shifts, and large-scale degradation of a Caribbean coral reef. Science 265:1547-1551. DOI: 10.1126/science.265.5178.1547

Jackson JBC, Donovan MK, Cramer KL, Lam V (eds). 2014. Status and Trends of Caribbean Coral Reefs: 1970-2012. Global Coral Reef Monitoring Network, IUCN, Gland, Switzerland.

Keith DA, Ferrer-Paris JR, Nicholson E, Kingsford RT (eds). 2020. IUCN Global Ecosystem Typology 2.0: Descriptive profiles for biomes and ecosystem functional groups. IUCN, Gland, Switzerland.

McField M, Kramer P. 2007. Healthy Reefs for Healthy People: A Guide to Indicators of Reef Health and Social Well-being in the Mesoamerican Reef Region. Smithsonian Institution.

Mumby PJ, Hastings A, Edwards HJ. 2007. Thresholds and the resilience of Caribbean coral reefs. Nature 450:98-101. DOI: 10.1038/nature06252

Perry CT, Murphy GN, Kench PS, Smithers SG, Edinger EN, Steneck RS, Mumby PJ. 2013. Caribbean-wide decline in carbonate production threatens coral reef growth. Nature Communications 4:1402. DOI: 10.1038/ncomms2409

Roff G, Bejarano S, Bozec YM, Nugues M, Steneck RS, Mumby PJ. 2018. Historical baselines of coral cover on tropical reefs as estimated by expert opinion. PeerJ 6:e4308. DOI: 10.7717/peerj.4308

Souter D, Planes S, Wicquart J, Logan M, Obura D, Staub F (eds). 2021. Status of Coral Reefs of the World: 2020. Global Coral Reef Monitoring Network / International Coral Reef Initiative. https://gcrmn.net/2020-report/

United Nations et al. 2021. System of Environmental-Economic Accounting: Ecosystem Accounting (SEEA EA). White cover publication. United Nations, New York.
