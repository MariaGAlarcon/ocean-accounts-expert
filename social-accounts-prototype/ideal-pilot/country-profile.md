# Ideal Worked Example: Tuvana (Fictional Pacific Island Country)

## Purpose

This is a reference implementation using synthetic data for a fictional country. It shows what the complete social accounts system looks like when all data is available at the spatial resolution needed. No data gaps, no proxies -- the "ideal case" that practitioners are building toward. All numbers are plausible but invented.

---

## Country profile: Tuvana

**Geography:** A small island developing state in the tropical Pacific. One main island (Viti) and an outer island group (Lau archipelago, 12 inhabited islands). Total land area ~2,100 km2. Exclusive Economic Zone ~120,000 km2.

**Population:** 142,000 (2022 census)
- Urban (Viti capital, Nasova): 68,000 (48%)
- Peri-urban coastal (Viti): 32,000 (23%)
- Rural coastal (Viti): 22,000 (15%)
- Outer islands (Lau): 20,000 (14%)

**Economy:** GDP ~USD 780 million. Ocean economy represents ~28% of GDP (fisheries 12%, tourism 11%, maritime transport 5%). Agriculture and fishing employ 35% of the rural workforce. Tourism employs 18% of the urban workforce.

**Marine ecosystems:**
- Coral reef: 3,200 km2
- Mangrove: 180 km2
- Seagrass: 95 km2
- Deep water (pelagic zone): ~116,000 km2

**Governance:** 24 customary marine tenure areas (comparable to Fiji's qoliqoli). National Marine Protected Area covering 15% of territorial waters. 6 co-management agreements between government and communities.

**Household survey:** National Household Income and Expenditure Survey conducted 2021-22, 4,000 households, includes food consumption by source (purchased, own production, gifted).

---

## Basic Spatial Units (BSUs)

Tuvana is divided into 8 BSUs for the social accounts pilot. Each BSU combines a marine ecosystem accounting area with the adjacent coastal community.

| BSU | Name | Ecosystem types | Area (km2 marine) | Population | Households | Primary livelihood |
|---|---|---|---|---|---|---|
| BSU-1 | Nasova Urban | Fringing reef, harbour | 45 | 68,000 | 15,200 | Services, tourism |
| BSU-2 | Viti North Coast | Barrier reef, mangrove | 380 | 12,000 | 2,700 | Commercial fishing, farming |
| BSU-3 | Viti South Coast | Fringing reef, seagrass | 290 | 10,000 | 2,200 | Tourism, mixed |
| BSU-4 | Viti West Coast | Mangrove, mudflat | 150 | 10,000 | 2,300 | Aquaculture, farming |
| BSU-5 | Lau North (4 islands) | Coral reef, deep channel | 520 | 6,000 | 1,300 | Subsistence fishing |
| BSU-6 | Lau Central (4 islands) | Coral reef, seagrass | 480 | 5,500 | 1,200 | Subsistence fishing, gleaning |
| BSU-7 | Lau South (4 islands) | Coral reef, deep water | 510 | 5,000 | 1,100 | Subsistence fishing |
| BSU-8 | Offshore (pelagic) | Open ocean | ~116,000 | -- | -- | Commercial tuna fleet |
| | **Total** | | **~118,375** | **~142,000** (some inland) | **~26,000** | |

### BSU map concept

```
                    BSU-8 (Offshore/Pelagic)
    ................................................
    .                                              .
    .     BSU-5          BSU-6          BSU-7      .
    .     (Lau N)        (Lau C)        (Lau S)   .
    .       o o            o o            o o      .
    .        o              o              o       .
    .                                              .
    .                                              .
    .          BSU-2 (Viti North)                   .
    .          _______________                      .
    .    BSU-4|               |BSU-3                .
    .   (West)|  VITI ISLAND  |(South)              .
    .         |    BSU-1      |                     .
    .         |   (Nasova)    |                     .
    .         |_______________|                     .
    .                                              .
    ................................................
```

---

## Ecosystem accounts summary (from ecosystem accounting)

### Extent account (km2)

| Ecosystem type | Opening (2020) | Additions | Reductions | Closing (2022) | Net change |
|---|---|---|---|---|---|
| Coral reef | 3,240 | 0 | -40 (bleaching) | 3,200 | -40 |
| Mangrove | 175 | +8 (restoration) | -3 (clearance) | 180 | +5 |
| Seagrass | 102 | 0 | -7 (sedimentation) | 95 | -7 |
| Total | 3,517 | +8 | -50 | 3,475 | -42 |

### Condition account (CI, 0 to 1)

| Indicator | BSU-1 | BSU-2 | BSU-3 | BSU-4 | BSU-5 | BSU-6 | BSU-7 | BSU-8 |
|---|---|---|---|---|---|---|---|---|
| Hard coral cover CI | 0.28 | 0.52 | 0.45 | -- | 0.68 | 0.71 | 0.65 | -- |
| Fish biomass CI | 0.22 | 0.48 | 0.40 | 0.35 | 0.72 | 0.75 | 0.70 | 0.55 |
| Mangrove condition CI | -- | 0.60 | -- | 0.55 | -- | -- | -- | -- |
| Seagrass condition CI | -- | -- | 0.50 | -- | -- | 0.62 | -- | -- |
| Water quality CI | 0.30 | 0.55 | 0.50 | 0.45 | 0.82 | 0.80 | 0.85 | 0.90 |

*See Figure 1 (`figures/tuvana-bsu-map.svg`) for the spatial layout of BSUs.*

**Pattern:** Urban and peri-urban BSUs (1-4) have lower condition indices. Outer island BSUs (5-7) are in better ecological condition due to lower population pressure and active customary management. This spatial gradient is the key test for whether social outcomes track ecosystem condition.
