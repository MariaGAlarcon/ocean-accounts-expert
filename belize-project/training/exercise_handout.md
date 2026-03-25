# Exercise: Building a Condition Account for Hol Chan Marine Reserve

## Context

Hol Chan Marine Reserve is located at the southern end of Ambergris Caye in the Northern Barrier Complex. Four AGRRA survey sites were monitored in both 2023 and 2025: BZHCCD01, BZHCCD02, BZ1231, and BZ1077. Your task is to compile a SEEA EA condition account for these 4 sites using the indicator values from the R pipeline.

## Reference Levels

| Indicator | Reference level | Unit | Direction |
|---|---|---|---|
| Live coral cover | 50 | % | Higher is better |
| Fleshy macroalgae cover | 50 | % | Higher is worse |
| Coral recruit density | 15 | per m2 | Higher is better |
| Coral diversity (H') | 2.0 | index | Higher is better |
| Reef relief | 150 | cm | Higher is better |

## Part 1: Normalize Site-Level Values (pen and paper)

The table below shows the site-level indicator values for live coral cover. Calculate the condition index for each site using the formula:

CI = min(value / reference, 1.0)

| Site | Year | Live Coral Cover (%) | CI (your calculation) |
|---|---|---|---|
| BZHCCD01 | 2023 | 8.55 | |
| BZHCCD02 | 2023 | 6.17 | |
| BZ1231 | 2023 | 11.33 | |
| BZ1077 | 2023 | 5.83 | |
| BZHCCD01 | 2025 | 2.10 | |
| BZHCCD02 | 2025 | 1.50 | |
| BZ1231 | 2025 | 5.80 | |
| BZ1077 | 2025 | 3.25 | |

Now do the same for fleshy macroalgae cover. Remember, this indicator uses the inverted formula:

CI = max(1 - value / reference, 0.0)

| Site | Year | Fleshy Macroalgae Cover (%) | CI (your calculation) |
|---|---|---|---|
| BZHCCD01 | 2023 | 28.63 | |
| BZHCCD02 | 2023 | 32.50 | |
| BZ1231 | 2023 | 30.10 | |
| BZ1077 | 2023 | 38.45 | |
| BZHCCD01 | 2025 | 40.15 | |
| BZHCCD02 | 2025 | 28.30 | |
| BZ1231 | 2025 | 32.50 | |
| BZ1077 | 2025 | 45.20 | |

## Part 2: Aggregate Across Sites (pen and paper)

Using your site-level values for live coral cover, calculate the mean and standard error for each year.

**Opening year (2023), 4 sites:**

Sum of values: ________ + ________ + ________ + ________ = ________

Mean = sum / 4 = ________

Standard deviation = ________

SE = SD / sqrt(4) = SD / 2 = ________

**Closing year (2025), 4 sites:**

Sum of values: ________ + ________ + ________ + ________ = ________

Mean = sum / 4 = ________

Standard deviation = ________

SE = SD / sqrt(4) = SD / 2 = ________

**Normalize the means:**

Opening CI = min(opening mean / 50, 1.0) = ________

Closing CI = min(closing mean / 50, 1.0) = ________

**Calculate change:**

CI Change = Closing CI - Opening CI = ________

SE of CI (opening) = Opening SE / 50 = ________

SE of CI (closing) = Closing SE / 50 = ________

SE threshold = average of the two SE of CI values = ________

Is |CI Change| greater than the SE threshold?  Yes / No

Interpretation (circle one):  Improving  /  Stable  /  Declining

## Part 3: Complete the Condition Account in Excel

Open the exercise workbook (`exercise_workbook.xlsx`). The Site_Data sheet has all indicator values pre-loaded. Use the Your_Calculations sheet to complete the full condition account for all 5 indicators.

For each indicator, calculate:

1. Opening and closing mean values (across the 4 sites)
2. Opening and closing standard errors
3. Opening and closing condition indices
4. CI change and percent change
5. Interpretation (Stable, Improving, or Declining)
6. Data quality rating

Transfer your results to the Condition_Account sheet.

## Part 4: Questions

Note: The current exercise covers five indicators. A sixth indicator, coral bleaching prevalence, has been added to the pipeline and will be included in future exercises once validated.

Answer these after completing the exercise.

1. Which indicator showed the largest absolute decline in condition index?

2. Which indicators are classified as Stable? Why?

3. Why does coral diversity have no opening-year data?

4. The data quality rating for all indicators is Moderate. What would need to change to achieve a Good rating?

5. If the reference level for live coral cover were lowered from 50% to 30%, what would the opening CI become? Would the interpretation change?
