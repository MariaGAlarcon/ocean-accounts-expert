# Condition Accounts

This folder contains skills for measuring ecosystem condition (health, integrity, functionality) across different ecosystem types and indicators.

## Contents

### Overview

Condition accounts measure how well an ecosystem is functioning relative to a reference level. Each skill addresses a specific ecosystem type and indicator category:

| Ecosystem Type | Folder | Coverage |
|---|---|---|
| **General/Multi-type** | `skill_condition_measurement.md` | Framework for all condition indicators across ecosystems |
| **Abiotic** | `skill_condition_abiotic.md` | Water quality, sediment, physical habitat (all ecosystems) |
| **Biotic — Coral** | `skill_condition_biotic_coral.md` | Coral cover, bleaching, benthic community (coral reefs) |
| **Biotic — Seagrass** | `skill_condition_biotic_seagrass.md` | Seagrass cover, shoot density, species composition (seagrass meadows) |
| **Biotic — Mangrove** | `skill_condition_biotic_mangrove.md` | Forest structure, basal area, species diversity (mangrove forests) |
| **Biotic — Fish & Invert** | `skill_condition_biotic_fish_invert.md` | Fish community (biomass, richness), invertebrate indicators (coral reefs, seagrass) |

---

## skill_condition_measurement.md

**Purpose:** Framework for measuring any ecosystem condition indicator following SEEA EA methodology.

**Covers:**
- General principles for condition indicator selection
- Reference level determination (literature, local baselines, model-derived)
- Normalisation to 0–1 condition indices
- Uncertainty and limitations documentation
- Temporal monitoring approaches
- Spatial stratification and extrapolation

**Use when:**
- Starting condition measurement for any ecosystem
- Need guidance on reference level choice
- Designing field survey or remote sensing protocol
- Normalising measured values to condition indices

---

## Abiotic Condition: `skill_condition_abiotic.md`

**Ecosystems:** All coastal/marine (coral reefs, mangroves, seagrass, estuaries)

**Indicators:**
- Water quality (temperature, salinity, turbidity, nutrients)
- Sediment quality (grain size, contaminants, organic content)
- Oxygen (dissolved oxygen, hypoxia)
- pH and carbonate system (acidification)
- Light availability (underwater light climate)

**Data sources:**
- Field sensors (CTD, spectrophotometer, sediment coring)
- Remote sensing (satellite water colour)
- Monitoring networks (real-time buoys, time series)

**Use when:**
- Assessing water/sediment quality conditions
- Quantifying environmental stressors on biota
- Detecting seasonal or long-term degradation

---

## Biotic Condition: Coral Reefs

### `skill_condition_biotic_coral.md`

**Ecosystem:** Photic coral reefs (M1.3)

**Indicators:**
- Live coral cover (% of reef surface)
- Coral bleaching index (% affected, severity)
- Coral disease prevalence
- Macroalgae cover (indicator of reef degradation)
- Coralline algae cover (indicator of reef calcification)
- Coral colony size structure (recruitment vs. mature)

**Data sources:**
- Underwater visual census (UVC) along transects
- Photo/video quadrats (permanent sites)
- Drone imagery (high-resolution orthomosaics)

**Outputs:**
- Site-level coral condition indices (0–1)
- SEEA EA coral condition account
- Temporal trends (opening vs. closing year)

**Use when:**
- Assessing reef health via benthic community
- Monitoring bleaching events
- Tracking coral recovery or degradation

---

## Biotic Condition: Seagrass Meadows

### `skill_condition_biotic_seagrass.md`

**Ecosystem:** Seagrass meadows (M2.1, M2.2)

**Indicators:**
- Seagrass area/extent (maps)
- Shoot density (shoots/m²)
- Leaf area index
- Species composition (dominance)
- Epiphyte load (indicator of eutrophication)
- Macroalgae/drift algae cover

**Data sources:**
- Aerial imagery + ground truthing
- Scuba survey transects (quadrats)
- Remote sensing (Sentinel-2, Planet Labs)

**Outputs:**
- Seagrass condition indices
- SEEA EA seagrass condition account
- Degradation stage classification (healthy, transitional, degraded)

**Use when:**
- Assessing seagrass health and productivity
- Tracking eutrophication impacts
- Monitoring species replacement or loss

---

## Biotic Condition: Mangrove Forests

### `skill_condition_biotic_mangrove.md`

**Ecosystem:** Mangrove forests (T2.1, T2.2)

**Indicators:**
- Forest basal area (m²/ha)
- Tree density (trees/ha by size class)
- Species composition and diversity
- Above-ground biomass (Mg/ha)
- Regeneration and recruitment (seedlings, saplings)
- Canopy closure (%)

**Data sources:**
- Permanent forest plots (tree census)
- Allometric equations (for biomass)
- Aerial imagery + ground truthing
- Satellite classification (Sentinel-2, SAR)

**Outputs:**
- Mangrove condition indices
- SEEA EA mangrove condition account
- Biomass (relevant for carbon service valuation)

**Use when:**
- Assessing forest health via stand structure
- Estimating carbon stocks (for climate service)
- Tracking forest recovery or degradation

---

## Biotic Condition: Fish & Invertebrate Communities

### `skill_condition_biotic_fish_invert.md`

**Ecosystems:** Coral reefs, seagrass meadows (mobile fauna, not benthic habitat)

**Indicators:**
- **Fish:** Biomass (kg/ha), abundance (ind/ha), species richness, trophic composition
- **Invertebrates:** COTS density (ind/ha), sea urchin density (ind/m²), clam/giant clam abundance, macroinvertebrate richness

**Data sources:**
- Underwater visual census (UVC) for fish
- Belt transects for macroinvertebrates
- Quadrats for benthic sessile invertebrates
- Field observer surveys

**Outputs:**
- Fish condition indices by functional group
- Invertebrate indicator values
- SEEA EA condition account (fish biomass, richness, COTS density)
- Site-level trends

**Use when:**
- Assessing ecosystem productivity via fish community
- Tracking reef degradation (COTS, urchin indicators)
- Evaluating trophic balance (herbivore/carnivore ratio)

---

## Workflow: From Field Survey to SEEA EA Condition Account

```
1. Choose indicator(s) for your ecosystem
   └─ Use: skill_condition_measurement.md (Section 1) + ecosystem-specific skill

2. Design field/remote sampling protocol
   └─ Use: ecosystem-specific skill (sampling design section)

3. Collect data
   └─ Field teams or remote sensing processors implement protocol

4. QA/QC data
   └─ Use: 01_framework/skill_data_quality_assessment.md

5. Calculate indicator values
   └─ Use: ecosystem-specific skill (calculation section)

6. Choose reference level
   └─ Use: skill_condition_measurement.md (Section 3)
   └─ Use: ecosystem-specific skill (reference level section)

7. Normalise to condition index (0–1)
   └─ Use: skill_condition_measurement.md (Section 4)

8. Assess uncertainty & limitations
   └─ Use: 01_framework/tiered_assessment_framework.md

9. Produce SEEA EA condition account
   └─ Use: 05_seea_accounting_tables/skill_condition_opening_closing_seea_account.md

10. Document findings
    └─ Output: site-level condition metrics, SEEA EA account table, metadata
```

---

## Key Decisions You'll Face

| Decision | Guidance |
|----------|----------|
| **Which indicators to measure?** | Match to ecosystem type and SEEA EA framework; start with 2–3 core indicators | |
| **Reference level source** | Literature (Tier 1) vs. local baseline (Tier 2) vs. modelled (Tier 3) — see skill_condition_measurement.md |
| **Field survey design** | Transect length, quadrat size, replication, frequency — see ecosystem-specific skill |
| **Spatial extrapolation** | Satellite-derived or field-only; depends on ecosystem type — see ecosystem-specific skill |
| **Temporal resolution** | Annual snapshots vs. seasonal monitoring — see skill_condition_measurement.md |

---

## Integration with Extent & Service Accounts

- **Extent accounts** (02_extent_accounts/): Condition is measured within extent polygons; stratified by ecosystem type
- **Service accounts** (04_service_accounts/): Condition indices inform service productivity (e.g., healthy reef → higher recreation value)
- **SEEA Accounting tables** (05_seea_accounting_tables/): Condition is the core row; opening/closing change is documented

---

## Quick Reference: Ecosystem Skill Comparison

| Skill | Ecosystem | Indicators | Complexity | Data Needs |
|-------|-----------|-----------|------------|-----------|
| `skill_condition_biotic_coral.md` | Coral reefs | Coral cover, bleaching, disease, macroalgae | Medium | UVC transects, photo quadrats, or drone |
| `skill_condition_biotic_seagrass.md` | Seagrass | Shoot density, leaf area, species, epiphytes | Medium | Aerial survey + ground truthing |
| `skill_condition_biotic_mangrove.md` | Mangrove | Basal area, biomass, diversity, regeneration | High | Permanent forest plots + allometrics |
| `skill_condition_biotic_fish_invert.md` | Coral reef/Seagrass | Fish biomass, richness, invertebrate indicators | Medium–High | UVC + species identification |
| `skill_condition_abiotic.md` | All ecosystems | Water quality, sediment, oxygen, pH | Low–Medium | Field sensors or satellite + buoys |

---

## Common Questions

**Q: How often should I measure condition?**
A: Annually (minimum) for temporal account; more frequently (quarterly) for monitoring trends. See skill_condition_measurement.md Section 5.

**Q: Can I use different indicators for different sites?**
A: Not recommended for SEEA EA consistency, but document any differences. See skill_condition_measurement.md Section 2.

**Q: What if my measured value exceeds the reference level?**
A: Normalize as 1.0 (capped). Document as "good condition" or "exceeds healthy baseline." See skill_condition_measurement.md Section 4.

**Q: How do I handle missing sites in year 2?**
A: See 05_seea_accounting_tables/skill_condition_opening_closing_seea_account.md (handling NA values).

---

**Related:** UN SEEA EA (2021) Chapter 5, GOAP technical guidance, WCS ecosystem monitoring guides
