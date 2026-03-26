# Ecosystem Services Accounts -- Step-by-Step Guide

## Structure

This guide is split into two independent parts:

- **Part A: Physical quantification** -- measure the service in physical units (kg, Mg CO2, visitors, metres). This is a complete account on its own.
- **Part B: Monetary valuation** -- assign economic values (USD/yr). Requires Part A first. Optional for a first account.

Each part has two pathways: Pathway 1 (no primary data) and Pathway 2 (local data available).

---

# PART A: PHYSICAL QUANTIFICATION

## Service 1: Carbon sequestration

### Where to get the data

| Data needed | Part | Source | URL |
|-------------|------|--------|-----|
| Ecosystem extent (ha) | A | Your extent account, or Global Mangrove Watch / Allen Coral Atlas | globalmangrovewatch.org, allencoralatlas.org |
| NCP rates (Mg CO2/ha/yr) | A | Published literature (see table below) or IPCC Wetlands Supplement | ipcc.ch |
| Primary carbon stock data | A | Field measurements: soil cores, allometric equations | National forest inventories |
| Social cost of carbon | B | US EPA Interagency Working Group (2021) | USD 51/Mg CO2 |
| Voluntary carbon market price | B | Ecosystem Marketplace, Verra VCS registry | ecosystemmarketplace.com, verra.org |

**NCP rates from literature (Mg CO2/ha/yr):**

| Ecosystem | Conservative | Central | High | Key source |
|-----------|---:|---:|---:|-----------|
| Mangroves | 2.0 | 3.7 | 17.2 | Alongi (2014), IPCC Wetlands Supplement |
| Seagrass | 0.4 | 1.3 | 4.4 | Fourqurean et al. (2012), Duarte et al. (2005) |
| Salt marshes | 1.5 | 2.1 | 6.0 | Chmura et al. (2003), IPCC Wetlands Supplement |

Use the conservative estimate for Tier 1 accounts. Use regionally calibrated values where available.

### Pathway 1: Literature rates (no field carbon data)

| Step | What to do | Your values |
|------|-----------|------------|
| 1 | Get ecosystem extent (ha) from your extent account | Mangrove: ___ ha, Seagrass: ___ ha |
| 2 | Look up NCP rate from table above (or IPCC Wetlands Supplement for your climate zone) | Mangrove: ___ Mg CO2/ha/yr, Seagrass: ___ Mg CO2/ha/yr |
| 3 | Physical supply = Extent x NCP rate | ___ Mg CO2/yr |

### Pathway 2: Primary carbon data

If you have soil carbon measurements, allometric biomass estimates, or flux tower data:

| Step | What to do |
|------|-----------|
| 1 | Calculate above-ground biomass (AGB) from allometric equations |
| 2 | Calculate below-ground biomass (BGB) using root:shoot ratios |
| 3 | Estimate soil organic carbon (SOC) from sediment cores |
| 4 | Sum total carbon stock (Mg C/ha) |
| 5 | Apply sequestration rate (annual carbon accumulation) |
| 6 | Convert to CO2 equivalents: Mg C x 3.67 = Mg CO2 |

**Physical output:** Total Mg CO2/yr sequestered, by ecosystem type

---

## Service 2: Fish provisioning

### Where to get the data

| Data needed | Part | Source | URL |
|-------------|------|--------|-----|
| Total annual catch (kg/yr) | A | National fisheries agency landing records | fao.org/fishery |
| Catch by country (Tier 1, no local data) | A | FAO FishStatJ or Sea Around Us | seaaroundus.org |
| Species-habitat associations | A | FishBase species database | fishbase.org |
| Fishing effort (spatial) | A | Global Fishing Watch (vessel tracking) | globalfishingwatch.org |
| Market prices per species (USD/kg) | B | Local fish market surveys, national statistics offices | |
| Fishing costs (labour, fuel, gear) | B | Fisher household surveys, cooperative records | GOAP provides survey templates |
| Vessel depreciation | B | Purchase price / expected lifespan (typically 15-20 years) | |

### Pathway 1: National statistics

| Step | What to do | Your values |
|------|-----------|------------|
| 1 | Get total annual catch from fisheries agency or FAO FishStatJ | ___ kg/yr |
| 2 | Disaggregate by species using landing records or Sea Around Us | |
| 3 | Assign catch to ecosystem type using FishBase species-habitat associations | Reef: ___ kg, Seagrass: ___ kg, Pelagic: ___ kg |

### Pathway 2: Fisher survey data

| Step | What to do |
|------|-----------|
| 1 | Compile catch by species from landing surveys |
| 2 | Record gear type and effort (trips, hours) |
| 3 | Disaggregate by ecosystem using FishBase species-habitat literature |
| 4 | Calculate CPUE (catch per unit effort) if effort data available |

**Physical output:** Total kg/yr by ecosystem type and species group

---

## Service 3: Coastal protection

### Where to get the data

| Data needed | Part | Source | URL |
|-------------|------|--------|-----|
| Ecosystem extent along coastline | A | GIS overlay of your extent account with coastline | From your extent account |
| Building footprints behind buffer | A | OpenStreetMap or Microsoft Building Footprints | openstreetmap.org |
| Population behind buffer | A | Census data or WorldPop gridded estimates | worldpop.org |
| Wave exposure data (Tier 2-3) | A | NOAA WaveWatch III, Copernicus Marine Service | |
| Seawall / breakwater cost per metre | B | Engineering firms, government infrastructure budgets | Range: USD 2,000-15,000/m |
| Infrastructure lifespan | B | Engineering standards | Typically 30-50 years |
| Wave attenuation by reefs | B | Beck et al. (2018): reefs reduce wave energy by 97% average | |

### Pathway 1: Spatial overlay

| Step | What to do | Your values |
|------|-----------|------------|
| 1 | Map ecosystem extent along coastline using your extent account in GIS | ___ m reef, ___ m mangrove |
| 2 | Overlay with OpenStreetMap buildings or WorldPop population within 200 m of shore | |
| 3 | Record: length of coastline protected (m), number of buildings, population behind buffer | |

### Pathway 2: Wave attenuation modelling

If you have bathymetry and wave data (NOAA WaveWatch III), apply a wave attenuation model to quantify the reduction in wave energy provided by the reef or mangrove.

**Physical output:** Metres of coastline protected, buildings/people behind ecosystem buffer

---

## Service 4: Recreation and tourism

### Where to get the data

| Data needed | Part | Source | URL |
|-------------|------|--------|-----|
| Total visitor arrivals | A | National tourism authority, airport/port statistics | UNWTO: unwto.org |
| Accommodation statistics | A | Hotel/resort occupancy records, national statistics | |
| Dive/snorkel activity counts | A | Dive centres, tour operators, PADI statistics | Local dive operator associations |
| MPA visitor counts | A | Park management authorities, entry permits | |
| Activity fees (dive, snorkel, kayak) | B | Operator records, online pricing | Direct observation |
| Visitor expenditure surveys | B | Tourist motivation and spending surveys | |
| Reef-attributable accommodation share | B | Tourist surveys asking "what share of your trip is for the reef?" | |

**Tier 1 shortcut (no local data):** Use UNWTO country data for total arrivals. Estimate reef-visitor share from literature (30-60% of visitors to tropical coastal destinations do reef-based activities).

### Pathway 1: Tourism statistics

| Step | What to do | Your values |
|------|-----------|------------|
| 1 | Get total visitor numbers from tourism authority or UNWTO | ___/yr |
| 2 | Estimate reef/ecosystem-attributable visitors (from surveys, MPA records, or Tier 1 literature share) | ___/yr |
| 3 | Record: dive trips, snorkel trips, kayak trips | |

### Pathway 2: Operator records

| Step | What to do |
|------|-----------|
| 1 | Compile activity records from dive centres, tour operators, MPA entry |
| 2 | Count participants per activity type |
| 3 | Record effort (trips/yr, hours/yr) |

**Physical output:** Visitor trips/yr or hours/yr by ecosystem type and activity

---

## Service 5: Nursery habitat

### Where to get the data

| Data needed | Part | Source | URL |
|-------------|------|--------|-----|
| Fish density in nursery vs non-nursery areas | A | Field surveys (UVC, seine nets), national monitoring programs | |
| Log Response Ratio (LRR) if no field data | A | Literature meta-analyses: coral reef 31%, seagrass 13% | Nagelkerken et al. (2015), Igulu et al. (2014) |
| Total fish biomass | A | From your fish provisioning account (Part A above) | |
| Juvenile survival rate | A | Standard ecological assumption: 5% | Literature |
| Market price of fish | B | Same as fish provisioning | |

### Steps

| Step | What to do | Your values |
|------|-----------|------------|
| 1 | Get fish density data for nursery areas (mangrove, seagrass) and non-nursery areas (open reef). If no field data, use LRR from literature (coral 31%, seagrass 13%). | |
| 2 | Calculate log response ratio (LRR): ln(density_nursery / density_non_nursery) | |
| 3 | Apply LRR to total fish biomass from provisioning account | |
| 4 | Apply juvenile survival rate (~5%) to get harvestable biomass from nursery | |

**Physical output:** kg juvenile biomass/yr attributable to nursery habitat

---

## Part A Summary: Physical Supply Table

**This is a valid, complete account.**

| Service | Unit | Coral reefs | Seagrass | Mangroves | Total |
|---------|------|---:|---:|---:|---:|
| Fish provisioning | kg/yr | | | | |
| Carbon sequestration | Mg CO2/yr | | | | |
| Coastal protection | m coastline | | | | |
| Nursery habitat | kg biomass/yr | | | | |
| Recreation | visitors/yr | | | | |
| Gleaning | hours/yr | | | | |

---

## Part A continued: Physical Use Table

The supply table shows which ecosystems provide each service. The **use table** shows which economic sectors or population groups benefit from each service. For each service, ask: **"Who benefits from this?"** and assign the physical quantity accordingly.

**Beneficiary mapping:**

| Service | Primary beneficiary | Rationale |
|---------|-------------------|-----------|
| Fish provisioning | Fisheries sector | Commercial and artisanal fishers harvest the catch |
| Carbon sequestration | Global community | Climate regulation benefits everyone globally |
| Coastal protection | Coastal households + Government | Protects private property and public infrastructure |
| Nursery habitat | Fisheries sector | Supports future fish stocks harvested by fishers |
| Recreation | Tourism sector | Tour operators and dive centres capture visitor spending |
| Gleaning | Coastal households | Subsistence activity by local coastal communities |

**Physical Use Table:**

| Service | Unit | Fisheries | Tourism | Coastal households | Government | Global community | Total |
|---------|------|---:|---:|---:|---:|---:|---:|
| Fish provisioning | kg/yr | | | | | | |
| Carbon sequestration | Mg CO2/yr | | | | | | |
| Coastal protection | m coastline | | | | | | |
| Nursery habitat | kg biomass/yr | | | | | | |
| Recreation | visitors/yr | | | | | | |
| Gleaning | hours/yr | | | | | | |

**Note:** Some services may be shared across beneficiaries (e.g., coastal protection benefits both private households and government-owned infrastructure). The total in the use table must equal the total in the supply table -- the same physical quantity, just organized differently.

---

# PART B: MONETARY VALUATION (builds on Part A)

**Only proceed to Part B if you have the economic data needed.** Part A alone is useful for policy.

## Valuation method selection

| Service | Physical quantity (Part A) | Method | Economic data needed | Where to find it |
|---------|--------------------------|--------|---------------------|-----------------|
| Fish provisioning | kg/yr by species | Resource rent | Market prices, fishing costs | Local fish markets, fisher surveys |
| Carbon sequestration | Mg CO2/yr | SCC or market price | Carbon price | US EPA ($51), Ecosystem Marketplace, Verra, IDXCarbon |
| Coastal protection | m coastline, assets | Replacement cost | Engineering cost per m | Govt infrastructure budgets ($2K-15K/m) |
| Nursery habitat | kg biomass/yr | Market price | Same market prices as fish | Same as fish provisioning |
| Recreation | visitors/yr | Direct expenditure | Spending per visitor | Tour operators, MPA fee records, tourist surveys |
| Gleaning | hours/yr, harvest kg/yr | Equivalent wage + market | Wage rate, harvest prices | National minimum wage, local market surveys |

**No local economic data at all?** Use value transfer from the ESVD database (esvd.info): published USD/ha/yr values from similar ecosystems, adjusted for income differences. This is a Tier 1 monetary estimate.

## Service 1: Fish provisioning -- resource rent

```
Resource rent = Gross revenue - Total costs
Gross revenue = Sum of (catch_species x market_price_species)
Total costs = Labour + Fuel + Gear maintenance + Capital depreciation
```

| Step | Formula | Your values |
|------|---------|------------|
| 1. Gross revenue | Catch (kg) x Price (USD/kg) | USD ___ |
| 2. Labour costs | Crew payments per year | USD ___ |
| 3. Fuel costs | Annual fuel expenditure | USD ___ |
| 4. Gear and maintenance | Annual equipment costs | USD ___ |
| 5. Capital depreciation | Vessel value / lifespan | USD ___ |
| 6. Total costs | Sum of steps 2-5 | USD ___ |
| 7. Resource rent | Step 1 minus Step 6 (min 0) | USD ___ |

If resource rent is negative, report zero. The ecosystem provides fish but the fishery is economically unprofitable.

## Service 2: Carbon sequestration -- SCC

```
Monetary value = Physical supply (Mg CO2/yr) x Carbon price (USD/Mg CO2)
```

| Carbon price option | Value (USD/Mg CO2) | Source | When to use |
|-------------------|---:|--------|------------|
| US EPA Social Cost of Carbon | 51 | US Interagency Working Group (2021) | NDC reporting, government policy analysis |
| UK BEIS carbon values | 85-300 (GBP, varies by year) | UK Green Book | UK-aligned policy |
| EU ETS price | 80-100 (EUR) | EU Emissions Trading System | EU-aligned compliance |
| Voluntary carbon market (mangrove) | 10-35 | ecosystemmarketplace.com | Carbon credit project feasibility |
| Voluntary carbon market (seagrass) | 5-20 | ecosystemmarketplace.com | Emerging market |
| Verra VCS blue carbon credits | 15-30 | verra.org | Project-level blue carbon finance |
| IDXCarbon (Indonesia) | Market price | Jakarta carbon exchange | Indonesia-specific |

Choose the price that matches your policy purpose: SCC for global damage estimates and NDC reporting, market price for revenue potential and project feasibility.

## Service 3: Coastal protection -- replacement cost

```
Total replacement = Length of protected coastline (m) x Cost per m of seawall (USD/m)
Annualized value = Total replacement / Infrastructure lifespan (years)
```

Typical seawall costs: USD 2,000 to 15,000 per metre depending on design and location.

## Service 4: Recreation -- direct expenditure

```
Value = Ecosystem visitors/yr x Average ecosystem-attributable spending per visitor
```

Spending includes: activity fees, equipment rental, allocated share of accommodation (based on visitor motivation surveys).

## Service 5: Gleaning -- equivalent wage

```
Value = (Hours/yr x Local hourly wage) + (Harvest kg/yr x Market price/kg)
```

---

## Part B Summary: Monetary Supply Table

| Service | Method | Value type | Coral reefs | Seagrass | Mangroves | Total |
|---------|--------|-----------|---:|---:|---:|---:|
| Fish provisioning | Resource rent | Market | | | | |
| Carbon sequestration | SCC | Non-market | | | | |
| Coastal protection | Replacement cost | Non-market | | | | |
| Nursery habitat | Market price | Market (indirect) | | | | |
| Recreation | Direct expenditure | Market | | | | |
| Gleaning | Equivalent wage | Mixed | | | | |
| **Total** | | | | | | |

---

## Part B continued: Monetary Use Table

The monetary use table assigns the economic value of each service to the sector that benefits, using the same beneficiary mapping as the physical use table.

**Monetary Use Table (USD/yr):**

| Service | Method | Fisheries | Tourism | Coastal households | Government | Global community | Total |
|---------|--------|---:|---:|---:|---:|---:|---:|
| Fish provisioning | Resource rent | | | | | | |
| Carbon sequestration | SCC | | | | | | |
| Coastal protection | Replacement cost | | | | | | |
| Nursery habitat | Market price | | | | | | |
| Recreation | Direct expenditure | | | | | | |
| Gleaning | Equivalent wage | | | | | | |
| **Total** | | | | | | | |

**Policy use:** The monetary use table reveals which sectors of the economy depend most on ecosystem services. This information supports cost-benefit analysis for conservation investments, identifies who bears costs when ecosystems degrade, and highlights sectors that should contribute to ecosystem management.

---

## Combining Part A and Part B

If you complete both parts, your full service account has:
1. Physical supply table (Part A) -- what the ecosystem provides
2. Monetary supply table (Part B) -- what it is worth economically
3. Supply and use tables showing which economic sectors or population groups use each service

You can report Part A alone, Part A + Part B for some services, or the full set. Each is a valid level of completeness.

---

## The Integrated Supply-Use Table (SEEA EA Table 7.1)

The SEEA EA presents supply and use together in a single integrated table. This is the final output of a complete ecosystem services account.

**Structure:**

The table has SUPPLY on top and USE on the bottom, sharing the same columns:
- Left columns: Economic units (industries by sector, households, government, exports/global)
- Right columns: Ecosystem types (by IUCN GET code)
- Far right: TOTAL

**SUPPLY half:** Ecosystem columns are filled (ecosystems supply services). Economic unit columns are empty.

**USE half:** Economic unit columns are filled (economic units use services). Ecosystem columns are empty (except for intermediate services between ecosystems).

**Accounting identity:** For each service row, Total supply must equal Total use. This is the fundamental check that the account is balanced.

**How to build it:**

1. Start with your completed supply tables (Part A physical + Part B monetary)
2. Add your completed use tables
3. Stack them in one table with a SUPPLY header and USE header
4. Verify that totals match for each service row
5. If totals do not match, identify the discrepancy and resolve

**Why it matters:**

The integrated SUT is the table format used in the SEEA EA standard (Table 7.1a for physical, Table 7.1b for monetary). It shows the complete picture in one place: where services come from (ecosystem assets) and who benefits (economic units). This is the table a national statistician would compile.

See the Excel template "SUT (Supply-Use Table)" sheet for the blank template, and the example workbook "Services - SUT" sheet for a filled example.
