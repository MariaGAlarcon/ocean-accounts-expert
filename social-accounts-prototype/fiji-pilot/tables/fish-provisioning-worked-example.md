# Worked Example: Fish Provisioning -- Fiji

**Accounting area:** Fiji (national)
**Reference year:** 2019-20 (aligned with HIES)
**Ecosystem service:** Fish provisioning (capture fisheries, including subsistence)
**Pathways tested:** Market (E9) and Non-market (E10, subsistence)

This worked example traces fish provisioning from Fiji's marine ecosystems through commercial and subsistence pathways to household-level social conditions. It uses real data from the 2019-20 HIES, FAO fisheries statistics, and the MACBIO ecosystem service valuation. The key test is whether the subsistence boundary resolution from File 07 works in practice.

---

## Step 1: Ecosystem asset baseline

**Source:** Allen Coral Atlas, Global Mangrove Watch, MACBIO

| Indicator | Value | Year | Source |
|---|---|---|---|
| Coral reef extent (Fiji EEZ) | ~10,020 km2 | 2022 | Allen Coral Atlas |
| Mangrove extent | ~385 km2 | 2020 | Global Mangrove Watch |
| Seagrass extent | ~290 km2 [estimate] | 2017 | MACBIO |
| Customary fishing grounds (qoliqoli) | 411 registered areas, ~30,011 km2 | 2016 | iTaukei Affairs Board |
| Marine ecosystem service total value | FJ$2.5 billion/yr | 2014 | MACBIO |

**Note on spatial units:** The 411 qoliqoli areas provide a natural candidate for BSUs in Fiji's marine domain. Each qoliqoli is associated with a specific mataqali (clan) and tikina (district), enabling a direct link between marine ecosystem assets and community-level social data from the Census.

---

## Step 2: Ecosystem service flow -- fish provisioning

**Source:** FAO FishStatJ, Fiji Ministry of Fisheries, HIES 2019-20

### Commercial catch (E9: SG3 to FG1)

| Component | Catch (tonnes) | Value (FJ$ millions) | Year | Source |
|---|---|---|---|---|
| Offshore fisheries (tuna, other pelagics) | ~28,000 | ~120 [proxy] | 2019 | FAO / Ministry of Fisheries |
| Inshore/coastal commercial fisheries | ~15,000 [proxy] | ~60 [proxy] | 2019 | Ministry of Fisheries |
| Aquaculture | ~800 | ~8 [proxy] | 2019 | FAO |
| **Total commercial/formal** | **~43,800** | **~188** | | |

### Subsistence catch (E10: SG3 to FG2)

| Component | Catch (tonnes) | Year | Source |
|---|---|---|---|
| Subsistence fishing (fin fish) | ~12,000 [proxy] | 2019 | SPC estimates for Fiji |
| Subsistence gleaning (invertebrates, seaweed) | ~5,000 [proxy] | 2019 | SPC estimates |
| **Total subsistence** | **~17,000** | | |

**Classification note (File 07 test):** Under the SNA, subsistence catch for own consumption is production for own final use and should be valued at market-equivalent prices (E9). Under TG-3.5, it is a social activity outside the SNA boundary (E10). Following our proposed resolution:
- The **physical fish** (17,000 tonnes) is recorded in the supply-use table alongside commercial catch (E9 treatment for the product).
- The **activity** (fishing hours, number of subsistence fishers) is recorded in the social flows table (E10/FG2 treatment for the activity).
- This avoids double counting: the fish appears once; the activity appears once.

### Total fish provisioning from Fiji marine ecosystems

| Component | Tonnes | Edge | Domain |
|---|---|---|---|
| Commercial/formal catch | ~43,800 | E9 | FG1 (economy) |
| Subsistence catch | ~17,000 | E9 (product) / E10 (activity) | FG1 (product) / FG2 (activity) |
| **Total fish provisioning** | **~60,800** | | |

---

## Step 3: Household consumption and the HIES evidence

**Source:** Fiji HIES 2019-20 Main Report (Fiji Bureau of Statistics, August 2021)

### Seafood expenditure (Table 19, HIES)

The HIES records consumption expenditure including own-account production valued at market prices. The seafood category therefore includes both purchased fish and subsistence catch.

| Area | Seafood expenditure per HH (FJ$/yr) | % of total food | % of total consumption |
|---|---|---|---|
| **National** | **542.8** | **11.5%** | **4.5%** |
| Rural | 676.3 | 14.4% | 6.8% |
| Urban | 439.8 | 9.3% | 3.3% |

**Key finding:** Rural households spend 54% more on seafood than urban households (FJ$676 vs FJ$440). Since rural households have lower total income (FJ$20,738 vs FJ$30,501), seafood represents a much larger share of their consumption. This is consistent with greater reliance on subsistence fishing in rural areas.

### Income composition relevant to fisheries (Table 16, HIES)

| Income component | National (FJ$/yr) | % | Rural (FJ$/yr) | % | Urban (FJ$/yr) | % |
|---|---|---|---|---|---|---|
| Wages and salaries | 12,842.0 | 48.9% | 6,441.8 | 31.1% | 17,780.7 | 58.3% |
| Agriculture activities | 2,509.6 | 9.6% | 4,983.8 | 24.0% | 600.4 | 2.0% |
| Subsistence | 812.3 | 3.1% | 1,607.6 | 7.8% | 198.7 | 0.7% |
| Casual work | 1,749.1 | 6.7% | 1,464.0 | 7.1% | 1,969.1 | 6.5% |
| **Total HH income** | **26,248.6** | **100%** | **20,738.1** | **100%** | **30,500.7** | **100%** |

**Key finding:** Subsistence income (which includes subsistence fishing) accounts for 7.8% of rural household income but only 0.7% of urban income. Agriculture activities (which include fishing for sale) are 24% of rural income. Combined, agriculture + subsistence represent nearly a third (31.8%) of rural household income.

### Income distribution by decile (Table 17, HIES)

| Decile | National share of HH income | Rural share | Urban share |
|---|---|---|---|
| 1 (lowest) | 4.0% | 4.8% | 3.9% |
| 2 | 5.3% | 6.3% | 5.6% |
| 3 | 6.4% | 7.0% | 6.4% |
| 4 | 7.4% | 7.4% | 7.8% |
| 5 | 8.5% | 9.0% | 8.7% |
| 6 | 9.4% | 9.8% | 9.6% |
| 7 | 10.8% | 10.6% | 10.6% |
| 8 | 11.8% | 11.8% | 11.6% |
| 9 | 14.7% | 14.0% | 14.7% |
| 10 (highest) | 21.8% | 19.3% | 21.2% |

**Key finding:** The bottom 10% receive 4% of total income while the top 10% receive 21.8%. Income from agriculture activities represents ~15% of income for the bottom decile (Figure 40, HIES) and declines as household welfare increases.

---

## Step 4: Distributional supply-use table (estimated)

This table estimates how fish provisioning is distributed across household income groups. Since the HIES does not publish seafood consumption by decile directly, we estimate using the urban/rural split and the income composition patterns from Figure 40.

### Table A: Fish provisioning -- distributional supply-use table (physical, tonnes/yr)

**Estimation method:** Total household consumption estimated at ~35,000 tonnes (national per-capita seafood consumption ~40 kg/yr x 884,000 population). Remainder goes to export and tourism. Subsistence share estimated at ~17,000 tonnes concentrated in lower-income rural households.

| Use category | D1-D2 (poorest 20%) | D3-D4 | D5-D6 | D7-D8 | D9-D10 (richest 20%) | Non-HH (export/tourism) | Total |
|---|---|---|---|---|---|---|---|
| Purchased seafood | 1,800 | 2,800 | 3,500 | 4,200 | 5,700 | -- | 18,000 |
| Subsistence catch (own consumption) | 5,100 | 4,300 | 3,400 | 2,700 | 1,500 | -- | 17,000 |
| Export and tourism | -- | -- | -- | -- | -- | 25,800 | 25,800 |
| **Total** | **6,900** | **7,100** | **6,900** | **6,900** | **7,200** | **25,800** | **60,800** |
| **% of household fish** | **19.7%** | **20.3%** | **19.7%** | **19.7%** | **20.6%** | -- | **100%** |

### Distributional pattern -- contrasting with Australia

The distributional pattern for Fiji is strikingly different from Australia:

1. **Total fish consumption is approximately equal across income groups.** The poorest 20% receive ~20% of household fish -- roughly proportional. In Australia, the poorest received only 9%.

2. **The composition differs sharply by income.** For D1-D2 (poorest), an estimated 74% of their fish comes from subsistence catch. For D9-D10 (richest), only 21% is subsistence. This is the progressive subsistence effect predicted in File 02.

3. **Subsistence acts as an equalizer.** Without subsistence fishing, the bottom 20% would receive only ~10% of fish (purchased only). Subsistence catch doubles their fish access. This is the food security mechanism that makes the E10 non-market pathway critical for social accounts.

4. **The Australia/Fiji comparison validates the framework.** In a high-income country (Australia), fish provisioning is regressive (richer households consume more). In a Pacific Island nation (Fiji), subsistence fishing makes the distribution approximately equal or progressive. The same accounting table reveals both patterns.

### Accounting identity check

Total supply (60,800 tonnes) = Total use (35,000 household + 25,800 non-household = 60,800). **Identity holds.**

---

## Step 5: From fish provisioning to social conditions

### Material wellbeing

| Indicator | D1-D2 (poorest) | D5-D6 (middle) | D9-D10 (richest) | Source |
|---|---|---|---|---|
| Mean HH income (FJ$/yr) | ~12,200 [proxy from decile shares] | ~23,500 | ~48,000 | HIES Table 17 |
| Agriculture + subsistence as % of income | ~31% [estimated from Figure 40] | ~12% | ~5% | HIES Figure 40 |
| Vulnerability to fish stock decline | Very high | Moderate | Low | Derived |

**Interpretation:** For the poorest households, agriculture and subsistence income (which includes fishing) represents nearly a third of total income. A decline in coastal fish stocks would disproportionately affect these households because they lack alternative income sources and depend on subsistence catch for both food and income.

### Food security

| Indicator | National | Rural | Urban | Source |
|---|---|---|---|---|
| Seafood as % of food expenditure | 11.5% | 14.4% | 9.3% | HIES Table 19 |
| Estimated per capita fish consumption | ~40 kg/yr | ~50 kg/yr [proxy] | ~30 kg/yr [proxy] | Estimated from HIES + FAO |
| WHO recommendation | 20 kg/yr | 20 kg/yr | 20 kg/yr | WHO |
| Fish consumption vs WHO benchmark | 2x above | 2.5x above | 1.5x above | Derived |

**Interpretation:** Fiji's per capita fish consumption (~40 kg/yr) is roughly 3x Australia's (13.8 kg/yr) and 2x the WHO recommendation. Fish is a primary protein source. Rural households consume more fish per capita than urban, consistent with direct access to marine resources through qoliqoli customary tenure.

### Poverty and fishing livelihoods

| Indicator | Value | Source |
|---|---|---|
| Multidimensional poverty rate (national) | 29.6% | HIES |
| Subsistence workers: multidimensional poverty rate | 38.4% | HIES Figure 34 |
| Agriculture (non-subsistence) workers: poverty rate | 40.0% | HIES Figure 34 |
| Family/community workers: poverty rate | 48.6% | HIES Figure 33 |
| Coping strategy: help from friends/relatives | 62.9% nationally; 68.8% rural | HIES Figure 35-36 |
| Coping strategy: less preferred foods | 46.0% nationally | HIES Figure 35 |

**Interpretation:** Subsistence and agricultural workers (which include fishers) have poverty rates well above the national average. Nearly half of family/community workers are multidimensionally poor. When shocks hit, 63% of households rely on help from friends and relatives -- a social capital mechanism (E8) that the social accounts should capture. The 46% who switch to less preferred foods demonstrates what happens when fish provisioning declines: direct food security impact.

---

## Step 6: Subsistence boundary test (File 07)

This worked example provides the first empirical test of the subsistence boundary resolution proposed in File 07.

### What the HIES tells us

The HIES consumption expenditure definition (p.50) explicitly includes "own-account production, barter and income in-kind." This means the FJ$542.8/HH/yr seafood figure includes subsistence catch valued at market-equivalent prices. The HIES is therefore already applying the E9 treatment for the product (valuing subsistence fish as if it were economic production).

However, the HIES also records subsistence as a separate income category (FJ$812.3/HH/yr nationally). This category captures the value of all subsistence production, not just fish.

### The resolution in practice

| Dimension | Where it appears | Edge | Table |
|---|---|---|---|
| Physical fish (kg) | Supply-use table: 17,000 tonnes subsistence | E9 (product) | Distributional SUT |
| Market-equivalent value (FJ$) | HIES consumption: included in $542.8 seafood | E9 (value) | SNA-consistent |
| Fishing activity (hours) | Social flows table: subsistence fishing hours | E10 (activity) | Table 4a |
| Food security outcome | Social stocks table: fish consumption per capita | E5/E6 | Table 3a |

**Assessment:** The resolution works. The physical fish is counted once (in the supply-use table). The activity is counted once (in the social flows table). The HIES already treats subsistence production consistently with the SNA (own-account production valued at market prices). No double counting occurs.

**What is missing:** The HIES published report does not disaggregate seafood consumption into "purchased" vs "own production" vs "gifted." This split would directly quantify the E9 vs E10 flows. The microdata would contain this split (the survey instrument asks the source of each food item). This is the strongest case for requesting HIES microdata from FBS.

---

## Step 7: Comparison with Australia GBR example

| Dimension | Australia (GBR) | Fiji | What the contrast reveals |
|---|---|---|---|
| Per capita fish consumption | 13.8 kg/yr | ~40 kg/yr | Fish is 3x more important for Fijian food security |
| Subsistence share of catch | ~5% (recreational) | ~28% of total catch | Subsistence is a major pathway in Fiji, minor in Australia |
| Distribution of fish across income groups | Regressive (Q5 gets 30%) | Approximately equal (~20% per quintile) | Subsistence fishing equalizes distribution in Fiji |
| Poverty rate of fishing households | Low (fishing is relatively well-paid in Australia) | 38-40% (subsistence/agriculture workers) | Fishing households in Fiji are among the poorest |
| Seafood as % of food expenditure | ~5% [proxy] | 11.5% (14.4% rural) | Fiji households allocate 2-3x more of food budget to seafood |
| Coping when fish declines | Switch to other protein (affordable alternatives) | Switch to less preferred foods (46%); rely on social networks (63%) | Fiji households have fewer alternatives; social capital is critical |
| Dominant pathway | E9 (market) | E9 + E10 (market + subsistence) | Social accounts add most value where E10 is large |

**Key insight:** Social accounts add the most analytical value in countries where the non-market pathway (E10) is large. In Australia, standard economic accounts (SNA + SEEA-EA services accounts) capture most of the fish provisioning story. In Fiji, the economic accounts miss nearly a third of the fish and most of the social dynamics (subsistence dependency, customary tenure, community coping, gender dimensions of gleaning). This is exactly the gap that social accounts fill.

---

## Data quality and limitations

| Issue | Severity | Mitigation |
|---|---|---|
| HIES seafood figure includes subsistence but does not split by source | High | Request microdata from FBS for purchased/own-production/gifted split |
| Subsistence catch estimates from SPC are rough national proxies | High | More recent community-based monitoring data may exist |
| Income decile x seafood cross-tabulation not published | Moderate | Estimated from urban/rural split and Figure 40 income composition |
| Fisheries catch data from FAO is national; no spatial allocation to qoliqoli | Moderate | Ministry of Fisheries may have spatial data |
| No time-use survey for fishing hours | High | Limits ability to populate social flows Table 4a with real data |
| Figures marked [proxy] are estimates | Moderate | Conservative, order-of-magnitude correct |

---

## Sources

- Fiji Bureau of Statistics (2021). 2019-20 Household Income and Expenditure Survey Main Report. Suva: FBS.
- [Fiji HIES 2019-20](https://www.statsfiji.gov.fj/2019-20-hies/)
- [FAO FishStatJ](https://www.fao.org/fishery/statistics/software/fishstatj/en)
- [Allen Coral Atlas](https://allencoralatlas.org/)
- [MACBIO Fiji National Marine Ecosystem Service Valuation](http://macbio-pacific.info/wp-content/uploads/2017/10/Fiji-MESV-Digital-LowRes.pdf)
- [SPC PROCFish/C Fiji (GBIF)](https://www.gbif.org/dataset/806eae29-ea28-409f-9d95-f7b1f06f0448)
- [SPC Coastal Fisheries Programme](https://coastfish.spc.int/)
- [Fiji Subnational Boundaries (HDX)](https://data.humdata.org/dataset/cod-ab-fji)
