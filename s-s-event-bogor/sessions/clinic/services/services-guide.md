# Ecosystem Services Accounts -- Step-by-Step Guide

## Structure

This guide is split into two independent parts:

- **Part A: Physical quantification** -- measure the service in physical units (kg, Mg CO2, visitors, metres). This is a complete account on its own.
- **Part B: Monetary valuation** -- assign economic values (USD/yr). Requires Part A first. Optional for a first account.

Each part has two pathways: Pathway 1 (no primary data) and Pathway 2 (local data available).

---

# PART A: PHYSICAL QUANTIFICATION

## Service 1: Carbon sequestration

### Pathway 1: Literature rates (no field carbon data)

| Step | What to do | Your values |
|------|-----------|------------|
| 1 | Get ecosystem extent (ha) from your extent account | Mangrove: ___ ha, Seagrass: ___ ha |
| 2 | Look up net carbon production rates from literature | Mangrove: ~3.7 Mg CO2/ha/yr, Seagrass: ~1.3 Mg CO2/ha/yr |
| 3 | Physical supply = Extent x NCP rate | ___ Mg CO2/yr |

Literature sources for NCP rates:
- Mangroves: Alongi (2014), range 2.0 to 6.0 Mg CO2/ha/yr depending on species and region
- Seagrass: Fourqurean et al. (2012), range 0.4 to 2.0 Mg CO2/ha/yr
- Use regionally appropriate values where available

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

### Pathway 1: National statistics

| Step | What to do | Your values |
|------|-----------|------------|
| 1 | Get total annual catch from fisheries agency records | ___ kg/yr |
| 2 | Disaggregate by species or species group | |
| 3 | Assign catch to ecosystem type using species-habitat associations | Reef: ___ kg, Seagrass: ___ kg, Pelagic: ___ kg |

### Pathway 2: Fisher survey data

| Step | What to do |
|------|-----------|
| 1 | Compile catch by species from landing surveys |
| 2 | Record gear type and effort (trips, hours) |
| 3 | Disaggregate by ecosystem using species-habitat literature |
| 4 | Calculate CPUE (catch per unit effort) if effort data available |

**Physical output:** Total kg/yr by ecosystem type and species group

---

## Service 3: Coastal protection

### Pathway 1: Spatial overlay

| Step | What to do | Your values |
|------|-----------|------------|
| 1 | Map ecosystem extent along coastline (coral reef, mangrove) | ___ m reef, ___ m mangrove |
| 2 | Identify assets behind ecosystem buffer (buildings, infrastructure, population) | |
| 3 | Record: length of coastline protected (m), number of buildings, population behind buffer | |

### Pathway 2: Wave attenuation modelling

If you have bathymetry and wave data, apply a wave attenuation model to quantify the reduction in wave energy provided by the reef or mangrove.

**Physical output:** Metres of coastline protected, buildings/people behind ecosystem buffer

---

## Service 4: Recreation and tourism

### Pathway 1: Tourism statistics

| Step | What to do | Your values |
|------|-----------|------------|
| 1 | Get total visitor numbers from tourism authority or accommodation records | ___/yr |
| 2 | Estimate reef/ecosystem-attributable visitors (from surveys or activity records) | ___/yr |
| 3 | Record: dive trips, snorkel trips, kayak trips, gleaning hours | |

### Pathway 2: Operator records

| Step | What to do |
|------|-----------|
| 1 | Compile activity records from dive centres, tour operators, park entry |
| 2 | Count participants per activity type |
| 3 | Record effort (trips/yr, hours/yr) |

**Physical output:** Visitor trips/yr or hours/yr by ecosystem type and activity

---

## Service 5: Nursery habitat

| Step | What to do | Your values |
|------|-----------|------------|
| 1 | Get fish density data for nursery areas (mangrove, seagrass) and non-nursery areas (open reef) | |
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

# PART B: MONETARY VALUATION (builds on Part A)

**Only proceed to Part B if you have the economic data needed.** Part A alone is useful for policy.

## Valuation method selection

| Service | Physical quantity needed (from Part A) | Valuation method | Economic data needed |
|---------|---------------------------------------|-----------------|---------------------|
| Fish provisioning | kg/yr by species | Resource rent | Market prices, fishing costs (labour, fuel, gear, capital) |
| Carbon sequestration | Mg CO2/yr | Social cost of carbon (SCC) or carbon market price | SCC value (e.g., USD 51/Mg CO2) or local carbon exchange price |
| Coastal protection | m coastline, assets behind | Replacement cost | Engineering cost per m of seawall or breakwater |
| Nursery habitat | kg biomass/yr | Market price of fish | Same market prices as fish provisioning |
| Recreation | visitors/yr | Direct expenditure | Per-visitor spending data (activity fees, accommodation allocation) |
| Gleaning | hours/yr, harvest kg/yr | Equivalent wage + market value | Local wage rate, market prices for harvested species |

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

| Carbon price option | Value | Source |
|-------------------|-------|--------|
| US EPA Social Cost of Carbon | USD 51/Mg CO2 (2020 USD) | US government central estimate |
| UK BEIS carbon values | GBP 70-250/tCO2 (varies by year) | UK Green Book |
| Voluntary carbon market | USD 5-50/Mg CO2 (varies) | Market transactions |
| IDXCarbon (Indonesia) | Market price | Jakarta carbon exchange |

Choose the price that matches your policy purpose: SCC for global damage estimates, market price for revenue potential.

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

## Combining Part A and Part B

If you complete both parts, your full service account has:
1. Physical supply table (Part A) -- what the ecosystem provides
2. Monetary supply table (Part B) -- what it is worth economically
3. Supply and use tables showing which economic sectors or population groups use each service

You can report Part A alone, Part A + Part B for some services, or the full set. Each is a valid level of completeness.
