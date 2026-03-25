# SEEA EA Accounting Tables

This folder contains skills for compiling extent, condition, and service data into formal SEEA EA accounting tables.

## Contents

### `skill_condition_opening_closing_seea_account.md`

**Purpose:** Standardized format for presenting condition account data in SEEA EA table format (opening year, closing year, change metrics).

**Covers:**
- Condition account table structure (rows = indicators, columns = years, change)
- Normalized vs. raw value tables
- Opening/closing value definition (first year surveyed vs. last year)
- Change metrics (absolute, percentage, interpretation: improving/stable/declining)
- Handling multi-year data (selecting opening/closing when intermediate years exist)
- Handling missing sites (interpolation vs. NA values)
- Metadata documentation (reference levels, uncertainties, data quality tier)

**Outputs:**
- Condition account table (per indicator, per site, per ecosystem type)
- Summary table (ecosystem-wide means and ranges)
- Metadata table (data quality, reference levels, limitations)

**Use when:**
- Finalizing condition measurement (ready to report)
- Comparing opening vs. closing ecosystem states
- Documenting temporal change over accounting period
- Preparing condition data for integration with services

**Structure:**
```
| Indicator | Site | Year_Open | Value_Open | Year_Close | Value_Close | Change | %_Change | Unit | Interpretation | CI_Open | CI_Close |
|-----------|------|-----------|-----------|-----------|-----------|--------|----------|------|---|---|---|
| Fish biomass | S001 | 2025 | 1850 | 2026 | 1920 | +70 | +3.8% | kg/ha | Improving | 0.92 | 0.96 |
```

---

## Planned/Needed Documents (Not Yet Created)

The following SEEA EA table formats are referenced in this skill but need to be developed:

### 1. **Extent Account Table** (To be added)
- Opening extent (Year 1)
- Transitions during accounting period (degradation, recovery, conversion)
- Closing extent (Year 2)
- Reconciliation (opening + transitions = closing)

**Example structure:**
```
| Ecosystem Type | Extent_Open (ha) | Degraded (ha) | Recovered (ha) | Converted (ha) | Extent_Close (ha) |
|---|---|---|---|---|---|
| Intact coral reef | 10,000 | -500 | +100 | -200 | 9,400 |
| Degraded coral reef | 2,000 | +500 | -100 | +200 | 2,600 |
```

### 2. **Service Supply Table** (To be added)
- Service by ecosystem type (rows)
- Opening year supply (kg/yr, Mg/yr, visitors/yr, USD/yr depending on service)
- Closing year supply
- Change in supply
- Physical unit and monetary unit tables (separate)

**Example structure:**
```
| Service | Ecosystem | Unit (Physical) | Supply_Open | Supply_Close | % Change | Unit (Monetary) | Value_Open | Value_Close |
|---|---|---|---|---|---|---|---|---|
| Fish provisioning | Coral reef | kg/yr | 50,000 | 52,000 | +4% | USD/yr | 125,000 | 130,000 |
| Reef recreation | Coral reef | trips/yr | 5,000 | 5,500 | +10% | USD/yr | 275,000 | 302,500 |
```

### 3. **Supply and Use Table** (To be added)
- Cross-tabulation: ecosystem services (columns) × economic sectors (rows)
- Shows which sectors use which services
- Physical and monetary balancing

**Example structure:**
```
| Sector | Fish Provisioning (USD) | Recreation (USD) | Coastal Protection (USD) | Total (USD) |
|---|---|---|---|---|
| Fisheries | 130,000 | — | — | 130,000 |
| Tourism | — | 302,500 | — | 302,500 |
| Coastal Management | — | — | 450,000 | 450,000 |
| **Total** | **130,000** | **302,500** | **450,000** | **882,500** |
```

---

## How to Use This Folder

### Step 1: Condition Account Compilation

Once you've completed condition measurement (extent, condition indicators):

1. Read `skill_condition_opening_closing_seea_account.md`
2. Organize your condition data (site-level values for Year 1 and Year 2)
3. Calculate change metrics (absolute and percentage)
4. Create condition account table (CSV format)
5. Document reference levels and uncertainties (metadata table)

### Step 2: Prepare for Service Integration

Once condition accounts are finalized:
- Use [06_templates/template_data_flow_condition_to_services.md](06_templates/) to link condition outputs to service inputs
- Identify which services depend on which condition indicators
- Determine data acquisition needs for services (see 04_service_accounts/)

### Step 3: Service Supply Tables (Future)

Once service accounts are complete:
1. Document service supply by ecosystem type and year
2. Create supply tables (physical and monetary, separate)
3. Compile supply and use table (cross-sector summary)

---

## Key Concepts

### Opening vs. Closing Year

- **Opening year:** First calendar year in accounting period (usually Year 1 of data collection)
- **Closing year:** Last calendar year in accounting period (usually Year 2 or later)
- **NOT opening/closing of a fiscal year** — these are calendar years

**Example:** If surveying 2025–2026, Opening = 2025, Closing = 2026

### Change Interpretation

For each indicator, classify change magnitude:

```
Condition Index Change (ΔCI):
- Improving:  ΔCI > +0.05  (condition improved by more than 5 percentage points)
- Stable:     |ΔCI| ≤ 0.05 (minimal change)
- Declining:  ΔCI < -0.05  (condition declined by more than 5 percentage points)
```

### Normalized vs. Raw Values

**Raw value table:** Actual measurements (e.g., 1,928.9 kg/ha)
**Normalized value table:** Condition indices 0–1 (e.g., 1.00 = condition ≥ reference level)

Create both for full transparency.

---

## Integration with Other Folders

- **02_extent_accounts/**: Extent account is the foundation row; condition and services are dependent accounts
- **03_condition_accounts/**: All condition measurements compiled here; converted to SEEA format here
- **04_service_accounts/**: Service accounts compiled separately; integrated into supply table in this folder
- **06_templates/**: Use data flow template to plan service integration

---

## SEEA EA Framework Context

```
┌─────────────────────────────────────────────────────┐
│         SEEA EA ECOSYSTEM ACCOUNTS                  │
├─────────────────────────────────────────────────────┤
│                                                     │
│  1. EXTENT ACCOUNT                                  │
│     (How much ecosystem? ha)                         │
│     └─ Opening extent | Transitions | Closing extent│
│                                                     │
│  2. CONDITION ACCOUNT                               │
│     (How healthy? 0–1 index)                        │
│     └─ Opening CI | Closing CI | Change             │
│                                                     │
│  3. SERVICE ACCOUNT                                 │
│     (What benefits? physical + USD/yr)              │
│     ├─ Physical supply (kg/yr, m³/yr, trips/yr)    │
│     └─ Monetary supply (USD/yr, indexed to prices) │
│                                                     │
│  4. INTEGRATED TABLES                               │
│     (Cross-sector summary)                          │
│     └─ Supply & Use table (ecosystem × sector)      │
│                                                     │
└─────────────────────────────────────────────────────┘
```

This folder documents how to compile accounts 2 (condition) and contains placeholders for 1, 3, and 4.

---

## Common Data Structures

### Condition Account Table (CSV)

**Columns:**
- Site (identifier)
- Indicator (name of metric)
- Year_Open (integer)
- Value_Open (numeric)
- CI_Open (0–1)
- Year_Close (integer)
- Value_Close (numeric)
- CI_Close (0–1)
- Absolute_Change (numeric)
- Percent_Change (percentage)
- Unit (standard unit, e.g., kg/ha)
- Reference_Level (benchmark)
- Interpretation (Improving/Stable/Declining)
- Data_Quality_Tier (1/2/3)
- Notes

**Example row:**
```
S001,Fish biomass,2025,1850,0.92,2026,1920,0.96,+70,+3.8%,kg/ha,500 kg/ha,Improving,2,Well-replicated survey; LW params from FishBase
```

### Metadata Table (CSV)

**Columns:**
- Indicator
- Reference_Level (value)
- Reference_Source (literature citation or local data)
- Measurement_Method (UVC, satellite, model, etc.)
- Temporal_Scope (snapshot vs. mean)
- Spatial_Scope (site vs. ecosystem-wide)
- Uncertainty_Range (confidence interval or ±%)
- Data_Quality_Tier (1/2/3 on feasibility and accuracy)
- Limitations (key caveats for policy use)

---

## Quick Reference: Outputting Condition Data

| Stage | Input | Output | Use |
|-------|-------|--------|-----|
| Measurement (03_condition_accounts/) | Field/remote data | Indicator values (per site, per year) | Raw data for accounting |
| Normalization (03_condition_accounts/) | Indicator values + reference level | Condition indices 0–1 | Standardized metrics |
| SEEA Format (05_seea_accounting_tables/) | Condition indices Year 1 & 2 | Condition account table (change metrics) | Formal reporting |
| Integration (06_templates/) | Condition + extent + services | Integrated supply/use table | Policy analysis |

---

## Questions?

- **How do I choose reference levels?** → See 03_condition_accounts/ (each ecosystem skill)
- **How do I compare sites with different data quality?** → Use Tier designation (documented in metadata table)
- **What if I only have Year 1 data?** → Document as "opening" and note in metadata that closing = TBD
- **How do I handle ecosystem transitions (e.g., coral → seagrass)?** → See 02_extent_accounts/skill_extent_change_matrix_seea_account.md
- **Can I disaggregate condition by management zone?** → Yes; create separate rows for each zone in account table

---

**Related:** UN SEEA EA (2021) Chapter 5–6, SEEA-CF (System of Environmental-Economic Accounting — Central Framework), GOAP technical guidance
