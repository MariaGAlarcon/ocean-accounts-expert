# Skill: Cultural Ecosystem Service Accounts

**Purpose:** Quantify the physical supply and monetary value of cultural ecosystem services — coral reef recreation, mangrove recreation, and seagrass gleaning — following the SEEA EA framework and CICES classification.

**Framework:** UN SEEA EA Ecosystem Service Accounts (Section 6.6)
**CICES Category:** Cultural services
**Services covered:**
1. Coral reef recreation (diving and snorkelling tourism)
2. Mangrove recreation (kayaking and ecotourism)
3. Seagrass gleaning (traditional harvesting with cultural dimensions)

---

## 1. Pipeline Overview

```
┌─────────────────────────────────────────────────────────────────────────┐
│                        DATA INGESTION LAYER                            │
│                                                                        │
│  Tourism Data               Socioeconomic Data       Survey Data       │
│  ┌──────────────┐           ┌───────────────┐       ┌──────────────┐  │
│  │ Resort visitor│           │ Tourist        │       │ Gleaner      │  │
│  │ statistics    │           │ expenditure    │       │ surveys      │  │
│  │               │           │ surveys        │       │ (effort,     │  │
│  │ Guesthouse   │           │                │       │  harvest,    │  │
│  │ visitor stats │           │ Tourist        │       │  species)    │  │
│  │               │           │ motivation     │       │              │  │
│  │ Dive centre  │           │ surveys        │       │ Local wage   │  │
│  │ activity logs │           │                │       │ data         │  │
│  │               │           │ Kayak tour     │       │              │  │
│  │               │           │ operator data  │       │ Market       │  │
│  │               │           │                │       │ prices       │  │
│  └──────┬───────┘           └──────┬────────┘       └──────┬───────┘  │
│         │                          │                        │          │
└─────────┼──────────────────────────┼────────────────────────┼──────────┘
          │                          │                        │
          ▼                          ▼                        ▼
┌─────────────────────────────────────────────────────────────────────────┐
│                    THREE CULTURAL SERVICE PIPELINES                     │
│                                                                        │
│  ┌──────────────────┐  ┌──────────────────┐  ┌──────────────────────┐ │
│  │ 1. CORAL REEF    │  │ 2. MANGROVE      │  │ 3. SEAGRASS          │ │
│  │    RECREATION    │  │    RECREATION    │  │    GLEANING          │ │
│  │                  │  │                  │  │                      │ │
│  │ Visitor stats    │  │ Trip counts      │  │ Gleaner counts       │ │
│  │ + activity       │  │ + group sizes    │  │ + effort (hrs/yr)    │ │
│  │   participation  │  │ + per-trip fee   │  │ + harvest (kg/yr)    │ │
│  │                  │  │                  │  │                      │ │
│  │ Direct           │  │ Direct           │  │ Equivalent wage      │ │
│  │ expenditure      │  │ expenditure      │  │ + market value       │ │
│  │ analysis         │  │ analysis         │  │ of harvest           │ │
│  │                  │  │                  │  │                      │ │
│  │ Value type:      │  │ Value type:      │  │ Value type:          │ │
│  │ Market-based     │  │ Market-based     │  │ Mixed                │ │
│  └────────┬─────────┘  └────────┬─────────┘  └──────────┬───────────┘ │
│           │                     │                        │             │
└───────────┼─────────────────────┼────────────────────────┼─────────────┘
            │                     │                        │
            ▼                     ▼                        ▼
┌─────────────────────────────────────────────────────────────────────────┐
│             SUPPLY AND USE TABLE COMPILATION                           │
│                                                                        │
│  Physical supply: visitors/trips/yr, hours/yr, harvest (kg/yr)         │
│                   — by ecosystem type                                  │
│  Monetary supply: expenditure, equivalent wage, harvest value          │
│                   — by ecosystem type and visitor segment              │
│  Use tables: tourism sector, local households (gleaning)               │
│                                                                        │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## 2. SOP: Coral Reef Recreation

**SEEA EA Section:** 6.6.1
**Providing ecosystem:** Coral reefs
**Valuation method:** Direct expenditure analysis
**Value type:** Market-based

### Part A: Physical Measurement

```
Step 1: Compile visitor statistics
    │
    ├── Obtain resort visitor statistics for the accounting area
    ├── Obtain guesthouse visitor statistics
    └── Record dive centre activity data (trips, participants)

Step 2: Quantify reef-based activity participation
    │
    ├── Number of dive trips per year
    ├── Number of snorkel trips per year
    ├── Number of participants by visitor segment:
    │     ├── Resort guests
    │     └── Guesthouse tourists
    └── Record activity rates (trips per visitor per stay)
```

**Physical account output:** Total reef-based activity trips and participants per year.

### Part B: Economic Valuation — Direct Expenditure Analysis

> **Value type: Market-based.** The valuation uses observed tourist spending data — actual transactions in functioning tourism markets.

```
Step 3: Identify coral reef-attributable expenditure
    │
    ├── Quantify spending directly attributable to reef-based activities:
    │     ├── Scuba diving excursion fees
    │     ├── Snorkelling excursion fees
    │     ├── Equipment rental
    │     └── Proportion of accommodation attributable to reef as
    │         primary attraction
    │
    └── Source: Tourist expenditure surveys, dive centre records

Step 4: Allocate accommodation expenditure
    │
    ├── Use tourist survey data to determine proportion of
    │   accommodation spending attributable to reef activities
    ├── Survey question: "How important were reef activities in
    │   your destination choice?"
    └── Apply allocation proportion to total accommodation expenditure

Step 5: Calculate total recreational value
    │
    │   Total value = Direct reef activity spending
    │               + Allocated accommodation spending
    │
    ├── Disaggregate by visitor segment:
    │     ├── Resort guests
    │     └── Guesthouse tourists
    │
    └── Example (Laamu Atoll, Maldives): USD 30.43 million/yr

Step 6: Map dive and snorkel sites
    │
    └── Produce spatial map: dive/snorkel sites relative to reef locations
```

**Formulae:**

```
Direct reef spending = Σ (Dive fees + Snorkel fees + Equipment rental)

Allocated accommodation = Total accommodation expenditure
                         × Reef attribution proportion (from tourist survey)

Total reef recreation value = Direct reef spending + Allocated accommodation

Per-visitor value = Total value / Total visitors
```

### Data Sources

| Data Source | Purpose |
|---|---|
| Resort visitor statistics | Tourist numbers and spending |
| Guesthouse visitor statistics | Budget tourist numbers and spending |
| Dive centre records | Activity participation rates |
| Tourist expenditure surveys | Reef-attributable spending |
| Tourist motivation surveys | Accommodation allocation factor |

### Tiered Monetary Valuation Methods — Coral Reef Recreation

| Monetary Tier | Method | NCAVES Category | Data Requirement |
|---|---|---|---|
| **Tier 1** | Value transfer — apply published per-visit consumer expenditure or recreation value from meta-analysis / ESVD for comparable tropical reef destinations; or use direct tour operator price × reported visit counts | I/V (published market price or value transfer) | National visitor statistics; published unit value from comparable sites (e.g., ESVD coral reef recreation values) |
| **Tier 2** | Direct expenditure analysis — reef-attributable tourist spending (dive/snorkel fees + allocated accommodation) from expenditure survey **(current method)** | I (directly observed market prices) | Tourist expenditure surveys; dive centre records; accommodation statistics; tourist motivation surveys for allocation factor |
| **Tier 3** | Travel cost model (TCM) / Random Utility Model (RUM) — estimate the value of reef visits from observed travel expenditure and trip behaviour; or simulated exchange value (SEV) conversion from WTP contingent valuation study | IV/V (revealed expenditure / simulated exchange value) | Structured visitor survey with origin, travel mode, travel cost, trip count, and stated motivations; or separate CV/DCE study with SEV conversion per NCAVES Chapter 3 |

> **NCAVES guidance (Chunk 25):** Direct consumer expenditure on recreation (Tier 2) is the preferred exchange-value-consistent method — it captures what the market actually transacts. TCM (Tier 3) estimates the **consumer surplus** component and must be converted to an exchange value via the SEV procedure before inclusion in SEEA EA monetary accounts. Hedonic pricing is theoretically applicable where reef proximity affects property values (NCAVES Cat. III), but data demands are very high.

---

## 3. SOP: Mangrove Recreation

**SEEA EA Section:** 6.6.2
**Providing ecosystem:** Mangroves
**Valuation method:** Direct expenditure analysis
**Value type:** Market-based

### Part A: Physical Measurement

```
Step 1: Identify mangrove tourism activities
    │
    ├── Catalogue all tourism activities at mangrove sites:
    │     ├── Guided kayaking
    │     ├── Birdwatching
    │     ├── Boardwalk tours
    │     └── Other ecotourism activities
    └── Example (Laamu Atoll, Maldives): Kayaking at Hithadhoo mangrove

Step 2: Compile activity data
    │
    ├── Number of trips per year (by activity type)
    └── Average group size per trip
```

**Physical account output:** Total trips and participants per year.

### Part B: Economic Valuation — Direct Expenditure Analysis

> **Value type: Market-based.** Based on actual fees charged for guided excursions.

```
Step 3: Calculate recreational value
    │
    │   Value = Number of trips × Average group size × Per-trip fee
    │
    └── Example (Laamu Atoll, Maldives): USD 2,400/yr
```

**Formula:**

```
Mangrove recreation value = Trips/yr × Group size × Fee/trip
```

### Notes

- Low values may reflect nascent or small-scale tourism operations
- Value may increase as ecotourism development expands
- Record activity as a baseline for tracking future growth
- Consider complementary valuation methods (e.g., willingness-to-pay) if direct expenditure appears to significantly underestimate the value

### Tiered Monetary Valuation Methods — Mangrove Recreation

| Monetary Tier | Method | NCAVES Category | Data Requirement |
|---|---|---|---|
| **Tier 1** | Value transfer — apply published recreation value per visit or per hectare for mangrove ecotourism from ESVD or regional comparable sites; multiply by current visit counts | V (simulated exchange value / value transfer) | Visit or trip counts (from operator records); published unit value from comparable mangrove ecotourism contexts |
| **Tier 2** | Direct expenditure analysis — tour operator fee × trips × group size **(current method)** | I (directly observed market prices) | Tour operator activity records (trips/yr, group size, per-trip fee) |
| **Tier 3** | Contingent valuation (CV) — stated willingness-to-pay for access to mangrove ecotourism experience, converted to simulated exchange value (SEV); applicable where nascent operations significantly understate the full value | V (simulated exchange value from stated WTP) | Designed CV survey (in-person or online); WTP elicitation with SEV conversion per NCAVES Chapter 3; recommended where direct expenditure is near-zero due to nascent market |

> **NCAVES guidance (Chunk 26 / Chapter 3):** For nascent or underdeveloped ecotourism operations where market prices do not yet exist or significantly understate value (as may be the case in early-stage mangrove tourism), contingent valuation converted to SEV can provide a legitimate exchange-value-consistent estimate. The SEV price represents the equilibrium price that would prevail in a functioning market under normal supply-demand conditions. This is appropriate when the physical quantity is already measured (trips/yr) and only the unit price is uncertain.

---

## 4. SOP: Seagrass Gleaning

**SEEA EA Section:** 6.6.3
**Providing ecosystem:** Seagrass meadows
**Valuation method:** Equivalent wage + market value of harvest
**Value type:** Mixed (market + imputed)

### Classification

- Classified as **cultural** rather than provisioning due to the strong social and cultural dimensions beyond subsistence value
- Predominantly undertaken by women
- Combines subsistence livelihood, social activity, and traditional practice

### Part A: Physical Measurement

```
Step 1: Survey gleaning activity
    │
    ├── Estimate the number of active gleaners in the accounting area
    ├── Record species harvested:
    │     ├── Sea cucumbers
    │     ├── Octopus
    │     ├── Shells
    │     └── Other invertebrates
    ├── Record timing: primarily during low tide events
    └── Example (Laamu Atoll, Maldives): 227 gleaners

Step 2: Estimate total effort
    │
    ├── Calculate total annual hours spent gleaning
    │     Total hours = Gleaners × Average trips/yr × Average hours/trip
    └── Example (Laamu Atoll, Maldives): 3,960 hours/yr

Step 3: Estimate total harvest
    │
    └── Record harvest quantities by species/type (kg/yr)
```

**Physical account output:** Number of gleaners, total effort (hours/yr), and harvest (kg/yr) by species.

### Part B: Economic Valuation — Equivalent Wage + Market Value

> **Value type: Mixed.** The harvest component uses observed market prices for harvested organisms. The labour component uses an imputed wage value — a standardised proxy for the opportunity cost of time, not a direct market observation.

```
Step 4: Calculate equivalent wage value
    │
    │   Wage value = Total hours × Local equivalent wage rate (currency/hr)
    │
    └── Use local minimum wage or average unskilled wage as proxy

Step 5: Calculate market value of harvest
    │
    └── Apply local market prices per kg for each harvested species

Step 6: Calculate total recreational/cultural value
    │
    │   Total value = Equivalent wage value + Market value of harvest
    │
    └── Present in supply and use table format
```

**Formulae:**

```
Equivalent wage value = Total gleaning hours (hr/yr)
                       × Local wage rate (currency/hr)

Market value of harvest = Σ (Harvest_species (kg/yr)
                           × Market price_species (currency/kg))

Total gleaning value = Equivalent wage value + Market value of harvest
```

### Tiered Monetary Valuation Methods — Seagrass Gleaning

| Monetary Tier | Method | NCAVES Category | Data Requirement |
|---|---|---|---|
| **Tier 1** | Value transfer — apply published per-hour equivalent wage or per-kg harvest value from comparable subsistence gleaning or traditional harvesting studies; or use national minimum wage and published harvest yield data | V (value transfer / imputed wage) | Gleaner count and estimated effort (hours/yr) from existing household surveys; national minimum wage data; published harvest value per species |
| **Tier 2** | Equivalent wage + market value of harvest **(current method)** — local wage rate × total gleaning hours, plus observed market prices × harvest quantities | I (market prices for harvest component) + imputed wage | Gleaner counts; gleaning effort (hrs/yr); local wage data; harvest quantities (kg/yr) by species; local market prices |
| **Tier 3** | Household production function — model the full economic value of gleaning to households, accounting for subsistence substitution value, cultural dimensions, and intra-household labour allocation; requires dedicated household survey with income and time-use module | III/V (productivity change / household production) | Detailed household survey (time use, income sources, subsistence consumption, market participation); econometric production function estimation; gender-disaggregated labour data |

> **NCAVES guidance:** The imputed wage (Tier 2) is the pragmatic SEEA EA approach — it values the labour input rather than the full economic surplus, which is consistent with the exchange value principle. Tier 3 household production models are methodologically demanding and most appropriate where gleaning represents a major livelihood component and policy decisions (e.g., access rights, ecosystem restoration) hinge on precise valuation.

---

## 5. Output: SEEA EA Supply and Use Tables

### 5.1 Physical Supply Table (Cultural Services)

```
┌─────────────────────────────────────────────────────────────────────────┐
│  PHYSICAL SUPPLY TABLE: Cultural Ecosystem Services                    │
│                                                                        │
│  ┌──────────────────────┬─────────────┬──────────┬───────────────────┐ │
│  │ Service              │ Coral Reefs │ Seagrass │ Mangroves         │ │
│  ├──────────────────────┼─────────────┼──────────┼───────────────────┤ │
│  │ Reef recreation      │ [visitors   │ —        │ —                 │ │
│  │                      │  or trips/  │          │                   │ │
│  │                      │  yr]        │          │                   │ │
│  ├──────────────────────┼─────────────┼──────────┼───────────────────┤ │
│  │ Mangrove recreation  │ —           │ —        │ [trips/yr]        │ │
│  ├──────────────────────┼─────────────┼──────────┼───────────────────┤ │
│  │ Seagrass gleaning    │ —           │ [hours/  │ —                 │ │
│  │ (effort)             │             │  yr]     │                   │ │
│  ├──────────────────────┼─────────────┼──────────┼───────────────────┤ │
│  │ Seagrass gleaning    │ —           │ [kg/yr]  │ —                 │ │
│  │ (harvest)            │             │          │                   │ │
│  └──────────────────────┴─────────────┴──────────┴───────────────────┘ │
└─────────────────────────────────────────────────────────────────────────┘
```

### 5.2 Monetary Supply Table (Cultural Services)

```
┌─────────────────────────────────────────────────────────────────────────┐
│  MONETARY SUPPLY TABLE: Cultural Ecosystem Services                    │
│                                                                        │
│  ┌──────────────────────┬─────────────┬──────────┬───────────────────┐ │
│  │ Service              │ Coral Reefs │ Seagrass │ Mangroves         │ │
│  ├──────────────────────┼─────────────┼──────────┼───────────────────┤ │
│  │ Reef recreation      │ [currency/  │ —        │ —                 │ │
│  │ (market-based)       │  yr]        │          │                   │ │
│  ├──────────────────────┼─────────────┼──────────┼───────────────────┤ │
│  │ Mangrove recreation  │ —           │ —        │ [currency/yr]     │ │
│  │ (market-based)       │             │          │                   │ │
│  ├──────────────────────┼─────────────┼──────────┼───────────────────┤ │
│  │ Gleaning — wage      │ —           │[currency/│ —                 │ │
│  │ (imputed)            │             │  yr]     │                   │ │
│  ├──────────────────────┼─────────────┼──────────┼───────────────────┤ │
│  │ Gleaning — harvest   │ —           │[currency/│ —                 │ │
│  │ (market-based)       │             │  yr]     │                   │ │
│  ├──────────────────────┼─────────────┼──────────┼───────────────────┤ │
│  │ Gleaning — total     │ —           │[currency/│ —                 │ │
│  │ (mixed)              │             │  yr]     │                   │ │
│  └──────────────────────┴─────────────┴──────────┴───────────────────┘ │
│                                                                        │
│  IMPORTANT: Label each value with its valuation type                   │
└─────────────────────────────────────────────────────────────────────────┘
```

### 5.3 Use Table (Cultural Services)

| Service | User / Beneficiary |
|---|---|
| Coral reef recreation | Tourism sector (resorts, guesthouses, dive operators) |
| Mangrove recreation | Tourism sector (ecotourism operators) |
| Seagrass gleaning | Local households (predominantly women) |

---

## 6. Example Summary Results (Laamu Atoll, Maldives)

```
┌─────────────────────────────────────────────────────────────────────────┐
│  CULTURAL SERVICE VALUES — Example from Laamu Atoll                    │
│                                                                        │
│  ┌──────────────────────────┬─────────────────┬──────────────────────┐ │
│  │ Service                  │ Value           │ Notes                │ │
│  ├──────────────────────────┼─────────────────┼──────────────────────┤ │
│  │ Coral reef recreation    │ USD 30.43M/yr   │ Dominant service;    │ │
│  │                          │                 │ 44.3% of all tourism │ │
│  │                          │                 │ spend attributable   │ │
│  │                          │                 │ to reefs             │ │
│  ├──────────────────────────┼─────────────────┼──────────────────────┤ │
│  │ Mangrove recreation      │ USD 2,400/yr    │ Small-scale; nascent │ │
│  │                          │                 │ ecotourism operation │ │
│  ├──────────────────────────┼─────────────────┼──────────────────────┤ │
│  │ Seagrass gleaning        │ Site-specific   │ 227 gleaners,        │ │
│  │                          │                 │ 3,960 hrs/yr        │ │
│  └──────────────────────────┴─────────────────┴──────────────────────┘ │
│                                                                        │
│  Note: Relative importance of services will vary by region.            │
│  In areas with less tourism, cultural service values may be lower      │
│  while provisioning or regulating services dominate.                   │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## 7. Data Quality and Limitations

| Service | Issue | Impact | Mitigation |
|---|---|---|---|
| Reef recreation | Accommodation allocation relies on tourist motivation survey | Methodology-dependent; sensitive to survey design | Standardise survey instrument; report methodology clearly |
| Reef recreation | Visitor statistics may be incomplete (informal operators) | Underestimate of physical activity | Cross-validate with dive centre logs |
| Mangrove recreation | Very small-scale activity at some sites | Low confidence in trend | Record as baseline; track over time |
| Mangrove recreation | Single operator data may not represent potential | Underestimates latent demand | Note nascent operation; consider contingent valuation |
| Gleaning | Limited baseline survey data | Moderate uncertainty in effort and harvest | Expand survey coverage; repeat surveys |
| Gleaning | Subsistence harvest difficult to price at market values | Market prices may not reflect true value | Use both wage and harvest components; document |
| Gleaning | Cultural and social value not fully captured by monetary methods | Monetary value is a lower bound | Note non-monetary significance; consider qualitative assessment |

---

## 8. Data Sources Summary

### Tourism Data

| Data Source | Purpose |
|---|---|
| Resort visitor statistics | Tourist numbers and reef activity participation |
| Guesthouse visitor statistics | Budget tourist numbers and participation |
| Dive centre records | Dive/snorkel trip counts, fees, equipment rental |
| Tour operator records | Mangrove kayaking trips, group sizes, fees |

### Survey Data

| Data Source | Purpose |
|---|---|
| Tourist expenditure surveys | Reef-attributable spending by category |
| Tourist motivation surveys | Accommodation allocation factor for reef value |
| Gleaner surveys | Number of gleaners, effort, species, harvest |

### Socioeconomic Data

| Data Source | Purpose |
|---|---|
| Local wage data | Equivalent wage rate for gleaning valuation |
| Local market prices (invertebrates) | Market value of gleaning harvest |
| National statistical office | Exchange rates, economic context |

---

## 9. Implementation Checklist

### Coral Reef Recreation
- [ ] **Obtain** resort visitor statistics for the accounting area
- [ ] **Obtain** guesthouse visitor statistics
- [ ] **Compile** dive centre activity data (trip counts, participants, fees)
- [ ] **Quantify** dive and snorkel trip participation by visitor segment
- [ ] **Conduct** or compile tourist expenditure surveys (reef-attributable spending)
- [ ] **Conduct** or compile tourist motivation surveys (accommodation allocation)
- [ ] **Calculate** direct reef activity spending
- [ ] **Calculate** allocated accommodation spending
- [ ] **Sum** total recreational value, disaggregated by visitor segment
- [ ] **Map** dive and snorkel sites relative to reef locations
- [ ] **Compile** physical and monetary supply and use tables

### Mangrove Recreation
- [ ] **Catalogue** all tourism activities at mangrove sites (across all sites if multiple)
- [ ] **Compile** trip counts, group sizes, and participation rates from tour operators
- [ ] **Obtain** per-trip fees; triangulate from operator interviews, booking platforms, and planning documents
- [ ] **Select** valuation approach: direct expenditure (Approach A) or P×Q with intermediate input deductions (Approach B)
- [ ] **If Approach B:** decompose expenditure into activities, accommodation (net of 54%/40%), and F&B (net of 30%)
- [ ] **Calculate** total mangrove recreation value per site and aggregate
- [ ] **Compile** physical and monetary supply and use tables
- [ ] **Note** whether activity is nascent or established; record as baseline

### Seagrass Gleaning
- [ ] **Survey** active gleaners (count, demographics, species harvested)
- [ ] **Estimate** total annual gleaning effort (hours/yr)
- [ ] **Estimate** total harvest by species (kg/yr)
- [ ] **Obtain** local equivalent wage rate
- [ ] **Calculate** equivalent wage value (hours × wage rate)
- [ ] **Obtain** local market prices for harvested species
- [ ] **Calculate** market value of harvest
- [ ] **Sum** total gleaning value (wage + harvest)
- [ ] **Compile** physical and monetary supply and use tables

### Cross-cutting
- [ ] **Assess** data quality for each service; flag data-deficient components
- [ ] **Document** metadata: data sources, assumptions, limitations, accounting period
- [ ] **Label** all monetary values with valuation type (market-based, imputed, or mixed)
- [ ] **Note** non-monetary cultural and social significance where applicable

---

## 10. Tiered Assessment

### Overview

This skill implements physical measurement and monetary valuation procedures for three cultural ecosystem services: coral reef recreation, mangrove recreation, and seagrass gleaning. The tier profiles differ meaningfully across these services, reflecting differences in data availability, institutional context, and methodological complexity. The current SOPs generally implement Tier 2 physical measurement and Tier 2 monetary valuation for all three services, though several sub-procedures within each service operate at Tier 1. Tier scores are drawn from the Summary Assessment Matrix (Section 4) and the Monetary Valuation Tier Matrix (Section 4a) of the Tiered Assessment Framework.

---

### Physical Measurement Tier Profiles

#### Coral Reef Recreation

Reference: Tiered Assessment Framework, Section 4 — Coral reef recreation rows.

| Sub-procedure | Approach description | A: Feasibility | B: Accuracy | C: Difficulty |
|---|---|---|---|---|
| Visitor count compilation (resort / guesthouse / dive centre records) | Extract annual visitor arrivals and activity participation from operator records and accommodation statistics | 1 | 1–2 | 1 |
| Reef attribution (motivation surveys or coral dependence fraction) | Apply allocation fraction from tourist motivation survey or literature-based coral-dependence factor to total visitor pool | 2 | 1–2 | 2 |
| Physical supply metric (visitor-days or activity-days at reef) | Aggregate reef-attributed visitor-days or activity-days as the physical output for the account | 1–2 | 2 | 1–2 |

**Current default tier:** Tier 2 on Dimensions A and C; Tier 1–2 on Dimension B.

**Binding constraint:** Dimension B — accuracy. The reef attribution step introduces the largest uncertainty in the physical measurement chain. The allocation factor derived from motivation surveys is sensitive to question framing and can range from 20% to 70% for the same visitor population, producing a corresponding range in the final physical supply figure.

---

#### Mangrove Recreation

Reference: Tiered Assessment Framework, Section 4 — Mangrove recreation rows.

| Sub-procedure | Approach description | A: Feasibility | B: Accuracy | C: Difficulty |
|---|---|---|---|---|
| Visitor count (tour operator records + on-site count) | Obtain trip counts and group sizes from operator records; supplement with on-site counting where multiple operators exist | 1 | 1–2 | 1 |
| Trip / activity documentation | Record activity type, group size, and seasonality across all mangrove sites | 1–2 | 2 | 1 |
| Physical supply metric (visitor-trips) | Sum total trips per year as the physical output for the account | 1 | 2 | 1 |

**Current default tier:** Tier 1–2 on most dimensions.

**Binding constraint:** Dimensions A and B — feasibility and accuracy. Mangrove ecotourism is nascent in many SIDS contexts, with a single operator and irregular activity. Single-operator, single-year data are subject to idiosyncratic variation and do not reflect the ecosystem's underlying capacity to supply recreational services. The observed physical quantity systematically understates latent demand where supply is constrained.

---

#### Seagrass Gleaning

Reference: Tiered Assessment Framework, Section 4 — Seagrass gleaning rows.

| Sub-procedure | Approach description | A: Feasibility | B: Accuracy | C: Difficulty |
|---|---|---|---|---|
| Gleaner survey (effort, catch, species) | Purpose-designed household survey or community logbook recording gleaning trips, duration, species, and harvest; requires female enumerators and local-language instruments | 1–2 | 2 | 1–2 |
| Harvest yield estimation (kg/trip or kg/ha) | Estimate total annual harvest by species from survey data; calibrate informal units to kg | 2 | 2 | 2 |
| Physical supply metric (kg/yr) | Aggregate harvest by species as the physical output for the account; supplemented by total effort (hours/yr) | 2 | 2 | 2 |

**Current default tier:** Tier 2 on most dimensions.

**Binding constraint:** No single dominant constraint — all three dimensions are at Tier 2. The household survey requirement (Dimension A) and the self-report accuracy limitation (Dimension B, CV 20–50%) are co-binding. Moving to Tier 3 on accuracy requires a biophysical production model linked to seagrass condition monitoring, which also elevates resource and difficulty requirements.

---

### Monetary Valuation Tier Profiles

Monetary valuation tiers are assessed on four dimensions from Tiered Assessment Framework Section 4a.3: A (Feasibility), B (Accuracy), B (Temporal consistency), C (Difficulty), and D (Exchange value consistency).

#### Coral Reef Recreation — Monetary Valuation

- **Tier 1:** Value transfer from ESVD or published per-visit recreation value from meta-analysis for comparable tropical reef destinations; or direct tour operator price multiplied by reported visit counts.
- **Tier 2 (current default):** Direct expenditure analysis — reef-attributable tourist spending (dive/snorkel activity fees plus allocated accommodation expenditure from motivation survey).
- **Tier 3:** Travel cost model (TCM) or random utility model (RUM) estimated from structured visitor survey; simulated exchange value (SEV) conversion from contingent valuation or discrete choice experiment; hedonic property pricing where reef proximity affects property values.

| Monetary dimension | Tier 2 score | Basis |
|---|---|---|
| A: Feasibility | 2 | Requires tourist expenditure surveys and operator interviews; 1–6 months to first estimate |
| B: Accuracy | 2 | Reflects actual local market expenditure; limited transfer error; CV 20–50% on accommodation attribution step |
| B: Temporal consistency | 2 | Annually updatable from consistent sources (operator records, accommodation statistics, motivation surveys) |
| C: Difficulty | 2 | Requires inter-agency coordination with tourism authorities; seasonal stratification; survey design expertise |
| D: Exchange value consistency | 2 | Direct expenditure is an exchange value by definition; consumer surplus is excluded; method is Category I compliant |

---

#### Mangrove Recreation — Monetary Valuation

- **Tier 1:** Value transfer from ESVD or comparable mangrove ecotourism sites multiplied by current trip counts.
- **Tier 2 (current default):** Direct expenditure — tour operator fee multiplied by trips per year multiplied by average group size.
- **Tier 3:** Contingent valuation (WTP converted to simulated exchange value); applicable where nascent operations significantly understate market value because current operator fees do not reflect what a functioning market would sustain.

| Monetary dimension | Tier 2 score | Basis |
|---|---|---|
| A: Feasibility | 1–2 | Operator fee data and trip counts obtainable from a single operator interview; minimal survey burden |
| B: Accuracy | 1–2 | Limited market data for nascent sector; observed operator fees may not represent full exchange value under normal supply-demand conditions |
| B: Temporal consistency | 2 | Updatable annually from operator records |
| C: Difficulty | 1–2 | Calculation is straightforward; inter-agency coordination minimal; interpretation of near-zero values is the principal challenge |
| D: Exchange value consistency | 2 | Operator fees are exchange values (Category I); method is compliant, though the fee may be unrepresentatively low |

Note: Where mangrove ecotourism is nascent and operator fees substantially understate market value, the SOP notes that Tier 3 — contingent valuation converted to SEV — may be warranted. This applies specifically to situations where the policy question concerns whether to develop or protect a site, and where current realised demand significantly understates latent demand.

---

#### Seagrass Gleaning — Monetary Valuation

- **Tier 1:** Value transfer — published per-hour imputed wage or per-kg harvest value from comparable subsistence gleaning studies; or national minimum wage applied to extrapolated effort hours.
- **Tier 2 (current default):** Equivalent wage (local wage rate multiplied by total gleaning hours) plus market value of harvest (local market price per kg multiplied by harvest quantities by species).
- **Tier 3:** Household production function — full economic value including subsistence substitution, cultural dimensions, and intra-household labour allocation; requires dedicated household survey with time-use and income module.

| Monetary dimension | Tier 2 score | Basis |
|---|---|---|
| A: Feasibility | 2 | Requires local wage data and harvest survey; 1–6 months to first estimate |
| B: Accuracy | 2 | Local wage and market prices used; limited transfer error; CV 20–50% reflecting self-report variability in effort and harvest |
| B: Temporal consistency | 2 | Updatable annually from wage statistics and market price monitoring |
| C: Difficulty | 2 | Requires gleaner survey logistics, female enumerators, local-language instruments, and community trust-building |
| D: Exchange value consistency | 2 | Imputed wage is an exchange value proxy; harvest market price is a Category I exchange value; consumer surplus excluded |

---

### Double-Counting Note

The seagrass gleaning service shares a physical pathway with wild fish provisioning: both draw from coastal fisheries stocks supported by seagrass meadow habitat. Where the accounting area includes both a seagrass gleaning account and a wild fish provisioning account, there is a risk that the same seagrass-supported harvest is counted under both service categories. Review the full set of service estimates before aggregating to ensure the same seagrass-supported invertebrate and fish harvest is not recorded under both gleaning and fish provisioning accounts. This double-counting risk is noted in the Tiered Assessment Framework (Section 4a.3) as a structural cross-service issue that is not resolved by any individual-method tier assignment.

---

### Progression Pathway

The following investments would unlock the next tier for each service:

- **Coral reef recreation → Tier 3 (physical and monetary):** Implement a travel cost model using a structured visitor survey that captures origin, travel mode, travel cost, and trip count. This avoids the accommodation attribution problem entirely and produces a defensible consumer surplus estimate that can be converted to SEV.
- **Mangrove recreation → Tier 3 (monetary):** Implement a contingent valuation survey to elicit WTP for access to mangrove ecotourism, converted to SEV. This is warranted where nascent operator fees substantially understate market value and where an active policy decision (development, protection, or restoration) is at stake.
- **Seagrass gleaning → Tier 3 (physical and monetary):** Implement a household production function survey with a full time-use and income module, linked to biophysical production models that relate seagrass condition to invertebrate productivity. This resolves the double-counting concern, captures condition-dependent supply, and produces a methodologically defensible full economic value.

---

*Derived from: SEEA EA Ecosystem Service Accounts (Section 6.6). Examples from ENDhERI Project — Compiling the first Natural Capital Accounts in the Maldives. Alternative methods from: Applying SEEA EA at the Project Level in Central Java (RNF BCAF, GOAP, 2025). Aligned with UN SEEA EA (2021), CICES v5.1, and GOAP technical guidance.*

---

## 11. Tiered Physical Measurement Methods

This section provides alternative physical measurement methods at three resource/accuracy tiers, following the Tiered Assessment Framework. **Physical values only** — monetary valuation is covered separately in each SOP's Part B.

### 10.1 Coral Reef Recreation — Visitor-Trips (trips/yr)

#### Tier 1: National Tourism Statistics with Activity Participation Rates

**Method:** Extract national visitor arrival statistics from national tourism authority or UNWTO. Downscale to accounting area by bed-share or accommodation capacity proportion. Apply published reef activity participation rates (proportion engaging in diving/snorkelling) from comparable SIDS or global meta-analyses.

| Attribute | Detail |
|---|---|
| Physical output | Estimated reef activity trips/yr — indicative |
| Key source | UNWTO, *Tourism Highlights / Compendium of Tourism Statistics* (annual) |
| Supporting sources | ENDhERI (2025), Section 6.6.1 — Tourism Yearbook downscaling method: Laamu Atoll's 0.75% bed-share of national arrivals → 15,356 visitors |
| | Maldives Bureau of Statistics, *Tourism Satellite Account*, 2017 (updated annually) |
| Data inputs | National visitor arrivals (UNWTO or tourism authority); proportion of accommodation capacity in accounting area; published activity participation rates; average length of stay by accommodation type |
| Budget | < USD 5,000 |
| Time | 1–3 months |
| CV | > 50% — relies on transferred participation rates; no site-specific validation |

#### Tier 2: On-Site Surveys, Operator Records, and Seasonal Stratification

**Method:** Combine dive/snorkel operator trip records with structured visitor intercept surveys at accommodation sites. Surveys capture activity participation (count per visitor), reef-related proportion of stay (φ = N_eco / N_total), and seasonal patterns. Stratify by accommodation type (resort, guesthouse) and season.

| Attribute | Detail |
|---|---|
| Physical output | Reef activity trips/yr and coral-related visitor-nights, by visitor segment and season |
| Key source | ENDhERI (2025), Section 6.6.1, Tables 6.27–6.28 — 53,250 coral-related visitor-nights; 15 activity types catalogued |
| Supporting sources | GOAP RNF BCAF (2025) — P × Q method across 9 ecotourism sites with operator/booking platform/planning document triangulation |
| Data inputs | On-site structured visitor survey; dive/snorkel centre trip records; resort/guesthouse visitor statistics; activity catalogue with per-unit participation; seasonal sampling (min wet + dry) |
| Budget | USD 15,000–50,000 |
| Time | 3–12 months |
| CV | 20–40% — direct activity fees measured accurately; seasonal and segment stratification reduces bias |

#### Tier 3: Spatially Explicit Visitor Tracking and Reef-Site Attribution

**Method:** Deploy automated visitor counting infrastructure (GPS loggers, camera traps at dive/snorkel entry points, vessel AIS tracking) to produce continuous, spatially referenced visitor trip data at the individual reef site level. Link site-level trip counts to reef condition data from monitoring programmes, producing a spatially explicit map of where recreation service is delivered and at what intensity.

| Attribute | Detail |
|---|---|
| Physical output | Visitor-trips/yr attributed to specific reef sites, with temporal resolution (weekly/monthly) and condition linkage |
| Key source | TNC, *Mapping Ocean Wealth*, 2017 — spatially explicit reef service mapping. URL: oceanwealth.org |
| Supporting sources | USAID Coral Triangle Support Partnership (2012) — spatial visitor flow models for reef destinations |
| | UNEP-WCMC, *The Tourism Value of Coral Reefs in South East Asia*, 2018 — reef condition layers linked to visitation patterns |
| Data inputs | GPS loggers / camera traps at entry points; vessel tracking (AIS); reef condition per site (coral cover, fish biomass, structural complexity); automated counters; multi-year continuous time series |
| Budget | > USD 100,000 |
| Time | > 12 months |
| CV | < 20% — continuous automated data eliminates recall bias and seasonal undercounting |

---

### 10.2 Mangrove Recreation — Trips (trips/yr)

#### Tier 1: Single-Operator Direct Count

**Method:** Obtain trip counts, group sizes, and frequency directly from the sole or primary operator. In many SIDS, mangrove tourism is operated by a single entity. Where no operator exists, record physical site attributes (accessibility, proximity to accommodation, biodiversity) as a baseline.

| Attribute | Detail |
|---|---|
| Physical output | Trips/yr, participants/yr — from direct operator records |
| Key source | ENDhERI (2025), Section 6.6.2 — Hithadhoo Mangrove Adventures: ~120 participants/yr, 10 tourists/month |
| Supporting sources | IUCN, *Mangroves for the Future Toolkit* (MFF programme), 2013–2018 — community ecotourism monitoring templates |
| | SPTO, *Pacific Sustainable Tourism Standard*, 2019 — nature-based activity indicators |
| Data inputs | Operator trip records; group sizes; per-trip fee; site classification (established / nascent / absent) |
| Budget | < USD 5,000 |
| Time | 1–3 months |
| CV | > 50% for nascent operations — single-operator, single-year data subject to idiosyncratic variation |

#### Tier 2: Multi-Operator Census with Structured Counts

**Method:** Conduct a census of all tourism operators offering mangrove-based activities. Implement structured visitor counts at multiple sites. Stratify by season and triangulate activity data from operator interviews, booking platforms, and planning documents.

| Attribute | Detail |
|---|---|
| Physical output | Trips/yr across all sites, by activity type and season |
| Key source | GOAP RNF BCAF (2025) — 9 ecotourism sites across 4 districts, ~11,000 annual visitors, triangulated from 3 data sources |
| Supporting sources | IUCN, *Tourism in Protected Areas: Guidelines* (Leung et al., 2018) — structured visitor counting protocols |
| Data inputs | Census of all operators at all mangrove sites; structured visitor counts with seasonal sampling; activity catalogue per site; multi-year data where available for averaging |
| Budget | USD 10,000–50,000 |
| Time | 3–12 months |
| CV | 20–50% — multi-site; seasonal variation captured |

#### Tier 3: Automated Visitor Monitoring with Demand Modelling

**Method:** Deploy automated counting infrastructure (trail counters, camera traps at boardwalk entries, vessel monitoring) for continuous visitor measurement. Combine with spatial analysis of site attributes (accessibility, biodiversity, proximity to accommodation) to model visitor demand as a function of ecosystem characteristics and supply conditions.

| Attribute | Detail |
|---|---|
| Physical output | Continuous visitor-trips/yr with temporal resolution; demand model predicting trips under different site-condition scenarios |
| Key source | SPC, *Community-Based Ecotourism Monitoring Toolkit* — automated counter protocols for Pacific Island protected areas |
| Supporting sources | World Bank, *Valuing Ecosystem Services from Mangroves*, 2015–2022 — demand function methodology |
| Data inputs | Automated trail counters / camera traps / vessel monitoring; periodic intercept surveys for calibration; site attribute data (accessibility, biodiversity, condition); multi-year continuous time series |
| Budget | > USD 50,000 |
| Time | > 12 months |
| CV | < 20% — continuous automated data eliminates single-operator and seasonal bias |

---

### 10.3 Seagrass Gleaning — Effort (hours/yr) and Harvest (kg/yr)

#### Tier 1: Household Survey Extrapolation

**Method:** Extract gleaning activity data from existing national household surveys — HIES (Household Income and Expenditure Survey) in Pacific, or census livelihood modules. Identify proportion of households reporting gleaning, estimate frequency, and extrapolate to population.

| Attribute | Detail |
|---|---|
| Physical output | Estimated gleaners, total effort (hours/yr), and harvest (kg/yr) — indicative |
| Key source | SPC, *Household Income and Expenditure Survey (HIES) Technical Guidelines and Country Reports* (various Pacific Island rounds, 2019–2023). URL: spc.int/statistics |
| Supporting sources | ENDhERI (2025), Section 6.6.3 — Rees et al. (2021) identified 227 gleaners (1.35% of Laamu population); extrapolated to 1,440 participants and 3,960 hours/yr |
| | SPC, *A New Song for Coastal Fisheries — The Noumea Strategy*, 2015 |
| Data inputs | National HIES or census data with livelihood module; population census for accounting area; published gleaning participation and time-use rates from comparable contexts |
| Budget | < USD 5,000 |
| Time | 1–3 months |
| CV | > 50% — relies on secondary surveys not designed for gleaning measurement |

#### Tier 2: Dedicated Gleaning Surveys and Community-Based Monitoring

**Method:** Purpose-designed gleaning surveys or community-based monitoring logbooks where gleaners record trips, duration, species, and harvest. Stratify by season (tidal cycles, monsoon) and seagrass condition. Requires female enumerators, local-language instruments, and gender-sensitive protocols.

| Attribute | Detail |
|---|---|
| Physical output | Gleaners, effort (hours/yr), harvest (kg/yr) by species — site-specific |
| Key source | ENDhERI (2025), Section 6.6.3 — McGowan (2023) dedicated survey: 7.9 days/month, 2.7 hr/trip, group size 4.5 |
| Supporting sources | WorldFish/SPC, *Community-Based Fisheries Monitoring* programmes — logbook systems with pictorial species ID sheets and stipends |
| | WorldFish/FAO/World Bank, *Hidden Harvest* (2nd ed.), 2023 — methodologies for estimating unreported subsistence harvest |
| Data inputs | Dedicated gleaning survey instrument; community logbooks (waterproof data cards); seasonal sampling; seagrass condition for stratification; calibration exercises (informal units → kg); female enumerators |
| Budget | USD 8,000–25,000 |
| Time | 3–12 months |
| CV | 20–50% — direct measurement; self-report discrepancies of 20–50% vs observer-verified catches |

#### Tier 3: Biophysical Production Model Linked to Condition Account

**Method:** Link seagrass condition monitoring data (SEQI or equivalent) to invertebrate productivity through biophysical production models, combined with detailed household time-use surveys. Produces condition-dependent sustainable yield estimate alongside empirical harvest measurement.

| Attribute | Detail |
|---|---|
| Physical output | Potential supply (kg/yr invertebrate production by condition class) + actual demand (hours/yr effort, kg/yr harvest) |
| Key source | ENDhERI (2025), Sections 5 + 6.6.3 combined — SEQI condition data (0.571–0.715) + gleaning survey |
| Supporting sources | WorldFish/SPC, Pacific invertebrate fisheries studies — species-specific stock-recruitment relationships as function of habitat quality |
| | SPC, *Invertebrate Fisheries and Gleaning in the Pacific Islands* technical bulletins |
| Data inputs | Seagrass condition monitoring (SEQI, spatially explicit, sub-annual); invertebrate density/biomass per condition class; biophysical production function parameters; household time-use survey; species-specific harvest per trip (calibrated vs observer); multi-season sampling |
| Budget | > USD 50,000 |
| Time | > 12 months |
| CV | < 20% with adequate sampling — explicitly links condition account to service account, capturing the condition-service feedback that Tiers 1–2 miss |

---

## 12. Expert Review: Cultural Ecosystem Service Accounts

**Reviewer expertise:** Tourism economics, cultural ecosystem service valuation, SIDS contexts
**Scope:** Service-by-service assessment of feasibility, accuracy, and difficulty, with tiered ratings and actionable recommendations

---

### 10.1 Coral Reef Recreation

#### Feasibility — Tier 2 (Moderate)

Resort visitor statistics are typically obtainable in countries where tourism is formally regulated (resorts report bed-nights to national tourism authorities). Guesthouse statistics are less consistently collected, particularly where informal operators exist outside the licensing system.

Dive centre data sharing is feasible but depends on operator willingness. In consolidated tourism markets (a single resort controlling dive operations), data may be commercially sensitive. In dispersed markets, compiling a complete census of trip counts requires sustained relationship-building. Expect 60–80% coverage from formal operators; informal snorkel excursions will be systematically undercounted.

Tourist expenditure and motivation surveys are the most resource-intensive requirement. A statistically valid intercept survey requires trained enumerators, translated instruments (at minimum English, Mandarin, and relevant regional languages), sampling frames stratified by accommodation type and season, and 4–8 weeks of fieldwork. Budget estimate: USD 15,000–40,000 for a single-round survey in a small atoll context.

#### Accuracy — Tier 2 (Moderate, with specific weaknesses)

The accommodation allocation step (Step 4) is the single largest source of methodological uncertainty. The question "How important were reef activities in your destination choice?" conflates several distinct behavioural concepts: (a) reef as a necessary condition for destination choice, (b) reef as an enhancement, and (c) reef as one attraction among many. Depending on question framing, the attribution proportion can range from 20% to 70% for the same population.

Specific biases in tourist motivation surveys include:

- **Hypothetical bias:** Tourists asked retrospectively tend to over-attribute importance to activities they enjoyed.
- **Social desirability bias:** In destinations marketed around marine conservation, tourists may overstate reef importance.
- **Segment non-response:** Budget tourists and domestic visitors are systematically harder to survey. If the allocation proportion is derived mainly from resort guests, the result will be biased upward.
- **Sensitivity:** A 10 percentage point shift in the allocation proportion (e.g., 44% to 34%) changes the total by several million USD. The final figure is more sensitive to this single parameter than to any other input.

Direct activity fees (dive and snorkel excursion fees, equipment rental) are measured with high accuracy because they come from transaction records.

#### Difficulty — Tier 2 (Moderate)

The core difficulty lies in survey design and execution. Designing a defensible motivation survey requires psychometric expertise or adoption of a validated instrument (e.g., Uyarra et al. 2009, Spalding et al. 2017). Seasonal variation is a real concern: in monsoon-affected SIDS, participation rates can drop 50–70% in the wet season.

#### Recommendations

1. **Lower-bound approach when accommodation allocation data is unavailable.** Report direct reef activity spending (dive fees + snorkel fees + equipment rental) as the conservative lower bound. This requires no survey and uses transaction data. The underestimate is transparent and can be clearly communicated to policymakers.
2. **Standardised survey instrument.** Adopt an existing validated instrument (Spalding et al. 2017 "reef-adjacent value" methodology; World Bank WAVES coral reef valuation toolkit) rather than designing bespoke.
3. **Sensitivity reporting.** Always report the total value at three allocation proportions (survey-derived estimate, plus/minus 10 percentage points).
4. **Alternative methods.** The travel cost method (TCM) avoids the accommodation allocation problem entirely but requires a different survey instrument and econometric capacity. Choice experiments are most informative but reserve for sites where tourism revenue exceeds USD 10M/yr. Contingent valuation is appropriate only when the policy question involves non-marginal changes to reef condition.
5. **Handling informal operators.** Conduct a rapid enumeration (count of operators, estimated trips per week) and apply average fee data from formal operators. Flag separately.

| Rating Dimension | Tier | Justification |
|---|---|---|
| Feasibility | 2 | Resort data accessible; guesthouse data patchy; survey logistics substantial |
| Accuracy | 2 | Direct fees accurate; accommodation allocation highly sensitive to survey design |
| Difficulty | 2 | Requires survey expertise, operator coordination, seasonal stratification |

---

### 10.2 Mangrove Recreation

#### Feasibility — Tier 1 (High, but often trivially so)

The calculation is straightforward: trips x group size x fee. In many SIDS contexts, mangrove-based tourism is operated by a single entity. Obtaining the data requires a single conversation with the operator. This makes data collection trivial but raises the question of whether formalising this into an ecosystem service account is proportionate.

#### Accuracy — Tier 3 (Low)

Single-operator data generates several accuracy problems. The value reflects the business model of one enterprise, not the ecosystem's capacity to supply recreational services. A single operator's trip count in one year is subject to idiosyncratic variation (staff illness, boat breakdown, marketing effort). Low sample sizes mean confidence intervals are wide.

There is a fundamental measurement problem with nascent ecotourism: the observed expenditure captures realised demand conditional on current supply. Latent demand — what tourists would pay if tours were regularly offered — is invisible in the direct expenditure approach. This means the SOP will systematically produce near-zero values in many SIDS contexts, even where the ecosystem has genuine recreational potential.

#### Difficulty — Tier 1 (Low)

The arithmetic is elementary. The difficulty is not in the calculation but in interpreting and communicating a result that may be misleadingly low.

#### Recommendations

1. **Threshold for inclusion vs. notation as negligible.** If the mangrove recreation value is less than 0.1% of the total cultural service value and is based on a single operator, record it in the physical and monetary accounts but flag explicitly as "nascent activity — value reflects current supply constraints, not ecosystem potential."
2. **Nascent vs. established classification.** Add a classification field to the supply table:
   - **Established:** Multiple operators, regular schedule, marketed activity, multi-year data.
   - **Nascent:** Single operator or irregular activity, <100 trips/yr, <2 years of data.
   - **Absent:** No commercial tourism currently operating, but ecosystem suitable.
3. **Recording future potential.** Where an ecosystem has recreational attributes (accessible mangrove, proximity to accommodation, biodiversity) but minimal tourism, record the physical attributes in a supplementary note as a basis for future valuation.
4. **When to invest in sophisticated valuation.** If the policy question concerns whether to develop or protect a mangrove site for tourism, a contingent valuation or choice experiment (USD 5,000–15,000) produces a demand estimate independent of current supply. Use only when an active policy decision is at stake.
5. **Multi-year averaging.** Where data is available for more than one year, report the average to smooth idiosyncratic variation.

| Rating Dimension | Tier | Justification |
|---|---|---|
| Feasibility | 1 | Data collection trivial for single-operator contexts |
| Accuracy | 3 | Single-operator, single-year data; does not reflect ecosystem potential |
| Difficulty | 1 | Calculation elementary; interpretation is the real challenge |

---

### 10.3 Seagrass Gleaning

#### Feasibility — Tier 3 (Low)

Gleaner surveys are among the most challenging socioeconomic data collection tasks in coastal ecosystem accounting. The target population — predominantly women engaged in informal, unregistered, subsistence-oriented harvesting — is not captured in any administrative dataset. Everything must come from primary surveys.

Building trust takes time. Gleaners may underreport activity (fear of harvesting restrictions; social stigma) or overreport (perception that demonstrating reliance may attract assistance). Effort estimation is inherently imprecise — gleaning follows tidal cycles, weather, and household needs, and gleaners rarely track hours. Harvest estimation is equally challenging: quantities are described in informal units (buckets, bags, handfuls) requiring calibration exercises. Species identification may not match scientific taxonomy.

Practical logistics: survey teams need female enumerators, surveys in local languages, visits timed to gleaning activity (early morning, specific tidal windows), and multiple visits for adequate sample sizes. Budget estimate: USD 8,000–25,000 for a single-round survey covering 100–300 gleaners across multiple islands.

#### Accuracy — Tier 2 (Moderate, with conceptual concerns)

**Double-counting risk.** Adding wage value and harvest value assumes gleaning labour and output are independent contributions. But the wage value is the opportunity cost of time, while the harvest is the product of that same time. The true economic value may be the greater of (wage value, harvest value), not the sum. The SEEA EA permits this additive approach as a convention, but it produces an upper-bound estimate. For subsistence activities where no real alternative employment exists (common in remote atolls), the opportunity cost wage rate overstates actual forgone income.

**Wage rate selection.** Using the minimum wage as a proxy is standard but problematic in SIDS labour markets. In many outer-atoll contexts, formal employment is scarce and the minimum wage does not reflect actual earning opportunities. Using the actual median wage of women in the accounting area would be more accurate.

**Market prices for subsistence species.** Many gleaned species are consumed within the household and never enter a market. Applying market prices to species that are not sold overstates the monetary value. Conversely, in communities with informal trading, market prices may understate social value.

**Self-report reliability.** Studies comparing self-reports with observer-verified catches in artisanal fisheries find discrepancies of 20–50%. Acceptable for routine accounting, but insufficient for high-stakes policy decisions.

#### Difficulty — Tier 3 (High)

This is the most socially complex service to measure. It requires:

- **Social science survey design:** Questionnaire construction, sampling strategy for hard-to-reach populations, enumerator training, ethical review.
- **Gender-sensitive methodology:** Female enumerators, awareness of intra-household dynamics, timing around women's domestic schedules.
- **Cultural competence:** Understanding local norms, building community trust, respecting indigenous knowledge.
- **Language:** Surveys in local languages with translation and back-translation of instruments.
- **Access:** Remote atoll communities require boat transport, accommodation, and substantial logistical planning.

#### Recommendations

1. **Community-based monitoring as an alternative to external surveys.** Train community members (ideally women who are gleaners or trusted figures) to maintain simple logbooks: gleaning trips, duration, species collected. Provide waterproof data cards, pictorial species ID sheets, and a small stipend. This produces longitudinal data at lower per-observation cost and builds community ownership. After the first year, data quality typically exceeds one-off recall surveys. Successfully implemented in Pacific Island fisheries monitoring (SPC programmes).

2. **Valuing what monetary methods miss.** Add a qualitative assessment component. At minimum, record alongside the monetary account:
   - Gleaner participation rate (proportion of adult women in community)
   - Intergenerational transfer indicator (gleaning knowledge being transmitted: yes/declining/no)
   - Food security function (year-round / seasonal supplement / occasional)
   - Community self-assessment of importance (focus group rating: essential / important / marginal)
   These require minimal additional data (one focus group per community, 1–2 hours) and prevent the monetary figure from being dismissed as trivially small when cultural and food-security functions are significant.

3. **Gender mainstreaming in data collection.** Require that all gleaner surveys:
   - Use female lead enumerators
   - Conduct interviews individually or in women-only groups
   - Record and report results disaggregated by gender
   - Include a question on whether gleaning income is controlled by the gleaner or pooled into household income
   - Schedule interviews around women's availability

4. **Addressing the double-counting concern.** Report three figures:
   - **(a) Harvest value only** (market value of catch) — most conservative
   - **(b) Wage value only** (hours x wage rate) — opportunity cost interpretation
   - **(c) Combined total** (wage + harvest, as in current SOP) — upper bound, consistent with SEEA EA convention
   Reporting all three allows account users to select the figure most appropriate to their policy question.

5. **Handling species with no market price.** For species consumed within the household, use the price of the nearest market substitute (e.g., cheapest market protein source available locally). For species with no food value (decorative shells, cultural items), exclude from monetary value but record in the physical account and qualitative assessment.

| Rating Dimension | Tier | Justification |
|---|---|---|
| Feasibility | 3 | No administrative data; primary surveys of hard-to-reach population required |
| Accuracy | 2 | Mixed valuation conceptually sound but double-counting risk; self-reports moderate |
| Difficulty | 3 | Social science skills, gender sensitivity, language, access, community trust required |

---

### 10.4 Summary Tier Ratings

| Service | Feasibility | Accuracy | Difficulty |
|---|---|---|---|
| Coral reef recreation | Tier 2 | Tier 2 | Tier 2 |
| Mangrove recreation | Tier 1 | Tier 3 | Tier 1 |
| Seagrass gleaning | Tier 3 | Tier 2 | Tier 3 |

**Interpretation:** Tier 1 = low barrier / high confidence; Tier 2 = moderate; Tier 3 = high barrier / low confidence.

Coral reef recreation is the most consequential by value and methodologically balanced across all dimensions. Mangrove recreation is trivially easy to calculate but produces the least informative result. Seagrass gleaning is the most challenging to measure but captures dimensions of ecosystem value (gender equity, food security, cultural identity) that the other two services do not.

---

### 10.5 Cross-Cutting Observations

1. **Value disparity context.** In the Laamu example, coral reef recreation (USD 30.43M/yr) exceeds mangrove recreation (USD 2,400/yr) by a factor of approximately 12,700. This reflects genuine economic structure, not data quality problems. However, presenting these values side-by-side without context risks marginalising mangrove and seagrass cultural services in policy decisions. The supply table should include a narrative explaining that monetary value and ecological or social importance are not synonymous.

2. **Temporal mismatch.** Coral reef recreation data can be compiled from annual administrative records. Mangrove recreation requires operator contact. Seagrass gleaning requires primary fieldwork. The three services will typically have different data vintages. Recommend reporting all three for the same reference year, using interpolation or extrapolation where necessary.

3. **Missing condition-service linkage.** The skill file does not describe how changes in ecosystem condition (e.g., coral bleaching reducing reef attractiveness, seagrass loss reducing gleaning productivity) should feed back into cultural service values. The direct expenditure approach will not capture value loss from condition decline until tourist numbers actually decline, which may lag by several years. A note on prospective valuation methods (stated preference) for capturing condition-dependent value changes would strengthen the skill file.

4. **Valuation type labelling.** The SOP correctly labels each value type (market-based, imputed, mixed) and the supply table template enforces this. This is a strength of the current design.
