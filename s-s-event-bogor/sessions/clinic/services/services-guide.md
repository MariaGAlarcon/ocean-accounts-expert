# Ecosystem Services Accounts -- Step-by-Step Guide

## Pathway A: No primary data / Value transfer (Tier 1)

Estimated time: 30-45 minutes

### Step 1: Select priority services

Which services are most relevant to your country's policy question?

| Policy priority | Most relevant services |
|----------------|----------------------|
| Climate commitments (NDC) | Carbon sequestration |
| Food security / fisheries | Fish provisioning |
| Coastal resilience / disaster risk | Coastal protection |
| Tourism / blue economy | Recreation |
| MPA justification | Multiple services (total value) |
| Blue carbon finance | Carbon sequestration + extent |

Pick 1-2 services to start with.

### Step 2: Get extent data

You need to know the area (ha) of each ecosystem providing the service. Use your extent account, or estimate from global datasets.

| Ecosystem | Your extent (ha) |
|-----------|---:|
| Coral reefs | |
| Seagrass | |
| Mangroves | |

### Step 3: Find published per-hectare values

Sources for value transfer:
- **ESVD** (Ecosystem Services Valuation Database): esvd.info
- **TEEB** (The Economics of Ecosystems and Biodiversity): teebweb.org
- **Published studies** from similar regions

Example values from literature (illustrative, verify for your context):

| Service | Ecosystem | Published value (USD/ha/yr) | Source region |
|---------|-----------|---:|--------------|
| Carbon sequestration | Mangroves | 188 | Global average |
| Carbon sequestration | Seagrass | 66 | Global average |
| Coastal protection | Coral reefs | 350 | Tropical average |
| Fish provisioning | Coral reefs | 150-600 | Varies widely |
| Recreation | Coral reefs | 200-1,000 | Tourism-dependent areas |

### Step 4: Calculate transferred value

```
Estimated value = Your extent (ha) x Published value (USD/ha/yr)
```

**Adjustments to consider:**
- Income adjustment: multiply by (your country GDP per capita / source country GDP per capita)
- Ecosystem quality: if your reefs are degraded, reduce proportionally
- Market conditions: if tourism is lower in your area, reduce recreation values

### Step 5: Document and flag limitations

| Limitation | Your note |
|-----------|----------|
| Source study location | |
| Year of source valuation | |
| Comparability to your ecosystem | |
| Adjustments applied | |
| Confidence level | Low / Medium |

---

## Pathway B: Primary calculation (Tier 2)

### Service 1: Carbon sequestration

**Data needed:**
- Ecosystem extent (ha) from extent account
- Net carbon production (NCP) rate (Mg CO2/ha/yr) from literature or field measurement
- Carbon price (SCC or market price)

**Calculation:**

| Step | Formula | Your values |
|------|---------|------------|
| 1. Extent | From extent account | ___ ha mangrove, ___ ha seagrass |
| 2. NCP rate | Literature (mangrove ~3.7, seagrass ~1.3 Mg CO2/ha/yr) | |
| 3. Physical supply | Extent x NCP rate | ___ Mg CO2/yr |
| 4. Price | SCC (USD 51/Mg CO2) or local carbon market price | USD ___/Mg CO2 |
| 5. Monetary value | Physical supply x Price | USD ___/yr |

---

### Service 2: Fish provisioning

**Data needed:**
- Annual catch by species (kg/yr) from fisheries records or fisher surveys
- Market price per species (USD/kg)
- Fishing costs: labour, fuel, gear, vessel maintenance

**Calculation:**

| Step | Formula | Your values |
|------|---------|------------|
| 1. Total catch | From fisheries data | ___ kg/yr |
| 2. Gross revenue | Sum of (catch per species x market price) | USD ___/yr |
| 3. Total costs | Labour + fuel + gear + capital depreciation | USD ___/yr |
| 4. Resource rent | Gross revenue - Total costs | USD ___/yr |

If resource rent is negative, the ecosystem service value is zero (the fishery is economically unprofitable even though the ecosystem provides fish).

**Disaggregation by ecosystem type:**
Assign catch to ecosystem types using species-habitat associations:
- Reef-associated species: coral reef ecosystem
- Seagrass-associated: seagrass ecosystem
- Pelagic species: open ocean

---

### Service 3: Coastal protection

**Data needed:**
- Length of coastline protected by ecosystems (m)
- Assets behind the coastline (buildings, infrastructure)
- Cost to replace protection if ecosystem were lost (seawall, breakwater)

**Calculation:**

| Step | Formula | Your values |
|------|---------|------------|
| 1. Protected coastline | Map reef/mangrove extent along coast | ___ m |
| 2. Assets at risk | Building count or value behind coastline | |
| 3. Replacement cost | Engineering cost per m of seawall or breakwater | USD ___/m |
| 4. Total value | Protected coastline x Replacement cost | USD ___/yr (annualized) |

---

### Service 4: Recreation / tourism

**Data needed:**
- Visitor numbers (tourists, divers, snorkelers per year)
- Per-visitor spending attributable to the ecosystem
- Or: activity fees, tour operator revenue

**Calculation:**

| Step | Formula | Your values |
|------|---------|------------|
| 1. Visitors | From tourism statistics or operator records | ___/yr |
| 2. Reef/ecosystem-attributable spending | Activity fees + allocated accommodation | USD ___/visitor |
| 3. Total value | Visitors x Spending per visitor | USD ___/yr |

---

## Reference: SEEA EA Supply and Use Table Format

**Table [X]: Ecosystem Service Supply and Use Account, [Area], [Year]**

**Physical supply:**

| Service | Unit | Coral reefs | Seagrass | Mangroves | Total |
|---------|------|---:|---:|---:|---:|
| Fish provisioning | kg/yr | | | | |
| Carbon sequestration | Mg CO2/yr | | | | |
| Coastal protection | m coastline | | | | |
| Recreation | visitors/yr | | | | |

**Monetary supply (USD/yr):**

| Service | Method | Coral reefs | Seagrass | Mangroves | Total |
|---------|--------|---:|---:|---:|---:|
| Fish provisioning | Resource rent | | | | |
| Carbon sequestration | SCC | | | | |
| Coastal protection | Replacement cost | | | | |
| Recreation | Expenditure | | | | |
| **Total** | | | | | |
