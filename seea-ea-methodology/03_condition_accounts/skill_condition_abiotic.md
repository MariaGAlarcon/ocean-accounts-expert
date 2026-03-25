# Skill: Ecosystem Condition — Abiotic Indicators & General Pipeline

**Purpose:** Convert remote sensing inputs and environmental data into spatially explicit abiotic condition values per Basic Spatial Unit (BSU), providing the environmental backbone for ecosystem condition accounts under the SEEA EA framework.

**Framework:** UN SEEA EA Ecosystem Condition Accounts
**Spatial backbone:** 10 m x 10 m BSU grid

---

## 1. Pipeline Overview

```
┌─────────────────────────────────────────────────────────────────────────┐
│                        DATA INGESTION LAYER                            │
│                                                                        │
│  Remote Sensing Data                              Reference Data       │
│  ┌───────────────┐  ┌───────────────┐            ┌─────────────┐      │
│  │ Sentinel-2    │  │ SST archives  │            │ Literature  │      │
│  │ Pleiades/SPOT │  │ Chl-a, Turb.  │            │ benchmarks  │      │
│  │ Planet        │  │ Ocean colour  │            │ IUCN GET    │      │
│  └──────┬────────┘  └──────┬────────┘            └──────┬──────┘      │
│         │                  │                            │             │
└─────────┼──────────────────┼────────────────────────────┼─────────────┘
          │                  │                            │
          ▼                  ▼                            ▼
┌─────────────────────────────────────────────────────────────────────────┐
│                      PREPROCESSING LAYER                               │
│                                                                        │
│  • Atmospheric correction (L2A)      • SST → Degree Heating Weeks     │
│  • Sun-glint removal                 • Chl-a composite generation     │
│  • Water column correction           • Turbidity mapping              │
│  • Spectral index derivation         • Co-registration to BSU grid    │
│  • Cloud masking & compositing                                        │
│                                                                        │
└──────────────────────────────┬──────────────────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────────────────┐
│              ABIOTIC INDICATOR CALCULATION LAYER                       │
│                                                                        │
│  Per-BSU abiotic condition values:                                     │
│  ┌──────────────────┐  ┌──────────────────┐  ┌──────────────────┐     │
│  │ Thermal stress   │  │ Water quality    │  │ Water clarity    │     │
│  │ SST anomaly      │  │ Chlorophyll-a    │  │ Turbidity        │     │
│  │ DHW              │  │ Nutrient proxy   │  │ Sediment load    │     │
│  └──────────────────┘  └──────────────────┘  └──────────────────┘     │
│                                                                        │
└──────────────────────────────┬──────────────────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────────────────┐
│              NORMALISATION & CONDITION INDEX LAYER                      │
│                                                                        │
│  Condition Index = f(Measured Value, Reference Level)                   │
│  • Standard:  CI = Measured / Reference       (higher = better)        │
│  • Inverted:  CI = 1 − (Measured / Reference) (higher = worse)         │
│  • Output range: 0.0 (degraded) to 1.0 (reference condition)          │
│                                                                        │
└──────────────────────────────┬──────────────────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────────────────┐
│            SPATIAL AGGREGATION & ASSET REPRESENTATION                   │
│                                                                        │
│  BSU-level (10m) → Site-level → Ecosystem type → Accounting area       │
│  • Area-weighted mean condition per ecosystem asset                     │
│  • Condition account table in SEEA EA format (Table 5.13)              │
│  • Temporal comparison: opening vs. closing accounting period           │
│                                                                        │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## 2. Remote Sensing Data Ingestion

| Dataset | Resolution | Purpose | Processing Level |
|---|---|---|---|
| Sentinel-2 | 10 m | Atoll-wide benthic classification + spectral predictors for condition | L2A (atmospherically corrected) |
| Pleiades | 0.3 m | High-resolution mapping (priority sites) | Ortho-rectified |
| Planet SuperDove | 3 m | Supplementary classification | Surface reflectance |
| SPOT 6/7 | 1.5 m | Supplementary classification | Surface reflectance |
| SST satellite archives | ~1 km | Thermal stress context | Derived product |
| Ocean colour (Chl-a) | ~300 m–1 km | Water quality / nutrient proxy | Derived product |
| Turbidity | ~300 m–1 km | Sediment loading / clarity | Derived product |

### Reference Data

| Type | Source | Use |
|---|---|---|
| IUCN Global Ecosystem Typology (GET) | IUCN | Ecosystem type classification codes (M1.1, M1.3, MFT1.2) |

---

## 3. Preprocessing

### 3.1 Remote Sensing Preprocessing

```
Raw satellite imagery
    │
    ├── Atmospheric correction → Surface reflectance (Sentinel-2 L2A via Sen2Cor or similar)
    ├── Sun-glint removal → Correct specular reflection from water surface
    ├── Water column correction → Retrieve depth-invariant bottom reflectance
    │       └── Lyzenga (1978/1981) or physics-based inversion
    ├── Spectral index derivation
    │       ├── NDVI, EVI (vegetation indices)
    │       ├── Band ratios (blue/green, green/red for benthic discrimination)
    │       └── Custom water column-corrected indices
    ├── Cloud masking and composite generation (best cloud-free pixel)
    └── Co-registration to BSU grid (10m x 10m)
```

### 3.2 SST and Biophysical Indicators

```
SST time series → Degree Heating Weeks (DHW)
    │
    ├── Climatological mean SST baseline (e.g., 1985-2012 MMM)
    ├── HotSpot = SST − MMM (when SST > MMM)
    ├── DHW = cumulative HotSpots over rolling 12-week window
    └── Assign DHW value to each BSU by spatial interpolation / nearest grid
```

---

## 4. Abiotic Indicator Calculation

| Indicator | Calculation | Unit | Direction |
|---|---|---|---|
| SST anomaly | SST − climatological mean | °C | Higher = worse (invert) |
| Degree Heating Weeks (DHW) | Cumulative thermal stress over 12-week window | °C-weeks | Higher = worse (invert) |
| Chlorophyll-a concentration | Ocean colour satellite product | mg/m³ | Context: oligotrophic = healthy reef/seagrass |
| Turbidity | Satellite-derived suspended sediment proxy | NTU or FNU | Higher = worse (invert) |

### Reference Levels

| Indicator | Reference Level | Source |
|---|---|---|
| SST anomaly (DHW) | 0 DHW | No thermal stress baseline |
| Chlorophyll-a | Low (oligotrophic) | Regional literature |

---

## 5. Normalisation Framework

### 5.1 Standard Formula

```
                    Measured Value
Condition Index = ─────────────────
                   Reference Level
```

- Capped at 1.0 (values exceeding reference are truncated to 1.0)
- Minimum 0.0

### 5.2 Inverted Indicators

For indicators where higher values indicate worse condition (e.g., DHW, turbidity):

```
                         Measured Value
Condition Index = 1  −  ─────────────────
                         Reference Level
```

---

## 6. Spatial Extrapolation — General Methodology

### 6.1 Model Training

Statistical models bridge spatially sparse field data to full spatial coverage using satellite-derived predictors.

```
Training data:
    X = satellite-derived predictors at survey site locations
        ├── Water column-corrected reflectance bands (Sentinel-2: B2, B3, B4, B8)
        ├── Spectral indices (NDVI, band ratios)
        ├── Depth estimates
        └── Biophysical context (SST, DHW, Chl-a, turbidity)

    y = field-measured indicator value at matched locations
```

### 6.2 Model Types

| Model | Strengths | Application |
|---|---|---|
| Generalised Linear Model (GLM) | Interpretable, handles bounded responses (beta regression for %), explicit uncertainty | Primary model where sample sizes are small |
| Random Forest regression | Captures nonlinear relationships, handles multi-collinearity, variable importance ranking | Where enough training data exist; provides ensemble predictions |

### 6.3 Validation Protocol

```
k-fold cross-validation (k = 5 or leave-one-site-out)
    │
    ├── Split training data into k folds
    ├── Train on k-1 folds, predict on held-out fold
    ├── Repeat k times
    ├── Report: RMSE, R², MAE, bias
    └── Independent test set validation (if available)
```

### 6.4 Prediction

```
For every BSU classified as ecosystem type T:
    │
    ├── Extract satellite predictor values at BSU centroid
    ├── Apply trained model → predicted indicator value
    ├── Attach prediction uncertainty (CI or prediction interval)
    └── Store: BSU_ID, ecosystem_type, indicator_name, predicted_value, uncertainty
```

---

## 7. Spatial Aggregation Framework

### 7.1 Aggregation Hierarchy

```
Level 1: BSU (10m x 10m)
    │   Each BSU holds:
    │     • ecosystem_type (from extent classification)
    │     • predicted condition indicator values (from extrapolation models)
    │     • condition index per indicator (from normalisation)
    │
    ▼
Level 2: Survey Site / Local Area
    │   Area-weighted mean of BSU-level condition indices
    │   within site catchment or local neighbourhood
    │
    ▼
Level 3: Ecosystem Type (asset-level)
    │   Area-weighted mean across all BSUs of that type
    │   within the accounting area
    │   = the headline condition index per indicator per ecosystem
    │
    ▼
Level 4: Accounting Area (Laamu Atoll)
        Summary condition across all ecosystem types
        (reported per-type, not typically averaged across types)
```

### 7.2 Area-Weighted Aggregation Formula

```
For ecosystem type T with N BSUs, each of area A_i (constant 100 m^2 for 10m grid):

                   Σ (CI_i × A_i)
CI_T (indicator) = ─────────────────
                      Σ A_i

Since all BSUs are equal area (100 m^2):

                   Σ CI_i
CI_T (indicator) = ───────
                     N
```

### 7.3 Handling Spatial Data Gaps

| Situation | Approach |
|---|---|
| BSU has no satellite predictor data (cloud, shadow) | Exclude from aggregation; flag as data gap |
| BSU at ecosystem type boundary (mixed pixel) | Assign to dominant type per classification; condition reflects dominant type |

---

## 8. Temporal Dimension

### 8.1 Multi-Period Comparison

```
Opening period (t1)                    Closing period (t2)
┌──────────────────┐                   ┌──────────────────┐
│ Extent: 2017     │                   │ Extent: 2020     │
│ Condition: 2022  │    ──────────►    │ Condition: 2023  │
└──────────────────┘                   └──────────────────┘
        │                                       │
        └──── Change = CI(t2) − CI(t1) ─────────┘
```

### 8.2 Temporal Aggregation Rules

- Condition values are point-in-time snapshots from field campaigns
- Where repeat surveys exist at the same site, report both periods and compute change
- Remote sensing biophysical indicators (SST, DHW) provide continuous temporal context
- Interpretation must reference disturbance history (e.g., 2016 bleaching event)

---

## 9. Output: SEEA EA Condition Account Table (Abiotic)

| Ecosystem Type | Condition Indicator | Reference Level | Measured Value (t) | Condition Index (0–1) | Accounting Period |
|---|---|---|---|---|---|
| All | SST anomaly (DHW) | 0 DHW | Measured | Context indicator | Continuous |
| All | Chlorophyll-a | Low (oligotrophic) | Measured | Context indicator | Continuous |

---

## 10. Data Quality and Limitations

| Issue | Impact | Mitigation |
|---|---|---|
| Temporal mismatch (extent 2017–2020 vs condition 2022–2023) | Condition assessed on potentially changed extent | Acknowledge in metadata; aim for synchronised campaigns |
| 10 m BSU resolution vs fine-scale heterogeneity | Sub-pixel variability not resolved | Use high-res imagery for priority sites; report sub-BSU variability |
| Reference levels from literature, not local pristine sites | May not reflect achievable local reference condition | Sensitivity analysis on reference level choice; update with local data |

---

## 11. Tiered Assessment

### Role in Service Account Tiers

Abiotic condition indicators — sea surface temperature (SST) and degree heating weeks (DHW), chlorophyll-a, and turbidity — function as contextual environmental drivers and quality-adjustment inputs for ecosystem service accounts rather than as service estimates in their own right. Their measurement quality feeds directly into the B: Accuracy dimension of any downstream service account that stratifies supply by abiotic condition class. This skill does not itself produce ecosystem service estimates, but it determines whether service account sub-procedures can achieve Tier 2 or Tier 3 on accuracy: a service account that conditions its supply estimates on abiotic indicators inherits the accuracy ceiling of those indicators. The binding constraint principle from Section 5.2 of the tiered assessment framework applies here — the weakest sub-procedure in the full measurement chain determines the overall tier for accuracy purposes.

### Sub-procedure Tier Assessment

| Sub-procedure | Tier 1 approach | Tier 2 approach | Tier 3 approach | Current implementation tier (A / B / C) |
|---|---|---|---|---|
| SST / DHW data ingestion and processing | Global 1-km SST products applied without local calibration | Same global products validated against in-situ temperature logger data, with documented comparison of satellite and logger-derived DHW values (this skill's approach) | In-situ continuous temperature logger array deployed across ecosystem types, providing direct high-frequency thermal stress measurements | A=1 / B=2 / C=1 |
| Chlorophyll-a / turbidity | Global ocean colour products applied at native resolution without local validation | Regional ocean colour products matched to in-situ water quality measurements; documented satellite-to-in-situ comparison (this skill's approach) | In-situ continuous water quality sensors across sites, with satellite products used only for spatial extrapolation | A=1 / B=1–2 / C=1 |
| Normalisation and reference level setting | Global literature reference values applied without local calibration (this skill's approach) | Regional or national calibrated reference values from monitoring data synthesis | Locally established reference conditions from pristine sites or historical baselines, with documented sampling design | A=1 / B=1 / C=1 |
| Spatial extrapolation to BSU grid | Uniform value applied across all BSUs; no spatial variation | Nearest-grid assignment of SST/Chl-a product pixel to each BSU centroid, preserving gradients at source product resolution (this skill's approach) | Site-specific model linking satellite spectral predictors to in-situ measurements, with k-fold cross-validation and spatially explicit prediction uncertainty | A=1–2 / B=1–2 / C=1–2 |

### Implications for Downstream Service Accounts

Because abiotic indicators in this skill are largely Tier 1 to Tier 2 on accuracy — relying on global satellite products and global or generic literature reference levels — they introduce a ceiling on the B: Accuracy score achievable for any service account that depends on condition-stratified service estimates. Service accounts that stratify supply by abiotic condition class (e.g., carbon sequestration modulated by thermal stress, coastal protection modulated by turbidity) should not claim Tier 3 accuracy if the underlying abiotic condition data are Tier 1. The reference level and normalisation sub-procedure — currently at B=1 due to reliance on global literature values — is the most immediate constraint on accuracy for services that use condition-stratified supply estimates.

### Progression Pathway

| Target | Investment required |
|---|---|
| Tier 2 for SST / DHW | Deploy in-situ temperature loggers at representative sites; conduct one-season comparison of logger-derived and satellite-derived DHW; document bias and correction factor |
| Tier 2 for Chl-a / turbidity | Conduct dry-season and wet-season water quality sampling campaigns matched to satellite overpass dates; document satellite-to-in-situ agreement |
| Tier 2 for reference level setting | Compile regional monitoring data to derive biogeographically appropriate reference thresholds; replace global literature defaults with regionally calibrated values |
| Tier 3 for SST / DHW | Permanent logger array (4–6 loggers across ecosystem types and exposure gradients); annual download and QC; use logger data as primary DHW source with satellite gap-fill |
| Tier 3 for Chl-a / turbidity | Continuous water quality sensors at 2+ representative sites; formal calibration model linking sensors to satellite retrievals; BSU-level predictions with documented uncertainty |
| Tier 3 for reference level setting | Local reference baselines from pristine sites within the accounting area, supplemented by paleoecological or historical data; documented statistical derivation |

---

*Derived from: ENDhERI Project — Compiling the first Natural Capital Accounts in the Maldives. Aligned with UN SEEA EA (2021) and GOAP technical guidance.*
