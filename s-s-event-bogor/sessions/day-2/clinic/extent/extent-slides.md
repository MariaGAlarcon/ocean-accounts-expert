# Extent Accounts -- Clinic Walkthrough Slides

**Time:** 15-30 min depending on participant level
**Purpose:** Guide a fellow through building an ecosystem extent account

---

## Slide 1: What is an extent account?

An extent account measures the **area of each ecosystem type** within your accounting area, and tracks how that area changes over time.

| Component | What it records |
|-----------|----------------|
| Opening extent | Area (ha) of each ecosystem at start of period |
| Additions | Area gained (expansion, restoration, reclassification) |
| Reductions | Area lost (degradation, conversion, reclassification) |
| Closing extent | Area at end of period |

Extent is the **foundation** for all other accounts. You need to know where ecosystems are before you can measure their condition or services.

---

## Slide 2: What ecosystem types?

Common marine/coastal types (adapt to your country):

| Ecosystem Type | IUCN GET Code | Global Dataset Available |
|---------------|---------------|------------------------|
| Coral reefs | M1.3 | Allen Coral Atlas |
| Seagrass meadows | M1.1 | Allen Coral Atlas, UNEP-WCMC |
| Mangroves | MFT1.2 | Global Mangrove Watch |
| Kelp forests | M1.2 | Literature |
| Coastal wetlands | TF1.2 | Global Wetlands Map |
| Open ocean / pelagic | M2.1 | EEZ boundaries |

**Your first task:** List the ecosystem types present in your accounting area.

---

## Slide 3: Two pathways

**Pathway A -- No data or global datasets only (Tier 1)**

Use freely available global products:
1. Download extent data from Allen Coral Atlas or Global Mangrove Watch
2. Clip to your accounting area boundary
3. Calculate area per ecosystem type
4. Compare two time periods if available

**Pathway B -- You have satellite imagery or national maps (Tier 2)**

Classify your own imagery:
1. Define your accounting area boundary
2. Obtain satellite imagery (Sentinel-2 is free, 10 m resolution)
3. Classify ecosystems using remote sensing methods
4. Validate with ground truth data
5. Compare opening and closing period maps

---

## Slide 4: The extent account table

This is what you are building:

| Ecosystem type | Opening extent (ha) | Additions (ha) | Reductions (ha) | Net change (ha) | Closing extent (ha) |
|---------------|--------------------:|----------------:|-----------------:|----------------:|--------------------:|
| Coral reefs | | | | | |
| Seagrass | | | | | |
| Mangroves | | | | | |
| Other (sand, rubble, deep water) | | | | | |
| **Total accounting area** | | | | | |

**Rules:**
- Total accounting area must be the same for opening and closing (area is conserved)
- "Other" category captures all non-target ecosystem types
- Every hectare must be assigned to exactly one category

---

## Slide 5: The change matrix

Shows where area moved between ecosystem types:

|  | Coral (closing) | Seagrass (closing) | Mangrove (closing) | Other (closing) | **Opening total** |
|---|---:|---:|---:|---:|---:|
| **Coral (opening)** | Stable | Coral to seagrass | Coral to mangrove | Coral lost | |
| **Seagrass (opening)** | Seagrass to coral | Stable | | Seagrass lost | |
| **Mangrove (opening)** | | | Stable | Mangrove lost | |
| **Other (opening)** | Coral gained | Seagrass gained | Mangrove gained | Stable | |
| **Closing total** | | | | | |

This tells you not just how much changed, but **what changed into what**.

---

## Slide 6: What to do right now

**If you have no data:**
1. Go to Allen Coral Atlas (allencoralatlas.org) or Global Mangrove Watch
2. Find your country or area
3. Download the habitat map
4. Fill in the extent table (Slide 4) with area estimates

**If you have data:**
1. Open your classified map or habitat data
2. Calculate area per ecosystem type
3. Fill in the extent table
4. If you have two time points, calculate the change matrix

**Need help?** Ask a facilitator to walk you through it.
