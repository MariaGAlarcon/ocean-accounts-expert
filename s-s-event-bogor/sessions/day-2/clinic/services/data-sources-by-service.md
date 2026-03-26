# Data Sources for Ecosystem Service Calculations

Where to find the data you need for each service, organized by Part A (physical supply and use) and Part B (monetary supply and use).

## Use tables: data for identifying beneficiaries

The SEEA EA requires both supply tables (which ecosystems provide services) and use tables (which economic sectors benefit). To build use tables, you need data on who uses each service:

| Beneficiary sector | Data needed | Where to find it |
|-------------------|------------|-----------------|
| Fisheries sector | Who catches the fish? Commercial vs artisanal? | Fisheries agency, fisher cooperatives, landing records |
| Tourism sector | Who operates reef/mangrove tours? Who captures visitor spending? | Tourism boards, dive operator records, MPA visitor data |
| Coastal households | Who gleans? Who depends on coastal protection? | Household surveys, census data for coastal communities |
| Government | What public infrastructure is protected by ecosystems? | Municipal records, public asset databases, infrastructure maps |
| Global community | Carbon sequestration benefits everyone globally | No allocation data needed (assign 100% to global community) |

For services shared across sectors (e.g., coastal protection benefits both households and government), use spatial data (building ownership maps, cadastral records) to split the allocation.

---

## 1. Fish Provisioning

### Part A: Physical supply (kg/yr)

| Data needed | Where to get it | Examples |
|-------------|----------------|---------|
| Total annual catch | National fisheries agency landing records | FAO country profiles (fao.org/fishery/en/countryprofiles), national fisheries departments |
| Catch by species | Landing site monitoring, logbook programs | National fisheries surveys, fisher cooperatives |
| Species-habitat associations | Scientific literature | FishBase (fishbase.org) for species-habitat lookup; Froese & Pauly (2023) |
| Spatial effort data | VMS (vessel monitoring systems), AIS | Global Fishing Watch (globalfishingwatch.org) for effort maps |
| Fisher surveys (if no agency data) | Design and conduct locally | GOAP provides survey templates; FAO small-scale fisheries guidelines |

**Tier 1 shortcut (no local data):** Use FAO FAOSTAT or Sea Around Us (seaaroundus.org) for country-level catch estimates. Allocate to ecosystems using FishBase habitat associations.

### Part B: Monetary value (resource rent)

| Data needed | Where to get it | Examples |
|-------------|----------------|---------|
| Market prices per species | Local fish markets, landing site price surveys | National statistics offices, WorldFish price databases |
| Labour costs | Fisher household surveys | Average crew wages x number of crew x trips/yr |
| Fuel costs | Fisher surveys, fuel price records | Litres per trip x trips/yr x price per litre |
| Gear and maintenance | Fisher surveys | Annual gear replacement and repair costs |
| Vessel depreciation | Purchase price / expected lifespan | Typical small vessel: USD 5,000-20,000 / 15-20 years |

---

## 2. Carbon Sequestration

### Part A: Physical supply (Mg CO2/yr)

| Data needed | Where to get it | Examples |
|-------------|----------------|---------|
| Ecosystem extent (ha) | Your extent account, or global datasets | Global Mangrove Watch (globalmangrovewatch.org), Allen Coral Atlas (allencoralatlas.org) |
| Net carbon production rate (NCP) | Published literature | See NCP table below |
| Primary carbon stock data (Tier 2-3) | Field measurements: soil cores, allometric equations | National forest inventories, blue carbon project reports |

**NCP rates from literature (Mg CO2/ha/yr):**

| Ecosystem | Conservative estimate | Central estimate | High estimate | Key sources |
|-----------|---:|---:|---:|-------------|
| Mangroves | 2.0 | 3.7 | 17.2 | Alongi (2014), Kauffman & Donato (2012), IPCC Wetlands Supplement |
| Seagrass | 0.4 | 1.3 | 4.4 | Fourqurean et al. (2012), Duarte et al. (2005) |
| Salt marshes | 1.5 | 2.1 | 6.0 | Chmura et al. (2003), IPCC Wetlands Supplement |

**Note:** The wide range reflects differences in species composition, latitude, age, and measurement methodology. Use regionally calibrated values where available. The conservative estimate is appropriate for Tier 1 accounts.

**Global data portals:**
- Global Mangrove Watch: extent + canopy height + biomass estimates
- IPCC Wetlands Supplement (2013): emission factors and default NCP rates by climate zone
- Blue Carbon Initiative (thebluecarboninitiative.org): methods and country resources

### Part B: Monetary value (SCC or market price)

| Carbon price | Value (USD/Mg CO2) | Source | When to use |
|-------------|---:|---------|------------|
| US EPA Social Cost of Carbon | 51 | US Interagency Working Group (2021) | Government policy analysis, NDC reporting |
| UK BEIS carbon values | 70-250 (GBP) | UK Green Book, varies by year | UK-aligned policy contexts |
| EU ETS price | ~80-100 (EUR) | EU Emissions Trading System | EU policy contexts |
| Voluntary carbon market (mangrove) | 10-35 | Ecosystem Marketplace (ecosystemmarketplace.com) | Carbon credit project feasibility |
| Voluntary carbon market (seagrass) | 5-20 | Ecosystem Marketplace | Emerging market, fewer projects |
| IDXCarbon (Indonesia) | Market price | Jakarta carbon exchange | Indonesia-specific |
| Verra VCS blue carbon credits | 15-30 | Verra registry (verra.org) | Project-level blue carbon finance |

---

## 3. Coastal Protection

### Part A: Physical supply (m coastline, buildings protected)

| Data needed | Where to get it | Examples |
|-------------|----------------|---------|
| Ecosystem extent along coastline | Your extent account, GIS overlay | Map coral reef or mangrove extent within 500 m of shore |
| Coastline length protected | GIS calculation | Length of shoreline with reef/mangrove between it and open ocean |
| Buildings behind ecosystem buffer | OpenStreetMap, national building datasets | OSM (openstreetmap.org), Microsoft Building Footprints, national cadastres |
| Population behind buffer | Census data, WorldPop | WorldPop (worldpop.org) for gridded population |
| Wave exposure data (Tier 2-3) | Wave models, buoy data | NOAA WaveWatch III, Copernicus Marine Service |

**Tier 1 shortcut:** Use satellite-derived extent maps to identify coastline with reef or mangrove in front. Count buildings from OpenStreetMap within 200 m of shore behind the ecosystem.

### Part B: Monetary value (replacement cost)

| Data needed | Where to get it | Examples |
|-------------|----------------|---------|
| Seawall or breakwater cost per metre | Engineering firms, government infrastructure budgets | Typical range: USD 2,000-15,000/m depending on design |
| Infrastructure lifespan | Engineering standards | Typically 30-50 years for concrete seawalls |
| Avoided damage estimates (Tier 3) | Flood risk models, insurance data | FEMA flood maps, Munich Re NatCat data |

**Published cost references:**
- Beck et al. (2018): coral reefs reduce wave energy by 97% on average
- Narayan et al. (2016): cost-effectiveness of natural vs. built infrastructure
- UNEP (2020): mangrove economic valuation guidelines

---

## 4. Nursery Habitat

### Part A: Physical supply (kg biomass/yr)

| Data needed | Where to get it | Examples |
|-------------|----------------|---------|
| Fish density in nursery areas | Field surveys (UVC, seine nets) | National monitoring programs, university research |
| Fish density in non-nursery areas | Same surveys, control sites | Open reef or unvegetated areas |
| Log Response Ratio (LRR) | Literature meta-analyses | Coral reef LRR: 31%, Seagrass LRR: 13% (scientific meta-analyses) |
| Total fish biomass | From your fish provisioning account (Part A) | |
| Juvenile survival rate | Literature | Standard ecological assumption: 5% survive to harvestable size |

### Part B: Monetary value

Use the same market prices as fish provisioning. The nursery value = additional harvestable biomass x market price.

---

## 5. Sediment Retention / Beach Nourishment

### Part A: Physical supply (m3 CaCO3/yr)

| Data needed | Where to get it | Examples |
|-------------|----------------|---------|
| Carbonate production rates | Literature | Perry et al. (2012): coral reef CaCO3 production rates by reef type and region |
| Reef area or length | Extent account | |
| Beach erosion rates (context) | National coastal monitoring | Coastal erosion surveys, satellite shoreline change analysis |

### Part B: Monetary value (replacement cost)

| Data needed | Where to get it | Examples |
|-------------|----------------|---------|
| Beach nourishment cost per m3 | Engineering firms, coastal management agencies | Range: USD 5-20/m3 depending on sand source distance |
| Dredging and transport costs | Port authorities, marine contractors | Often the largest cost component |

---

## 6. Recreation and Tourism

### Part A: Physical supply (visitors/yr, trips/yr)

| Data needed | Where to get it | Examples |
|-------------|----------------|---------|
| Total visitor arrivals | National tourism authority, airport/port statistics | UNWTO Tourism Dashboard (unwto.org), national tourism boards |
| Accommodation statistics | Hotel/resort occupancy records | National statistics offices, booking platforms |
| Dive and snorkel activity | Dive centres, tour operators, MPA entry records | PADI statistics, local dive operator associations |
| Mangrove/kayak tours | Tour operators | Trip counts, group sizes, seasonal patterns |
| MPA visitor counts | Park management authorities | Entry permits, ranger counts |

**Tier 1 shortcut:** Use UNWTO country data for total arrivals. Estimate reef-visitor share from tourism surveys or literature (e.g., 30-60% of visitors to tropical coastal destinations engage in reef-based activities).

### Part B: Monetary value (direct expenditure)

| Data needed | Where to get it | Examples |
|-------------|----------------|---------|
| Activity fees (dive, snorkel, kayak) | Operator records or online pricing | Direct price per activity |
| Equipment rental | Operator records | Mask, fins, tank rental per trip |
| Reef-attributable accommodation spending | Tourist expenditure surveys | Ask: "what share of your trip motivation is the reef?" |
| Tour operator revenue | Business records, tax filings | Gross revenue from reef/mangrove activities |
| MPA entry fees | Park management | Fee x number of paying visitors |

---

## 7. Gleaning and Subsistence

### Part A: Physical supply (hours/yr, kg/yr)

| Data needed | Where to get it | Examples |
|-------------|----------------|---------|
| Number of gleaners | Household surveys, community census | Village records, community-based monitoring |
| Effort (hours per trip, trips per week) | Gleaner interviews, time diaries | Participatory monitoring |
| Harvest by species | Gleaner interviews, landing measurements | Octopus, sea cucumber, shellfish, seaweed (kg/trip) |
| Seasonal patterns | Monthly monitoring | Harvest varies by tide, weather, species availability |

### Part B: Monetary value (equivalent wage + market)

| Data needed | Where to get it | Examples |
|-------------|----------------|---------|
| Local hourly wage rate | National statistics, minimum wage records | Equivalent agricultural or fisheries wage |
| Market prices for gleaned species | Local market surveys | Price per kg for each harvested species |

---

## Quick Reference: Global Open Datasets

These are freely available and can get you started on any service:

| Dataset | URL | What it provides |
|---------|-----|-----------------|
| Allen Coral Atlas | allencoralatlas.org | Coral reef and seagrass extent, benthic cover |
| Global Mangrove Watch | globalmangrovewatch.org | Mangrove extent 1996-2020, canopy height, biomass |
| Global Fishing Watch | globalfishingwatch.org | Fishing effort, vessel tracking |
| Sea Around Us | seaaroundus.org | Reconstructed catch by country, EEZ, species |
| FAO FishStatJ | fao.org/fishery/statistics | National fisheries production and trade |
| UNWTO | unwto.org | International tourism arrivals and receipts |
| WorldPop | worldpop.org | Gridded population estimates |
| OpenStreetMap | openstreetmap.org | Building footprints, infrastructure |
| NOAA Coral Reef Watch | coralreefwatch.noaa.gov | SST, DHW, bleaching alerts |
| NASA Ocean Color | oceancolor.gsfc.nasa.gov | Chlorophyll-a, water quality |
| ESVD | esvd.info | Published ecosystem service valuations for value transfer |
| Ecosystem Marketplace | ecosystemmarketplace.com | Carbon credit prices and market trends |
| IPCC Wetlands Supplement | ipcc.ch | Default emission factors and NCP rates |
| Verra | verra.org | Blue carbon project registry and methodologies |

---

## Validating the Supply-Use Table

When you build the integrated SUT, check these balances:

| Check | What to verify | If it fails |
|-------|---------------|-------------|
| Row balance | Total supply = Total use for each service | Recheck allocation to beneficiary sectors |
| Column balance | Sum of ecosystem supply = total physical supply | Recheck ecosystem-level disaggregation |
| Completeness | Every service has at least one ecosystem supplier and one economic user | Identify missing allocations |
| Consistency with extent | Ecosystem types in SUT match those in extent account | Align ecosystem classifications |
| Consistency with condition | Services from degraded ecosystems should reflect reduced supply | Cross-check with condition CI |

The integrated SUT is the standard SEEA EA output format (Table 7.1). Once balanced, it can be submitted to the national statistical office alongside extent and condition accounts.
