# Skill: Regulating Ecosystem Service Accounts

**Purpose:** Quantify the physical supply and monetary value of regulating ecosystem services — fisheries nursery, carbon sequestration, coastal protection, and sediment nourishment — following the SEEA EA framework and CICES classification.

**Framework:** UN SEEA EA Ecosystem Service Accounts (Sections 6.2–6.5)
**CICES Category:** Regulating and maintenance services
**Services covered:**
1. Fisheries nursery service
2. Carbon sequestration (global climate regulation)
3. Coastal protection
4. Sediment nourishment

---

## 1. Pipeline Overview

```
┌─────────────────────────────────────────────────────────────────────────┐
│                        DATA INGESTION LAYER                            │
│                                                                        │
│  Ecological Data          Spatial/GIS Data          Reference Data     │
│  ┌──────────────┐        ┌───────────────┐         ┌──────────────┐   │
│  │ Fish density  │        │ Extent account│         │ LRR values   │   │
│  │ surveys       │        │ (ecosystem    │         │ (literature) │   │
│  │               │        │  maps)        │         │              │   │
│  │ Catch data    │        │ Building      │         │ NCP rates    │   │
│  │ (from SOP 1)  │        │ footprints    │         │ (literature) │   │
│  │               │        │               │         │              │   │
│  │ Condition     │        │ Coastline     │         │ SCC values   │   │
│  │ data          │        │ shapefiles    │         │ (IWG/EPA)    │   │
│  └──────┬───────┘        └──────┬────────┘         │              │   │
│         │                       │                   │ CaCO3 rates  │   │
│         │                       │                   │ (literature) │   │
│         │                       │                   │              │   │
│         │                       │                   │ Engineering  │   │
│         │                       │                   │ cost data    │   │
│         │                       │                   └──────┬───────┘   │
└─────────┼───────────────────────┼──────────────────────────┼───────────┘
          │                       │                          │
          ▼                       ▼                          ▼
┌─────────────────────────────────────────────────────────────────────────┐
│                    FOUR REGULATING SERVICE PIPELINES                    │
│                                                                        │
│  ┌───────────────┐  ┌───────────────┐  ┌──────────────┐ ┌───────────┐ │
│  │ 1. FISHERIES  │  │ 2. CARBON     │  │ 3. COASTAL   │ │ 4. SEDI-  │ │
│  │    NURSERY    │  │    SEQUEST.   │  │    PROTECT.  │ │    MENT   │ │
│  │               │  │               │  │              │ │           │ │
│  │ LRR method    │  │ Extent × NCP  │  │ Buffer zone  │ │ CaCO3    │ │
│  │ → enhanced    │  │ → Mg CO2/yr   │  │ → assets     │ │ production│ │
│  │   biomass     │  │               │  │   protected  │ │ rates     │ │
│  │ → mortality   │  │ × SCC         │  │              │ │           │ │
│  │   discount    │  │ → USD/yr      │  │ Replacement  │ │ × beach   │ │
│  │ → market      │  │               │  │ cost method  │ │ nourish-  │ │
│  │   price       │  │ Sensitivity   │  │              │ │ ment cost │ │
│  │               │  │ analysis      │  │              │ │           │ │
│  └───────┬───────┘  └───────┬───────┘  └──────┬───────┘ └─────┬─────┘ │
│          │                  │                  │               │       │
└──────────┼──────────────────┼──────────────────┼───────────────┼───────┘
           │                  │                  │               │
           ▼                  ▼                  ▼               ▼
┌─────────────────────────────────────────────────────────────────────────┐
│             SUPPLY AND USE TABLE COMPILATION                           │
│                                                                        │
│  Physical supply: biomass (kg/yr), CO2 (Mg/yr), coastline (m),        │
│                   sediment (m^3/yr) — by ecosystem type                │
│  Monetary supply: resource rent, SCC value, replacement cost           │
│                   — by ecosystem type and value type                   │
│  Use tables: fisheries sector, global community, coastal households,   │
│              tourism sector                                            │
│                                                                        │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## 2. SOP: Fisheries Nursery Service

**SEEA EA Section:** 6.2
**Providing ecosystems:** Coral reefs, seagrass
**Valuation method:** Productivity change (market price of landed fish)
**Value type:** Market-based (indirect)

### Part A: Physical Measurement — Productivity Change with Log Response Ratio (LRR)

```
Step 1: Establish baseline fish density
    │
    ├── Obtain fish density data from areas WITHOUT nursery habitat
    └── This serves as the counterfactual baseline

Step 2: Calculate the Log Response Ratio (LRR)
    │
    ├── Compare fish density in areas WITH nursery habitat to areas WITHOUT
    ├── LRR quantifies proportional increase attributable to nursery habitat
    │
    │   ┌──────────────────────┬─────────────────────────────┐
    │   │ Nursery Habitat      │ LRR (density enhancement)   │
    │   ├──────────────────────┼─────────────────────────────┤
    │   │ Coral reef           │ 31%                         │
    │   │ Seagrass             │ 13%                         │
    │   └──────────────────────┴─────────────────────────────┘
    │
    └── Source: Scientific literature (meta-analyses)

Step 3: Estimate enhanced juvenile production
    │
    └── Apply LRR to total fish biomass in accounting area
        Enhanced juvenile biomass = Total biomass × LRR

Step 4: Apply juvenile mortality rate
    │
    ├── Juvenile mortality rate: 95% (i.e., 5% survive to harvestable size)
    └── Nursery contribution to harvest (kg/yr) = Enhanced juvenile biomass × 0.05
```

**Physical account output:** Additional harvestable fish biomass (kg/yr) attributable to nursery habitat, by ecosystem type.

### Part B: Economic Valuation — Market Price of Landed Fish

> **Value type: Market-based (indirect).** The physical biomass enhancement is valued at observed market prices for landed fish. The underlying nursery service is not itself traded.

```
Step 5: Calculate monetary value
    │
    ├── Nursery value = Additional harvestable biomass (kg) × Market price (currency/kg)
    └── Compile into supply and use table format by ecosystem type
```

**Formulae:**

```
Enhanced juvenile biomass (coral reef) = Total fish biomass × 0.31
Enhanced juvenile biomass (seagrass)   = Total fish biomass × 0.13

Harvestable contribution = Enhanced juvenile biomass × 0.05

Monetary value = Harvestable contribution (kg/yr) × Market price (currency/kg)
```

### Tiered Monetary Valuation Methods — Fisheries Nursery (NCAVES/MAIA)

| Monetary Tier | Method | NCAVES Category | Data Requirement |
|---|---|---|---|
| Tier 1 | Residual value method: attribute a proportion of total fisheries resource rent to nursery-dependent species based on literature | III (residual) | Resource rent from provisioning account; nursery-dependent species list from FishBase |
| Tier 2 | Productivity change × market price (as described above): LRR × survival × market price | III (productivity change) | LRR values; survival rates; local market prices |
| Tier 3 | Stochastic production frontier: regress fishery productivity on nursery habitat area controlling for other inputs, estimate marginal nursery productivity × market price | III (productivity change) | Multi-year fisheries production data; habitat area time series; econometric modelling capacity |

> **NCAVES reference (Chunk 26):** Anneboina & Kumar (2017) used the productivity change method with a stochastic production frontier model to value mangrove nursery services for Indian fisheries, estimating marginal mangrove productivity at 1.86 tonnes/ha/yr, yielding ~146,000 Rs/ha/yr (USD 1,900/ha/yr). Since the marginal productivity increase already controls for other inputs, a market price / gross value approach is accounting-compatible for the nursery service. The residual value method (Tier 1) attributes a portion of the final product's value to the nursery service based on the proportion of the production chain dependent on nursery habitat.

### Key Parameters

| Parameter | Value | Source |
|---|---|---|
| Coral reef nursery LRR | 31% | Scientific literature (meta-analysis) |
| Seagrass nursery LRR | 13% | Scientific literature (meta-analysis) |
| Juvenile mortality rate | 95% | Standard ecological assumption |
| Survival to harvest | 5% | Derived from mortality rate |
| Market price of landed fish | Site-specific (local currency/kg) | Local market data |

---

## 3. SOP: Carbon Sequestration

**SEEA EA Section:** 6.3
**Providing ecosystems:** Mangroves, seagrass
**Valuation method:** Social Cost of Carbon (SCC) or market-based pricing (carbon exchange)
**Value type:** Non-market (shadow price) or Market-based (exchange price)

### Part A: Physical Measurement

```
Step 1: Determine ecosystem extent
    │
    ├── Obtain from the extent account
    │
    │   ┌──────────────────────┬─────────────────────────────────┐
    │   │ Ecosystem            │ Example Extent (Laamu Atoll)    │
    │   ├──────────────────────┼─────────────────────────────────┤
    │   │ Mangroves            │ 18.7 ha                         │
    │   │ Seagrass             │ 4,855.5 ha                      │
    │   └──────────────────────┴─────────────────────────────────┘
    │
    └── Substitute with values from your own extent account

Step 2: Establish per-hectare sequestration rates (Approach A: Literature NCP)
    │
    ├── Use Net Carbon Production (NCP) rates from published literature
    ├── Calibrate to local conditions where possible
    │
    │   ┌──────────────────────┬─────────────┬──────────────────────────────────┐
    │   │ Ecosystem            │ NCP         │ Components                       │
    │   │                      │ (Mg CO2/    │                                  │
    │   │                      │  ha/yr)     │                                  │
    │   ├──────────────────────┼─────────────┼──────────────────────────────────┤
    │   │ Mangrove             │ 17.23       │ AGB accumulation + soil C seq.   │
    │   │ Seagrass             │ 4.44        │ C burial in sediments + biomass  │
    │   └──────────────────────┴─────────────┴──────────────────────────────────┘
    │
    └── Source: Published literature (calibrated locally)

Step 3: Calculate total annual sequestration
    │
    │   Total sequestration = Extent (ha) × NCP (Mg CO2/ha/yr)
    │
    │   ┌──────────────────────┬────────────────────┬──────────────────┐
    │   │ Ecosystem            │ Calculation        │ Example Total    │
    │   │                      │                    │ (Mg CO2/yr)      │
    │   ├──────────────────────┼────────────────────┼──────────────────┤
    │   │ Mangrove             │ Extent × NCP       │ ~322             │
    │   │ Seagrass             │ Extent × NCP       │ ~21,558          │
    │   │ Combined             │                    │ Sum of above     │
    │   └──────────────────────┴────────────────────┴──────────────────┘
    │
    └── Present by ecosystem type and carbon pool (AGB vs soil)

Step 4: Compile physical account
    │
    └── Supply and use table format:
        sequestration rates by ecosystem type, total annual sequestration
```

**Physical account output:** Annual carbon sequestration (Mg CO2/yr) by ecosystem type and carbon pool.

### Alternative Physical Measurement: Incremental Biomass Change from Permanent Plots (Approach B)

**When to use:** Where permanent monitoring plots exist and repeated tree censuses can provide locally calibrated sequestration rates, rather than relying on literature-derived NCP rates. More data-intensive but captures inter-annual variability and species-level drivers.

```
Step 2b: Measure incremental biomass change
    │
    ├── Tag all trees ≥5 cm DBH in permanent plots (e.g., 0.1 ha each)
    ├── Measure stems at baseline and follow-up (e.g., 2-year interval)
    ├── Transform measurements to biomass using species-specific allometrics:
    │     AGB = a × ρ × DBH^b   (ρ = wood density)
    ├── Estimate BGB using conversion equations (e.g., Komiyama et al. 2008)
    ├── Apply carbon fractions: 47% AGB, 39% BGB (Kauffman & Donato 2012)
    ├── Track mortality (subtract biomass of dead trees)
    ├── Track ingrowth (add new recruits ≥5 cm DBH)
    └── Annual sequestration = (Live C stock at t₂ − Live C stock at t₁)
                                / measurement interval

Step 2c: Measure Soil Organic Carbon (SOC)
    │
    ├── Collect soil cores (e.g., r = 2.54 cm, l = 30 cm) to 10–20 cm depth
    ├── Analyse using Walkley-Black wet-oxidation (K₂Cr₂O₇-H₂SO₄)
    │     following national standards (e.g., SNI7724:2011)
    └── Where direct SOC data unavailable for follow-up, apply Tier 2 rate
          (e.g., 1.2 ± 0.2 Mg C ha⁻¹ yr⁻¹ for degraded forests;
           Murdiyarso et al. 2023)
```

> **RNF BCAF example (Central Java):** 13 permanent plots (0.1 ha each) measured in 2023 and 2025 yielded locally calibrated rates. Total annual mangrove sequestration: 24,227 Mg C (88,831 Mg CO₂e). High plot-to-plot variability compounded through allometric equations into wide confidence intervals for district means. (Source: GOAP, 2025)

> **Quality stratification recommendation:** Future assessments should stratify mangrove extent by quality class (intact, degraded, regenerating, converted) using satellite-derived indicators combined with ground-truthing, then assign class-specific sequestration rates. The difference between pristine mangroves (>7 Mg C ha⁻¹ yr⁻¹) and degraded stands (<1 Mg C ha⁻¹ yr⁻¹) makes single average rates inadequate for heterogeneous landscapes.

### Part B: Economic Valuation — Social Cost of Carbon (SCC)

> **Value type: Non-market.** The SCC is a shadow price, not a market price. There is no functioning market in which the climate regulation service of mangroves and seagrass is bought or sold. The SCC estimates the economic damage avoided by preventing the emission of one additional tonne of CO2. The resulting monetary figure represents an estimate of economic significance for policy analysis, not a revenue stream or market transaction.

```
Step 5: Select the Social Cost of Carbon (SCC) value
    │
    ├── Must be from a recognised, peer-reviewed source
    ├── Value used: USD 51 per Mg CO2
    │     (U.S. IWG central estimate at 3% discount rate, 2020 base year)
    │
    ├── Why SCC and not a carbon market price?
    │     • Voluntary market prices reflect willingness-to-pay in thin markets
    │     • Compliance market prices reflect regulatory dynamics
    │     • SCC captures avoided damage to society per tonne CO2 sequestered
    │     • SCC is the theoretically correct measure for SEEA EA
    │
    └── Higher SCC estimates exist (e.g., USD 185/Mg CO2 from EPA)
        Choice of SCC is a policy/ethical decision — document transparently

Step 6: Calculate annual monetary value
    │
    │   Monetary value = Total sequestration (Mg CO2/yr) × SCC (USD/Mg CO2)
    │
    │   ┌──────────────────────┬────────────────────┬─────────────────────┐
    │   │ Ecosystem            │ Calculation        │ Example Value       │
    │   │                      │                    │ (USD/yr)            │
    │   ├──────────────────────┼────────────────────┼─────────────────────┤
    │   │ Mangrove             │ Seq. × SCC         │ ~16,422             │
    │   │ Seagrass             │ Seq. × SCC         │ ~1,099,458          │
    │   │ Combined             │                    │ Sum of above        │
    │   └──────────────────────┴────────────────────┴─────────────────────┘
    │
    └── Convert to local currency using prevailing exchange rate

Step 7: Convert to local currency
    │
    └── Compile into supply and use table format

Step 8: Sensitivity analysis
    │
    ├── Recalculate using alternative SCC values:
    │
    │   ┌─────────────────────────┬──────────┬──────────────────────────────┐
    │   │ SCC Scenario            │ USD/Mg   │ Source / Rationale           │
    │   │                         │ CO2      │                              │
    │   ├─────────────────────────┼──────────┼──────────────────────────────┤
    │   │ IWG central (3%)        │ 51       │ U.S. IWG central estimate   │
    │   │ IWG high (2.5%)         │ 76       │ U.S. IWG higher estimate    │
    │   │ EPA updated (2%)        │ 185      │ EPA lower discount rate     │
    │   └─────────────────────────┴──────────┴──────────────────────────────┘
    │
    └── Present range of plausible monetary estimates
```

### Alternative Monetary Valuation: Market-Based Carbon Pricing (Approach B)

**When to use:** Where a domestic regulatory carbon market exists (e.g., Indonesia's IDXCarbon exchange), market-based pricing may be preferred as the "best available estimate" over the SCC shadow-price approach.

```
Step 6b: Apply market carbon price
    │
    ├── Convert Mg C to Mg CO₂e using IPCC molecular weight ratio:
    │     CO₂e = Mg C × (44/12) = Mg C × 3.67
    │
    ├── Monetary value = Total sequestration (Mg CO₂e/yr)
    │                    × Market price (local currency/Mg CO₂e)
    │
    │   ┌────────────────────┬──────────────────┬─────────────────────────┐
    │   │ Pricing Approach   │ Value            │ When to Use             │
    │   ├────────────────────┼──────────────────┼─────────────────────────┤
    │   │ SCC (shadow price) │ USD 51–185/Mg CO₂│ No domestic market;     │
    │   │                    │                  │ national statistics     │
    │   │ Market-based       │ e.g., IDR 150,000│ Operational domestic    │
    │   │ (carbon exchange)  │ /tCO₂e           │ carbon exchange;        │
    │   │                    │                  │ investor communication  │
    │   └────────────────────┴──────────────────┴─────────────────────────┘
    │
    └── Document which approach was used and why
```

> **RNF BCAF example (Central Java):** IDXCarbon market price of IDR 150,000/tCO₂e applied to 88,831 Mg CO₂e yielded IDR 13.3 billion in annual carbon sequestration value. The report acknowledges both SCC and market approaches but recommends compliance market pricing where available. (Source: GOAP, 2025)

**Reporting requirement:** When reporting carbon sequestration monetary values, always state:
1. The SCC value used and its source
2. The discount rate assumed
3. That the value is a non-market shadow price, not a market transaction
4. Sensitivity to alternative SCC values

### Key Parameters

| Parameter | Value | Source |
|---|---|---|
| Mangrove NCP | 17.23 Mg CO2/ha/yr | Published literature (calibrated locally) |
| Seagrass NCP | 4.44 Mg CO2/ha/yr | Published literature (calibrated locally) |
| SCC (central) | USD 51/Mg CO2 | U.S. IWG (3% discount rate, 2020) |
| SCC (high) | USD 76/Mg CO2 | U.S. IWG (2.5% discount rate) |
| SCC (EPA updated) | USD 185/Mg CO2 | U.S. EPA (2% discount rate) |
| IDXCarbon market price | IDR 150,000/tCO2e | Indonesian Carbon Exchange (market-based alternative) |
| Exchange rate | Prevailing local currency:USD rate | National statistical office or central bank |
| AGB carbon fraction | 47% | Kauffman & Donato (2012) — for plot-based approach |
| BGB carbon fraction | 39% | Kauffman & Donato (2012) — for plot-based approach |
| SOC Tier 2 rate | 1.2 ± 0.2 Mg C ha⁻¹ yr⁻¹ | Murdiyarso et al. (2023) — degraded forests |

### Tiered Monetary Valuation Methods — Carbon Sequestration (NCAVES/MAIA)

| Monetary Tier | Method | NCAVES Category | Data Requirement |
|---|---|---|---|
| Tier 1 | Value transfer: apply published per-hectare carbon values from ESVD (median climate regulation ~USD 172/ha/yr) adjusted for biome and income | V (transferred) | Published unit values; extent data |
| Tier 2 | SCC × physical sequestration (as described above) with sensitivity analysis across SCC scenarios (USD 51–185/Mg CO2) | II (prices from similar markets — SCC is a modelled shadow price) or II (carbon exchange market price) | Physical sequestration from Tier 1–2 measurement; SCC or market price selection |
| Tier 3 | Maintenance cost approach: estimate the cost of maintaining carbon stocks (avoided deforestation programmes, blue carbon project management costs) as a proxy for exchange value; or NPV asset valuation using site-specific sequestration and retention flows discounted over 100-year asset life | V (replacement/maintenance cost) or NPV framework | Programme cost data; or site-specific sequestration rates + discount rate + projected future flows |

> **NCAVES distinction (Chunk 17):** Carbon sequestration (flow of CO2 removal during accounting period) and carbon retention (ongoing storage preventing release) are both ecosystem services. Service flow accounts value sequestration; asset accounts value the NPV of future flows including retention risk. The SEEA EA recommends social discount rates for climate regulation services (collective benefits). Drupp et al. (2015) median recommended long-term SDR: 2.25%. UK Treasury Green Book: declining rates from 3.5% (years 0–30) to 1.0% (300+ years).

> **NCAVES asset valuation formula (Chunk 27):** V = Σ [R_t / (1+r)^t] for t = 0 to N, where R_t = expected annual service flow, r = social discount rate, N = asset lifetime (up to 100 years). For carbon, R_t includes both sequestration value (annual flow × SCC) and the risk-adjusted retention value.

---

## 4. SOP: Coastal Protection

**SEEA EA Section:** 6.4
**Providing ecosystems:** Coral reefs, mangroves
**Valuation method:** Replacement cost
**Value type:** Non-market (cost-based proxy)

### Part A: Physical Measurement

```
Step 1: Establish the coastal buffer zone (Approach A: Uniform Buffer)
    │
    ├── Define a 100-metre buffer zone landward from the shoreline
    └── Apply to all inhabited islands in the accounting area

    Alternative Step 1b: Differentiated buffer by exposure (Approach B)
    │
    ├── Low energy coast (sheltered seas, embayments):     100 m buffer
    ├── High energy coast (open ocean, exposed):           300 m buffer
    ├── Classify mangroves as coastal (sea-facing) vs estuarine (riverine)
    │     → Only coastal mangroves assessed for ocean-facing protection
    ├── Require minimum continuous mangrove width of 25 m
    │     within 200 m of shoreline for protective service eligibility
    └── Exclude coastline segments with existing grey infrastructure
          (seawalls, quaywalls)

Step 2: Map protective ecosystem features
    │
    ├── Identify coral reef systems fronting inhabited coastlines
    │     (from extent account)
    └── Identify mangrove areas providing wave attenuation
          (from extent account)

Step 3: Identify protected built assets
    │
    ├── Overlay building footprint data with the 100 m buffer zone
    ├── Count and categorise buildings within the buffer:
    │     ├── Residential
    │     ├── Commercial
    │     └── Institutional
    └── Example (Laamu Atoll, Maldives): 778 buildings
    Note: Where local building survey data is unavailable, use
          Google Open Buildings (v3) or Microsoft Building Footprints

Step 4: Measure protected coastline length
    │
    ├── Calculate total coastline length fronted by reef or mangrove
    ├── Example (Laamu Atoll, Maldives): 33,142 metres
    └── Example (Central Java, RNF): 30,500+ buildings, 64.58 km coastline
```

**Physical account output:** Number and type of protected buildings; total protected coastline length (m); spatial maps of protective features and buffer zones.

### Part B: Economic Valuation — Replacement Cost Method

> **Value type: Non-market (cost-based proxy).** There is no market where coastal protection by coral reefs is traded. The replacement cost method estimates what it would cost to build engineered infrastructure providing equivalent protection. This yields a lower-bound estimate.

```
Step 5: Assign replacement values to buildings
    │
    ├── Obtain local construction cost data by building type
    └── Assign replacement values per building category

Step 6: Select engineering replacement benchmarks
    │
    ├── Identify cost of engineered coastal defence alternatives
    │
    │   ┌───────────────────────┬────────────────────────────────────┐
    │   │ Defence Type          │ Example Cost (currency per         │
    │   │                       │ linear metre)                      │
    │   ├───────────────────────┼────────────────────────────────────┤
    │   │ Quaywall construction │ e.g., MVR 60,000 (Maldives)       │
    │   │ Sheet pile install.   │ e.g., MVR 170,000 (Maldives)      │
    │   └───────────────────────┴────────────────────────────────────┘
    │
    └── Obtain locally relevant engineering cost estimates

Step 7: Calculate replacement cost
    │
    ├── Assign defence type to each coastline segment based on:
    │     ├── Exposure conditions
    │     ├── Wave energy
    │     └── Engineering specification required
    ├── Replacement cost = Σ (Segment length (m) × Unit cost (currency/m))
    └── Sum across all segments for total coastal protection value

Step 8: Compile account
    │
    ├── Present in supply and use table format
    └── Produce spatial maps: buffer zone, buildings, reef systems
```

### Alternative Monetary Valuation: Annualised Depreciation Model

**When to use:** To convert the stock-based replacement cost into an annual service flow consistent with SEEA EA supply and use table requirements (paragraphs 9.50–9.51). This better aligns with SEEA EA's flow-based accounting by converting capital replacement values into annual ecosystem service equivalents.

```
Annual Value = (Construction Cost − Salvage Value) / Service Life

    Where:
    ├── Salvage value: zero (standard assumption)
    ├── Service life: 25 years (standard engineering lifetime)
    └── Erosion rate (e.g., 2 m/yr) may justify service-life comparability
```

> **RNF BCAF example (Central Java):** Differentiated buffers (100 m for Demak/Jepara on the Java Sea; 300 m for Cilacap/Kebumen on the Indian Ocean) with the annualised depreciation model yielded an annual coastal protection value exceeding IDR 17.2 billion. Engineered shorelines were explicitly excluded. (Source: GOAP, 2025)

### Data Sources

| Data Source | Purpose |
|---|---|
| Building footprint data (local survey, Google Open Buildings v3, or Microsoft Building Footprints) | Asset identification within buffer zone |
| Reef extent (from extent account) | Mapping protective reef features |
| Local construction cost data | Building replacement values |
| Coastal engineering cost data | Quaywall and sheet pile unit costs |
| Island coastline GIS data | Buffer zone and coastline length |

### Limitations

- The replacement cost approach is a **lower-bound estimate** — captures only direct infrastructure costs
- Not included: maintenance costs, environmental impacts of hard infrastructure, loss of aesthetic/recreational values
- Does not reflect what society would actually pay to preserve the reef

### Tiered Monetary Valuation Methods — Coastal Protection

| Monetary Tier | Method | NCAVES Category | Data Requirement |
|---|---|---|---|
| **Tier 1** | Value transfer — apply global or regional average avoided damage per hectare of reef or mangrove from ESVD database or published meta-analysis (e.g., Barbier et al. 2011) | V (simulated exchange value / value transfer) | Ecosystem extent; published unit value; basic exposure indicator (e.g., population within 1 km) |
| **Tier 2** | Replacement cost — annualised cost of equivalent hard infrastructure (seawall, quaywall) protecting the same coastline length **(current method)** | V (replacement cost) | Local construction cost data; coastline length protected; asset data within buffer zone |
| **Tier 3** | Expected damage function (EDF) — estimate probability-weighted avoided damages using hydrodynamic wave attenuation modelling (World Bank 2016; Menendez et al. 2020); alternatively, insurance premium differential between properties with and without reef/mangrove protection | V (avoided damage cost) | Storm frequency/intensity data; hydrodynamic model (e.g., XBeach, Delft3D); high-resolution asset exposure mapping; or paired insurance premium data |

> **NCAVES guidance (Chunk 23):** The replacement cost method (Tier 2) is pragmatic but captures only infrastructure costs. The EDF approach (Tier 3) provides a more comprehensive avoided-damage estimate. For SEEA EA, values should be expressed as exchange values — the price at which the protective service would be transacted between the ecosystem as institutional unit and the beneficiary sector. Where WTP estimates are available, the simulated exchange value (SEV) conversion must be applied.

---

## 5. SOP: Sediment Nourishment

**SEEA EA Section:** 6.5
**Providing ecosystems:** Coral reefs, seagrass
**Valuation method:** Replacement cost (beach nourishment)
**Value type:** Non-market (cost-based proxy)

### Part A: Physical Measurement

```
Step 1: Estimate coral reef carbonate production rate
    │
    ├── Use published rates for the relevant bioregion
    ├── Rate incorporates:
    │     ├── Carbonate production from coral growth
    │     ├── Coralline algae contribution
    │     ├── Foraminifera contribution
    │     ├── Halimeda contribution
    │     └── NET OF bioerosion losses (borers, grazers, dissolution)
    └── Example rate (Maldives): 0.049 m^3/m/yr
        (cubic metres sediment per linear metre reef crest per year)

Step 2: Estimate seagrass epibiontic sediment production
    │
    ├── Calculate CaCO3 production from organisms on seagrass blades:
    │     ├── Coralline algae
    │     └── Foraminifera
    └── Use published production rates for regional seagrass assemblage

Step 3: Calculate total physical sediment supply
    │
    ├── Coral reef: Production rate (m^3/m/yr) × Reef crest length (m)
    └── Seagrass: Per-hectare epibiontic production × Seagrass extent (ha)
```

**Physical account output:** Annual sediment production (m^3 CaCO3/yr) by ecosystem type.

### Part B: Economic Valuation — Replacement Cost (Beach Nourishment)

> **Value type: Non-market (cost-based proxy).** Natural sediment production has no market. The replacement cost of importing and mechanically placing equivalent volumes of sand provides a proxy value. This is a lower-bound estimate.

```
Step 4: Establish beach nourishment cost
    │
    ├── Determine cost of importing and placing equivalent volumes of sand
    └── Obtain local or regional beach nourishment cost data (currency/m^3)

Step 5: Calculate monetary value
    │
    └── Monetary value = Physical sediment production (m^3/yr)
                         × Beach nourishment cost (currency/m^3)

Step 6: Compile account
    │
    └── Present in supply and use table format (physical and monetary)
```

### Key Parameters

| Parameter | Value | Source |
|---|---|---|
| Coral reef carbonate production | 0.049 m^3/m/yr | Published literature (Indo-Pacific reefs) |
| Seagrass epibiontic CaCO3 production | Species/site-specific | Published literature |
| Beach nourishment cost | Local engineering data (currency/m^3) | Local engineering cost estimates |

### Tiered Monetary Valuation Methods — Sediment Nourishment

| Monetary Tier | Method | NCAVES Category | Data Requirement |
|---|---|---|---|
| **Tier 1** | Value transfer — apply published unit replacement costs for beach nourishment per m³ from comparable island or coastal contexts, or use global average unit values from ESVD | V (simulated exchange value / value transfer) | Physical sediment supply (m³/yr from Tier 1 physical estimate); published unit cost from comparable context |
| **Tier 2** | Replacement cost — local beach nourishment cost per m³ × physical sediment supply **(current method)** | V (replacement cost) | Physical sediment supply (m³/yr); local or regional engineering cost data for mechanical beach nourishment |
| **Tier 3** | Avoided erosion damage cost — value of coastline and beach assets protected from erosion by natural sediment supply; requires sediment transport modelling and asset exposure mapping | V (avoided damage cost) | Sediment transport model calibrated with bathymetric and wave data; coastal asset register; erosion rate estimates with/without natural sediment supply |

> **Note:** The replacement cost approach (Tier 2) is the practical standard for most accounting contexts. It assumes that the cost of importing and mechanically placing equivalent sand volumes represents the minimum value of the natural service. This is a lower-bound estimate. For SEEA EA exchange value consistency, costs should reflect the market price of beach nourishment as a transacted service, not willingness-to-pay.

### Significance

This service is critical for low-lying coastal areas and island nations, where natural sediment supply from reefs maintains island elevation and beach width against erosion and sea level rise. Particularly significant for atoll nations (e.g., Maldives, Pacific Island states) and other reef-fronted coastlines.

---

## 6. Output: SEEA EA Supply and Use Tables

### 6.1 Physical Supply Table (Regulating Services)

```
┌─────────────────────────────────────────────────────────────────────────┐
│  PHYSICAL SUPPLY TABLE: Regulating Ecosystem Services                  │
│                                                                        │
│  ┌──────────────────┬─────────────┬──────────┬───────────┬──────────┐  │
│  │ Service          │ Coral Reefs │ Seagrass │ Mangroves │ Total    │  │
│  ├──────────────────┼─────────────┼──────────┼───────────┼──────────┤  │
│  │ Nursery service  │ [kg/yr]     │ [kg/yr]  │ —         │ [total]  │  │
│  │ (biomass)        │             │          │           │          │  │
│  ├──────────────────┼─────────────┼──────────┼───────────┼──────────┤  │
│  │ Carbon seq.      │ —           │ [Mg      │ [Mg       │ [total]  │  │
│  │ (Mg CO2/yr)      │             │ CO2/yr]  │ CO2/yr]   │          │  │
│  ├──────────────────┼─────────────┼──────────┼───────────┼──────────┤  │
│  │ Coastal protect. │ [m]         │ —        │ [m]       │ [total]  │  │
│  │ (coastline m)    │             │          │           │          │  │
│  ├──────────────────┼─────────────┼──────────┼───────────┼──────────┤  │
│  │ Sediment nour.   │ [m^3/yr]    │ [m^3/yr] │ —         │ [total]  │  │
│  │ (CaCO3)          │             │          │           │          │  │
│  └──────────────────┴─────────────┴──────────┴───────────┴──────────┘  │
└─────────────────────────────────────────────────────────────────────────┘
```

### 6.2 Monetary Supply Table (Regulating Services)

```
┌─────────────────────────────────────────────────────────────────────────┐
│  MONETARY SUPPLY TABLE: Regulating Ecosystem Services                  │
│                                                                        │
│  ┌──────────────────┬─────────────┬──────────┬───────────┬──────────┐  │
│  │ Service          │ Coral Reefs │ Seagrass │ Mangroves │ Total    │  │
│  ├──────────────────┼─────────────┼──────────┼───────────┼──────────┤  │
│  │ Nursery          │ [currency]  │[currency]│ —         │ [total]  │  │
│  │ (market-based    │             │          │           │          │  │
│  │  indirect)       │             │          │           │          │  │
│  ├──────────────────┼─────────────┼──────────┼───────────┼──────────┤  │
│  │ Carbon seq.      │ —           │[currency]│ [currency]│ [total]  │  │
│  │ (NON-MARKET:     │             │          │           │          │  │
│  │  shadow price)   │             │          │           │          │  │
│  ├──────────────────┼─────────────┼──────────┼───────────┼──────────┤  │
│  │ Coastal protect. │ [currency]  │ —        │ [currency]│ [total]  │  │
│  │ (NON-MARKET:     │             │          │           │          │  │
│  │  replacement     │             │          │           │          │  │
│  │  cost)           │             │          │           │          │  │
│  ├──────────────────┼─────────────┼──────────┼───────────┼──────────┤  │
│  │ Sediment nour.   │ [currency]  │[currency]│ —         │ [total]  │  │
│  │ (NON-MARKET:     │             │          │           │          │  │
│  │  replacement     │             │          │           │          │  │
│  │  cost)           │             │          │           │          │  │
│  └──────────────────┴─────────────┴──────────┴───────────┴──────────┘  │
│                                                                        │
│  IMPORTANT: Label each value with its valuation type                   │
└─────────────────────────────────────────────────────────────────────────┘
```

### 6.3 Use Table (Regulating Services)

| Service | User / Beneficiary |
|---|---|
| Fisheries nursery | Fisheries sector (indirect) |
| Carbon sequestration | Global community |
| Coastal protection | Coastal households, businesses, government infrastructure |
| Sediment nourishment | Coastal communities, tourism sector |

---

## 7. Data Quality and Limitations

| Service | Issue | Impact | Mitigation |
|---|---|---|---|
| Nursery | LRR values from literature, not locally calibrated | Moderate uncertainty | Conduct local density comparison studies |
| Carbon seq. | NCP rates from literature, limited local calibration | Low–moderate uncertainty (physical) | Update with local biomass accumulation data |
| Carbon seq. | SCC value is a policy choice with wide range | High sensitivity (monetary) | Report sensitivity analysis across SCC scenarios |
| Coastal prot. | Lower-bound estimate (replacement cost only) | Underestimates true value | Document limitations; consider complementary methods |
| Coastal prot. | Engineering costs vary by construction market | Site-specific uncertainty | Use locally sourced cost data |
| Sediment | Carbonate production rates from literature | Moderate uncertainty | Update with local reef production studies |
| Sediment | Beach nourishment costs vary by location | Site-specific uncertainty | Use locally sourced cost data |

---

## 8. Implementation Checklist

### Fisheries Nursery Service
- [ ] **Obtain** fish density data from areas with and without nursery habitat
- [ ] **Apply** Log Response Ratio (LRR) values (coral reef: 31%, seagrass: 13%)
- [ ] **Calculate** enhanced juvenile production from total fish biomass
- [ ] **Apply** juvenile mortality rate (95%) to estimate harvestable contribution
- [ ] **Value** harvestable contribution at market price of landed fish
- [ ] **Compile** physical and monetary supply and use tables

### Carbon Sequestration
- [ ] **Obtain** ecosystem extent from the extent account (mangrove and seagrass ha)
- [ ] **Apply** Net Carbon Production rates (mangrove: 17.23, seagrass: 4.44 Mg CO2/ha/yr)
- [ ] **Calculate** total annual sequestration (Mg CO2/yr)
- [ ] **Select** valuation approach: SCC (shadow price) or market-based (carbon exchange) — document rationale
- [ ] **Calculate** monetary value (sequestration × SCC or market price)
- [ ] **Convert** to local currency if using SCC in USD
- [ ] **Conduct** sensitivity analysis at multiple SCC values or compare SCC vs market pricing
- [ ] **Document** whether monetary value is a non-market shadow price or market-based
- [ ] **Compile** physical and monetary supply and use tables

### Coastal Protection
- [ ] **Define** coastal buffer zone (uniform 100 m, or differentiated by exposure: 100 m low energy / 300 m high energy)
- [ ] **Map** protective ecosystem features (reefs and mangroves) from extent account
- [ ] **Overlay** building footprints with buffer zone; count and categorise
- [ ] **Measure** total protected coastline length (m)
- [ ] **Obtain** local construction cost data and engineering replacement benchmarks
- [ ] **Assign** defence types to coastline segments by exposure and wave energy
- [ ] **Calculate** replacement cost (segment length × unit cost)
- [ ] **Produce** spatial maps (buffer zone, buildings, reef systems)
- [ ] **Compile** physical and monetary supply and use tables

### Sediment Nourishment
- [ ] **Obtain** coral reef carbonate production rate for bioregion
- [ ] **Measure** reef crest length from GIS data
- [ ] **Estimate** seagrass epibiontic CaCO3 production
- [ ] **Calculate** total physical sediment supply (m^3 CaCO3/yr)
- [ ] **Obtain** local beach nourishment cost data (currency/m^3)
- [ ] **Calculate** monetary value (sediment production × nourishment cost)
- [ ] **Compile** physical and monetary supply and use tables

### Cross-cutting
- [ ] **Assess** data quality for each service; flag data-deficient components
- [ ] **Document** metadata: data sources, assumptions, limitations, accounting period
- [ ] **Label** all monetary values with valuation type (market-based vs non-market)

---

## 11. Tiered Assessment

### Overview

This skill implements physical measurement and monetary valuation for four regulating services. Tier profiles differ substantially across the services, with carbon sequestration and coastal protection being the most resource-intensive at higher tiers. The current SOP implements Tier 2 approaches for most sub-procedures.

### Fisheries Nursery Service

**Physical measurement tier profile:**
Reference Section 4 fisheries nursery rows:
- Tier 1: Literature-based habitat contribution factors applied to extent data; A=1, B=1, C=1–2
- Tier 2: Regionally calibrated nursery function estimates with connectivity modelling; A=2, B=2, C=2
- Tier 3: Otolith microchemistry, acoustic telemetry, or stable isotope tracing; A=3, B=2–3, C=3

| Sub-procedure | Current approach | A | B | C |
|---|---|---|---|---|
| Habitat contribution factor (LRR or literature) | Literature LRR values per species-habitat pair | 1–2 | 1–2 | 1–2 |
| Ecosystem extent input (from extent account) | Sentinel-2 classification | 2 | 2 | 2 |
| Nursery service supply (tonnes/yr attributed to habitat) | Habitat-attributed fish biomass x contribution factor | 2 | 1–2 | 2 |

Current overall: **Tier 2** on A and C; **Tier 1–2** on B. Binding constraint: B-accuracy limited by high uncertainty in literature LRR values (CV typically >50%). This means nursery service estimates should be reported as Tier 1 on accuracy regardless of other sub-procedure quality.

**Monetary valuation tier profile:**
Reference Section 4a nursery valuation:
- Tier 1: Residual value method (nursery-attributed proportion of fish catch value from literature)
- Tier 2 (current default): Productivity change — habitat-attributed fish biomass x market price
- Tier 3: Stochastic production frontier (SPF) econometric estimation; or NPV of nursery service cash flows

Monetary dimension scores for Tier 2:
- A=2, B=2, B-temporal=2, C=2, D=2 (productivity change is an exchange value)

### Carbon Sequestration

**Physical measurement tier profile:**
Reference Section 4 carbon sequestration rows:
- Tier 1: IPCC Tier 1 defaults applied to extent from global maps; A=1, B=1, C=1
- Tier 2: Country-specific emission factors from literature; national extent mapping; A=1–2, B=2, C=2
- Tier 3: Flux measurements, sediment coring, allometric equations from local plots; A=3, B=3, C=3

| Sub-procedure | Current approach | A | B | C |
|---|---|---|---|---|
| NCP rate (net carbon production per ha) | Literature rates by ecosystem type and condition class | 1 | 1–2 | 1 |
| Ecosystem extent input | From extent account (Sentinel-2) | 2 | 2 | 2 |
| Condition adjustment (if applied) | Condition index from condition accounts used to adjust NCP rate | 2 | 2 | 2 |
| Carbon sequestration supply (Mg CO2/yr) | NCP rate x extent x condition adjustment | 1–2 | 1–2 | 1–2 |

Current overall: **Tier 1–2** across dimensions. B-accuracy is Tier 1 if global default NCP rates used; Tier 2 if country-specific literature values with documented uncertainty ranges.

Note: The distinction between carbon stock retention (asset account) and annual carbon sequestration (service flow) must be maintained. Both are distinct flows and must not be double-counted.

**Monetary valuation tier profile:**
Reference Section 4a carbon sequestration valuation:
- Tier 1: Value transfer from ESVD; or published SCC per tonne CO2 from comparable contexts
- Tier 2 (current default): SCC x net annual sequestration (Mg CO2/yr)
- Tier 3: Maintenance cost approach; or NPV: V = Σ [R_t/(1+r)^t]

Monetary dimension scores for Tier 2:
- A=1–2, B=2, B-temporal=2 (SCC updates annually from consistent sources), C=1–2, D=2 (SCC is an exchange value proxy consistent with NCAVES Category V)

Note on SCC: the social cost of carbon is a Category V (expected/simulated expenditure) valuation approach. Exchange value consistency (D) requires documenting that SCC represents the social willingness to pay for avoided emissions, which is an exchange value approximation rather than a welfare surplus.

### Coastal Protection

**Physical measurement tier profile:**
Reference Section 4 coastal protection rows:
- Tier 1: Replacement cost or global average avoided damage per hectare; A=1, B=1, C=1
- Tier 2: Expected damage function with regional storm data and stratified exposure; A=2, B=2, C=2–3
- Tier 3: Hydrodynamic modelling with local calibration and probabilistic damage assessment; A=3, B=3, C=3

| Sub-procedure | Current approach | A | B | C |
|---|---|---|---|---|
| Exposed asset inventory (building footprints, population) | National GIS data | 1–2 | 2 | 1–2 |
| Storm/wave return period data | Regional cyclone/wave database | 2 | 2 | 2 |
| Coastal protection physical supply metric (people/assets protected) | Ecosystem width x attenuation factor from literature | 2 | 2 | 2–3 |
| Wave attenuation parameterisation | Literature attenuation coefficients (no local calibration) | 1 | 1–2 | 1 |

Current overall: **Tier 2** on A; **Tier 1–2** on B (binding constraint: wave attenuation coefficients from literature, no local hydrodynamic calibration); **Tier 2–3** on C (requires multi-agency data).

**Monetary valuation tier profile:**
Reference Section 4a coastal protection valuation:
- Tier 1: Value transfer — global average avoided damage per ha from ESVD (Barbier et al. 2011)
- Tier 2 (current default): Annualised replacement cost of equivalent hard infrastructure (seawall/quaywall)
- Tier 3: Expected damage function (EDF) using hydrodynamic modelling (Menendez et al. 2020); or insurance premium differential

Monetary dimension scores for Tier 2 (replacement cost):
- A=2, B=2, B-temporal=2, C=2, D=2 (replacement cost is a Category V approach; exchange value consistency requires that cost reflects what a beneficiary would pay to maintain the same protection standard)

### Sediment Nourishment

**Physical measurement tier profile:**
Reference Section 4 sediment nourishment rows:
- Tier 1: Proxy indicators with literature rates; A=1, B=1, C=1–2
- Tier 2: Sediment budget approach using regional accretion rates and shoreline change; A=2, B=2, C=2
- Tier 3: Sediment transport modelling calibrated with field measurements; A=3, B=2–3, C=3

| Sub-procedure | Current approach | A | B | C |
|---|---|---|---|---|
| Sediment accretion/supply rate | Literature rates by ecosystem type | 1 | 1 | 1 |
| Ecosystem extent input | From extent account | 2 | 2 | 2 |
| Sediment supply metric (m3/yr or tonnes/yr) | Rate x extent | 1 | 1–2 | 1 |
| Shoreline change / beneficiary area | Satellite-derived or regional estimate | 2 | 2 | 2 |

Current overall: **Tier 1–2** across dimensions. B-accuracy is typically Tier 1 because global/regional literature accretion rates have very high uncertainty (CV >50%) for specific site conditions.

Note: The framework explicitly states (Section 4, sediment nourishment) that Tier 3 on accuracy is not achievable with sediment transport modelling alone (B=2–3 at most), reflecting the inherent difficulty of measuring this service. The guidance from Section 6.4 on accepting Tier 1 applies here.

**Monetary valuation tier profile:**
Reference Section 4a sediment nourishment valuation:
- Tier 1: Value transfer — published beach nourishment unit cost x physical supply
- Tier 2 (current default): Local beach nourishment cost (currency/m3) x physical sediment supply (m3/yr)
- Tier 3: Avoided erosion damage cost — requires sediment transport modelling and asset exposure mapping

Monetary dimension scores for Tier 2:
- A=1–2, B=2, B-temporal=2, C=1–2, D=2 (nourishment cost is a Category V replacement cost; exchange value consistency straightforward)

### Double-Counting Note

Reference the framework's double-counting caution (Section 4a.3). Specifically for regulating services:
- Fisheries nursery and wild fish provisioning share the same fish stock: ensure nursery service is measured as the habitat-attributed counterfactual reduction in catch, not as an additional harvest.
- Sediment nourishment and coastal protection may protect the same coastal assets in beach-backed reef systems: review whether the same asset is protected by both services before aggregating values.
- Carbon sequestration and carbon stock retention are distinct flows: annual sequestration (service flow) and standing stock (asset value) must not both be monetised against the same tonne of carbon.

### Progression Pathway

For each service, priority investments to reach the next tier:
- Fisheries nursery — Tier 3 on B-accuracy: otolith microchemistry or stable isotope tracing to empirically calibrate habitat contribution
- Carbon sequestration — Tier 2 on B-accuracy: use country-specific literature NCP rates with documented uncertainty; Tier 3: flux tower measurements or sediment coring
- Coastal protection — Tier 3: implement coupled hydrodynamic-wave model (e.g., Delft3D or XBeach) calibrated with local bathymetry and wave buoy data
- Sediment nourishment: accept Tier 1–2 as appropriate given methodological frontier limitations; invest in regional accretion rate literature synthesis

---

*Derived from: SEEA EA Ecosystem Service Accounts (Sections 6.2–6.5). Examples from ENDhERI Project — Compiling the first Natural Capital Accounts in the Maldives. Alternative methods from: Applying SEEA EA at the Project Level in Central Java (RNF BCAF, GOAP, 2025). Aligned with UN SEEA EA (2021), CICES v5.1, and GOAP technical guidance.*

---

## 9. Tiered Physical Measurement Methods

This section provides alternative physical measurement methods at three resource/accuracy tiers, following the Tiered Assessment Framework. **Physical values only** — monetary valuation is covered separately in each SOP's Part B.

### 9.1 Fisheries Nursery — Additional Harvestable Biomass (kg/yr)

#### Tier 1: Literature LRR Applied to National Catch Data

**Method:** Apply published Log Response Ratios from global/tropical meta-analyses to national fisheries catch data (from provisioning account) for nursery-dependent species families. LRR quantifies proportional increase in fish density in areas with nursery habitat vs unstructured habitat. Apply juvenile survival rate (default 5%) to estimate recruitment to fishery.

| Attribute | Detail |
|---|---|
| Physical output | Additional harvestable biomass (kg/yr) by ecosystem type — indicative |
| Formula | Nursery contribution = Catch of nursery-dependent spp × LRR × Survival rate (0.05) |
| Key parameters | Coral reef LRR: 31% (Lefcheck et al. 2019); Seagrass LRR: 13%; Survival: 5% (range 2–10%) |
| Key source | ENDhERI Project, *Compiling the first Natural Capital Accounts in the Maldives: Methods Report*, Section 6.2, GOAP/UNEP, 2025 |
| Data inputs | National/subnational fisheries catch (kg/yr); nursery-dependent species list (FishBase); LRR values; juvenile survival rate; ecosystem extent (ha) |
| Budget | < USD 10,000 |
| Time | 1–3 months |
| CV | > 50% — global LRR obscures near-zero to >100% site-level variation; sensitivity cascade across 4 multiplicative parameters can produce 3–4× estimate range |

**Mandatory sensitivity analysis:** Vary survival rate 2–10% and LRR ±50%.

#### Tier 2: Locally Calibrated Density Comparison with Cohort Export

**Method:** Replace global LRR with locally derived fish density enhancement from UVC or BRUV surveys at paired nursery vs non-nursery sites. Calculate family-specific juvenile export to fishery using locally observed juvenile densities, species-specific juvenile phase durations, and family-specific mortality rates.

| Attribute | Detail |
|---|---|
| Physical output | Family-specific adults exported to fishery (individuals/yr and kg/yr) by ecosystem type |
| Key source | ENDhERI Project (2025), Section 6.2.1–6.2.2 — worked example with Maldives Resilient Reefs survey data |
| Supporting sources | WorldFish Center, *Small-Scale Fisheries Monitoring: A Practical Guide*, 2018 |
| Data inputs | Paired fish density surveys (nursery vs non-nursery); nursery habitat extent (Sentinel-2, 10 m); juvenile density per ha by family; juvenile phase duration (months); family-specific mortality rates; adult weight from FishBase L-W relationships |
| Budget | USD 10,000–100,000 |
| Time | 3–12 months |
| CV | 20–50% — site-specific but not individually verified fish origin |

#### Tier 3: Direct Nursery Origin Verification

**Method:** Directly determine what proportion of adult fish in the harvest originated from specific nursery habitats. Three principal techniques: (a) **Otolith microchemistry** — trace element ratios in juvenile core of adult otoliths matched against reference nursery signatures; (b) **Acoustic telemetry** — tagged juveniles tracked from nursery to adult habitats; (c) **Stable isotope tracing** — tissue δ¹³C/δ¹⁵N/δ³⁴S distinguish nursery vs non-nursery food web origins via isotopic mixing models (MixSIAR).

| Attribute | Detail |
|---|---|
| Physical output | Proportion of adult harvest originating from each nursery type (kg/yr) — empirically verified |
| Key source | Tiered Assessment Framework (2026), line 137 — identifies these as Tier 3 nursery methods |
| Supporting sources | Gillanders, B.M. et al. (2003) — otolith microchemistry protocols |
| | Nagelkerken, I. et al. (2015) — meta-analysis of nursery function providing context for LRR variation |
| Data inputs | (Otolith) Adult otolith samples (min 30–50 per species per habitat) + juvenile reference signatures + LA-ICP-MS facility. (Telemetry) Acoustic transmitters + receiver array (12–24 months). (Isotopes) Tissue samples + baseline signatures from each habitat + mixing model software |
| Budget | > USD 100,000 |
| Time | > 12 months |
| CV | < 20% — directly traces individual fish to nursery origin, resolving the ambiguity inherent in Tiers 1–2 |

---

### 9.2 Carbon Sequestration — Annual Sequestration (Mg CO2/yr)

#### Tier 1: IPCC Tier 1 Defaults Applied to Global Extent Maps

**Method:** Multiply ecosystem extent (ha) from globally available maps by IPCC Tier 1 default NCP rates from the 2013 Wetlands Supplement. No site-specific field data required.

| Attribute | Detail |
|---|---|
| Physical output | Total sequestration (Mg CO2/yr) by ecosystem type — indicative |
| Formula | Total sequestration = Extent (ha) × Default NCP rate (Mg CO2/ha/yr) |
| Key source | IPCC, *2013 Supplement to the 2006 IPCC Guidelines for National Greenhouse Gas Inventories: Wetlands*, Chapter 4, 2014. URL: ipcc-nggip.iges.or.jp/public/wetlands |
| Supporting sources | Global Mangrove Watch (GMW) v3.0 — 25 m extent, freely available. URL: globalmangrovewatch.org |
| | UNEP-WCMC Global Seagrass Distribution |
| Default rates | Mangrove soil C accumulation: ~1.62 Mg C/ha/yr (IPCC Table 4.11); Seagrass soil C burial: ~0.43 Mg C/ha/yr (IPCC Table 4.13). CO2 conversion: × 3.67 |
| Budget | < USD 10,000 |
| Time | 1–3 months |
| CV | > 50% — global averages; no condition stratification |

#### Tier 2: Regionally Calibrated Rates with National Extent Mapping

**Method:** Replace IPCC defaults with country-specific or regionally calibrated NCP rates from literature synthesis. Apply to nationally produced extent maps (Sentinel-2 at 10 m). Stratify by ecosystem condition class (intact, degraded, regenerating) where possible, assigning class-specific sequestration rates.

| Attribute | Detail |
|---|---|
| Physical output | Sequestration (Mg CO2/yr) by ecosystem type, stratified by condition class |
| Key source | GOAP, *Applying SEEA EA at the Project Level in Central Java* (RNF BCAF), 2025 — condition stratification recommendation |
| Supporting sources | ENDhERI (2025) — literature NCP rates: mangrove 17.23 Mg CO2/ha/yr (Kamruzzaman et al. 2017); seagrass 4.44 Mg CO2/ha/yr (Ganguly et al. 2017) |
| | Murdiyarso et al. (2023) — Tier 2 SOC rate: 1.2 ± 0.2 Mg C/ha/yr for degraded mangrove |
| Data inputs | National Sentinel-2 extent (10 m) with field validation; condition classification (satellite-derived + ground-truthing); regional NCP rates from literature synthesis; carbon content fractions (mangrove 42%, seagrass 35%) |
| Budget | USD 10,000–100,000 |
| Time | 3–12 months |
| CV | 20–50% — condition-stratified; regional parameters |

#### Tier 3: Permanent Plots, Sediment Coring, and Direct Measurement

**Method:** Three integrated measurement streams: (a) **Above/below-ground biomass** from permanent plots (all trees ≥ 5 cm DBH tagged, re-measured at 2+ yr intervals) with species-specific allometrics (AGB = a × ρ × DBH^b); C fractions 47% AGB, 39% BGB. (b) **Soil organic carbon** from sediment coring + Walkley-Black wet-oxidation or elemental analysis. (c) **Burial rates** from radiometric dating (Pb-210, Cs-137).

| Attribute | Detail |
|---|---|
| Physical output | Site-specific sequestration rates (Mg CO2/yr) by ecosystem type and carbon pool, with documented uncertainty |
| Key source | CIFOR, *Protocols for the Measurement, Monitoring and Reporting of Structure, Biomass and Carbon Stocks in Mangrove Forests* (Kauffman & Donato), Working Paper 86, 2012. URL: cifor.org |
| Supporting sources | Howard, J. et al. (2014), *Coastal Blue Carbon: Methods for Assessing Carbon Stocks and Emissions Factors*, Conservation International / IOC-UNESCO / IUCN. URL: thebluecarboninitiative.org/manual |
| | GOAP RNF BCAF (2025) — 13 permanent plots, 11 allometric sources, yielding 24,227 Mg C (88,831 Mg CO2e) for Central Java |
| Data inputs | Permanent plots (min 0.1 ha each, all trees ≥ 5 cm DBH); species-specific allometrics; wood density; soil cores (10–100 cm depth); laboratory SOC analysis; radiometric dating; high-resolution extent (drone/<5 m) |
| Budget | > USD 100,000 |
| Time | > 12 months |
| CV | < 20% with adequate sampling — but high plot-to-plot variability can compound through allometrics |

---

### 9.3 Coastal Protection — Protected Assets and Coastline (buildings, metres)

#### Tier 1: GIS Buffer and Asset Counting

**Method:** Define a fixed-distance buffer zone (100 m) landward from shoreline on coastlines fronted by reef or mangrove. Overlay building footprints from global datasets (Google Open Buildings v3). Count buildings by type. Measure protected coastline length. Variant: differentiated buffers (100 m low-energy coast; 300 m high-energy coast) with mangrove typology classification and grey infrastructure exclusion.

| Attribute | Detail |
|---|---|
| Physical output | Number/type of protected buildings; total protected coastline (m); spatial maps |
| Key source | ENDhERI (2025) — 100 m buffer, 778 buildings, 33,142 m coastline (Laamu Atoll) |
| Supporting sources | GOAP RNF BCAF (2025) — differentiated buffers, 30,500+ buildings, 64.58 km coastline (Central Java) |
| | ABS, *Experimental Environmental-Economic Accounts: Coastal Protection Services*, 2022. URL: abs.gov.au |
| Data inputs | Ecosystem extent maps; Google Open Buildings v3 or Microsoft Building Footprints; coastline shapefile; GIS software (QGIS — free) |
| Budget | < USD 10,000 |
| Time | 1–3 months |
| CV | > 50% — assumes binary protection; ignores topography, wave exposure, reef condition |

#### Tier 2: Expected Damage Function with Regional Storm Data

**Method:** Probabilistic expected damage framework combining: (a) storm frequency/intensity from regional databases (IBTrACS, EM-DAT); (b) exposure analysis using DEM (SRTM 30 m or FABDEM); (c) generic depth-damage curves; (d) ecosystem attenuation factor from meta-analyses. Alternative: InVEST Coastal Vulnerability model (freely available) producing a relative exposure index per coastal segment with/without ecosystems.

| Attribute | Detail |
|---|---|
| Physical output | Expected annual avoided flooding (buildings, people, area); relative exposure index per segment |
| Key source | Beck, M.W. & Lange, G.-M. (eds.), *Managing Coasts with Natural Solutions*, World Bank WAVES, 2016. URL: documents.worldbank.org |
| Supporting sources | TNC, *Mapping Ocean Wealth*, 2017. URL: oceanwealth.org |
| | Natural Capital Project, *InVEST Coastal Vulnerability Model*. URL: invest.readthedocs.io |
| | UNDRR, *Global Assessment Report on Disaster Risk Reduction 2022* |
| Data inputs | IBTrACS/EM-DAT storm data; SRTM 30 m or FABDEM; building footprints; ecosystem extent at 10 m; depth-damage curves; meta-analysis wave attenuation rates; condition data for stratification |
| Budget | USD 10,000–100,000 |
| Time | 3–12 months |
| CV | 20–50% — condition-responsive; risk-stratified |

#### Tier 3: Coupled Hydrodynamic Modelling

**Method:** Process-based numerical models simulating wave propagation and attenuation across reef/mangrove systems. Couples regional hydrodynamic model (ADCIRC or Delft3D) + spectral wave model (SWAN) + nearshore dissipation model (XBeach). Paired "with/without ecosystem" scenarios quantify avoided flood extent, depth, and wave run-up. Full probabilistic variant simulates 1,000–10,000 synthetic storms producing exceedance probability curves.

| Attribute | Detail |
|---|---|
| Physical output | Avoided flood area (ha); avoided flood depth (m); wave height reduction (m); exceedance probability curves |
| Key source | Storlazzi, C.D. et al., *Mapping the Global Value of Coral Reef Coastal Protection*, USGS Open-File Report 2019-1027. URL: pubs.usgs.gov/of/2019/1027 |
| Supporting sources | TNC / Swiss Re, *Risky Business: Insurance, Reefs, and the Value of Coral Ecosystems*, 2019 |
| | Menendez, P. et al., *The Global Flood Protection Benefits of Mangroves*, TNC/IH Cantabria/World Bank, 2020. URL: oceanwealth.org/mangrove-flood-protection |
| Data inputs | High-resolution bathymetry (<10 m on reef flat); topographic LiDAR (<5 m); tidal records (10+ yr); wave buoy data; reef structural parameters (width, crest depth, rugosity); mangrove parameters (stem density, root diameter); storm climatology; HPC cluster |
| Budget | > USD 100,000 |
| Time | > 12 months |
| CV | < 20% where fully calibrated |

---

### 9.4 Sediment Nourishment — CaCO3 Production (m³/yr)

#### Tier 1: Literature-Transfer Sediment Delivery Rate

**Method:** Apply a single published average net carbonate sediment delivery rate (m³/m/yr) from a regional meta-analysis to total reef-adjacent shoreline length measured from global extent maps. For seagrass: average epibiontic CaCO3 rate × extent / CaCO3 density.

| Attribute | Detail |
|---|---|
| Physical output | Annual sediment production (m³ CaCO3/yr) by ecosystem type |
| Formula | Coral: Production rate (m³/m/yr) × shoreline length (m). Seagrass: Rate (kg/m²/yr) × extent (m²) / density (2,711 kg/m³) |
| Key source | ENDhERI (2025), Section 6.5 — rate of 0.049 m³/m/yr from Ainesi et al. (2024) meta-analysis of Indo-Pacific reef islands |
| Supporting sources | East, H.K. et al. (2023) — species-specific seagrass epibiontic CaCO3 rates (Tc: 2.7 Mg/ha/yr; Th: 0.7 Mg/ha/yr) |
| Data inputs | Average sediment delivery rate from regional literature; reef crest/shoreline length from GIS (Allen Coral Atlas); seagrass extent; epibiontic CaCO3 rate; CaCO3 density constant |
| Budget | < USD 10,000 |
| Time | 1–3 months |
| CV | > 50% — insensitive to reef condition; net production varies from negative (degraded) to >0.15 m³/m/yr (highly productive) |

#### Tier 2: Condition-Adjusted Carbonate Budget (ReefBudget Regression)

**Method:** Use published empirical relationship between live coral cover and net carbonate production (Perry et al. 2018 for Indian Ocean) applied to benthic monitoring data from national/regional reef programmes (GCRMN data). Stratify by reef zone and condition class. For seagrass: species-specific epibiontic rates applied to field-measured species composition data.

| Attribute | Detail |
|---|---|
| Physical output | Net CaCO3 production (m³/yr) stratified by reef zone, island, and condition class |
| Key source | Perry, C.T. et al., *ReefBudget: Carbonate Budget Methodology*, University of Exeter. URL: geography.exeter.ac.uk/reefbudget |
| Supporting sources | GCRMN/ICRI, *Status of Coral Reefs of the World: 2020*, 2021. URL: gcrmn.net/2020-report |
| | TNC, *Mapping Ocean Wealth* project and datasets. URL: oceanwealth.org |
| Data inputs | Live coral cover (%) from monitoring programme; coral community composition (genus, growth form); coralline algae cover; reef extent by zone (Allen Coral Atlas geomorphic zonation); seagrass species composition and cover; bioerosion estimates from ReefBudget lookup tables |
| Budget | USD 10,000–50,000 |
| Time | 3–12 months |
| CV | 20–50% — condition-responsive but still relies on literature-derived calcification/bioerosion rates; does not model sediment transport pathways |

#### Tier 3: Full Field Carbonate Budget with Sediment Transport Modelling

**Method:** (a) Full ReefBudget field census: UVC of coral colonies (dimensions, genus, growth form), parrotfish and urchin counts, boring sponge and coralline algae cover. (b) Sediment trap deployment at reef-to-shore transects capturing actual flux rates and grain-size distributions. (c) Sediment transport modelling (XBeach, Delft3D, MIKE21) calibrated with local bathymetry and wave climate, tracing produced carbonate from reef to shoreline.

| Attribute | Detail |
|---|---|
| Physical output | Net CaCO3 production and modelled delivery to specific shoreline segments (m³/yr) — spatially explicit |
| Key source | Perry, C.T. et al., *ReefBudget Indo-Pacific and Caribbean Methodology Workbooks*, University of Exeter. URL: geography.exeter.ac.uk/reefbudget |
| Supporting sources | USGS Pacific Coral Reef Research Program — carbonate budget and sediment transport reports (Storlazzi et al.). URL: usgs.gov/centers/pcmsc |
| | SPC, *Pacific Reef and Island Resilience Science Plan*, 2021 |
| Data inputs | Coral colony census (genus, growth form, dimensions); parrotfish/urchin census; boring sponge and CCA cover; sediment traps; grain-size analysis; multibeam bathymetry (<5 m); wave buoy/hindcast; tidal records; sediment transport model |
| Budget | > USD 100,000 |
| Time | > 12 months |
| CV | < 20% where fully calibrated — appropriate for atoll nations where sediment supply is existentially important |

**Note:** The tiered assessment framework (Section 6.4) identifies sediment nourishment as a service where "Tier 1 may be acceptable as a permanent state rather than merely a stepping stone," because the methodological frontier does not yet offer a clear Tier 2 path for most countries.

---

## 10. Expert Review: Regulating Ecosystem Service Accounts

**Reviewer expertise:** Marine ecosystem services science, carbon biogeochemistry, coastal geomorphology, reef ecology
**Scope:** Service-by-service assessment of feasibility, accuracy, and difficulty, with tiered ratings and actionable recommendations

---

### 9.1 Fisheries Nursery Service

#### Feasibility — Tier 2

The method requires fish density comparison data from areas with and without nursery habitat, which presents a real bottleneck. Underwater visual census (UVC) data at the spatial resolution needed to distinguish "with nursery" from "without nursery" areas is not routinely collected outside of dedicated research programmes. The fallback — applying literature LRR values to total catch data — is feasible but fundamentally changes what the method is measuring: it shifts from a locally grounded productivity comparison to a benefit-transfer exercise.

The LRR approach itself is conceptually sound and well-established in fisheries ecology (Halpern 2003; Lester et al. 2009), but the step of obtaining "total fish biomass in accounting area" (Step 3) is poorly defined. The SOP says to "apply LRR to total fish biomass," but the ENDhERI report uses catch data from the provisioning service account rather than standing biomass surveys. This conflation between standing stock biomass and annual harvest needs clarification.

**Key feasibility constraint:** Paired fish density data (nursery vs. non-nursery) are rarely available. Most users will default to the literature LRR values, which is acceptable but should be explicitly presented as the standard pathway rather than a fallback.

#### Accuracy — Tier 3

Several compounding uncertainties make this the least accurate of the four services:

**The 31% and 13% LRR values.** These are presented as fixed parameters from "scientific literature (meta-analysis)" but without specific citation. The likely sources are meta-analyses such as Nagelkerken et al. (2015), where LRR values vary enormously depending on species assemblage, reef structure, latitude, and proximity to other habitats. A single LRR for "coral reef" globally obscures variation that can span from near-zero to over 100% enhancement. For Indo-Pacific reefs specifically, the 31% figure is plausible as a central tendency but the confidence interval is wide.

**The 95% juvenile mortality rate.** Described as a "standard ecological assumption," but juvenile mortality in coral reef fishes is highly species-specific and density-dependent. Published estimates range from approximately 80% to 99%+ depending on species and predation environment (Doherty et al. 2004; Almany & Webster 2006). A shift from 95% to 90% mortality doubles the final estimate. This parameter is the single largest source of sensitivity in the entire nursery calculation and the SOP does not flag it as requiring sensitivity analysis.

**Sensitivity cascade.** The final monetary value is the product of four uncertain parameters: total biomass x LRR x survival rate x market price. Error propagation through this chain means that even moderate uncertainty in each parameter can produce a final estimate that varies by a factor of 3–4x. The SOP includes no sensitivity analysis requirement for the nursery service, unlike the carbon sequestration SOP which correctly mandates one.

#### Difficulty — Tier 2

The calculation itself is arithmetically simple. The difficulty lies in: (a) correctly interpreting what the LRR applies to — standing biomass vs. catch; (b) understanding that the 95% mortality rate is not a fixed constant but a parameter that should be varied; and (c) recognising that the method implicitly assumes all enhanced juvenile production is additional to what would exist without the nursery. A fisheries ecologist would navigate these issues; a GIS analyst following the SOP alone likely would not.

#### Recommendations

1. **Mandatory sensitivity analysis.** Add a sensitivity analysis step equivalent to the carbon sequestration SOP. At minimum, vary the juvenile survival rate between 2% and 10% (mortality 90–98%) and the LRR by +/−50% of the central value.
2. **Clarify the biomass input.** Explicitly state whether the LRR is applied to standing stock biomass from underwater surveys or to annual catch data from the provisioning service account. Acknowledge the transfer assumption if using catch data.
3. **When local fish density data are unavailable.** Use provisioning service catch data disaggregated by ecosystem type, apply literature LRR values, apply a survival rate range of 2–10%, and report the nursery value as a range rather than a point estimate.
4. **Cite the meta-analysis source.** Each parameter should be traceable to a named publication with year so users can assess relevance to their site.
5. **Consider species-specific nursery dependency.** Restrict the calculation to species with documented juvenile dependence on nursery habitat (e.g., Lutjanidae, Haemulidae, Siganidae in the Indo-Pacific) rather than applying to all reef-associated biomass.

---

### 9.2 Carbon Sequestration

#### Feasibility — Tier 1

This is the most straightforward of the four services to implement. The data chain is: extent (ha) x NCP rate (Mg CO2/ha/yr) = physical account; physical account x SCC = monetary account. Extent data should already exist from the extent account. NCP rates are readily available from global or regional meta-analyses (e.g., Ouyang & Lee 2020 for mangroves; Fourqurean et al. 2012 for seagrass). SCC values are published by the U.S. IWG and EPA. The calculation can be completed in a spreadsheet in under an hour.

**Feasibility note:** The SOP lists NCP rates as "published literature (calibrated locally)" but does not explain what local calibration entails. For most users, local calibration will not be possible. The SOP should be explicit that using uncalibrated literature rates is acceptable for a first-generation account.

#### Accuracy — Tier 2

**Physical measurement uncertainty.** The mangrove NCP of 17.23 Mg CO2/ha/yr is high relative to global averages. Global meta-analyses report total NCP in the range of 10–25 Mg CO2/ha/yr depending on species, latitude, and stand age (Alongi 2014; Ouyang & Lee 2020). The seagrass NCP of 4.44 Mg CO2/ha/yr is more conservative and consistent with global estimates of 2–8 Mg CO2/ha/yr for tropical seagrass (Kennedy et al. 2010; Duarte et al. 2013).

The critical accuracy issue is whether the NCP rate represents **net ecosystem production** (accounting for respiration, dissolved carbon export, and methane emissions) or **gross carbon burial**. Seagrass systems can export a significant fraction of fixed carbon as dissolved organic and inorganic carbon, and mangroves can emit methane that partially offsets CO2 sequestration. Using gross burial rates to represent net sequestration could overestimate the climate regulation service by 20–40%.

**Monetary valuation uncertainty.** The SCC sensitivity analysis is well-handled, with three scenarios spanning USD 51–185/Mg CO2. The practical question is: does physical NCP uncertainty or SCC choice dominate the total error budget? For most sites, the SCC choice dominates by a factor of 2–3x, because NCP rates typically vary by +/−50% while SCC varies by +/−260%. This means investing in local NCP calibration, while scientifically valuable, will not substantially narrow the uncertainty in the monetary value.

#### Difficulty — Tier 1

Arithmetically trivial. The main judgement call is SCC selection, which is a policy decision not a scientific one. The SOP handles this well by requiring transparent documentation.

#### Recommendations

1. **When local NCP calibration is worth the investment.** Local calibration is worthwhile when: (i) the ecosystem is atypical for its region; (ii) the account will be updated annually; or (iii) the physical account will be used independently of the monetary account. For a first-generation account using SCC valuation, literature rates are adequate.
2. **Clarify what NCP includes.** Specify whether the 17.23 and 4.44 values include or exclude dissolved carbon export and methane emissions. For SEEA EA purposes, only the net greenhouse gas balance matters.
3. **SCC policy choice.** Recommend that the choice of preferred SCC value be made by the commissioning agency, not by the technical team. This separates the scientific measurement from the policy valuation.
4. **Add coral reef carbon exclusion note.** Explicitly state that coral reefs are excluded from carbon sequestration because reef calcification is a net CO2 source. This is a common point of confusion.

---

### 9.3 Coastal Protection

#### Feasibility — Tier 2

Building footprint data is the most significant constraint. In the Maldives, where islands are small and buildings sparse, footprint data may be derivable from high-resolution satellite imagery (e.g., Google Open Buildings, Microsoft Building Footprints). In more complex coastal settings — mainland coastlines in Southeast Asia, West Africa, or the Pacific — building footprint coverage is incomplete, particularly for informal settlements which are often the most vulnerable.

Engineering replacement cost data (quaywall and sheet pile costs) are obtainable but highly variable. The Maldives values are site-specific; comparable data in other SIDS contexts may require consultation with coastal engineering firms.

The 100m buffer zone is technically simple in GIS but involves a strong assumption: that all buildings within 100m receive meaningful protection from the reef or mangrove. This distance suits the Maldives atoll context where islands are narrow, but on larger landmasses a 100m buffer captures only a thin coastal strip.

#### Accuracy — Tier 3

This is the service with the most structural accuracy concerns:

**The buffer zone approach** ignores: (i) topography and elevation; (ii) wave regime and exposure differences (windward vs. leeward); (iii) reef structural complexity — a healthy reef with high rugosity provides much greater wave attenuation than a degraded, flattened reef at the same extent. The method assumes binary protection: everything within 100m is "protected," everything beyond is not. In reality, protection is a gradient function of distance, bathymetry, and incident wave energy.

**Replacement cost as a proxy** can both overestimate and underestimate. It overestimates protection on leeward coasts where wave exposure is already low. It underestimates on exposed windward coasts where reef attenuation is most critical. It also misses the non-linear relationship between reef health (condition) and protection capacity.

#### Difficulty — Tier 2

Requires GIS competence (buffer operations, overlay analysis) and access to building footprint and coastline datasets. The more difficult component is assigning defence types to coastline segments based on exposure and wave energy, which requires basic coastal engineering understanding.

#### Recommendations

1. **Simplified approaches when GIS capacity is limited.** Use Google Earth Pro to manually digitise buildings within an estimated 100m of the shoreline. Count buildings from high-resolution imagery. Apply a single average replacement cost per building rather than categorising by type.
2. **Alternative buffer widths.** For small atoll islands (<500m wide), 100m is appropriate. For larger islands or mainland coastlines, consider 200–500m. If a DEM is available, replace the buffer with an elevation-based approach (e.g., all buildings below 3m elevation).
3. **Condition-protection linkage.** Explicitly link to the condition account. A reef at reference condition provides full structural protection; a degraded reef provides less. At minimum, require a qualitative statement about reef condition. Ideally, apply a condition-based discount factor.
4. **Annualise the replacement cost.** Clarify whether the value is a stock or flow measure. For SEEA EA supply and use tables, the service should be expressed as an annual flow, typically by dividing by the expected lifetime of the engineered alternative (30–50 years).

---

### 9.4 Sediment Nourishment

#### Feasibility — Tier 3

This is the most data-constrained of the four services. The core parameter — reef carbonate production rate — is available for very few sites globally. Published net carbonate production rates exhibit enormous variation: from negative values (net erosion) on degraded reefs to over 0.15 m^3/m/yr on highly productive reef crests (Perry et al. 2018; Januchowski-Hartley et al. 2017). Converting mass production rates (kg CaCO3/m^2/yr) to volumetric rates per linear metre of reef crest requires additional assumptions about reef width and porosity.

Seagrass epibiontic carbonate production data are even scarcer. Published rates exist for a handful of Mediterranean and Caribbean sites; Indo-Pacific data are sparse.

Beach nourishment cost data are poorly documented in most SIDS and developing tropical countries where this service is most relevant.

#### Accuracy — Tier 3

**Carbonate production rate variability** is the dominant uncertainty. Net reef carbonate production depends on coral community composition, live coral cover, bioerosion rate, and whether the rate accounts for sediment transport (not all sediment produced on the reef reaches the beach). Perry et al. (2018) showed that Indian Ocean reef carbonate budgets shifted from net positive to net negative following the 2016 bleaching event. A fixed rate of 0.049 m^3/m/yr does not capture this dynamism.

**Replacement cost accuracy.** Beach nourishment costs vary by an order of magnitude depending on source material distance, grain size matching, and equipment mobilisation (extremely expensive for remote island sites).

#### Difficulty — Tier 3

This is the most specialist of the four services. Correctly estimating net carbonate production requires understanding of reef carbonate budgets, bioerosion, sediment transport pathways, and unit conversions between mass and volumetric rates. Very few environmental consultancies or national statistics offices have this expertise in-house.

#### Recommendations

1. **When to include this service vs. flagging as data-deficient.** Include when: (i) the accounting area is an atoll or low-lying reef island system where sediment supply is existentially important; (ii) reef carbonate budget data exist from the ReefBudget programme or equivalent; and (iii) beach nourishment has been conducted locally. Otherwise, acknowledge qualitatively and flag monetary value as "data deficient."
2. **Site-specificity of carbonate rates.** Never transfer rates between ocean basins. Within the Indo-Pacific, match rates by reef type and approximate live coral cover. If live coral cover is below approximately 10%, the net carbonate budget is likely near zero or negative.
3. **Simplified physical estimate.** Use the Perry et al. (2018) relationship between live coral cover and net carbonate production for the relevant ocean basin. Obtain live coral cover from the condition account. This ties the estimate to observed reef condition rather than a fixed literature rate.
4. **Consider omitting the monetary value.** The physical account (m^3 CaCO3/yr by ecosystem type) may be more informative and defensible than the monetary value. It can stand alone in the supply table with a note that monetary valuation requires locally sourced cost data.

---

### 9.5 Summary Tier Ratings

| Service | Feasibility | Accuracy | Difficulty |
|---|---|---|---|
| Fisheries Nursery | Tier 2 | Tier 3 | Tier 2 |
| Carbon Sequestration | Tier 1 | Tier 2 | Tier 1 |
| Coastal Protection | Tier 2 | Tier 3 | Tier 2 |
| Sediment Nourishment | Tier 3 | Tier 3 | Tier 3 |

**Interpretation:** Tier 1 = straightforward / high confidence; Tier 2 = moderate; Tier 3 = advanced / low confidence.

Carbon sequestration is the clear "quick win" — straightforward to calculate with moderate accuracy. Sediment nourishment is the most challenging across all three dimensions. Nursery and coastal protection are intermediate but have structural accuracy limitations that additional resources cannot easily resolve.

---

### 9.6 Cross-Cutting Observations

1. **Sensitivity analysis gap.** The carbon sequestration SOP correctly requires sensitivity analysis across SCC values. The other three services have parameters of comparable or greater sensitivity (LRR and mortality rate for nursery; buffer width and defence type for coastal protection; carbonate production rate for sediment) but include no sensitivity analysis requirement. All four services should mandate sensitivity analysis on their most influential parameters.

2. **Condition-service linkage.** The skill file treats ecosystem extent as the primary driver of service supply but does not systematically link ecosystem condition to service capacity. A degraded reef at 5% live coral cover does not provide the same nursery, coastal protection, or sediment production as a reef at 40% cover. The condition account data should be formally connected to the service accounts, at minimum through qualitative flags and ideally through condition-adjusted multipliers.

3. **Stock vs. flow confusion.** The coastal protection account may conflate a stock value (total replacement cost of infrastructure) with an annual flow (the annual service of protection). The SEEA EA framework requires annual flows for supply and use tables. The SOP should clarify the temporal dimension of each value.

4. **Provenance of key parameters.** The LRR values (31%, 13%), NCP rates (17.23, 4.44), mortality rate (95%), and carbonate production rate (0.049) are all presented without specific citations in the skill file. For a document intended to guide replication, each parameter should be traceable to a named publication with year.
