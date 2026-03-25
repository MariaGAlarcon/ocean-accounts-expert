# Tiered Assessment Framework for Ecosystem Service Measurement SOPs

## SEEA EA Coastal and Marine Ecosystem Services

---

## 1. Purpose and Scope

This framework provides a structured approach for evaluating and selecting measurement procedures for ecosystem service accounts under the System of Environmental-Economic Accounting — Ecosystem Accounting (SEEA EA) framework. It applies to coastal and marine ecosystems, specifically mangrove, seagrass, and coral reef ecosystem types, and covers the following eight ecosystem services:

| Category | Service |
|---|---|
| Provisioning | Wild fish provisioning |
| Regulating | Fisheries nursery habitat |
| Regulating | Carbon sequestration |
| Regulating | Coastal protection |
| Regulating | Sediment retention and nourishment |
| Cultural | Coral reef recreation |
| Cultural | Mangrove recreation |
| Cultural | Seagrass gleaning |

The framework is intended for national statistical offices, environment ministries, research institutions, and consultancies tasked with compiling ecosystem service accounts. It allows users to select a measurement tier appropriate to their available resources, institutional capacity, and accuracy requirements, and to do so independently for each service and each sub-procedure within a service.

---

## 2. Assessment Dimensions

Each SOP (and each sub-procedure within an SOP) is evaluated across three independent dimensions. The dimensions are orthogonal: a procedure can be high on one dimension and low on another. For example, a procedure may be highly accurate (Tier 3 on Accuracy) but also highly resource-intensive (Tier 3 on Feasibility) and difficult to implement (Tier 3 on Difficulty).

### 2.1 Dimension A: Feasibility and Resource Intensiveness

This dimension captures the total resource envelope required to implement the procedure. It answers the question: **What does it cost — in money, people, time, and equipment — to produce the measurement?**

> **Distinction from Dimension C:** A measures the *cost* of assembling required staff, equipment, and time. C measures the *domestic availability* of required expertise — a procedure may be affordable (A: Tier 2) but still highly difficult if no domestic team has the necessary skills (C: Tier 3). Score these independently.

Components assessed:

- **Staff requirements** — Number of personnel, person-months of effort, and whether dedicated staff are needed or whether the work can be absorbed into existing roles.
- **Equipment and infrastructure** — Field instruments, laboratory facilities, computing hardware, software licences, and vessel or vehicle access.
- **Budget** — Direct expenditure on fieldwork, data acquisition (e.g., satellite imagery), laboratory analysis, and external consultancies.
- **Time to first output** — Calendar time from project initiation to production of the first usable estimate, including procurement, training, fieldwork, and analysis.
- **Recurrent cost** — Annual or periodic cost to maintain and update the account once the initial estimate has been produced.

### 2.2 Dimension B: Accuracy and Confidence

This dimension captures the reliability of the outputs produced by the procedure. It answers the question: **How much should a decision-maker trust the resulting numbers?**

> **Distinction from Dimension C:** B: Data quality assesses the intrinsic properties of whatever input data are used (resolution, frequency, provenance). C: Data availability assesses whether the required primary inputs exist and can be accessed. Data can exist and be accessible (C: Tier 1) yet still be poor quality (B: Tier 1). Score these independently.

Components assessed:

- **Data quality** — Spatial resolution, temporal frequency, completeness, and provenance of input datasets. For value transfer methods (Tier 1 monetary), also assess **transfer appropriateness**: the degree to which the source study's ecological, socioeconomic, and cultural context matches the target accounting area; transfer error can exceed 100% when contexts diverge substantially.
- **Parameter uncertainty** — Width of confidence intervals or coefficient of variation for key parameters (e.g., carbon stock per hectare, fish catch per unit effort).
- **Method validation and protocol maturity** — Whether the procedure (a) has been validated against independent measurements, peer-reviewed, or endorsed by an international body (e.g., IPCC, FAO, SEEA technical guidance), *and* (b) follows a standardised, documented protocol with clear steps and worked examples. These aspects are assessed together because validated methods are almost always also mature protocols; a method lacking both should score Tier 1 on this criterion regardless of other scores.
- **Sensitivity to assumptions** — Degree to which outputs change when key assumptions are varied within plausible ranges. Distinct from QA feasibility (C): this criterion addresses model-internal robustness, not external verifiability.
- **Spatial and temporal representativeness** — Whether the procedure captures real variation across the accounting area and accounting period, or relies on a single point estimate or transfer value.
- **Temporal consistency** — Whether the method produces comparable, trend-compatible estimates across successive accounting periods. Methods using fixed published values (e.g., value transfer, global defaults) produce stable time series but may drift from true values; methods using current market prices are locally accurate in each period but can produce large inter-period swings that complicate trend analysis. Recalibrated models risk producing inconsistent series if assumptions change between rounds.

### 2.3 Dimension C: Difficulty of Implementation

This dimension captures the practical barriers to carrying out the procedure, independent of cost. It answers the question: **How hard is it to actually do this, even if resources are available?**

> **Distinction from Dimension A:** C assesses non-financial barriers — expertise availability, institutional access, legal constraints, and methodological standing. See the note under Dimension A on the A vs C distinction for staff/expertise.

Components assessed:

- **Technical complexity** — Level of specialist knowledge required (e.g., remote sensing, hydrodynamic modelling, econometrics) and whether that knowledge is available domestically. Note: the *cost* of obtaining that expertise is captured in A; C asks whether the expertise exists domestically at all.
- **Institutional and legal barriers** — Data-sharing agreements, inter-agency coordination, access permits for protected areas, and ethical approvals for household surveys.
- **Data availability** — Whether required input data already exist and are accessible in usable formats. Note: the intrinsic *quality* of those data is captured in B: Data quality.
- **Institutional and method acceptance** — Whether the procedure and its outputs will be accepted by national statistics offices, SEEA EA reporting bodies, peer reviewers, or policymakers. Methodologically contested approaches (e.g., stated-preference / contingent valuation) may be technically feasible and affordable but rejected in official statistics contexts, creating a barrier to publication and use that is independent of cost or technical complexity.
- **Quality assurance and replicability** — Whether it is practical to implement quality checks and independent verification *and* whether a second analyst following the same protocol with the same data would reproduce the same estimate. Both external verifiability and internal replicability are required for institutional capacity transfer and for official statistics use.

---

## 3. Tier Definitions and Scoring Criteria

### 3.1 Dimension A: Feasibility and Resource Intensiveness

| Criterion | Tier 1 — Low Resource | Tier 2 — Moderate Resource | Tier 3 — High Resource |
|---|---|---|---|
| **Staff** | 1–2 analysts working part-time; no dedicated field team | Small team of 3–5 with some field personnel; partial dedication to the account | Large multidisciplinary team (>5) with dedicated field crews, laboratory technicians, and modelling specialists |
| **Equipment** | Standard office computing; freely available satellite imagery and software (e.g., Google Earth Engine, QGIS) | Mid-range computing; licensed software (e.g., ArcGIS); basic field instruments (GPS, quadrat frames, handheld sensors) | High-performance computing or cloud clusters; specialised instruments (side-scan sonar, eddy covariance towers, wave buoys); vessel charters |
| **Budget** | < USD 10,000 per service per accounting period (excluding staff salaries) | USD 10,000–100,000 per service per accounting period | > USD 100,000 per service per accounting period |
| **Time to first output** | 1–3 months from initiation | 3–12 months | > 12 months |
| **Recurrent cost** | Minimal; update requires re-running existing scripts on new data vintages | Moderate; annual field campaign or data purchase required | Substantial; continuous monitoring infrastructure and ongoing analytical effort |

**Concrete examples for Dimension A:**

- *Tier 1:* Estimating carbon sequestration using global default emission factors (IPCC Tier 1) applied to national mangrove extent mapped from freely available Landsat imagery. One analyst can produce the estimate in a few weeks.
- *Tier 2:* Estimating carbon sequestration using regionally calibrated stock-change factors derived from a literature synthesis, applied to extent data from Sentinel-2 with supervised classification. Requires a small remote sensing team and modest computing.
- *Tier 3:* Estimating carbon sequestration from repeated sediment core sampling, laboratory analysis of organic carbon content and radiometric dating, combined with high-resolution drone mapping of canopy condition. Requires field crews, laboratory access, and months of analytical work.

---

### 3.2 Dimension B: Accuracy and Confidence

| Criterion | Tier 1 — Indicative | Tier 2 — Moderate Confidence | Tier 3 — High Confidence |
|---|---|---|---|
| **Data quality** *(incl. transfer appropriateness for value transfer methods)* | Global or continental default values; coarse spatial resolution (>250 m); infrequent temporal updates (>5 years). For value transfer: source study context diverges substantially from target area (different income levels, ecology, or culture); transfer error likely >50% | Regional or national datasets; moderate resolution (10–30 m); annual updates. For value transfer: source study from same biogeographic region with comparable socioeconomic context; transfer error estimated and reported | Site-specific primary data; high resolution (<10 m); sub-annual or continuous monitoring. No value transfer used: all values derived from primary data in the accounting area |
| **Parameter uncertainty** | Coefficient of variation >50% or no uncertainty estimate available; reliance on global averages that may not reflect local conditions | CV 20–50%; parameters derived from regional meta-analysis or calibrated transfer functions | CV <20%; parameters derived from in-situ measurement with documented sampling design and statistical power |
| **Method validation and protocol maturity** | Method is plausible but not validated locally and lacks a standardised protocol; output is based on benefit transfer or expert judgment with ad hoc adaptation | Method has been applied and published in peer-reviewed studies for similar ecosystems in the same biogeographic region; documented protocol exists but requires local adaptation | Method has been validated against independent measurements in the specific accounting area; endorsed by a relevant technical body; step-by-step protocol with worked examples is available and has been applied without modification |
| **Sensitivity to assumptions** | Outputs are highly sensitive to 2 or more key assumptions that are not empirically constrained | Outputs are moderately sensitive; key assumptions are bounded by regional evidence | Outputs are robust; sensitivity analysis shows <20% change across plausible assumption ranges |
| **Spatial and temporal representativeness** | Single point estimate applied uniformly across the accounting area; no stratification by ecosystem condition or subtype | Stratified estimates (e.g., by ecosystem condition class or management zone) with some spatial differentiation | Spatially explicit estimates with documented variation; temporal dynamics captured within the accounting period |
| **Temporal consistency** | Method produces estimates that are not directly comparable across accounting periods without re-basing (e.g., uses published values that are periodically revised; requires full recalibration each round with potentially changing assumptions) | Method produces broadly comparable time series; key parameters updated annually from consistent sources; documented change-control procedure for recalibration | Method produces fully consistent, trend-compatible time series; same protocol and parameter set applied each period; deviations from prior rounds are documented and attributed |

**Concrete examples for Dimension B:**

- *Tier 1:* Estimating coastal protection value using a single global average of avoided damage per hectare of mangrove, applied uniformly to all mangrove patches regardless of exposure, forest width, or settlement proximity. No uncertainty bounds are reported.
- *Tier 2:* Estimating coastal protection using a regionally parameterised expected damage function that accounts for mangrove width and population density, with storm frequency from a 30-year cyclone database. Uncertainty propagated through Monte Carlo simulation.
- *Tier 3:* Estimating coastal protection using a coupled hydrodynamic-wave attenuation model (e.g., Delft3D, XBeach) calibrated with local bathymetry, tidal records, and wave buoy data, combined with high-resolution asset exposure mapping. Validated against observed flood extents.

---

### 3.3 Dimension C: Difficulty of Implementation

| Criterion | Tier 1 — Straightforward | Tier 2 — Moderate Complexity | Tier 3 — High Complexity |
|---|---|---|---|
| **Technical complexity** *(domestic expertise availability, independent of budget)* | Spreadsheet-based calculations or simple GIS overlay; skills available in any government statistical office | Intermediate GIS analysis, basic statistical modelling, or structured survey design; specialist skills needed but widely available domestically or through regional partners | Advanced numerical modelling (hydrodynamic, biogeochemical, econometric), machine learning, or complex spatial statistics; requires rare specialist expertise not available domestically without long-term training investment |
| **Institutional and legal barriers** *(data access)* | All required data are publicly available or held within a single agency; no inter-agency coordination required | Data must be obtained from 2–3 agencies under existing data-sharing protocols; moderate coordination effort | Data scattered across multiple agencies and jurisdictions with no established sharing mechanism; legal or political sensitivities |
| **Data availability** *(existence and accessibility of primary inputs; quality assessed in B)* | All required input data already exist and are accessible in usable formats | Most data exist but require cleaning, harmonisation, or gap-filling; some primary data collection needed | Substantial primary data collection required (e.g., multi-season field campaigns, dedicated household surveys, monitoring instruments) |
| **Institutional and method acceptance** | Method is well-established and routinely accepted by national statistics offices and SEEA EA reporting bodies (e.g., market price methods, IPCC Tier 1 defaults) | Method is accepted in principle but requires additional documentation or expert endorsement for official statistics use; some methodological debate exists in the literature | Method is methodologically contested or novel in the official statistics context (e.g., stated-preference / contingent valuation, stochastic production frontiers); acceptance by NSO or reporting body is not assured without additional peer review or policy endorsement |
| **Quality assurance and replicability** | Results can be checked against published benchmarks or cross-validated with independent global datasets; protocol is sufficiently explicit that a second analyst would reproduce the same estimate | QA requires comparison with regional studies or expert review; a second analyst with the same data would likely reach the same result with minor variation; reproducibility achievable but not trivial | Independent verification requires additional primary data collection or parallel modelling effort; replication by a second analyst may diverge due to underdetermined choices in the protocol or proprietary model code |

**Concrete examples for Dimension C:**

- *Tier 1:* Estimating recreational visits to coral reefs by extracting annual visitor numbers from a national park authority database and multiplying by an average consumer surplus per visit from a published meta-analysis.
- *Tier 2:* Estimating recreational value using a travel cost model fitted to a structured visitor survey, combined with spatial data on reef condition from a national monitoring programme.
- *Tier 3:* Estimating recreational value using a choice experiment that elicits willingness-to-pay for changes in reef condition attributes, combined with a spatially explicit reef condition model and visitor flow model.

---

## 4. Summary Assessment Matrix

The matrix below provides an indicative tier assignment for each service across the three dimensions. These assignments reflect the typical situation for a developing country in the tropical Indo-Pacific undertaking its first coastal ecosystem service accounts.

| Ecosystem Service | A: Feasibility (Resource) | B: Accuracy (Confidence) | C: Difficulty (Implementation) | Notes |
|---|---|---|---|---|
| **Wild fish provisioning** | | | | |
| — Tier 1 approach | 1 | 1 | 1 | National catch statistics with global price data |
| — Tier 2 approach | 2 | 2 | 2 | Spatially allocated catch with local market prices and ecosystem attribution |
| — Tier 3 approach | 3 | 3 | 3 | Stock assessment models, fishery-independent surveys, ecosystem-based attribution |
| **Fisheries nursery habitat** | | | | |
| — Tier 1 approach | 1 | 1 | 1–2 | Literature-based habitat contribution factors applied to extent data |
| — Tier 2 approach | 2 | 2 | 2 | Regionally calibrated nursery function estimates with connectivity modelling |
| — Tier 3 approach | 3 | 2–3 | 3 | Otolith microchemistry, acoustic telemetry, or stable isotope tracing |
| **Carbon sequestration** | | | | |
| — Tier 1 approach | 1 | 1 | 1 | IPCC Tier 1 defaults applied to extent from global maps |
| — Tier 2 approach | 1–2 | 2 | 2 | Country-specific emission factors from literature; national extent mapping |
| — Tier 3 approach | 3 | 3 | 3 | Flux measurements, sediment coring, allometric equations from local plots |
| **Coastal protection** | | | | |
| — Tier 1 approach | 1 | 1 | 1 | Replacement cost or global average avoided damage per hectare |
| — Tier 2 approach | 2 | 2 | 2–3 | Expected damage function with regional storm data and stratified exposure |
| — Tier 3 approach | 3 | 3 | 3 | Hydrodynamic modelling with local calibration and probabilistic damage assessment |
| **Sediment nourishment** | | | | |
| — Tier 1 approach | 1 | 1 | 1–2 | Proxy indicators with literature rates |
| — Tier 2 approach | 2 | 2 | 2 | Sediment budget approach using regional accretion rates and shoreline change |
| — Tier 3 approach | 3 | 2–3 | 3 | Sediment transport modelling calibrated with field measurements |
| **Coral reef recreation** | | | | |
| — Tier 1 approach | 1 | 1 | 1 | Visitor counts multiplied by unit value from meta-analysis |
| — Tier 2 approach | 2 | 2 | 2 | Travel cost model from structured visitor survey |
| — Tier 3 approach | 3 | 3 | 3 | Choice experiment linked to spatially explicit reef condition model |
| **Mangrove recreation** | | | | |
| — Tier 1 approach | 1 | 1 | 1 | Visitor counts and benefit transfer from comparable sites |
| — Tier 2 approach | 1–2 | 2 | 2 | On-site visitor survey with zonal travel cost method |
| — Tier 3 approach | 2–3 | 3 | 3 | Discrete choice experiment with ecosystem condition attributes |
| **Seagrass gleaning** | | | | |
| — Tier 1 approach | 1 | 1 | 1–2 | Household livelihood surveys (existing) with extrapolation |
| — Tier 2 approach | 2 | 2 | 2 | Dedicated gleaning yield surveys stratified by condition and season |
| — Tier 3 approach | 2–3 | 2–3 | 3 | Biophysical production model linked to seagrass health and household survey |

---

## 4a. Monetary Valuation Tiers

The tiers above (Section 4) apply to **physical measurement** of ecosystem service supply. Monetary valuation has its own tiered structure, based on the NCAVES/MAIA (2022) five-category method typology and the SEEA EA requirement for **exchange values** (not welfare/consumer surplus values).

### 4a.1 NCAVES/MAIA Method Category Reference

| Category | Method Type | Examples |
|---|---|---|
| **I** | Directly observable prices | Market prices for fish, timber, tour fees, beach nourishment costs |
| **II** | Prices from comparable markets | Prices from substitute products; regional price benchmarks |
| **III** | Prices embodied in market transactions | Resource rent; hedonic pricing; productivity change |
| **IV** | Revealed expenditure | Averting behaviour costs; travel cost method |
| **V** | Expected/simulated expenditure | Replacement cost; avoided damage cost; contingent valuation converted to SEV; value transfer |

> **Key principle:** SEEA EA monetary accounts record **exchange values** — the price at which a service would be transacted between an institutional supplier (the ecosystem) and a beneficiary. Consumer surplus (WTP above price) must be excluded or converted via the **simulated exchange value (SEV)** procedure.

---

### 4a.2 Monetary Valuation Tier Matrix — All Eight Services

| Ecosystem Service | Monetary Tier 1 | Monetary Tier 2 | Monetary Tier 3 |
|---|---|---|---|
| **Wild fish provisioning** | Value transfer from ESVD or published resource rent ratios; or simple catch × published average unit price | Resource rent = landed value − fishing costs (domestic data); spatially allocated catch × local market price **(current)** | Full production account: total revenue − intermediate inputs − CoE − CFC − return on produced assets (NCAVES formal decomposition) |
| **Fisheries nursery habitat** | Residual value method — nursery-attributed proportion of fish catch value from literature (Anneboina & Kumar 2017); or ESVD nursery value per ha | Productivity change — habitat-attributed fish biomass × market price **(current)** | Stochastic production frontier (SPF) — econometric estimation of nursery marginal product; or NPV of nursery service cash flows |
| **Carbon sequestration** | Value transfer from ESVD; or published social cost of carbon (SCC) per tonne CO2 from comparable contexts | SCC × net annual sequestration (Mg CO2/yr) **(current)** | Maintenance cost approach (cost of preventing equivalent CO2 from being emitted); or NPV of sequestration service: V = Σ [R_t/(1+r)^t] with appropriate social discount rate |
| **Coastal protection** | Value transfer — global average avoided damage per ha from ESVD (Barbier et al. 2011) | Annualised replacement cost of equivalent hard infrastructure (seawall/quaywall) **(current)** | Expected damage function (EDF) — probability-weighted avoided damages from hydrodynamic modelling (Menendez et al. 2020); or insurance premium differential |
| **Sediment nourishment** | Value transfer — published beach nourishment unit cost (currency/m³) from comparable island contexts × physical supply | Local beach nourishment cost (currency/m³) × physical sediment supply (m³/yr) **(current)** | Avoided erosion damage cost — value of assets protected by natural sediment supply; requires sediment transport modelling and asset exposure mapping |
| **Coral reef recreation** | Value transfer from ESVD or published per-visit recreation value; or direct tour fee × visit counts | Direct expenditure analysis — reef-attributable tourist spending (activity fees + allocated accommodation) **(current)** | Travel cost model (TCM) or random utility model (RUM); SEV conversion from contingent valuation / DCE; hedonic property pricing |
| **Mangrove recreation** | Value transfer from ESVD or comparable mangrove ecotourism sites × trip counts | Direct expenditure — tour operator fee × trips × group size **(current)** | Contingent valuation (WTP converted to SEV); applicable where nascent operations significantly understate market value |
| **Seagrass gleaning** | Value transfer — published per-hour imputed wage or per-kg harvest value from comparable subsistence gleaning studies | Equivalent wage (local rate × gleaning hours) + market value of harvest (price × kg) **(current)** | Household production function — full economic value including subsistence substitution; requires dedicated household survey with time-use and income module |

**Notes on the matrix:**
- **(current)** indicates the default method used in the accompanying SOPs.
- All Tier 1 monetary methods require at minimum a physical quantity estimate from the physical measurement pipeline.
- Tier 3 monetary methods generally require Tier 2 or 3 physical measurement as inputs.
- For asset valuation (Blue Carbon stocks, standing reef), apply NPV formula: V = Σ [R_t / (1+r)^t] for t = 0 to N, using a social discount rate of 3.5–5% (UK Treasury Green Book; Drupp et al. 2015).

---

### 4a.3 Monetary Tier Assessment Dimensions

Monetary valuation tiers are assessed on the same three dimensions as physical measurement, plus one additional dimension specific to monetary valuation. Criteria are calibrated for valuation rather than physical measurement:

| Criterion | Monetary Tier 1 | Monetary Tier 2 | Monetary Tier 3 |
|---|---|---|---|
| **A: Feasibility** | Minimal: desktop only, spreadsheet calculation, no surveys; < 1 month to first estimate | Moderate: local cost/price data collection, expenditure surveys, operator interviews; 1–6 months | High: primary stated-preference surveys (CV, DCE), full production account assembly, or hydrodynamic damage modelling; > 6 months |
| **B: Accuracy** *(incl. transfer appropriateness)* | Low–Moderate: transfer error may be 50–200% if source study context diverges from target; exchange value consistency depends on whether source study used exchange values or welfare measures | Moderate: reflects actual local market conditions; limited transfer error; CV 20–50%; transfer appropriateness checked if value transfer used | High: locally calibrated primary valuation; CV < 20%; exchange value consistency explicitly verified; sensitivity analysis documented |
| **B: Temporal consistency** | Fixed published values used; estimates may not be updatable annually without re-basing; inter-period comparability uncertain | Parameters updated from consistent annual sources (market prices, cost indices); documented update procedure | Fully consistent time series; same methodology and data sources applied each period; deviations attributed and documented |
| **C: Difficulty** | Low: standard spreadsheet; value transfer databases (ESVD) freely accessible; skills available in any statistical office | Moderate: requires local data collection, inter-agency coordination (fisheries, tourism, engineering departments); skills widely available | High: stated-preference survey design; econometric modelling (SPF, RUM, hedonic); hydrodynamic damage modelling; specialist expertise required |
| **D: Exchange value consistency** *(monetary only)* | Risk: method uses welfare values (WTP/consumer surplus) without SEV conversion; not directly compliant with SEEA EA exchange value requirement | Acceptable: method uses observed market prices or cost-based proxies; exchange value compliance straightforward; any WTP component is converted to SEV with documented procedure | Fully compliant: primary valuation explicitly designed to produce exchange values; SEV conversion applied and documented where WTP used; reviewed against NCAVES/MAIA Category classification |

> **Double-counting risk (all monetary tiers):** Several services in this framework share physical pathways — fisheries nursery supports wild fish provisioning; sediment nourishment protects the same coastal assets as coastal protection in beach-backed reef systems; carbon sequestration and carbon stock retention are distinct flows that must not both be monetised against the same tonne of carbon. Review the full set of service estimates before aggregating to confirm no physical flow is valued twice. This risk is structural and not fully captured by any individual-method tier score.

---

---

## 5. Interpreting the Tiers

### 5.1 When to Use Each Tier

**Tier 1 — Rapid Assessment and Baseline Accounts**

Use Tier 1 when the objective is to produce a first-generation ecosystem service account that establishes orders of magnitude, identifies the most important services, and demonstrates the feasibility of natural capital accounting to policymakers. Tier 1 is appropriate when:

- The country or jurisdiction is compiling ecosystem accounts for the first time.
- Timelines are short (e.g., producing estimates for a national development plan or international reporting commitment within 6 months).
- Budget is limited and no dedicated project funding is available.
- The primary audience needs directional information ("Is this service worth tens of thousands or tens of millions?") rather than precise estimates.
- The purpose is to prioritise which services warrant deeper investment in Tier 2 or 3 measurement.

Tier 1 estimates should always be presented with explicit caveats about the level of uncertainty and the assumptions underpinning them. They are not suitable for use in cost-benefit analyses of specific investments or for setting payment-for-ecosystem-service rates.

**Tier 2 — Operational Accounts and Policy Analysis**

Use Tier 2 when the objective is to produce accounts that are robust enough to inform policy decisions, track trends over time, and support comparisons across regions or ecosystem types. Tier 2 is appropriate when:

- An initial Tier 1 account has been produced and there is demand for more reliable estimates.
- The accounts will be used to inform spatial planning, protected area management, or budget allocation decisions.
- The country has access to moderate technical capacity (e.g., a national remote sensing agency, a fisheries research institute, university partnerships).
- Multi-year project funding is available (e.g., through GEF, World Bank WAVES, bilateral donors).
- The accounting period will be repeated, justifying investment in reusable methods and datasets.

Tier 2 represents the appropriate target for most national ecosystem accounting programmes in the medium term.

**Tier 3 — Investment-Grade Accounts and Research Frontier**

Use Tier 3 when the objective is to produce high-confidence estimates suitable for economic valuation of specific policy interventions, natural capital disclosure, sovereign wealth fund management, or legal proceedings. Tier 3 is appropriate when:

- The accounts will inform decisions involving large financial flows (e.g., blue bond issuance, insurance pricing, infrastructure siting).
- There is a legal or regulatory requirement for high-precision environmental information.
- The ecosystem is of exceptional conservation or economic value and warrants the investment.
- Strong research partnerships and sustained institutional capacity are in place.
- The jurisdiction aims to be at the frontier of SEEA EA implementation.

Tier 3 should be seen as aspirational for most developing countries in the near term.

### 5.2 Mixing Tiers Across Services and Sub-Procedures

It is both expected and advisable to use different tiers for different services and different sub-procedures within a single service. For example:

- A country might use Tier 2 for carbon sequestration (because extent mapping capacity is well developed) and Tier 1 for coastal protection (because no hydrodynamic modelling capacity exists).
- Within wild fish provisioning, a country might use Tier 2 for catch estimation and Tier 1 for resource rent (because cost-of-fishing data are unavailable).

The guiding principle is that the overall account quality is determined by the weakest link. If one sub-procedure is at Tier 1, the overall service estimate should be characterised as Tier 1 for accuracy purposes, even if other sub-procedures are at Tier 2 or 3.

### 5.3 Progression Pathways

The tiers define a natural progression:

1. **Establish baseline at Tier 1.** Produce an initial estimate using globally available data and default values. Document all assumptions and data gaps.
2. **Identify bottlenecks.** Use the three-dimensional assessment to identify which dimension is the binding constraint for moving to Tier 2.
3. **Invest strategically in Tier 2.** Prioritise investments that unlock the largest accuracy gains for the lowest additional cost. Often this means improving extent and condition mapping (which benefits multiple services simultaneously) before investing in service-specific modelling.
4. **Target Tier 3 selectively.** Move to Tier 3 only for services where policy demand and institutional capacity justify the investment.

---

## 6. Trade-Offs and Recommendations for Resource-Constrained Teams

### 6.1 The Fundamental Trade-Off

There is an inherent tension between accuracy and feasibility. Moving from Tier 1 to Tier 3 on accuracy almost always requires moving from Tier 1 to Tier 3 on resource requirements. However, the relationship is not linear. Certain investments yield disproportionate accuracy gains:

**Most cost-effective investments:**

1. **National ecosystem extent mapping** (moderate cost, benefits all services). A national coastal habitat map at 10 m resolution from Sentinel-2 imagery is achievable within a Tier 2 resource envelope and immediately improves the spatial basis for every service estimate.
2. **Ecosystem condition classification** (moderate cost, benefits all services). Even a simple three-class condition scheme (good, moderate, degraded) applied to existing extent maps allows stratification that substantially reduces transfer error.
3. **Harvesting existing data** (low cost, high return). Many countries have fisheries catch data, visitor statistics, and household survey data that have never been compiled for ecosystem accounting purposes.

**Least cost-effective investments:**

1. **Primary biophysical data collection for a single service** (high cost, benefits only one service). Deploying eddy covariance towers or wave buoys is expensive and benefits only the carbon or coastal protection account respectively.
2. **Bespoke stated preference surveys** (high cost, contestable results). Choice experiments and contingent valuation studies are expensive, methodologically demanding, and often yield results sensitive to design choices.

### 6.2 Recommended Strategy for a Typical Developing Country

For a coastal developing country with limited statistical capacity, moderate scientific capacity, and access to a single round of project funding (USD 200,000–500,000 over 2–3 years):

**Phase 1 (Months 1–6): Tier 1 baseline for all eight services**

- Compile all available secondary data (national catch statistics, park visitor records, existing household surveys, published literature).
- Produce a national coastal habitat extent map from freely available satellite imagery.
- Apply IPCC default values for carbon, global meta-analysis values for cultural services, and literature-based estimates for regulating services.
- Produce a complete Tier 1 account for all eight services.
- Estimated cost: USD 20,000–50,000 (primarily staff time).

**Phase 2 (Months 6–18): Tier 2 for priority services**

- Select 3–4 services for Tier 2 improvement based on policy relevance and data availability.
- Invest in ecosystem condition mapping.
- Conduct targeted field campaigns for calibration and validation.
- Develop regionally calibrated parameters for carbon, nursery function, and fish provisioning.
- Implement a structured visitor survey at key recreation sites.
- Estimated cost: USD 100,000–250,000.

**Phase 3 (Months 18–36): Consolidation and institutionalisation**

- Produce a complete second-generation account combining Tier 2 estimates for priority services with Tier 1 for the remainder.
- Document all methods in SOPs suitable for repetition by government staff.
- Train national counterparts.
- Identify services where Tier 3 investment would be justified.
- Estimated cost: USD 50,000–100,000 (primarily staff time and training).

### 6.3 Common Pitfalls to Avoid

1. **Pursuing Tier 3 accuracy on one service while neglecting others entirely.** A complete Tier 1 account for all services is more useful for policy than a Tier 3 account for carbon alone.
2. **Treating the tiers as quality labels rather than fit-for-purpose descriptors.** A Tier 1 estimate that is clearly documented and honestly caveated is preferable to a Tier 3 estimate that is never completed.
3. **Investing in primary data collection before exhausting secondary data.** Many developing countries have more data than they realise, scattered across fisheries agencies, tourism boards, port authorities, and household survey programmes.
4. **Ignoring the difficulty dimension.** Some procedures that appear feasible on paper fail in practice because of institutional barriers.
5. **Failing to plan for recurrent costs.** An account that cannot be updated is of limited value. The choice of tier should consider not just the cost of the first estimate but the cost of maintaining the account over time.

### 6.4 When to Accept Tier 1

Tier 1 should be considered acceptable — and not merely a stepping stone — when:

- The service is of low relative magnitude in the accounting area and does not warrant further investment (e.g., mangrove recreation in a country where mangrove tourism is negligible).
- The service is inherently difficult to measure beyond Tier 1 and the methodological frontier does not yet offer a clear Tier 2 path (e.g., sediment nourishment).
- The account is being produced for awareness-raising or advocacy purposes rather than operational decision-making.
- The country is in the early stages of SEEA EA implementation and building institutional buy-in is more important than producing precise numbers.

---

## 7. Applying the Framework to SOP Review

When reviewing an existing SOP or designing a new one, apply the framework as follows:

1. **Decompose the SOP into sub-procedures.** Most SOPs contain 4–8 distinct analytical steps. Assess each sub-procedure independently.

2. **Score each sub-procedure on each dimension.** For each of the three dimensions, assign a tier (1, 2, or 3) using the criteria in Section 3. Where a sub-procedure falls between tiers, assign the higher tier (round up on resource and difficulty, round down on accuracy).

3. **Identify the binding constraint.** For each sub-procedure, determine which dimension is the most limiting.

4. **Assess coherence within the SOP.** Check whether tier assignments across sub-procedures are coherent. An SOP that uses Tier 3 biophysical modelling but Tier 1 valuation has an internal inconsistency.

5. **Recommend a target tier profile.** Based on available resources, policy context, and institutional capacity, recommend a target tier for each sub-procedure.

6. **Document assumptions and limitations.** For each sub-procedure at Tier 1 or Tier 2, explicitly document what would be needed to move to the next tier and what accuracy improvement would be expected.

---

## 8. Version Control and Updates

This framework should be reviewed and updated when:

- The SEEA EA technical guidance is revised by the UN Committee of Experts on Environmental-Economic Accounting.
- Significant new methodological developments change the feasibility or accuracy of specific procedures (e.g., new satellite missions that enable routine high-resolution coastal habitat mapping).
- Practical experience from applying the framework to SOP review reveals gaps or inconsistencies in the tier definitions.

---

*Framework version: 1.0*
*Date: February 2026*
*Applicable standard: SEEA EA (UN 2021)*
*Ecosystem scope: Coastal and marine (mangrove, seagrass, coral reef)*
