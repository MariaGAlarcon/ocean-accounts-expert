# Skill: Ecosystem Condition — Opening & Closing Condition Accounts (SEEA EA Format)

**Purpose:** Compile raw and normalized biotic condition indicator values into standardized SEEA EA ecosystem condition account tables, presenting opening (year 1) and closing (year 2) condition states with calculated change metrics.

**Framework:** UN SEEA EA Ecosystem Condition Accounts
**Ecosystem type:** Photic Coral Reefs (M1.3); applies to other ecosystem types
**Spatial scope:** Site-level indicators aggregated to accounting-area means (or per-BSU if spatially explicit)
**Companion skills:**
- [skill_condition_biotic_fish_invert.md](skill_condition_biotic_fish_invert.md) — indicator calculation from field surveys
- [skill_condition_biotic_coral.md](skill_condition_biotic_coral.md) — coral cover and bleaching indicators
- [skill_extent_change_matrix_seea_account.md](skill_extent_change_matrix_seea_account.md) — extent accounts (asset definition context)

---

## 1. Overview

This skill transforms per-site (or per-BSU) raw condition indicators into the canonical SEEA EA condition account structure: opening condition, closing condition, and change metrics, normalized to a 0–1 condition index scale. The result is a publication-ready condition account table linking ecosystem asset characterisation across an accounting period (Year 1 → Year 2).

```
Calculated Condition Indicators (per site, per year)
    ├── Raw Values Table (measured units: kg/ha, individuals/ha, species count, etc.)
    ├── Reference Levels (normalisation thresholds)
    ├── Condition Index Derivation (0–1 normalisation)
    ├── Opening/Closing Table Compilation (Year 1 vs Year 2)
    ├── Change Metrics Calculation (absolute, %, direction)
    └── Outputs: SEEA EA condition account tables, data quality summary
```

---

## 2. Input Specifications

### 2.1 Indicator Data by Source

| Indicator | Format | Key Fields | Time Points | Source |
|---|---|---|---|---|
| Fish biomass | CSV (site × FG × year) | site_id, functional_group, year, biomass_mean_kgha, biomass_se | Opening year, Closing year | [skill_condition_biotic_fish_invert.md](skill_condition_biotic_fish_invert.md) §3 |
| Fish abundance | CSV (site × FG × year) | site_id, functional_group, year, abundance_mean_indha, abundance_se | Opening year, Closing year | [skill_condition_biotic_fish_invert.md](skill_condition_biotic_fish_invert.md) §3 |
| Fish species richness | CSV (site × year) | site_id, year, richness_count | Opening year, Closing year | [skill_condition_biotic_fish_invert.md](skill_condition_biotic_fish_invert.md) §3 |
| COTS density | CSV (site × year) | site_id, year, cots_density_perha, cots_density_se | Opening year, Closing year | [skill_condition_biotic_fish_invert.md](skill_condition_biotic_fish_invert.md) §3 |
| Sea urchin density | CSV (site × year) | site_id, year, urchin_density_perm2 | Opening year, Closing year | [skill_condition_biotic_fish_invert.md](skill_condition_biotic_fish_invert.md) §3 |
| Giant clam abundance | CSV (site × year) | site_id, year, clam_count_mean | Opening year, Closing year | [skill_condition_biotic_fish_invert.md](skill_condition_biotic_fish_invert.md) §3 |
| Coral cover | CSV (site × year) | site_id, year, coral_cover_pct | Opening year, Closing year | [skill_condition_biotic_coral.md](skill_condition_biotic_coral.md) |
| Coral bleaching prevalence | CSV (site × year) | site_id, year, bleaching_pct | Opening year, Closing year | [skill_condition_biotic_coral.md](skill_condition_biotic_coral.md) |

### 2.2 Reference Levels (Normalisation Thresholds)

| Indicator | Reference Level | Type | Source | Direction |
|---|---|---|---|---|
| Fish biomass (total) | 500 kg/ha | Higher-is-better | MacNeil et al. (2015) *Nature* | ↑ |
| Fish species richness | Max observed at any site | Higher-is-better | Site-level pool | ↑ |
| COTS density | 0 ind/ha (ideal); outbreak ≥ 30/ha | Inverted (lower is better) | AIMS LTMP | ↓ |
| Sea urchin density | Regional healthy-reef mean (TBD) | Context-dependent | Literature or regional baseline | Context |
| Giant clam abundance | Regional mean abundance (TBD) | Higher-is-better | Regional surveys | ↑ |
| Coral cover | Healthy-reef reference (80–90% for pristine) | Higher-is-better | Regional data / expert judgment | ↑ |
| Coral bleaching prevalence | 0% (ideal) | Inverted (lower is better) | NOAA thermal stress | ↓ |

**Note:** Reference levels must be established *before* opening/closing account compilation. See [skill_condition_biotic_fish_invert.md](skill_condition_biotic_fish_invert.md) §5 for derivation methods.

### 2.3 Accounting Period Definition

| Parameter | Value | Notes |
|---|---|---|
| Opening Year | YYYY (e.g., 2025) | First survey date; typically start of accounting period |
| Closing Year | YYYY (e.g., 2026) | Final survey date; typically end of accounting period |
| Accounting Period Span | N years | Recommend 2–5 years for meaningful change detection |
| Spatial Coverage | N sites (or N BSUs) | Survey sites or grid cells covering accounting area |
| Data Quality | Complete for both years | Missing data → interpolation or exclusion per QA/QC protocol |

---

## 3. Aggregation to Accounting-Area Level

### 3.1 Site-Level to Accounting-Area Aggregation

For indicators calculated at the site level, aggregate to an accounting-area representative value:

```
For each indicator I and year Y:

    Site-level values:    value_i(Y)  for sites i = 1..N

    Accounting-area mean: mean_I(Y) = Σ value_i(Y) / N

    Standard error:       SE_I(Y) = √[ Σ(value_i(Y) − mean_I(Y))² / (N − 1) ]

    95% confidence interval: [mean_I(Y) − 1.96×SE_I(Y), mean_I(Y) + 1.96×SE_I(Y)]

    (Optional) Area-weighted mean: mean_weighted_I(Y) = Σ (area_i × value_i(Y)) / Σ area_i
```

**Selection logic:**
- If sites are a random sample of the accounting area: use simple mean
- If sites are purposively selected (e.g., priority conservation zones): use area-weighted mean and note sampling design
- If sites represent distinct spatial strata: aggregate separately per stratum, then report stratum-level results alongside area mean

### 3.2 Functional Group Aggregation (Fish Indicators)

For fish indicators grouped by functional group (carnivore, herbivore, etc.):

```
Per site, per year, per functional group (FG):
    site_fg_biomass_mean    (kg/ha)
    site_fg_abundance_mean  (ind/ha)

Accounting-area FG totals:
    area_fg_biomass_mean = Σ site_fg_biomass_mean / N_sites
    area_fg_abundance_mean = Σ site_fg_abundance_mean / N_sites

Total fish (all FGs combined):
    area_fish_biomass_total = Σ area_fg_biomass_mean   (sum across FGs)
    area_fish_abundance_total = Σ area_fg_abundance_mean (sum across FGs)

Trophic composition:
    proportion_fg = area_fg_biomass_mean / area_fish_biomass_total
```

---

## 4. Condition Index Derivation

### 4.1 Standard Normalisation (Higher Is Better)

For indicators where higher measured values = better condition:

```
                    Measured Value (Year Y)
Condition Index(Y) = ─────────────────────────     (capped at 1.0)
                     Reference Level

CI ∈ [0, 1]   where 1.0 = reference level achieved, 0 = zero/minimum
```

**Example — Fish Biomass:**
```
Reference level = 500 kg/ha (unfished reef)

Opening year: Measured = 180 kg/ha  →  CI_opening = 180 / 500 = 0.36
Closing year: Measured = 220 kg/ha  →  CI_closing = 220 / 500 = 0.44
```

### 4.2 Inverted Normalisation (Lower Is Better)

For indicators where higher measured values = worse condition (e.g., COTS density, bleaching %):

```
                      Measured Value (Year Y)
Condition Index(Y) = 1 − ─────────────────────     (capped at [0, 1])
                         Maximum Acceptable Value

CI ∈ [0, 1]   where 1.0 = no degradation, 0 = maximum acceptable exceeded
```

**Example — COTS Density:**
```
Maximum acceptable = 30 ind/ha (outbreak threshold)

Opening year: Measured = 8 ind/ha   →  CI_opening = 1 − (8 / 30) = 0.73
Closing year: Measured = 2 ind/ha   →  CI_closing = 1 − (2 / 30) = 0.93
```

**Example — Coral Bleaching Prevalence:**
```
Maximum acceptable = 50% bleached (severe threshold)

Opening year: Measured = 22%  →  CI_opening = 1 − (22 / 50) = 0.56
Closing year: Measured = 8%   →  CI_closing = 1 − (8 / 50) = 0.84
```

### 4.3 Confidence Intervals on Condition Index

Propagate measurement uncertainty from raw values to condition index:

```
If indicator has standard error SE_measured, then:

    SE_CI ≈ SE_measured / Reference_Level   (for higher-is-better)

    95% CI on condition index:
        [CI − 1.96×SE_CI, CI + 1.96×SE_CI]   (capped at [0, 1])

Example — Fish Biomass with Uncertainty:
    Measured = 180 ± 35 kg/ha (SE = 35)
    Reference = 500 kg/ha
    CI = 0.36
    SE_CI = 35 / 500 = 0.07
    95% CI_opening = [0.36 − 0.137, 0.36 + 0.137] = [0.22, 0.50]
```

---

## 5. Opening/Closing Condition Account Table Compilation

### 5.1 Standard Format (Per-Site Results)

For detailed reporting, present one row per site per indicator:

```
| Site | Indicator | Unit | Opening Year | Opening Value (Raw) | Opening CI | Closing Year | Closing Value (Raw) | Closing CI | Absolute CI Change | % CI Change | Interpretation |
|---|---|---|---|---|---|---|---|---|---|---|---|
| M1 | Fish biomass | kg/ha | 2025 | 180 | 0.36 | 2026 | 220 | 0.44 | +0.08 | +22% | Improving |
| M1 | Fish richness | count | 2025 | 64 | 0.85 | 2026 | 68 | 0.90 | +0.05 | +6% | Improving |
| M1 | COTS density | ind/ha | 2025 | 8 | 0.73 | 2026 | 2 | 0.93 | +0.20 | +27% | Improving |
| M2 | Fish biomass | kg/ha | 2025 | 95 | 0.19 | 2026 | 110 | 0.22 | +0.03 | +16% | Stable |
| ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... |
```

### 5.2 Aggregated Format (Accounting-Area Summary)

For SEEA EA condition account publication, aggregate to accounting-area representative values:

```
| Ecosystem Type | Indicator | IUCN Code | Opening Year | Opening Value (Raw) | Opening CI | Closing Year | Closing Value (Raw) | Closing CI | Change in CI | % Change in CI | Interpretation | Data Quality |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Photic Coral Reef | Fish biomass (total) | M1.3 | 2025 | 164 ± 52 kg/ha | 0.33 ± 0.10 | 2026 | 189 ± 48 kg/ha | 0.38 ± 0.10 | +0.05 | +15% | Improving | Good (n=27) |
| Photic Coral Reef | Fish richness | M1.3 | 2025 | 71 ± 8 | 0.94 ± 0.11 | 2026 | 74 ± 7 | 0.97 ± 0.09 | +0.03 | +3% | Stable | Good (n=27) |
| Photic Coral Reef | COTS density | M1.3 | 2025 | 12 ± 6 ind/ha | 0.60 ± 0.20 | 2026 | 3 ± 2 ind/ha | 0.90 ± 0.07 | +0.30 | +50% | Improving | Good (n=27) |
| Photic Coral Reef | Coral cover | M1.3 | 2025 | 32 ± 8% | 0.35 ± 0.09 | 2026 | 38 ± 10% | 0.42 ± 0.11 | +0.07 | +20% | Improving | Moderate (n=15 sites with photo-quadrats) |
| Photic Coral Reef | Coral bleaching | M1.3 | 2025 | 18 ± 5% | 0.64 ± 0.10 | 2026 | 6 ± 3% | 0.88 ± 0.06 | +0.24 | +38% | Improving | Good (n=27) |
| Photic Coral Reef | Sea urchin density | M1.3 | 2025 | 8.2 ± 2.1 ind/m² | TBD | 2026 | 6.5 ± 1.8 ind/m² | TBD | TBD | TBD | Declining | Good (n=27); reference level TBD |
```

### 5.3 Functional Group Breakdown (Fish Indicators)

Optionally report fish biomass and abundance by functional group:

```
| Ecosystem Type | Calendar Year | Functional Group | Biomass Mean (kg/ha) | Biomass SE | Abundance Mean (ind/ha) | Abundance SE | Trophic Composition (% of Total Biomass) |
|---|---|---|---|---|---|---|---|
| Photic Coral Reef | 2025 | Carnivore | 52.3 | 16.4 | 45.2 | 14.1 | 32% |
| Photic Coral Reef | 2025 | Herbivore | 48.1 | 12.7 | 156.3 | 48.9 | 29% |
| Photic Coral Reef | 2025 | Planktivore | 38.2 | 11.5 | 248.7 | 81.3 | 23% |
| Photic Coral Reef | 2025 | Omnivore | 19.4 | 7.2 | 89.5 | 28.1 | 12% |
| Photic Coral Reef | 2025 | Other FGs | 6.0 | 2.1 | 22.3 | 8.6 | 4% |
| Photic Coral Reef | 2025 | **Total** | **164.0** | **52.1** | **562.0** | **176.3** | **100%** |
| | | | | | | | |
| Photic Coral Reef | 2026 | Carnivore | 58.7 | 15.2 | 48.1 | 13.4 | 31% |
| Photic Coral Reef | 2026 | Herbivore | 52.4 | 13.1 | 168.2 | 51.7 | 28% |
| Photic Coral Reef | 2026 | Planktivore | 44.6 | 10.8 | 271.5 | 78.4 | 24% |
| Photic Coral Reef | 2026 | Omnivore | 22.1 | 6.8 | 98.3 | 25.9 | 12% |
| Photic Coral Reef | 2026 | Other FGs | 11.2 | 3.4 | 42.7 | 12.1 | 6% |
| Photic Coral Reef | 2026 | **Total** | **189.0** | **47.8** | **628.8** | **190.2** | **100%** |
```

---

## 6. Change Metrics Calculation

### 6.1 Raw Value Change

For each indicator, calculate absolute and relative change:

```
Absolute Change = Closing Value − Opening Value

Percent Change = ((Closing Value − Opening Value) / Opening Value) × 100%
                 (handle division by zero for species richness if opening = 0)

Change Direction = {
    "Improving"  if: (higher is better AND closing > opening) OR (lower is better AND closing < opening)
    "Declining"  if: (higher is better AND closing < opening) OR (lower is better AND closing > opening)
    "Stable"     if: |Closing − Opening| < 5% of opening value OR |ΔCI| < 0.05
}
```

### 6.2 Condition Index Change

For policy interpretation, report condition index change separately:

```
Absolute CI Change = CI_closing − CI_opening    (range: −1.0 to +1.0)

Percent CI Change = ((CI_closing − CI_opening) / CI_opening) × 100%
                    (interpret cautiously if CI_opening near 0)

Strength of change: {
    "Large"    if: |ΔCI| ≥ 0.20
    "Moderate" if: 0.05 ≤ |ΔCI| < 0.20
    "Small"    if: |ΔCI| < 0.05
}
```

### 6.3 Confidence in Change Direction

Perform statistical test to assess whether observed change is significant given measurement uncertainty:

```
If 95% confidence intervals overlap:
    Conclusion: "No significant change detected"

If 95% CIs do NOT overlap:
    Conclusion: "Significant change detected (p < 0.05, approximate)"

Example:
    Opening CI: 0.36 [0.22, 0.50]
    Closing CI: 0.44 [0.30, 0.58]
    → CIs overlap; change is not significant

    Opening CI: 0.36 [0.30, 0.42]
    Closing CI: 0.48 [0.42, 0.54]
    → CIs do NOT overlap; change is significant
```

---

## 7. Data Quality and Uncertainty Summary

### 7.1 Data Completeness

For each indicator and year, document:

```
| Indicator | Opening Year | Data Completeness | Closing Year | Data Completeness | Notes |
|---|---|---|---|---|---|
| Fish biomass | 2025 | 100% (27/27 sites) | 2026 | 100% (27/27 sites) | Complete |
| Fish richness | 2025 | 100% (27/27) | 2026 | 100% (27/27) | Complete |
| COTS density | 2025 | 96% (26/27) | 2026 | 100% (27/27) | M7 missing 2025 data; interpolated from regional mean |
| Coral cover | 2025 | 56% (15/27 sites photo-sampled) | 2026 | 56% (15/27 sites) | Subset: only sites with photo-quadrat imagery |
| Sea urchin density | 2025 | 100% (27/27) | 2026 | 100% (27/27) | Complete |
```

### 7.2 Measurement Uncertainty

Document sources and magnitude of measurement error:

```
| Indicator | Source of Error | Magnitude | Mitigation |
|---|---|---|---|
| Fish biomass | Visual length estimate bias (±10–20% per individual) | ±30% | Validated against stereo-BRUV subset (n=3 sites) |
| Fish richness | Observer detection probability | ±5–10% | Single observer (Laza); consistent across surveys |
| COTS density | Small sample size at low-density sites | CV ~40% at sites with <5 COTS/ha | Reported with 95% CI; note interpretation at low densities |
| Coral cover | Photo-quadrat subsampling (n=50 quadrats/site) | ±3–5% per site | Sufficient replication per standard coral monitoring protocols |
| Bleaching assessment | Categorical visual estimate | ±2–3% per site | Cross-trained observers; reference photos provided |
```

### 7.3 Overall Assessment

Summarize data quality tier achieved:

```
┌───────────────────────────────────────────────────────────────┐
│ SEEA EA CONDITION ACCOUNT DATA QUALITY SUMMARY               │
│ Ecosystem: Photic Coral Reefs (M1.3)                          │
│ Accounting Area: SW Madagascar, Menabe District              │
│ Accounting Period: 2025–2026                                 │
│                                                              │
│ Overall Data Quality Tier: 2/3                               │
│ ├─ Spatial representation: Tier 2 (27 sites; adequate)      │
│ ├─ Indicator coverage: Tier 2 (6 indicators; good)          │
│ ├─ Measurement method: Tier 2 (UVC + allometric; validated) │
│ ├─ Reference level accuracy: Tier 1 (global benchmarks)     │
│ └─ Temporal monitoring: Tier 1 (single opening/closing pair)│
│                                                              │
│ Key Limitations:                                            │
│ • Fish biomass reference (500 kg/ha) is global benchmark;  │
│   regional calibration recommended                          │
│ • Single observer per dataset → cannot separate bias from   │
│   real change                                               │
│ • Coral cover data subset (15/27 sites); extrapolation      │
│   uncertain                                                 │
│                                                              │
│ Confidence in Results:                                       │
│ • Fish biomass & abundance: HIGH (replicated surveys)       │
│ • Fish richness: HIGH                                       │
│ • Invertebrate indicators: GOOD (complete coverage)        │
│ • Coral cover: MODERATE (subset of sites only)             │
│ • Overall change signal: GOOD (confident in direction,     │
│   magnitude has ±20% uncertainty)                           │
│                                                              │
│ Next Steps for Improvement:                                 │
│ 1. Derive regional fish biomass reference (Western Indian  │
│    Ocean); recalibrate CIs                                 │
│ 2. Expand coral cover monitoring to all 27 sites (2027)   │
│ 3. Implement stereo-BRUV validation at 5 sites (2027)     │
│ 4. Establish permanent monitoring stations for Tier 3      │
│    (2028+)                                                 │
└───────────────────────────────────────────────────────────────┘
```

---

## 8. Integration with SEEA EA Ecosystem Asset Account

The condition account feeds into the broader ecosystem asset characterisation:

```
┌─────────────────────────────────────────────────────────────────┐
│ ECOSYSTEM ASSET: Photic Coral Reefs (M1.3)                     │
│ SW Madagascar, Menabe District                                 │
│                                                                 │
│ Asset Characterisation (Opening Year 2025):                     │
│ ├─ Extent: 7,650 ha [from extent account]                      │
│ ├─ Condition: 0.35 (average across indicators) [← this skill]  │
│ ├─ Service Flow: Fish catch = 0.12 t/ha/yr [economic account] │
│ └─ Asset Value: (Extent × Condition × Service) discounted      │
│    V = f(7,650 ha, 0.35, 0.12 t/ha/yr, discount_rate)         │
│                                                                 │
│ Asset Characterisation (Closing Year 2026):                     │
│ ├─ Extent: 7,580 ha (−70 ha net loss) [extent account]        │
│ ├─ Condition: 0.40 (improving) [← this skill]                 │
│ ├─ Service Flow: Fish catch = 0.13 t/ha/yr                     │
│ └─ Asset Value: V' = f(7,580 ha, 0.40, 0.13 t/ha/yr, ...)      │
│                                                                 │
│ Accounting Period Change (2025 → 2026):                        │
│ • Extent: −70 ha (−0.9%)                                       │
│ • Condition: +0.05 CI (improving, +14%)                        │
│ • Service Flow: +0.01 t/ha/yr (+8%)                            │
│ • Asset Value Change: ΔV = V' − V (net accounting result)      │
│                                                                 │
│ Interpretation:                                                │
│ Reef is shrinking slightly (extent loss) but condition        │
│ is improving (fish biomass recovering, bleaching declining).  │
│ Net asset value depends on relative weighting of extent vs     │
│ condition vs service flows in valuation model.                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## 9. Output: Opening/Closing Condition Account

### 9.1 Publication-Ready Table Format

```
┌─────────────────────────────────────────────────────────────────────────────────────┐
│ ECOSYSTEM CONDITION ACCOUNT                                                        │
│ Photic Coral Reefs (M1.3) — Fish & Invertebrate Biotic Condition                   │
│ SW Madagascar, Menabe District                                                     │
│ Accounting Period: 2025 (Opening) – 2026 (Closing)                                 │
│                                                                                     │
│ ╔═════════════════════╦════════════════════════════╦══════════════════════════╗   │
│ ║ Condition           ║ 2025 (Opening)             ║ 2026 (Closing)           ║   │
│ ║ Indicator           ║ Raw Value  │  Condition    ║ Raw Value  │  Condition  ║   │
│ ║                     ║            │   Index       ║            │   Index     ║   │
│ ╠═════════════════════╬════════════╬═══════════════╬════════════╬═════════════╣   │
│ ║ Fish biomass (total)║ 164 ± 52   │ 0.33 ± 0.10  ║ 189 ± 48   │ 0.38 ± 0.10║   │
│ ║ [kg/ha]             ║            │              ║            │             ║   │
│ ║                     ║            │              ║            │             ║   │
│ ║ Fish abundance      ║ 562 ± 176  │ NA (non-     ║ 629 ± 190  │ NA          ║   │
│ ║ (total) [ind/ha]    ║            │  normalized) ║            │             ║   │
│ ║                     ║            │              ║            │             ║   │
│ ║ Fish species        ║ 71 ± 8     │ 0.94 ± 0.11 ║ 74 ± 7     │ 0.97 ± 0.09║   │
│ ║ richness [count]    ║            │              ║            │             ║   │
│ ║                     ║            │              ║            │             ║   │
│ ║ COTS density        ║ 12 ± 6     │ 0.60 ± 0.20 ║ 3 ± 2      │ 0.90 ± 0.07║   │
│ ║ [ind/ha]            ║            │ (inverted)   ║            │ (inverted)  ║   │
│ ║                     ║            │              ║            │             ║   │
│ ║ Sea urchin density  ║ 8.2 ± 2.1  │ TBD (ref     ║ 6.5 ± 1.8  │ TBD         ║   │
│ ║ [ind/m²]            ║            │  level TBD)  ║            │             ║   │
│ ║                     ║            │              ║            │             ║   │
│ ║ Coral cover [%]     ║ 32 ± 8     │ 0.36 ± 0.09 ║ 38 ± 10    │ 0.42 ± 0.11║   │
│ ║ (n=15 sites)        ║            │              ║            │             ║   │
│ ║                     ║            │              ║            │             ║   │
│ ║ Coral bleaching [%] ║ 18 ± 5     │ 0.64 ± 0.10 ║ 6 ± 3      │ 0.88 ± 0.06║   │
│ ║ prevalence          ║            │ (inverted)   ║            │ (inverted)  ║   │
│ ║                     ║            │              ║            │             ║   │
│ ║ COMPOSITE CONDITION ║             0.58*          ║             0.68*         ║   │
│ ║ INDEX (avg)         ║ [TBD: weighted or         ║             weighted avg  ║   │
│ ║                     ║  simple avg per           ║             approach to   ║   │
│ ║                     ║  weighting scheme]        ║             be specified] ║   │
│ ╚═════════════════════╩════════════╩═══════════════╩════════════╩═════════════╝   │
│                                                                                     │
│ CHANGE METRICS (2025 → 2026):                                                      │
│ ├─ Fish biomass: +25 kg/ha (+15%) → CI +0.05 (+15%)  [Improving, significant]    │
│ ├─ Fish richness: +3 sp. (+4%) → CI +0.03 (+3%)   [Stable, not significant]      │
│ ├─ COTS density: −9 ind/ha (−75%) → CI +0.30 (+50%) [Improving, significant]    │
│ ├─ Coral cover: +6% (+19%) → CI +0.06 (+17%) [Improving] *limited data          │
│ ├─ Bleaching: −12% (−67%) → CI +0.24 (+38%)  [Improving, significant]           │
│ └─ Overall: Composite CI +0.10 (+17%) — STRONG IMPROVEMENT                       │
│                                                                                     │
│ DATA QUALITY:                                                                      │
│ • Fish & invertebrate indicators: 100% data completeness (27 sites, both years)  │
│ • Coral cover: 56% completeness (15/27 sites with photo-quadrats)                │
│ • Measurement uncertainty: ±15–20% (propagated to CI uncertainty bands)          │
│ • Overall tier: 2/3 (good feasibility & accuracy; limited temporal depth)        │
│                                                                                     │
│ SIGN-OFF:                                                                          │
│ Analysis by: [Name, Role]          Date: [ISO 8601]    │                         │
│ Quality review: [Name, Role]       Status: ✓ APPROVED  │                         │
│                                                                                     │
│ * Composite CI approach: To be specified by accounting team (simple mean of all   │
│   indicators, or weighted mean prioritizing fish + invertebrate taxa). Sensitivity│
│   analysis recommended.                                                           │
└─────────────────────────────────────────────────────────────────────────────────────┘
```

### 9.2 CSV Export Format

```
# SEEA_EA_Condition_Account_Fish_Invert_2025_2026.csv

ecosystem_type,iucn_code,indicator,measurement_unit,opening_year,opening_value,opening_value_se,opening_ci,opening_ci_se,closing_year,closing_value,closing_value_se,closing_ci,closing_ci_se,absolute_change_raw,pct_change_raw,absolute_change_ci,pct_change_ci,change_interpretation,data_quality,reference_level,normalization_type
Photic Coral Reef,M1.3,Fish Biomass (total),kg/ha,2025,164,52,0.33,0.10,2026,189,48,0.38,0.10,+25,+15%,+0.05,+15%,Improving,Good (n=27),500 kg/ha,higher_is_better
Photic Coral Reef,M1.3,Fish Abundance (total),ind/ha,2025,562,176,NA,NA,2026,629,190,NA,NA,+67,+12%,NA,NA,Increasing,Good (n=27),NA,non_normalized
Photic Coral Reef,M1.3,Fish Species Richness,count,2025,71,8,0.94,0.11,2026,74,7,0.97,0.09,+3,+4%,+0.03,+3%,Stable,Good (n=27),Max Observed,higher_is_better
Photic Coral Reef,M1.3,COTS Density,ind/ha,2025,12,6,0.60,0.20,2026,3,2,0.90,0.07,-9,-75%,+0.30,+50%,Improving,Good (n=26),30 ind/ha,inverted_lower_is_better
Photic Coral Reef,M1.3,Sea Urchin Density,ind/m2,2025,8.2,2.1,TBD,TBD,2026,6.5,1.8,TBD,TBD,-1.7,-21%,TBD,TBD,Declining,Good (n=27),TBD,context_dependent
Photic Coral Reef,M1.3,Coral Cover (subset),pct,2025,32,8,0.36,0.09,2026,38,10,0.42,0.11,+6,+19%,+0.06,+17%,Improving,Moderate (n=15/27),80% (pristine),higher_is_better
Photic Coral Reef,M1.3,Coral Bleaching Prevalence,pct,2025,18,5,0.64,0.10,2026,6,3,0.88,0.06,-12,-67%,+0.24,+38%,Improving,Good (n=27),50% (severe),inverted_lower_is_better
```

---

## 10. Composite Condition Index (Optional)

If a single summary measure is required for the ecosystem asset:

### 10.1 Aggregation Approach (User Choice)

**Option A: Simple Average of Normalized Indicators**
```
Composite_CI = (CI_fish_biomass + CI_richness + CI_cots + CI_bleaching) / 4

2025: (0.33 + 0.94 + 0.60 + 0.64) / 4 = 0.628 ≈ 0.63
2026: (0.38 + 0.97 + 0.90 + 0.88) / 4 = 0.783 ≈ 0.78
Change: +0.15 (+24%)
```

**Option B: Weighted Average (e.g., prioritize fish biomass)**
```
Weights: Fish_biomass=0.40, Fish_richness=0.20, COTS=0.20, Bleaching=0.20

Composite_CI = (0.40×CI_biomass) + (0.20×CI_richness) + (0.20×CI_cots) + (0.20×CI_bleaching)

2025: (0.40×0.33) + (0.20×0.94) + (0.20×0.60) + (0.20×0.64) = 0.132 + 0.188 + 0.120 + 0.128 = 0.568
2026: (0.40×0.38) + (0.20×0.97) + (0.20×0.90) + (0.20×0.88) = 0.152 + 0.194 + 0.180 + 0.176 = 0.702
Change: +0.134 (+24%)
```

**Option C: Geometric Mean (less sensitive to outliers)**
```
Composite_CI = (CI_biomass × CI_richness × CI_cots × CI_bleaching)^(1/4)

2025: (0.33 × 0.94 × 0.60 × 0.64)^0.25 = (0.1198)^0.25 = 0.587
2026: (0.38 × 0.97 × 0.90 × 0.88)^0.25 = (0.2979)^0.25 = 0.740
Change: +0.153 (+26%)
```

**Recommendation:** Declare your weighting scheme *a priori*; justify weights based on:
- Ecological importance of each indicator
- Policy relevance
- Data quality / confidence
- Accounting period objectives

Document sensitivity analysis showing how composite CI changes if weights shift by ±10%.

---

## 11. Implementation Checklist

- [ ] **Obtain** calculated indicator values from field survey scripts (or companion condition skills)
- [ ] **Verify** that data exist for both opening and closing years
- [ ] **Select** reference levels for each indicator (see §2.2)
- [ ] **Validate** reference levels against literature and regional baselines
- [ ] **Aggregate** site-level values to accounting-area mean (or per-stratum if applicable)
- [ ] **Calculate** condition indices using appropriate normalisation formula (higher/lower/context)
- [ ] **Propagate** measurement uncertainty to CI uncertainty bands (95% CI)
- [ ] **Assess** whether observed change is significant (CI overlap test)
- [ ] **Compile** opening/closing condition account table (per-site and aggregated formats)
- [ ] **Calculate** change metrics (absolute, %, direction, strength)
- [ ] **Document** data quality: completeness, measurement error sources, overall tier
- [ ] **Flag** confidence intervals that exceed acceptable bounds (>50% relative uncertainty)
- [ ] **Optional: Calculate composite condition index** if single summary measure required (justify weighting)
- [ ] **Export** all tables as CSV; link raw values to Excel source data
- [ ] **Produce** summary report with sign-off and quality checklist (see §9.1)
- [ ] **Link** condition account outputs to extent account and economic account inputs

---

## 12. Data Quality & Limitations

| Issue | Impact | Mitigation |
|---|---|---|
| Reference levels are global / regional benchmarks, not local baselines | Condition indices may not reflect local ecological context (e.g., Madagascar reefs naturally lower biomass than Indo-Pacific) | Establish local baseline from >10 yr regional monitoring; recalibrate reference levels; report all assumptions |
| Single observer per dataset (e.g., fish: Laza, invertebrates: Maka) | Cannot separate observer bias from true ecosystem change | Note as limitation; validate subset with second observer; conduct sensitivity analysis |
| Limited temporal replication (opening/closing pair only) | Cannot distinguish true trends from inter-annual noise | Recommend future annual monitoring; establish >3 time points before claiming trend |
| Coral cover measured at only 15/27 sites | Cannot extrapolate condition to all sites | Report as subset result; expand coral cover monitoring in next cycle (2027) |
| Fish size estimates are visual (no stereo-video) | Biomass has ±10–20% uncertainty per individual; compounds to ±30% accounting-area mean | Validate subset with BRUV; report uncertainty bands; note as Tier 2 limitation |
| Sea urchin reference level TBD | Condition index cannot be calculated until regional baseline established | Literature review + expert elicitation; interim = descriptive reporting only |
| Measurement SE propagated to CI SE assumes independence | If errors are correlated across sites or methods, uncertainty estimates may be conservative or optimistic | Conduct sensitivity analysis: vary SE ±20%, re-calculate composite CI range |

---

## 13. Tiered Assessment

### Sub-procedure Tier Progression

| Sub-procedure | Tier 1 | Tier 2 | Tier 3 | Current (A / B / C) |
|---|---|---|---|---|
| Opening/closing condition table compilation | Manual spreadsheet aggregation | Automated script (e.g., R function) with validation checks (this skill) | Automated with uncertainty propagation, spatial heterogeneity quantified | 2 / 2 / 1–2 |
| Reference level selection | Ad-hoc, single global value | Literature review + documented assumption (this skill) | Multi-source evidence synthesis (local monitoring + paleocecological + expert panels) with Tier 3 confidence | 1 / 1–2 / 2–3 |
| Condition index normalisation | Simple ratio, no uncertainty | Standard formulae with SE propagation (this skill, §4.3) | Bayesian uncertainty integration accounting for classifier confidence | 2 / 2 / 2–3 |
| Change significance testing | Visual inspection only | Overlapping CI test (this skill, §6.3) | Formal hypothesis test (e.g., t-test or Wilcoxon) with multiple comparisons correction | 2 / 2 / 2–3 |
| Composite condition index | None or ad-hoc weighting | Documented weighting scheme with sensitivity analysis (this skill, §10) | Evidence-based weighting from stakeholder panels + formal elicitation; dynamic weighting by monitoring cycle | 2 / 2 / 2–3 |
| Integration to asset valuation | Conceptual only | Conceptual + worked example (this skill, §8) | Formal economic model linking extent, condition, services, and discount rates for asset value estimation | 1 / 1 / 2–3 |

### Binding Constraints

**Overall tier: 2/2 (Feasibility / Accuracy)**

The **reference level selection sub-procedure (A=2/B=1–2) is the binding constraint**. Global fish biomass reference (500 kg/ha) is scientifically defensible but may not reflect southwest Madagascar's local ecological context. To reach **Tier 3**, establish regional baselines from >10 years of monitoring data or paleocological reconstruction.

---

## 14. References

- **UN SEEA EA (2021).** *System of Environmental-Economic Accounting — Ecosystem Accounting: Final Draft (EEA).* UN Statistics Division.
  - See: Chapter 5 (Ecosystem Condition Accounts), Sections 5.1–5.3

- **MacNeil et al. (2015).** *Recovery potential of the world's coral reef fishes.* Nature, 520: 341–344.
  - Global unfished reef fish biomass benchmark (500 kg/ha)

- **AIMS Long-Term Monitoring Programme.** *Crown-of-thorns starfish monitoring and data interpretation.*
  - COTS outbreak threshold standards

- **ENDhERI Project (2023).** *Natural Capital Accounts for the Maldives: Ecosystem Extent and Condition.* UN Environment Programme.
  - Example opening/closing condition accounts with worked tables

- **GOAP Technical Guidance (2025).** *Integrating Ecosystem Accounts into National Environmental-Economic Accounting Systems.*
  - Tiered assessment framework for condition account accuracy

---

## 15. Related Skills and Companion Documents

- [skill_condition_biotic_fish_invert.md](skill_condition_biotic_fish_invert.md) — Calculate fish and invertebrate indicators from field survey data
- [skill_condition_biotic_coral.md](skill_condition_biotic_coral.md) — Calculate coral cover, bleaching, and benthic condition indicators
- [skill_extent_change_matrix_seea_account.md](skill_extent_change_matrix_seea_account.md) — Ecosystem extent accounts and change matrices
- [skill_extent_data_pipeline.md](skill_extent_data_pipeline.md) — Classification pipeline for satellite-derived extent data

---

*Derived from: UN SEEA EA (2021); ENDhERI Project (2023); GOAP technical guidance. Aligned with ISO 19115 metadata standards for ecosystem accounting data.*

*Version 1.0 | Last updated: 2026-03-04*
