# Skill: Ecosystem Extent Data Pipeline

**Purpose:** Convert raw satellite imagery and field ground truth observations into spatially explicit ecosystem type classifications at the BSU level, producing SEEA EA extent account tables with opening extent, additions, reductions, and closing extent.

**Framework:** UN SEEA EA Ecosystem Extent Accounts
**Spatial backbone:** 10 m x 10 m BSU grid (or MBSU grid — see §2.3)

---

## 1. Pipeline Overview

```
┌─────────────────────────────────────────────────────────────────────────┐
│                        DATA INGESTION LAYER                            │
│                                                                        │
│  Satellite Imagery          Ground Truth Data         Reference Data   │
│  ┌──────────────┐           ┌───────────────┐         ┌─────────────┐  │
│  │ Sentinel-2   │           │ Drop-camera   │         │ IUCN GET    │  │
│  │ (10m, L2A)   │           │ Snorkel/diver │         │ ecosystem   │  │
│  │              │           │ Intertidal    │         │ typology    │  │
│  │ Pleiades     │           │ walk          │         │             │  │
│  │ Planet/SPOT  │           │               │         │ Bathymetry  │  │
│  │ (0.3–5m)    │           │ 357+ georef.  │         │ Coastline   │  │
│  └──────┬───────┘           │ points        │         │ shapefiles  │  │
│         │                   └──────┬────────┘         └──────┬──────┘  │
│         │                          │                         │         │
└─────────┼──────────────────────────┼─────────────────────────┼─────────┘
          │                          │                         │
          ▼                          ▼                         ▼
┌─────────────────────────────────────────────────────────────────────────┐
│                      PREPROCESSING LAYER                               │
│                                                                        │
│  Satellite imagery:                Ground truth:                       │
│  • Atmospheric correction (L2A)    • Validate GPS coordinates          │
│  • Sun-glint removal               • Standardise substrate codes       │
│  • Water column correction         • QA/QC depth and cover records     │
│  • Cloud masking + compositing     • Split: ~70–80% train / 20–30%    │
│  • Co-registration to BSU grid       validation                        │
│  • Depth mask application                                              │
│                                                                        │
└──────────────────────────────┬──────────────────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────────────────┐
│                    CLASSIFICATION LAYER                                 │
│                                                                        │
│  Two parallel approaches (use one or both):                            │
│  ┌──────────────────────────┐  ┌──────────────────────────┐            │
│  │ SAM (Sentinel-2, 10m)   │  │ Random Forest (HR, 0.3–5m)│           │
│  │ • Extract endmembers    │  │ • Train on ground truth    │           │
│  │ • Spectral angle per    │  │ • Ensemble of decision     │           │
│  │   pixel vs endmember    │  │   trees (500+)             │           │
│  │ • Assign to min-angle   │  │ • Majority vote per pixel  │           │
│  │   class                 │  │ • Variable importance      │           │
│  │ • Max-angle threshold   │  │ • OOB error estimate       │           │
│  └──────────────────────────┘  └──────────────────────────┘            │
│                                                                        │
│  Post-classification: majority filter, depth mask, BSU assignment      │
│                                                                        │
│  Output classes: Coral reef (M1.3) | Seagrass (M1.1) | Mangrove       │
│  (MFT1.2) | Sand | Rubble | Rock | Macroalgae | Deep water | Land     │
│                                                                        │
└──────────────────────────────┬──────────────────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────────────────┐
│                    ACCURACY ASSESSMENT LAYER                           │
│                                                                        │
│  • Validate against withheld ground truth (20–30%)                     │
│  • Confusion matrix: classified vs reference per class                 │
│  • Overall accuracy (target >80%), producer's and user's accuracy      │
│  • Kappa coefficient                                                   │
│  • Identify and document systematic misclassification patterns         │
│                                                                        │
└──────────────────────────────┬──────────────────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────────────────┐
│                    CHANGE DETECTION LAYER                              │
│                                                                        │
│  Compare opening (t1) and closing (t2) classified maps:                │
│  • Per-BSU transition: opening class → closing class                   │
│  • Ecosystem type change matrix (cross-tabulation)                     │
│  • Additions = BSUs gained by ecosystem type T                         │
│  • Reductions = BSUs lost by ecosystem type T                          │
│  • Net change = additions − reductions                                 │
│  • Spatial change maps (gain, loss, stable areas)                      │
│                                                                        │
└──────────────────────────────┬──────────────────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────────────────┐
│                 OUTPUT: SEEA EA EXTENT ACCOUNT TABLE                   │
│                                                                        │
│  Per ecosystem type: Opening extent → Additions → Reductions →         │
│  Net change → Closing extent (ha)                                      │
│  + Ecosystem type change matrix                                        │
│  + BSU-level classified maps (opening and closing)                     │
│  + Accuracy assessment report                                          │
│                                                                        │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## 2. Data Ingestion

### 2.1 Satellite Imagery

| Dataset | Resolution | Purpose | Processing Level |
|---|---|---|---|
| Sentinel-2 | 10 m (multispectral, 13 bands) | Atoll-wide or region-wide classification | L2A (atmospherically corrected) |
| Pleiades | 0.3 m (4 bands + pan) | Priority site detailed mapping | Ortho-rectified |
| Planet SuperDove | 3 m (8 bands) | Supplementary classification | Surface reflectance |
| SPOT 6/7 | 1.5–5 m (4 bands + pan) | Supplementary classification | Surface reflectance |
| Landsat 8/9 | 30 m (11 bands) | Historical change detection / broad scale | L2 (surface reflectance) |

**Temporal requirements:** Acquire imagery for both the opening period (e.g., 2017) and closing period (e.g., 2020), selecting cloud-free composites from the same season.

### 2.2 Ground Truth Data

| Source | Records | Key Fields |
|---|---|---|
| Drop-camera survey | Rapid assessment across the accounting area | Substrate type, benthic cover class, depth, GPS coordinates, photograph |
| Snorkel transect | Shallow reef and seagrass verification | Cover class, species presence, habitat boundary, GPS |
| Diver observation | Deeper reef slopes and complex habitats | Detailed benthic composition, depth, GPS |
| Intertidal walk | Mangrove and intertidal habitats | Species composition, boundary delineation, GPS |

**Example (Laamu Atoll, Maldives):** 357 georeferenced ground truth points were collected across the accounting area, covering all ecosystem types and depth ranges.

### 2.3 Reference Data

| Type | Source | Use |
|---|---|---|
| IUCN Global Ecosystem Typology (GET) | IUCN | Classification codes for ecosystem types (M1.1, M1.3, MFT1.2) |
| Bathymetry | National hydrographic office; satellite-derived | Depth mask for classification; depth limit enforcement |
| Accounting area boundary | National/regional mapping agency; project GIS; Badan Pusat Statistik (BPS) for Indonesian administrative units | Spatial extent of the accounts |
| Coastline shapefiles | National mapping agency | Landward boundary for marine accounts |
| MBSU grid specification | Rahayu et al. (2024) | Alternative spatial unit for Indonesian coastal systems — majority rule (>51%) classification per cell |

---

## 3. Preprocessing

### 3.1 Satellite Imagery Preprocessing

```
Raw satellite imagery
    │
    ├── Atmospheric correction
    │       └── Sentinel-2: L2A via Sen2Cor or equivalent
    │       └── Commercial: FLAASH, ATCOR, 6S, or provider-supplied
    │
    ├── Sun-glint removal
    │       └── Hedley et al. (2005) or Kay et al. (2009)
    │       └── Critical for tropical waters (high sun, low wind)
    │
    ├── Water column correction
    │       └── Lyzenga (1978/1981) depth-invariant indices
    │       └── Or physics-based radiative transfer inversion
    │       └── Essential for discriminating benthic habitats at varying depths
    │
    ├── Cloud masking and compositing
    │       └── Apply cloud + cloud-shadow masks
    │       └── Generate best-pixel composite from multiple dates
    │       └── Ensure temporal consistency within accounting year
    │
    ├── Depth mask application
    │       └── Mask pixels deeper than depth limit (e.g., 25 m)
    │       └── Assign masked pixels to "deep water" class
    │
    └── Co-registration to BSU grid
            └── Align to 10 m x 10 m grid
            └── Resample if pixel size differs (majority for thematic; bilinear for reflectance)
            └── Verify geometric accuracy against reference points
```

### 3.2 Ground Truth QA/QC

```
Raw ground truth records
    │
    ├── Validate GPS coordinates against accounting area boundary
    ├── Verify depth plausibility (within 0–25 m range for marine)
    ├── Standardise substrate classification codes across all survey methods
    ├── Flag and resolve inconsistencies (conflicting codes, duplicate points)
    ├── Attach photograph reference for QA verification
    ├── Correct for tidal state (adjust depth if needed)
    └── Split into training (~70–80%) and validation (~20–30%) subsets
            └── Stratified split: maintain proportional representation of all classes
```

---

## 4. Classification

### 4.1 SAM Classification (Sentinel-2)

| Step | Operation | Parameters |
|---|---|---|
| 1 | Extract endmembers from training points | Average spectra per class from training locations |
| 2 | Calculate spectral angle per pixel | Angle between pixel vector and each endmember vector |
| 3 | Assign pixel to minimum-angle class | Smallest spectral angle = most similar class |
| 4 | Apply maximum angle threshold | 0.1–0.15 radians (reject ambiguous pixels) |
| 5 | Post-classification majority filter | 3x3 or 5x5 window to remove salt-and-pepper noise |
| 6 | Enforce depth mask | Pixels beyond depth limit → "deep water" |
| 7 | Assign to BSU grid | Each 10 m x 10 m BSU gets its classified type |

**Output:** Classified raster map at BSU resolution for one accounting period.

### 4.2 Random Forest Classification (High-Resolution Imagery)

| Step | Operation | Parameters |
|---|---|---|
| 1 | Extract spectral values at training points | All available bands at each ground truth location |
| 2 | Train Random Forest model | 500 trees; features per split = sqrt(total bands); min node = 1–5 |
| 3 | Evaluate OOB error | Out-of-bag error estimate from training |
| 4 | Extract variable importance | Rank spectral bands by contribution to classification accuracy |
| 5 | Classify every pixel | Majority vote across all trees |
| 6 | Post-classification filtering | Majority filter + depth mask |
| 7 | Aggregate to BSU grid | Majority class within each 10 m x 10 m cell |

**Output:** Classified raster map at BSU resolution for one accounting period (higher spatial detail at priority sites).

### 4.3 Supervised Classification (Alternative to SAM/Random Forest)

**When to use:** Where in-situ ground truth observations from field campaigns provide well-defined training samples, particularly in terrestrial-coastal contexts (e.g., mangrove-dominated coastlines) where water column corrections are less critical than in marine environments.

| Step | Operation | Parameters |
|---|---|---|
| 1 | Extract spectral values at ground truth training locations | All available bands from preprocessed imagery (e.g., SPOT 6/7 at 5 m, Sentinel-2 at 10 m) |
| 2 | Train supervised classifier (e.g., Maximum Likelihood, SVM) | Training samples from field campaigns; class separability analysis |
| 3 | Classify every pixel | Assign to class with highest probability or minimum distance |
| 4 | GIS-based refinement | Filter isolated pixels; enhance spatial coherence |
| 5 | Validate against field data and expert interpretation | Confusion matrix with overall, producer's, and user's accuracy |
| 6 | Assign to BSU/MBSU grid | Dominant class within each grid cell |

**Output:** Classified raster map at BSU/MBSU resolution for one accounting period.

> **RNF BCAF example (Central Java):** Supervised classification was applied to SPOT 6/7 (5 m) and Sentinel-2 (10 m) imagery using ground truth from field campaigns. Classification distinguished mangrove habitats from mudflats, aquaculture ponds, and terrestrial vegetation. GIS refinement filtered isolated pixels. This approach was chosen over SAM because the terrestrial-coastal context did not require the illumination-insensitivity advantages of SAM that are critical in shallow marine environments. (Source: GOAP, 2025)

---

### 4.4 Classification Categories

| Class | IUCN GET Code | Extent Account Inclusion |
|---|---|---|
| Coral reef | M1.3 | Yes — ecosystem extent |
| Seagrass | M1.1 | Yes — ecosystem extent |
| Mangrove | MFT1.2 | Yes — ecosystem extent |
| Sand | — | Context (non-ecosystem) |
| Rubble | — | Context (non-ecosystem) |
| Rock | — | Context (non-ecosystem) |
| Macroalgae | — | Context (may be ecosystem-relevant) |
| Deep water | — | Context (beyond classification depth limit) |
| Land | — | Context (terrestrial) |

---

## 5. Accuracy Assessment

### 5.1 Validation Protocol

```
Withheld validation ground truth points (20–30% of total)
    │
    ├── At each validation point: compare classified type vs field-observed type
    │
    ├── Construct confusion matrix:
    │       ├── Rows = classified classes
    │       └── Columns = reference (field-observed) classes
    │
    ├── Calculate metrics:
    │       ├── Overall accuracy = correct / total (target >80%)
    │       ├── Producer's accuracy per class = correct / total reference for class
    │       ├── User's accuracy per class = correct / total classified as class
    │       └── Kappa coefficient (target >0.6)
    │
    └── Document systematic errors:
            ├── Seagrass ↔ sand confusion (shallow water spectral similarity)
            ├── Coral ↔ rubble confusion (dead coral spectral overlap)
            ├── Mangrove boundary uncertainty (mixed pixels, tidal variation)
            └── Deep water edge effects (attenuated benthic signal)
```

### 5.2 Example Accuracy Results (Laamu Atoll, Maldives)

| Class | Producer's Accuracy | User's Accuracy | Notes |
|---|---|---|---|
| Coral reef | Highest | Highest | Strong spectral contrast with surrounding substrate |
| Mangrove | High | High | Strong vegetation signal |
| Seagrass | Moderate | Moderate | Spectral confusion with sand and algae in shallow water |
| Sand | High | Moderate | Misclassified sparse seagrass sometimes included |

Overall accuracy: >80% for Sentinel-2 atoll-wide classification.

### 5.3 Remediation if Accuracy is Below Target

| Action | When to Apply |
|---|---|
| Collect additional ground truth in problematic areas | Persistent seagrass–sand or coral–rubble confusion |
| Refine water column correction | Depth-related misclassification patterns |
| Multi-temporal compositing | Seasonal or tidal variation causing inconsistent classification |
| Test alternative classifier | SAM underperforming → try Random Forest or SVM |
| Add textural features | Where spectral bands alone are insufficient (e.g., OBIA) |

---

## 6. Change Detection

### 6.1 Per-BSU Transition Analysis

```
For each BSU in the accounting area:
    │
    ├── Extract opening period class (t1)
    ├── Extract closing period class (t2)
    │
    ├── If t1 == t2 → Stable (no change)
    ├── If t1 ≠ t2  → Transition recorded:
    │       ├── If t2 is ecosystem type T and t1 is not → Addition to T
    │       └── If t1 is ecosystem type T and t2 is not → Reduction from T
    │
    └── Store: BSU_ID, opening_class, closing_class, transition_type
```

### 6.2 Ecosystem Type Change Matrix

```
                          Closing Period (t2)
                   Coral    Seagrass   Mangrove   Sand    Rubble   Other
Opening (t1):
  Coral          [stable]  [C→SG]     [C→M]      [C→S]   [C→R]   [C→O]
  Seagrass       [SG→C]   [stable]    [SG→M]     [SG→S]  [SG→R]  [SG→O]
  Mangrove       [M→C]    [M→SG]     [stable]    [M→S]   [M→R]   [M→O]
  Sand           [S→C]    [S→SG]      [S→M]      [stable] [S→R]  [S→O]
  Rubble         [R→C]    [R→SG]      [R→M]      [R→S]   [stable] [R→O]
  Other          [O→C]    [O→SG]      [O→M]      [O→S]   [O→R]   [stable]

Row totals = opening extent per type
Column totals = closing extent per type
Diagonal = stable (unchanged) BSUs
Off-diagonal = transitions
```

### 6.3 Extent Change Calculations

```
For ecosystem type T:

Additions_T = Σ (BSUs transitioning from any other type to T)

Reductions_T = Σ (BSUs transitioning from T to any other type)

Net_change_T = Additions_T − Reductions_T

Closing_extent_T = Opening_extent_T + Net_change_T

Verification: Opening_extent_T + Additions_T − Reductions_T = Closing_extent_T
```

### 6.4 Spatial Change Mapping

```
For each ecosystem type T, produce three spatial layers:
    │
    ├── Gain map: BSUs where T was absent at t1 but present at t2
    ├── Loss map: BSUs where T was present at t1 but absent at t2
    └── Stable map: BSUs where T was present at both t1 and t2
```

---

## 7. Output: SEEA EA Extent Account Table

The final output is an extent account table in the standard SEEA EA format:

| Ecosystem Type | Opening Extent (ha) | Additions (ha) | Reductions (ha) | Net Change (ha) | Closing Extent (ha) | Accounting Period |
|---|---|---|---|---|---|---|
| Coral reef (M1.3) | 7,437.2 | 121.3 | -163.2 | -41.9 | 7,395.3 | 2017–2020 |
| Seagrass (M1.1) | 4,892.6 | 86.4 | -123.5 | -37.1 | 4,855.5 | 2017–2020 |
| Mangrove (MFT1.2) | 18.7 | 0.0 | 0.0 | 0.0 | 18.7 | 2017–2020 |
| Other (sand, rubble, deep) | 149,599.2 | — | — | — | 149,678.2 | 2017–2020 |
| **Total accounting area** | **161,947.7** | — | — | — | **161,947.7** | — |

**Supplementary outputs:**

```
┌─────────────────────────────────────────────────────────────┐
│  ECOSYSTEM EXTENT ACCOUNT: Laamu Atoll, Maldives            │
│  Accounting period: 2017 (opening) – 2020 (closing)         │
│  Total accounting area: 161,947.7 ha (884.63 km²)           │
│  BSU count: ~16,194,770 cells (10m x 10m)                   │
│                                                              │
│  ┌─────────────┬──────────┬──────────┬──────────┬─────────┐ │
│  │ Ecosystem   │ Opening  │ Net      │ Closing  │ Change  │ │
│  │ Type        │ (ha)     │ Change   │ (ha)     │ (%)     │ │
│  ├─────────────┼──────────┼──────────┼──────────┼─────────┤ │
│  │ Coral reef  │ 7,437.2  │ -41.9    │ 7,395.3  │ -0.56%  │ │
│  │ Seagrass    │ 4,892.6  │ -37.1    │ 4,855.5  │ -0.76%  │ │
│  │ Mangrove    │ 18.7     │ 0.0      │ 18.7     │ 0.00%   │ │
│  └─────────────┴──────────┴──────────┴──────────┴─────────┘ │
│                                                              │
│  Change interpretation:                                      │
│  • Coral loss predominantly to rubble/sand (reef degradation)│
│  • Seagrass loss to sand (physical disturbance / stress)     │
│  • Both consistent with 2016 mass bleaching residual effects │
│  • Mangrove stable at Hithadhoo (18.7 ha)                    │
│                                                              │
│  Classification: Sentinel-2 SAM, overall accuracy >80%      │
│                                                              │
│  Spatial outputs:                                            │
│  • BSU-level classified maps (opening + closing)             │
│  • Ecosystem type change matrix                              │
│  • Gain/loss/stable spatial layers per ecosystem type        │
└─────────────────────────────────────────────────────────────┘
```

---

## 8. Downstream Integration

The classified BSU grid and extent account feed directly into all other accounts:

```
EXTENT ACCOUNT OUTPUTS
    │
    ├──► Condition Account
    │       Each BSU has an assigned ecosystem type from the extent classification
    │       Condition indicators are measured and reported per ecosystem type
    │       Condition models are trained within ecosystem type strata
    │
    ├──► Ecosystem Service Account
    │       Service flows are attributed to the providing ecosystem type
    │       Physical supply scales with ecosystem extent
    │       E.g., Carbon sequestration (Mg CO₂/yr) = NCP rate × extent (ha)
    │
    ├──► Asset Account
    │       Carbon stock = per-hectare density × ecosystem extent
    │       Asset value (NPV) depends on extent as a multiplier
    │
    └──► Data Quality Assessment
            Extent classification accuracy directly affects confidence
            in all downstream accounts
```

---

## 9. Data Quality and Limitations

| Issue | Impact | Mitigation |
|---|---|---|
| Seagrass–sand spectral confusion | Lower classification accuracy for seagrass BSUs; potential overestimate of sand or underestimate of seagrass | Ground truth densification in transition zones; multi-temporal composites; water column correction refinement |
| Mixed pixels at ecosystem boundaries | Misclassification of edge BSUs; uncertain boundary position | High-resolution imagery for priority boundaries; sub-pixel classification methods |
| Temporal mismatch (imagery vs ground truth) | Ground truth may not reflect conditions at image acquisition date | Minimise time gap; document any mismatch; prefer near-simultaneous collection |
| Cloud cover gaps | Incomplete spatial coverage in composites | Multi-date compositing; alternative imagery sources |
| Depth limit uncertainty | Benthic signal attenuates with depth; deep ecosystems may be missed | Enforce conservative depth mask; supplement with acoustic survey data |
| 10 m BSU resolution vs fine-scale heterogeneity | Mangrove canopy gaps, species zonation, small seagrass patches not resolved | High-resolution imagery for small or heterogeneous ecosystems |
| Classification method consistency across periods | Different methods or training data between periods introduce artefactual change | Apply identical methods, class definitions, and training approach to both periods |
| Cannot distinguish natural vs anthropogenic drivers | Change matrix shows what changed, not why | Supplement with disturbance history, land-use data, environmental pressure records. Note: RNF BCAF (GOAP, 2025) explicitly acknowledged this limitation for mangrove transitions in Central Java — a practice recommended for all extent accounts |

---

## 10. Implementation Checklist

- [ ] **Define** accounting area boundary and depth/elevation limits
- [ ] **Acquire** Sentinel-2 imagery for opening and closing periods (L2A, <10% cloud)
- [ ] **Acquire** high-resolution imagery for priority sites (if available)
- [ ] **Collect** georeferenced ground truth points across all ecosystem types and depths
- [ ] **Preprocess** satellite imagery (atmospheric correction, sun-glint, water column, cloud mask, composite)
- [ ] **QA/QC** ground truth data (GPS, depth, substrate codes, photographs)
- [ ] **Split** ground truth into training (~70–80%) and validation (~20–30%) subsets
- [ ] **Train** SAM classifier on Sentinel-2 using training endmembers
- [ ] **Train** Random Forest classifier on high-resolution imagery (if applicable)
- [ ] **Classify** both opening and closing period imagery
- [ ] **Post-process** classifications (majority filter, depth mask, BSU assignment)
- [ ] **Validate** against withheld ground truth; compute confusion matrix and accuracy metrics
- [ ] **Construct** ecosystem type change matrix (opening vs closing)
- [ ] **Calculate** additions, reductions, and net change per ecosystem type
- [ ] **Compile** SEEA EA extent account table
- [ ] **Produce** BSU-level classified maps (opening + closing) and spatial change maps
- [ ] **Document** metadata: imagery dates, classification method, accuracy, ground truth count, limitations

---

## 11. Tiered Assessment

### Role in Service Account Tiers

Ecosystem extent is the spatial foundation for all service accounts: physical supply is expressed as a rate per unit area multiplied by the extent of the providing ecosystem. Extent classification accuracy therefore propagates into the B: Accuracy score of every downstream service account. Since extent error multiplies through to service supply estimates (supply = rate × extent), a 5% overestimate in extent produces a 5% overestimate in all services that rely on it. The tiered assessment framework (Section 6.1, "Most cost-effective investments") identifies national ecosystem extent mapping as one of the highest-return investments, noting that it benefits all services simultaneously.

### Sub-procedure Tier Assessment

| Sub-procedure | Tier 1 | Tier 2 | Tier 3 | Current tier (A / B / C) |
|---|---|---|---|---|
| Satellite imagery basis | Global ecosystem maps (e.g., Global Mangrove Watch, UNEP WCMC coral maps) without local refinement | National or site-specific classification of Sentinel-2 (10 m) with ground truth validation (this skill — SAM/RF on Sentinel-2) | High-resolution imagery (Pleiades ≤1 m) with rigorous accuracy assessment and area-adjusted extent estimates | A=1–2 / B=2 / C=1–2 |
| Ground truth data | <50 points or borrowed from other projects | 200–500 georeferenced points stratified by ecosystem type and depth (this skill — 357 points) | >1,000 stratified points with replicated visits to assess temporal stability | A=2 / B=2 / C=2 |
| Classification method | Visual interpretation or global map overlay | Supervised classification (SAM, Random Forest) with accuracy assessment >80% OA (this skill) | Object-based image analysis (OBIA) or physics-based inversion, with area-adjusted accuracy estimates | A=2 / B=2 / C=2 |
| Accuracy assessment | None or OA only | Confusion matrix with producer's and user's accuracy per class and Kappa (this skill) | Design-based area-adjusted accuracy estimates with uncertainty bounds per class (Olofsson et al. 2014) | A=2 / B=2 / C=2 |
| Change detection temporal consistency | Two-date comparison without method consistency check | Same methods and class definitions applied to both periods (this skill) | Post-classification comparison with error-adjusted area estimates and attribution of drivers | A=2 / B=2 / C=2 |

### Overall Extent Tier Assessment

The current implementation — Sentinel-2 SAM/RF classification, 357 ground truth points, confusion matrix accuracy assessment >80% OA, same methods applied to both periods — corresponds to **Tier 2 across all three dimensions**. This is the appropriate target for most national ecosystem accounting programmes in the medium term and is consistent with the tiered assessment framework's Tier 2 recommendations.

### Implications for Downstream Service Accounts

Tier 2 accuracy (>80% OA) introduces per-class extent uncertainty that should be propagated into service account uncertainty ranges when service supply is expressed as rate × extent. Service account B: Accuracy claims should not exceed Tier 2 on the spatial accuracy component unless area-adjusted extent estimates with confidence intervals are provided. This ceiling applies equally to carbon sequestration, coastal protection, fisheries nursery, and all other services that use ecosystem extent as a direct multiplier. The area adjustment step — which corrects classification map areas using confusion matrix proportions — can be implemented within a Tier 2 resource envelope and significantly improves the reliability of extent estimates without requiring additional field surveys.

### Progression Pathway

To reach Tier 3 on B-accuracy: apply design-based area adjustment following Olofsson et al. (2014), collect >1,000 stratified validation points with replicated revisits, report per-class area estimates with 95% confidence intervals, and use high-resolution imagery (Pleiades or Planet) for boundary refinement at priority sites. The transition from confusion-matrix OA to area-adjusted estimates is the single most impactful step for improving service account accuracy without additional field campaigns.

---

*Derived from: ENDhERI Project — Compiling the first Natural Capital Accounts in the Maldives. Alternative methods from: Applying SEEA EA at the Project Level in Central Java (RNF BCAF, GOAP, 2025). Aligned with UN SEEA EA (2021) and IUCN Global Ecosystem Typology.*
