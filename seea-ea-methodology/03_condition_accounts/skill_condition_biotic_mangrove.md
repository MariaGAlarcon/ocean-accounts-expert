# Skill: Ecosystem Condition — Biotic Indicators: Mangrove

**Purpose:** Calculate biotic condition indicators for mangrove ecosystems (IUCN GET MFT1.2) from field survey data, normalise to condition indices, and compile for the SEEA EA condition account. Spatial extrapolation is constrained by single-site data availability.

**Framework:** UN SEEA EA Ecosystem Condition Accounts
**Ecosystem type:** Mangroves (MFT1.2)
**Spatial backbone:** 10 m x 10 m BSU grid

---

## 1. Field Survey Data

| Source | Records | Key Fields |
|---|---|---|
| Quadrat survey | 10 m x 10 m plots along transects at Hithadhoo | Species ID, tree height (m), DBH (cm, stems >= 2.5 cm), stem density (stems/ha), canopy cover (%), seedling count |
| Drop-camera / snorkel | 357 georeferenced points (shared across ecosystems) | Substrate type, benthic cover, depth, GPS coordinates |

### Reference Data

| Type | Source | Use |
|---|---|---|
| Mature Indo-Pacific mangrove stand metrics | Published literature | Reference levels for height, DBH, density |
| IUCN Global Ecosystem Typology (GET) | IUCN | Ecosystem type classification code MFT1.2 |

---

## 2. Field Data QA/QC

```
Raw field sheets / tablets
    │
    ├── Validate GPS coordinates against accounting area boundary
    ├── Standardise taxonomic names (species-level for mangrove)
    ├── Unit harmonisation (height in m, DBH in cm, density as stems/ha, cover as %)
    ├── Flag and resolve outliers
    ├── Calculate plot-level means from within-plot measurements
    └── Calculate site-level means ± SE from plot replicates
```

---

## 3. Indicator Calculation

| Indicator | Calculation | Unit |
|---|---|---|
| Tree height | Clinometer measurement per stem; or direct measurement for trees <3 m | m |
| DBH | Diameter tape for stems >= 2.5 cm (at 1.3 m height) | cm |
| Stem density | Count all stems / plot area | stems/ha |
| Canopy cover | Spherical densiometer readings, mean per plot (default); or hemispherical photography with ImageJ (alternative) | % |
| Seedling density | Count seedlings + saplings / plot area | count/ha |
| Basal area | π × (DBH/2)² per stem, summed per plot | cm²/ha |

### Plot-Level Aggregation

```
plot_mean_height  = mean(tree_heights in 10m x 10m quadrat)
plot_stem_density = (stem_count / 100 m²) × 10,000  → stems/ha
plot_canopy       = mean(densiometer readings at 4 cardinal points)
                    OR mean(ImageJ canopy cover % from hemispherical photographs)
plot_basal_area   = Σ(π × (DBH_i/2)²) / plot_area × 10,000  → cm²/ha
```

### Alternative Survey Design: Nested Sub-Plots (Quarter-Plot Approach)

**When to use:** Where different mangrove growth stages require separate measurement protocols, or where dense thickets prevent standard 10 × 10 m quadrat sampling.

The quarter-plot approach splits a fixed 10 × 10 m replicate plot into three nested sections:

| Section | Dimensions | Target |
|---|---|---|
| Full quadrat | 10 × 10 m | Adult mangrove trees |
| Inner sub-plot | 5 × 5 m | Saplings (<1.5 m height) |
| Micro-plot | 1 × 1 m | Seedlings |

> **RNF BCAF example (Central Java):** 15 plots across four districts were sampled using this nested design between 2023–2025. Field limitations were explicitly documented — most fixed locations could not be surveyed as full 10 × 10 m squares because mangrove thickets were too dense, and tidal windows sometimes submerged corners, requiring enumerators to sample adjacent areas. (Source: GOAP, 2025)

### Alternative Canopy Cover Method: Hemispherical Photography

**When to use:** Where precise, repeatable canopy cover estimates are required, or where densiometer readings are considered too subjective.

| Step | Operation |
|---|---|
| 1 | Mount camera with hemispherical (fisheye) lens at 1.3 m height at plot centre |
| 2 | Capture upward-facing photograph of canopy |
| 3 | Process image in ImageJ software using binarisation threshold (sky vs canopy) |
| 4 | Calculate canopy cover (%) = canopy pixels / total pixels × 100 |

> **RNF BCAF example:** Hemispherical camera + ImageJ was used instead of densiometers for canopy assessment across Central Java mangrove plots. (Source: GOAP, 2025)

### Composite Condition Metric: Mangrove Health Index (MHI)

**When to use:** As a standardised composite metric integrating multiple structural parameters into a single health score, particularly where comparison with Indonesian national mangrove benchmarks is required.

The MHI (Indrazora et al., 2024) integrates three structural parameters:

```
MHI components:
    1. Canopy cover percentage
    2. Average DBH
    3. Sapling density per plot

Each parameter is scored and combined → overall MHI percentage
    → Excellent: MHI > [threshold]
    → Moderate:  MHI in [range]
    → Poor:      MHI < [threshold]
```

This contrasts with the normalised 0–1 condition index (measured/reference) used in the ENDhERI approach. The MHI is an Indonesia-specific standardised metric that stratifies plots into health categories rather than producing a continuous index.

### Supplementary Biodiversity Indices

**When to use:** Where formal species diversity metrics are required to supplement structural condition indicators.

| Index | Formula | Interpretation |
|---|---|---|
| Shannon-Wiener (H') | H' = −Σ(p_i × ln(p_i)) | Higher = more diverse; 0 = single species |
| Pielou's Evenness (J') | J' = H' / ln(S) | Ratio 0–1; 1 = perfectly even distribution |
| Simpson's Dominance (D') | D' = Σ(p_i²) | Higher = more dominated by few species |

Where p_i = proportion of individuals of species i; S = total number of species.

> **RNF BCAF example (Central Java):** Cilacap showed highest diversity (H' = 0.67, 10 species including *Rhizophora mucronata*, *Bruguiera gymnorrhiza*, *Sonneratia alba*), while Jepara scored 0, indicating single-species dominance. *Avicennia marina* was consistently present in three districts. Species identification was conducted by trained botanists using morphological characteristics. (Source: GOAP, 2025)

---

## 4. Spatial Extrapolation

Mangrove condition data are limited to a single site (Hithadhoo). This severely constrains spatial extrapolation.

```
Training data:
    X = satellite-derived predictors at survey site locations
        ├── Water column-corrected reflectance bands (Sentinel-2: B2, B3, B4, B8)
        ├── Spectral indices (NDVI, band ratios)
        └── Canopy structure proxies

    y = field-measured indicator value at matched locations
        └── Canopy cover (limited by single-site data)
```

**Single-site constraint:** Plot-level condition values are applied uniformly across all mangrove BSUs. This is flagged as limited spatial representativeness.

See [skill_condition_abiotic.md](skill_condition_abiotic.md) §6 for general model types, validation protocol, and prediction workflow.

---

## 5. Normalisation to Condition Index

Two alternative approaches:

### Approach A: Normalised 0–1 Index (ENDhERI / SEEA EA default)

#### Reference Levels

| Indicator | Reference Level | Source |
|---|---|---|
| Tree height | Mature *R. mucronata* stands (regional) | Indo-Pacific mangrove literature |
| Stem density | Mature stand density benchmarks | Indo-Pacific mangrove literature |
| Canopy cover | Closed-canopy mature forest | Indo-Pacific mangrove literature |

#### Formula

**Standard (higher = better):**
```
                    Measured Value
Condition Index = ─────────────────
                   Reference Level
```

### Approach B: Mangrove Health Index (MHI) (RNF BCAF alternative)

Integrates canopy cover %, average DBH, and sapling density into a scored composite yielding an overall MHI percentage, stratifying plots into excellent / moderate / poor categories (Indrazora et al., 2024). Use where Indonesian national benchmarks or categorical health assessments are preferred over continuous 0–1 indices.

---

## 6. Ecosystem Asset Representation

```
┌─────────────────────────────────────────────────────────────┐
│  ECOSYSTEM ASSET: Mangroves (MFT1.2)                       │
│  Total extent: 18.7 ha (stable)                            │
│                                                             │
│  ┌───────────────────┬────────┬──────────┬────────────────┐ │
│  │ Condition         │ Ref.   │ Measured │ Condition      │ │
│  │ Indicator         │ Level  │ Value    │ Index (0–1)    │ │
│  ├───────────────────┼────────┼──────────┼────────────────┤ │
│  │ Tree height       │ mature │ 3.7 m    │ variable       │ │
│  │ DBH               │ mature │ small    │ variable       │ │
│  │ Stem density      │ mature │ 3.5-4.5k │ variable       │ │
│  │ Canopy cover      │ closed │ 60-90%   │ variable       │ │
│  │ Regeneration      │ active │ active   │ variable       │ │
│  └───────────────────┴────────┴──────────┴────────────────┘ │
└─────────────────────────────────────────────────────────────┘
```

---

## 7. Output: SEEA EA Condition Account Table (Mangrove)

| Ecosystem Type | Condition Indicator | Reference Level | Measured Value (t) | Condition Index (0–1) | Accounting Period |
|---|---|---|---|---|---|
| Mangrove (MFT1.2) | Tree height | Mature stand ref. | 3.7 m | Variable | 2022–2023 |
| Mangrove (MFT1.2) | Stem density | Mature stand ref. | 3,500–4,500/ha | Variable | 2022–2023 |

---

## 8. Data Quality and Limitations

| Issue | Impact | Mitigation |
|---|---|---|
| Single survey site only (Hithadhoo) | Condition values applied uniformly to all 18.7 ha of mangrove; no spatial differentiation | Flag limited spatial representativeness; prioritise additional survey sites |
| 10 m BSU resolution vs fine-scale heterogeneity | Mangrove canopy gaps and species zonation not resolved | Use high-res imagery (Pleiades 0.3 m) for sub-BSU variability |

---

## 9. Implementation Checklist

- [ ] **Ingest** mangrove field data and validate GPS, taxonomy, units
- [ ] **Calculate** per-plot mangrove indicator values (height, DBH, stem density, canopy cover, seedlings)
- [ ] **Apply** plot-level condition values uniformly across mangrove BSUs (single-site constraint)
- [ ] **Normalise** values against mature stand reference levels
- [ ] **Aggregate** BSU-level indices to mangrove asset level (area-weighted mean)
- [ ] **Compile** mangrove rows in SEEA EA condition account table
- [ ] **Map** BSU-level mangrove condition indices for spatial visualisation
- [ ] **Flag** limited spatial representativeness in metadata

---

## 10. Tiered Assessment

### Role in Service Account Tiers

Mangrove structural condition indicators (tree height, DBH, stem density, canopy cover, seedling density) feed into service accounts for carbon sequestration (via biomass-to-stock allometry), coastal protection (via forest width and density), and mangrove recreation (via habitat attractiveness). Their measurement quality constrains achievable B: Accuracy for those services. The single-survey-site constraint documented in this skill (§4, §8) is particularly significant: it means any service account that uses mangrove condition as an input is effectively Tier 1 on B: Accuracy for the condition component, regardless of how sophisticated the service model itself is.

### Sub-procedure Tier Assessment

| Sub-procedure | Tier 1 | Tier 2 | Tier 3 | Current tier (A / B / C) |
|---|---|---|---|---|
| Field survey coverage | Single site used uniformly for all mangrove BSUs (this skill — Hithadhoo only) | 3–5 sites stratified by mangrove condition class or location | Systematic stratified sampling across all distinct mangrove patches with statistical power analysis | A=1, B=1, C=1 |
| Structural indicator measurement (height, DBH, density) | 10×10 m plots, basic instruments, limited replication at single site (this skill) | Multiple plots per site with nested sub-plots (e.g., RNF BCAF quarter-plot design) | Plot network with dendrometer bands, canopy height lidar, AGB validation against allometric samples | A=1–2, B=1–2, C=1–2 |
| Canopy cover measurement | Visual estimation or densiometer | Hemispherical photography processed in ImageJ (RNF BCAF alternative in this skill) | Drone-derived canopy height model and canopy cover from point cloud | A=1–2, B=1–2, C=1–2 |
| Reference level setting | Published Indo-Pacific mature stand benchmarks (this skill) | Regional calibrated benchmarks from the same species composition | Locally established reference from undisturbed or restored stand monitoring | A=1, B=1, C=1 |
| Spatial extrapolation | Uniform single-site value across all mangrove BSUs (this skill's constraint) | Satellite-based NDVI stratification with multi-site calibration | Full spatial model validated at multiple sites | A=1, B=1, C=1 |

### Implications for Service Accounts

The single-survey-site constraint is the binding limitation for all downstream service accounts that use mangrove condition as an input. Carbon sequestration estimates conditioned on canopy structure, and coastal protection estimates conditioned on forest density, both inherit a Tier 1 accuracy ceiling from this skill as currently implemented. Priority investment: additional survey sites across all distinct mangrove patches to enable Tier 2 spatial stratification. Without multiple sites, no improvement in the service-side modelling can raise the overall service account above Tier 1 on B: Accuracy.

### Alternative Method: MHI vs SEEA EA Approach

The Mangrove Health Index (MHI, Indrazora et al. 2024) described in this skill produces categorical health assessments (excellent/moderate/poor) rather than continuous 0–1 condition indices. In terms of the tiered assessment framework: MHI is Tier 1–2 on A (moderate cost, standard instruments) and Tier 1–2 on B (validated for Indonesian contexts but not locally calibrated). It is an acceptable alternative where national benchmarks are preferred, but its categorical output is less compatible with SEEA EA's continuous condition index requirement and cannot directly substitute for the normalised 0–1 index used in service account stratification.

### Progression Pathway

To reach Tier 2: survey 3–5 sites across all distinct mangrove patches, use hemispherical photography for canopy cover, derive NDVI-based spatial stratification from satellite imagery, replace uniform single-site values with class-based condition layers.

To reach Tier 3: establish a permanent plot network across all mangrove patches, validate allometric equations locally, use drone lidar for canopy structure, calibrate reference levels against undisturbed reference plots within the accounting area.

---

*Derived from: ENDhERI Project — Compiling the first Natural Capital Accounts in the Maldives. Alternative methods from: Applying SEEA EA at the Project Level in Central Java (RNF BCAF, GOAP, 2025). Aligned with UN SEEA EA (2021) and GOAP technical guidance.*
