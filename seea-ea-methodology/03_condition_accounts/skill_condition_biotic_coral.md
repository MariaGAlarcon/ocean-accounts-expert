# Skill: Ecosystem Condition — Biotic Indicators: Coral Reef

**Purpose:** Calculate biotic condition indicators for photic coral reef ecosystems (IUCN GET M1.3) from field survey data, extrapolate spatially via satellite predictors, and normalise to condition indices for the SEEA EA condition account.

**Framework:** UN SEEA EA Ecosystem Condition Accounts
**Ecosystem type:** Photic Coral Reefs (M1.3)
**Spatial backbone:** 10 m x 10 m BSU grid

---

## 1. Field Survey Data

| Source | Records | Key Fields |
|---|---|---|
| Underwater Visual Census (UVC) | 17 sites, 4 transects/site (20 m x 20 m) at 5–10 m depth | % live coral by genus, % soft coral, % dead coral, % algae (macro, turf, CCA), bleaching %, fish counts, invertebrates |
| Drop-camera / snorkel | 357 georeferenced points (shared across ecosystems) | Substrate type, benthic cover, depth, GPS coordinates |

### Reference Data

| Type | Source | Use |
|---|---|---|
| Healthy Indo-Pacific reef benchmarks | Published literature | Reference level for coral cover (~40%) |
| IUCN Global Ecosystem Typology (GET) | IUCN | Ecosystem type classification code M1.3 |

---

## 2. Field Data QA/QC

```
Raw field sheets / tablets
    │
    ├── Validate GPS coordinates against accounting area boundary
    ├── Standardise taxonomic names (genus-level for coral)
    ├── Unit harmonisation (all cover as %)
    ├── Flag and resolve outliers (e.g., cover summing > 100%)
    ├── Calculate transect-level means from within-transect replicates
    └── Calculate site-level means ± SE from transect replicates
```

---

## 3. Indicator Calculation

| Indicator | Calculation | Unit | Direction |
|---|---|---|---|
| Live hard coral cover | Mean % cover across transects at site | % | Higher = better |
| Coral bleaching prevalence | % colonies showing bleaching signs | % | Higher = worse (invert) |
| Fish abundance / biomass | Count and estimated biomass from visual census | biomass kg/ha or count | Higher = better |
| Dead coral cover | Mean % recently dead coral | % | Higher = worse (invert) |
| Algal cover (turf + macroalgae) | Mean % combined algal cover | % | Higher = worse (invert) |
| CCA cover | Mean % crustose coralline algae | % | Higher = better (reef consolidation) |

### Site-Level Aggregation

```
site_coral_cover = mean(transect_coral_cover[1..4])
site_bleaching   = mean(transect_bleaching[1..4])
```

---

## 4. Spatial Extrapolation

Field-measured condition indicators are spatially sparse (17 coral sites). Statistical models bridge field data to full spatial coverage.

```
Training data:
    X = satellite-derived predictors at survey site locations
        ├── Water column-corrected reflectance bands (Sentinel-2: B2, B3, B4, B8)
        ├── Spectral indices (NDVI, band ratios)
        ├── Depth estimates
        └── Biophysical context (SST, DHW, Chl-a, turbidity)

    y = field-measured indicator value at matched locations
        └── % live coral cover
```

See [skill_condition_abiotic.md](skill_condition_abiotic.md) §6 for general model types, validation protocol, and prediction workflow.

---

## 5. Normalisation to Condition Index

### Reference Levels

| Indicator | Reference Level | Source |
|---|---|---|
| Live hard coral cover | ~40% | Healthy Indo-Pacific reef literature |
| Bleaching prevalence | 0% | No-bleaching baseline |

### Formulae

**Standard (higher = better):**
```
                    Measured Value
Condition Index = ─────────────────
                   Reference Level

Example: CI_coral = 19.67% / 40% = 0.49
```

**Inverted (higher = worse):**
```
                         Measured Value
Condition Index = 1  −  ─────────────────
                         Reference Level

Example: CI_bleaching = 1 − (10.97% / 100%) = 0.89
```

---

## 6. Ecosystem Asset Representation

```
┌─────────────────────────────────────────────────────────────┐
│  ECOSYSTEM ASSET: Photic Coral Reefs (M1.3)                │
│  Total extent: 7,395.3 ha (closing 2020)                   │
│  BSU count: ~739,530 cells                                  │
│                                                             │
│  ┌───────────────────┬────────┬──────────┬────────────────┐ │
│  │ Condition         │ Ref.   │ Measured │ Condition      │ │
│  │ Indicator         │ Level  │ Value    │ Index (0–1)    │ │
│  ├───────────────────┼────────┼──────────┼────────────────┤ │
│  │ Live coral cover  │ 40%    │ 19.67%   │ 0.49           │ │
│  │ Bleaching prev.   │ 0%     │ 10.97%   │ 0.89 (inv.)   │ │
│  │ Fish biomass      │ TBD    │ TBD      │ TBD            │ │
│  │ Algal cover       │ low    │ TBD      │ TBD            │ │
│  └───────────────────┴────────┴──────────┴────────────────┘ │
│                                                             │
│  Spatial distribution:                                      │
│  BSU-level condition map showing within-asset heterogeneity │
└─────────────────────────────────────────────────────────────┘
```

---

## 7. Output: SEEA EA Condition Account Table (Coral Reef)

| Ecosystem Type | Condition Indicator | Reference Level | Measured Value (t) | Condition Index (0–1) | Accounting Period |
|---|---|---|---|---|---|
| Coral reef (M1.3) | Live hard coral cover | ~40% | 19.67% | 0.49 | 2023 |
| Coral reef (M1.3) | Bleaching prevalence | 0% | 10.97% | 0.89 (inverted) | 2023 |

---

## 8. Data Quality and Limitations

| Issue | Impact | Mitigation |
|---|---|---|
| Limited spatial sampling (17 coral sites) | Extrapolation uncertainty across 7,395 ha | Report prediction intervals; increase survey density in future |
| Deep reef beyond survey range | Condition unknown for deeper BSUs | Extrapolation model predicts if spectral signal exists; otherwise exclude |
| Seagrass spectral confusion with sand/algae at reef margins | Lower classification accuracy for boundary BSUs | Ground truth densification; multi-temporal composites |

---

## 9. Implementation Checklist

- [ ] **Ingest** UVC field data and validate GPS, taxonomy, units
- [ ] **Calculate** per-site coral indicator values from transect data
- [ ] **Train** GLM / Random Forest models: coral cover ~ satellite predictors
- [ ] **Validate** models via cross-validation; report accuracy metrics
- [ ] **Predict** coral indicator values at every coral reef BSU
- [ ] **Normalise** predicted values against reference levels (40% coral cover, 0% bleaching)
- [ ] **Aggregate** BSU-level indices to coral reef asset level (area-weighted mean)
- [ ] **Compile** coral reef rows in SEEA EA condition account table
- [ ] **Map** BSU-level coral condition indices for spatial visualisation

---

## 10. Tiered Assessment

### Role in Service Account Tiers

Coral reef condition indicators (live hard coral cover, bleaching prevalence, fish biomass, algal cover) feed into ecosystem service accounts — particularly coral reef recreation (via reef quality/attractiveness), fisheries nursery (via coral structural complexity), and wild fish provisioning (via fish biomass). Their measurement quality constrains the achievable B: Accuracy tier for those service accounts. The binding constraint principle (tiered assessment framework Section 5.2) applies: if coral condition data are Tier 1 on accuracy, service accounts that use condition-stratified supply estimates cannot claim Tier 2 or above on B: Accuracy.

### Sub-procedure Tier Assessment

| Sub-procedure | Tier 1 | Tier 2 | Tier 3 | Current tier (A / B / C) |
|---|---|---|---|---|
| Field survey design (UVC) | Rapid visual survey without replicated transects (<5 sites) | Replicated transects at 10–20 sites (this skill — 17 sites, 4 transects/site) | Permanent monitoring stations with >30 sites, diver-tow, or stereo-video BRUVs | 2 / 2 / 2 |
| Spatial extrapolation (satellite models) | No extrapolation; point values reported for sampled sites only | GLM/Random Forest trained on satellite predictors at 17 sites (this skill) | Validated model with >50 training sites and independent test set with CV <20% | 1–2 / 1–2 / 2 |
| Reference level setting | Global average (40% coral cover from literature, this skill's current approach) | Regional published benchmarks from same biogeographic region | Locally established historical reference from long-term monitoring or paleoecological records | 1 / 1 / 1 |
| Temporal monitoring | Single snapshot (this skill) | Biennial surveys at fixed sites | Annual permanent monitoring stations | 1 / 1 / 1 |

### Implications for Service Accounts

The current coral condition assessment is Tier 2 on A (moderate field campaign) but Tier 1–2 on B (accuracy limited by 17 survey sites extrapolated across 7,395 ha, and literature-based reference levels). Service accounts relying on stratified condition data (e.g., reef recreation value adjusted for reef quality) can at most claim Tier 2 on accuracy given these inputs. The reference level sub-procedure (B=1) is the binding constraint on accuracy: a global 40% coral cover benchmark does not account for local species composition, historical range, or atoll-specific ecology. Expansion to permanent transects at more sites and validation of reference levels against local pristine-area benchmarks would be the priority investments for upgrading service account accuracy.

### Progression Pathway

To reach Tier 2 on B-accuracy: establish permanent monitoring stations (30+ sites), calibrate satellite extrapolation model against 50+ ground truth points, conduct independent cross-validation, derive reference coral cover from regional monitoring programmes (e.g., GCRMN Indo-Pacific).

To reach Tier 3 on B-accuracy: validate fish biomass estimates against independent stereo-BRUV surveys, establish locally calibrated reference levels from historical coral cover records or paleoecological data, implement annual permanent transect resurveys, and correlate condition indices with ecosystem function measurements.

---

*Derived from: ENDhERI Project — Compiling the first Natural Capital Accounts in the Maldives. Aligned with UN SEEA EA (2021) and GOAP technical guidance.*
