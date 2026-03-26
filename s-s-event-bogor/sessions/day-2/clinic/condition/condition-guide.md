# Condition Accounts -- Step-by-Step Guide

## Pathway A: No field data (Tier 1)

Estimated time: 30 minutes

### Step 1: Identify available proxies

Check what remote sensing and global assessment data exist for your area:

| Proxy source | What it tells you | Where to get it |
|-------------|-------------------|----------------|
| Sea surface temperature (SST) anomalies | Heat stress on coral reefs | NOAA Coral Reef Watch (coralreefwatch.noaa.gov) |
| Degree Heating Weeks (DHW) | Cumulative thermal stress | NOAA Coral Reef Watch |
| Chlorophyll-a concentration | Water quality / eutrophication | NASA Ocean Color (oceancolor.gsfc.nasa.gov) |
| Allen Coral Atlas condition layer | Reef benthic cover classes | allencoralatlas.org |
| Global Mangrove Watch canopy metrics | Mangrove canopy height/density | globalmangrovewatch.org |
| IUCN Red List of Ecosystems | Overall ecosystem risk status | iucnrle.org |

### Step 2: Set reference levels from literature

Use published benchmarks. Some starting points:

| Ecosystem | Indicator | Reference level source |
|-----------|-----------|----------------------|
| Coral reefs | Live coral cover 40-50% | Perry et al. 2013, regional reef health assessments |
| Coral reefs | Fish biomass 500 kg/ha | McClanahan et al. 2011 (unfished reef baseline) |
| Mangroves | Canopy cover 80-90% | Kauffman & Donato 2012 |
| Seagrass | Shoot density | Species-specific; check local literature |

### Step 3: Estimate condition from proxies

Example for coral reefs using SST:
- DHW > 4: likely bleaching stress
- DHW > 8: severe bleaching likely
- This gives a qualitative condition assessment, not a precise CI

Document clearly that this is a Tier 1 estimate. The purpose is to establish a baseline and identify what field data to collect.

### Step 4: Plan the field monitoring gap-fill

What indicators would improve this account? What is the minimum viable monitoring program?

| Indicator needed | Method | Estimated effort | Priority |
|-----------------|--------|-----------------|----------|
| | | | |
| | | | |

---

## Pathway B: You have field data (Tier 2)

Estimated time: 45-60 minutes

### Step 1: Inventory your indicators

List what your monitoring program measures:

| Indicator | Unit | Ecosystem type | Measured values available? | How many sites? | How many years? |
|-----------|------|---------------|--------------------------|----------------|----------------|
| | | | | | |
| | | | | | |
| | | | | | |

### Step 2: Choose reference levels

The SEEA EA (2021, Chapter 5.3.2-5.3.3 and Appendix A5.2) defines the reference condition as the **natural state** of the ecosystem -- the condition in the absence of major human modification. The reference level is the value of a variable at that reference condition.

The SEEA EA standard provides six methods for establishing reference conditions. Use the one most appropriate to your data and ecosystem:

| Method | SEEA EA ref | Description | When to use | Example |
|--------|------------|-------------|------------|---------|
| 1. Reference sites | A5.2 | Use undisturbed or least-disturbed sites as the benchmark | You have protected or remote sites with minimal human impact | Unfished reef biomass from no-take MPA |
| 2. Modelled reference | A5.2 | Use ecological models to estimate the natural state | You have modelling capacity and environmental predictors | Species distribution models predicting pre-disturbance cover |
| 3. Statistical approaches | A5.2 | Use the best percentile of observed data across sites | You have a large monitoring dataset with gradient of disturbance | Top 10th percentile of coral cover across all surveyed reefs |
| 4. Historical observations | A5.2 | Use pre-disturbance data (pre-1970 or earlier records) | Historical monitoring data, museum records, or paleo data exist | AGRRA data from earliest monitoring period; historical photos |
| 5. Contemporary baseline | A5.2 | Use a specific recent baseline year for comparison | Routine monitoring started at a known date | Reef condition at 2005 as baseline for trend tracking |
| 6. Prescribed levels | A5.2 | Use policy targets, sustainability thresholds, or ecological limits | You want to assess progress toward a management target | Zero bleaching as the upper reference; policy target cover levels |

**The most important thing is to document your choice.** State which method you used, cite the source, and explain why it is appropriate for your ecosystem and region. The SEEA EA says (para 5.73): "It is important to describe the rationale for their selection."

**Note on the Belize example used in this clinic:**
The reference levels in our exercises (coral cover 50%, fish biomass 500 kg/ha, etc.) use a mix of methods 1, 3, and 6. They are practical starting points from regional literature. For your own account, consider whether more locally appropriate reference levels exist from your monitoring history or regional benchmarks.

**Fill this table:**

| Indicator | Unit | Direction | Reference level | Source | SEEA EA method (1-6) |
|-----------|------|-----------|----------------|--------|---------------------|
| | | Higher is better / worse | | | |
| | | | | |

### Step 3: Normalize to condition index (CI)

**For each site and each indicator:**

Higher-is-better:
```
CI = min(Measured / Reference, 1.0)
```

Higher-is-worse:
```
CI = max(1 - (Measured / Reference), 0.0)
```

**Work through it in a spreadsheet:**

| Site | Indicator | Measured | Reference | Direction | CI |
|------|-----------|---------|-----------|-----------|---:|
| Site 1 | Coral cover | 25% | 50% | Higher better | =25/50 = 0.50 |
| Site 1 | Macroalgae | 35% | 60% | Higher worse | =1-(35/60) = 0.42 |
| Site 2 | Coral cover | 40% | 50% | Higher better | =40/50 = 0.80 |
| ... | | | | | |

### Step 4: Aggregate across sites

For each indicator, calculate the accounting-area average:

```
Mean CI = sum of all site CIs / number of sites
SE = standard deviation / sqrt(number of sites)
```

| Indicator | N sites | Mean CI | SE | 95% CI lower | 95% CI upper |
|-----------|---------|---------|-----|-------------|-------------|
| Coral cover | | | | | |
| Macroalgae | | | | | |
| Fish biomass | | | | | |

### Step 5: Build the condition account table

If you have two time periods (opening and closing):

| Indicator | Reference | Opening CI | Closing CI | Absolute change | Direction |
|-----------|----------|--------:|--------:|--------:|-----------|
| | | | | | Improving / declining / stable |
| | | | | | |

If you have only one time period, report it as either opening or closing. A single-period account is valid and provides a baseline for future comparison.

### Step 6: Interpret results

For each indicator:
- CI close to 1.0: near reference condition (healthy)
- CI close to 0.0: highly degraded
- Positive change: improving
- Negative change: declining

---

## Reference: SEEA EA Condition Account Table Format

**Table [X]: Ecosystem Condition Account, [Ecosystem Type], [Area], [Period]**

| Ecosystem type | Indicator | Unit | Reference level | Opening value | Opening CI | Closing value | Closing CI | Change in CI |
|---------------|-----------|------|----------------|---:|---:|---:|---:|---:|
| [type] | | | | | | | | |
| | | | | | | | | |

**Composite condition index** (optional): average of all individual indicator CIs, giving a single summary score per ecosystem type.
