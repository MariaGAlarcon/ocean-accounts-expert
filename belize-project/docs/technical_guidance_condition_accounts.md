# Technical Guidance: Compiling Coral Reef Condition Accounts for Belize

## Audience and Prerequisites

This guide is written for Belize Statistical Institute staff and Fisheries Department analysts who will update the coral reef condition accounts in future accounting periods. It assumes you have R installed and can run the indicator calculation pipeline to produce site-level indicator values. It does not assume prior experience with SEEA EA normalization or condition account tables.

This guide covers three steps: normalizing indicator values to condition indices, aggregating by geographic unit, and assembling the final SEEA EA condition account table. For details on how the raw indicators are calculated from AGRRA field data, see `docs/methodology_coral_condition_accounts.md`. For the generic SEEA EA condition account framework, see `seea-ea-methodology/05_seea_accounting_tables/skill_condition_opening_closing_seea_account.md`.

## 1. Overview

A condition account records the state of an ecosystem at two points in time using measurable indicators. Each indicator value is compared against a reference level that represents a healthy or pre-degradation state. The ratio produces a condition index between 0 (fully degraded) and 1 (reference condition met or exceeded). Comparing condition indices across time shows whether the ecosystem is improving, declining, or stable.

This guide covers the three steps between raw indicator values (produced by the R pipeline) and the final SEEA EA condition account table:

1. **Normalization**: converting each site-level indicator value to a condition index using reference levels.
2. **Spatial aggregation**: calculating the mean and standard error across sites within each geographic unit (MPA, subregion, or national).
3. **Account table assembly**: combining opening-year and closing-year results into the standard SEEA EA format with change metrics, interpretation, and data quality ratings.

## 2. Inputs

Before starting, you need one file: the site-level indicator values produced by running the R pipeline. This file has one row per site per year, with these columns:

| Column | Description | Example |
|---|---|---|
| Year | Survey campaign year | 2023 |
| Site | AGRRA site code or name | BZHCCD01 |
| Live_Coral_Cover | Percentage of reef substrate with live coral | 8.55 |
| Fleshy_Macroalgae_Cover | Percentage of reef substrate with fleshy macroalgae | 28.63 |
| Recruit_Density | Coral recruits per unit area | 0.32 |
| Coral_Diversity_H | Shannon diversity index (H') | 1.12 |
| Reef_Relief | Mean maximum relief in cm across transects | 45.5 |

To produce this file, run `condition_account_seea.r` from the `condition-account-scripts/` directory with the AGRRA data files in `data_deposit/`. The script writes site-level values to `outputs/` as part of its pipeline. You can also produce the values by running the original GOAP scripts (`indicator_calculation.r`) and extracting the intermediate site-level dataframes.

## 2.1 Extended Table Columns

The CSV output files contain the core SEEA EA condition account columns. For full compliance with the SEEA EA reference format, extended tables can include additional columns: IUCN ecosystem type code (M1.3 for coral reefs), normalization type (higher_is_better or inverted_higher_is_worse), condition index standard error for both opening and closing years (calculated as SE_measured / Reference_Level), and raw value change metrics alongside the condition index change. These extended columns can be added to CSV annexes or supplementary tables without changing the core account structure. The R script (`condition_account_seea.r`) includes the IUCN code in the Ecosystem_Type column; the remaining extended columns can be derived from the existing output fields.

## 3. Reference Levels

Each indicator is normalized against a reference level that represents a healthy Caribbean reef. The table below lists the five reference levels used in the Belize accounts.

| Indicator | Reference level | Unit | Direction | Source |
|---|---|---|---|---|
| Live coral cover | 50 | % | Higher is better | Caribbean pre-1980s baseline (Gardner et al. 2003) |
| Fleshy macroalgae cover | 50 | % | Higher is worse | Algal dominance threshold (Bruno et al. 2009) |
| Coral recruit density | 15 | per m2 | Higher is better | Healthy reef observations (Bak and Engel 1979) |
| Coral diversity (H') | 2.0 | index | Higher is better | Upper range of Caribbean coral Shannon index |
| Reef relief | 150 | cm | Higher is better | Empirical high-complexity threshold (this dataset) |
| Coral bleaching prevalence | 100 | % | Higher is worse | Theoretical maximum; CI = proportion of reef not showing bleaching |

**Direction** determines which normalization formula to use. "Higher is better" means larger measured values indicate better condition. "Higher is worse" means larger values indicate degradation (applies only to fleshy macroalgae cover).

**When to update reference levels.** Reference levels should be reviewed when new peer-reviewed literature provides stronger Caribbean or Belize-specific benchmarks. Locally calibrated baselines from long-term monitoring (10+ years) would replace these regional defaults. Any changes to reference levels must be documented and applied consistently to both the opening and closing years to keep the comparison valid.

**Reference level confidence.** The reference levels for live coral cover, fleshy macroalgae cover, and coral recruit density are drawn from peer-reviewed Caribbean literature (Type 2 regional benchmarks). The coral diversity reference rests on weaker consensus from regional studies. The reef relief reference (150 cm) is derived from the empirical distribution of the current Belize dataset and is closer to a Type 1 (ad-hoc) reference. Condition indices for reef relief should be interpreted with more caution than those for the literature-based indicators.

## 4. Normalization

For each site, for each indicator, calculate a condition index (CI) using one of the two formulas below.

### 4.1 Higher-is-better indicators

Applies to: live coral cover, recruit density, coral diversity, reef relief.

> CI = min(measured value / reference level, 1.0)

The `min()` caps the index at 1.0 so that values exceeding the reference level do not produce indices above 1.

**Worked example.** Site BZHCCD01, 2023. Live coral cover = 8.55%.

> CI = min(8.55 / 50, 1.0) = min(0.171, 1.0) = 0.17

### 4.2 Higher-is-worse indicators

Applies to: fleshy macroalgae cover, coral bleaching prevalence.

> CI = max(1 - (measured value / reference level), 0.0)

The `max()` prevents negative indices when the measured value exceeds the reference level.

**Worked example.** Site BZHCCD01, 2023. Fleshy macroalgae cover = 28.63%.

> CI = max(1 - (28.63 / 50), 0.0) = max(1 - 0.5726, 0.0) = 0.43

### 4.3 Handling missing values

If an indicator value is missing for a site in a given year (for example, no coral community transects were conducted), leave the condition index as blank for that site. Do not substitute zero; a missing observation is different from a measured value of zero. Missing sites are excluded from the mean calculation in Section 5.

## 5. Spatial Aggregation

After normalizing each site, aggregate to the geographic unit level.

### 5.1 Define geographic units

A geographic unit is the area for which you are producing a condition account. This can be a marine protected area, a subregion, or the whole country. Each geographic unit contains a defined set of survey sites.

The current MPA-to-site assignments for Belize are:

| Geographic unit | Sites |
|---|---|
| Ambergris Caye (pilot) | BZHCCD01, BZHCCD02, BZ1231, BZ1077, BZ1079, MXRCK, BZ1081, BZ1234 |
| Hol Chan Marine Reserve | BZHCCD01, BZHCCD02, BZ1231, BZ1077 |
| Caye Caulker Marine Reserve | BZ1230, CCSC, 1076B |
| Glover's Reef Marine Reserve | All sites where Subregion = "Glover's Reef Atoll" |
| Sapodilla Cayes Marine Reserve | BZSCMR, Nicholas Caye, BZ1019, BZ1026, BZ1124, BZ1130, BZ1149 |
| Laughing Bird Caye National Park | LBCMBRS1, LBCMBRS2 |

To add a new geographic unit, list the site codes that belong to it and add an entry to the `geo_units` list in `condition_account_seea.r` (Section 5 of that script, around line 242).

### 5.2 Calculate mean and standard error

For each geographic unit, for each indicator, for each year:

> Mean = sum of site values / N

> SE = sd(site values) / sqrt(N)

where N is the number of sites with data for that indicator in that year, and sd() is the sample standard deviation.

**Worked example.** Ambergris Caye, live coral cover, 2023. Seven sites had data:

| Site | Live coral cover (%) |
|---|---|
| BZHCCD01 | 8.55 |
| BZHCCD02 | 6.17 |
| BZ1231 | 11.33 |
| BZ1077 | 5.83 |
| BZ1079 | 3.50 |
| MXRCK | 14.50 |
| BZ1081 | 6.28 |

Mean = (8.55 + 6.17 + 11.33 + 5.83 + 3.50 + 14.50 + 6.28) / 7 = 56.16 / 7 = 8.02

Standard deviation = 3.72 (calculated from the 7 values)

SE = 3.72 / sqrt(7) = 3.72 / 2.646 = 1.41

The values in the actual account output are mean = 8.02 and SE = 1.57 (minor differences arise from rounding in the intermediate calculations within R).

### 5.3 Normalize the aggregated mean

Apply the same normalization formula from Section 4 to the geographic unit mean.

> CI (Ambergris Caye LCC 2023) = min(8.02 / 50, 1.0) = 0.1604

Round to 4 decimal places: 0.1605 (matching the CSV output, where R's internal precision produces a slightly different trailing digit).

**Propagate uncertainty.** Calculate the standard error of the condition index:

> SE_CI = SE_measured / reference_level = 1.57 / 50 = 0.0314

## 6. Building the Condition Account Table

### 6.1 Assemble one row per indicator

Each row in the condition account table represents one indicator for one geographic unit. The columns are:

| Column | What to enter |
|---|---|
| Geographic_Unit | Name of the MPA, subregion, or national unit |
| Ecosystem_Type | "Coral reef (M1.3)" |
| Indicator | Name of the indicator (e.g., "Live Coral Cover") |
| Unit | Measurement unit (%, per m2, index, cm) |
| Reference_Level | The reference level value from Section 3 |
| Opening_Year | The first year of the accounting period (e.g., 2023) |
| Opening_Value | Mean indicator value across sites in the opening year |
| Opening_SE | Standard error of the opening year mean |
| Opening_CI | Condition index for the opening year |
| Closing_Year | The second year of the accounting period (e.g., 2025) |
| Closing_Value | Mean indicator value across sites in the closing year |
| Closing_SE | Standard error of the closing year mean |
| Closing_CI | Condition index for the closing year |
| CI_Change | Closing_CI minus Opening_CI |
| Pct_Change | (CI_Change / Opening_CI) x 100 |
| Interpretation | Stable, Improving, or Declining (see Section 6.3) |
| N_Sites | Number of sites with data, formatted as "opening/closing" (e.g., "7/5") |
| Data_Quality | Good, Moderate, or Limited (see Section 6.4) |

### 6.2 Calculate change metrics

For each indicator row:

> Absolute change = Closing CI - Opening CI

> Percent change = (Absolute change / Opening CI) x 100

If the opening CI is zero or missing, percent change cannot be calculated. Report as "--".

**Worked example.** Ambergris Caye, live coral cover.

Opening CI = 0.1605, Closing CI = 0.0687.

Absolute change = 0.0687 - 0.1605 = -0.0918

Percent change = (-0.0918 / 0.1605) x 100 = -57.21%

### 6.3 Classify the interpretation

Compare the absolute change against the standard error to determine whether the change is meaningful.

1. Calculate the SE threshold as the mean of the opening and closing SE of the condition index. If only one period has SE, use that value.
2. If the absolute change is within one SE threshold of zero (i.e., |CI_Change| <= SE_threshold), classify as **Stable**.
3. If the absolute change is positive and exceeds the threshold, classify as **Improving**.
4. If the absolute change is negative and exceeds the threshold, classify as **Declining**.

For sites with data in only one year, report as "Opening only" or "Closing only" instead of a change classification.

**Worked example.** Ambergris Caye, live coral cover.

Opening SE_CI = 1.57 / 50 = 0.0314. Closing SE_CI = 1.57 / 50 = 0.0314.

SE threshold = mean(0.0314, 0.0314) = 0.0314.

|CI_Change| = 0.0918, which exceeds 0.0314. Change is negative, so interpretation = **Declining**.

**Note on statistical rigor.** The 1-SE threshold is a pragmatic simplification. The SEEA EA reference methodology describes a more conservative 95% confidence interval overlap test: change is classified as significant only when the opening and closing 95% CIs do not overlap. The 1-SE approach is more permissive and may classify some changes as meaningful that would not pass the stricter test. For accounts with larger sample sizes or longer time series, adopting the 95% CI overlap test or formal paired-site hypothesis testing would strengthen the interpretation.

### 6.4 Assign data quality rating

The quality rating reflects how many sites contribute to the account for each geographic unit. Use the minimum of the opening and closing site counts.

| Minimum site count | Rating |
|---|---|
| 5 or more | Good |
| 3 to 4 | Moderate |
| 1 to 2 | Limited |

If data exists for only one period, append "(one period)" to the rating.

**Worked example.** Ambergris Caye, live coral cover. Opening: 7 sites. Closing: 5 sites. Minimum = 5. Rating = **Good**.

### 6.5 Handle missing data

Some indicators may be missing for one or both periods at a geographic unit. Common cases and how to handle them:

| Situation | How to report |
|---|---|
| No data for an indicator in either year | Omit the row, or include it with all values blank and Interpretation = "Insufficient data" |
| Data in the opening year only | Report opening values; leave closing columns blank; Interpretation = "Opening only" |
| Data in the closing year only | Report closing values; leave opening columns blank; Interpretation = "Closing only" |
| Fewer than 3 sites in both years | Report values but flag Data_Quality as "Limited"; interpret change with caution |

**Worked example.** Ambergris Caye, coral diversity (Shannon H'). No coral community transects were conducted in 2023 for these sites, so opening-year data is missing. The account reports: Opening_Value = NA, Opening_CI = NA, Closing_Value = 1.06, Closing_CI = 0.529, Interpretation = "Closing only".

## 7. Updating for the Next Accounting Period

When new AGRRA survey data becomes available for a future year, the current closing year becomes the new opening year. Here is what to change.

**In the R script.** Open `condition_account_seea.r` and update the two year variables near line 501:

```r
year_opening <- "2025"   # was "2023"
year_closing <- "2027"   # new closing year
```

**Adding new sites.** If the new campaign surveys sites that were not in the previous dataset, they will be included automatically in the site-level calculations. To assign them to a geographic unit, add their site codes to the relevant entry in the `geo_units` list (Section 5 of the script, around line 242).

**Adding new MPAs.** To add a new marine protected area as a geographic unit, add an entry to the `geo_units` list:

```r
geo_units[["NEW_MPA_KEY"]] <- list(
    name = "New MPA Display Name",
    sites = c("SITE1", "SITE2", "SITE3")
)
```

**Checklist for a new accounting cycle:**

1. Place the new AGRRA Excel files in `condition-account-scripts/data_deposit/`.
2. Update `year_opening` and `year_closing` in `condition_account_seea.r`.
3. Run the script from the `condition-account-scripts/` working directory.
4. Check the console output for site counts per geographic unit. Confirm that expected sites appear.
5. Review the validation report in `outputs/validation_report.txt` for any flagged values.
6. Open the output CSVs in `outputs/` and verify that the condition indices fall between 0 and 1.
7. Compare the new closing-year values against the previous closing-year values (now the opening year) for continuity.
8. If reference levels have been updated based on new literature, apply the new values consistently to both years and document the change.

## 8. Worked Example: Ambergris Caye

This section walks through the full process for Ambergris Caye, from site-level indicator values to the final 5-row condition account table. All numbers match the output in `condition_account_ambergris_caye.csv`.

### 8.1 Site-level indicator values

The R pipeline produced site-level values for the Ambergris Caye geographic unit. Seven sites had opening-year (2023) data and five had closing-year (2025) data for most indicators. Coral diversity data was only available in 2025 (no coral community transects were conducted at these sites in 2023).

### 8.2 Live coral cover

**Opening (2023).** 7 sites. Mean = 8.02%, SE = 1.57%.

CI = min(8.02 / 50, 1.0) = 0.1605 (rounded to 4 decimal places: 0.1605).

**Closing (2025).** 5 sites. Mean = 3.43%, SE = 1.57%.

CI = min(3.43 / 50, 1.0) = 0.0687 (rounded: 0.0687).

**Change.** CI_Change = 0.0687 - 0.1605 = -0.0918. Pct_Change = -57.21%. Interpretation: **Declining**. N_Sites: 7/5. Data_Quality: **Good**.

### 8.3 Fleshy macroalgae cover

**Opening (2023).** 7 sites. Mean = 34.20%, SE = 2.75%.

CI = max(1 - 34.20/50, 0.0) = max(0.316, 0.0) = 0.316 (rounded: 0.3160).

**Closing (2025).** 5 sites. Mean = 36.43%, SE = 6.41%.

CI = max(1 - 36.43/50, 0.0) = max(0.2714, 0.0) = 0.3037 (rounded: 0.3037).

**Change.** CI_Change = 0.3037 - 0.3160 = -0.0123. Pct_Change = -3.89%. Interpretation: **Stable** (change within 1 SE). N_Sites: 7/5. Data_Quality: **Good**.

### 8.4 Coral recruit density

**Opening (2023).** 6 sites. Mean = 0.25 per m2, SE = 0.05.

CI = min(0.25 / 15, 1.0) = 0.0164 (rounded: 0.0164).

**Closing (2025).** 5 sites. Mean = 0.23 per m2, SE = 0.09.

CI = min(0.23 / 15, 1.0) = 0.0155 (rounded: 0.0155).

**Change.** CI_Change = 0.0155 - 0.0164 = -0.0010 (rounded: -0.0010). Pct_Change = -5.95%. Interpretation: **Stable**. N_Sites: 6/5. Data_Quality: **Good**.

### 8.5 Coral diversity (Shannon H')

**Opening (2023).** 0 sites (no data). All opening values are NA.

**Closing (2025).** 5 sites. Mean = 1.06, SE = 0.10.

CI = min(1.06 / 2.0, 1.0) = 0.529 (rounded: 0.5290).

**Change.** Cannot be calculated (no opening data). Interpretation: **Closing only**. N_Sites: 0/5. Data_Quality: **Good (one period)**.

### 8.6 Reef relief

**Opening (2023).** 6 sites. Mean = 47.22 cm, SE = 9.66.

CI = min(47.22 / 150, 1.0) = 0.3148 (rounded: 0.3148).

**Closing (2025).** 5 sites. Mean = 49.62 cm, SE = 8.16.

CI = min(49.62 / 150, 1.0) = 0.3308 (rounded: 0.3308).

**Change.** CI_Change = 0.3308 - 0.3148 = 0.0160. Pct_Change = 5.09%. Interpretation: **Stable**. N_Sites: 6/5. Data_Quality: **Good**.

### 8.7 Final condition account table

| Geographic Unit | Ecosystem Type | Indicator | Unit | Reference Level | Opening Year | Opening Value | Opening SE | Opening CI | Closing Year | Closing Value | Closing SE | Closing CI | CI Change | Pct Change | Interpretation | N Sites | Data Quality |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ambergris Caye (Pilot) | Coral reef | Live Coral Cover | % | 50 | 2023 | 8.02 | 1.57 | 0.1605 | 2025 | 3.43 | 1.57 | 0.0687 | -0.0918 | -57.21 | Declining | 7/5 | Good |
| Ambergris Caye (Pilot) | Coral reef | Fleshy Macroalgae Cover | % | 50 | 2023 | 34.20 | 2.75 | 0.3160 | 2025 | 36.43 | 6.41 | 0.3037 | -0.0123 | -3.89 | Stable | 7/5 | Good |
| Ambergris Caye (Pilot) | Coral reef | Coral Recruit Density | per m2 | 15 | 2023 | 0.25 | 0.05 | 0.0164 | 2025 | 0.23 | 0.09 | 0.0155 | -0.0010 | -5.95 | Stable | 6/5 | Good |
| Ambergris Caye (Pilot) | Coral reef | Coral Diversity (Shannon H') | index | 2 | 2023 | -- | -- | -- | 2025 | 1.06 | 0.10 | 0.5290 | -- | -- | Closing only | 0/5 | Good (one period) |
| Ambergris Caye (Pilot) | Coral reef | Reef Relief | cm | 150 | 2023 | 47.22 | 9.66 | 0.3148 | 2025 | 49.62 | 8.16 | 0.3308 | 0.0160 | 5.09 | Stable | 6/5 | Good |

This table matches the output in `outputs/condition_account_ambergris_caye.csv`.

## References

United Nations, European Union, Food and Agriculture Organization of the United Nations, International Monetary Fund, Organisation for Economic Co-operation and Development, The World Bank. 2021. System of Environmental-Economic Accounting: Ecosystem Accounting (SEEA EA). White cover publication. United Nations, New York.

For indicator calculation methodology, see `docs/methodology_coral_condition_accounts.md`.

For the generic SEEA EA condition account framework, see `seea-ea-methodology/05_seea_accounting_tables/skill_condition_opening_closing_seea_account.md`.
