# Skill: Ecosystem Condition — Biotic Indicators: Seagrass

**Purpose:** Calculate biotic condition indicators for seagrass meadow ecosystems (IUCN GET M1.1) from field survey data, compute the Seagrass Ecosystem Quality Index (SEQI), extrapolate spatially, and normalise to condition indices for the SEEA EA condition account.

**Framework:** UN SEEA EA Ecosystem Condition Accounts
**Ecosystem type:** Seagrass Meadows (M1.1)
**Spatial backbone:** 10 m x 10 m BSU grid

---

## 1. Field Survey Data

| Source | Records | Key Fields |
|---|---|---|
| Benthic survey | Multiple sites from 357 ground truth points | Species ID, shoot density (shoots/m²), canopy height (cm), % cover, AGB (g DW/m²), BGB (g DW/m²) |
| Drop-camera / snorkel | 357 georeferenced points (shared across ecosystems) | Substrate type, benthic cover, depth, GPS coordinates |

### Reference Data

| Type | Source | Use |
|---|---|---|
| Species-specific seagrass reference values | Published literature | Normalisation denominators for SEQI sub-indicators |
| IUCN Global Ecosystem Typology (GET) | IUCN | Ecosystem type classification code M1.1 |

---

## 2. Field Data QA/QC

```
Raw field sheets / tablets
    │
    ├── Validate GPS coordinates against accounting area boundary
    ├── Standardise taxonomic names (species-level for seagrass)
    ├── Unit harmonisation (density as shoots/m², cover as %, biomass as g DW/m²)
    ├── Flag and resolve outliers (e.g., cover summing > 100%)
    ├── Calculate transect-level means from within-transect replicates
    └── Calculate site-level means ± SE from transect replicates
```

---

## 3. Indicator Calculation

| Indicator | Calculation | Unit |
|---|---|---|
| Shoot density | Counts per quadrat, scaled to shoots/m² | shoots/m² |
| Canopy height | Mean height of leaf blades | cm |
| Percentage cover | Visual estimate or point-intercept | % |
| Species richness | Count of species present at site | integer |
| AGB / BGB | Harvest, dry, weigh per m² | g DW/m² |

### Composite — SEQI Calculation

```
For each sub-indicator i at site j:
    normalised_i_j = measured_i_j / reference_i

SEQI_j = mean(normalised_shoot_density_j,
              normalised_canopy_height_j,
              normalised_cover_j,
              normalised_species_richness_j)

Output range: 0.0 to 1.0
```

---

## 4. Spatial Extrapolation

Field-measured condition indicators are spatially sparse (limited seagrass plots). Statistical models bridge field data to full spatial coverage.

```
Training data:
    X = satellite-derived predictors at survey site locations
        ├── Water column-corrected reflectance bands (Sentinel-2: B2, B3, B4, B8)
        ├── Spectral indices (NDVI, band ratios)
        ├── Depth estimates
        └── Biophysical context (SST, DHW, Chl-a, turbidity)

    y = field-measured indicator value at matched locations
        ├── % cover
        ├── Biomass
        └── SEQI composite
```

See [skill_condition_abiotic.md](skill_condition_abiotic.md) §6 for general model types, validation protocol, and prediction workflow.

---

## 5. Normalisation to Condition Index

### Reference Levels

| Indicator | Reference Level | Source |
|---|---|---|
| SEQI sub-indicators | Species-specific published values | Regional seagrass literature |
| SEQI composite | 1.0 | By construction |

### Formula

The SEQI itself is already a normalised composite index (0.0–1.0), where each sub-indicator is divided by its species-specific reference value before averaging:

```
SEQI = mean(CI_shoot_density, CI_canopy_height, CI_cover, CI_species_richness)

where CI_i = measured_i / reference_i    (capped at 1.0)
```

---

## 6. Ecosystem Asset Representation

```
┌─────────────────────────────────────────────────────────────┐
│  ECOSYSTEM ASSET: Seagrass Meadows (M1.1)                  │
│  Total extent: 4,855.5 ha (closing 2020)                   │
│                                                             │
│  ┌───────────────────┬────────┬──────────┬────────────────┐ │
│  │ Condition         │ Ref.   │ Measured │ Condition      │ │
│  │ Indicator         │ Level  │ Value    │ Index (0–1)    │ │
│  ├───────────────────┼────────┼──────────┼────────────────┤ │
│  │ SEQI (composite)  │ 1.0    │ 0.64     │ 0.64           │ │
│  │ Shoot density     │ sp.ref │ measured │ normalised     │ │
│  │ Canopy height     │ sp.ref │ measured │ normalised     │ │
│  │ % cover           │ sp.ref │ measured │ normalised     │ │
│  │ Species richness  │ sp.ref │ measured │ normalised     │ │
│  └───────────────────┴────────┴──────────┴────────────────┘ │
└─────────────────────────────────────────────────────────────┘
```

---

## 7. Output: SEEA EA Condition Account Table (Seagrass)

| Ecosystem Type | Condition Indicator | Reference Level | Measured Value (t) | Condition Index (0–1) | Accounting Period |
|---|---|---|---|---|---|
| Seagrass (M1.1) | SEQI composite | 1.0 | 0.64 | 0.64 | 2022–2023 |

---

## 8. Data Quality and Limitations

| Issue | Impact | Mitigation |
|---|---|---|
| Seagrass spectral confusion with sand/algae | Lower classification accuracy for seagrass BSUs | Ground truth densification; multi-temporal composites |
| Species-specific reference values from literature | May not reflect achievable local reference condition | Sensitivity analysis on reference level choice; update with local data |

---

## 9. Implementation Checklist

- [ ] **Ingest** seagrass field data and validate GPS, taxonomy, units
- [ ] **Calculate** per-site seagrass indicator values (shoot density, canopy height, cover, species richness)
- [ ] **Compute** SEQI composite index at each site
- [ ] **Train** GLM / Random Forest models: seagrass indicators ~ satellite predictors
- [ ] **Validate** models via cross-validation; report accuracy metrics
- [ ] **Predict** seagrass indicator values at every seagrass BSU
- [ ] **Normalise** predicted values against species-specific reference levels
- [ ] **Aggregate** BSU-level indices to seagrass asset level (area-weighted mean)
- [ ] **Compile** seagrass rows in SEEA EA condition account table
- [ ] **Map** BSU-level seagrass condition indices for spatial visualisation

---

## 10. Tiered Assessment

### Role in Service Account Tiers

Seagrass condition indicators (SEQI composite, shoot density, canopy height, % cover, species richness, AGB/BGB) feed into service accounts for carbon sequestration (via biomass stocks and NCP rates adjusted for condition), fisheries nursery (via habitat quality), and seagrass gleaning (via harvest yield modulated by meadow health). The quality of these condition measurements constrains the achievable B: Accuracy tier for those downstream service accounts: a service account cannot exceed the accuracy ceiling of its condition inputs.

### Sub-procedure Tier Assessment

| Sub-procedure | Tier 1 | Tier 2 | Tier 3 | Current tier (A / B / C) |
|---|---|---|---|---|
| Field survey design | Rapid visual assessment at <5 sites with no biomass measurements | Replicated benthic transects at multiple sites including shoot density and cover (this skill's approach from 357 ground truth points) | Permanent monitoring transects at 20+ sites with seasonal repeats, full AGB/BGB destructive sampling | A=1–2 / B=1–2 / C=1–2 |
| SEQI calculation | Cover-only index | Composite SEQI integrating shoot density, canopy height, cover, species richness using species-specific literature reference values (this skill) | SEQI validated against independent health assessments and correlated with ecosystem function measurements (e.g., productivity, carbon stock) | A=1 / B=2 / C=1 |
| Reference level setting for SEQI sub-indicators | Global published species averages (this skill) | Regional published values from same species assemblage | Locally measured reference from pristine seagrass meadow or historical baseline | A=1 / B=1 / C=1 |
| Spatial extrapolation | Limited ground truth; point values only | GLM/Random Forest models trained on satellite predictors at survey sites (this skill) | Validated model with independent test set; cross-validation CV <20%; high-resolution drone survey for priority patches | A=1–2 / B=1–2 / C=1–2 |
| Biomass measurement (AGB/BGB) | Literature default biomass per unit cover | Limited destructive sampling at representative sites | Replicated destructive sampling stratified by cover class and species, with local allometric equations | A=1–2 / B=1–2 / C=1–2 |

### Implications for Service Accounts

The SEQI composite sits at Tier 2 on method maturity — it applies a published, peer-reviewed composite index adapted to regional species — but at Tier 1 on reference level accuracy, because the sub-indicator denominators are sourced from global literature rather than locally or regionally measured reference conditions. Service accounts that use condition-adjusted service rates (carbon sequestration, fisheries nursery, seagrass gleaning) therefore inherit a Tier 1–2 accuracy ceiling on B: Accuracy, regardless of the quality of the service-side modelling. The spectral confusion issue identified in §8 (seagrass misclassified as sand or algae in satellite imagery) is an additional B-accuracy constraint that acts on the spatial extrapolation step, introducing uncertainty in BSU-level condition predictions. Because both the reference level limitation and spectral confusion affect the same downstream services, priority investment should target both jointly: establishing local reference levels and improving ground truth density would move the binding sub-procedures from Tier 1 toward Tier 2 on B: Accuracy.

### Progression Pathway

To reach Tier 2 on B-accuracy: establish 5–10 permanent monitoring plots for repeat SEQI surveys, conduct limited destructive biomass sampling at a subset of sites to replace global literature AGB/BGB defaults, and validate the satellite extrapolation model with an independent field dataset withheld from model training.

To reach Tier 3 on B-accuracy: deploy 20+ permanent plots with seasonal resurveys, develop locally calibrated SEQI reference levels by measuring healthy reference meadows within the accounting area, validate AGB/BGB estimates against local allometric equations, and correlate SEQI scores with independent ecosystem function measurements (e.g., primary productivity, sediment carbon stock).

---

*Derived from: ENDhERI Project — Compiling the first Natural Capital Accounts in the Maldives. Aligned with UN SEEA EA (2021) and GOAP technical guidance.*
