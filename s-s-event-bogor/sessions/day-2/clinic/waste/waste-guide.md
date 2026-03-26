# Ocean Waste and Emissions Accounts -- Step-by-Step Guide

This guide covers 3 sub-accounts for tracking residual flows from the economy to the marine environment, following SEEA-CF Chapter 3.6 methodology.

---

## Sub-account 1: Water Emissions to Sea

### Pathway A: National statistics (Tier 1)

Estimated time: 30-45 minutes

#### Step 1: Get national wastewater discharge data

Contact the environment ministry or water authority. You need:
- Total volume of wastewater discharged (m3/yr)
- Substance loads: nitrogen (N), phosphorus (P), BOD, heavy metals
- Breakdown by source: industry (by sector), households, agriculture

#### Step 2: Identify coastal point sources

From the discharge permit register or monitoring records:
- List industrial facilities along the coast that discharge to rivers, estuaries, or sea
- List sewerage treatment plants serving coastal municipalities
- Identify major river systems that carry inland pollution to the coast

#### Step 3: Estimate the coastal share of total discharges

If facility-level data are not available, estimate the coastal share using:
- Share of industrial output located in coastal municipalities
- Share of population served by coastal sewerage systems
- Share of agricultural land in coastal catchments

#### Step 4: Record by substance

For each source sector, record annual discharge loads:

| Substance | Industry (tonnes/yr) | Households (tonnes/yr) | Agriculture (tonnes/yr) | Total (tonnes/yr) |
|-----------|---:|---:|---:|---:|
| Nitrogen (N) | | | | |
| Phosphorus (P) | | | | |
| BOD | | | | |
| Heavy metals | | | | |
| Other chemicals | | | | |

#### Step 5: Record by destination

| Destination | Volume (m3/yr) | Treatment level |
|-------------|---:|----------------|
| Sewerage -- primary treatment | | Solids removal only |
| Sewerage -- secondary treatment | | Biological treatment |
| Sewerage -- tertiary treatment | | Nutrient removal |
| Direct discharge to rivers | | None |
| Direct discharge to sea | | None |
| Septic/on-site systems | | Partial |

### Pathway B: Environmental monitoring data (Tier 2)

#### Step 1: Get water quality monitoring data

Obtain data from coastal monitoring stations operated by the environment ministry or EPA equivalent:
- Sampling locations (river mouths, coastal outfalls, nearshore stations)
- Pollutant concentrations (mg/L) for N, P, BOD, heavy metals
- Flow rates (m3/day or m3/yr) at monitoring points

#### Step 2: Calculate pollutant loads

For each monitoring point:
- Load (tonnes/yr) = concentration (mg/L) x flow rate (m3/yr) x 0.001 (conversion factor)

#### Step 3: Attribute to source sectors

Use upstream land use, discharge permits, or pollutant fingerprinting to attribute loads to:
- Industrial sectors
- Households / sewerage
- Agriculture

### Where to get the data: Water emissions

| Data source | What it provides | URL / contact |
|-------------|-----------------|---------------|
| National environment ministry | Wastewater discharge permits, monitoring data | Country-specific |
| Water utilities | Sewerage treatment volumes and effluent quality | Country-specific |
| GEMS/Water (UN) | Global water quality database | gemstat.org |
| WHO/UNICEF JMP | Sanitation and wastewater treatment coverage | washdata.org |
| FAO AQUASTAT | Water resources and use, wastewater data | fao.org/aquastat |
| National water quality monitoring programs | Coastal station data | Country-specific |

---

## Sub-account 2: Solid Waste Entering the Sea

### Pathway A: Waste statistics (Tier 1)

Estimated time: 30-45 minutes

#### Step 1: Get national solid waste generation data

From the waste management agency or statistics office:
- Total municipal solid waste generated (tonnes/yr)
- Composition by type: plastics, organics, metals, glass, other

#### Step 2: Estimate mismanaged waste fraction

Mismanaged waste is waste not properly collected, contained, or disposed of. It includes:
- Uncollected waste (not reached by waste collection services)
- Waste disposed in open dumps or uncontrolled landfills

Data source: national waste surveys, or use Jambeck et al. (2015) country estimates as a starting point.

#### Step 3: Apply coastal proximity factor

Marine debris from land-based sources originates primarily within 50 km of the coast.
- Determine the share of national population living within 50 km of the coast
- Apply this share to national mismanaged waste to estimate coastal mismanaged waste

#### Step 4: Estimate marine leakage rate

Not all mismanaged coastal waste reaches the sea. Estimate the fraction that enters the marine environment through:
- Wind transport to waterways
- River transport
- Direct dumping on beaches or in coastal waters
- Stormwater runoff

Typical estimates range from 10% to 25% of coastal mismanaged waste, depending on terrain, rainfall, and proximity to waterways.

#### Step 5: Compile the account

| Waste type | National generation (t/yr) | Mismanaged (t/yr) | Coastal share (t/yr) | Marine leakage (t/yr) |
|------------|---:|---:|---:|---:|
| Plastics | | | | |
| Organic waste | | | | |
| Metals | | | | |
| Glass | | | | |
| Other | | | | |
| **Total** | | | | |

### Pathway B: Direct measurement (Tier 2)

#### Step 1: Beach litter surveys

Use standardized survey protocols:
- OSPAR beach litter monitoring protocol (100 m transects, item counts by category)
- ICC (International Coastal Cleanup) methodology
- National litter survey protocols

Convert item counts to weight estimates using standard item weights.

#### Step 2: Port waste reception facility records

Under IMO MARPOL Annex V, ports must provide waste reception facilities. Collect:
- Volume and type of waste received from ships (garbage, oily waste, sewage)
- Number of ships using waste reception facilities

#### Step 3: Fishing vessel waste records

From fisheries agencies or port authorities:
- Lost or abandoned fishing gear (nets, traps, lines) -- reported or estimated
- Onboard waste disposal practices

#### Step 4: River-to-sea transport estimates

If available, use river monitoring data:
- Floating debris counts at river mouths
- Sediment trap data for microplastics
- Modelled riverine plastic transport (e.g., Lebreton et al. 2017 estimates)

### Where to get the data: Solid waste

| Data source | What it provides | URL / contact |
|-------------|-----------------|---------------|
| Municipal waste agencies | Generation, collection, and disposal data | Country-specific |
| Jambeck et al. (2015) | Country-level estimates of mismanaged waste and marine debris | science.sciencemag.org |
| Ocean Conservancy ICC | Beach cleanup data by country and item type | oceanconservancy.org |
| OSPAR Commission | Beach litter monitoring data (NE Atlantic) | ospar.org |
| UNEP Global Partnership on Marine Litter | Reports, data, and methodology guidance | unep.org/explore-topics/oceans-seas/what-we-do/addressing-land-based-pollution/global-partnership-marine |
| National litter surveys | Country-specific beach and waterway surveys | Country-specific |
| Port authorities | Ship waste reception records (MARPOL Annex V) | Country-specific |

---

## Sub-account 3: Air Emissions from Ocean Industries

### Step 1: Get emission data from ocean economy sectors

Use the ocean economy sectors identified in your OESA. Key sectors:
- Maritime shipping (domestic and international)
- Fishing fleet
- Offshore oil and gas
- Port operations
- Marine construction

#### Step 2: Apply emission factors

| Sector | Data needed | Emission factor source |
|--------|-----------|----------------------|
| Maritime shipping | Fuel consumption (tonnes/yr) by fuel type | IMO Fourth GHG Study (2020) |
| Fishing fleet | Fuel consumption (tonnes/yr) | National fisheries agency, IMO |
| Offshore oil and gas | Fuel use, flaring, venting volumes | National GHG inventory, operator reports |
| Port operations | Electricity use, cargo handling equipment fuel | Port emission inventories |

Standard emission factors for marine fuels:
- Heavy fuel oil (HFO): 3.114 tonnes CO2 per tonne fuel
- Marine diesel oil (MDO): 3.206 tonnes CO2 per tonne fuel
- Marine gas oil (MGO): 3.206 tonnes CO2 per tonne fuel

#### Step 3: Compile the account

| Ocean sector | CO2 (t/yr) | CH4 (t/yr) | N2O (t/yr) | SO2 (t/yr) | NOx (t/yr) | CO2e (t/yr) |
|-------------|---:|---:|---:|---:|---:|---:|
| Maritime shipping | | | | | | |
| Fishing fleet | | | | | | |
| Offshore energy | | | | | | |
| Port operations | | | | | | |
| Other ocean sectors | | | | | | |
| **Total** | | | | | | |

### Where to get the data: Air emissions

| Data source | What it provides | URL / contact |
|-------------|-----------------|---------------|
| IMO Fourth GHG Study (2020) | Shipping emission factors and global estimates | imo.org |
| National GHG inventory (UNFCCC) | Emissions by sector, including transport and energy | unfccc.int |
| Port emission inventories | Emissions from port operations and vessel movements | Country-specific / port authority |
| Fisheries agencies | Fleet size, vessel types, fuel consumption | Country-specific |
| Offshore operators | Fuel use, flaring, venting data | Country-specific / petroleum authority |

---

## Reference: SEEA-CF Account Table Formats

### Water emissions: Supply table (generation by industry)

**Table: Water Emissions Account -- Supply of Residuals, [Country], [Year]**

| Substance | Agriculture | Manufacturing | Sewerage services | Other industry | Households | Total |
|-----------|---:|---:|---:|---:|---:|---:|
| Nitrogen (tonnes) | | | | | | |
| Phosphorus (tonnes) | | | | | | |
| BOD (tonnes) | | | | | | |
| Heavy metals (tonnes) | | | | | | |

### Water emissions: Use table (destination of residuals)

| Substance | To sewerage (treatment) | Direct to inland waters | Direct to sea | To soil/groundwater | Total |
|-----------|---:|---:|---:|---:|---:|
| Nitrogen (tonnes) | | | | | |
| Phosphorus (tonnes) | | | | | |
| BOD (tonnes) | | | | | |
| Heavy metals (tonnes) | | | | | |

### Solid waste: Generation by source and type

**Table: Solid Waste to Marine Environment, [Country], [Year]**

| Waste type | Coastal municipalities | Shipping | Fishing | Other sea-based | Total |
|------------|---:|---:|---:|---:|---:|
| Plastics (tonnes) | | | | | |
| Fishing gear (tonnes) | | | | | |
| Organic waste (tonnes) | | | | | |
| Other (tonnes) | | | | | |
| **Total** | | | | | |

### Air emissions: Emissions by ocean sector and substance

**Table: Air Emissions from Ocean Industries, [Country], [Year]**

| Substance | Shipping | Fishing | Offshore energy | Ports | Other | Total |
|-----------|---:|---:|---:|---:|---:|---:|
| CO2 (tonnes) | | | | | | |
| CH4 (tonnes) | | | | | | |
| N2O (tonnes) | | | | | | |
| SO2 (tonnes) | | | | | | |
| NOx (tonnes) | | | | | | |
