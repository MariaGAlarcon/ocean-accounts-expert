# Standard Operating Procedures: Measuring Ecosystem Services

**Framework:** SEEA EA Ecosystem Service Accounts
**Applicable to:** Coastal and marine ecosystem accounting in tropical and subtropical regions
**Accounting Period:** [Define for your accounting area]
**Total Services Valued:** Seven ecosystem services across three CICES categories

---

## 1. Overview

Ecosystem service accounts record the supply and use of ecosystem services in both physical and monetary terms. Each service is first quantified in physical units (Part A), then valued in monetary terms using an appropriate economic valuation method (Part B). The two parts serve different purposes and can be reported independently.

> **Important note on valuation types:** Not all monetary values represent market transactions. Some ecosystem services (e.g., carbon sequestration, coastal protection) have no functioning market and are valued using non-market methods such as shadow prices or replacement costs. These non-market values represent estimated economic significance, not prices observed in any marketplace. Each SOP below identifies whether the valuation is market-based or non-market.

### 1.1 Ecosystem Services Valued

| # | Ecosystem Service | CICES Category | Providing Ecosystem(s) | SEEA EA Section |
|---|---|---|---|---|
| 1 | Wild fish provisioning | Provisioning | Coral reefs, seagrass, pelagic | 6.1 |
| 1b | Wood provisioning (fuel wood) | Provisioning | Mangroves | 6.1 |
| 2 | Fisheries nursery service | Regulating | Coral reefs, seagrass | 6.2 |
| 3 | Carbon sequestration | Regulating (global climate regulation) | Mangroves, seagrass | 6.3 |
| 4 | Coastal protection | Regulating | Coral reefs, mangroves | 6.4 |
| 5 | Sediment nourishment | Regulating | Coral reefs, seagrass | 6.5 |
| 6 | Recreation — coral reef tourism | Cultural | Coral reefs | 6.6.1 |
| 7 | Recreation — mangrove tourism and seagrass gleaning | Cultural | Mangroves, seagrass | 6.6.2–6.6.3 |

### 1.2 Valuation Methods Summary

| Ecosystem Service | Physical Unit | Primary Valuation Method | Alternative Methods (NCAVES/MAIA) | Value Type |
|---|---|---|---|---|
| Wild fish provisioning | kg/yr | Resource rent (4-component or 5-component with WACC) | Directly observed market prices (Category I) adjusted by resource rent decomposition | Market-based |
| Wood provisioning | kg/yr or tonnes/yr | Substitute-cost (avoided LPG/kerosene energy cost) | Resource rent (stumpage value) where marketed timber data exist | **Non-market** (cost-based proxy) or Market-based |
| Fisheries nursery service | kg biomass/yr | Productivity change (market price) | Residual value method (Tier 1); stochastic production frontier (Tier 3) | Market-based (indirect) |
| Carbon sequestration | Mg CO2/yr | Social Cost of Carbon (SCC) or market-based pricing (carbon exchange) | Maintenance cost approach; value transfer from ESVD | **Non-market** (SCC) or Market-based (exchange price) |
| Coastal protection | Buildings and coastline length protected | Replacement cost (undepreciated or annualised via depreciation) | Expected damage function / avoided damage cost (Tier 3); insurance premium differentials | **Non-market** (cost-based proxy) |
| Sediment nourishment | m^3 CaCO3/yr | Replacement cost (beach nourishment) | Avoided damage cost (erosion damage prevented) | **Non-market** (cost-based proxy) |
| Coral reef recreation | Visitor expenditure/yr | Direct expenditure analysis or activity-based P×Q with intermediate input deductions | Travel cost method / RUM (Tier 2–3); simulated exchange value / SEV (Tier 3); hedonic pricing (Tier 3) | Market-based |
| Mangrove recreation | Trips/yr or visitors/yr | Direct expenditure analysis or activity-based P×Q with intermediate input deductions | Contingent valuation for nascent operations; travel cost method; consumer expenditure method (Tier 1) | Market-based |
| Seagrass gleaning | Hours and harvest/yr | Equivalent wage + market value | Averting behaviour method (lower-bound); value transfer from ESVD | Mixed (market + imputed) |

### 1.3 NCAVES/MAIA Valuation Framework

> **Source:** NCAVES/MAIA (2022), *Monetary Valuation of Ecosystem Services and Assets for Ecosystem Accounting: Interim Version*, 1st Edition.

The NCAVES/MAIA report establishes the international best-practice framework for monetary valuation in SEEA EA ecosystem accounting. Key principles relevant to all services:

**Exchange values, not welfare values.** The SEEA EA requires exchange values — the price at which ecosystem services would be exchanged between a willing buyer and seller — consistent with the System of National Accounts (SNA). Welfare values (which include consumer surplus and non-use values) will generally be higher. Methods that estimate willingness to pay (WTP), such as contingent valuation and choice experiments, capture welfare values and must be converted to exchange values through the simulated exchange value (SEV) method before use in accounts.

**Five-category method typology (Table 1 of NCAVES report):**

| Category | Price Basis | Methods | Typical Tier |
|---|---|---|---|
| I — Directly observable prices | Service traded in markets | Market price (adjusted for distortions) | Tier 1–2 |
| II — Prices from similar markets | Substitute good traded | Surrogate market pricing (e.g., managed pollination cost for wild pollination; carbon credit price for sequestration) | Tier 2 |
| III — Prices embodied in market transactions | Value extracted statistically | Resource rent; hedonic pricing; productivity change | Tier 1–3 |
| IV — Revealed expenditure | Spending reveals value | Averting behaviour; travel expenditure | Tier 2–3 |
| V — Expected/simulated expenditure | No market exists | Replacement cost; avoided damage cost; simulated exchange value (SEV) | Tier 1–3 |

**Value transfer as Tier 1 option.** Where primary valuation is infeasible, value transfer (VT) from existing studies is acceptable as an initial estimate. Three VT methods exist in order of increasing accuracy: (1) unit value transfer (single value from study site, optionally income-adjusted); (2) value function transfer (regression from study site applied with local characteristics); (3) meta-analytic value function transfer (meta-regression across multiple studies). The Ecosystem Services Valuation Database (ESVD; de Groot et al. 2020) provides 2,917 data points across biomes. **Caution:** not all ESVD values are exchange values — screen for SNA compatibility before use.

**Ecosystem as institutional supplier.** The ecosystem is treated as a distinct "supplier" of services. For marketed goods, the resource rent method decomposes the final product value into the ecosystem's contribution versus human labour, produced capital, and other inputs. The formal NCAVES resource rent formula is:

```
Resource Rent = Total Revenue − Intermediate Inputs − Compensation of Employees
                − Consumption of Fixed Capital − Return on Produced Assets
```

Where the return on produced assets = value of produced capital × appropriate rate of return. A negative residual implies zero ecosystem service value (the ecosystem still provides its function but the economic activity is unprofitable).

**Asset valuation (NPV framework).** The SEEA EA values ecosystem assets as the net present value of expected future ecosystem service flows: V = Σ [R_t / (1+r)^t] for t = 0 to N, where R_t is the expected net income from the asset in period t, r is the discount rate, and N is the asset lifetime (up to 100 years). The SEEA EA recommends: market-based discount rates for services whose users are private economic units; social discount rates for services with collective benefits (e.g., climate regulation, coastal protection). The UK Treasury Green Book recommends declining rates: 3.5% for years 0–30, 3.0% for years 31–75, 2.5% for years 76–125.

---

### 1.4 Tiered Assessment Profile

This SOP is assessed against the [Tiered Assessment Framework](tiered_assessment_framework.md), which evaluates procedures across three independent dimensions for physical measurement (**A — Feasibility**, **B — Accuracy**, **C — Difficulty**) plus an additional dimension specific to monetary valuation (**D — Exchange Value Consistency**). The framework covers eight ecosystem services; the additional service in this SOP (wood provisioning, SOP 1b) falls outside the framework's scope and should be assessed independently.

**Current SOP method tier profile — physical measurement:**

The table maps each SOP's default ("current") physical measurement method to its position in the tier hierarchy from [Tiered Assessment Framework Section 4](tiered_assessment_framework.md).

| Service | Current SOP Method | A: Feasibility | B: Accuracy | C: Difficulty |
|---|---|---|---|---|
| Wild fish provisioning | National catch statistics + resource rent | 2 | 2 | 2 |
| Fisheries nursery service | Productivity change (LRR, literature values) | 2 | 1–2 | 2 |
| Carbon sequestration | Literature NCP rates × national extent | 1–2 | 1–2 | 1–2 |
| Coastal protection | Building inventory × replacement cost | 1–2 | 1 | 1–2 |
| Sediment nourishment | Carbonate production rate × reef length | 1–2 | 1–2 | 1–2 |
| Coral reef recreation | Direct expenditure analysis (reef-attributable share) | 1–2 | 2 | 1–2 |
| Mangrove recreation | Activity-based P×Q (tour operator fee × trips) | 1 | 1–2 | 1 |
| Seagrass gleaning | Equivalent wage + market value of harvest | 1–2 | 2 | 2 |

For Tier 1 and Tier 3 physical measurement alternatives for each service, see [Tiered Assessment Framework Section 4](tiered_assessment_framework.md). For monetary valuation alternatives, see [Section 4a.2](tiered_assessment_framework.md).

**Current SOP method tier profile — monetary valuation:**

All current SOP monetary methods correspond to **Monetary Tier 2** in the framework (Section 4a.2): they use locally observable prices or cost-based proxies rather than value transfer (Monetary Tier 1) or primary stated-preference valuation (Monetary Tier 3).

| Service | Current Monetary Method | D: Exchange Value Consistency |
|---|---|---|
| Wild fish provisioning | Resource rent (4- or 5-component) | Fully compliant — isolates ecosystem contribution from produced capital |
| Fisheries nursery service | Market price × biomass enhancement | Acceptable — market prices observed; indirect ecosystem attribution |
| Carbon sequestration | SCC (shadow price) or market carbon price | Acceptable — label explicitly as non-market estimate where SCC used; see SOP 3 Part B |
| Coastal protection | Annualised replacement cost | Acceptable — cost-based proxy; exchange value compliance straightforward |
| Sediment nourishment | Beach nourishment replacement cost | Acceptable — cost-based proxy |
| Coral reef recreation | Direct expenditure (reef-attributable share) | Acceptable — market prices; confirm ecosystem attribution is isolated from broader tourism spending |
| Mangrove recreation | Tour operator fee × trips | Acceptable — market-observed prices |
| Seagrass gleaning | Equivalent wage + market value | Acceptable — mixed market and imputed wage; consumer surplus not included |

**Double-counting risks (see also Tiered Assessment Framework Section 4a.3):**

Before aggregating monetary values across services, check the following potential overlaps:

- **Nursery service and fish provisioning (SOPs 1–2):** The nursery service enhances the fish stock valued in SOP 1. The nursery monetary value should reflect only the *incremental* fish biomass attributable to nursery habitat — not the full catch value also estimated in SOP 1.
- **Coastal protection and sediment nourishment (SOPs 4–5):** Both services may protect the same built assets on beach-backed reef coastlines. Cross-check whether the building inventory (SOP 4) and the sediment supply buffer zone (SOP 5) overlap geographically.
- **Carbon sequestration flow and carbon stock asset (SOP 3):** Service flow accounts value annual sequestration (Mg CO2/yr × SCC). Asset accounts value the NPV of future sequestration. Do not monetise the same tonne of carbon in both a service flow account and a carbon stock asset account without explicitly treating the stock/flow distinction.

---

## 2. SOP 1 — Wild Fish Provisioning

### 2.1 Objective

Quantify the contribution of marine ecosystems to fisheries catch within the accounting area, in both physical (kg/yr) and monetary (local currency/yr) terms.

### 2.2 Data Sources

| Data Source | Purpose |
|---|---|
| National or regional fisheries agency catch records | Official landings data by species and gear type |
| Local fisher surveys | Supplementary catch data, effort, and cost information |
| Scientific literature | Species–habitat association data for ecosystem allocation |
| Local fisher knowledge | Validation of species–habitat allocations |

---

### Part A: Physical Measurement

**Step 1: Compile total annual catch**
- Obtain fisheries catch records from the relevant national or regional fisheries agency for the accounting area
- Supplement with catch estimates from local fisher surveys
- Express as total annual landed catch in kg/yr
- *Example (Laamu Atoll, Maldives): 61,228 kg/yr*

**Step 2: Disaggregate catch by ecosystem association**
- Classify each fish species/group as:
  - Coral reef-associated
  - Seagrass-associated
  - Pelagic (not attributed to a specific benthic ecosystem)
- Use species habitat associations from scientific literature, validated by local fisher knowledge
- Allocate catch weight (kg) to each ecosystem type

**Step 3: Disaggregate by gear type**
- Record gear type for each catch component (pole-and-line, handline, net, etc.)
- Compile into supply and use table format: catch by species group, ecosystem association, and gear type

**Step 4: Map fishing effort**
- Record spatial distribution of fishing effort across the accounting area
- Produce spatial map of fishing effort

**Physical account output:** Total catch (kg/yr) disaggregated by ecosystem type and gear type.

---

### Part B: Economic Valuation — Resource Rent Method

> **Value type: Market-based.** Resource rent isolates the ecosystem's contribution to fishery revenue using observed market prices and costs.

**Step 5: Calculate gross revenue**
- Multiply catch (kg) by market price (local currency/kg) for each species group
- Sum to obtain total gross revenue

**Step 6: Calculate total fishing costs**
- Labour costs (crew wages and fisher opportunity costs)
- Capital costs (vessel depreciation, gear replacement)
- Fuel costs
- Equipment and maintenance costs

**Step 7: Calculate resource rent**
```
Resource Rent = Gross Revenue − Total Costs (labour + capital + fuel + equipment)
```
- A positive value indicates the ecosystem's economic contribution (the "nature premium")
- A negative value indicates fishing costs exceed revenue (e.g., −3,636,324 MVR in Laamu Atoll, Maldives)

### Alternative: Five-Component Cost Structure with WACC

**When to use:** Where detailed cost disaggregation is feasible and a weighted-average cost of capital (WACC) can be established for the local financial context.

The five-component resource rent method decomposes costs as follows:

| Component | Description |
|---|---|
| (i) Gross Output Value | Catch volume × first-sale prices per species |
| (ii) Operational Expenses | Consumables, fuel, maintenance, repairs (sourced from advertised/online prices where survey data unavailable) |
| (iii) Labour Costs | Alternative comparative wages from the dominant employment sector (e.g., agriculture) where fisher wage surveys are unavailable |
| (iv) Capital Costs | Vessel and gear depreciation + return on fixed capital using WACC (e.g., 9% for Indonesian financial conditions) |
| (v) Resource Rent | Residual: Gross Output − (Operational + Labour + Capital) |

**Survey calibration:** Compare survey catch volumes against provincial/national fisheries statistics to estimate survey coverage (e.g., 1% of total fishing trips), then extrapolate accordingly.

> **RNF BCAF example (Central Java):** The five-component method applied to crab fisheries in Demak yielded a positive resource rent of IDR 5.59 billion annually — contrasting with the ENDhERI Maldives result of −3.6M MVR, demonstrating that the resource rent method is highly sensitive to cost estimation assumptions in artisanal fishery contexts. (Source: GOAP, 2025)

### 2.3 Known Limitations and Quality Flags

- Cost data may be limited by survey response rates
- Subsistence fishing (non-market catch) is difficult to value at market prices
- Artisanal and informal labour arrangements are poorly captured by standard resource rent
- **Flag as data-deficient if cost data quality is insufficient**

---

## 3. SOP 2 — Fisheries Nursery Service

### 3.1 Objective

Quantify the contribution of coral reef and seagrass nursery habitats to harvestable adult fish biomass.

---

### Part A: Physical Measurement — Productivity Change with Log Response Ratio (LRR)

**Step 1: Establish baseline fish density**
- Obtain fish density data from areas without significant nursery habitat (coral reef or seagrass)
- This serves as the counterfactual baseline

**Step 2: Calculate the Log Response Ratio (LRR)**
- Compare fish density in areas with nursery habitat to areas without
- LRR quantifies the proportional increase in fish density attributable to nursery habitat

| Nursery Habitat | LRR (density enhancement) |
|---|---|
| Coral reef | 31% |
| Seagrass | 13% |

**Step 3: Estimate enhanced juvenile production**
- Apply the LRR to the total fish biomass within the accounting area to estimate the additional juvenile fish biomass supported by nursery habitats

**Step 4: Apply juvenile mortality rate to estimate recruitment to fishery**
- Apply a juvenile mortality rate of 95% (i.e., 5% survival to harvestable size)
- This reflects the high natural mortality of juvenile fish before recruitment to the adult fishable population
```
Nursery contribution to harvest (kg/yr) = Enhanced juvenile biomass × 0.05
```

**Physical account output:** Additional harvestable fish biomass (kg/yr) attributable to nursery habitat, by ecosystem type.

---

### Part B: Economic Valuation — Market Price of Landed Fish

> **Value type: Market-based (indirect).** The physical biomass enhancement is valued at observed market prices for landed fish. The valuation depends on market data but the underlying service (nursery function) is not itself traded.

**Step 5: Calculate monetary value**
- Multiply the estimated additional harvestable biomass (kg) by the market price of landed fish (local currency/kg)
- Compile into supply and use table format

### Alternative Monetary Valuation: Residual Value Method (NCAVES Tier 1)

**When to use:** As a simpler alternative when productivity change data (LRR, fish density comparisons) are unavailable. Attributes a proportion of the final fisheries product value to the nursery service based on the share of the production chain dependent on nursery habitat.

**Step 5b: Estimate nursery contribution to fisheries value**
- Determine the proportion of commercially harvested species that are nursery-dependent (from FishBase or local ecological literature)
- Multiply total fisheries resource rent (from SOP 1) by the nursery-dependent species proportion
- This yields an indicative nursery service value without requiring paired fish density data

> **NCAVES reference:** Anneboina & Kumar (2017) used the productivity change method with a stochastic production frontier model to value mangrove nursery services for Indian fisheries at approximately 146,000 Rs/ha/yr (USD 1,900/ha/yr), demonstrating that a market price / gross value approach is accounting-compatible for nursery services when marginal productivity controls for other inputs.

### 3.2 Key Parameters

| Parameter | Value | Source |
|---|---|---|
| Coral reef nursery LRR | 31% | Scientific literature |
| Seagrass nursery LRR | 13% | Scientific literature |
| Juvenile mortality rate | 95% | Standard ecological assumption |
| Survival to harvest | 5% | Derived from mortality rate |

---

## 4. SOP 3 — Carbon Sequestration

### 4.1 Objective

Quantify the annual carbon sequestration by mangroves and seagrass ecosystems in physical terms (Mg CO2/yr), and estimate its economic significance using the Social Cost of Carbon.

---

### Part A: Physical Measurement

**Step 1: Determine ecosystem extent**
- Obtain extent data from the extent account

| Ecosystem | Example Extent (Laamu Atoll, Maldives) |
|---|---|
| Mangroves | 18.7 ha |
| Seagrass | 4,855.5 ha |

> Substitute with extent values from your own extent account.

**Step 2: Establish per-hectare sequestration rates**
- Use Net Carbon Production (NCP) rates from published literature, calibrated to local conditions

| Ecosystem | NCP (Mg CO2/ha/yr) | Components |
|---|---|---|
| Mangrove | 17.23 | Above-ground biomass accumulation + soil carbon sequestration |
| Seagrass | 4.44 | Carbon burial in sediments + biomass accumulation |

**Step 3: Calculate total annual sequestration**
```
Total sequestration = Extent (ha) × NCP (Mg CO2/ha/yr)
```

| Ecosystem | Calculation | Example Total (Mg CO2/yr) |
|---|---|---|
| Mangrove | Extent (ha) × NCP | e.g., 18.7 × 17.23 = ~322 |
| Seagrass | Extent (ha) × NCP | e.g., 4,855.5 × 4.44 = ~21,558 |
| **Combined** | | **Sum of above** |

**Step 4: Compile physical account**
- Present in supply and use table format: sequestration rates by ecosystem type, total annual sequestration, breakdown between above-ground and below-ground carbon pools

**Physical account output:** Annual carbon sequestration (Mg CO2/yr) by ecosystem type and carbon pool.

---

### Part B: Economic Valuation — Social Cost of Carbon (SCC)

> **Value type: Non-market.** The SCC is a **shadow price**, not a market price. There is no functioning market in which the climate regulation service of mangroves and seagrass is bought or sold. The SCC estimates the economic damage avoided by preventing the emission of one additional tonne of CO2. It is derived from integrated assessment models of climate change impacts on agriculture, human health, property damage, and other sectors — not from carbon credit markets or emissions trading schemes. The resulting monetary figure represents an estimate of economic significance for policy analysis, not a revenue stream or market transaction.

**Step 5: Select the Social Cost of Carbon (SCC) value**

The SCC value must be drawn from a recognised, peer-reviewed source. The U.S. federal government's Interagency Working Group (IWG) on the Social Cost of Greenhouse Gases provides widely referenced estimates.

- **Value used: USD 51 per Mg CO2** (U.S. IWG central estimate at 3% discount rate, 2020 base year)

> **Why USD 51 and not a carbon market price?**
> - Voluntary carbon market prices (e.g., USD 5–50/tonne for forestry credits) reflect willingness-to-pay in a thin, voluntary market — not the full societal cost of emissions.
> - EU ETS or other compliance market prices (e.g., EUR 50–100/tonne) reflect regulatory cap-and-trade dynamics — they are policy instruments, not damage estimates.
> - The SCC is the theoretically correct measure for the SEEA EA framework because it captures the **avoided damage** to society from each tonne of CO2 sequestered, regardless of whether a market exists.
> - Higher SCC estimates exist (e.g., USD 185/Mg CO2 from EPA updated analyses using lower discount rates). The choice of SCC value is a **policy and ethical decision** about discount rates and intergenerational equity, and should be documented transparently.

**Step 6: Calculate annual monetary value**
```
Monetary value = Total sequestration (Mg CO2/yr) × SCC (USD/Mg CO2)
```

| Ecosystem | Calculation | Example Annual Value (USD/yr) |
|---|---|---|
| Mangrove | Sequestration × SCC | e.g., 322 × USD 51 = ~16,422 |
| Seagrass | Sequestration × SCC | e.g., 21,558 × USD 51 = ~1,099,458 |
| **Combined** | | **Sum of above** |

**Step 7: Convert to local currency**
- Convert USD values to local currency using prevailing exchange rate
- Compile into supply and use table format

> **Reporting requirement:** When reporting carbon sequestration monetary values, always state:
> 1. The SCC value used and its source
> 2. The discount rate assumed
> 3. That the value is a non-market shadow price (avoided damage estimate), not a market transaction
> 4. Sensitivity to alternative SCC values (see Step 8)

**Step 8: Sensitivity analysis**
- Recalculate using alternative SCC values to show the range of plausible estimates:

| SCC Scenario | USD/Mg CO2 | Source / Rationale | Combined Annual Value |
|---|---|---|---|
| IWG central (3% discount) | 51 | U.S. IWG central estimate | ~USD 1,115,880/yr |
| IWG high (2.5% discount) | 76 | U.S. IWG higher estimate | ~USD 1,662,880/yr |
| EPA updated (2% discount) | 185 | U.S. EPA lower discount rate; ENDhERI report value | ~USD 4,047,800/yr |

### Alternative Physical Measurement: Incremental Biomass Change from Permanent Plots

**When to use:** Where permanent monitoring plots exist and repeated tree censuses can provide locally calibrated sequestration rates, rather than relying on literature-derived NCP rates.

**Step 2b: Measure incremental biomass change**
- Tag all trees ≥5 cm DBH in permanent plots (e.g., 0.1 ha each)
- Measure stems at baseline and follow-up (e.g., 2-year interval)
- Transform measurements to biomass using species-specific allometric equations: AGB = a × ρ × DBH^b (where ρ = wood density)
- Estimate BGB using conversion equations (e.g., Komiyama et al., 2008)
- Apply carbon fractions: 47% for AGB, 39% for BGB (Kauffman & Donato, 2012)
- Track mortality (subtract biomass of trees lost) and ingrowth (add new recruits ≥5 cm DBH)
- Annual sequestration = (Live carbon stock at t₂ − Live carbon stock at t₁) / measurement interval

**Step 2c: Measure Soil Organic Carbon (SOC)**
- Collect soil cores (e.g., r = 2.54 cm, l = 30 cm) to 10–20 cm depth
- Analyse using Walkley-Black wet-oxidation digestion (K₂Cr₂O₇-H₂SO₄) following national standards (e.g., SNI7724:2011)
- Where direct SOC data is unavailable for follow-up, apply a Tier 2 conservative rate (e.g., 1.2 ± 0.2 Mg C ha⁻¹ yr⁻¹ for degraded forests; Murdiyarso et al., 2023)

> **RNF BCAF example (Central Java):** 13 permanent plots (0.1 ha each) measured across 2023–2025 yielded locally calibrated rates capturing inter-annual variability and species-level drivers, though high plot-to-plot variability produced wide confidence intervals. Total annual mangrove sequestration was estimated at 24,227 Mg C (88,831 Mg CO₂e). (Source: GOAP, 2025)

### Alternative Monetary Valuation: Market-Based Carbon Pricing

**When to use:** Where a domestic regulatory carbon market exists (e.g., Indonesia's IDXCarbon exchange), market-based pricing may be preferred as the "best available estimate" over the SCC shadow-price approach.

**Step 6b: Apply market carbon price**
```
Monetary value = Total sequestration (Mg CO2e/yr) × Market price (local currency/Mg CO2e)
```

| Pricing Approach | Value | Source | When to Use |
|---|---|---|---|
| SCC (shadow price) | USD 51–185/Mg CO2 | U.S. IWG / EPA | No domestic carbon market; national statistical reporting |
| Market-based | e.g., IDR 150,000/tCO2e | IDXCarbon (Indonesia) | Operational domestic carbon exchange; investor communication |

> **RNF BCAF example (Central Java):** Market-based pricing at IDR 150,000/tCO₂e yielded IDR 13.3 billion for 88,831 Mg CO₂e of mangrove sequestration. The report recommends future assessments stratify mangrove extent by quality class (intact, degraded, regenerating, converted) with class-specific sequestration rates, since the difference between pristine mangroves (>7 Mg C ha⁻¹ yr⁻¹) and degraded stands (<1 Mg C ha⁻¹ yr⁻¹) makes single average rates inadequate. (Source: GOAP, 2025)

### 4.2 Key Parameters

| Parameter | Value | Source |
|---|---|---|
| Mangrove NCP | 17.23 Mg CO2/ha/yr | Published literature (calibrated locally) |
| Seagrass NCP | 4.44 Mg CO2/ha/yr | Published literature (calibrated locally) |
| SCC (central) | USD 51/Mg CO2 | U.S. IWG (3% discount rate, 2020) |
| Exchange rate | Prevailing local currency:USD rate | National statistical office or central bank |

---

## 5. SOP 4 — Coastal Protection

### 5.1 Objective

Quantify the coastal protection provided by coral reefs and mangroves in terms of protected assets and coastline, and estimate its economic value using the replacement cost method.

---

### Part A: Physical Measurement

**Step 1: Establish the coastal buffer zone**
- Define a 100-metre buffer zone landward from the shoreline on all inhabited islands in the accounting area

**Step 2: Map protective ecosystem features**
- Identify coral reef systems fronting inhabited coastlines (from extent account)
- Identify mangrove areas providing wave attenuation (from extent account)

**Step 3: Identify protected built assets**
- Overlay building footprint data with the 100 m buffer zone
- Count and categorise buildings within the buffer:
  - Residential
  - Commercial
  - Institutional
- *Example (Laamu Atoll, Maldives): 778 buildings within the buffer zone*

**Step 4: Measure protected coastline length**
- Calculate the total length of coastline fronted by reef or mangrove wave attenuation
- *Example (Laamu Atoll, Maldives): 33,142 metres*

**Physical account output:** Number and type of protected buildings; total protected coastline length (m); spatial maps of protective ecosystem features and buffer zones.

---

### Part B: Economic Valuation — Replacement Cost Method

> **Value type: Non-market (cost-based proxy).** There is no market where coastal protection by coral reefs is traded. The replacement cost method estimates what it would cost to build engineered infrastructure providing equivalent protection. This is a proxy for the service's value, not an observed market price. It yields a **lower-bound estimate** because it captures only direct construction costs.

**Step 5: Assign replacement values to buildings**
- Obtain local construction cost data for each building type
- Assign replacement values per building category

**Step 6: Select engineering replacement benchmarks**
- Identify the cost of engineered coastal defence alternatives that would provide equivalent protection

| Defence Type | Example Cost (local currency per linear metre) |
|---|---|
| Quaywall construction | e.g., MVR 60,000 (Maldives) |
| Sheet pile installation | e.g., MVR 170,000 (Maldives) |

> Obtain locally relevant engineering cost estimates. Costs will vary significantly by country and construction market.

**Step 7: Calculate replacement cost**
- Assign the appropriate defence type to each coastline segment based on:
  - Exposure conditions
  - Wave energy
  - Engineering specification required
- Multiply segment length (m) by unit cost (local currency/m)
- Sum across all segments for total coastal protection value

**Step 8: Compile account**
- Present in supply and use table format
- Produce spatial maps: 100 m buffer zone, building locations, reef systems

### Alternative: Differentiated Buffer Zones by Coastal Exposure

**When to use:** Where the accounting area spans coastlines with markedly different wave energy environments (e.g., sheltered vs. open ocean coasts), or where mangrove protection capacity varies by type (coastal vs. estuarine).

**Step 1b: Apply exposure-differentiated buffers**

| Coastal Exposure | Buffer Width | Rationale |
|---|---|---|
| Low energy (sheltered seas, embayments) | 100 m | Standard protection distance |
| High energy (open ocean coast) | 300 m | Greater wave penetration and risk |

**Step 2b: Classify mangrove protection type**
- **Coastal mangroves** (directly facing the sea): Assessed for coastline protection service
- **Estuarine mangroves** (along rivers and inlets): Not assessed for ocean-facing protection
- Require minimum continuous width of 25 m within 200 m of shoreline for protective service eligibility
- Exclude coastline segments with existing grey infrastructure (seawalls, quaywalls)

**Step 3b: Use open-access building footprint data**
- Where local building survey data is unavailable, use Google Open Buildings (v3) or Microsoft Building Footprints to identify structures within the buffer zone

### Alternative Monetary Valuation A: Annualised Depreciation Model

**When to use:** To convert the stock-based replacement cost into an annual service flow consistent with SEEA EA supply and use table requirements (paragraphs 9.50–9.51).

**Step 7b: Apply straight-line depreciation**
```
Annual Value = (Construction Cost − Salvage Value) / Service Life
```
- Salvage value: zero (standard assumption)
- Service life: 25 years (standard engineering lifetime for coastal defences)
- Erosion rate assumption (e.g., 2 m/yr) may be used to justify service-life comparability

> **RNF BCAF example (Central Java):** Differentiated buffers (100 m for Demak/Jepara on the Java Sea; 300 m for Cilacap/Kebumen on the Indian Ocean) identified 30,500+ buildings and 64.58 km of protected coastline. The annualised depreciation model yielded an annual coastal protection value exceeding IDR 17.2 billion. (Source: GOAP, 2025)

### Alternative Monetary Valuation B: Expected Damage Function (NCAVES Tier 3)

**When to use:** Where storm/flood frequency data and elevation models are available, and a more rigorous valuation is warranted. The NCAVES report recommends the expected damage function (EDF) approach — endorsed by World Bank (2016) — as the preferred Tier 3 method over replacement cost.

**Step 7c: Calculate expected avoided damages**
- Compile storm frequency/intensity data from regional databases (IBTrACS, EM-DAT)
- Develop exposure analysis using a digital elevation model (SRTM 30 m or FABDEM)
- Apply depth-damage curves (e.g., Global Flood Depth-Damage Function, Huizinga et al. 2017)
- Model ecosystem attenuation factors from meta-analyses of wave reduction by reefs/mangroves
- Calculate expected annual damages WITH ecosystem vs WITHOUT ecosystem (counterfactual)
- Coastal protection value = Expected damages WITHOUT ecosystem − Expected damages WITH ecosystem

> **NCAVES reference:** Menendez et al. (2020) used a 2-D hydrodynamic model coupled with economic damage models to estimate that global mangrove flood protection benefits exceed USD 65 billion annually. The EDF approach calculates each possible damage scenario multiplied by its probability, grounded in engineering and insurance risk assessment. This is classified as NCAVES Category V (avoided damage cost) and is considered Tier 3 for SEEA EA.

**Additional NCAVES option: Insurance premium differentials**
- Where property insurance markets function, the difference in premiums between properties behind ecosystems vs exposed properties reveals the market-implied protection value
- This provides a Category III (prices embodied in market transactions) estimate
- Feasibility limited to contexts with well-functioning property insurance markets

### 5.2 Data Sources

| Data Source | Purpose |
|---|---|
| Building footprint data | Asset identification within buffer zone |
| Reef extent (from extent account) | Mapping protective reef features |
| Local construction cost data | Building replacement values |
| Coastal engineering cost data | Quaywall and sheet pile unit costs |
| Island coastline GIS data | Buffer zone and coastline length |

### 5.3 Limitations

- The replacement cost approach is a **lower-bound estimate** — it captures only direct infrastructure costs
- Not included: maintenance costs, environmental impacts of hard infrastructure, loss of aesthetic/recreational values of natural shorelines
- The estimate does not reflect what society would actually pay to preserve the reef — only the minimum cost of a hard-infrastructure substitute

---

## 6. SOP 5 — Sediment Nourishment

### 6.1 Objective

Quantify the production of calcareous sediment (CaCO3) by coral reefs and seagrass epibionts that contributes to beach maintenance and island stability.

---

### Part A: Physical Measurement

**Step 1: Estimate coral reef carbonate production rate**
- Use published rates for the relevant bioregion (e.g., Indo-Pacific reefs), adjusted for local conditions
- Rate incorporates:
  - Carbonate production from coral growth
  - Coralline algae contribution
  - Foraminifera contribution
  - *Halimeda* contribution
  - **Net of** bioerosion losses (borers, grazers, dissolution)
- *Example rate (Maldives): 0.049 m^3/m/yr (cubic metres of sediment per linear metre of reef crest per year)*

**Step 2: Estimate seagrass epibiontic sediment production**
- Calculate CaCO3 production from organisms growing on seagrass blades:
  - Coralline algae
  - Foraminifera
- Use published production rates appropriate to the regional seagrass assemblage

**Step 3: Calculate total physical sediment supply**
- Coral reef: Multiply production rate (m^3/m/yr) by total reef crest length (m)
- Seagrass: Multiply per-hectare epibiontic production by seagrass extent (ha)

**Physical account output:** Annual sediment production (m^3 CaCO3/yr) by ecosystem type.

---

### Part B: Economic Valuation — Replacement Cost (Beach Nourishment)

> **Value type: Non-market (cost-based proxy).** Natural sediment production has no market. The replacement cost of importing and mechanically placing equivalent volumes of sand provides a proxy value. As with coastal protection, this is a lower-bound estimate.

**Step 4: Establish beach nourishment cost**
- Determine the cost of importing and placing equivalent volumes of sand
- Obtain local or regional beach nourishment cost data (local currency/m^3)

**Step 5: Calculate monetary value**
```
Monetary value = Physical sediment production (m^3/yr) × Beach nourishment cost (local currency/m^3)
```

**Step 6: Compile account**
- Present in supply and use table format (physical and monetary terms)

### 6.2 Key Parameters

| Parameter | Value | Source |
|---|---|---|
| Coral reef carbonate production | 0.049 m^3/m/yr | Published literature (Indo-Pacific reefs) |
| Seagrass epibiontic CaCO3 production | Species/site-specific | Published literature |
| Beach nourishment cost | Local engineering data | Local currency/m^3 |

### 6.3 Significance

This service is critical for low-lying coastal areas and island nations, where natural sediment supply from reefs maintains island elevation and beach width against erosion and sea level rise. It is particularly significant for atoll nations (e.g., Maldives, Pacific Island states) and other reef-fronted coastlines.

---

## 7. SOP 6 — Recreational Services

Three distinct recreational services are measured and valued.

---

### 7.1 Coral Reef Recreation

#### Objective
Quantify the recreational value of coral reefs from diving and snorkelling tourism.

#### Part A: Physical Measurement

**Step 1: Compile visitor statistics**
- Obtain resort visitor statistics for the accounting area
- Obtain guesthouse visitor statistics
- Record dive centre activity data (number of trips, participants)

**Step 2: Quantify reef-based activity participation**
- Number of dive trips per year
- Number of snorkel trips per year
- Number of participants by visitor segment (resort guests vs. guesthouse tourists)

**Physical account output:** Total reef-based activity trips and participants per year.

#### Part B: Economic Valuation — Direct Expenditure Analysis

> **Value type: Market-based.** The valuation uses observed tourist spending data — actual transactions in functioning tourism markets.

**Step 3: Identify coral reef-attributable expenditure**
- Quantify spending directly attributable to coral reef-based activities:
  - Scuba diving excursion fees
  - Snorkelling excursion fees
  - Equipment rental
  - Proportion of accommodation expenditure attributable to reef as primary attraction

**Step 4: Allocate accommodation expenditure**
- Use tourist survey data to determine the proportion of accommodation spending attributable to reef activities
- Ask tourists: "How important were reef activities in your destination choice?"
- Apply the resulting allocation proportion to total accommodation expenditure

**Step 5: Calculate total recreational value**
```
Total value = Direct reef activity spending + Allocated accommodation spending
```
- Disaggregate by visitor segment: resort guests vs. guesthouse tourists
- *Example (Laamu Atoll, Maldives): USD 30.43 million/yr*

**Step 6: Map dive and snorkel sites**
- Produce spatial map: distribution of dive/snorkel sites relative to reef locations

#### Data Sources

| Data Source | Purpose |
|---|---|
| Resort visitor statistics | Tourist numbers and spending |
| Dive centre records | Activity participation rates |
| Tourist expenditure surveys | Reef-attributable spending |
| Tourist motivation surveys | Accommodation allocation factor |

---

### Alternative Valuation A: Activity-Based P×Q Method with Intermediate Input Deductions

**When to use:** Where multiple ecotourism activities exist across distributed sites and gross direct expenditure would overstate the ecosystem's contribution by including intermediate inputs (labour, utilities, raw materials) that are not ecosystem service flows.

The activity-based method structures total expenditure per site (E_total) as the sum of three components, each net of intermediate inputs:

| Component | Gross Value | Intermediate Input Deduction |
|---|---|---|
| (1) Activities | Entrance fees, boat tours, equipment hire | No deduction (prices = final transaction values) |
| (2) Accommodation | Gross room rate | 54% for hotels; 40% for guesthouses (labour, housekeeping, utilities, OTA commissions, maintenance) |
| (3) Food & Beverage | Daily F&B spend | 30% (raw ingredient and labour share) |

**Activity participation rate estimation:**
- 100% for obligatory activities (entrance fees)
- Declining rates for optional activities (down to 2% for premium/mechanised activities)
- Visitors assumed to engage with mangrove activities once during their holiday

**Price triangulation from three sources:**
1. Semi-structured discussions with operators
2. Publicly posted tariffs on booking platforms
3. Price bands from spatial planning documents (e.g., RTRW in Indonesia)

> **RNF BCAF example (Central Java):** Nine ecotourism sites across four districts generated approximately IDR 2.72 billion in direct annual expenditure from an estimated 11,000 visitors. Revenue profiles differed markedly: Demak's single-site Morosari hub generated IDR 994 million through premium mechanised activities, while Jepara's three-site portfolio generated IDR 989 million from diversified community-based tourism. (Source: GOAP, 2025)

### Alternative Valuation B: NCAVES Tiered Recreation Valuation Methods

The NCAVES/MAIA report identifies three additional monetary valuation approaches for recreation-related ecosystem services, listed in order of increasing data requirements:

**Consumer expenditure method (NCAVES Tier 1)**
- Use tourism/visitation statistics cross-classified by purpose
- Allocate spatially based on relative landscape attractiveness
- Market goods consumed during visits (fuel, transport, admission, parking) provide the expenditure base
- Excludes consumer surplus — approximates exchange value directly
- Lowest data requirement; suitable as initial estimate

**Travel cost method / Random Utility Model (NCAVES Tier 2–3)**
- Values recreation based on costs incurred to access the site (transport, accommodation, entrance fees, time costs)
- Does not capture consumer surplus — approximates exchange value rather than welfare value
- Multi-site Random Utility Models (RUM) model site choice among substitutes, estimating how environmental quality changes affect visitation and expenditure
- Avoids the accommodation allocation problem of direct expenditure analysis
- Requires travel cost survey or mobile phone tracking data (Tier 2) or full demand curve estimation (Tier 3)

**Simulated exchange value / SEV (NCAVES Tier 3)**
- Uses stated preference surveys (contingent valuation or choice experiments) to elicit willingness to pay
- Converts WTP (welfare measure) to exchange value by modelling a hypothetical supply curve and finding equilibrium price
- Most data-intensive; recommended only where tourism revenue exceeds USD 10M/yr or an active policy decision is at stake
- NCAVES classifies this as Category V and the method of last resort when other approaches are not feasible

> **Note on hedonic pricing:** For reef or mangrove sites that provide local amenity value to adjacent properties, the hedonic pricing method (NCAVES Category III, Tier 3) can extract the implicit value from property market data by regressing property prices on environmental attributes. Requires large, geocoded property transaction datasets.

---

### 7.2 Mangrove Recreation

#### Objective
Quantify the recreational value of mangrove-based tourism (kayaking).

#### Part A: Physical Measurement

**Step 1: Identify mangrove tourism activities**
- Catalogue all tourism activities at mangrove sites (e.g., guided kayaking, birdwatching, boardwalk tours)
- *Example (Laamu Atoll, Maldives): Kayaking at Hithadhoo mangrove*

**Step 2: Compile activity data**
- Number of kayaking trips per year
- Average group size per trip

**Physical account output:** Total trips and participants per year.

#### Part B: Economic Valuation — Direct Expenditure Analysis

> **Value type: Market-based.** Based on actual fees charged for guided excursions.

**Step 3: Calculate recreational value**
```
Value = Number of trips × Average group size × Per-trip fee
```
- *Example (Laamu Atoll, Maldives): USD 2,400/yr*

#### Notes
- Low values may reflect nascent or small-scale tourism operations
- Value may increase as ecotourism development expands
- Record activity as a baseline for tracking future growth

#### Alternative Monetary Valuation: Contingent Valuation for Nascent Operations (NCAVES Tier 3)

**When to use:** Where direct expenditure produces near-zero values because tourism supply is nascent, but the ecosystem has genuine recreational potential. The NCAVES report recognises that direct expenditure captures only realised demand conditional on current supply — contingent valuation captures latent demand independent of supply constraints.

- Conduct a stated preference survey (contingent valuation or choice experiment) asking tourists or local residents their willingness to pay for mangrove recreation experiences
- Convert WTP to exchange value using the simulated exchange value (SEV) method (NCAVES Category V)
- Recommended only when an active policy decision on site development or protection is at stake (budget: USD 5,000–15,000)
- Report alongside the direct expenditure figure as a "potential value" scenario

---

### 7.3 Seagrass Gleaning

#### Objective
Quantify the cultural and livelihood value of traditional seagrass gleaning activities.

#### Classification
- Classified as **cultural** rather than provisioning due to the strong social and cultural dimensions beyond subsistence value
- Predominantly undertaken by women

#### Part A: Physical Measurement

**Step 1: Survey gleaning activity**
- Estimate the number of active gleaners in the accounting area
- Record species harvested: sea cucumbers, octopus, shells, and other invertebrates
- Record timing: primarily during low tide events
- *Example (Laamu Atoll, Maldives): 227 gleaners*

**Step 2: Estimate total effort**
- Calculate total annual hours spent gleaning
- *Example (Laamu Atoll, Maldives): 3,960 hours/yr*

**Step 3: Estimate total harvest**
- Record harvest quantities by species/type (kg/yr)

**Physical account output:** Number of gleaners, total effort (hours/yr), and harvest (kg/yr) by species.

#### Part B: Economic Valuation — Equivalent Wage + Market Value

> **Value type: Mixed.** The harvest component uses observed market prices for harvested organisms. The labour component uses an imputed wage value, which is not a direct market observation but a standardised proxy for the opportunity cost of time.

**Step 4: Calculate equivalent wage value**
```
Wage value = Total hours × Local equivalent wage rate (local currency/hr)
```

**Step 5: Calculate market value of harvest**
- Apply local market prices per kg for each harvested species

**Step 6: Calculate total recreational/cultural value**
```
Total value = Equivalent wage value + Market value of harvest
```

**Step 7: Compile account**
- Present in supply and use table format

---

## 8. SOP 7 — Supply and Use Table Compilation

### 8.1 Objective

Compile all ecosystem service accounts into standardised SEEA EA supply and use tables that record which ecosystem types supply each service and which economic units use (benefit from) each service.

### 8.2 Physical Supply and Use Tables

**Step 1: Construct the physical supply table**

| Service | Coral Reefs | Seagrass | Mangroves | Total |
|---|---|---|---|---|
| Wild fish provisioning (kg/yr) | [reef catch] | [seagrass catch] | — | [total catch] |
| Nursery service (kg biomass/yr) | [reef nursery] | [seagrass nursery] | — | [total] |
| Carbon sequestration (Mg CO2/yr) | — | [seagrass seq.] | [mangrove seq.] | [total] |
| Coastal protection (m coastline) | [reef protected] | — | [mangrove protected] | [total] |
| Sediment nourishment (m^3/yr) | [reef CaCO3] | [seagrass CaCO3] | — | [total] |
| Recreation (visitors or hours/yr) | [reef visitors] | [gleaning hours] | [kayak trips] | [total] |

**Step 2: Construct the physical use table**
- Assign each service to its user/beneficiary:

| Service | User / Beneficiary |
|---|---|
| Wild fish provisioning | Fisheries sector, subsistence households |
| Nursery service | Fisheries sector (indirect) |
| Carbon sequestration | Global community |
| Coastal protection | Coastal households, businesses, government infrastructure |
| Sediment nourishment | Coastal communities, tourism sector |
| Recreation | Tourism sector, local households (gleaning) |

### 8.3 Monetary Supply and Use Tables

**Step 3: Construct the monetary supply table**
- Convert all physical supply values to monetary values using the valuation methods from SOPs 1–6
- Present in the same ecosystem-type x service matrix as the physical table
- **Clearly label** each value with its valuation type (market-based or non-market)

**Step 4: Construct the monetary use table**
- Allocate monetary values to economic sectors and user groups

### 8.4 Example Summary Results (Laamu Atoll, Maldives, using SCC = USD 51/Mg CO2)

| Ecosystem Type | Dominant Service by Value | Approximate Total Value |
|---|---|---|
| Coral reefs | Recreational tourism | USD 30.43M/yr (dominant) |
| Seagrass | Carbon sequestration | ~USD 1.10M/yr (at SCC $51; dominant component) |
| Mangroves | Carbon sequestration | Smallest total (limited extent: 18.7 ha) |

> The relative importance of services will vary by region. In areas with less tourism, provisioning or regulating services may dominate.

### 8.5 Visualisation

Produce summary figures:
- Pie chart: service value by ecosystem type
- Bar chart: value by service category
- Spatial maps where applicable

---

## 9. Carbon Stock Estimation (for Asset Account)

Although carbon stocks feed into the asset account rather than the service flow accounts, they are derived from the same field measurements and are included here for completeness.

---

### Part A: Physical Measurement

#### 9.1 Mangrove Carbon Stock

**Step 1: Apply allometric equations**
- Use species-specific allometric equations from peer-reviewed literature appropriate to your region (e.g., Wartman et al. 2022 for Indo-Pacific species)
- Apply calibrated parameters for the dominant species in your accounting area

**Step 2: Estimate carbon pools**

| Pool | Method |
|---|---|
| Above-ground biomass (AGB) | Allometric equation from DBH and height |
| Below-ground biomass (BGB) | Fixed proportion of AGB using root-to-shoot ratios |
| Soil organic carbon (SOC) | Estimated to 1 m depth |

- *Example (Laamu Atoll, Maldives): 1,283.58 Mg C*

**Step 3: Calculate sequestration rate**
- *Mangrove sequestration: 17.23 Mg CO2/ha/yr*

#### 9.2 Seagrass Carbon Stock

**Step 4: Apply regression models**

| Carbon Pool | Model |
|---|---|
| Above-ground carbon (AGC) | AGC = 21.337810 + 0.13514 x [Coverage (%)] |
| Below-ground carbon (BGC) | BGC = 53.2301 + 0.3055 x [Coverage (%)] |

**Step 5: Extrapolate to total extent**
- Apply models to each survey site
- Extrapolate to total seagrass extent using the spatial coverage data
- *Example (Laamu Atoll, Maldives): 4,209.34 tonnes C*

**Step 6: Calculate sequestration rate**
- *Seagrass sequestration: 4.44 Mg CO2/ha/yr*

**Physical stock output:** Total carbon stock (Mg C) by ecosystem type and pool; annual sequestration rate (Mg CO2/ha/yr).

---

### Part B: Asset Valuation (NPV Method)

> **Value type: Non-market (shadow price).** The asset value uses the same SCC-based approach as the service flow account. It represents the net present value of avoided climate damages if stored carbon were released — not a price at which the ecosystem could be sold or a revenue the ecosystem generates. See SOP 3, Part B for full explanation of the non-market nature of SCC.

**Step 7: Convert total stock to CO2 equivalent**
```
CO2 equivalent = Carbon stock (Mg C) × 3.67
```

**Step 8: Calculate Net Present Value**
```
Asset value = NPV of future ecosystem service flows + Carbon stock value (SCC × CO2 equivalent)

NPV formula (NCAVES Chapter 5):
V = Σ [R_t / (1+r)^t]  for t = 0 to N

Where:
  R_t = expected net income from the asset in period t
  r   = discount rate
  N   = asset lifetime (up to 100 years for sustainably managed ecosystems)
```
- Apply SCC of USD 51/tonne CO2 (IWG central estimate)
- Apply discount rate of 3% (consistent with IWG central SCC discount rate)

> **NCAVES discount rate guidance:** The SEEA EA recommends social discount rates for services with collective benefits (climate regulation). Options: (1) government-specified SDR where available; (2) long-term government bond rates as proxy; (3) declining rates following UK Treasury Green Book (3.5% for years 0–30, 3.0% for years 31–75, 2.5% for years 76–125). Conduct sensitivity analysis with alternative rates. Drupp et al. (2015) survey of 200+ economists found median recommended long-term SDR of 2.25%.

**Step 9: Sensitivity analysis**
- Test at multiple discount rates and SCC scenarios:

| SCC Scenario | Discount Rate | SCC (USD/Mg CO2) | Rationale |
|---|---|---|---|
| IWG central | 3% | 51 | U.S. IWG central estimate |
| IWG higher | 2.5% | 76 | Lower discounting of future damages |
| EPA updated | 2% | 185 | EPA analysis with lower discount rate; used in ENDhERI report |

- Document sensitivity of asset value to discount rate and SCC choice
- *Example: The Maldives ENDhERI report used SCC = USD 185 with a 2% discount rate, yielding an asset value of ~USD 94.4 million. Using the IWG central SCC of USD 51 at 3% would yield a substantially lower asset value.*

> **NCAVES distinction — sequestration vs retention:** The SEEA EA distinguishes carbon sequestration (the flow of CO2 removal during an accounting period) from carbon retention (the ongoing storage of carbon in existing stocks). Both are ecosystem services. Service flow accounts value sequestration (annual flow × SCC). Asset accounts value retention via the NPV of future service flows, plus the risk-adjusted value of the stored stock that would be released under the counterfactual.

---

## 10. Equipment and Data Requirements Summary

### 10.1 Field Survey Equipment (shared with Condition Account surveys)

| Equipment | Used For |
|---|---|
| GPS units | Georeferencing survey sites and fishing effort |
| Underwater camera / drop-camera | Reef condition ground-truthing |
| Dive equipment (SCUBA, snorkel) | Reef surveys |
| Belt transect equipment | Reef condition surveys (shared with condition SOP) |
| Quadrat frames / markers | Mangrove and seagrass surveys |
| Clinometer, diameter tape, densiometer | Mangrove biometric measurements |
| Tablets / data sheets | Field recording |

### 10.2 Socioeconomic Survey Equipment

| Equipment / Resource | Used For |
|---|---|
| Fisher survey instruments | Catch data, effort, cost data |
| Tourist expenditure survey forms | Recreational value assessment |
| Dive centre activity logs | Tourism participation data |
| Gleaner survey instruments | Gleaning effort and harvest data |

### 10.3 Spatial and Remote Sensing Data

| Data Source | Used For |
|---|---|
| Building footprint GIS data | Coastal protection asset inventory |
| Island coastline shapefiles | Buffer zone and coastline length |
| Sentinel-2 satellite imagery | Extent accounts, spectral indices |
| Reef crest line GIS data | Sediment nourishment reef length |

### 10.4 Secondary Data Sources

| Data Source | Used For |
|---|---|
| National or regional fisheries agency records | Fish provisioning catch data |
| National statistical office | Exchange rates, construction costs |
| Tourism authority or resort visitor statistics | Tourism recreational value |
| Recognised SCC estimates (e.g., U.S. IWG) | Carbon sequestration non-market valuation |
| Published peer-reviewed literature | Sequestration rates, LRR values, carbonate production rates |
| Local construction cost data | Building replacement values |
| Coastal engineering cost data | Quaywall and sheet pile unit costs |

> Identify the specific agencies and data repositories relevant to your country. Open-access sources (e.g., FAO FishStatJ, World Bank, Copernicus) can supplement national data where gaps exist.

---

## 11. Quality Assurance and Data Flags

### 11.1 Data Quality Assessment

For each ecosystem service, assess and document data quality:

| Quality Criterion | Assessment |
|---|---|
| Data completeness | Are all required input datasets available? |
| Spatial coverage | Do surveys/data cover the full accounting area? |
| Temporal alignment | Are data from the current accounting period? |
| Method appropriateness | Is the valuation method suitable for local context? |
| Parameter uncertainty | Are key parameters (rates, costs) well-constrained? |

### 11.2 Common Data Gaps (with examples from Laamu Atoll, Maldives)

| Service | Data Gap | Impact |
|---|---|---|
| Wild fish provisioning | Limited cost survey data; subsistence catch undervalued | Monetary value flagged as data-deficient |
| Nursery service | LRR values from literature, not locally calibrated | Moderate uncertainty |
| Carbon sequestration | NCP rates from literature, limited local calibration; SCC value is a policy choice with wide range | Low–moderate uncertainty (physical); high sensitivity (monetary) |
| Coastal protection | Lower-bound estimate (replacement cost only) | Underestimates true value |
| Sediment nourishment | Carbonate production rates from literature | Moderate uncertainty |
| Recreation (coral reef) | Accommodation allocation relies on tourist survey | Methodology-dependent |
| Recreation (mangrove) | Very small-scale activity | Low confidence in trend |
| Gleaning | Limited baseline survey data | Moderate uncertainty |

---

## 12. Temporal Design for Repeat Accounting

- Ecosystem service accounts should be compiled for each accounting period
- Repeat field surveys at the same sites enable detection of trends in physical supply
- Monetary values should be updated with current prices, exchange rates, and SCC estimates
- The supply and use table structure enables direct comparison between accounting periods
- Condition account data (from the Condition SOP) feed into interpreting changes in service flows — e.g., declining coral cover may explain declining reef-associated fish catch or reduced tourist satisfaction

---

*Framework aligned with the UN SEEA EA (2021) international statistical standard and the Common International Classification of Ecosystem Services (CICES). Maldives examples drawn from: Compiling the first Natural Capital Accounts in the Maldives: Methods report (ENDhERI Project). Alternative methods from: Applying SEEA EA at the Project Level in Central Java (RNF BCAF, GOAP, 2025). Aligned with GOAP technical guidance.*
