# Extent Accounts -- Step-by-Step Guide

## Pathway A: No data / Global datasets (Tier 1)

Estimated time: 30-45 minutes

### Step 1: Define your accounting area

- What geographic area are you accounting for? (country EEZ, province, MPA, bay, atoll)
- Get or draw a boundary polygon (shapefile, GeoJSON, or even a screenshot from Google Maps)
- Note the total area in hectares or km2

### Step 2: Identify ecosystem types present

Fill this table for your area:

| Ecosystem type | IUCN GET code | Present? (Y/N) | Global dataset to use |
|---------------|---------------|----------------|----------------------|
| Coral reefs | M1.3 | | Allen Coral Atlas |
| Seagrass meadows | M1.1 | | Allen Coral Atlas, UNEP-WCMC |
| Mangroves | MFT1.2 | | Global Mangrove Watch (v3.0) |
| Kelp forests | M1.2 | | Literature review |
| Salt marshes | TF1.2 | | Global Wetlands Map |
| Sandy shores | T2.1 | | Manual digitization |
| Rocky shores | | | Manual digitization |
| Deep water / open ocean | M2.1 | | Bathymetry data |

### Step 3: Download global extent data

**For coral reefs and seagrass:**
- Go to allencoralatlas.org
- Navigate to your area
- Use the "Download" or area statistics feature
- Record hectares per benthic class

**For mangroves:**
- Go to globalmangrovewatch.org
- Select your country or draw your area
- Record mangrove extent in hectares for each available year

**For multiple time periods:**
- Allen Coral Atlas has some change detection products
- Global Mangrove Watch has extent for 1996, 2007-2020 (annual)
- Record opening year and closing year extent

### Step 4: Fill the extent account table

Transfer your data into the SEEA EA format:

| Ecosystem type | Opening extent (ha) [year: ___] | Closing extent (ha) [year: ___] | Net change (ha) | Net change (%) |
|---------------|---:|---:|---:|---:|
| Coral reefs | | | | |
| Seagrass | | | | |
| Mangroves | | | | |
| Other/unclassified | | | | |
| **Total** | | | | 0 |

### Step 5: Document limitations

For Tier 1 accounts using global data, note:
- Global products have transfer errors for your local conditions
- Resolution may be coarser than national needs (e.g., 10 m vs. 1 m)
- Some ecosystem types may be underrepresented or misclassified
- Validate against any available local knowledge or reports

---

## Pathway B: National/regional data or satellite imagery (Tier 2)

Estimated time: varies (the clinic session focuses on structuring, not full classification)

### Step 1: Define accounting area (same as Pathway A)

### Step 2: Inventory your data

| Data type | What you have | Format | Resolution | Time period |
|-----------|--------------|--------|-----------|-------------|
| Satellite imagery | | | | |
| Habitat maps | | | | |
| Ground truth points | | | | |
| Previous classifications | | | | |
| National statistics | | | | |

### Step 3: Determine classification approach

| Your situation | Recommended approach |
|---------------|---------------------|
| You have classified maps for two periods | Go directly to Step 4 |
| You have raw satellite imagery | Classify using SAM (Sentinel-2) or Random Forest (high-res) |
| You have monitoring data but no maps | Use point data to estimate cover fractions per spatial unit |
| You have national statistics (e.g., mangrove area from forestry dept) | Use as-is for first account, plan spatial improvement |

### Step 4: Calculate extent per ecosystem type

For each time period:
1. Count the area (ha) assigned to each ecosystem type
2. Ensure complete coverage (every hectare assigned to exactly one type)
3. Fill the extent account table

### Step 5: Build the change matrix (if two periods available)

Cross-tabulate opening vs. closing classifications:

| Opening \ Closing | Coral | Seagrass | Mangrove | Other | Row total |
|-------------------|------:|--------:|---------:|------:|----------:|
| Coral | | | | | |
| Seagrass | | | | | |
| Mangrove | | | | | |
| Other | | | | | |
| **Column total** | | | | | |

Row totals = opening extent per type.
Column totals = closing extent per type.
Off-diagonal cells = transitions between types.

### Step 6: Validate transitions

Flag any transitions that seem ecologically unlikely:
- Coral converting to mangrove (usually impossible; likely misclassification)
- Large area changes (>10%) need explanation (real change vs. classification error)
- Check boundary areas between ecosystem types (common source of false transitions)

---

## Reference: SEEA EA Extent Account Table Format

The final output should follow this structure:

**Table [X]: Ecosystem Extent Account, [Accounting Area], [Opening Year] to [Closing Year]**

| | Coral reefs (M1.3) | Seagrass (M1.1) | Mangroves (MFT1.2) | Other | Total |
|---|---:|---:|---:|---:|---:|
| **Opening extent (ha)** | | | | | |
| Additions: managed expansion | | | | | |
| Additions: natural expansion | | | | | |
| Additions: reclassification | | | | | |
| **Total additions** | | | | | |
| Reductions: managed reduction | | | | | |
| Reductions: natural reduction | | | | | |
| Reductions: reclassification | | | | | |
| **Total reductions** | | | | | |
| **Net change** | | | | | |
| **Closing extent (ha)** | | | | | |
