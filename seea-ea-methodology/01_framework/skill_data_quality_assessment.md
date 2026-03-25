# Standard Operating Procedures: Identifying Data Quality and Relevance for Accounting Activities

**Framework:** UN SEEA EA (2021) — System of Environmental-Economic Accounting: Ecosystem Accounting
**Applicable To:** Any environmental-economic accounting project requiring systematic data assessment
**Standards Referenced:** ABS Data Quality Framework; UN SEEA Central Framework (2014); UN SEEA EA (2021); UNESCAP Data Inventory; Technical Guidance on Ocean Accounting (GOAP, 2019)

---

## 1. Overview

Before environmental-economic accounts can be compiled, the underlying data must be systematically assessed for quality and relevance. This SOP provides a standardised process for evaluating whether existing datasets are suitable for inclusion in accounting activities. It covers the full data assessment workflow: organising data against an accounting framework, scoring quality across multiple dimensions, evaluating spatial and temporal fitness, determining transformation effort to reach account-ready status, and identifying gaps that require modelling or primary data collection.

The procedures in this SOP are domain-agnostic — they apply equally to marine, coastal, freshwater, and terrestrial ecosystem accounting projects. Where examples are needed, this SOP draws on the Geographe Marine Park ocean accounting pilot (IDEEA Group, 2020) as an illustrative case study.

### 1.1 When to Use This SOP

Use this SOP at the data collection and data transformation phases of the accounting process:

| Accounting Phase | Role of This SOP |
|---|---|
| Data collection | Organise, discover, and inventory datasets against the accounting framework |
| Data transformation | Assess suitability, determine transformation effort, and identify modelling requirements |
| Account compilation | Inform decisions on which datasets to include and what caveats to attach |
| Decision making | Provide quality metadata so decision makers understand the reliability of accounts |

### 1.2 Scope

This SOP applies to any environmental-economic accounting project that draws on heterogeneous datasets (remote sensing, field surveys, administrative records, research outputs, socioeconomic statistics) to compile extent, condition, asset, service, or use accounts. It is relevant to:

- Marine and coastal ecosystem accounts (ocean accounting)
- Terrestrial ecosystem accounts (forests, grasslands, wetlands, urban ecosystems)
- Freshwater ecosystem accounts (rivers, lakes, groundwater-dependent ecosystems)
- Integrated landscape accounts spanning multiple ecosystem types

---

### 1.3 Tiered Assessment Profile

This SOP is assessed against the [Tiered Assessment Framework](tiered_assessment_framework.md), which evaluates procedures across three independent dimensions: **A — Feasibility and Resource Intensiveness**, **B — Accuracy and Confidence**, and **C — Difficulty of Implementation**. Because this SOP covers the data assessment workflow (rather than ecosystem measurement directly), its tier profile reflects the resource and difficulty requirements of the assessment process itself, not the tier of the datasets being assessed.

**Sub-procedure tier matrix:**

| Sub-procedure | A: Feasibility | B: Accuracy | C: Difficulty | Notes |
|---|---|---|---|---|
| Data inventory and organisation (SOP 1) | 1 | 1 | 1 | Desk-based; spreadsheet or database |
| Quality scoring — desktop review (SOP 2) | 1 | 2 | 1 | Expert judgment applied to existing metadata |
| Spatial assessment of candidate datasets (SOP 3) | 1–2 | 2 | 1–2 | GIS overlay and coverage analysis |
| Temporal alignment assessment (SOP 3) | 1 | 1–2 | 1 | Metadata review; calendar comparison |
| Accounting compliance assessment (SOP 3) | 1 | 2 | 1–2 | SEEA EA standards alignment; crosswalk development |
| Account-readiness synthesis (SOP 4) | 1 | 2 | 1 | Compilation; follows from earlier assessments |
| Gap analysis and recommendations (SOP 5) | 1 | 2 | 1–2 | Requires domain knowledge across ecosystem and accounting fields |
| Documentation and quality flags (SOP 6) | 1 | 1 | 1 | Metadata and flag assignment |

This SOP is consistently **A: Tier 1** (feasibility): the assessment workflow is desk-based and requires standard GIS and spreadsheet tools. Difficulty (C) may rise to Tier 2–3 where institutional coordination is required to access restricted or privately held datasets.

**Crosswalk — quality scoring dimensions to tiered framework dimensions:**

The six quality dimensions in SOP 2 (scored 0–10) map to the Tiered Assessment Framework dimensions as follows. These crosswalks inform how scored datasets feed into tier assessments in the downstream extent, condition, and service SOPs.

| SOP 2 Quality Dimension | Maps to Tiered Framework Dimension | Interpretation |
|---|---|---|
| Dimension 5: Accuracy | B — Accuracy and Confidence | Low score (0–4) → Tier 1 B; moderate (4–7) → Tier 2 B; high (7–10) → Tier 3 B |
| Dimension 3: Relevance (spatial and temporal) | B — Spatial and temporal representativeness | Coarse resolution or outdated data → lower B tier |
| Dimension 6: Accessibility | C — Data availability | Restricted or pay-access data → higher C difficulty tier |
| Dimension 1: Interpretability | B — Method validation and protocol maturity | Poor documentation → Tier 1 B |
| Dimension 2: Institutional Environment | C — Institutional and legal barriers | Ad hoc, non-mandated collection → higher C difficulty tier |
| Transformation effort (SOPs 3–4) | A — Feasibility | High transformation effort → higher A resource tier for the downstream SOP using that dataset |

**Quality flag to accuracy tier crosswalk:**

| Quality Flag (SOP 6) | Tiered Framework Dimension B |
|---|---|
| A — High confidence | Tier 2–3 (data directly measured; high quality score; full spatial and temporal coverage) |
| B — Moderate confidence | Tier 2 (transformed, modelled, or from adjacent area) |
| C — Low confidence | Tier 1 (proxy measure, sparse coverage, or outdated source) |
| D — Data-deficient | Tier 1 (modelled with high uncertainty; major gaps remain) |
| X — Not compiled | Cannot be assessed; treat as a data availability gap (Tier 3 C difficulty) in downstream SOPs |

---

## 2. SOP 1 — Organising Data Against the Accounting Framework

### 2.1 Objective

Classify all candidate datasets into a structured data collection framework so that coverage and gaps can be systematically assessed across accounting components.

### 2.2 Data Collection Framework

Adopt the SEEA EA accounting structure, supplemented by the UNESCAP data inventory structure for marine/coastal projects. The framework comprises five core components, each with subcomponents. Adapt subcomponent labels to match the ecosystem domain (marine, terrestrial, freshwater, or integrated).

| Component | Subcomponent | Definition | Marine Examples | Terrestrial Examples |
|---|---|---|---|---|
| Ecosystem Extent | Physical extent | Physical area, depth, elevation, arrangement | Bathymetry, topography, coastline | Elevation models, slope, land surface |
| | Institutional extent | Regulatory and planning boundaries | Maritime zones, IUCN marine categories | Protected area boundaries, land tenure, zoning |
| | Ecosystem type extent | Extent and composition of ecosystem types | Seagrass, reef, mangrove, saltmarsh | Forest, grassland, wetland, cropland |
| | Context | Broader socio-ecological setting | River connections, coastal settlements | Upstream catchments, urban centres, transport |
| Use | Designated use | Areas designated for specific use | Ports, fisheries management, aquaculture | Agricultural zones, forestry concessions, mining |
| | Observed use | Recorded patterns of human activity | Shipping lanes, fishing effort | Land use intensity, grazing pressure, recreation |
| Ecosystem Condition | Physical characteristics | Physical attributes of the system | Temperature, salinity, turbidity, wave energy | Soil depth, canopy height, hydrology |
| | Chemical characteristics | Chemical and nutrient properties | Phosphate, nitrate, pH, dissolved oxygen | Soil nutrient content, water chemistry |
| | Biological characteristics | Biological attributes | Chlorophyll, plankton, algal bloom | Vegetation indices (NDVI), pest/disease |
| | Ecological characteristics | Ecological properties | Species cover, density, diversity | Species richness, structural complexity |
| Ecosystem Assets | Biotic assets | Living natural assets (stocks) | Fish stock, aquatic plants, marine mammals | Timber volume, wildlife populations, soil biota |
| | Abiotic assets | Non-living natural assets | Minerals, petroleum, seafloor substrates | Soil carbon, mineral deposits, water reserves |
| Ecosystem Services (supply and use) | Physical services | Services measured in biophysical units | Fish catch, carbon sequestration, nursery | Crop yield, timber harvest, water filtration |
| | Monetary services | Services valued in monetary terms | Market prices, resource rent, SCC | Market prices, replacement cost, travel cost |

### 2.3 Step-by-Step

**Step 1: Define the accounting area**
- Establish the spatial boundary for the accounts (e.g., marine park, river basin, national park, municipality)
- Identify adjacent areas that may supply relevant contextual data
- Justify any broader scoping — data from adjacent areas may fill gaps or provide context

> **Geographe Bay example:** The accounting area was Geographe Marine Park (977 km^2 of Commonwealth waters), but the data assessment was scoped to the broader Geographe Bay to ensure full consideration of key assets, services, and pressures, and to enable data from State waters and coastal areas to fill gaps in the marine park.

**Step 2: Build the data inventory**
- Assign a unique code to each dataset using a consistent scheme (e.g., component prefix + sequential number)
- Record for each entry: source, data type (polygonal, point, raster, tabular), spatial coverage, temporal coverage, access status (public/private), and a short description
- Structure entries according to the data collection framework components

> **Geographe Bay example:** Datasets were coded by component — OE_ for Ocean Extent, OC_ for Ocean Condition, OA_ for Ocean Asset, OS_ for Ocean Services, DU_ for Designated Use, and MUL_ for multi-component datasets. Over 100 entries were catalogued across global, national, state, and local sources.

**Step 3: Classify each dataset**
- Assign each dataset to one or more framework subcomponents
- Flag datasets that span multiple components — this is common, as ecological surveys often cover extent, condition, and asset information simultaneously

> **Geographe Bay example:** A BRUV (Baited Remote Underwater Video) survey dataset (MUL_036) spanned Ecosystem Extent (benthic habitat presence/absence), Ecological Condition (fish assemblage diversity), and Biotic Assets (fish species data).

**Step 4: Conduct gap analysis by component**
- For each subcomponent, summarise: number of datasets, spatial coverage, temporal range, and overall adequacy
- Identify components with no data, sparse data, or data limited to areas outside the accounting boundary

---

## 3. SOP 2 — Scoring Data Quality

### 3.1 Objective

Apply a standardised, multi-dimensional quality score to each candidate dataset so that datasets can be compared and selection decisions are transparent and auditable.

### 3.2 Data Quality Framework

Adapted from the ABS Data Quality Framework. Each dataset is scored across six dimensions. Each dimension receives a score from 0 to 10 based on expert assessment:

| Score Range | Quality Rating |
|---|---|
| 0–2 | Very low |
| 2–4 | Low |
| 4–6 | Average |
| 6–8 | High |
| 8–10 | Very high |

### 3.3 Quality Dimensions — Detailed Assessment Criteria

#### Dimension 1: Interpretability

| Sub-criterion | Assessment Question |
|---|---|
| Documentation availability | Are concepts, methods, and metadata documented? |
| User guides | Do manuals or user guides exist for the dataset? |
| Accuracy reporting | Are measures of accuracy or uncertainty reported? |

**Scoring guidance:** Score high (8–10) if comprehensive metadata, methods documentation, and accuracy measures are publicly available. Score low (0–2) if no supporting documentation exists.

#### Dimension 2: Institutional Environment

| Sub-criterion | Assessment Question |
|---|---|
| Impartiality and objectivity | Was data produced transparently by a professional agency? |
| Professional independence | Is the data producer independent from policy/regulatory bodies or private interests? |
| Mandate for data collection | Was data collected under a legal or institutional mandate? |

**Scoring guidance:** Government statistical agencies and mandated monitoring programs score highest. Ad hoc research outputs without institutional backing score lower.

> **Geographe Bay example:** Institutional extent data produced by government agencies (e.g., gazetted marine park boundaries) scored highest on this dimension, as they were produced under legislative mandate with formal quality assurance.

#### Dimension 3: Relevance (for accounting in the target area)

| Sub-criterion | Assessment Question |
|---|---|
| Geographic detail | At what spatial resolution is data available? Does it match or exceed the accounting area? |
| Scope and coverage | Does the dataset target the population/area relevant to the accounts? Who/what is excluded? |
| Reference period | Is the temporal period consistent with accounting requirements? Is data collected at regular intervals? |
| Main outputs / data items | Does the data directly measure the accounting concept, or is it a proxy? |
| Classifications and standards | Were formal classifications used (e.g., SEEA ecosystem typology, IUCN categories, LULC classes)? |
| Other cautions | Any other issues affecting use in accounts? |

**Scoring guidance:** A dataset that directly measures the accounting concept at the correct spatial resolution for the accounting area, using standard classifications, with consistent temporal coverage scores highest. A proxy measure at coarse resolution with irregular timing scores lowest.

> **Geographe Bay example:** A seagrass meadow mapping dataset (OE_001) scored 87% overall — high interpretability and accuracy, but lower on temporal coverage because it was a one-off survey (2004–2007) with no repeat sampling. A recreational fisheries dataset (OS_006) scored 72% — collected at the bioregional scale, requiring spatial disaggregation to the marine park level.

#### Dimension 4: Timeliness

| Sub-criterion | Assessment Question |
|---|---|
| Frequency of collection | Is data from a one-off study, or is collection ongoing and repeated? |
| Currency | How recent is the most current data release? |
| Update schedule | Is there a known schedule for future data releases? |

**Scoring guidance:** Ongoing monitoring programs with regular, recent releases score highest. One-off studies from >10 years ago with no planned repetition score lowest.

#### Dimension 5: Accuracy

| Sub-criterion | Assessment Question |
|---|---|
| Sample error | What is the sample size? Are sampling errors quantified? |
| Other error sources | Are there known processing errors, confidentiality adjustments, or rounding issues? |
| Revisions | Is the data subject to revision? Over what period? |

**Scoring guidance:** Large-sample systematic surveys with known and low error margins score highest. Small convenience samples with unknown error score lowest.

> **Geographe Bay example:** Commercial fisheries catch data (OS_001, OS_002) scored high on accuracy (90%, 87%) because data collection was mandated by fisheries regulation. However, confidentiality rules meant data was suppressed where fewer than three operators existed in a reporting block, creating spatial gaps.

#### Dimension 6: Accessibility

| Sub-criterion | Assessment Question |
|---|---|
| Public availability | Is data openly accessible, restricted, or private? |
| Data products | In what formats is data available (GIS, spreadsheet, report-only, raw data)? |
| Cost | Is access free or does it require payment/licensing? |
| Usability | Can data be used directly, or does it require significant preprocessing? |

**Scoring guidance:** Freely available GIS or tabular data with open licensing scores highest. Data locked in narrative reports with no raw data access scores lowest.

### 3.4 Step-by-Step Scoring Process

**Step 1: Assemble assessment team**
- Include domain experts (ecologists, economists, spatial analysts) and accounting specialists
- Ensure familiarity with both the data sources and the accounting requirements

**Step 2: Score each dataset**
- For each of the six dimensions, assign a score from 0 to 10
- Document the rationale for each score
- Note any dimensions where insufficient information is available to make a judgement

**Step 3: Calculate composite quality score**
- Compute the unweighted mean across all six dimensions to produce a single quality percentage
- Formula: `Quality Score (%) = (Sum of dimension scores / 60) x 100`
- Example: A dataset scoring Interpretability 8, Institutional 7, Relevance 6, Timeliness 5, Accuracy 9, Accessibility 7 = (42/60) x 100 = 70%

**Step 4: Record and attach scores to the data inventory**
- Each entry in the data inventory should carry its composite quality score and dimension-level breakdown
- Flag datasets where scoring is uncertain due to limited information

---

## 4. SOP 3 — Assessing Data Relevance for Specific Accounts

### 4.1 Objective

Determine whether each dataset is suitable for inclusion in a specific account, considering both the data quality score and its alignment with accounting requirements.

### 4.2 Account-Readiness Criteria

A dataset is account-ready when it satisfies three conditions:

| Criterion | Requirement | Assessment |
|---|---|---|
| Spatial coverage | Data is aligned to the accounting area boundary | Full coverage, partial coverage, or no coverage |
| Temporal coverage | Data is aligned to the accounting period, with seasonality controlled | Consistent reference period, or requires interpolation |
| Accounting compliance | Data conforms to SEEA EA definitions, classifications, and measurement units | Direct compliance, minor adjustments needed, or major transformation required |

A fourth consideration — **account coherence** — applies at the system level: accounts should be internally consistent so that stock accounts, flow accounts, and supply-and-use tables support a coherent narrative.

### 4.3 Spatial Assessment

**Step 1: Classify spatial characteristics of each dataset**

| Characteristic | Categories | Implication |
|---|---|---|
| Spatial coverage | Full / Partial / None for accounting area | Full = no transformation; Partial = interpolation likely needed; None = extrapolation needed |
| Data type | Polygonal / Raster / Point / Tabular | Polygonal/raster = low transformation; Point = interpolation/extrapolation needed |
| Spatial resolution | Finer than, equal to, or coarser than accounting area | Finer = aggregation needed; Equal = no change; Coarser = disaggregation needed |

**Step 2: Assign spatial transformation effort**

| Scenario | Transformation Required | Effort Level |
|---|---|---|
| Full coverage, polygonal/raster, matching resolution | Clip to accounting area boundary | Low |
| Partial coverage, polygonal | Merge multiple sources; model gaps | Medium–High |
| Point data with extensive coverage | Interpolation (e.g., kriging, IDW) | High–Very High |
| Point data with sparse coverage | Extrapolation using covariates | High–Very High |
| Coarser resolution than accounting area | Disaggregation using proportional estimates | Medium |
| No spatial data for accounting area | Extrapolation from adjacent areas or modelling | Very High |

> **Geographe Bay example — spatial assessment of seagrass extent data:**
> - Three polygonal datasets (OE_001, OE_003, OE_004) covered only the inshore portion of the marine park → classified as Partial coverage, requiring gap-filling
> - One point dataset (MUL_036, presence/absence from BRUV surveys) had extensive coverage across the marine park but was not account-ready because point data does not delineate ecosystem area
> - Bathymetry (OE_013/OE_014) and primary productivity (OC_016) rasters had full coverage and could serve as covariates for spatial extrapolation

### 4.4 Temporal Assessment

**Step 1: Check temporal alignment**
- Does the data period match the accounting period?
- If data spans multiple years, are seasonal effects controlled?

**Step 2: Assign temporal transformation effort**

| Scenario | Transformation Required | Effort Level |
|---|---|---|
| Data matches accounting period exactly | None | Low |
| Data from different months/seasons across years | Seasonal adjustment | Medium |
| Data exists at two time points, accounts needed for intermediate years | Linear interpolation | Medium |
| No data for accounting period; nearest data is >5 years old | Extrapolation with uncertainty flags | High |

> **Geographe Bay example — temporal issues:** Seagrass condition may differ significantly between summer and winter due to varied rainfall and runoff. Data collected in different seasons across different years required temporal normalisation before comparison. Most ecological studies in the bay were discrete, one-off investigations — only the KeepWatch Seagrass Monitoring Program and Reef Life Surveys provided repeated annual measurements.

### 4.5 Accounting Compliance Assessment

**Step 1: Check definitional alignment**
- Does the dataset use SEEA EA definitions for the measured concept?
- Are ecosystem classifications compatible with the accounting typology?
- Are measurement units consistent with accounting requirements?

**Step 2: Check standards alignment**
- Were standard classifications used (e.g., IUCN categories, ISIC industries, LULC classification)?
- Can crosswalks be constructed to align non-standard classifications?

**Step 3: Assign compliance transformation effort**

| Scenario | Transformation Required | Effort Level |
|---|---|---|
| Data uses SEEA EA definitions and standard classifications | None or minor relabelling | Low |
| Data uses non-standard but compatible classifications | Crosswalk development | Medium |
| Data measures a proxy concept | Modelling to estimate target variable | High |
| Data uses incompatible definitions | Major re-estimation or exclusion | Very High |

> **Geographe Bay example — proxy measures:** The number of commercial fishing operators in a reporting block was used as a proxy for fishing use intensity, since vessel-level spatial tracking data was not accessible. This required a compliance transformation: the proxy had to be clearly labelled, and its limitations documented.

---

## 5. SOP 4 — Determining Overall Account-Readiness and Transformation Effort

### 5.1 Objective

For each proposed account, synthesise the spatial, temporal, and compliance assessments into an overall judgement of transformation effort and feasibility.

### 5.2 Account Assessment Summary Table

For each account, compile the following summary:

| Field | Content |
|---|---|
| Account name | e.g., Seagrass meadow ecosystem extent account; Forest carbon stock account |
| Priority | Primary / Secondary |
| Candidate datasets | List with inventory codes |
| Preferred approach | Which dataset(s) and transformation pathway |
| Data type | Polygonal / Point / Raster / Grid / Tabular |
| Transformation required | Description of spatial, temporal, and compliance transformations |
| Overall effort | Low / Medium / High / Very High |
| Spatial coverage achieved | Full / Partial (with description) |
| Quality score(s) | Composite score for each candidate dataset |
| Data gaps | Description of missing data and its importance |
| Modelling options | If gaps exist, what modelling approaches could fill them? |
| Scalability | Could this approach be applied at broader scales (regional, national)? |

### 5.3 Step-by-Step

**Step 1: For each proposed account, list all candidate datasets from the inventory**

**Step 2: For each candidate, record:**
- Data type (polygonal, point, raster, grid, tabular)
- Required transformation (merge, interpolate, extrapolate, compile indicator, etc.)
- Transformation effort (Low / Medium / High / Very High)
- Resulting spatial coverage (Full / Partial / None, with description)
- Quality score

**Step 3: Identify the preferred approach**
- Select the combination of datasets and transformations that achieves the best coverage at acceptable effort and quality
- If multiple approaches exist, rank them by effort and coverage trade-off

**Step 4: Identify data gaps and modelling options**
- For each gap: describe what is missing, rate its importance (High / Medium / Low), and list potential modelling approaches
- Common modelling strategies:

| Strategy | When to Use | Typical Effort |
|---|---|---|
| Proportional estimation | Point data exists with known area | Medium |
| Covariate-based extrapolation | Relationships exist between target variable and fully-covered covariates (e.g., bathymetry, elevation, climate) | High |
| Geostatistical interpolation (kriging, IDW) | Extensive point data exists | Very High |
| Per-hectare / per-unit-area scaling | Per-unit-area estimates available from literature or adjacent sites | Low–Medium |
| Linear temporal interpolation | Two time-points available, intermediate values needed | Medium |
| Remote sensing classification | Satellite imagery available; ground-truth data exists for training | High |

**Step 5: Assess scalability**
- Could the same dataset and methods be used to produce accounts at broader scales (state, national, regional)?
- What additional data collection or coordination would be required?

> **Geographe Bay example — scalability assessment:** Seamap Australia (OE_025) provided a national composite of marine ecosystem extent but had significant gaps in Commonwealth waters. The assessment concluded that national extent accounts would require a coordinated data collection effort across states and territories, supplementing Seamap with local datasets similar to those used in the Geographe pilot.

---

## 6. SOP 5 — Gap Analysis and Recommendations

### 6.1 Objective

Systematically identify and prioritise data gaps across all accounting components, and recommend strategies for filling them.

### 6.2 Gap Analysis Framework

For each accounting component, assess the following:

| Assessment Criterion | Questions |
|---|---|
| Spatial coverage | Does data cover the full accounting area? Where are the gaps? |
| Temporal coverage | Is there a time series, or only discrete snapshots? Are surveys repeated? |
| Ecosystem bias | Is data biased toward certain ecosystems or habitat types? |
| Disciplinary bias | Is data biased toward certain disciplines (e.g., fisheries over general ecology, timber over non-timber values)? |
| Resolution | Is spatial resolution sufficient for the accounting area, or only suitable for broader regions? |
| Access | Is data publicly available, or does it require private agreements? |
| Replication | Have surveys been repeated to enable trend analysis? |
| Inclusivity | Are all knowledge systems represented (e.g., Indigenous and local knowledge, citizen science)? |

> **Geographe Bay example — bias patterns identified:**
> - **Ecosystem bias:** Data was heavily concentrated on seagrass meadow health and fisheries, with limited information on rocky reef ecology and deep-water habitats
> - **Spatial bias:** High-resolution ecosystem mapping existed only for shallow inshore waters (eastern half of the bay); deeper offshore waters and the western half had sparse or no coverage
> - **Temporal bias:** Most studies were one-off investigations; only two programs (KeepWatch, Reef Life Surveys) provided repeated annual datasets
> - **Access gaps:** Key datasets (e.g., NESP 2016 benthic survey, whale research) were privately held and required negotiation for access
> - **Inclusivity gap:** No input from Traditional Owners of Southwest Australia was included in the assessment — noted as a significant gap applicable across all components

### 6.3 Gap Prioritisation

| Priority | Criteria |
|---|---|
| Critical | Gap prevents compilation of a primary account; no modelling workaround exists |
| High | Gap significantly reduces accuracy of a primary account; modelling possible but uncertain |
| Medium | Gap affects a secondary account or reduces precision of a primary account; workarounds available |
| Low | Gap affects supplementary information or context; accounts can proceed without it |

> **Geographe Bay example — critical gaps:**
> - Ecosystem extent in deeper offshore waters of the marine park: Critical — extent accounts are foundational to all other accounts, and no polygonal data existed for these areas
> - Climate change model specific to Geographe Bay: High — no local model existed, though national-scale inferences could partially fill the gap
> - Recreational fishing visitation: High — no reliable spatial data existed for the marine park, and modelling approaches were considered infeasible without ground-truth survey data

### 6.4 Strategies for Filling Gaps

| Strategy | Description | Typical Application |
|---|---|---|
| Additional field surveys | Targeted sampling to fill spatial or temporal gaps | Missing ecosystem extent data, condition indicators |
| Remote sensing / satellite data | Use freely available imagery (e.g., Sentinel-2, Landsat) for extent mapping or condition proxies | Ecosystem extent, vegetation indices, sea surface temperature |
| Stakeholder engagement | Obtain private datasets through partnerships with researchers, agencies, or industry | Unpublished research data, commercial records |
| Indigenous and local knowledge | Engage Traditional Owners and local communities for ecological knowledge and baseline data | Cultural values, historical baselines, species presence |
| Citizen science | Use community-collected data (e.g., recreational fishing apps, eBird, iNaturalist, dive surveys) | Recreational use, species presence, phenology |
| Literature-based estimation | Apply published per-hectare or per-unit rates from comparable systems | Carbon sequestration rates, nursery service values |
| Statistical modelling | Develop models linking available covariates to target variables | Habitat extent prediction, species distribution |
| Administrative data linkage | Connect datasets from different agencies (e.g., tourism, employment, fisheries, land management) | Economic accounts, use accounts |

---

## 7. SOP 6 — Documenting and Reporting Data Quality Decisions

### 7.1 Objective

Ensure that all data quality and relevance decisions are transparently documented so that account users understand the strengths and limitations of the compiled accounts.

### 7.2 Required Documentation

For each compiled account, produce the following metadata:

| Document Element | Content |
|---|---|
| Data sources used | Inventory codes, names, and descriptions of all datasets contributing to the account |
| Quality scores | Composite and dimension-level scores for each dataset |
| Transformations applied | Description of spatial, temporal, and compliance transformations |
| Modelling applied | Description of any gap-filling models, including assumptions and parameters |
| Coverage achieved | Map or description of spatial coverage, with areas flagged as modelled or missing |
| Uncertainty assessment | Qualitative or quantitative description of uncertainty by component |
| Known limitations | Specific issues that affect interpretation (e.g., proxy measures, outdated data, spatial mismatch) |
| Recommendations | Priority data collection actions to improve the account in future iterations |

### 7.3 Quality Flag System

Attach quality flags to account entries to communicate confidence:

| Flag | Meaning | Action Required |
|---|---|---|
| A — High confidence | Data directly measured, high quality score, full spatial and temporal coverage | None |
| B — Moderate confidence | Data adequate but transformed (interpolated, modelled, or from adjacent area) | Document transformation method |
| C — Low confidence | Data from proxy measures, sparse coverage, or outdated sources | Flag in reporting; prioritise for improvement |
| D — Data-deficient | Account compiled from modelled estimates with high uncertainty, or major gaps remain | Highlight as provisional; plan targeted data collection |
| X — Not compiled | Insufficient data to compile account | Document gap and required data |

---

## 8. Decision Flowchart — Is This Dataset Suitable for Accounting?

```
START: Candidate dataset identified
  |
  v
[1] Does it relate to a proposed account component?
  |-- No  -> Exclude (record in inventory as contextual)
  |-- Yes
  v
[2] Score data quality (SOP 2, 6 dimensions)
  |-- Score < 40%  -> Flag as low quality; consider only if no alternatives exist
  |-- Score >= 40%
  v
[3] Does data cover the accounting area spatially?
  |-- Full coverage    -> Low spatial transformation effort
  |-- Partial coverage -> Assess interpolation/extrapolation feasibility
  |-- No coverage      -> Can data from adjacent areas be extrapolated?
  |     |-- No  -> Flag as data gap; seek alternatives
  |     |-- Yes -> High transformation effort; flag uncertainty
  v
[4] Does data align with the accounting period temporally?
  |-- Yes -> Low temporal transformation effort
  |-- No  -> Can temporal interpolation/extrapolation be applied?
  |     |-- No  -> Flag as data gap
  |     |-- Yes -> Medium-High effort; flag uncertainty
  v
[5] Does data comply with SEEA EA definitions and classifications?
  |-- Directly compliant -> Low compliance effort
  |-- Compatible         -> Crosswalk required (Medium effort)
  |-- Proxy measure      -> Modelling required (High effort)
  |-- Incompatible       -> Exclude or major re-estimation
  v
[6] Compile overall assessment:
  |-- Effort = max(spatial, temporal, compliance effort)
  |-- Assign quality flag (A/B/C/D)
  |-- Record in account assessment summary table
  |
END: Dataset assessed and documented
```

---

## 9. Accounting Considerations by Component

When assessing data relevance, apply the following component-specific considerations:

| Component | Key Consideration |
|---|---|
| All components | Consistent definition of spatial units across all accounting components |
| Ecosystem Extent | Classifications and crosswalks between ecosystem typologies; consideration of context (e.g., upstream land use affecting downstream ecosystems) |
| Use | Classifications complementary with extent accounts; distinction between use types and their potential pressures |
| Ecosystem Condition | Reference periods and aggregation methods for condition indicators; alignment of condition variables with the SEEA EA condition typology |
| Ecosystem Assets | Measurement units; balancing of opening and closing stock with flows (additions and reductions) |
| Ecosystem Services (physical) | Measurement units; balancing of supply and use; avoiding double-counting between intermediate and final services |
| Ecosystem Services (monetary) | Market prices for marketed services; non-market valuation methods for non-marketed services; clear labelling of value types; balancing of supply and use |

---

## 10. Equipment and Resource Requirements

### 10.1 Desktop Assessment Resources

| Resource | Purpose |
|---|---|
| GIS software (QGIS, ArcGIS) | Spatial data assessment, coverage analysis, overlay analysis |
| Spreadsheet software | Quality scoring, inventory management, summary tables |
| Database or inventory system | Structured storage of dataset metadata and quality scores |
| Access to data portals | Downloading public datasets (e.g., government open data portals, global repositories) |

### 10.2 Stakeholder Engagement Resources

| Resource | Purpose |
|---|---|
| Contact database | Tracking data providers, researchers, and agencies |
| Engagement log | Recording communications, data requests, and responses |
| Data sharing agreements | Formalising access to private or restricted datasets |

### 10.3 Assessment Team Expertise

| Expertise | Role in Assessment |
|---|---|
| Environmental science | Evaluating ecological data quality and relevance |
| Spatial analysis / GIS | Assessing spatial characteristics, coverage, and transformation requirements |
| Economics / statistics | Evaluating socioeconomic data, valuation data quality |
| Environmental-economic accounting | Ensuring compliance with SEEA EA standards |
| Data management | Maintaining inventory, documentation, and quality records |

---

## 11. Temporal Design for Iterative Assessment

- The data inventory is a living document — add new datasets as they are discovered
- Quality scores should be updated when new information about a dataset becomes available
- Re-assess data gaps after each accounting cycle to track improvement
- Coordinate with data providers to align future collection with accounting needs
- Where ongoing monitoring programs exist, engage early to influence survey design for accounting compatibility

---

## 12. Worked Example — Geographe Marine Park Seagrass Extent Account

This example illustrates the full assessment workflow using the Geographe Marine Park ocean accounting pilot (IDEEA Group, 2020).

### 12.1 Context

Geographe Marine Park is located within Geographe Bay, Western Australia (977 km^2 of Commonwealth waters). The project aimed to compile extent, condition, asset, service, and use accounts for the marine park under the Technical Guidance on Ocean Accounting. Seagrass meadow extent was identified as a primary account — foundational to all subsequent condition, asset, and service accounts.

### 12.2 Step 1 — Identify candidate datasets from inventory

| Inventory Code | Data Type | Coverage | Quality Score |
|---|---|---|---|
| OE_001 | Polygonal (seagrass mapping 2004–2007) | Partial (inshore shallow waters) | 87% |
| OE_003 | Polygonal (national seagrass distribution) | Partial (inshore, overlapping with OE_001) | 68% |
| OE_004 | Polygonal (WA Department of Parks and Wildlife habitat mapping) | Partial (inshore, most detailed) | 80% |
| MUL_036 | Point (BRUV presence/absence data) | Extensive across marine park | 72% |
| OE_025 | Polygonal (Seamap Australia national composite) | Combines OE_001/OE_003/OE_004; no additional coverage | — |

### 12.3 Step 2 — Assess each dataset against account-readiness criteria

| Dataset | Spatial Transformation | Effort | Temporal Alignment | Compliance | Notes |
|---|---|---|---|---|---|
| OE_001 + OE_003 + OE_004 | Merge; clip to marine park boundary | Low | One-off surveys (2004–2007); no repeat | Compatible with SEEA ecosystem extent definitions | Partial inshore coverage only; deeper waters unrepresented |
| MUL_036 | Not account-ready (point data) | — | One-off survey (2016) | Presence/absence not directly mappable to polygonal extent | Useful for understanding ecosystem distribution in unmapped areas |

### 12.4 Step 3 — Identify data gaps

- **Gap:** No polygonal extent data for deeper offshore waters of the marine park
- **Priority:** Critical — extent is foundational to all other accounts, and the delineation of ecosystem types is required for condition, asset, and service accounts
- **Cause:** Research effort in Geographe Bay was concentrated on shallow inshore waters (seagrass monitoring, fisheries), leaving deeper Commonwealth waters unmapped

### 12.5 Step 4 — Assess modelling options for gap-filling

| Approach | Input Data | Method | Effort | Expected Coverage |
|---|---|---|---|---|
| 1 | MUL_036 (point data) | Proportional estimate: multiply proportion of seagrass-positive observations by total marine park area | Medium | All (non-spatial estimate only) |
| 2 | OE_001/OE_003/OE_004 (polygonal) + OE_013/OE_014 (bathymetry) + OC_016 (primary productivity) | Determine statistical relationship between known extent and covariates; extrapolate to unmapped areas | High | Partial–Full (depends on strength of covariate relationships) |
| 3 | MUL_036 (point data) | Geostatistical interpolation (kriging) to produce continuous coverage surface | Very High | All (spatial) |

### 12.6 Step 5 — Preferred approach and quality flags

- **Preferred approach:** Use merged polygonal data (OE_004 as primary source for greatest detail) for mapped inshore areas, supplemented by covariate-based extrapolation (Approach 2) to extend coverage into deeper waters
- **Quality flags:**
  - Directly mapped inshore areas: **Flag B** (moderate confidence — data adequate but multiple sources merged)
  - Modelled offshore areas: **Flag C** (low confidence — extrapolated, dependent on covariate relationships)
- **Improvement recommendation:** An additional benthic habitat survey of the marine park's deeper waters was planned for 2020 but cancelled due to Covid-19. This survey remains the highest-priority data collection action.

### 12.7 Step 6 — Scalability assessment

- Seamap Australia (OE_025) provides a national composite of marine ecosystem extent but has significant gaps in Commonwealth waters compared to State waters
- National seagrass extent accounts would require coordinated data collection across states and territories, combining local high-resolution datasets (similar to the Geographe approach) with national composites
- For other ecosystem types (rocky reef, macroalgae, sandy bottoms), the same assessment workflow applies — each showed similar patterns of partial inshore coverage and offshore gaps

---

*Framework aligned with the ABS Data Quality Framework, UN SEEA Central Framework (2014), UN SEEA EA (2021), and the Technical Guidance on Ocean Accounting (GOAP, 2019). Case study examples drawn from: IDEEA Group (2020) Data Assessment Report, Ocean Accounting Pilot for Geographe Marine Park.*
