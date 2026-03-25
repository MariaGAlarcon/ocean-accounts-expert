# Standard Operating Procedures: Measuring Ecosystem Condition

**Framework:** SEEA EA Ecosystem Condition Accounts
**Applicable to:** Coastal and marine ecosystem accounting in tropical and subtropical regions
**Accounting Period:** [Define for your accounting area]

---

## 1. Overview

Ecosystem condition accounts measure the state or quality of an ecosystem asset relative to a reference condition. Condition is assessed through ecological indicators compared to reference benchmarks, producing a condition index between 0 (completely degraded) and 1 (reference/undegraded state).

Three marine ecosystem types are commonly assessed in tropical coastal accounts:

| Ecosystem Type | IUCN GET Code | Example Area (Laamu Atoll, Maldives) |
|---|---|---|
| Photic coral reefs | M1.3 | 7,395.3 ha |
| Seagrass meadows | M1.1 | 4,855.5 ha |
| Intertidal forests / Mangroves | MFT1.2 | 18.7 ha |

> **Note:** The ecosystem types, extent values, and species assemblages will vary by accounting area. Adapt the list above to the ecosystems present in your study region. Examples from other regions (e.g., Southeast Asian mangrove-dominated coasts, Pacific Island reef systems, East African seagrass beds) may include different species and spatial scales.

### 1.1 Tiered Assessment Profile

This SOP is assessed against the [Tiered Assessment Framework](tiered_assessment_framework.md), which evaluates procedures across three independent dimensions: **A — Feasibility and Resource Intensiveness**, **B — Accuracy and Confidence**, and **C — Difficulty of Implementation**. Condition measurement is inherently more resource-intensive than extent measurement because it requires in-situ field surveys. Sub-procedures range from remote sensing proxies (Tier 1) to multi-site, multi-indicator field campaigns with statistical spatial extrapolation (Tier 3).

**Sub-procedure tier matrix:**

| Sub-procedure | A: Feasibility | B: Accuracy | C: Difficulty | Notes |
|---|---|---|---|---|
| **Coral reef condition** | | | | |
| Remote sensing proxies only (SST, DHW, chlorophyll-a; Section 6) | 1 | 1 | 1 | Free satellite archives; no field effort required |
| Limited UVC field campaign — few sites, single season (Section 3) | 2 | 2 | 2 | Dive logistics; moderate personnel and equipment |
| Full UVC with multi-season repeat and statistical spatial modelling | 3 | 3 | 3 | Large multidisciplinary team; repeat surveys required |
| **Seagrass condition** | | | | |
| Literature benchmarks only — no primary field data | 1 | 1 | 1 | Desk-based; high transfer uncertainty |
| Field SEQI survey — shoot density, cover, biomass (Section 4) | 2 | 2 | 2 | Snorkel or dive access; species identification skills |
| SEQI field survey + spatially explicit RS extrapolation (Section 7) | 2–3 | 3 | 3 | Statistical modelling and RS calibration expertise |
| **Mangrove condition** | | | | |
| Canopy extent from satellite only — no structural data | 1 | 1 | 1 | Free imagery; no field work required |
| Standard quadrat survey — height, DBH, density, canopy (Section 5) | 2 | 2 | 2 | Field access; basic allometric equations |
| Nested-plot survey with allometric equations and SOC measurement | 3 | 3 | 3 | Laboratory carbon analysis; specialist expertise |
| **Cross-cutting** | | | | |
| Statistical spatial extrapolation — GLM or Random Forest (Section 7) | 2–3 | 2 | 3 | Specialist statistical and remote sensing skills |
| Condition account compilation — SEEA EA format (Section 8) | 1 | 2 | 1 | Spreadsheet; follows from field or RS data |

**Default approach tier profile:** The standard workflow in this SOP — UVC field surveys for coral, SEQI surveys for seagrass, quadrat surveys for mangrove — is **A: Tier 2, B: Tier 2, C: Tier 2**.

**Tier 1 (rapid) alternative:** Use remote sensing proxies (SST, DHW, turbidity from Section 6) combined with condition classes from global assessments (e.g., Allen Coral Atlas reef condition layer). This approach is not described in detail in this SOP; outputs must be flagged as low confidence, and field calibration is strongly recommended before condition estimates are used in service accounts.

**Binding constraint:** Dimensions A and C typically bind together for condition accounts — field campaigns are both expensive and logistically demanding. Statistical spatial extrapolation (Section 7) can extend spatial coverage without proportional field effort, but requires specialist skills (C: Tier 3).

**Coherence note:** Remote sensing proxies (Tier 1 B) cannot substitute for field condition indicators in SEEA EA-compliant accounts — they provide environmental context but not the direct ecological variables required for condition indices (Section 8). A coherent condition account requires at minimum Tier 2 field data for each ecosystem type reported.

---

## 2. Spatial Framework

All condition data are referenced to a **Basic Spatial Unit (BSU)** grid:

- **Resolution:** Typically 10 m x 10 m cells (adjust based on available imagery and ecosystem grain)
- **Coverage:** Shoreline to the practical depth limit for satellite-based benthic classification (e.g., ~25 m depth), encompassing all target ecosystem types across the accounting area
- **Assignment rule:** Each BSU is assigned to exactly one ecosystem type based on dominant cover class
- **Depth limit rationale:** Represents the practical limit for satellite-based benthic classification and encompasses the depth range of all target ecosystem types

---

## 3. Coral Reef Condition

### 3.1 Indicators Measured

| Indicator | Unit | Reference Level | Example Measured Value | Condition Index |
|---|---|---|---|---|
| Live hard coral cover | % cover | Regional benchmark (e.g., ~40% for healthy Indo-Pacific reefs) | e.g., 19.67% | e.g., 0.49 |
| Coral bleaching prevalence | % of colonies affected | 0% (no bleaching) | e.g., 10.97% | — |
| Fish abundance and diversity | Biomass / species count | Site-specific benchmark | Measured per site | — |
| Dead coral / recently dead coral cover | % cover | 0% | Measured per site | — |
| Algal cover (macroalgae, turf, CCA) | % cover | Low (site-specific) | Measured per site | — |
| Key invertebrate presence | Presence / abundance | — | Recorded per site | — |

**Example dominant coral genera (Maldives):** Porites, Acropora, Pocillopora. Dominant genera will vary by region — identify locally relevant taxa.

### 3.2 Survey Design

- **Method:** Underwater Visual Census (UVC) using belt transects
- **Number of sites:** Sufficient to represent the range of reef habitats (e.g., 17 sites were used in Laamu Atoll, Maldives)
- **Site selection criteria:** Representative of the range of reef habitats and exposure conditions present in the accounting area (e.g., exposed outer reef slopes, sheltered lagoon reefs, channel reefs, fringing reefs)
- **Transect depth:** 5–10 m on the reef slope
- **Transect dimensions:** 20 m x 20 m per transect; 4 transects per site
- **Survey area per site:** 1,600 m^2
- **Survey timing:** Repeat surveys across multiple field campaigns for temporal comparison

### 3.3 Field Protocol

At each transect, record:

1. **Percent cover of live hard coral** — identified to genus level
2. **Percent cover of soft coral**
3. **Percent cover of dead coral and recently dead coral**
4. **Percent cover of algae** — distinguished as:
   - Macroalgae
   - Turf algae
   - Crustose coralline algae (CCA)
5. **Percent cover of other substrate** — sand, rubble, rock
6. **Coral bleaching** — presence and severity
7. **Fish abundance and diversity** — using standard reef fish visual census protocols
8. **Key invertebrate species** — crown-of-thorns starfish (Acanthaster), giant clams (Tridacna), sea urchins

### 3.4 Data Collection Methods

- **Drop-camera surveys** for ground truth verification
- **Snorkel transects** for shallow reef assessment
- **Diver observations** along belt transects at depth

### 3.5 Example Results (Laamu Atoll, Maldives, 2022–2023)

- Mean live hard coral cover: 17.44% (2022) rising to 19.67% (2023) — early recovery from 2016 mass bleaching but still well below the ~40% reference
- Bleaching prevalence: 0.34% (2022) increasing to 10.97% (2023) — renewed thermal stress linked to elevated SST
- Turf algae cover inversely correlated with live coral cover, consistent with coral-algae competitive dynamics on degraded reefs

> **Other regions:** Results will differ based on local disturbance history, reef type, and biogeographic setting. Record your own baseline and interpret against regional reference benchmarks.

---

## 4. Seagrass Condition

### 4.1 Indicators Measured

| Indicator | Unit | Reference Level | Example Measured Value | Condition Index |
|---|---|---|---|---|
| Seagrass Ecological Quality Index (SEQI) | Composite (0–1) | 1.0 | 0.64 (mean) | 0.64 |
| Shoot density | Shoots per m^2 | Species-specific reference | Measured per site | — |
| Canopy height | cm | Species-specific reference | Measured per site | — |
| Percentage cover | % | Species-specific reference | Measured per site | — |
| Species richness | Count | Reference community composition | Up to 6 species | — |
| Above-ground biomass | g dry weight / m^2 | Literature values | Measured per site | — |
| Below-ground biomass | g dry weight / m^2 | Literature values | Measured per site | — |

### 4.2 Species Identified

Seagrass species composition will vary by region. Identify all species present to species level and record relative dominance. Example species recorded in Laamu Atoll, Maldives:

1. *Thalassia hemprichii* (dominant)
2. *Cymodocea rotundata* (dominant)
3. *Cymodocea serrulata*
4. *Halodule uninervis*
5. *Syringodium isoetifolium*
6. *Halophila ovalis*

> **Other regions:** Indo-Pacific sites may share similar species. Caribbean/Atlantic sites will have different assemblages (e.g., *Thalassia testudinum*, *Syringodium filiforme*). Adapt the species list accordingly.

### 4.3 Composite Index — SEQI

The **Seagrass Ecological Quality Index (SEQI)** integrates multiple condition indicators into a single composite score:

- **Input variables:** Shoot density, canopy height, percentage cover, species richness
- **Normalisation:** Each variable is normalised against reference values for the relevant species assemblage
- **Scale:** 0 (completely degraded) to 1 (reference condition)
- **Result range:** 0.571–0.715 across sites; mean ~0.64
- **Interpretation:** Moderate to good ecological quality

### 4.4 Survey Design

- **Method:** Benthic survey at designated seagrass sites across the accounting area
- **Data recorded per site:**
  1. Species identification and composition
  2. Shoot density (shoots per m^2)
  3. Canopy height (cm)
  4. Percentage cover (%)
  5. Above-ground biomass
  6. Below-ground biomass
- **Ground truth points:** Should be collected across the accounting area (shared with extent account validation). The number of points depends on the size and heterogeneity of the area (e.g., 357 points were used in Laamu Atoll, Maldives)

---

## 5. Mangrove Condition

### 5.1 Indicators Measured

| Indicator | Unit | Reference Level | Example Measured Value |
|---|---|---|---|
| Tree height | m | Mature stands of regionally dominant species | e.g., 3.7 m (mean) |
| Diameter at breast height (DBH) | cm (stems >= 2.5 cm) | Literature benchmarks | Measured per site |
| Stem density | Stems per hectare | Reference stand density | e.g., 3,500–4,500 stems/ha |
| Canopy cover | % (densiometer) | Mature closed canopy | e.g., 60–90% across plots |
| Species composition | Species presence/dominance | — | Region-specific (e.g., *Rhizophora mucronata*, *Ceriops tagal* in the Indo-Pacific) |
| Seedling / sapling density | Count per plot | Active regeneration benchmark | Recorded per plot |
| Substrate characteristics | Qualitative / categorical | — | Recorded per plot |

### 5.2 Survey Design

**Default approach:**
- **Location:** All significant mangrove sites within the accounting area (e.g., Hithadhoo island was the sole site in Laamu Atoll, Maldives)
- **Method:** Quadrat-based sampling along transects
- **Quadrat size:** 10 m x 10 m
- **Transect orientation:** Perpendicular to the shoreline, from seaward fringe to landward boundary
- **Total mangrove area:** Determined from extent account (e.g., 18.7 ha in Laamu Atoll, Maldives)

**Alternative: Nested sub-plot (quarter-plot) approach:**
- **Method:** Fixed 10 × 10 m plots subdivided into nested sections for different growth stages
- **Sub-plot structure:** 10 × 10 m for adult trees, 5 × 5 m for saplings (<1.5 m height), 1 × 1 m for seedlings
- **When to use:** Where dense mangrove thickets prevent standard quadrat deployment, where tidal inundation limits sampling area, or where growth-stage-specific data is required
- **Sampling limitations:** Document where full 10 × 10 m squares cannot be completed and enumerators sample adjacent areas

> **RNF BCAF example (Central Java):** 15 nested plots across four districts were sampled 2023–2025. Most fixed locations could not be surveyed as full squares due to dense thickets and tidal submersion. (Source: GOAP, 2025)

### 5.3 Field Protocol

Within each 10 m x 10 m quadrat, measure:

1. **Tree species identification** for every stem
2. **Tree height** — using clinometer and measuring tape
3. **Diameter at breast height (DBH)** — for all stems >= 2.5 cm diameter
4. **Stem density** — count of all stems per plot
5. **Canopy cover** — using a spherical densiometer
6. **Seedling and sapling counts** — for regeneration assessment
7. **Substrate characteristics** — soil type, depth, waterlogging

### 5.4 Equipment Required

| Equipment | Purpose |
|---|---|
| Clinometer | Tree height measurement |
| Measuring tape (diameter tape) | DBH measurement |
| Spherical densiometer | Canopy cover estimation (Method A) |
| Hemispherical (fisheye) camera + ImageJ software | Canopy cover estimation (Method B — alternative) |
| Quadrat frame / markers | Plot delineation (10 × 10 m; or nested sub-plots: 10 × 10 m, 5 × 5 m, 1 × 1 m) |
| Data sheets / tablet | Field recording |
| GPS | Georeferencing plot locations |

### 5.5 Example Results (Laamu Atoll, Maldives)

- Mean tree height of 3.7 m indicates a relatively young or stunted stand compared to mature Indo-Pacific mangroves
- High stem density (3,500–4,500 stems/ha) with small mean DBH — consistent with a recovering stand
- Active seedling recruitment confirms natural regeneration capacity
- Internal heterogeneity in canopy density and species composition not fully captured at 10 m BSU resolution

> **Other regions:** Mangrove structural characteristics vary greatly — mature deltaic mangroves (e.g., Sundarbans, Mekong Delta) may have substantially greater tree height and biomass. Calibrate reference levels to the regional species assemblage and growth conditions.

---

## 6. Biophysical Condition Indicators (Remote Sensing)

Additional broad-scale environmental indicators were derived from satellite remote sensing to provide context for interpreting field-measured condition:

| Indicator | Data Source | Purpose |
|---|---|---|
| Sea Surface Temperature (SST) | Satellite archives | Detect thermal anomalies linked to bleaching |
| Degree Heating Weeks (DHW) | Derived from SST time series | Cumulative thermal stress metric |
| Chlorophyll-a concentration | Satellite ocean colour | Water quality / nutrient status proxy |
| Turbidity | Satellite reflectance | Sediment loading / water clarity |

These variables provide atoll-wide environmental context and help explain spatial variation in field-measured ecosystem condition.

---

## 7. Statistical Modelling for Spatial Extrapolation

Field survey data are spatially limited. Statistical models were developed to extrapolate condition indicators across the full accounting area using remote sensing as predictors.

### 7.1 Approach

| Step | Description |
|---|---|
| 1. Predictor variables | Satellite-derived spectral indices and water column-corrected reflectance values (Sentinel-2) |
| 2. Response variables | Field-measured condition indicators (coral cover, seagrass biomass/coverage) |
| 3. Model types tested | Generalised Linear Models (GLMs) and Random Forest regression |
| 4. Validation | Cross-validation and independent test datasets |

### 7.2 Application by Ecosystem Type

- **Coral reefs:** Relationships between in-situ coral cover and satellite-derived spectral indices
- **Seagrass:** Biomass and coverage models using empirical relationships between field measurements and water column-corrected reflectance from Sentinel-2

---

## 8. Condition Account Compilation (SEEA EA Format)

### 8.1 Structure

The final condition account table records for each indicator:

| Column | Description |
|---|---|
| Ecosystem type | Coral reef, seagrass, or mangrove |
| Condition indicator | The measured variable |
| Reference level | Benchmark representing natural/undegraded state |
| Measured value | Value from the current accounting period |
| Condition index | Measured value normalised against reference level (0–1 scale) |

### 8.2 Condition Index Calculation

```
Condition Index = Measured Value / Reference Level
```

- Values closer to **1.0** indicate near-reference (good) condition
- Values closer to **0.0** indicate severely degraded condition
- For indicators where higher values indicate worse condition (e.g., bleaching), the index is inverted

### 8.3 Example Summary of Condition Indices (Laamu Atoll, Maldives)

| Ecosystem Type | Key Indicator | Condition Index | Interpretation |
|---|---|---|---|
| Coral reef | Live hard coral cover | ~0.49 | Poor — well below reference |
| Seagrass | SEQI composite | ~0.64 | Moderate to good |
| Mangrove | Mixed (height, density, canopy) | Variable | Young/recovering stand; mixed signals |

> Populate this table with your own measured values and interpret against region-appropriate reference levels.

---

## 9. Data Sources Summary

| Data Type | Source |
|---|---|
| Ground truth points | Benthic survey field campaign (drop-camera, snorkel, diver) — number of points depends on accounting area size |
| Coral reef condition | Underwater Visual Census at representative sites across multiple field campaigns |
| Seagrass condition | Field surveys with species ID, shoot density, biomass |
| Mangrove condition | Quadrat surveys at mangrove sites (height, DBH, density, canopy) |
| Satellite imagery (extent) | Freely available: Sentinel-2 (10 m); commercial options: Pleiades, Planet, SPOT, or equivalent |
| Remote sensing (condition) | SST, Chlorophyll-a, Turbidity from satellite archives (e.g., Copernicus, NASA) |
| Classification method | Spectral Angle Mapper (SAM), Random Forest, or other supervised classification on available imagery |
| Classification accuracy | Target >80% overall; accuracy typically varies by ecosystem type |
| Carbon stock (mangrove) | Species-specific allometric equations applied to DBH and height data |
| Carbon stock (seagrass) | Regression models relating carbon pools to field-measured coverage |

> **Data sources will vary by country and region.** Obtain fisheries, environmental, and spatial data from the relevant national agencies, regional bodies, or open-access repositories. Where possible, use locally validated parameters rather than global defaults.

---

## 10. Temporal Comparison Design

- **Extent accounts:** Opening vs. closing period from repeat satellite classification (define years for your accounting area)
- **Condition accounts:** Repeat field campaigns at the same sites provide inter-annual comparison
- Repeat surveys enable detection of trends (e.g., coral recovery, renewed bleaching, seagrass expansion or loss)
- Condition data should be interpreted against known disturbance history (e.g., mass bleaching events, cyclones, land-use change)

---

## Appendix A: Step-by-Step Measurement Instructions per Indicator

---

### A.1 Live Hard Coral Cover (% by genus)

**Ecosystem:** Coral reef
**Unit:** Percentage cover
**Reference level:** Regional benchmark for healthy reefs (e.g., ~40% for Indo-Pacific reefs)

**Equipment:** SCUBA gear, underwater slate/tablet, transect tape (20 m), quadrat frame or line-intercept tape, underwater camera, species ID guide.

**Steps:**

1. Navigate to the predetermined survey site on the reef slope at 5–10 m depth.
2. Lay a 20 m transect tape along the reef slope contour.
3. Along the transect, use point-intercept or line-intercept method: at regular intervals (e.g., every 0.5 m), record the substrate directly beneath the point.
4. For each point falling on live hard coral, identify the coral to **genus level** (e.g., *Porites*, *Acropora*, *Pocillopora*).
5. Repeat across 4 parallel transects per site, each 20 m x 20 m, totalling 1,600 m^2 survey area.
6. Calculate percent live hard coral cover = (number of points on live hard coral / total points surveyed) x 100.
7. Record genus-level breakdown as proportion of total live coral cover.
8. Photograph representative sections for QA verification.

**Calculation for condition index:**

```
Condition Index = Measured live coral cover (%) / Reference level (%)
Example (Maldives): 19.67% / 40% = 0.49
```

---

### A.2 Soft Coral Cover (%)

**Ecosystem:** Coral reef
**Unit:** Percentage cover

**Equipment:** Same as A.1.

**Steps:**

1. Use the same transect layout as the live hard coral survey (A.1).
2. At each intercept point, if the substrate is soft coral (e.g., Alcyonacea), record as "soft coral."
3. Calculate percent soft coral cover = (number of soft coral points / total points) x 100.
4. Record separately from hard coral — do not combine totals.

---

### A.3 Dead Coral and Recently Dead Coral Cover (%)

**Ecosystem:** Coral reef
**Unit:** Percentage cover

**Equipment:** Same as A.1.

**Steps:**

1. Use the same transect layout as A.1.
2. At each intercept point, distinguish between:
   - **Recently dead coral** — coral skeleton still intact, white or lightly algae-covered, retaining recognisable corallite structure (death likely within weeks to months).
   - **Old dead coral** — skeleton heavily encrusted by algae, sponges, or other organisms; corallite structure obscured.
3. Record each category separately at each intercept point.
4. Calculate percent cover for each category = (number of points in category / total points) x 100.
5. Note: recently dead coral is a key indicator of acute stress (e.g., recent bleaching mortality).

---

### A.4 Algal Cover — Macroalgae, Turf Algae, Crustose Coralline Algae (%)

**Ecosystem:** Coral reef
**Unit:** Percentage cover per algal functional group

**Equipment:** Same as A.1; magnifying lens optional for distinguishing CCA from turf.

**Steps:**

1. Use the same transect layout as A.1.
2. At each intercept point where algae is the dominant substrate, classify into one of three functional groups:
   - **Macroalgae** — fleshy, erect algae visible to naked eye (e.g., *Sargassum*, *Halimeda*, *Dictyota*). Typically >1 cm height.
   - **Turf algae** — short (<1 cm), filamentous algal mat covering substrate. Often mixed species.
   - **Crustose coralline algae (CCA)** — hard, encrusting pink/purple calcareous algae adhering flat to the substrate.
3. Record each group separately.
4. Calculate percent cover for each group = (points in group / total points) x 100.
5. Note: high turf algae cover relative to live coral is an indicator of degraded reef state.

---

### A.5 Other Substrate Cover — Sand, Rubble, Rock (%)

**Ecosystem:** Coral reef
**Unit:** Percentage cover per substrate category

**Equipment:** Same as A.1.

**Steps:**

1. Use the same transect layout as A.1.
2. At each intercept point not classified as living coral or algae, record substrate as:
   - **Sand** — loose unconsolidated sediment.
   - **Rubble** — broken, loose coral fragments not cemented together.
   - **Rock** — solid, consolidated reef framework with no living cover.
3. Calculate percent cover for each = (points in category / total points) x 100.
4. High rubble cover may indicate storm damage or bioerosion; document alongside condition notes.

---

### A.6 Coral Bleaching Prevalence (%)

**Ecosystem:** Coral reef
**Unit:** Percentage of colonies affected

**Equipment:** SCUBA gear, underwater slate/tablet, transect tape.

**Steps:**

1. Along the same belt transects used for cover assessment (A.1), conduct a colony-level bleaching survey.
2. Within each 20 m x 20 m transect area, count all **individual coral colonies** visible within the belt.
3. For each colony, assess bleaching status:
   - **Normal** — full pigmentation, no visible paling.
   - **Pale** — noticeably lighter than normal colouration but not white.
   - **Bleached** — colony is white or near-white; zooxanthellae largely expelled.
   - **Recently dead from bleaching** — white skeleton with intact corallite structure, tissue sloughing.
4. Record severity per colony: normal, pale, bleached, recently dead.
5. Calculate bleaching prevalence = (number of pale + bleached + recently dead colonies / total colonies counted) x 100.
6. Optionally record bleaching by genus to identify differentially susceptible taxa.
7. Cross-reference with SST data from satellite records to contextualise thermal stress.

---

### A.7 Fish Abundance and Diversity

**Ecosystem:** Coral reef
**Unit:** Abundance (individuals per transect), biomass (kg/ha), species richness (count)

**Equipment:** SCUBA gear, underwater slate, transect tape (50 m recommended for fish), fish species ID guide, optional: underwater camera.

**Steps:**

1. At each of the 17 reef sites, establish a **fish visual census transect** along the reef slope (standard protocol, typically 50 m x 5 m belt).
2. Swim the transect at a slow, constant pace (approximately 5–10 minutes per 50 m).
3. Record all fish observed within the 5 m belt width:
   - **Species** (identify to species level where possible, genus level otherwise).
   - **Abundance** — count of individuals per species.
   - **Estimated body length** (total length in cm) — for later biomass conversion using length-weight relationships.
4. Complete the transect in a single pass; do not double back.
5. Repeat at multiple transects per site as per survey design.
6. Post-survey, calculate:
   - **Species richness** = total number of species recorded.
   - **Abundance** = total individuals per transect area.
   - **Biomass** = convert length estimates to weight using published length-weight parameters (W = a x L^b), then sum per hectare.

---

### A.8 Key Invertebrate Species Presence

**Ecosystem:** Coral reef
**Unit:** Presence / absence; abundance where feasible

**Equipment:** SCUBA gear, underwater slate, transect tape.

**Steps:**

1. During the belt transect surveys (A.1), concurrently scan for the following key invertebrate species:
   - **Crown-of-thorns starfish** (*Acanthaster* spp.) — count all individuals within the belt transect. Note size (estimated arm diameter).
   - **Giant clams** (*Tridacna* spp.) — count all individuals; estimate shell length.
   - **Sea urchins** (e.g., *Diadema* spp.) — count all individuals within the belt.
2. Record presence/absence and counts per transect.
3. Note: Crown-of-thorns outbreaks (>0.3 individuals per survey tow or elevated densities) are a significant coral predation pressure indicator.

---

### A.9 Seagrass Species Composition

**Ecosystem:** Seagrass meadows
**Unit:** Species list and relative dominance

**Equipment:** Snorkel/SCUBA gear, quadrat frame (e.g., 0.25 m^2 or 0.5 m x 0.5 m), underwater slate, species ID guide, GPS.

**Steps:**

1. At each seagrass survey site, place the quadrat frame at predetermined or random points within the meadow.
2. Within each quadrat, identify all seagrass species present to species level. Example target species (Indo-Pacific):
   - *Thalassia hemprichii*
   - *Cymodocea rotundata*
   - *Cymodocea serrulata*
   - *Halodule uninervis*
   - *Syringodium isoetifolium*
   - *Halophila ovalis*

   Adapt to regionally present species (e.g., *Thalassia testudinum*, *Syringodium filiforme* in the Caribbean).
3. Record the relative dominance of each species (e.g., estimated % contribution to total cover within the quadrat).
4. Count the total number of species present per quadrat = **species richness**.
5. Repeat across multiple quadrats per site (minimum 3–5 replicates).

---

### A.10 Seagrass Shoot Density

**Ecosystem:** Seagrass meadows
**Unit:** Shoots per m^2

**Equipment:** Quadrat frame (0.25 m^2), underwater slate, snorkel/SCUBA gear.

**Steps:**

1. Place the quadrat frame on the seagrass bed at the survey point.
2. Count **all individual shoots** of each seagrass species within the quadrat. A shoot is defined as a single vertical stem arising from the rhizome, bearing one or more leaves.
3. For dense beds where a full count is impractical, count shoots within a sub-quadrat (e.g., 0.0625 m^2 = 0.25 m x 0.25 m) and scale up.
4. Record counts by species.
5. Calculate shoot density = total shoots / quadrat area (m^2). Extrapolate to shoots per m^2.
6. Repeat for a minimum of 3–5 replicates per site.
7. This value feeds into the SEQI calculation (see A.13).

---

### A.11 Seagrass Canopy Height

**Ecosystem:** Seagrass meadows
**Unit:** cm

**Equipment:** Ruler or measuring tape (mm precision), quadrat frame, snorkel/SCUBA gear.

**Steps:**

1. Within each quadrat, select a representative subset of shoots (e.g., 10–20 shoots per quadrat, or all shoots in a sub-quadrat).
2. For each selected shoot, measure the **length of the longest leaf** from the base of the leaf sheath to the leaf tip. Do not pull the leaf taut — measure its natural extended length in the water column.
3. Record all measurements to the nearest 0.5 cm.
4. Calculate mean canopy height per quadrat.
5. Average across replicates for a site-level mean.
6. This value feeds into the SEQI calculation (see A.13).

---

### A.12 Seagrass Percentage Cover

**Ecosystem:** Seagrass meadows
**Unit:** Percentage (%)

**Equipment:** Quadrat frame, underwater slate, snorkel/SCUBA gear, optional: standard photoquadrat reference images.

**Steps:**

1. Place the quadrat frame on the seabed at the survey point.
2. Visually estimate the percentage of the quadrat area occupied by living seagrass (leaves and visible above-ground structures), to the nearest 5%.
3. For consistency, use standard reference images or a Braun-Blanquet cover scale calibrated to percentage values.
4. Exclude bare sediment, algae, and dead seagrass material from the living cover estimate.
5. Record separately if significant epiphyte loading is present on seagrass blades.
6. Repeat for 3–5 replicates per site.
7. This value feeds into the SEQI calculation (see A.13) and the carbon stock regression models (Appendix B).

---

### A.13 Seagrass Ecological Quality Index (SEQI)

**Ecosystem:** Seagrass meadows
**Unit:** Composite index, 0–1 scale

**Inputs required:** Shoot density (A.10), canopy height (A.11), percentage cover (A.12), species richness (A.9).

**Steps:**

1. For each survey site, compile the measured values of:
   - Shoot density (shoots/m^2)
   - Canopy height (cm)
   - Percentage cover (%)
   - Species richness (count)
2. Obtain the **reference values** for each variable. Reference values represent the expected value in an undegraded seagrass meadow of the same species assemblage and bioregion (Indo-Pacific). Derive from published literature or regional baseline datasets.
3. **Normalise** each measured variable against its reference value:
   ```
   Normalised variable = Measured value / Reference value
   ```
   Cap at 1.0 (values exceeding the reference are set to 1.0).
4. **Calculate the SEQI** by integrating the normalised variables (e.g., arithmetic mean or weighted mean, depending on the SEQI formulation adopted):
   ```
   SEQI = mean(Normalised shoot density, Normalised canopy height,
               Normalised cover, Normalised species richness)
   ```
5. The resulting SEQI score ranges from 0 (completely degraded) to 1 (reference condition).
6. Report the SEQI score as the **condition index** for seagrass in the SEEA EA condition account table.

---

### A.14 Seagrass Above-Ground and Below-Ground Biomass

**Ecosystem:** Seagrass meadows
**Unit:** g dry weight / m^2

**Equipment:** Quadrat frame, corer (for below-ground), labelled bags, drying oven, balance (0.01 g precision).

**Steps:**

1. Within a quadrat at each survey site, **harvest all above-ground seagrass material** (leaves, sheaths, vertical stems) by cutting at the sediment surface. Place in a labelled bag.
2. For below-ground biomass, use a sediment corer (e.g., 15 cm diameter PVC pipe) pushed into the sediment to a depth of 20–30 cm within the same quadrat area. Extract the core and wash sediment through a sieve (1–2 mm mesh) to isolate roots and rhizomes.
3. In the laboratory:
   - Rinse samples in freshwater to remove salt and sediment.
   - Separate above-ground and below-ground fractions by species if required.
   - Dry at 60 degrees C to constant weight (typically 48–72 hours).
   - Weigh on a balance to 0.01 g precision.
4. Calculate biomass per m^2:
   ```
   Biomass (g/m^2) = Dry weight (g) / Quadrat area (m^2)
   ```
5. Report above-ground biomass (AGB) and below-ground biomass (BGB) separately.

---

### A.15 Mangrove Tree Height

**Ecosystem:** Mangroves
**Unit:** Metres

**Equipment:** Clinometer (e.g., Suunto PM-5), measuring tape (30 m+), data sheet, GPS.

**Steps:**

1. Within a 10 m x 10 m quadrat plot, measure the height of **every tree with DBH >= 2.5 cm**.
2. Stand at a known horizontal distance from the tree base (measure with tape; e.g., 10 m).
3. Using the clinometer:
   - Sight to the **top of the tree** and record the angle (degrees).
   - Sight to the **base of the tree** and record the angle (degrees).
4. Calculate tree height using trigonometry:
   ```
   Height = Distance x (tan(angle to top) - tan(angle to base)) + observer eye height
   ```
   If the base is at the same elevation as the observer, simplify to:
   ```
   Height = Distance x tan(angle to top) + (eye height - base height)
   ```
5. For trees shorter than ~3 m, a direct measurement with a telescoping height pole or measuring tape held vertically may be more practical and accurate.
6. Record height to the nearest 0.1 m.

---

### A.16 Diameter at Breast Height (DBH)

**Ecosystem:** Mangroves
**Unit:** cm

**Equipment:** Diameter tape (pi tape) or standard measuring tape, data sheet.

**Steps:**

1. Within the 10 m x 10 m quadrat, identify **all stems >= 2.5 cm diameter**.
2. Measure at **breast height** = 1.3 m above the ground on the uphill side of the tree.
3. For **stilt-root species** (e.g., *Rhizophora mucronata*):
   - Measure DBH at 1.3 m above the highest prop root or at the point where the main trunk is clearly discernible, whichever is higher.
   - If the trunk forks below 1.3 m, measure each fork stem separately as an individual tree.
4. Wrap the diameter tape around the trunk at breast height, keeping it horizontal and snug against the bark (no compression of bark).
5. If using a standard measuring tape, record circumference (cm) and convert:
   ```
   DBH (cm) = Circumference (cm) / pi (3.14159)
   ```
6. Record to the nearest 0.1 cm.
7. Record the species of each measured stem alongside the DBH value.

---

### A.17 Mangrove Stem Density

**Ecosystem:** Mangroves
**Unit:** Stems per hectare

**Equipment:** 10 m x 10 m quadrat frame / corner markers, data sheet.

**Steps:**

1. Within the established 10 m x 10 m quadrat (area = 100 m^2), count **all living stems with DBH >= 2.5 cm**.
2. Include multi-stemmed individuals: each stem arising from the same root mass that is >= 2.5 cm DBH is counted as a separate stem.
3. Record count by species.
4. Calculate stem density:
   ```
   Stems per hectare = (Total stems in plot / Plot area in m^2) x 10,000
   ```
   Example: 40 stems in a 100 m^2 plot = 4,000 stems/ha.
5. Average across all quadrats for a site-level estimate.

---

### A.18 Mangrove Canopy Cover

**Ecosystem:** Mangroves
**Unit:** Percentage (%)

Two methods are available:

#### Method A: Spherical Densiometer (default)

**Equipment:** Spherical densiometer (convex or concave), data sheet.

**Steps:**

1. Stand at the **centre of the 10 m x 10 m quadrat**.
2. Hold the densiometer at elbow height (approximately waist-to-chest level), level it using the built-in spirit level.
3. Count the number of **grid intersection points on the densiometer mirror that are covered by canopy** (i.e., where you can see canopy reflected, not open sky).
4. Take **four readings**, facing North, East, South, and West respectively.
5. Calculate canopy cover for each reading:
   ```
   Canopy cover (%) = (Number of covered points / Total grid points) x 100
   ```
   (For a standard concave densiometer with 24 grid points: multiply count by 4.17 to get %)
6. Average the four directional readings for the plot-level canopy cover estimate.
7. Repeat at each quadrat across the mangrove transect.

#### Method B: Hemispherical Photography with ImageJ (alternative)

**Equipment:** Camera with hemispherical (fisheye) lens, tripod or monopod, ImageJ software (free, open source).

**Steps:**

1. Mount camera with hemispherical lens on tripod/monopod at **1.3 m height** at the **centre of the quadrat**.
2. Level the camera and orient upward (lens facing the sky).
3. Capture photograph — ensure even exposure; avoid direct sunlight on the lens.
4. Import photograph into **ImageJ** software.
5. Convert to binary image using thresholding (canopy = dark, sky = light).
6. Calculate canopy cover:
   ```
   Canopy cover (%) = (canopy pixels / total pixels) x 100
   ```
7. Repeat at each plot.

**Advantages:** More objective and repeatable than densiometer; produces a permanent photographic record; enables consistent re-analysis.

> **RNF BCAF example (Central Java):** Hemispherical photography with ImageJ was used for all canopy assessments, replacing densiometers. (Source: GOAP, 2025)

---

### A.19 Mangrove Seedling and Sapling Density

**Ecosystem:** Mangroves
**Unit:** Count per plot (or per m^2)

**Equipment:** Quadrat frame, data sheet, ruler.

**Steps:**

1. Within the same 10 m x 10 m quadrat (or a nested sub-plot, e.g., 5 m x 5 m, if seedlings are very dense):
2. Count all **seedlings**: individuals < 1 m height and < 2.5 cm DBH.
3. Count all **saplings**: individuals >= 1 m height but < 2.5 cm DBH.
4. Identify each to species level.
5. Record counts separately for seedlings and saplings, by species.
6. Calculate density:
   ```
   Density per hectare = (Count / Plot area m^2) x 10,000
   ```
7. Active regeneration (high seedling/sapling density) indicates ecosystem resilience and recovery capacity.

---

### A.20 Mangrove Substrate Characteristics

**Ecosystem:** Mangroves
**Unit:** Qualitative/categorical

**Equipment:** Soil probe or small hand auger (optional), data sheet.

**Steps:**

1. At the centre and corners of each quadrat (5 points), describe:
   - **Soil type**: mud, sand, peat, coral rubble, mixed.
   - **Depth to hard substrate**: push a thin rod or soil probe into the sediment until refusal; record depth (cm).
   - **Waterlogging**: note whether the plot is inundated at time of survey (standing water depth in cm) or dry.
2. Record tidal state at the time of observation (high, mid, low tide).
3. Optionally, collect a small soil sample (top 5 cm) for laboratory analysis of organic matter content if soil organic carbon (SOC) estimation is planned.

---

### A.21 Sea Surface Temperature (SST) — Remote Sensing

**Ecosystem:** All (cross-cutting biophysical indicator)
**Unit:** Degrees Celsius (^o C)

**Steps:**

1. **Acquire SST data**: Download satellite-derived SST products covering the accounting area. Recommended sources:
   - NOAA Coral Reef Watch (daily, 5 km resolution)
   - MODIS/Aqua or VIIRS SST products (daily, 1 km resolution)
   - Copernicus Marine Service (multi-sensor, various resolutions)
2. **Define the time period**: Extract SST values for the accounting period and a climatological baseline period (e.g., 30-year long-term mean).
3. **Calculate anomalies**:
   ```
   SST anomaly = Observed SST - Long-term mean SST (for the same calendar period)
   ```
4. **Calculate Degree Heating Weeks (DHW)**:
   - DHW accumulates thermal stress above the bleaching threshold (defined as the maximum monthly mean SST + 1 ^o C) over a rolling 12-week window.
   ```
   DHW = Sum of (weekly SST - bleaching threshold) for all weeks where SST > threshold,
         over the preceding 12 weeks
   ```
   - DHW >= 4 indicates significant bleaching risk; DHW >= 8 indicates mass bleaching and mortality risk.
5. Extract values for each BSU or aggregate to reef/site level.
6. Report SST anomaly and DHW as biophysical context in the condition account.

---

### A.22 Chlorophyll-a Concentration — Remote Sensing

**Ecosystem:** All (cross-cutting biophysical indicator)
**Unit:** mg/m^3

**Steps:**

1. **Acquire ocean colour data**: Download satellite-derived chlorophyll-a products. Recommended sources:
   - Copernicus Marine Service (Sentinel-3 OLCI, 300 m resolution)
   - NASA MODIS/Aqua OC3M algorithm (4 km, or 1 km for regional products)
2. **Define the time period**: Extract monthly or seasonal composites for the accounting period.
3. **Extract values** for the accounting area or individual BSUs.
4. **Compare to baseline**: Calculate the ratio or anomaly relative to a climatological mean for the same season.
5. **Interpretation**: Elevated chlorophyll-a may indicate nutrient enrichment (eutrophication), which can promote algal growth on reefs and reduce water clarity for seagrass.
6. Report as a supporting biophysical indicator alongside field-measured condition data.

---

### A.23 Turbidity — Remote Sensing

**Ecosystem:** All (cross-cutting biophysical indicator)
**Unit:** NTU (Nephelometric Turbidity Units) or FNU, or satellite-derived reflectance proxy

**Steps:**

1. **Acquire turbidity or suspended sediment data**: Use satellite reflectance products that estimate turbidity or total suspended matter (TSM). Recommended:
   - Sentinel-2 Band 4 (665 nm) or Band 5 (705 nm) reflectance as a turbidity proxy after atmospheric correction.
   - Copernicus Marine Service TSM products.
2. **Apply a turbidity algorithm**: Convert reflectance to turbidity using an empirical or semi-analytical algorithm validated for the region (e.g., Dogliotti et al. 2015 for moderate turbidity waters).
3. **Extract values** for the accounting area, matching the spatial resolution of the BSU grid where feasible.
4. **Compare to baseline** or water quality thresholds relevant to coral reef and seagrass light requirements.
5. **Interpretation**: Elevated turbidity reduces light penetration, directly affecting coral and seagrass photosynthesis and growth.
6. Report as a supporting biophysical indicator.

---

## Appendix B: Carbon Stock Estimation Methods (Step-by-Step)

Although carbon stocks feed into the asset account rather than the condition account, they are derived from the same field measurements and are included here for completeness.

### B.1 Mangrove Carbon Stock

**Inputs required:** DBH (A.16) and tree height (A.15) from quadrat surveys.

Two allometric approaches are available:

#### Approach A: Height-Based Allometry (ENDhERI default)

1. For each measured stem, apply species-specific allometric equations using DBH and height (e.g., Wartman et al. 2022 for Indo-Pacific mangroves):
   ```
   Above-ground biomass (AGB) = a x DBH^b x Height^c
   ```
   Where a, b, c are species-specific parameters from a single primary source calibrated for the dominant species.

#### Approach B: Wood-Density-Based Multi-Source Allometry (RNF BCAF alternative)

1. For each measured stem, apply species-specific allometric equations using **wood density (ρ)** as an explicit variable, drawing from multiple published sources:
   ```
   Above-ground biomass (AGB) = a x ρ x DBH^b
   ```
   Where ρ = species-specific wood density (g/cm³).

   Key allometric sources for Indonesian mangroves:
   - Komiyama et al. (2005) — general mangrove allometry
   - Komiyama et al. (2008) — below-ground biomass conversion
   - Kauffman & Donato (2012) — carbon fractions
   - Kusmana et al. (2018) — Indonesian-specific models
   - Sidik et al. (2019), Dharmawan & Siregar (2008), Tarlan (2008), Malabrigo et al. (2017), Sutaryo (2009), Forqurean et al. (2014)

2. **Below-ground biomass (BGB)** — use the Komiyama et al. (2008) equation as a simplified conversion from AGB, rather than fixed root-to-shoot ratios.

3. **Carbon fractions** — apply 47% for AGB and 39% for BGB (Kauffman & Donato, 2012), rather than a single 47% fraction for all pools.

> **When to use Approach B:** Where diverse mangrove assemblages (>3 species) require species-level resolution, where 11+ allometric sources are available, or where wood density varies significantly across species (e.g., Central Java with 10+ species including *Rhizophora mucronata*, *Avicennia marina*, *Bruguiera gymnorrhiza*, *Sonneratia alba*). (Source: GOAP, 2025)

#### Common Steps (both approaches)

2. Sum AGB across all stems in each quadrat. Convert to per-hectare values.
3. Estimate **below-ground biomass (BGB)** using root-to-shoot ratios (Approach A) or Komiyama et al. 2008 conversion (Approach B).
4. Convert biomass to carbon:
   ```
   Carbon (Mg C) = AGB biomass (Mg) x 0.47 (Approach A)
                    AGB biomass (Mg) x 0.47 + BGB biomass (Mg) x 0.39 (Approach B)
   ```
5. Estimate **soil organic carbon (SOC)** to 1 m depth using soil core samples or published values.

   **Alternative SOC method (RNF BCAF):** Metal corer (r = 2.54 cm, l = 30 cm) to 10–20 cm depth with Walkley-Black wet-oxidation digestion (K₂Cr₂O₇-H₂SO₄) following Indonesia's National Standard SNI7724:2011. Where SOC data is unavailable for a follow-up period, apply a Tier 2 conservative rate of 1.2 ± 0.2 Mg C ha⁻¹ yr⁻¹ for degraded forests (Murdiyarso et al., 2023).

6. Sum all pools:
   ```
   Total carbon stock = Above-ground C + Below-ground C + SOC
   ```
7. Report total carbon stock for the accounting area (e.g., 1,283.58 Mg C for Hithadhoo, Maldives).
8. **Sequestration rate**: Apply published Net Carbon Production rates (Approach A) or use plot-based incremental biomass change from repeated tree censuses (see skill_regulating_services.md §3 alternative method).

### B.2 Seagrass Carbon Stock

**Inputs required:** Seagrass percentage cover (A.12) from field surveys.

**Steps:**

1. For each survey site, apply the **linear regression models**:
   ```
   Above-ground carbon (AGC) = 21.337810 + 0.13514 x Coverage (%)
   Below-ground carbon (BGC) = 53.2301 + 0.3055 x Coverage (%)
   ```
   (Units: g C per m^2.)
2. Calculate total carbon per site:
   ```
   Total C per m^2 = AGC + BGC
   ```
3. Extrapolate to the total seagrass extent:
   ```
   Total seagrass C = Mean C per m^2 x Total seagrass area (m^2)
   ```
4. Convert units: g C to tonnes C (divide by 1,000,000).
5. Report total for the accounting area (e.g., 4,209.34 tonnes C for Laamu Atoll, Maldives).
6. **Sequestration rate**: Apply published rates calibrated to local conditions (e.g., 4.44 Mg CO2/ha/yr for Indo-Pacific seagrass systems).

---

*Framework aligned with the UN SEEA EA (2021) international statistical standard. Maldives examples drawn from: Compiling the first Natural Capital Accounts in the Maldives: Methods report (ENDhERI Project). Alternative methods from: Applying SEEA EA at the Project Level in Central Java (RNF BCAF, GOAP, 2025).*
