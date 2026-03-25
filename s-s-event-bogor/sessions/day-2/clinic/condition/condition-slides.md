# Condition Accounts -- Clinic Walkthrough Slides

**Time:** 15-30 min depending on participant level
**Purpose:** Guide a fellow through building an ecosystem condition account

---

## Slide 1: What is a condition account?

A condition account measures **ecosystem health** relative to a reference condition. It answers: how healthy is this ecosystem compared to an undegraded state?

| Component | What it records |
|-----------|----------------|
| Indicators | Measurable properties of ecosystem health (e.g., coral cover, fish biomass) |
| Reference levels | Benchmark for "healthy" state (from literature, historical data, or expert judgment) |
| Condition index (CI) | Normalized score from 0 (degraded) to 1 (reference condition) |
| Opening / closing | CI at start and end of accounting period |
| Change | How condition changed between periods |

---

## Slide 2: How it works -- the normalization step

Every indicator gets normalized to a 0-1 scale using a reference level.

**Higher-is-better indicators** (e.g., coral cover, fish biomass):

```
CI = Measured value / Reference level
```

Example: Measured coral cover = 20%, Reference = 50%
CI = 20 / 50 = 0.40

**Higher-is-worse indicators** (e.g., macroalgae cover, bleaching prevalence):

```
CI = 1 - (Measured value / Reference level)
```

Example: Measured macroalgae = 30%, Reference (max degraded) = 60%
CI = 1 - (30 / 60) = 0.50

**CI is capped at 1.0** (if measured value exceeds reference for higher-is-better, CI = 1.0)

---

## Slide 3: Common indicators by ecosystem type

**Coral reefs:**

| Indicator | Unit | Direction | Typical reference |
|-----------|------|-----------|------------------|
| Live coral cover | % | Higher is better | 40-50% (regional) |
| Fleshy macroalgae cover | % | Higher is worse | 60% (max degraded) |
| Fish biomass | kg/ha | Higher is better | 500 kg/ha (unfished) |
| Coral diversity (Shannon) | H' | Higher is better | Site-specific |
| Bleaching prevalence | % colonies | Higher is worse | 100% |

**Mangroves:**

| Indicator | Unit | Direction | Typical reference |
|-----------|------|-----------|------------------|
| Canopy cover | % | Higher is better | 80-90% |
| Tree density | stems/ha | Higher is better | Species-specific |
| Mean DBH | cm | Higher is better | Species-specific |

**Seagrass:**

| Indicator | Unit | Direction | Typical reference |
|-----------|------|-----------|------------------|
| Shoot density | shoots/m2 | Higher is better | Species-specific |
| Percent cover | % | Higher is better | 70-80% |
| Leaf area index | m2/m2 | Higher is better | Species-specific |

---

## Slide 4: Two pathways

**Pathway A -- No field data (Tier 1)**

Use remote sensing proxies and literature:
1. Sea surface temperature anomalies (DHW) as stress proxy
2. Chlorophyll-a as water quality proxy
3. Global condition assessments (e.g., Allen Coral Atlas condition layer)
4. Literature reference levels
5. Flag as "low confidence" -- plan for field validation

**Pathway B -- You have field survey data (Tier 2)**

Calculate from your monitoring data:
1. Select indicators based on what was measured
2. Set reference levels from literature or historical baselines
3. Normalize each indicator to 0-1 scale
4. Aggregate across sites (mean, SE)
5. Build the condition account table

---

## Slide 5: The condition account table

This is what you are building:

**Table [X]: Ecosystem Condition Account, [Area], [Opening] to [Closing]**

| Ecosystem type | Indicator | Reference level | Opening value | Opening CI | Closing value | Closing CI | Change in CI |
|---------------|-----------|----------------|---:|---:|---:|---:|---:|
| Coral reef (M1.3) | Live coral cover (%) | 50% | | | | | |
| | Macroalgae cover (%) | 60% | | | | | |
| | Fish biomass (kg/ha) | 500 | | | | | |
| Seagrass (M1.1) | Shoot density (shoots/m2) | [ref] | | | | | |
| | Percent cover (%) | [ref] | | | | | |
| Mangrove (MFT1.2) | Canopy cover (%) | 85% | | | | | |

---

## Slide 6: What to do right now

**If you have no field data:**
1. Check what remote sensing proxies exist for your area (SST, chlorophyll)
2. Check global assessments for baseline condition information
3. Document what indicators you would measure with field surveys
4. Plan a monitoring program to fill the gap

**If you have field data:**
1. List the indicators you have measured
2. Look up or decide on reference levels
3. Do the normalization calculation (use the exercise sheet)
4. Fill in the condition account table

**Worked example:** See the Belize coral reef condition account in `belize-project/`
