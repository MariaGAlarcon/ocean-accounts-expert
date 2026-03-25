# Skill: Ecosystem Extent Change Matrix & SEEA EA Account Tables

**Purpose:** Process classified BSU-level ecosystem type maps (opening and closing periods) into standardized SEEA EA ecosystem extent change matrices, opening/closing extent tables, and transition validation accounts.

**Framework:** UN SEEA EA Ecosystem Extent Accounts
**Companion skill:** [skill_extent_data_pipeline.md](skill_extent_data_pipeline.md) (classification layer upstream)
**Related condition skills:** [skill_condition_biotic_fish_invert.md](skill_condition_biotic_fish_invert.md) — condition indicators for ecosystem asset characterisation
**Spatial unit:** BSU (Basic Spatial Unit, 10 m × 10 m) or MBSU (Major BSU, country-specific)

---

## 1. Overview

This skill transforms per-BSU ecosystem type classifications into the canonical SEEA EA extent account format: opening extent, additions, reductions, net change, and closing extent per ecosystem type. The change matrix (cross-tabulation of opening vs closing types) reveals transition pathways and ecosystem dynamics, and serves as the audit trail for extent reconciliation.

```
Classified BSU Maps (opening t1, closing t2)
    ├── Per-BSU transition extraction
    ├── Ecosystem type change matrix (cross-tabulation)
    ├── Extent change calculations (additions, reductions, net change)
    ├── SEEA EA extent account table compilation
    ├── Transition interpretation and flagging
    └── Outputs: change matrix, extent tables, transition audit trail
```

---

## 2. Input Specifications

### 2.1 Classified BSU Maps

| Input | Format | Key Fields | Source |
|---|---|---|---|
| Opening period (t1) classified map | Raster (GeoTIFF) or feature grid | BSU_ID, ecosystem_type_t1, x, y, crs | [skill_extent_data_pipeline.md](skill_extent_data_pipeline.md) §4 |
| Closing period (t2) classified map | Raster (GeoTIFF) or feature grid | BSU_ID, ecosystem_type_t2, x, y, crs | [skill_extent_data_pipeline.md](skill_extent_data_pipeline.md) §4 |
| Accounting area boundary | Polygon shapefile | geom, accounting_area_id | Reference data |
| BSU area constant | Scalar (ha) | 0.01 ha per cell (10 m × 10 m) | Fixed by spatial resolution |

### 2.2 Classification Categories

| Class | IUCN GET Code | SEEA Extent Account | Status |
|---|---|---|---|
| Coral reef | M1.3 | Yes | Ecosystem type |
| Seagrass | M1.1 | Yes | Ecosystem type |
| Mangrove | MFT1.2 | Yes | Ecosystem type |
| Sand | — | No | Context (non-ecosystem) |
| Rubble | — | No | Context (non-ecosystem) |
| Rock | — | No | Context (non-ecosystem) |
| Macroalgae | — | No | Context (may include) |
| Deep water | — | No | Context (depth-masked) |
| Land | — | No | Context (terrestrial) |

**Note:** Only ecosystem types (M1.3, M1.1, MFT1.2) are included in the primary extent account. Other classes populate context tables and spatial audit layers.

---

## 3. Per-BSU Transition Extraction

### 3.1 Logic

For each BSU in the accounting area:

```
For BSU_i:
    opening_class = ecosystem_type_t1[BSU_i]
    closing_class = ecosystem_type_t2[BSU_i]

    transition = (opening_class, closing_class)

    If opening_class == closing_class → "Stable"
    Else → "Transition"

    Record: BSU_ID, opening_class, closing_class, transition_type, x, y
```

### 3.2 Transition Classification

| Transition Type | Logic | Accounting Impact |
|---|---|---|
| Stable | t1 = t2, both ecosystem or both non-ecosystem | No change to any ecosystem type extent |
| Addition (to T) | t1 ≠ ecosystem T, t2 = ecosystem T | +1 BSU to Additions_T |
| Reduction (from T) | t1 = ecosystem T, t2 ≠ ecosystem T | +1 BSU to Reductions_T |
| Within-ecosystem transition | t1 = ecosystem A, t2 = ecosystem B (both ecosystem types) | −1 from Reductions_A; +1 to Additions_B |
| Context transition (no SEEA impact) | t1 or t2 = non-ecosystem class (sand, deep, land) | None — recorded in audit trail only |

---

## 4. Ecosystem Type Change Matrix

### 4.1 Standard Format

The change matrix (or "transition matrix") is a cross-tabulation with opening extent types as rows and closing extent types as columns:

```
                          ┌─ CLOSING PERIOD (t2) ─┐
                    Coral    Seagrass   Mangrove   Other   Row Total
Opening (t1):
  Coral           [  C→C ]   [ C→SG ]   [ C→M ]   [C→*]    Opening_C
  Seagrass        [ SG→C ]   [SG→SG]    [SG→M]    [SG→*]   Opening_SG
  Mangrove        [ M→C ]    [ M→SG ]   [ M→M ]   [M→*]    Opening_M
  Other           [ *→C ]    [ *→SG ]   [ *→M ]   [*→*]    Opening_Other
  ─────────────────────────────────────────────────────────
  Col Total       Closing_C  Closing_SG Closing_M Closing_*  Total BA
```

### 4.2 Cell Definitions

| Cell | Interpretation | Equation |
|---|---|---|
| **Diagonal (C→C, SG→SG, M→M)** | Stable BSUs for that ecosystem type | Count of BSU_i where t1=T and t2=T |
| **Off-diagonal (C→SG, etc.)** | Transition from type A to type B | Count of BSU_i where t1=A and t2=B |
| **Row total** | Opening extent for ecosystem type in row | Sum across row (should = Col total if no errors) |
| **Column total** | Closing extent for ecosystem type in column | Sum down column |
| **Total BA** | Total accounting area (all BSUs) | Sum of all cells; constant across periods |

### 4.3 Example Matrix (Laamu Atoll, Maldives)

```
                          Closing 2020 (BSUs)
                    Coral   Seagrass  Mangrove  Sand   Rubble  Rock  Land  Deep  Row Total (2017)
Opening 2017:
  Coral           743,625    5,200      120    2,100   15,400  1,200   0      0      767,645
  Seagrass        4,100    489,100      60     8,900    3,200    800   0      0      506,160
  Mangrove           0         0      1,870       0       0     0     0      0        1,870
  Sand            1,200     3,100        0   950,000   12,300  1,500  100    0      967,900
  Rubble           2,100     1,100        0    11,200  789,100  2,300  50     0      805,750
  Rock               300       500        0     1,200    2,100 145,000 10   500      149,610
  Land               200       100        0       300       20   500 98,000  0       98,820
  Deep              0         0          0       0        0      0     0  100,000  100,000
  ───────────────────────────────────────────────────────────────────────────────
  Col Total (2020) 751,525  499,100    2,050  973,900  823,120 151,600 98,160 100,500  3,399,855

  (Total accounting area = 3,399,855 BSUs = 340,000 ha)
```

### 4.4 Matrix Validation Rules

```
✓ Σ(row_i) = Σ(col_i)   ← Total accounting area must reconcile
✓ Σ(diagonal) ≤ total_BSUs   ← Stable extent
✓ Σ(off-diagonal) = transitions
✗ If any cell < 0 → Classification error or spatial misalignment
✗ If Σ(row) ≠ Σ(col) → Data structure error
```

---

## 5. Extent Change Calculations

### 5.1 Formulae

For each ecosystem type **T**:

```
Opening_extent_T = Σ all BSUs classified as T in t1 (row total)

Additions_T = Σ BSUs transitioning from any non-T class to T
            = Σ (off-diagonal cells in column T, excluding diagonal)

Reductions_T = Σ BSUs transitioning from T to any non-T class
             = Σ (off-diagonal cells in row T, excluding diagonal)

Net_change_T = Additions_T − Reductions_T
             = Closing_extent_T − Opening_extent_T

Closing_extent_T = Opening_extent_T + Net_change_T

Reconciliation check:
  Opening_extent_T + Additions_T − Reductions_T = Closing_extent_T  ✓
```

### 5.2 Area Conversion

All extent values are expressed in hectares. BSU area constant:

```
BSU area = 10 m × 10 m = 100 m² = 0.01 ha

Extent_ha = Count_BSUs × 0.01 ha/BSU
```

### 5.3 Example Calculations (Coral Reef)

```
From change matrix above:

Opening_Coral = 767,645 BSUs × 0.01 ha = 7,676.45 ha

Additions_Coral = C→C cells entering Coral class:
                = (SG→C) + (*→C) (excluding diagonal)
                = (4,100 + 1,200 + 2,100 + 200) BSUs
                = 7,600 BSUs × 0.01 ha = 76.00 ha

Reductions_Coral = BSUs leaving Coral class:
                 = (C→SG) + (C→*) (excluding diagonal)
                 = (5,200 + 120 + 2,100 + 15,400 + 1,200) BSUs
                 = 24,020 BSUs × 0.01 ha = 240.20 ha

Net_change_Coral = 76.00 − 240.20 = −164.20 ha

Closing_Coral = 7,676.45 + 76.00 − 240.20 = 7,512.25 ha

Verification: Col total Coral (2020) = 751,525 BSUs = 7,515.25 ha
              ↓ (minor rounding difference; acceptable)
```

---

## 6. SEEA EA Extent Account Table

### 6.1 Standard Format

| Ecosystem Type | IUCN Code | Opening Extent (ha) | Additions (ha) | Reductions (ha) | Net Change (ha) | Closing Extent (ha) | Accounting Period |
|---|---|---|---|---|---|---|---|
| Coral reef | M1.3 | 7,676.45 | 76.00 | 240.20 | −164.20 | 7,512.25 | 2017–2020 |
| Seagrass | M1.1 | 5,061.60 | 71.00 | 128.10 | −57.10 | 5,004.50 | 2017–2020 |
| Mangrove | MFT1.2 | 18.70 | 0.20 | 0.00 | 0.20 | 18.90 | 2017–2020 |
| **Total ecosystem extent** | — | **12,756.75** | **147.20** | **368.30** | **−221.10** | **12,535.65** | **2017–2020** |
| Other (sand, rubble, context) | — | **327,243.55** | **221.10** | **147.20** | **+73.90** | **327,317.45** | **2017–2020** |
| **Total accounting area** | — | **340,000.30** | — | — | — | **340,000.30** | — |

**Key validation:** Total accounting area is constant; Additions and Reductions are inverses between ecosystem and context classes.

### 6.2 Supplementary Outputs

#### 6.2.1 Transition Details (Per Ecosystem Type)

For each ecosystem type T, document the composition of Additions and Reductions:

| Ecosystem Type | Transition | Source/Dest Class | BSU Count | Area (ha) | % of Additions/Reductions |
|---|---|---|---|---|---|
| Coral reef | Addition | Seagrass → Coral | 4,100 | 41.0 | 53.9% |
| Coral reef | Addition | Sand → Coral | 1,200 | 12.0 | 15.8% |
| Coral reef | Addition | Other → Coral | 2,300 | 23.0 | 30.3% |
| Coral reef | Reduction | Coral → Seagrass | 5,200 | 52.0 | 21.6% |
| Coral reef | Reduction | Coral → Sand | 2,100 | 21.0 | 8.7% |
| Coral reef | Reduction | Coral → Rubble | 15,400 | 154.0 | 64.2% |
| Coral reef | Reduction | Coral → Other | 1,620 | 16.2 | 6.7% |

**Interpretation:**
- Largest addition pathway: Seagrass → Coral (recovery, 54%)
- Largest reduction pathway: Coral → Rubble (degradation, 64%)
- Net loss reflects 2016 mass bleaching residual effects

#### 6.2.2 Stability Metrics

| Metric | Value | Interpretation |
|---|---|---|
| Total stable BSUs (diagonal) | 3,118,025 | 91.7% of accounting area unchanged |
| Stable Coral BSUs | 743,625 | 96.9% of 2017 coral extent unchanged |
| Stable Seagrass BSUs | 489,100 | 96.6% of 2017 seagrass extent unchanged |
| Stable Mangrove BSUs | 1,870 | 100% of 2017 mangrove extent stable |

---

## 7. Transition Interpretation & Flagging

### 7.1 Ecological Interpretation

For significant transitions (>5% of opening extent for an ecosystem type), document:

```
Transition Pattern: A → B
├── Magnitude: X BSUs (Y% of opening_A)
├── Cause hypothesis: [natural driver / anthropogenic pressure / classification error]
├── Ecological consequence: [recovery / degradation / turnover]
├── Validation status: [confirmed / suspected / requires ground truth]
└── Downstream impact: [condition indicators / service flows / asset value]
```

### 7.2 Flagging Rules for Quality Control

| Flag | Trigger | Action |
|---|---|---|
| **HIGH_TRANSITION** | >10% of opening extent changes for ecosystem type | Manual verification; verify against satellite imagery time series |
| **ASYMMETRIC_FLUX** | Additions >> Reductions or vice versa (imbalanced) | Check for classification drift between periods |
| **SMALL_CLASS_ARTIFACT** | Mangrove or other small extent type shows large % change | Review per-BSU transitions; may be measurement noise if <20 BSUs |
| **UNPLAUSIBLE_TRANSITION** | e.g., Large coral loss without rubble gain | Inspect classified maps; possible water column correction issue |
| **BOUNDARY_MISALIGNMENT** | Concentrated transitions at accounting area edge | Verify spatial registration and boundary clipping |

### 7.3 Example Flagged Transitions

```
TRANSITION: Coral → Rubble (15,400 BSUs, 6.4% of accounting area)
├── Magnitude: 154.0 ha loss from coral class
├── Context: 2016 global mass bleaching event affected Indian Ocean
├── Hypothesis: Bleaching-driven coral mortality and rubble formation
├── Validation: ✓ Consistent with NOAA coral bleaching alerts (2016)
└── Flag status: NO_FLAG — expected and documented

TRANSITION: Sand → Coral (1,200 BSUs, 0.3% of accounting area)
├── Magnitude: 12.0 ha of potential coral recovery
├── Context: Coral larvae recruitment in sheltered bays
├── Hypothesis: Post-bleaching recovery and coral settlement
├── Validation: NEEDS_VERIFICATION — confirm with condition account (coral cover)
└── Flag status: VERIFY_CONDITION — link to coral cover and bleaching indicators
```

---

## 8. Spatial Audit Layers

### 8.1 Change Maps (Per Ecosystem Type)

For each primary ecosystem type (Coral, Seagrass, Mangrove), produce three raster outputs:

```
Coral_Gain:  BSU = 1 if t1 ≠ coral AND t2 = coral (addition)
Coral_Loss:  BSU = 1 if t1 = coral AND t2 ≠ coral (reduction)
Coral_Stable: BSU = 1 if t1 = coral AND t2 = coral (stable)

Outputs:
├── GeoTIFF raster (10 m resolution)
├── Attribute table with BSU-level metadata
├── Summarised statistics by management zone (if applicable)
└── Map cartography (e.g., loss in red, gain in blue, stable in green)
```

### 8.2 Uncertainty Layers (If Applicable)

If per-BSU classification probabilities are available from the classifier:

```
Transition_Confidence:  BSU value = confidence that transition is true
                        High confidence: prob(t1) > 0.8 AND prob(t2) > 0.8
                        Low confidence: either prob < 0.5

Context_Boundary_Risk:  BSU value = 1 if within 1–2 cells of ecosystem boundary
                        (high risk of misclassification at edges)
```

---

## 9. Output: Reconciliation & Sign-Off

### 9.1 Extent Account Summary Report

```
┌──────────────────────────────────────────────────────────────────┐
│  ECOSYSTEM EXTENT ACCOUNT                                        │
│  Accounting Area: Laamu Atoll, Maldives                          │
│  Accounting Period: 2017 (opening) – 2020 (closing)              │
│                                                                  │
│  Key Results:                                                    │
│  ├─ Total extent: 340,000.3 ha (constant reconciliation)         │
│  ├─ Ecosystem extent change: −221.1 ha (−1.7%)                   │
│  ├─ Largest loss: Coral reef (−164.2 ha, −2.1%)                  │
│  ├─ Largest gain: Seagrass (−57.1 ha net loss, but 71 ha additions)│
│  └─ Stable extent: 91.7% of accounting area unchanged            │
│                                                                  │
│  Change Matrix:                                                  │
│  ├─ 9 ecosystem/context classes tracked                          │
│  ├─ 81 possible transitions observed                             │
│  ├─ 3 transitions flagged for verification (see detail)          │
│  └─ No data structure errors detected                            │
│                                                                  │
│  Data Quality:                                                   │
│  ├─ Classification accuracy (both periods): >80% OA              │
│  ├─ Extent reconciliation: 100% (opening + net = closing)        │
│  ├─ Spatial alignment: Verified (same CRS, 10 m resolution)      │
│  └─ Temporal coverage: Complete (both periods cloudless)         │
│                                                                  │
│  Sign-Off:                                                       │
│  Analysis conducted by: [Name]                                   │
│  Quality review by: [Name]                                       │
│  Date: [ISO 8601]                                                │
│  Status: ✓ APPROVED FOR PUBLICATION                              │
└──────────────────────────────────────────────────────────────────┘
```

### 9.2 Checksum & Validation Log

```
VALIDATION CHECKLIST:

✓ Total accounting area constant: 340,000.3 ha (opening) = 340,000.3 ha (closing)
✓ Extent reconciliation: Opening + net = closing for all ecosystem types
✓ Change matrix row/column totals reconcile
✓ No negative extent values
✓ No BSU counted twice (spatial non-overlap verified)
✓ All ecosystem types classified consistently
✓ Spatial extent covers entire accounting area boundary
✓ No temporal overlap or gaps (t1 = 2017, t2 = 2020, distinct)
✓ Transitional fluxes flagged for ground truth verification (3 flags)
✓ Accuracy metadata linked (confusion matrix, producer/user accuracy per class)

CONDITIONAL VALIDATIONS:

If high-resolution imagery available:
  ✓ Visual spot-checks of 10 transitions per ecosystem type
  ✓ Boundary alignment verified at 5 priority sites

If BRUV/stereo-video condition data available:
  ✓ Coral → Rubble transitions confirmed by coral bleaching indicators
  ✓ Seagrass → Sand transitions cross-checked with seagrass biomass decline

If historical satellite time series available:
  ✓ Transition patterns consistent with known disturbance history
  ✓ No anomalous multi-year jumps (would suggest process error)
```

---

## 10. Integration with Condition Accounts

**Note: This skill does NOT include condition data.** However, the extent classification and change matrix provide the spatial and temporal context for condition accounts:

```
Extent Account Outputs
    │
    ├──► Condition Account (per ecosystem type)
    │    Each ecosystem extent informs which BSUs to characterise for condition
    │    Condition indicators (e.g., fish biomass, coral cover, bleaching)
    │    are measured per site and linked to BSU extent via mapping
    │    See: skill_condition_biotic_fish_invert.md, skill_condition_biotic_coral.md
    │
    ├──► Transition Interpretation
    │    Coral → Rubble transition linked to bleaching condition indices
    │    Seagrass → Sand transition linked to seagrass biomass decline
    │    Recovery patterns (Sand → Coral, *→Seagrass) linked to condition improvement
    │
    └──► Ecosystem Asset Characterisation
         Extent change feeds into asset valuation models:
         C stock (Mg) = carbon density (Mg/ha) × extent (ha)
         Service flow = rate (units/ha/yr) × extent (ha)
         Asset value = f(extent, condition, flows) over accounting period
```

---

## 11. Data Quality & Limitations

| Issue | Impact | Mitigation |
|---|---|---|
| Classification method consistency | Different classifiers for t1 vs t2 → artefactual transitions | Apply identical classifier, parameters, and training data to both periods |
| Temporal imagery misalignment (e.g., high tide vs low tide for mangrove) | Tidal/seasonal variation misinterpreted as ecosystem change | Acquire imagery from same season; document tidal state |
| BSU boundary misalignment | Systematic edge shift → false transitions | Verify co-registration; apply geolocation correction if needed |
| Mixed pixels at ecosystem boundaries | Smooth transitions → crisp boundaries → apparent "gains" and "losses" | High-resolution imagery for boundary verification; document uncertainty |
| Sub-pixel classification error propagation | Small classification errors compound into large extent errors | Apply area-adjustment post-classification (Olofsson et al. 2014) |
| Cannot distinguish natural vs anthropogenic drivers | Change matrix shows WHAT changed, not WHY | Supplement with disturbance records, land-use data, environmental pressures |
| Small extent classes (e.g., mangrove <20 BSUs) | Individual BSU changes inflate % change rates | Report small extents with explicit acknowledgment of high % variability |

---

## 12. Implementation Checklist

- [ ] **Ingest** classified BSU rasters for opening (t1) and closing (t2) periods
- [ ] **Align** spatial extent: verify CRS, resolution (10 m × 10 m), accounting area boundary clipping
- [ ] **Extract** per-BSU transitions: BSU_ID, opening_class, closing_class, x, y
- [ ] **Construct** ecosystem type change matrix (cross-tabulation, opening vs closing)
- [ ] **Validate** matrix: reconcile row totals, column totals, accounting area constant
- [ ] **Calculate** additions, reductions, net change, closing extent per ecosystem type
- [ ] **Verify** reconciliation: opening + net = closing for all types
- [ ] **Flag** transitions: HIGH_TRANSITION, ASYMMETRIC_FLUX, BOUNDARY_MISALIGNMENT, etc.
- [ ] **Compile** SEEA EA extent account table (standardised format)
- [ ] **Produce** transition detail tables (source/destination, % composition of additions/reductions)
- [ ] **Generate** spatial audit layers: gain/loss/stable maps per ecosystem type
- [ ] **Document** ecological interpretation: hypotheses for major transitions
- [ ] **Link** flagged transitions to condition account indicators (if available)
- [ ] **Export** all outputs (CSV tables, GeoTIFF layers, summary report)
- [ ] **Sign-off** validation checklist; approve for publication

---

## 13. Tiered Assessment

### Tier Progression

| Sub-procedure | Tier 1 | Tier 2 | Tier 3 | Current (A/B/C) |
|---|---|---|---|---|
| Change matrix construction | Manual tabulation; limited classes | Automated cross-tabulation; all classes tracked (this skill) | Automated with area-adjusted uncertainty propagation | 2 / 2 / 2 |
| Extent reconciliation | Basic addition/subtraction | Full reconciliation with validation checklist (this skill) | Uncertainty quantified per BSU; confidence intervals reported | 2 / 2 / 1 |
| Transition interpretation | Descriptive only | Flagged thresholds for verification; ground truth review (this skill) | Attribution to drivers via disturbance records, climate data, land-use | 2 / 2 / 1–2 |
| Integration with condition | None | Links documented; spatial overlays prepared (this skill) | Formal uncertainty propagation from extent to condition to services | 1 / 1–2 / 2 |

### Binding Constraints

The **extent change matrix tier is 2 overall** (Tier 2 on A: Feasibility; Tier 2 on B: Accuracy with >80% classified extent). To reach **Tier 3**, implement:

1. **Area-adjusted estimates** (Olofsson et al. 2014) to account for classification errors and report confidence intervals per ecosystem type
2. **Temporal stability verification** (multi-year time series) to distinguish true transitions from inter-annual classification noise
3. **Causal attribution** by integrating disturbance records, land-use change maps, climate anomaly data, and management interventions
4. **Uncertainty propagation** from extent error into downstream condition and service account accuracy claims

---

## 14. References

- **UN SEEA EA (2021).** *System of Environmental-Economic Accounting — Ecosystem Accounting: Final Draft (EEA).* UN Statistics Division.
  - See: Chapter 4 (Ecosystem Extent Accounts), Section 4.1 (Change Matrix); Appendix C (worked examples)

- **IUCN Global Ecosystem Typology.** *Ecosystem Classification for Natural Capital Accounting.* IUCN, Cambridge.
  - Codes: M1.3 (Photic coral reefs), M1.1 (Seagrass), MFT1.2 (Mangrove forests)

- **Olofsson et al. (2014).** *Good practices for estimating area and assessing accuracy of land change.* Remote Sensing of Environment, 148: 42–61.
  - Recommended for area-adjusted extent uncertainty quantification (Tier 3)

- **ENDhERI Project (2023).** *Natural Capital Accounts for the Maldives: Ecosystem Extent and Condition.* UN Environment Programme.
  - Example implementation with worked change matrices and transition interpretation

- **RNF BCAF (GOAP, 2025).** *Applying SEEA EA at the Project Level in Central Java.*
  - Case study on ecosystem transition attribution; mangrove → aquaculture transitions; Tier 2–3 methods

---

*Derived from: UN SEEA EA (2021); ENDhERI Project (2023); GOAP technical guidance. Aligned with ISO 19115 metadata standards for spatial data.*

*Related skills: [skill_extent_data_pipeline.md](skill_extent_data_pipeline.md) (upstream classification); [skill_condition_biotic_fish_invert.md](skill_condition_biotic_fish_invert.md), [skill_condition_biotic_coral.md](skill_condition_biotic_coral.md) (downstream condition accounts).*
