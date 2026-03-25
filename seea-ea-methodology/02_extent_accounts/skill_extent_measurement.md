# Standard Operating Procedures: Measuring Ecosystem Extent

**Framework:** SEEA EA Ecosystem Extent Accounts
**Applicable to:** Coastal and marine ecosystem accounting in tropical and subtropical regions
**Accounting Period:** [Define for your accounting area]

---

## 1. Overview

Ecosystem extent accounts measure the area (in hectares) of each ecosystem type within the accounting area, tracking changes between an opening period and a closing period. Extent accounts are the spatial foundation for all other accounts — condition, ecosystem service, and asset accounts depend on knowing where ecosystems are and how much area they cover.

The extent account records:

| Component | Description |
|---|---|
| Opening extent | Area of each ecosystem type at the start of the accounting period |
| Additions | Area gained through ecosystem expansion, restoration, or reclassification |
| Reductions | Area lost through degradation, conversion, or reclassification |
| Net change | Additions minus reductions |
| Closing extent | Area at the end of the accounting period |

Three marine ecosystem types are commonly mapped in tropical coastal accounts:

| Ecosystem Type | IUCN GET Code | Example Extent (Laamu Atoll, Maldives) |
|---|---|---|
| Photic coral reefs | M1.3 | 7,395.3 ha (closing 2020) |
| Seagrass meadows | M1.1 | 4,855.5 ha (closing 2020) |
| Intertidal forests / Mangroves | MFT1.2 | 18.7 ha (stable) |

> **Note:** The ecosystem types, extent values, and classification categories will vary by accounting area. Adapt the list above to the ecosystems present in your study region. Additional categories (e.g., sand, rubble, deep water, land) are typically included to ensure complete spatial coverage of the accounting area.

### 1.1 Tiered Assessment Profile

This SOP is assessed against the [Tiered Assessment Framework](tiered_assessment_framework.md), which evaluates procedures across three independent dimensions: **A — Feasibility and Resource Intensiveness**, **B — Accuracy and Confidence**, and **C — Difficulty of Implementation**. Users should select a tier appropriate to their available resources, institutional capacity, and accuracy requirements; different tiers may be used for different sub-procedures within the same workflow.

**Sub-procedure tier matrix:**

| Sub-procedure | A: Feasibility | B: Accuracy | C: Difficulty | Notes |
|---|---|---|---|---|
| Accounting area boundary definition | 1 | 1 | 1 | Administrative or geomorphic boundary from existing data |
| Imagery — Sentinel-2 (free, 10 m) | 1 | 2 | 1 | Free via Copernicus; cloud processing in GEE available |
| Imagery — commercial HR (Pleiades, Planet, 0.3–3 m) | 2–3 | 3 | 1–2 | Procurement cost; licensing required |
| Ground truth — existing or reused data | 1 | 1 | 1 | No field mobilisation required |
| Ground truth — targeted field campaign | 2 | 2 | 2 | Vessel access, dive personnel, drop-camera equipment |
| Ground truth — intensive multi-season campaign | 3 | 3 | 2–3 | Multiple seasons; large multidisciplinary team |
| Image preprocessing — standard (L2A, glint, water column) | 1–2 | 2 | 1–2 | Well-documented methods; GEE or QGIS |
| Image preprocessing — physics-based radiative transfer inversion | 2–3 | 3 | 3 | Specialist remote sensing expertise required |
| Classification — SAM on Sentinel-2 (Sections 7.1, A.3) | 1 | 2 | 1–2 | Standard method; free software |
| Classification — Random Forest on HR imagery (Sections 7.2, A.4) | 2 | 2–3 | 2 | Statistical skills; commercial imagery required |
| Classification — deep learning | 3 | 3 | 3 | Rare expertise; large labelled training dataset required |
| Accuracy assessment (Section 8) | 1 | 2 | 1 | Standard confusion matrix; included in any workflow |
| Extent account compilation (Section 9) | 1 | 2 | 1 | Spreadsheet calculation from classified map |

**Default approach tier profile:** The standard workflow in this SOP — Sentinel-2 SAM classification with targeted field campaign and standard preprocessing — is **A: Tier 1–2, B: Tier 2, C: Tier 1–2**. This represents the appropriate baseline for operational national accounts.

**Tier 1 (rapid) alternative:** For a Tier 1 approach, use existing global habitat products (e.g., Global Mangrove Watch, Allen Coral Atlas) or Landsat-based classifications without a dedicated field campaign. This approach is not described in detail in this SOP; outputs should be flagged as low confidence and transfer errors relative to local conditions must be documented.

**Binding constraint:** For most applications, Dimension B (accuracy) is the binding constraint. Moving from Tier 2 to Tier 3 accuracy requires commercial HR imagery and intensive field validation — significant escalations in both A and C.

**Coherence note:** Extent account accuracy is the foundation for all downstream condition, service, and asset accounts. An extent account at Tier 1 accuracy limits all downstream accounts to Tier 1 regardless of the quality of subsequent data collection.

---

## 2. Spatial Framework

All extent data are referenced to a **Basic Spatial Unit (BSU)** grid:

- **Resolution:** Typically 10 m x 10 m cells (adjust based on available imagery and ecosystem grain)
- **Coverage:** Shoreline to the practical depth limit for satellite-based benthic classification (e.g., ~25 m depth), encompassing all target ecosystem types across the accounting area
- **Assignment rule:** Each BSU is assigned to exactly one ecosystem type based on dominant cover class
- **Depth limit rationale:** Represents the practical limit for satellite-based benthic classification and encompasses the depth range of all target ecosystem types

> **Alternative spatial units:** Some projects use a Marine Basic Spatial Unit (MBSU) grid following Rahayu et al. (2024), where each cell is classified by dominant ecosystem type using a majority rule (>51% coverage). Both BSU and MBSU approaches align with SEEA EA spatial accounting recommendations.

---

## 3. Accounting Area Definition

### 3.1 Boundary Establishment

**Step 1: Define the spatial extent of the accounting area**
- The accounting area boundary determines the spatial scope of all accounts
- Boundaries may be defined by:
  - Natural geomorphic features (e.g., atoll rim, reef crest, coastline)
  - Administrative boundaries (e.g., district, province, marine park)
  - Project-specific boundaries (e.g., restoration site perimeter)

| Boundary Type | Example | Advantages | Limitations |
|---|---|---|---|
| Geomorphic | Laamu Atoll boundary to ~25 m depth | Ecologically coherent; captures full ecosystem extent | May not align with administrative reporting units |
| Administrative | District boundaries (e.g., Central Java regencies via BPS/Statistics Indonesia) | Integrates with government statistics and multi-tier reporting hierarchies (province, regency, district, village) | May cut across ecosystem boundaries |
| Project-level | Restoration site + buffer; investor-focused accounting area | Directly relevant to management intervention; supports investment readiness and financing | Limited scope; may miss landscape context |

> **RNF BCAF example (Central Java):** Administrative boundaries from BPS (Statistics Indonesia) were used to define the accounting area across four coastal districts (Demak, Jepara, Kebumen, Cilacap) spanning two provinces. This enabled integration with Indonesia's four-tier government reporting hierarchy and direct support for silvofishery investment decisions and blue carbon market access through the IDXCarbon exchange. The project explicitly linked SEEA outputs to investor communication and financing readiness — demonstrating a value proposition beyond national statistical reporting. (Source: GOAP, 2025)

> **Maldives example:** The accounting area for Laamu Atoll covers 884.63 km^2 (161,947.7 ha total), encompassing 56 reefs and 90 islands, extending from the shoreline to approximately 25 m depth.

**Step 2: Establish depth and elevation limits**
- Define the seaward limit based on the practical depth for satellite-based benthic classification
- Define the landward limit to include all terrestrial margins of coastal ecosystems (e.g., mangrove landward boundary)

**Step 3: Document boundary justification**
- Record the rationale for the chosen boundary
- Note any areas excluded and the reasons for exclusion

---

## 4. Satellite Imagery Acquisition

### 4.1 Imagery Requirements

| Parameter | Requirement | Notes |
|---|---|---|
| Spatial resolution | 10 m or finer for atoll-wide classification | Higher resolution (0.3–3 m) for priority sites |
| Spectral bands | Visible (blue, green, red) + near-infrared minimum | Additional bands improve discrimination |
| Cloud cover | <10% over the accounting area | Composite generation may use multiple dates |
| Tidal state | Low tide preferred for intertidal and shallow habitats | Critical for mangrove and seagrass boundary accuracy |
| Time of year | Consistent season across accounting periods | Minimises seasonal variation in benthic reflectance |

### 4.2 Recommended Imagery Sources

| Satellite | Resolution | Access | Recommended Use |
|---|---|---|---|
| Sentinel-2 | 10 m (multispectral) | Free (Copernicus) | Atoll-wide or region-wide classification |
| Pleiades | 0.3 m (multispectral) | Commercial | Priority site detailed mapping |
| Planet SuperDove | 3 m (multispectral) | Commercial / research access | Supplementary classification |
| SPOT 6/7 | 1.5–5 m (multispectral) | Commercial | Supplementary classification |
| Landsat 8/9 | 30 m (multispectral) | Free (USGS) | Broad-scale or historical change detection |

> **Minimum approach:** Sentinel-2 provides adequate resolution for aggregate accounting purposes and is freely available. Commercial high-resolution imagery substantially improves boundary delineation and detection of fine-scale features (e.g., mangrove canopy gaps) but is not essential for all applications.

### 4.3 Temporal Requirements

- **Opening period:** Acquire imagery for the start of the accounting period (e.g., 2017)
- **Closing period:** Acquire imagery for the end of the accounting period (e.g., 2020)
- Both periods should use the best available cloud-free composites from the same season

---

## 5. Ground Truth Data Collection

### 5.1 Objective

Collect georeferenced field observations of benthic substrate and ecosystem type to train and validate the satellite image classification.

### 5.2 Survey Design

- **Number of points:** Sufficient to train and validate the classification across all ecosystem types (e.g., 357 georeferenced points were used in Laamu Atoll, Maldives)
- **Distribution:** Points should be stratified across:
  - All ecosystem types present (coral reef, seagrass, mangrove, sand, rubble, deep water)
  - The full range of depths and exposure conditions
  - Both optically clear and turbid areas
- **Allocation:** Reserve a subset (~20–30%) as independent validation data not used for training

### 5.3 Field Methods

| Method | Application | Data Collected |
|---|---|---|
| Drop-camera survey | Rapid assessment across a wide area | Substrate type, benthic cover class, depth, GPS coordinates |
| Snorkel transect | Shallow reef and seagrass verification | Cover class, species presence, habitat boundary |
| Diver observation | Deeper reef slopes and complex habitats | Detailed benthic composition, depth, GPS |
| Intertidal walk | Mangrove and intertidal habitats | Species composition, boundary delineation, GPS |

### 5.4 Field Protocol

At each ground truth point, record:

1. **GPS coordinates** (minimum accuracy: ±5 m; differential GPS preferred)
2. **Depth** (metres below sea surface, corrected for tidal state)
3. **Dominant substrate type** — the single cover class occupying >50% of the observation area:
   - Live coral (hard coral)
   - Seagrass
   - Mangrove
   - Sand
   - Rubble
   - Rock / consolidated reef
   - Macroalgae
   - Deep water (no benthic signal)
4. **Secondary substrate** — any cover class occupying >20% of the area
5. **Photograph** for QA verification
6. **Notes** — water clarity, tidal state, any unusual features

### 5.5 Timing

- Conduct ground truth surveys as close as possible to the satellite image acquisition dates
- Temporal mismatch between field data and imagery introduces classification uncertainty

---

## 6. Image Preprocessing

### 6.1 Atmospheric Correction

- Convert raw satellite imagery to surface reflectance
- For Sentinel-2: use Level-2A product (atmospherically corrected via Sen2Cor or equivalent)
- For commercial imagery: apply atmospheric correction provided by the imagery supplier or use standard algorithms (e.g., FLAASH, ATCOR, 6S)

### 6.2 Sun-Glint Removal

- Correct specular reflection from the water surface that obscures benthic signatures
- Apply established sun-glint correction methods (e.g., Hedley et al. 2005; Kay et al. 2009)
- Critical for tropical waters with low wind conditions and high sun angles

### 6.3 Water Column Correction

- Retrieve depth-invariant bottom reflectance to account for the attenuation of light through the water column
- Apply depth-invariant index methods (e.g., Lyzenga 1978/1981) or physics-based radiative transfer inversion
- Essential for discriminating benthic habitats at varying depths

### 6.4 Cloud Masking and Compositing

- Apply cloud and cloud-shadow masks
- Generate best-pixel composites from multiple acquisition dates within the target period
- Ensure temporal consistency within the composite

### 6.5 Co-Registration

- Align all imagery to the BSU grid (10 m x 10 m)
- Verify geometric accuracy against reference points
- Resample higher-resolution imagery to the BSU grid resolution using majority resampling for thematic classes or bilinear/bicubic for reflectance values

---

## 7. Classification Methods

Two classification approaches are commonly applied, either independently or in parallel:

### 7.1 Spectral Angle Mapper (SAM) — Sentinel-2

**Purpose:** Atoll-wide or region-wide classification at 10 m resolution.

**Steps:**

1. Extract spectral signatures (endmembers) for each target class from ground truth locations on the preprocessed Sentinel-2 imagery
2. For each pixel in the image, calculate the spectral angle between the pixel's spectral vector and each endmember spectral vector
3. Assign each pixel to the class with the smallest spectral angle (highest spectral similarity)
4. Apply a maximum angle threshold to reject pixels that do not closely match any endmember (classified as unassigned or mixed)

**Advantages:**
- Relatively insensitive to illumination variations and albedo effects — important in shallow marine environments where water column effects alter spectral signatures
- Computationally efficient for large-area classification

> **Maldives example:** SAM was applied to atmospherically corrected and sun-glint removed Sentinel-2 Level-2A imagery for both 2017 (opening) and 2020 (closing), classifying into coral reef, seagrass, mangrove, sand, rubble, deep water, and land categories.

### 7.2 Random Forest Machine Learning — High-Resolution Imagery

**Purpose:** Detailed classification at priority sites using high-resolution imagery (0.3–5 m).

**Steps:**

1. Prepare training data by extracting spectral values from ground truth locations on the high-resolution imagery
2. Train a Random Forest classifier: an ensemble of decision trees, each trained on a random subset of training data with a random subset of spectral features
3. Classify each pixel by majority vote across all trees in the ensemble
4. Extract variable importance rankings to understand which spectral features drive the classification

**Advantages:**
- Captures nonlinear relationships between spectral features and ecosystem types
- Handles correlated predictor variables (multi-band imagery)
- Provides variable importance and out-of-bag error estimates

> **Maldives example:** Random Forest was applied to Pleiades (0.3 m) and Planet SuperDove (3 m) imagery for detailed classification at priority sites. A comparison at Hithadhoo island showed that high-resolution imagery substantially improved mangrove boundary delineation and detection of canopy gaps.

### 7.3 Supervised Classification with Ground Truth Training (Alternative)

**Purpose:** Classification of terrestrial-coastal ecosystems where field campaigns provide well-defined training samples and water column corrections are less critical.

**When to use:** Mangrove-dominated coastlines, estuarine systems, or project-level accounts where field ground truth is available and the primary classification challenge is discriminating between mangrove, mudflat, aquaculture, and terrestrial vegetation — rather than depth-affected marine benthic habitats.

**Steps:**

1. Combine medium- and high-resolution imagery (e.g., SPOT 6/7 at 5 m + Sentinel-2 at 10 m) with atmospheric corrections applied by the imagery provider
2. Extract spectral values at ground truth training locations from field campaigns
3. Train a supervised classifier (Maximum Likelihood, SVM, or similar) on the training dataset
4. Classify all pixels in the imagery
5. Apply GIS-based post-classification refinement: filter isolated pixels and enhance spatial coherence
6. Validate against field-collected data and expert interpretation using confusion matrices
7. Assign to BSU or MBSU grid (dominant class per cell)

**Advantages over SAM/Random Forest in terrestrial-coastal contexts:**
- Field campaign ground truth provides well-defined training classes for mangrove features
- No need for water column correction in predominantly terrestrial-coastal settings
- GIS refinement step addresses spatial noise effectively
- Simpler workflow when spectral angle sensitivity to illumination is not required

> **RNF BCAF example (Central Java):** SPOT 6/7 and Sentinel-2 imagery were classified using supervised methods with ground truth from field campaigns across four coastal districts. Classification distinguished mangrove from mudflat, aquaculture ponds, and terrestrial vegetation. Only one IUCN GET ecosystem type was mapped (MFT1.2 — mangroves), compared to three in the Maldives. (Source: GOAP, 2025)

### 7.4 Other Supervised Classification Methods

Additional supervised approaches may be appropriate depending on local conditions:

| Method | Application Context |
|---|---|
| Maximum Likelihood | Where class distributions are approximately Gaussian; well-established baseline method |
| Support Vector Machine (SVM) | Where training samples are limited; effective for high-dimensional data |
| Object-Based Image Analysis (OBIA) | Where spatial context and texture are important for discrimination |
| Deep Learning (CNN) | Where large training datasets are available; best for very high resolution imagery |

### 7.4 Classification Categories

The classification must include all major benthic cover classes to achieve complete spatial coverage:

| Class | IUCN GET Code | Description |
|---|---|---|
| Coral reef | M1.3 | Live coral-dominated reef structures in the photic zone |
| Seagrass | M1.1 | Submerged marine vegetation meadows |
| Mangrove | MFT1.2 | Intertidal forest and shrubland |
| Sand | — | Unconsolidated sandy substrate |
| Rubble | — | Broken coral fragments, not cemented |
| Rock | — | Consolidated reef framework without living cover |
| Macroalgae | — | Fleshy algae-dominated areas (if spectrally distinguishable) |
| Deep water | — | Beyond depth limit for benthic classification |
| Land | — | Terrestrial surface above high-water mark |

> Each BSU is assigned to exactly one class based on dominant cover. Only the ecosystem type classes (coral reef, seagrass, mangrove) contribute to the ecosystem extent account; other classes provide spatial context and enable accounting area completeness.

---

## 8. Classification Accuracy Assessment

### 8.1 Objective

Quantify classification reliability using independent validation data withheld from the training process.

### 8.2 Accuracy Metrics

| Metric | Definition | Target |
|---|---|---|
| Overall accuracy | Proportion of correctly classified validation points across all classes | >80% |
| Producer's accuracy (per class) | Proportion of reference points for a given class that were correctly classified (1 − omission error) | Report per class |
| User's accuracy (per class) | Proportion of classified pixels for a given class that are actually that class (1 − commission error) | Report per class |
| Kappa coefficient | Agreement corrected for chance | >0.6 |

### 8.3 Confusion Matrix

Construct a confusion matrix (error matrix) cross-tabulating the classification result against the ground truth validation data:

```
                        Ground Truth (Reference)
                   Coral    Seagrass   Mangrove   Sand    Other
Classified as:
  Coral          [n_cc]    [n_cs]     [n_cm]     [n_cd]  [n_co]
  Seagrass       [n_sc]    [n_ss]     [n_sm]     [n_sd]  [n_so]
  Mangrove       [n_mc]    [n_ms]     [n_mm]     [n_md]  [n_mo]
  Sand           [n_dc]    [n_ds]     [n_dm]     [n_dd]  [n_do]
  Other          [n_oc]    [n_os]     [n_om]     [n_od]  [n_oo]
```

### 8.4 Common Accuracy Issues

| Issue | Typical Cause | Mitigation |
|---|---|---|
| Seagrass–sand confusion | Spectral similarity in shallow water; sparse seagrass cover | Multi-temporal composites; additional ground truth in ambiguous areas |
| Coral–rubble confusion | Dead coral and rubble share spectral characteristics | Water column correction; inclusion of textural features |
| Mangrove boundary uncertainty | Mixed pixels at ecosystem edge; tidal state variation | High-resolution imagery for boundary refinement; consistent tidal state |
| Deep water misclassification | Benthic signal attenuated beyond depth limit | Enforce depth mask based on bathymetry |

> **Maldives example:** Overall accuracy exceeded 80% for Sentinel-2 mapping. Coral reef had the highest classification accuracy, followed by mangrove and seagrass. Seagrass accuracy was somewhat lower due to spectral confusion with sand in shallow water and algal communities.

---

## 9. Extent Account Compilation (SEEA EA Format)

### 9.1 Structure

The extent account records the area of each ecosystem type at two time points and the changes between them:

| Column | Description |
|---|---|
| Ecosystem type | Classification category (IUCN GET code) |
| Opening extent (ha) | Area at the start of the accounting period |
| Additions (ha) | Area gained (expansion, restoration, reclassification from other types) |
| Reductions (ha) | Area lost (degradation, conversion, reclassification to other types) |
| Net change (ha) | Additions minus reductions |
| Closing extent (ha) | Area at the end of the accounting period |

### 9.2 Calculating Extent from the Classified BSU Grid

**Step 1: Count BSUs per ecosystem type for each period**

For each classified image (opening and closing):
```
Extent (ha) = Number of BSUs classified as ecosystem type T × BSU area (ha)
```
For a 10 m x 10 m BSU grid: BSU area = 100 m^2 = 0.01 ha

**Step 2: Calculate additions and reductions**

Compare the opening and closing classifications on a per-BSU basis:
- **Addition to type T:** A BSU classified as another type in the opening period is classified as type T in the closing period
- **Reduction from type T:** A BSU classified as type T in the opening period is classified as another type in the closing period

**Step 3: Compile the ecosystem type change matrix**

The change matrix cross-tabulates ecosystem types between opening and closing periods:

```
                          Closing Period (2020)
                   Coral    Seagrass   Mangrove   Sand    Other   Total (Opening)
Opening (2017):
  Coral          [stable]  [C→SG]     [C→M]      [C→S]   [C→O]   Opening coral
  Seagrass       [SG→C]   [stable]    [SG→M]     [SG→S]  [SG→O]  Opening seagrass
  Mangrove       [M→C]    [M→SG]     [stable]    [M→S]   [M→O]   Opening mangrove
  Sand           [S→C]    [S→SG]      [S→M]      [stable] [S→O]  Opening sand
  Other          [O→C]    [O→SG]      [O→M]      [O→S]   [stable] Opening other
  Total (Closing): Closing coral  Closing seagrass  ...
```

- Diagonal entries = BSUs that remained the same type (stable)
- Off-diagonal entries = BSUs that changed type (transitions)
- Row totals = opening extent per type
- Column totals = closing extent per type

### 9.3 Example Extent Account (Laamu Atoll, Maldives, 2017–2020)

| Ecosystem Type | Opening 2017 (ha) | Additions (ha) | Reductions (ha) | Net Change (ha) | Closing 2020 (ha) |
|---|---|---|---|---|---|
| Coral reef (M1.3) | 7,437.2 | 121.3 | -163.2 | -41.9 | 7,395.3 |
| Seagrass (M1.1) | 4,892.6 | 86.4 | -123.5 | -37.1 | 4,855.5 |
| Mangrove (MFT1.2) | 18.7 | 0.0 | 0.0 | 0.0 | 18.7 |
| Other (sand, rubble, deep) | 149,599.2 | — | — | — | 149,678.2 |
| **Total accounting area** | **161,947.7** | — | — | — | **161,947.7** |

> The total accounting area should remain constant between opening and closing periods — all changes are internal reclassifications between ecosystem types. If the accounting area boundary changes between periods, document and reconcile the boundary adjustment.

### 9.4 Interpreting Change

| Change Pattern | Possible Drivers | Investigation |
|---|---|---|
| Coral reef → Sand/Rubble | Reef degradation (bleaching mortality, storm damage, bioerosion) | Cross-reference with condition data, disturbance history |
| Seagrass → Sand | Physical disturbance, environmental stress, dredging, anchor damage | Cross-reference with use accounts, environmental pressures |
| Sand → Coral reef | Reef recovery, coral recruitment on previously bare substrate | Verify with field data; may also be classification artefact |
| Sand → Seagrass | Seagrass colonisation of bare substrate | Verify with field data |
| Mangrove → Other | Land clearing, coastal development, natural dieback | Cross-reference with land-use change data |
| Stable mangrove | Small extent; no change detected at BSU resolution | High-resolution imagery may reveal sub-BSU changes |

> **Maldives example:** Coral reef loss was predominantly through conversion to rubble/sand (reef degradation) rather than to other living ecosystem types. Seagrass losses were similarly to sand substrate, suggesting physical disturbance or environmental stress. Both declines are consistent with known pressures including residual effects of the 2016 mass coral bleaching event and ongoing coastal development.

---

## 10. Multi-Resolution Comparison

Where both Sentinel-2 (10 m) and high-resolution commercial imagery are available, conduct a comparison for critical habitats:

### 10.1 Purpose

Evaluate whether the standard 10 m classification captures fine-scale features relevant to accounting accuracy.

### 10.2 Method

**Step 1:** Classify both Sentinel-2 and high-resolution imagery for the same area using the same ground truth training data

**Step 2:** Compare extent estimates for each ecosystem type between resolutions

**Step 3:** Identify discrepancies — where do they occur and why?

### 10.3 Expected Outcomes

| Feature | 10 m Sentinel-2 | 0.3–3 m High-Resolution |
|---|---|---|
| Aggregate extent (large meadows/reefs) | Adequate for accounting totals | Confirms totals with finer boundary delineation |
| Mangrove boundary | Adequate for total extent | Detects canopy gaps, zonation, and boundary detail |
| Small or fragmented patches | May be missed (below minimum mapping unit) | Detected and mapped |
| Internal heterogeneity | Not resolved within BSU | Reveals sub-BSU variation in canopy and species composition |

> **Maldives example:** A comparison at Hithadhoo island showed that high-resolution Pleiades imagery substantially improved boundary delineation and detection of mangrove canopy gaps. However, Sentinel-2 was adequate for aggregate atoll-wide accounting totals.

---

## 11. Data Sources Summary

| Data Type | Source |
|---|---|
| Satellite imagery (primary) | Sentinel-2 (10 m, free via Copernicus) |
| Satellite imagery (detailed) | Pleiades, Planet, SPOT, or equivalent (commercial) |
| Ground truth field data | Benthic survey campaigns — drop-camera, snorkel, diver, intertidal walk |
| Accounting area boundary | National or regional mapping agency; project-specific GIS data |
| Bathymetry | National hydrographic office; satellite-derived bathymetry |
| IUCN ecosystem typology | IUCN Global Ecosystem Typology (GET) |
| Historical imagery | Landsat archive (free via USGS) for long-term change detection |

> **Data sources will vary by country and region.** Obtain satellite imagery, boundary data, and bathymetry from the relevant national agencies, regional bodies, or open-access repositories. Where possible, use locally validated classification parameters rather than global defaults.

---

## 12. Temporal Comparison Design

- **Accounting period:** Define opening and closing years (e.g., 2017 opening, 2020 closing)
- **Imagery selection:** Select cloud-free composites from the same season in both periods to minimise seasonal variation
- **Classification consistency:** Apply the same classification method, training approach, and class definitions to both periods
- **Change attribution:** Use the ecosystem type change matrix (Section 9.2) to track transitions between specific types
- **Repeat cycles:** Plan for repeat extent assessments at regular intervals (e.g., every 3–5 years) to build a time series
- **Drivers of change:** Note that satellite classification alone cannot distinguish natural from anthropogenic drivers of change — supplementary data (disturbance history, land-use records, environmental pressures) is required for interpretation

---

## 13. Linkages to Other Accounts

The extent account provides the spatial foundation for all other accounts:

| Downstream Account | How Extent Data Is Used |
|---|---|
| Condition account | Each BSU is assigned an ecosystem type from the extent classification; condition indicators are measured and reported per ecosystem type |
| Ecosystem service account | Service flows are attributed to the providing ecosystem type; total service supply scales with ecosystem extent |
| Asset account | Monetary asset values incorporate ecosystem extent (e.g., carbon stock = per-hectare density x extent) |
| Data quality assessment | The extent classification defines which BSUs are available for condition measurement and service attribution |

---

## Appendix A: Step-by-Step Image Classification Instructions

---

### A.1 Sentinel-2 Acquisition and Preprocessing

**Steps:**

1. Access the Copernicus Open Access Hub or a cloud processing platform (e.g., Google Earth Engine, Microsoft Planetary Computer)
2. Search for Sentinel-2 Level-2A (atmospherically corrected) tiles covering the accounting area
3. Filter by date range (within the opening or closing accounting year), cloud cover (<10%), and tidal state (low tide preferred)
4. If multiple tiles are needed to cover the accounting area, ensure overlap and consistent acquisition conditions
5. Download or process in cloud environment
6. Apply additional preprocessing:
   - Sun-glint correction (Hedley et al. 2005 or equivalent)
   - Water column correction (Lyzenga depth-invariant indices or physics-based inversion)
   - Cloud and cloud-shadow masking
   - Composite generation from multiple dates if needed
7. Clip to the accounting area boundary
8. Align to the BSU grid (10 m x 10 m)

---

### A.2 Ground Truth Point Collection

**Equipment:** GPS unit (±5 m accuracy minimum), drop-camera system or snorkel/dive gear, underwater camera, data recording tablet or waterproof data sheets, depth sounder or dive computer.

**Steps:**

1. Pre-plan ground truth locations using a stratified random design overlaid on preliminary satellite imagery, ensuring representation of all expected ecosystem types and depth ranges
2. Navigate to each planned location by boat
3. Record GPS coordinates at the observation point
4. Deploy drop-camera, snorkel, or dive to observe the substrate
5. Record:
   - Dominant substrate class (>50% cover)
   - Secondary substrate class (>20% cover)
   - Depth (metres, corrected for tidal state)
   - Photograph
   - Water clarity (qualitative: clear, moderate, turbid)
   - Notes (any unusual features)
6. Repeat for all planned points
7. Post-survey: enter all records into a georeferenced database; perform QA checks (GPS coordinates within accounting area, valid substrate codes, depth plausibility)

---

### A.3 SAM Classification Workflow

**Software:** GIS or remote sensing package supporting SAM (e.g., ENVI, QGIS with Orfeo Toolbox, or equivalent)

**Steps:**

1. Load the preprocessed Sentinel-2 imagery (surface reflectance, sun-glint corrected, water column corrected)
2. Load the ground truth training dataset
3. Extract spectral signatures (endmembers) for each target class from the training locations:
   - Coral reef, seagrass, mangrove, sand, rubble, rock, macroalgae, deep water, land
   - Average multiple training points per class to produce robust endmember spectra
4. Run the SAM algorithm:
   - For each image pixel, calculate the spectral angle to each endmember
   - Assign the pixel to the class with the minimum spectral angle
   - Apply a maximum angle threshold (e.g., 0.1–0.15 radians) to reject ambiguous pixels
5. Post-classification filtering:
   - Remove isolated single-pixel classifications (salt-and-pepper noise) using a majority filter
   - Enforce the depth mask: pixels deeper than the depth limit are assigned to "deep water"
6. Reclassify to BSU grid: assign each 10 m x 10 m BSU to its classified ecosystem type

---

### A.4 Random Forest Classification Workflow

**Software:** GIS or statistical environment supporting Random Forest (e.g., R with `randomForest` or `ranger`; Python with `scikit-learn`; QGIS with dzetsaka plugin)

**Steps:**

1. Load the preprocessed high-resolution imagery (e.g., Pleiades 0.3 m)
2. Extract spectral values at all ground truth training locations
3. Split the training data: ~70–80% for model training, ~20–30% for independent validation
4. Train the Random Forest classifier:
   - Number of trees: 500 (default starting point; increase if OOB error is unstable)
   - Number of features sampled per split: sqrt(total bands) (default for classification)
   - Minimum node size: 1–5 (balance accuracy vs overfitting)
5. Evaluate out-of-bag (OOB) error and variable importance
6. Apply the trained model to classify every pixel in the image
7. Post-classification:
   - Majority filter to reduce noise
   - Enforce depth mask
   - Aggregate to BSU grid if pixel size differs from BSU resolution
8. Validate against the withheld test set; compute confusion matrix and accuracy metrics

---

### A.5 Change Detection Between Accounting Periods

**Steps:**

1. Ensure both the opening and closing period classified maps use:
   - The same classification method (SAM or Random Forest)
   - The same class definitions and number of classes
   - The same BSU grid alignment
2. Overlay the two classified maps on a per-BSU basis
3. For each BSU, record the transition:
   - Opening class → Closing class
4. Construct the ecosystem type change matrix (Section 9.2)
5. Calculate additions and reductions for each ecosystem type:
   - Additions to type T = sum of all BSUs transitioning from any other type to type T
   - Reductions from type T = sum of all BSUs transitioning from type T to any other type
6. Calculate net change = additions − reductions
7. Verify: opening extent + additions − reductions = closing extent (for each type)
8. Examine the spatial distribution of changes: map areas of gain, loss, and stability for each ecosystem type

---

### A.6 Accuracy Assessment Protocol

**Steps:**

1. From the original ground truth dataset, extract the validation subset (withheld from training)
2. At each validation point, compare the classified ecosystem type against the field-observed type
3. Construct the confusion matrix
4. Calculate:
   - Overall accuracy = (sum of diagonal entries) / (total validation points)
   - Producer's accuracy per class = (correctly classified points for class T) / (total reference points for class T)
   - User's accuracy per class = (correctly classified points for class T) / (total classified points for class T)
   - Kappa coefficient (optional but recommended)
5. Report per-class accuracies alongside overall accuracy
6. Identify systematic errors (e.g., consistent seagrass–sand confusion) and document their potential impact on extent estimates
7. If accuracy is below target (>80% overall), consider:
   - Additional ground truth collection in problematic areas
   - Refining preprocessing (water column correction, composite quality)
   - Testing alternative classification algorithms
   - Multi-temporal compositing to capture seasonal differences

---

## Appendix B: Special Considerations by Ecosystem Type

---

### B.1 Coral Reef Extent

- Coral reefs typically have the highest classification accuracy due to strong spectral contrast with surrounding substrate
- Include both live coral-dominated and structurally complex reef areas (not just live coral cover)
- Reef extent is distinct from condition — a degraded reef with low live coral cover is still a reef ecosystem for extent purposes
- Atoll rim reefs, lagoonal patch reefs, and channel reefs may require separate mapping attention due to varying spectral signatures

### B.2 Seagrass Extent

- Seagrass classification accuracy is often lower than other classes due to:
  - Spectral similarity with sand in shallow water
  - Confusion with macroalgae communities
  - Sparse or patchy seagrass beds falling below minimum mapping thresholds
- Mitigation: multi-temporal composites (seagrass biomass varies seasonally), additional ground truth densification in seagrass–sand transition zones
- Below-ground rhizome networks are not detected by optical remote sensing — extent reflects above-ground canopy presence only

### B.3 Mangrove Extent

- Mangroves are typically well-discriminated from surrounding land and water classes due to strong vegetation signal
- At 10 m BSU resolution, internal heterogeneity (canopy gaps, species zonation, varying canopy density) is not captured
- High-resolution imagery (0.3–3 m) reveals significant within-mangrove variation relevant to condition and carbon stock estimates
- For very small mangrove areas (e.g., 18.7 ha at Hithadhoo), the 10 m BSU grid provides limited spatial detail — consider high-resolution mapping as standard practice

---

*Framework aligned with the UN SEEA EA (2021) international statistical standard. Maldives examples drawn from: Compiling the first Natural Capital Accounts in the Maldives: Methods report (ENDhERI Project). Alternative methods from: Applying SEEA EA at the Project Level in Central Java (RNF BCAF, GOAP, 2025).*
