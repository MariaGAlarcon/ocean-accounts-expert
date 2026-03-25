# Skill: Provisioning Ecosystem Service Accounts

**Purpose:** Quantify the physical supply and monetary value of provisioning ecosystem services — wild fish provisioning and wood provisioning — following the SEEA EA framework and CICES classification.

**Framework:** UN SEEA EA Ecosystem Service Accounts (Section 6.1)
**CICES Category:** Provisioning services
**Services covered:**
1. Wild fish provisioning
2. Wood provisioning (fuel wood from mangroves)

---

## 1. Pipeline Overview

```
┌─────────────────────────────────────────────────────────────────────────┐
│                        DATA INGESTION LAYER                            │
│                                                                        │
│  Fisheries Data              Socioeconomic Data       Reference Data   │
│  ┌──────────────┐           ┌───────────────┐         ┌─────────────┐  │
│  │ Agency catch  │           │ Fisher surveys│         │ Species–    │  │
│  │ records       │           │ (effort, cost)│         │ habitat     │  │
│  │ (landings by  │           │               │         │ association │  │
│  │ species/gear) │           │ Market prices │         │ literature  │  │
│  └──────┬───────┘           └──────┬────────┘         └──────┬──────┘  │
│         │                          │                         │         │
└─────────┼──────────────────────────┼─────────────────────────┼─────────┘
          │                          │                         │
          ▼                          ▼                         ▼
┌─────────────────────────────────────────────────────────────────────────┐
│                      PREPROCESSING LAYER                               │
│                                                                        │
│  • Validate catch records (species IDs, weights, dates)                │
│  • Standardise units (all catch to kg/yr)                              │
│  • Reconcile agency data with fisher survey supplements                │
│  • Classify species by habitat association (reef, seagrass, pelagic)   │
│  • Validate species–habitat assignments with local fisher knowledge    │
│  • Disaggregate catch by gear type                                     │
│                                                                        │
└──────────────────────────────┬──────────────────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────────────────┐
│              PHYSICAL ACCOUNT LAYER (Part A)                           │
│                                                                        │
│  Total annual catch (kg/yr) disaggregated by:                          │
│  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐        │
│  │ Ecosystem type  │  │ Gear type       │  │ Species group   │        │
│  │ • Coral reef    │  │ • Pole-and-line │  │ • Reef fish     │        │
│  │ • Seagrass      │  │ • Handline      │  │ • Seagrass spp  │        │
│  │ • Pelagic       │  │ • Net           │  │ • Pelagic spp   │        │
│  └─────────────────┘  │ • Other         │  └─────────────────┘        │
│                        └─────────────────┘                             │
│  + Spatial map of fishing effort distribution                          │
│                                                                        │
└──────────────────────────────┬──────────────────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────────────────┐
│             MONETARY VALUATION LAYER (Part B)                          │
│                                                                        │
│  Resource Rent Method:                                                 │
│  ┌───────────────────────────────────────────────────────────────┐     │
│  │                                                               │     │
│  │  Gross Revenue = Σ (Catch_species × Market Price_species)     │     │
│  │                                                               │     │
│  │  Total Costs = Labour + Capital + Fuel + Equipment            │     │
│  │                                                               │     │
│  │  Resource Rent = Gross Revenue − Total Costs                  │     │
│  │                                                               │     │
│  │  → Positive = ecosystem economic contribution                 │     │
│  │  → Negative = costs exceed revenue                            │     │
│  │                                                               │     │
│  └───────────────────────────────────────────────────────────────┘     │
│  Value type: Market-based                                              │
│                                                                        │
└──────────────────────────────┬──────────────────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────────────────┐
│             SUPPLY AND USE TABLE COMPILATION                           │
│                                                                        │
│  Physical supply table: catch (kg/yr) by ecosystem type                │
│  Monetary supply table: resource rent by ecosystem type                │
│  Use table: fisheries sector, subsistence households                   │
│                                                                        │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## 2. Data Ingestion

### 2.1 Fisheries Data

| Source | Records | Key Fields |
|---|---|---|
| National or regional fisheries agency catch records | Official landings by species and gear type | Species, weight (kg), gear type, date, landing site |
| Local fisher surveys | Supplementary catch, effort, and cost data | Species, weight (kg), effort (hours/trips), costs by category |

### 2.2 Socioeconomic Data

| Source | Purpose | Key Fields |
|---|---|---|
| Fisher cost surveys | Input costs for resource rent | Labour wages, fuel, gear replacement, vessel depreciation |
| Market price data | Revenue calculation | Price per kg by species group (local currency) |
| National statistical office | Exchange rates, economic context | Currency conversion, inflation indices |

### 2.3 Reference Data

| Source | Purpose |
|---|---|
| Scientific literature (species–habitat associations) | Allocate catch to ecosystem type |
| Local fisher knowledge | Validate habitat allocations and supplement spatial effort data |

---

## 3. SOP: Wild Fish Provisioning

### Part A: Physical Measurement

```
Step 1: Compile total annual catch
    │
    ├── Obtain fisheries agency catch records for the accounting area
    ├── Supplement with catch estimates from local fisher surveys
    ├── Reconcile data sources (avoid double-counting)
    └── Express as total annual landed catch (kg/yr)
         Example (Laamu Atoll, Maldives): 61,228 kg/yr

Step 2: Disaggregate catch by ecosystem association
    │
    ├── Classify each fish species/group:
    │     ├── Coral reef-associated
    │     ├── Seagrass-associated
    │     └── Pelagic (not attributed to specific benthic ecosystem)
    ├── Use species–habitat associations from scientific literature
    ├── Validate with local fisher knowledge
    └── Allocate catch weight (kg) to each ecosystem type

Step 3: Disaggregate by gear type
    │
    ├── Record gear type for each catch component
    │     ├── Pole-and-line
    │     ├── Handline
    │     ├── Net
    │     └── Other
    └── Compile into supply and use table format:
         catch × species group × ecosystem × gear type

Step 4: Map fishing effort
    │
    ├── Record spatial distribution of fishing effort
    └── Produce spatial map of fishing effort across accounting area
```

**Physical account output:**

```
┌─────────────────────────────────────────────────────────────┐
│  PHYSICAL SUPPLY TABLE: Wild Fish Provisioning              │
│                                                             │
│  ┌─────────────────┬────────────┬────────────┬───────────┐  │
│  │ Species Group   │ Coral Reef │ Seagrass   │ Pelagic   │  │
│  │                 │ (kg/yr)    │ (kg/yr)    │ (kg/yr)   │  │
│  ├─────────────────┼────────────┼────────────┼───────────┤  │
│  │ [Group 1]       │ [value]    │ [value]    │ [value]   │  │
│  │ [Group 2]       │ [value]    │ [value]    │ [value]   │  │
│  │ ...             │ ...        │ ...        │ ...       │  │
│  ├─────────────────┼────────────┼────────────┼───────────┤  │
│  │ Total           │ [total]    │ [total]    │ [total]   │  │
│  └─────────────────┴────────────┴────────────┴───────────┘  │
│                                                             │
│  USE TABLE:                                                 │
│  ┌─────────────────────────┬───────────────────────────┐    │
│  │ User / Beneficiary      │ Allocation                │    │
│  ├─────────────────────────┼───────────────────────────┤    │
│  │ Fisheries sector        │ Commercial catch          │    │
│  │ Subsistence households  │ Non-market catch          │    │
│  └─────────────────────────┴───────────────────────────┘    │
└─────────────────────────────────────────────────────────────┘
```

---

### Part B: Economic Valuation — Resource Rent Method

> **Value type: Market-based.** Resource rent isolates the ecosystem's contribution to fishery revenue using observed market prices and costs.

```
Step 5: Calculate gross revenue
    │
    ├── For each species group:
    │     Revenue_species = Catch_species (kg) × Market Price_species (currency/kg)
    └── Gross Revenue = Σ Revenue_species

Step 6: Calculate total fishing costs
    │
    ├── Labour costs (crew wages + fisher opportunity costs)
    ├── Capital costs (vessel depreciation + gear replacement)
    ├── Fuel costs
    └── Equipment and maintenance costs

Step 7: Calculate resource rent
    │
    ├── Resource Rent = Gross Revenue − Total Costs
    │
    ├── Positive value → ecosystem's economic contribution ("nature premium")
    └── Negative value → fishing costs exceed revenue
         Example (Laamu Atoll, Maldives): −3,636,324 MVR
```

**Resource rent formula:**

```
                                                     n
Resource Rent = Gross Revenue − Total Costs = [ Σ (C_i × P_i) ] − [L + K + F + E]
                                                    i=1

Where:
  C_i = catch of species group i (kg)
  P_i = market price of species group i (local currency/kg)
  L   = labour costs
  K   = capital costs (depreciation)
  F   = fuel costs
  E   = equipment and maintenance costs
```

**NCAVES formal decomposition (Chapter 3):** The full NCAVES resource rent formula decomposes costs more precisely as:
```
Resource Rent = Total Revenue − Intermediate Inputs − Compensation of Employees
                − Consumption of Fixed Capital − Return on Produced Assets

Where:
  Return on Produced Assets = Value of produced capital × appropriate rate of return
```
A negative residual implies zero ecosystem service value — the ecosystem still provides its function but the economic activity is unprofitable (NCAVES Chapter 3, Chunk 8). The resource rent method is NCAVES Category III and is classified as Tier 1 or 2 depending on data specificity.

### Alternative: Five-Component Cost Structure with WACC (RNF BCAF)

**When to use:** Where detailed cost decomposition is available or can be estimated, particularly for crustacean fisheries or small-scale artisanal fisheries where standard cost surveys have low response rates.

```
Step 5a: Gross Output Value
    │
    └── Catch volume × first-sale prices (by species, by size grade)

Step 6a: Detailed cost components
    │
    ├── (i)  Operational expenses: consumables, fuel (litres × price),
    │        maintenance, repairs
    │        → Source: advertised prices online for consumable costs
    │
    ├── (ii) Labour costs: alternative comparative wages from dominant
    │        local sector (e.g., agriculture) when direct fisher wage
    │        survey data is unavailable
    │        → Source: regional agricultural wage rates as proxy
    │
    └── (iii) Capital costs: vessel depreciation + gear depreciation +
              return on fixed capital using WACC
              → WACC = weighted-average cost of capital reflecting
                national financial conditions (e.g., 9% for Indonesia)

Step 7a: Resource Rent = Gross Output − (Operational + Labour + Capital)
```

**Survey coverage calibration:** Where landing surveys cover only a fraction of total fishing trips, calibrate survey coverage by comparing catch volumes against provincial/regional statistics to derive an extrapolation factor.

> **RNF BCAF example (Central Java):** Blue swimmer crabs (*Portunus pelagicus*) and mud crabs (*Scylla serrata*) were surveyed over 20 months from 35 boats. Survey coverage was estimated at 1% of total fishing trips by comparison with Dinas Perikanan provincial statistics. The five-component cost structure yielded a positive resource rent of IDR 5.59 billion annually for Demak — contrasting with the negative rent (-3,636,324 MVR) from the ENDhERI Maldives calculation, illustrating how the resource rent method is highly sensitive to cost estimation assumptions in artisanal fishery contexts. (Source: GOAP, 2025)

**Monetary account output:**

```
┌─────────────────────────────────────────────────────────────┐
│  MONETARY SUPPLY TABLE: Wild Fish Provisioning              │
│                                                             │
│  ┌──────────────────┬────────────┬──────────────────┐       │
│  │ Component        │ Value      │ Currency         │       │
│  ├──────────────────┼────────────┼──────────────────┤       │
│  │ Gross Revenue    │ [value]    │ local currency   │       │
│  │ − Labour costs   │ [value]    │ local currency   │       │
│  │ − Capital costs  │ [value]    │ local currency   │       │
│  │ − Fuel costs     │ [value]    │ local currency   │       │
│  │ − Equipment      │ [value]    │ local currency   │       │
│  ├──────────────────┼────────────┼──────────────────┤       │
│  │ Resource Rent    │ [value]    │ local currency   │       │
│  └──────────────────┴────────────┴──────────────────┘       │
│                                                             │
│  Value type: Market-based                                   │
└─────────────────────────────────────────────────────────────┘
```

### Tiered Monetary Valuation Methods (NCAVES/MAIA)

This section provides alternative monetary valuation methods at three tiers aligned with the NCAVES/MAIA (2022) five-category typology. The primary method (resource rent) is described above.

#### Monetary Tier 1: Value Transfer from Published Resource Rent Estimates

**Method:** Apply published per-kg resource rent values from comparable fisheries contexts, adjusted for local price and income levels using PPP income adjustment: V_local = V_study × (Y_local/Y_study)^e, where e is income elasticity. Source values from the ESVD or regional fisheries economics literature.

| Attribute | Detail |
|---|---|
| NCAVES Category | III (prices embodied in market transactions) — transferred |
| Monetary output | Resource rent (local currency/yr) — indicative |
| Key source | ESVD (de Groot et al. 2020) — median food provisioning values by biome; World Bank, *The Sunken Billions Revisited* (2017) — fisheries rent by ocean basin |
| Data inputs | Published resource rent per kg from comparable context; local market prices for income adjustment; catch data from physical account |
| Accuracy note | Average value transfer errors ~40% (Kaul et al. 2013); acceptable for initial accounts |

#### Monetary Tier 2: Resource Rent with Domestic Cost Data

**Method:** As described in Part B above (4-component or 5-component with WACC). Uses domestically sourced cost data (fisher surveys, national fisheries statistics, regional wage data).

#### Monetary Tier 3: Full Production Account with Site-Specific Data

**Method:** Detailed farm-level (vessel-level) production accounts following the NCAVES formal decomposition: Total Revenue − Intermediate Inputs − Compensation of Employees − Consumption of Fixed Capital − Return on Produced Assets. Requires individual vessel-level cost surveys, accurate capital stock valuation, and a defensible rate of return on produced capital. At this tier, ensure that subsidy-distorted prices are adjusted to approximate undistorted exchange values (NCAVES Chapter 3).

---

## 4. SOP: Wood Provisioning (Mangrove Fuel Wood)

**SEEA EA Section:** 6.1 (Provisioning)
**Providing ecosystems:** Mangroves
**Valuation method:** Substitute-cost (avoided cost of purchasing equivalent energy)
**Value type:** Non-market (cost-based proxy)
**When to include:** Where mangrove extent supports rural household energy use and fuel wood collection is a significant livelihood activity. Not applicable where mangrove extent is minimal (e.g., <20 ha) or where wood harvesting is not practised.

### Part A: Physical Measurement — Spatial Proxy Model

**When to use:** Where direct household survey data on fuel wood collection is unavailable. The model uses spatial and literature-derived parameters to estimate per-household extraction.

```
Step 1: Estimate per-household wood extraction (W_i)
    │
    │   W_i = D_base × f(d_i) × g(S_i) × h(A_i)
    │
    │   Where:
    │     D_base = baseline household demand (kg/yr)
    │              e.g., 2,496 kg/yr (Astana 2012, rural Java: 208 kg/month)
    │
    │     f(d_i) = accessibility index declining with Euclidean distance
    │              from household to nearest mangrove edge
    │              Maximum search distance: 1 km
    │              Distance elasticity: 0.8 (Heltberg et al. 2000)
    │              → 1% increase in distance = 0.8% reduction in collection
    │
    │     g(S_i) = accessible deadwood stock function
    │              Based on woody biomass and mangrove area within 1 km
    │              Use rate: 8% of standing stock
    │              (vs ~4% sustainable yield at 20-25 year rotation, Suman 2019)
    │
    │     h(A_i) = building footprint size as demand modifier
    │
    └── Calibrate for districts where mangroves remain relatively intact
        Exclude districts where mangroves have been converted to aquaculture

Step 2: Aggregate total collection
    │
    └── Sum W_i across all eligible households within 1 km of mangrove edge
```

### Part B: Economic Valuation — Substitute-Cost Approach

```
Step 3: Calculate avoided energy cost
    │
    ├── Convert air-dried wood to energy equivalent (MJ/kg)
    │   (exclude leaves and bark — sap and heartwood only)
    ├── Calculate equivalent LPG or kerosene energy cost
    └── Monetary value = total collection (kg/yr) × market price of biomass (currency/kg)

Step 4: Compile account
    │
    └── Present in supply and use table format
        SNA beneficiary: households (fuel wood collection)
```

> **RNF BCAF example (Central Java):** Total annual collection was estimated at 162,137 tonnes valued at IDR 2.92 billion in avoided fuel costs (Rp 18/kg market price). Model was calibrated for Cilacap and Kebumen; Jepara and Demak excluded due to mangrove conversion to aquaculture. Charcoal production via pyrolysis (~20% efficiency) generates additional value not captured. (Source: GOAP, 2025)

### Alternative Monetary Valuation: Resource Rent (Stumpage Value) — NCAVES Category I

**When to use:** Where mangrove wood is marketed (sold as timber, poles, or firewood in local markets) and stumpage value data exist. The NCAVES report identifies the resource rent method as the primary valuation approach for wood provisioning, based on stumpage value — the price of standing timber minus harvesting and transport costs (Chapter 4, Chunk 15).

```
Resource Rent (stumpage) = Market price of wood at point of sale
                          − Harvesting costs (labour, tools)
                          − Transport costs
```

This provides a market-based (Category I) exchange value. Where wood enters informal or subsistence economies without recorded market prices, the substitute-cost approach (described above) remains appropriate as a Category V method.

> **NCAVES reference:** "For timber, [the resource rent based on stumpage value] is well-established and data are typically available from forestry statistics. Non-wood forest products are more difficult because they often enter informal or subsistence economies without recorded market prices." (Chunk 15)

### Tiered Monetary Valuation Methods — Wood Provisioning (NCAVES/MAIA)

| Monetary Tier | Method | NCAVES Category | Data Requirement |
|---|---|---|---|
| Tier 1 | Value transfer: published per-kg fuelwood value from ESVD or regional forestry studies, adjusted for local prices | V (transferred) | Published unit values; local price index |
| Tier 2 | Substitute-cost (avoided energy cost) as described above | V (replacement cost) | Local fuelwood and LPG/kerosene prices; physical extraction estimate |
| Tier 3 | Resource rent (stumpage value) with detailed harvesting cost data | I (directly observed prices) | Timber market prices; detailed harvesting and transport cost surveys |

### Key Parameters

| Parameter | Value | Source |
|---|---|---|
| Baseline household demand | 2,496 kg/yr | Astana 2012 (rural Java) |
| Distance elasticity | 0.8 | Heltberg et al. 2000 (rural India) |
| Use rate of standing stock | 8% | Literature; higher than 4% sustainable yield (Suman 2019) |
| Maximum search distance | 1 km | Model parameter |
| Wood biomass market price | Site-specific (e.g., Rp 18/kg in Central Java) | Local market data |

---

## 5. Data Quality and Limitations

| Issue | Impact | Mitigation |
|---|---|---|
| Limited cost survey data / low response rates | Unreliable resource rent calculation | Increase survey effort; supplement with focus groups |
| Subsistence fishing (non-market catch) | Difficult to value at market prices | Record subsistence catch separately; note as data gap |
| Artisanal and informal labour arrangements | Poorly captured by standard resource rent | Use opportunity cost of labour; document assumptions |
| Species–habitat allocations from literature | May not reflect local conditions | Validate with local fishers; update with local ecological data |
| Temporal mismatch between catch records and accounting period | Misaligned physical account | Use records matching the accounting period; interpolate if necessary |

**Flag as data-deficient if cost data quality is insufficient for a credible resource rent estimate.**

| Wood provisioning: spatial proxy relies on literature-derived elasticity parameters | Model outputs sensitive to distance elasticity and use rate assumptions | Validate against local household surveys where feasible; conduct sensitivity analysis on key parameters |
| Wood provisioning: excludes charcoal production value | Underestimates total wood-derived value | Note additional value streams not captured; consider separate charcoal account |
| Wood provisioning: 8% use rate exceeds sustainable yield (4%) | Implies mangrove biomass reduction over time | Cross-reference with extent account change detection for consistency |

---

## 6. Key Parameters

| Parameter | Value | Source |
|---|---|---|
| Total annual catch | Site-specific (e.g., 61,228 kg/yr for Laamu Atoll) | Fisheries agency + fisher surveys |
| Market price per species group | Site-specific (local currency/kg) | Local market data |
| Labour cost | Site-specific | Fisher cost surveys |
| Capital cost (vessel depreciation) | Site-specific | Fisher cost surveys |
| Fuel cost | Site-specific | Fisher cost surveys |
| Equipment cost | Site-specific | Fisher cost surveys |
| Species–habitat allocation proportions | Literature + local validation | Scientific literature, fisher knowledge |

---

## 7. Implementation Checklist

- [ ] **Obtain** fisheries agency catch records for the accounting area and period
- [ ] **Conduct** or compile local fisher surveys for supplementary catch and cost data
- [ ] **Reconcile** agency records with fisher survey data; resolve discrepancies
- [ ] **Classify** all fish species/groups by ecosystem association (reef, seagrass, pelagic)
- [ ] **Validate** species–habitat allocations with local fisher knowledge
- [ ] **Disaggregate** catch by ecosystem type, gear type, and species group
- [ ] **Map** spatial distribution of fishing effort
- [ ] **Compile** physical supply table (kg/yr by ecosystem type)
- [ ] **Obtain** market prices for each species group
- [ ] **Calculate** gross revenue (catch × price by species)
- [ ] **Compile** fishing cost data (labour, capital, fuel, equipment)
- [ ] **Calculate** resource rent (gross revenue − total costs)
- [ ] **Compile** monetary supply and use tables
- [ ] **Assess** data quality; flag data-deficient components
- [ ] **Document** metadata: data sources, assumptions, limitations, accounting period

### Wood Provisioning (where applicable)
- [ ] **Assess** whether mangrove extent and local livelihoods support fuel wood collection
- [ ] **Obtain** baseline household demand parameter from literature or local surveys
- [ ] **Map** households within 1 km of mangrove edge using building footprint data
- [ ] **Calculate** accessibility index using distance from household to mangrove edge
- [ ] **Estimate** accessible deadwood stock from biomass data and mangrove area
- [ ] **Apply** spatial proxy model to estimate per-household extraction
- [ ] **Aggregate** total collection across all eligible households
- [ ] **Obtain** local biomass market price or LPG/kerosene equivalent energy cost
- [ ] **Calculate** monetary value using substitute-cost approach
- [ ] **Compile** physical and monetary supply and use tables
- [ ] **Document** districts excluded (e.g., converted to aquaculture) and additional value streams not captured (e.g., charcoal)

---

## 9. Tiered Assessment

### Overview

This skill implements physical measurement and monetary valuation for wild fish provisioning (the primary service) and wood provisioning (an extension). The current SOP implements Tier 2 approaches for most wild fish provisioning sub-procedures.

### Wild Fish Provisioning — Physical Measurement Tier Profile

Reference: Tiered Assessment Framework, Section 4 (Summary Assessment Matrix), wild fish provisioning rows.

| Tier | A: Feasibility | B: Accuracy | C: Difficulty | Description |
|---|---|---|---|---|
| Tier 1 | 1 | 1 | 1 | National catch statistics with global price data |
| Tier 2 | 2 | 2 | 2 | Spatially allocated catch with local market prices and ecosystem attribution |
| Tier 3 | 3 | 3 | 3 | Stock assessment models, fishery-independent surveys, ecosystem-based attribution |

| Sub-procedure | Tier 1 approach | Tier 2 approach | Tier 3 approach | Current tier (A / B / C) |
|---|---|---|---|---|
| Catch data compilation | National aggregate statistics | Landings by species/gear from fisheries agency records, validated against fisher surveys (this skill) | Fishery-independent trawl surveys + logbook data | A=1–2, B=2, C=1–2 |
| Spatial allocation of catch to ecosystems | Global literature habitat-dependence fractions | Species-habitat association literature combined with local habitat maps — LRR approach or literature fractions (this skill) | Acoustic telemetry, otolith microchemistry, or diel habitat use models | A=1–2, B=1–2, C=1–2 |
| Ecosystem attribution (habitat contribution factor) | Single global average fraction (e.g., 50% mangrove-dependent) | Species-specific literature LRR combined with local species composition data (this skill) | Controlled mark-recapture or habitat manipulation experiment | A=2, B=1–2, C=2 |
| Physical supply metric (tonnes/yr by ecosystem type) | Aggregate national total | Ecosystem-attributed tonnes/yr using habitat maps × contribution factor (this skill) | Spatially explicit production model | A=2, B=2, C=2 |

Current overall tier: **Tier 2** across A, B, C dimensions. Binding constraint on B-accuracy: habitat attribution factor derived from literature LRR values with high parameter uncertainty (CV typically >30%).

### Wild Fish Provisioning — Monetary Valuation Tier Profile

Reference: Tiered Assessment Framework, Section 4a (Monetary Valuation Tier Matrix), wild fish provisioning row.

| Monetary Tier | Description |
|---|---|
| Tier 1 | Value transfer from ESVD or published resource rent ratios; or simple catch × published average unit price |
| Tier 2 (current default) | Resource rent = landed value − fishing costs (domestic data); spatially allocated catch × local market price |
| Tier 3 | Full production account: total revenue − intermediate inputs − CoE − CFC − return on produced assets (NCAVES formal decomposition) |

Monetary dimension scores for Tier 2 (current):

| Dimension | Score | Rationale |
|---|---|---|
| A: Feasibility | 2 | Requires fisher surveys for cost data, market price collection; 1–6 months |
| B: Accuracy | 2 | Reflects local market conditions; CV 20–50%; transfer error minimal |
| B: Temporal consistency | 2 | Annual price updates from consistent market monitoring |
| C: Difficulty | 2 | Inter-agency coordination with fisheries agencies; fisher survey logistics |
| D: Exchange value consistency | 2 | Resource rent is an exchange value; consumer surplus excluded |

For Tier 3: requires full NCAVES-compliant production account decomposition; specialist econometric capacity and detailed cost-of-fishing data not yet available.

### Wood Provisioning — Indicative Tier Assessment

Wood provisioning from mangroves is not among the eight services in the framework's Summary Assessment Matrix but can be assessed using the same three-dimensional approach. Tier scores below are indicative.

| Approach | A | B | C | Notes |
|---|---|---|---|---|
| Literature fuelwood yield per ha × extent (Tier 1) | 1 | 1 | 1 | Global defaults applied to mangrove extent |
| Household survey of fuelwood collection (Tier 2) | 2 | 2 | 2 | Dedicated survey, local prices |
| Biophysical yield model + harvest survey (Tier 3) | 3 | 2–3 | 3 | Rarely applied in practice |

Current implementation: if using literature fuelwood yield rates, Tier 1 on B-accuracy. If using household survey data, Tier 2. Monetary valuation uses local fuelwood market prices × collected volume (an exchange value by definition).

### Double-Counting Note

Wild fish provisioning and fisheries nursery habitat share the same physical catch stock. The nursery service account measures the habitat-attributed contribution to fish biomass production — not an additional harvest on top of the catch. Ensure that the same tonnes of fish are not counted as provisioning output AND as nursery service output. The tiered assessment framework's double-counting caution (Section 4a.3) applies here. The nursery service is the counterfactual reduction in catch attributable to habitat loss, not an additional flow.

### Progression Pathway

- To upgrade wild fish provisioning from Tier 2 to Tier 3 on B-accuracy: implement fishery-independent surveys (trawl transects or BRUVS), validate spatial attribution with acoustic telemetry or stable isotope tracing, produce full NCAVES production account decomposition.
- To upgrade ecosystem attribution from Tier 1–2 to Tier 2–3: conduct a local mark-recapture study or stable isotope analysis to empirically calibrate habitat contribution fractions.

---

*Derived from: SEEA EA Ecosystem Service Accounts (Section 6.1). Examples from ENDhERI Project — Compiling the first Natural Capital Accounts in the Maldives. Alternative methods from: Applying SEEA EA at the Project Level in Central Java (RNF BCAF, GOAP, 2025). Aligned with UN SEEA EA (2021) and CICES v5.1.*

---

## 7. Tiered Physical Measurement Methods

This section provides alternative physical measurement methods at three resource/accuracy tiers, following the Tiered Assessment Framework. **Physical values only** — monetary valuation is covered separately in each SOP's Part B.

### 7.1 Wild Fish Provisioning — Physical Catch (kg/yr)

#### Tier 1: National Statistics Downscaling

**Method:** Extract national catch data from FAO FishStatJ and downscale to accounting area by population, coastline length, or registered fishers. Classify species into habitat groups (reef, seagrass, pelagic) using FishBase habitat fields and gear type as proxy.

| Attribute | Detail |
|---|---|
| Physical output | Total catch (kg/yr) by ecosystem type (indicative) |
| Key source | FAO, *Yearbook: Fishery and Aquaculture Statistics* (annual). Rome. URL: fao.org/fishery/en/statistics |
| Supporting sources | GOAP, *Technical Guidance on Ocean Accounting for Sustainable Development*, 2nd ed., 2022. URL: oceanaccounts.org |
| | SPC, *Coastal Fisheries Report Card* (periodic). Noumea. URL: coastfish.spc.int |
| Data inputs | FAO FishStatJ national catch; population/coastline data for downscaling; FishBase species–habitat fields |
| Budget | < USD 5,000 |
| Time | 1–3 months |
| Staff | 1–2 analysts (part-time) |
| CV | > 50% — national statistics systematically under-report artisanal/subsistence catch (30–70% of actual in tropical small-scale fisheries) |

#### Tier 2: Spatially Allocated Catch with Landing Site Calibration

**Method:** Combine spatially reconstructed catch data (Sea Around Us, 0.5° grid, including unreported/IUU estimates) with primary landing site surveys or fisher logbooks in the accounting area. Calibrate survey coverage against provincial statistics. Disaggregate by ecosystem type using species–habitat literature validated by fisher interviews.

| Attribute | Detail |
|---|---|
| Physical output | Catch (kg/yr) by ecosystem type, gear type, and species group |
| Key source | ENDhERI Project, *Compiling the first Natural Capital Accounts in the Maldives: Methods Report*, GOAP/UNEP, 2025 |
| Supporting sources | Sea Around Us Project, *Catch Reconstruction Working Papers*, UBC. URL: seaaroundus.org |
| | WorldFish Center, *Small-Scale Fisheries Monitoring: A Practical Guide*, 2018 |
| | FAO, *Guidelines for the Routine Collection of Capture Fishery Data*, Technical Paper 382, 1999 |
| | GOAP, *Applying SEEA EA at the Project Level in Central Java* (RNF BCAF), 2025 |
| Data inputs | Sea Around Us gridded catch; agency landing records; primary landing site surveys/logbooks; species–habitat association data; fisher knowledge validation |
| Budget | USD 10,000–50,000 |
| Time | 3–12 months |
| Staff | 3–5 including field enumerators |
| CV | 20–40% — captures formal/semi-formal fleet; may miss subsistence and night fishers |

#### Tier 3: Fishery-Independent Surveys and Ecosystem Models

**Method:** Directly estimate fish biomass and production through underwater visual census (UVC), acoustic surveys, and/or stock assessment models (surplus production, age-structured). Ecosystem-based models (Ecopath with Ecosim) simulate trophic flows and attribute production to habitat types, resolving the ecosystem allocation problem that plagues Tiers 1–2.

| Attribute | Detail |
|---|---|
| Physical output | Standing biomass and sustainable harvest (kg/yr) by ecosystem type, from direct observation and/or modelled food-web attribution |
| Key source | SPC, *Underwater Visual Census Methods for Assessing Coral Reef Fish Stocks: A Practical Guide for Pacific Island Countries*, 2006. URL: coastfish.spc.int |
| Supporting sources | FAO, *Stock Assessment Tools of FiSAT II*, Technical Paper 487, 2005 |
| | WorldFish Center, *Ecopath with Ecosim Models for Coral Reef Ecosystems* (multiple technical reports) |
| | World Bank, *The Sunken Billions Revisited*, 2017 |
| Data inputs | UVC transect data (fish counts, size, species); acoustic survey biomass; 10–15 yr catch-effort time series for stock assessment; Ecopath diet/production parameters; extent and condition account data |
| Budget | > USD 100,000 |
| Time | > 12 months |
| Staff | > 5 multidisciplinary (dive team, fisheries modellers, reef ecologists) |
| CV | < 20% (with adequate survey design) — but UVC limited to diurnal shallow reef fish; stock assessment requires long time series rarely available in small-scale tropical fisheries |

---

### 7.2 Wood Provisioning — Physical Extraction (kg/yr)

#### Tier 1: National Default Rate Extrapolation

**Method:** Apply a published per-household fuelwood consumption rate from national forestry or household energy statistics to the count of households within a defined distance of mangrove forest. No spatial modelling or distance-weighting.

| Attribute | Detail |
|---|---|
| Physical output | Total extraction (tonnes/yr) — single aggregate estimate |
| Key source | FAO, *Global Forest Resources Assessment 2020*, Rome. URL: fao.org/forest-resources-assessment |
| Supporting sources | Astana, S. (2012) — baseline household demand of 2,496 kg/yr (208 kg/month) for rural Java, Indonesia |
| Data inputs | National per-household fuelwood rate; census household counts; national mangrove extent map (e.g., Global Mangrove Watch); simple distance threshold (e.g., 1–5 km) |
| Budget | < USD 10,000 |
| Time | 1–3 months |
| Staff | 1–2 analysts |
| CV | > 50% — national averages may not reflect local conditions; no spatial differentiation |

#### Tier 2: Spatial Proxy Model with Distance Elasticity

**Method:** Modify baseline demand using a spatial model accounting for household distance to mangrove edge, accessible biomass stock, and household characteristics: W_i = D_base × f(d_i) × g(S_i) × h(A_i). Aggregate across eligible households within 1 km of mangrove edge.

| Attribute | Detail |
|---|---|
| Physical output | Spatially differentiated extraction by district/community (tonnes/yr) |
| Key source | GOAP, *Applying SEEA EA at the Project Level in Central Java* (RNF BCAF), 2025 |
| Supporting sources | Heltberg, R. et al. (2000) — distance elasticity of 0.8 (rural India) |
| | Suman, D.O. (2019) — sustainable yield benchmark of ~4% standing stock/yr |
| | Google Open Buildings v3 — household footprint identification |
| Data inputs | Baseline demand (literature); distance elasticity parameter; Sentinel-2 mangrove extent (10 m); building footprints; standing biomass estimates; use rate of standing stock |
| Budget | USD 10,000–50,000 |
| Time | 3–6 months |
| Staff | 3–5 including GIS analyst |
| CV | 20–50% — sensitive to distance elasticity and use rate assumptions; not independently validated against household surveys |

#### Tier 3: Dedicated Household Surveys and Permanent Plot Monitoring

**Method:** (a) Stratified random household fuelwood survey with physical weighing of collected wood, repeated monthly/quarterly across seasons. (b) Permanent plot biomass monitoring in harvested vs control areas, distinguishing harvest-related loss from natural mortality.

| Attribute | Detail |
|---|---|
| Physical output | Household-level extraction with species composition and seasonal variation (kg/household/yr); biomass removal from plots |
| Key source | CIFOR, *Protocols for the Measurement, Monitoring and Reporting of Structure, Biomass and Carbon Stocks in Mangrove Forests* (Kauffman & Donato), Working Paper 86, 2012. URL: cifor.org |
| Supporting sources | FAO, *National Socioeconomic Surveys in Forestry*, Forestry Paper 179, 2016 |
| | Wetlands International — mangrove livelihood dependence assessments (Indonesia, West Africa, Western Indian Ocean) |
| Data inputs | Dedicated household survey (min 30 households/stratum); weighing scales; moisture content measurement; GPS; permanent plots (min 10–15 × 0.1 ha) with tagged trees ≥ 5 cm DBH; species-specific allometric equations |
| Budget | > USD 100,000 |
| Time | > 12 months |
| Staff | > 5 (survey team + field botanists) |
| CV | < 20% with adequate sampling — but high plot-to-plot variability can widen confidence intervals |

---

## 8. Expert Review: Wild Fish Provisioning Accounts

**Reviewer expertise:** Fisheries economics, natural capital accounting, small-scale fisheries data systems
**Scope:** Step-by-step assessment of the SOP (Steps 1--7) for feasibility, accuracy, difficulty, and practical implementation, with tier assignments and actionable recommendations.

---

### 7.1 Step-by-Step Assessment

#### Step 1: Compile Total Annual Catch

**Feasibility / Resource Intensiveness**

- Staff: 1 fisheries data analyst (part-time, 2--4 weeks). If fisher surveys are needed, add 2--4 enumerators for 4--8 weeks of field time.
- Equipment: Minimal for desk-based compilation (computer, spreadsheet). Field surveys require tablets or data sheets, scales, transport to landing sites.
- Budget: Low if agency data exists and is accessible; moderate-to-high (USD 5,000--20,000) if primary fisher surveys are required, depending on geographic spread and number of landing sites.
- Time: 2--6 weeks for desk-based compilation; 2--4 months if primary surveys are required.
- Institutional access: Formal data-sharing agreement with the national or regional fisheries agency (e.g., MMRI in the Maldives, BFAR in the Philippines, DOF in Indonesia). This is often the single largest institutional bottleneck. In many developing-country contexts, fisheries agencies are protective of raw catch data, release only aggregated national statistics, or have lengthy bureaucratic approval processes. Budget 1--3 months for access negotiations.
- Bottleneck: Reconciling agency data with fisher survey supplements. Agency data typically covers only the formal commercial sector. Artisanal, subsistence, and informal catches --- which may represent 30--70% of total catch in tropical small-scale fisheries --- are systematically under-reported or absent. The Laamu Atoll figure of 61,228 kg/yr should be interpreted as a likely underestimate unless the fisher surveys specifically targeted non-commercial fishing.

**Accuracy / Confidence**

- Uncertainty entry points: (i) Under-reporting of artisanal and subsistence catch in agency records; (ii) recall bias in fisher surveys (fishers typically overestimate good trips and underestimate bad ones); (iii) species misidentification in landing records, particularly in multi-species tropical fisheries; (iv) spatial mismatch --- agency records may report at the district or atoll level, not at the ecosystem accounting boundary.
- Likely confidence: Moderate for total catch volume (+/- 25--40% in typical small-scale fishery settings). Higher confidence for commercially important species with dedicated monitoring (e.g., tuna in the Maldives); lower for reef gleaning, bycatch, and subsistence harvest.
- Most sensitive parameter: Whether the catch estimate captures the full fishing population. Missing a major landing site or an entire fisher segment (e.g., women gleaners, night fishers) can introduce systematic bias exceeding 30%.

**Difficulty of Implementation**

- Technical skills: Basic fisheries data management; survey design for supplementary data collection.
- Common failure points: (i) Agency data arrives in incompatible formats or with unexplained codes; (ii) double-counting when agency records and fisher surveys overlap; (iii) no standardised species list across data sources.
- Institutional barriers: Fisheries data is politically sensitive in many countries --- catch statistics are tied to quota allocations, subsidy claims, and international reporting obligations (e.g., FAO, WCPFC, IOTC). Agencies may be reluctant to share raw data that could reveal discrepancies with official national statistics.

| Dimension | Tier |
|---|---|
| Feasibility | 1 (if agency data accessible) / 2 (if primary surveys needed) |
| Accuracy | 2 |
| Difficulty | 1--2 |

---

#### Step 2: Disaggregate Catch by Ecosystem Association

**Feasibility / Resource Intensiveness**

- Staff: 1 marine ecologist or fisheries biologist (1--2 weeks) plus consultation time with local fishers (1--3 days of focus groups or interviews).
- Equipment: None beyond desktop access to FishBase, scientific literature databases, and local species lists.
- Budget: Low (USD 500--2,000) for the literature review and fisher consultations.
- Time: 1--3 weeks.
- Institutional access: Access to local species lists and taxonomic expertise. If the study area has a well-documented fish fauna (e.g., Maldives, Caribbean), this is straightforward. In poorly studied regions, the species--habitat literature may not exist for the local assemblage.
- Bottleneck: Many commercially important species are habitat generalists. Groupers, for example, may use reef, seagrass, and mangrove habitats at different life stages. Tuna and other pelagic species pass over multiple ecosystem types. The allocation is inherently an expert judgement exercise, not a measurement.

**Accuracy / Confidence**

- Uncertainty entry points: (i) Species--habitat allocation proportions are subjective --- different experts will assign different proportions, and the literature provides ranges, not point estimates; (ii) ontogenetic habitat shifts mean a species might be "seagrass-associated" as a juvenile but "reef-associated" as an adult; (iii) local conditions may deviate from published regional habitat associations (e.g., a species classified as reef-associated in the literature may feed primarily over sand in the accounting area); (iv) catch records may use common names or species groups rather than species-level taxonomy, making literature-based allocation imprecise.
- Likely confidence: Low to moderate. The allocation of pelagic catch to "no specific benthic ecosystem" is defensible. The split between reef-associated and seagrass-associated species is the weakest link, potentially carrying +/- 30--50% uncertainty on the individual ecosystem allocations.
- Most sensitive parameter: The proportion of total catch allocated to each ecosystem type. Because this allocation directly determines the physical supply table and feeds into the monetary allocation, errors here propagate through the entire account.

**Difficulty of Implementation**

- Technical skills: Marine ecology knowledge (species identification, habitat ecology); ability to conduct structured fisher interviews.
- Common failure points: (i) Over-reliance on FishBase or regional literature without local validation; (ii) failure to account for habitat generalists; (iii) treating the allocation as precise when it is fundamentally approximate.
- Institutional barriers: Low. This step relies on scientific literature and local knowledge rather than institutional data.

| Dimension | Tier |
|---|---|
| Feasibility | 1 |
| Accuracy | 3 (this is the most subjective step in Part A) |
| Difficulty | 2 |

---

#### Step 3: Disaggregate by Gear Type

**Feasibility / Resource Intensiveness**

- Staff: Same fisheries data analyst as Step 1 (additional 1--2 days).
- Equipment: None beyond desktop.
- Budget: Negligible if gear type is recorded in agency data. If not, this information must come from fisher surveys (already budgeted in Step 1).
- Time: 1--3 days if gear codes exist in the catch records; 1--2 weeks if gear type must be inferred or collected separately.
- Institutional access: Same as Step 1. Gear type is typically recorded in well-managed fisheries data systems but may be absent in artisanal fisheries monitoring.
- Bottleneck: Multi-gear trips. A single fishing trip may use handline, trolling, and nets. Allocating catch to a single gear type per trip oversimplifies the data. In the Maldives context, pole-and-line tuna fishing is well-delineated, but reef fishing often involves mixed methods.

**Accuracy / Confidence**

- Uncertainty entry points: (i) Gear misclassification in records; (ii) multi-gear trips assigned to a single gear; (iii) gear categories may be too aggregated (e.g., "net" covers gillnet, cast net, and beach seine, which have very different ecological implications).
- Likely confidence: Moderate to high for dominant gear types (e.g., pole-and-line in the Maldives); low for minor or mixed-method fisheries.
- Most sensitive parameter: Whether the gear categories are ecologically meaningful for the accounting purpose. For SEEA EA, gear type matters primarily as a descriptor in the supply table, not as a driver of the valuation.

**Difficulty of Implementation**

- Technical skills: Basic data management.
- Common failure points: Inconsistent gear coding across data sources.
- Institutional barriers: Minimal.

| Dimension | Tier |
|---|---|
| Feasibility | 1 |
| Accuracy | 1--2 |
| Difficulty | 1 |

---

#### Step 4: Map Fishing Effort

**Feasibility / Resource Intensiveness**

- Staff: 1 GIS analyst (1--2 weeks); fisher interviews for spatial knowledge if no VMS/GPS data.
- Equipment: GIS software (QGIS or ArcGIS); GPS tracks if available. If spatial effort data does not exist, participatory mapping with fishers requires printed maps, markers, and facilitation skills.
- Budget: Low (USD 1,000--3,000) for participatory mapping; moderate (USD 5,000--15,000) if GPS loggers need to be deployed on vessels.
- Time: 2--4 weeks for participatory mapping; 3--6 months if vessel tracking data must be collected from scratch.
- Institutional access: VMS (Vessel Monitoring System) data is extremely difficult to access in most countries --- it is managed by fisheries enforcement agencies and is typically classified or restricted. AIS (Automatic Identification System) data from Global Fishing Watch covers only larger vessels (>15m) and misses the small-scale fleet entirely.
- Bottleneck: In small-scale tropical fisheries, spatial effort data almost never exists in a usable form. This is the most resource-intensive step in Part A relative to the analytical value it adds. The SOP underspecifies what "spatial map of fishing effort" means in practice --- resolution, data source, and the link between effort maps and the ecosystem allocation in Step 2.

**Accuracy / Confidence**

- Uncertainty entry points: (i) Participatory mapping produces approximate spatial footprints, not quantitative effort distributions; (ii) fishing effort is highly seasonal and inter-annual, so a single mapping exercise may not represent the accounting period; (iii) fishers may not distinguish their fishing locations at the ecosystem-type resolution needed for the account (e.g., "near the reef" vs. "on the reef slope" vs. "in the channel").
- Likely confidence: Low. Unless vessel tracking data exists, the spatial map will be qualitative rather than quantitative.
- Most sensitive parameter: Spatial resolution. A map that shows "fishing occurs here" is different from a map that quantifies effort in hours/km2 per ecosystem type.

**Difficulty of Implementation**

- Technical skills: GIS; participatory mapping facilitation; spatial analysis.
- Common failure points: (i) Conflating fishing "areas" with fishing "effort"; (ii) producing a map that cannot be linked quantitatively to the catch data in Steps 1--3; (iii) the map becomes a one-off product disconnected from the accounting cycle.
- Institutional barriers: VMS data access (high barrier); AIS data limitations for small-scale fisheries.

| Dimension | Tier |
|---|---|
| Feasibility | 2--3 (the hardest step in Part A for small-scale fisheries) |
| Accuracy | 3 |
| Difficulty | 2--3 |

---

#### Step 5: Calculate Gross Revenue

**Feasibility / Resource Intensiveness**

- Staff: 1 economist or data analyst (1--2 weeks).
- Equipment: Desktop; access to market price data.
- Budget: Low (USD 500--2,000) if market prices are documented; moderate (USD 3,000--8,000) if a market price survey must be conducted.
- Time: 1--3 weeks.
- Institutional access: Market price data may come from fisheries agencies, national statistical offices, or direct market surveys. In many developing countries, ex-vessel prices (the price fishers receive at the landing site) are not systematically recorded, and the only available prices are retail or wholesale market prices, which overstate fisher revenue.
- Bottleneck: (i) Species-level price differentiation --- many tropical fisheries sell mixed species lots at a single price, making species-specific revenue calculation unreliable; (ii) price seasonality --- a single annual average price may mask significant intra-annual variation; (iii) subsistence catch has no observed market transaction, so assigning a "market price" to it is an imputation, not a measurement.

**Accuracy / Confidence**

- Uncertainty entry points: (i) Price data may not represent the prices actually received by fishers (ex-vessel vs. retail distinction); (ii) barter and in-kind transactions are invisible in market price data; (iii) the revenue calculation inherits all uncertainty from Step 1 (catch volume) and compounds it with price uncertainty.
- Likely confidence: Moderate for commercial species with documented market prices; low for subsistence or low-value species.
- Most sensitive parameter: The total catch figure from Step 1. Revenue = Catch x Price, and catch uncertainty (+/- 25--40%) dominates the revenue estimate.

**Difficulty of Implementation**

- Technical skills: Basic economics; survey design for market price collection if needed.
- Common failure points: (i) Using retail prices instead of ex-vessel prices; (ii) failing to account for post-harvest losses (fish that spoils before sale); (iii) applying national average prices to a local fishery with different market dynamics.
- Institutional barriers: Low to moderate. Price data is generally less politically sensitive than catch data.

| Dimension | Tier |
|---|---|
| Feasibility | 1--2 |
| Accuracy | 2 |
| Difficulty | 1--2 |

---

#### Step 6: Calculate Total Fishing Costs

**Feasibility / Resource Intensiveness**

- Staff: 1 fisheries economist (2--4 weeks for survey design, implementation, and analysis). If primary cost surveys are needed, add 2--4 enumerators for 4--8 weeks of field work.
- Equipment: Survey instruments (tablets or paper forms); transport to fishing communities.
- Budget: Moderate to high (USD 5,000--25,000). Fisher cost surveys are expensive relative to catch surveys because they require detailed, repeated interviews about expenditure categories that fishers do not routinely track.
- Time: 2--4 months for a credible cost survey, including design, piloting, data collection, and analysis. This is the most time-consuming step in the entire SOP.
- Institutional access: Low --- cost data rarely exists in any institutional database. The fisheries agency records catches, not costs. This data must almost always be collected through primary surveys.
- Bottleneck: This step is the single most critical bottleneck in the entire provisioning services account. Fisher cost surveys are notoriously difficult for the following reasons: (i) Fishers in artisanal and small-scale fisheries do not keep financial records; (ii) costs are irregular --- a new engine every 5 years, a net every 2 years, daily fuel purchases; (iii) labour is often unpaid family labour or shared crew arrangements where compensation is a catch share, not a wage; (iv) vessel ownership and capital cost structures vary enormously within a single fishery; (v) response rates for cost questions are typically 20--40% lower than for catch questions because fishers consider financial data private; (vi) the Laamu Atoll result (negative resource rent of -3,636,324 MVR) strongly suggests either cost over-estimation, revenue under-estimation, or both --- a common outcome when cost surveys are applied to artisanal fisheries without careful calibration.

**Accuracy / Confidence**

- Uncertainty entry points: (i) Labour cost imputation --- the SOP correctly identifies "crew wages + fisher opportunity costs" but does not specify how to handle unpaid family labour or catch-sharing arrangements, which are the norm in small-scale fisheries. Using a minimum wage or agricultural wage as the opportunity cost of labour is standard practice but produces very different results from using the actual cash wages paid (which may be zero); (ii) capital cost depreciation --- vessel and gear depreciation requires knowing the original purchase price and expected lifespan, both of which fishers estimate poorly; (iii) fuel costs are the most reliably reported cost category because fishers buy fuel in identifiable quantities at known prices; (iv) the cost structure of one vessel or fisher may not be representative of the fleet.
- Likely confidence: Low. The ENDhERI report itself flagged this step as data-deficient. In my experience, fisher cost data in small-scale tropical fisheries typically carries +/- 40--60% uncertainty, which is wider than the margin between positive and negative resource rent in many fisheries.
- Most sensitive parameter: Labour cost. In small-scale fisheries, labour is typically the largest single cost component (40--60% of total costs). The method used to impute the value of unpaid family labour can swing the resource rent from positive to negative.

**Difficulty of Implementation**

- Technical skills: Fisheries economics; survey design and sampling; understanding of artisanal fishery economic structures.
- Common failure points: (i) Under-sampling --- too few fisher interviews to represent fleet diversity; (ii) applying cost structures from one vessel class to the entire fleet; (iii) failing to distinguish between variable costs (fuel, bait) and fixed costs (vessel, gear); (iv) failing to annualise lumpy capital expenditures; (v) not accounting for multi-purpose vessels (e.g., a boat used for both fishing and transport).
- Institutional barriers: Moderate. Fisher trust is essential --- cost data collection requires sustained engagement with fishing communities, ideally through local intermediaries or community leaders.

| Dimension | Tier |
|---|---|
| Feasibility | 3 (the most resource-intensive step) |
| Accuracy | 3 (the least reliable step) |
| Difficulty | 3 (the most technically demanding step) |

---

#### Step 7: Calculate Resource Rent

**Feasibility / Resource Intensiveness**

- Staff: Same economist as Step 6 (1--3 days of calculation and interpretation).
- Equipment: Spreadsheet.
- Budget: Negligible (calculation only).
- Time: 1--3 days.
- Institutional access: None required.
- Bottleneck: Not the calculation itself but interpreting and communicating the result. A negative resource rent (as in the Laamu Atoll case) is an analytically valid but politically difficult result. It implies that the ecosystem's contribution to the fishery is effectively zero or that the fishery is economically unsustainable. Fisheries agencies and fishing communities may reject this finding, particularly if it is used in policy settings.

**Accuracy / Confidence**

- Uncertainty entry points: All uncertainty from Steps 1, 5, and 6 compounds here. The resource rent is a residual --- the difference between two large, uncertain numbers (revenue and cost). Small percentage errors in either input can produce large percentage errors in the residual, or even flip its sign.
- Likely confidence: Low to very low. The resource rent estimate is the weakest single number in the entire provisioning services account. This is not unique to this SOP --- it is a well-known limitation of the resource rent approach in fisheries economics (see Lange et al. 2018, Changing Wealth of Nations; World Bank WAVES programme documentation).
- Most sensitive parameter: The resource rent is most sensitive to: (1) the labour cost imputation method, (2) the total catch estimate, and (3) the market price used. A sensitivity analysis varying these three parameters should be mandatory.

**Difficulty of Implementation**

- Technical skills: Basic arithmetic, but high-level judgement required for interpretation.
- Common failure points: (i) Reporting the resource rent as a point estimate without uncertainty bounds; (ii) not conducting sensitivity analysis; (iii) confusing resource rent with profit (resource rent deducts normal returns to labour and capital --- if these are set too high, rent appears negative even in a profitable fishery); (iv) not disaggregating the resource rent by ecosystem type, which the SOP requires but does not explain how to operationalise (costs are incurred per trip, not per ecosystem type --- allocating costs to ecosystems requires an additional assumption layer).
- Institutional barriers: High for communication and uptake. A negative resource rent may be misinterpreted as "the ocean is worthless" in policy discussions, undermining the credibility of the entire accounting exercise.

| Dimension | Tier |
|---|---|
| Feasibility | 1 (the calculation is trivial) |
| Accuracy | 3 (the result is the least reliable number in the account) |
| Difficulty | 2 (calculation is easy; interpretation and communication are hard) |

---

### 7.2 Tier Summary Table

| Step | Description | Feasibility Tier | Accuracy Tier | Difficulty Tier |
|---|---|---|---|---|
| 1 | Compile total annual catch | 1--2 | 2 | 1--2 |
| 2 | Disaggregate by ecosystem association | 1 | 3 | 2 |
| 3 | Disaggregate by gear type | 1 | 1--2 | 1 |
| 4 | Map fishing effort | 2--3 | 3 | 2--3 |
| 5 | Calculate gross revenue | 1--2 | 2 | 1--2 |
| 6 | Calculate total fishing costs | 3 | 3 | 3 |
| 7 | Calculate resource rent | 1 | 3 | 2 |

**Interpretation:** Tier 1 = simplest/most reliable; Tier 2 = moderate; Tier 3 = advanced/least reliable.

The table reveals that the physical account (Part A, Steps 1--4) is substantially more feasible and reliable than the monetary account (Part B, Steps 5--7), and that the bottleneck for the entire SOP is Step 6 (cost data collection). Step 2 (ecosystem allocation) is the Achilles heel of the physical account.

---

### 7.3 Specific Recommendations

#### Recommendations for Rapid First Assessment

For a team with limited time and budget seeking a defensible first-pass account:

1. **Physical account first, monetary account later.** Compile Steps 1--3 and the physical supply table. Defer Steps 4--7. A physical supply table showing catch by ecosystem type is analytically useful, SEEA EA-compliant, and achievable with agency data alone.

2. **Simplify Step 2 with a three-category rule.** For the initial iteration, classify species as reef-associated, pelagic, or "other/unassigned" rather than attempting the full reef/seagrass/pelagic split. The seagrass allocation is the most uncertain because relatively few commercially harvested species are obligate seagrass associates in most tropical fisheries. Report the seagrass allocation as a range in future iterations when better data are available.

3. **Defer Step 4.** Spatial effort mapping adds substantial cost and time for limited analytical payoff in a first assessment. The SEEA EA requires the supply table, not the effort map. If participatory mapping data exist from other projects (e.g., MPA management plans, fisheries management plans), use them as-is rather than conducting a new exercise.

4. **For the monetary account, use gross revenue only as a first pass.** Gross revenue (Step 5) is far more reliable than resource rent (Step 7) and still provides a policy-relevant measure of the fishery's economic scale attributable to each ecosystem type. Flag it as an upper-bound estimate of the ecosystem's economic contribution and commit to resource rent in a future iteration when cost data can be properly collected.

#### Recommendations Requiring Greatest Investment

1. **Step 6 deserves a dedicated, well-designed fisher economic survey.** This is not a step that can be done cheaply or quickly. A credible cost survey requires: (i) a stratified sampling frame covering all vessel/gear classes; (ii) a minimum of 30 respondents per stratum for statistical reliability; (iii) repeated visits (not single-visit recall surveys); (iv) pilot testing of the survey instrument; (v) enumerators with existing relationships with fishing communities. Budget at least USD 15,000--25,000 and 3--4 months for a small-scale fishery context.

2. **Invest in reconciling agency data and fisher surveys (Step 1).** The difference between these two sources is not noise --- it reveals the structure of under-reporting. Documenting this discrepancy and its causes improves the account and builds institutional capacity for future iterations.

#### Practical Workarounds When Data Are Unavailable

| Data Gap | Workaround | Quality Flag |
|---|---|---|
| No fisheries agency data for the accounting area | Use FAO FishStatJ national data + proportional downscaling by population or coastline length | C (low confidence) |
| No fisher cost surveys | Use cost-revenue ratios from comparable fisheries in the same region (e.g., WorldFish studies, FAO cost-of-fishing studies) applied to local revenue | C (low confidence) |
| No species--habitat association literature for local species | Use FishBase habitat fields + gear type as a proxy (e.g., pole-and-line = pelagic; speargun/reef gleaning = reef-associated) | B--C |
| No spatial effort data | Omit Step 4; describe fishing grounds qualitatively in the metadata | B |
| No ex-vessel price data | Use wholesale market prices discounted by 20--30% as a proxy for ex-vessel prices, or conduct a rapid price survey at 3--5 landing sites over 1 week | B |
| Labour cost structure unknown | Apply the regional median labour share of gross revenue (typically 40--55% in small-scale tropical fisheries, per FAO/WorldFish benchmarks) rather than bottom-up cost estimation | C |

#### Methodological Weaknesses and Missing Considerations

1. **The SOP does not address IUU (illegal, unreported, and unregulated) fishing.** In many tropical fisheries, IUU catch is 20--50% of reported catch. The physical account will systematically underestimate the ecosystem's provisioning service if IUU catch is not at least acknowledged and bounded. Recommendation: Add an IUU adjustment factor based on regional estimates (e.g., from Sea Around Us reconstructed catch data).

2. **The SOP does not address discards and post-harvest losses.** Landed catch understates total extraction from the ecosystem. Discards (fish caught and thrown back, often dead) and post-harvest losses (spoilage before sale) mean the ecosystem is providing more provisioning service than the landed catch records show. Recommendation: Apply a species-group-specific discard rate from regional fisheries literature.

3. **The resource rent method conflates rents from the ecosystem with rents from fisheries management.** A well-managed fishery with restricted access may generate positive rent because of management, not because the ecosystem is inherently productive. An open-access fishery will dissipate rent to zero regardless of ecosystem productivity. The SOP does not discuss the management regime, which fundamentally determines whether resource rent is a meaningful measure of ecosystem contribution.

4. **No guidance on allocating costs to ecosystem types.** The SOP requires resource rent disaggregated by ecosystem type (implied by the supply table structure), but costs are incurred at the trip level, not the ecosystem level. A fisher who catches reef fish and pelagic fish on the same trip incurs joint costs. The SOP needs to specify an allocation rule (e.g., allocate costs in proportion to catch value, or in proportion to catch weight). This is non-trivial and introduces another layer of assumption.

5. **The SOP does not discuss the treatment of subsidies.** Fuel subsidies, vessel construction subsidies, and other government transfers artificially reduce fishing costs and inflate resource rent. Subsidised fisheries can show positive resource rent even when they are economically inefficient. The SEEA EA framework requires accounts to reflect observed market conditions (i.e., include subsidies), but the resulting resource rent may be misleading for policy purposes. Recommendation: Report both subsidised and unsubsidised resource rent where subsidy data are available.

6. **Temporal coverage of the Laamu Atoll example.** The single-year estimate of 61,228 kg/yr is a snapshot. Fisheries catch is highly variable inter-annually due to recruitment variation, weather, El Nino/La Nina cycles, and market demand. A single year may be atypical. Recommendation: Where possible, compile 3--5 years of catch data and report the mean and range.

7. **Missing linkage to condition accounts.** The SOP does not explain how the condition account (e.g., coral cover = 0.49, a depleted state) should inform interpretation of the provisioning account. Coral reefs at 19.67% live cover are likely delivering lower fish provisioning services than they would at reference condition. The physical account captures what is currently supplied, not what the ecosystem could supply if in good condition. This distinction matters for asset valuation and policy.

8. **No treatment of the exchange rate between the physical and monetary accounts when allocating resource rent to ecosystem types.** If total resource rent is negative (as in Laamu Atoll), allocating it to ecosystem types is conceptually problematic. Do you allocate the loss in proportion to catch? In proportion to revenue? The SOP is silent on this. A negative resource rent allocated to each ecosystem type would imply each ecosystem is delivering a negative economic contribution, which is misleading --- the ecosystem is still supplying fish, but the fishery's cost structure is inefficient.

---

### 7.4 Overall Assessment

The skill file provides a clear, well-structured, and SEEA EA-compliant pipeline for wild fish provisioning accounts. Its architecture --- separating physical and monetary accounts, using supply and use tables, and flagging data quality --- follows best practice. The pipeline diagram and step-by-step format are well suited for operationalisation by accounting teams.

The principal vulnerabilities are concentrated in two areas:

1. **The monetary account depends critically on fisher cost data (Step 6), which is the hardest data to collect reliably in small-scale tropical fisheries.** The Laamu Atoll case study itself demonstrates this --- the negative resource rent result was flagged as data-deficient. This is not a failure of the SOP design but a structural limitation of the resource rent method in artisanal fishery contexts. Teams implementing this SOP should be prepared for the possibility that a credible monetary account may require 2--3 accounting iterations to produce, with the first iteration flagged as provisional.

2. **The species--ecosystem allocation (Step 2) is the analytical foundation of the physical account, yet it rests on subjective expert judgement.** This is an inherent limitation acknowledged in the SOP's data quality table, but the implications for downstream accuracy deserve more emphasis. The allocation determines which ecosystem type "gets credit" for provisioning services, which in turn shapes policy narratives about ecosystem importance.

For teams implementing this SOP for the first time: **start with the physical supply table and gross revenue; defer the full resource rent calculation until cost data infrastructure is mature; and invest the freed-up resources in understanding the species--ecosystem allocation, which is analytically more important for ecosystem accounting than a precise monetary figure.**
