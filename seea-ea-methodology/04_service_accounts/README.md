# Service Accounts

This folder contains skills for quantifying ecosystem services (physical supply and monetary value) following SEEA EA methodology and CICES classification.

## Contents Overview

Service accounts measure the benefits provided by ecosystems to human populations. This folder contains:

| Document | Scope | CICES Categories |
|----------|-------|-----------------|
| `skill_services_measurement.md` | General SOP for all services | Provisioning, Regulating, Cultural (overview) |
| `skill_services_provisioning.md` | Wild-caught fish, wood/fuel | 3.1 (food), 3.2 (materials) |
| `skill_services_regulating.md` | Nursery, carbon, coastal protection, sediment | 2.1–2.2 (maintenance of biotic processes, physical processes) |
| `skill_services_cultural.md` | Recreation, gleaning, spiritual | 7.1 (recreation), 7.2 (cultural, spiritual) |

---

## skill_services_measurement.md

**Purpose:** Framework for measuring any ecosystem service following SEEA EA methodology.

**Covers:**
- Service classification and CICES alignment
- Physical quantification (biophysical measurement or models)
- Monetary valuation (market-based and non-market methods)
- Valuation methods by tier (Tier 1 = simple, Tier 3 = complex)
- Value type documentation (market vs. non-market, use vs. use value)
- Aggregation to supply and use tables
- Uncertainty and limitations

**Use when:**
- Starting service account development for any ecosystem
- Choosing between Tier 1/2/3 valuation methods
- Deciding on value type (market vs. shadow price)
- Aggregating service values across ecosystem or sectors

---

## Provisioning Services: `skill_services_provisioning.md`

**SEEA EA Sections:** 6.1

**Services covered:**
- **Wild fish provisioning** (capture fisheries) — CICES 3.1.1
- **Wood provisioning** (fuel wood, timber from mangroves) — CICES 3.2.1

### Wild Fish Provisioning

**Ecosystem types:** Coral reefs, seagrass, mangroves, estuaries

**Physical quantification:**
- Current catch data (kg/yr by species/gear)
- Sustainable harvest potential (relative to stock assessment)
- Output: Annual fish supply (kg/yr)

**Monetary valuation:**
- Market price (USD/kg) × catch volume
- Value type: Market-based
- Tier 1: National average price × landings
- Tier 2: Species-specific price × species catch
- Tier 3: Market segmentation (export vs. domestic) × catch composition

**Data needed:**
- Fisheries landings records (national, regional, or project catch records)
- Market price data (fish market surveys, wholesale prices)
- Catch composition by species/family
- Stock status assessment (is harvest sustainable?)

### Wood Provisioning (Mangroves)

**Physical quantification:**
- Mangrove extent (ha)
- Wood density/volume (m³/ha)
- Annual sustainable harvest (m³/yr)
- Output: Annual wood supply (m³/yr or Mg/yr)

**Monetary valuation:**
- Market price (USD/m³) × volume
- Value type: Market-based
- Tier 1: Average regional wood price
- Tier 2: Fuelwood vs. charcoal price differentiation
- Tier 3: Full supply chain (processing margins, transport)

---

## Regulating Services: `skill_services_regulating.md`

**SEEA EA Sections:** 6.2–6.5

**Services covered:**
- **Fisheries nursery** (CICES 6.1.1)
- **Carbon sequestration** (CICES 2.3.2)
- **Coastal protection** (CICES 2.2.6)
- **Sediment nourishment** (CICES 2.2.3)

### Fisheries Nursery Service

**Ecosystem types:** Coral reefs, seagrass meadows

**Physical quantification:**
- Fish density in nursery habitat vs. open ocean (Log Response Ratio)
- Enhanced juvenile survival due to nursery provision
- Harvestable contribution to adult stock (kg/yr)
- Output: Additional fish biomass available for harvest (kg/yr)

**Monetary valuation:**
- Market price of adult fish (USD/kg) × harvestable contribution
- Value type: Market-based (indirect)
- Tier 1: Residual value method (attribute portion of fishery rent to nursery)
- Tier 2: Productivity change × market price (LRR method)
- Tier 3: Stochastic production frontier (econometric)

**Key parameters:**
- Coral reef nursery LRR: ~31% (literature meta-analysis)
- Seagrass nursery LRR: ~13% (literature meta-analysis)
- Juvenile survival: ~5% (ecological estimate)

### Carbon Sequestration Service

**Ecosystem types:** Mangroves, seagrass (not coral reefs)

**Physical quantification:**
- Ecosystem extent (ha)
- Net Carbon Production (NCP) rate (Mg CO₂/ha/yr)
- Annual sequestration: Extent × NCP
- Output: Annual CO₂ sequestration (Mg CO₂/yr)

**Monetary valuation:**
- Social Cost of Carbon (SCC) × sequestration volume
- Value type: Non-market (shadow price)
- Tier 1: U.S. IWG SCC ($51/Mg CO₂ at 3% discount)
- Tier 2: EPA updated SCC ($185/Mg CO₂ at 2% discount)
- Tier 3: Domestic carbon market price (if available)

### Coastal Protection Service

**Ecosystem types:** Coral reefs, mangroves, salt marshes

**Physical quantification:**
- Reef/forest extent (km of coastline or ha buffer)
- Wave attenuation / energy dissipation (%)
- Protected assets (building values, infrastructure)
- Output: Length/area of protected coastline (km or ha)

**Monetary valuation:**
- Replacement cost method (engineering cost to build seawall)
- Value type: Market-based (indirect)
- Tier 1: Average seawall cost (USD/m) × protected coastline
- Tier 2: Asset-based (value of protected property)
- Tier 3: Avoided damage (risk reduction approach)

### Sediment Nourishment Service

**Ecosystem types:** Coral reefs, mangroves, seagrass

**Physical quantification:**
- CaCO₃ or sediment production rate (m³/ha/yr or Mg/ha/yr)
- Beach nourishment needs (estimated from erosion rate)
- Annual sediment supply to downdrift beaches (m³/yr)
- Output: Annual sediment nourishment (m³/yr or Mg/yr)

**Monetary valuation:**
- Replacement cost of beach nourishment (USD/m³)
- Value type: Market-based (indirect)
- Tier 1: Average beach renourishment cost (USD/m × beach length)
- Tier 2: Cost differentiated by sand type and transport distance
- Tier 3: Engineering design + cost analysis per project

---

## Cultural Services: `skill_services_cultural.md`

**SEEA EA Sections:** 6.6

**Services covered:**
- **Coral reef recreation** (CICES 7.1.1) — diving, snorkelling, tourism
- **Mangrove recreation** (CICES 7.1.1) — kayaking, birdwatching, ecotourism
- **Seagrass gleaning** (CICES 7.1.2 + 7.2) — traditional harvesting, cultural harvesting

### Coral Reef Recreation

**Ecosystem:** Coral reefs

**Physical quantification:**
- Annual visitor count (trips/yr)
- Average trip duration (hours/person)
- Output: Annual recreation supply (visitor-trips/yr)

**Monetary valuation:**
- Direct expenditure method: visitor spending per trip (USD/person)
- Contingent valuation: willingness-to-pay
- Travel cost method: inferred from visitor origin distance
- Value type: Market-based
- Tier 1: Average daily spend (USD) × visitor-days
- Tier 2: Expenditure segmented by visitor type (day-trip vs. resort stay)
- Tier 3: Full economic impact analysis (multipliers, jobs)

**Data needed:**
- Resort visitor records (annual arrivals)
- Dive centre logs (dives per month)
- Tourist expenditure surveys (accommodation, food, activities)
- Tourist demographics and origin

### Mangrove Recreation (Ecotourism)

**Ecosystem:** Mangrove forests

**Physical quantification:**
- Kayak tours/birdwatching trips per year
- Average group size
- Trip duration
- Output: Annual ecotourism supply (visitor-trips/yr)

**Monetary valuation:**
- Per-trip fee (USD/person/trip)
- Operator spending on maintenance, guide wages, fuel
- Visitor indirect spending (accommodation, food, transport to site)
- Value type: Market-based (Tier 2) to full economic impact (Tier 3)

### Seagrass Gleaning (Cultural)

**Ecosystem:** Seagrass meadows

**Physical quantification:**
- Annual gleaner count (persons engaged)
- Hours per gleaner per year (effort)
- Harvest per gleaner (kg/yr)
- Output: Annual gleaning supply (kg/yr or person-hours/yr)

**Monetary valuation:**
- Equivalent wage method: market wage × gleaning hours
- Harvest value method: market price × gleaning yield
- Value type: Mixed (wage + product value)
- Tier 1: Local daily wage × estimated annual effort
- Tier 2: Gleaner survey (time use) × local wage
- Tier 3: Full livelihood analysis (gleaning + other income)

---

## Workflow: From Data to SEEA EA Service Account

### Generic Workflow (All Services)

```
1. Choose service(s) to account
   └─ Use: skill_services_measurement.md (Section 1)

2. Review ecosystem-specific SOP
   └─ Use: skill_services_provisioning/regulating/cultural.md

3. Gather data
   └─ Internal: condition/extent data (use what you have)
   └─ External: catch/price data, tourism records, valuation parameters

4. Calculate physical supply
   └─ Use: ecosystem-specific skill (physical quantification section)

5. Choose valuation method & value type
   └─ Use: skill_services_measurement.md (Sections 3–4)
   └─ Use: ecosystem-specific skill (monetary valuation section)

6. Document assumptions & sensitivity
   └─ Use: skill_services_measurement.md (Section 5)

7. Produce SEEA EA service account
   └─ Use: 05_seea_accounting_tables/supply_and_use_table_format.md [to be added]

8. Prepare supply and use tables
   └─ Output: Physical and monetary service tables by service and ecosystem
```

---

## Key Decisions You'll Face

| Decision | Guidance |
|----------|----------|
| **Service priority** | Start with 1–2 services with best data; expand later | |
| **Physical quantification method** | Direct measurement vs. literature values vs. modelling | |
| **Valuation method (Tier)** | Limited budget → Tier 1; good data → Tier 2; research → Tier 3 |
| **Value type** | Market vs. shadow price — depends on service and policy use |
| **Monetary baseline** | Which year's prices? Currency? Discount rate for future values? |
| **Aggregation scope** | Annual vs. multi-year? Ecosystem-wide vs. site-level? |

---

## Integration with Condition & Extent Accounts

- **Extent accounts** (02_extent_accounts/): Service supply = ecosystem function × per-hectare rate × extent (ha)
- **Condition accounts** (03_condition_accounts/): Service productivity often depends on condition state (e.g., healthy reef → higher recreation value)
- **SEEA Accounting tables** (05_seea_accounting_tables/): Service account → supply and use table format

---

## Quick Reference: Service Skill Comparison

| Service | Ecosystem | Physical Input | Valuation Method | Complexity |
|---------|-----------|----------------|------------------|-----------|
| Wild fish provisioning | All | Catch data (kg/yr) | Market price × catch | Low–Medium |
| Fisheries nursery | Coral, Seagrass | Juvenile production (kg/yr) | Market price × LRR × survival | Medium |
| Carbon sequestration | Mangrove, Seagrass | Sequestration rate (Mg CO₂/yr) | SCC (USD/Mg CO₂) | Medium |
| Coastal protection | Coral, Mangrove | Protected coastline (km) | Replacement cost (USD/m) | Medium–High |
| Reef recreation | Coral | Visitor count (trips/yr) | Expenditure per trip (USD) | Medium |
| Mangrove ecotourism | Mangrove | Ecotourism trips (trips/yr) | Per-trip fee + indirect spending | Medium |
| Gleaning | Seagrass | Harvest (kg/yr) + effort (hrs/yr) | Wage + harvest value | Medium |

---

## Common Questions

**Q: Should I use local prices or global commodity prices?**
A: Local retail/market prices preferred for SEEA EA. See skill_services_provisioning.md (pricing section).

**Q: What if I don't have fisheries landings data?**
A: Estimate from ecosystem productivity (condition biomass) × sustainable harvest rate. See skill_services_provisioning.md Tier 1 approach.

**Q: How do I value a service that's not traded in markets?**
A: Use shadow prices (SCC for carbon, replacement cost for coastal protection). See skill_services_measurement.md (non-market valuation).

**Q: Should I include jobs/employment in service value?**
A: Yes, document separately as "economic significance" but distinguish from direct ecosystem service value. See skill_services_measurement.md.

**Q: How do I handle discounting for future benefits?**
A: Depends on context. For provisioning: no discount (annual flow). For carbon: use standard social discount rate. See ecosystem-specific skill.

---

**Related:** UN SEEA EA (2021) Chapter 6, CICES v5.1 classification, NCAVES monetary valuation guidance, SEEA-CF (supply-use tables)
