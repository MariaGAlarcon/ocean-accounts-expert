# How to Use: Data Flow Template (Condition → Services)

## Overview

The **`template_data_flow_condition_to_services.md`** file is a reusable template for mapping ecosystem condition account outputs to ecosystem service account inputs within the SEEA EA framework.

**Use this template when:**
- You have completed condition account analysis and are planning service accounts
- You want to identify which services can use your condition data
- You need to plan data acquisition for missing service inputs
- You're integrating condition and service modules across an ecosystem accounting project

---

## Step-by-Step Instructions

### 1. Copy the Template

```bash
cp template_data_flow_condition_to_services.md [YOUR_PROJECT]/docs/data_flow_condition_to_services.md
```

### 2. Global Find-and-Replace

Replace all placeholders using your text editor:

| Placeholder | Replace With | Example |
|------------|--------------|---------|
| `[ECOSYSTEM TYPE CODE]` | Your ecosystem code | M1.3 (Photic Coral Reef) |
| `[ECOSYSTEM TYPE]` | Descriptive name | Coral reef, Mangrove, Seagrass |
| `[PROJECT]` | Project name | AFRICA — Madagascar |
| `[TIMEFRAME]` | Duration in weeks/months | 1 month, 3–4 months |
| `[SERVICE NAME]` | SEEA EA service name | Fisheries Nursery, Wild Fish Provisioning |
| `[YEAR]` | Calendar year | 2025, 2026 |
| `[X sites, Y transects]` | Your survey design | 27 sites, 2 transects per site |

### 3. Populate Part 1: Condition Account Outputs

#### 3a. Ecosystem Summary
Fill in:
- Ecosystem type and code (e.g., M1.3, M1.2, T2.1)
- Number of survey sites/stations
- Replication design (transects, quadrats, etc.)
- Spatial extent in hectares or km²

#### 3b. Indicator Table

For each main condition indicator:
1. **Indicator name** — What you measured (e.g., "Fish biomass", "Coral cover")
2. **Unit** — Standard unit (e.g., kg/ha, %, individuals/m²)
3. **Reference level** — Benchmark or target (from your condition skill document)
4. **Mean (Year 1)** — Average measured value in opening year
5. **Range** — Min–Max across all sites
6. **Notes** — Key context (e.g., "Inverted indicator", "Functional group breakdown available")

**Example:**
```
| Fish biomass | kg/ha | 500 kg/ha (unfished reef) | 1,928.9 | 1,200–2,500 | Total across all families; breakdown by functional group available |
```

#### 3c. Output Files

List the CSV files your analysis produces:
- `fish_invert_site_condition.csv` — what does it contain?
- `fish_invert_seea_condition.csv` — what does it contain?
- etc.

### 4. Populate Part 2: Service Requirements

For each planned service account, fill in:

#### 4a. Service Header
- SEEA EA section number (e.g., 6.1, 6.2, 6.6)
- CICES classification code
- Ecosystems that provide this service (e.g., "Coral reef, Seagrass")

#### 4b. Inputs Table

For each required input:
1. **Input name** — What's needed? (e.g., "Fish biomass (kg/ha)")
2. **Source type** — Where does it come from? (Condition account, External data, Literature)
3. **Your coverage** — Do you have it? Mark ✅ (yes), ⚠️ (partial), ❌ (no)
4. **Gap?** — YES or NO (is this a missing data item?)
5. **Notes** — Why is this needed, how will it be used, etc.

**Example:**
```
| Fish biomass (kg/ha) | Condition account | ✅ 1,928.9 kg/ha (2025) | NO | Direct input; already calculated |
| Market price of landed fish (USD/kg) | External data | ❌ — | YES | Must acquire from local fish markets |
```

#### 4c. Calculation Pathway

Write a simplified formula showing how inputs combine:

```
Enhanced juvenile biomass = Fish biomass × Nursery LRR (31%)
Harvestable contribution = Enhanced juvenile biomass × Survival rate (5%)
Nursery value (USD/yr) = Harvestable contribution × Market price (USD/kg)
```

### 5. Populate Part 3: Coverage Matrix

| Service | % of Inputs from Condition | Linkage | Actions |
|---------|----------------------------|---------|---------|
| Fisheries Nursery | 70% | STRONG | Acquire market prices |
| Wild Fish Provisioning | 50% | STRONG | Link to landings data |

**Coverage %:** Rough estimate of how many service inputs you can supply from condition accounts
- 0–30% = Weak linkage (condition is contextual only)
- 30–70% = Medium linkage (some core inputs from condition)
- >70% = Strong linkage (most inputs from condition)

**Linkage strength:** Narrative assessment
- STRONG: Condition data directly feed service quantification
- MEDIUM: Condition data inform service but require significant external data
- WEAK: Condition data provide context but not core inputs

### 6. Populate Part 4: Detailed Mapping Tables

For each service, create a data flow diagram showing:
- What condition outputs you'll use
- What external data you need
- How they'll be combined in calculation

**Template structure:**
```
CONDITION ACCOUNT INPUTS:
├── ✅ [INDICATOR FROM YOUR ACCOUNT]     → [DATA FILE]
├── ✅ [INDICATOR FROM YOUR ACCOUNT]     → [DATA FILE]
│
EXTERNAL INPUTS REQUIRED:
├── ⚠️ [MISSING DATA 1]                  → [ACQUISITION METHOD]
├── ⚠️ [MISSING DATA 2]                  → [ACQUISITION METHOD]
└── ⚠️ [MISSING DATA 3]                  → [ACQUISITION METHOD]

CALCULATION:
   [Your data] + [External data] = [Service value]
```

### 7. Populate Part 5: Missing Data Acquisitions

Create three-tier priority list:

**Priority 1 — Critical (needed for multiple services, urgent)**
- What data? Why needed? Who to contact? Timeline?

**Priority 2 — Important (service-specific, 1–3 month timeline)**
- What data? Why needed? Who to contact? Timeline?

**Priority 3 — Supplementary (nice to have, >3 month timeline)**
- What data? Why needed? Who to contact? Timeline?

### 8. Populate Part 6: Implementation Phases

Break down your integration work into 2–4 phases:

**Phase 1 (Weeks 1–4):** Quantify first service
- Task 1: Do X, create `file_a.csv`
- Task 2: Contact Y for data, create `file_b.csv`
- Task 3: Calculate Z using files A+B, create `file_c.csv`

**Phase 2 (Weeks 5–12):** Quantify second + third services
- Task 1: Acquire tourism data
- Task 2: Integrate with condition data
- Task 3: Produce preliminary service accounts

### 9. Populate Part 7: Template CSVs

For each service, sketch out what template CSV files you'll create:

**Filename:** `fish_biomass_by_family.csv`
**Columns:** Family | Species_count | Total_biomass_kg | Pct_of_total | Commercial_value | Market_price_USD_kg | Notes
**Example rows:** Scaridae | 12 | 425.3 | 23.8% | Yes | 2.50 | Primary harvest

### 10. Populate Part 8: Data Dictionary

Link each condition indicator to the services that use it:

| Condition Indicator | Unit | Service(s) | How It's Used |
|-------------------|------|-----------|---------------|
| Fish biomass | kg/ha | Nursery, Provisioning | Direct input for nursery LRR calculation |
| Fish richness | count | Recreation | Proxy for reef attractiveness to tourists |
| COTS density | ind/ha | Recreation | Negative valuation (coral damage) |

---

## Common Pitfalls to Avoid

❌ **Don't:**
- Skip the coverage analysis — be honest about gaps
- Assume all condition data feed all services (they usually don't)
- Underestimate time needed for external data acquisition
- Forget to document data sources and assumptions
- Leave placeholders unfilled

✅ **Do:**
- Be specific about which output files you're using from condition accounts
- Break missing data into priorities — you won't get everything at once
- Document who you'll contact and why
- Include realistic timelines based on your team's capacity
- Review with your data providers early and often

---

## Example: Real Project (Madagascar Coral Reef)

To see how this template was instantiated for a real project, refer to:
**`/Users/z5238824/Documents/GitHub/AFRICA - accounts/Madagascar/docs/data_flow_condition_to_services.md`**

This shows:
- All placeholders filled with project-specific data
- Specific service inputs mapped to fish/invertebrate condition outputs
- Concrete data acquisition leads (e.g., "Contact Laza for market price data")
- Detailed Phase 1–3 timeline with assigned tasks
- Template CSVs with example headers and rows

---

## When to Update This Document

- **Monthly:** Add new data acquisitions to Part 5
- **End of each phase:** Update coverage percentages, mark completed tasks
- **Quarterly:** Review linkages with project team, adjust priorities if needed
- **At project completion:** Archive as project documentation with lessons learned

---

## Questions?

Refer to:
1. **`skill_condition_*.md`** — Understand your condition account structure and outputs
2. **`skill_services_*.md`** — Understand service account input requirements
3. **`skill_services_measurement.md`** — General overview of all services across CICES categories
4. **UN SEEA EA (2021)** — Authoritative framework documentation

---

**Template version:** 1.0
**Last updated:** 2026-03-04
**Maintained by:** Accounting bot repository
