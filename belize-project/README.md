# Belize Ocean Accounts

Coral reef condition accounts for Belize using AGRRA survey data and the SEEA EA framework.

## Overview

This project calculates coral reef condition indicators from AGRRA (Atlantic and Gulf Rapid Reef Assessment) field data and formats them as SEEA EA (System of Environmental-Economic Accounting — Ecosystem Accounting) condition account tables. The ecosystem type is photic coral reefs (IUCN GET M1.3).

**Indicators calculated:**
- Live Coral Cover (%)
- Fleshy Macroalgae Cover (%)
- Coral Recruit Density (per 25 m2)
- Coral Diversity (Shannon index + richness)
- Reef Relief (cm)
- Coral Bleaching Prevalence (%)

## Repository Structure

| Folder | Contents |
|--------|----------|
| `condition-account-scripts/` | R pipeline for data processing and indicator calculation |
| `docs/` | Methodology report, technical guidance, and GOAP document conventions |
| `training/` | Workshop facilitator guide, exercise handouts, and workbooks |
| `GOAP-condition-account-belize-feedback/` | Feedback on the original GOAP pipeline scripts |
| `seea-ea-methodology/` | SEEA EA methodology reference and guidance documents |

## Quick Start

### Test with dummy data

1. Open R with working directory set to `condition-account-scripts/`
2. Open `indicator_calculation.r`
3. Set `test_on <- TRUE`
4. Run the script

### Run with real AGRRA data

1. Place AGRRA Excel files in `condition-account-scripts/data_deposit/`:
   - `BenthicRaw.xlsx`
   - `CoralRaw.xlsx`
   - `FishRaw.xlsx`
   - `Metadata.xlsx`
2. Open R with working directory set to `condition-account-scripts/`
3. Set `test_on <- FALSE` in `indicator_calculation.r`
4. Run the script
5. Check `condition-account-scripts/outputs/validation_report.txt` for data quality results

## Requirements

- R (≥ 4.0)
- R packages: tidyverse, readxl, knitr (auto-installed on first run)
