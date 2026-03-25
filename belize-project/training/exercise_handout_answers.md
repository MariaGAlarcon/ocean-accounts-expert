# Exercise Answers: Building a Condition Account for Hol Chan Marine Reserve

## Part 1: Normalize Site-Level Values

**Live coral cover** (higher is better, reference = 50%):

CI = min(value / 50, 1.0)

| Site | Year | Live Coral Cover (%) | CI |
|---|---|---|---|
| BZHCCD01 | 2023 | 8.55 | 0.17 |
| BZHCCD02 | 2023 | 6.17 | 0.12 |
| BZ1231 | 2023 | 11.33 | 0.23 |
| BZ1077 | 2023 | 5.83 | 0.12 |
| BZHCCD01 | 2025 | 2.10 | 0.04 |
| BZHCCD02 | 2025 | 1.50 | 0.03 |
| BZ1231 | 2025 | 5.80 | 0.12 |
| BZ1077 | 2025 | 3.25 | 0.07 |

**Fleshy macroalgae cover** (higher is worse, reference = 50%):

CI = max(1 - value / 50, 0.0)

| Site | Year | Fleshy Macroalgae Cover (%) | CI |
|---|---|---|---|
| BZHCCD01 | 2023 | 28.63 | 0.43 |
| BZHCCD02 | 2023 | 32.50 | 0.35 |
| BZ1231 | 2023 | 30.10 | 0.40 |
| BZ1077 | 2023 | 38.45 | 0.23 |
| BZHCCD01 | 2025 | 40.15 | 0.20 |
| BZHCCD02 | 2025 | 28.30 | 0.43 |
| BZ1231 | 2025 | 32.50 | 0.35 |
| BZ1077 | 2025 | 45.20 | 0.10 |

## Part 2: Aggregate Across Sites (Live Coral Cover)

**Opening year (2023), 4 sites:**

Sum of values: 8.55 + 6.17 + 11.33 + 5.83 = 31.88

Mean = 31.88 / 4 = **7.97**

Standard deviation: deviations from mean are 0.58, -1.80, 3.36, -2.14. Squared: 0.34, 3.24, 11.29, 4.58. Sum = 19.45. Variance = 19.45 / 3 = 6.48. SD = **2.55**

SE = 2.55 / sqrt(4) = 2.55 / 2 = **1.27**

**Closing year (2025), 4 sites:**

Sum of values: 2.10 + 1.50 + 5.80 + 3.25 = 12.65

Mean = 12.65 / 4 = **3.16**

Standard deviation: deviations from mean are -1.06, -1.66, 2.64, 0.09. Squared: 1.12, 2.76, 6.97, 0.01. Sum = 10.86. Variance = 10.86 / 3 = 3.62. SD = **1.90**

SE = 1.90 / sqrt(4) = 1.90 / 2 = **0.95**

**Normalize the means:**

Opening CI = min(7.97 / 50, 1.0) = **0.1594**

Closing CI = min(3.16 / 50, 1.0) = **0.0632**

**Calculate change:**

CI Change = 0.0632 - 0.1594 = **-0.0962**

SE of CI (opening) = 1.27 / 50 = **0.0254**

SE of CI (closing) = 0.95 / 50 = **0.0190**

SE threshold = (0.0254 + 0.0190) / 2 = **0.0222**

Is |CI Change| greater than the SE threshold? |-0.0962| = 0.0962 > 0.0222. **Yes.**

Interpretation: **Declining**

## Part 4: Questions

**1. Which indicator showed the largest absolute decline in condition index?**

Live coral cover, with a CI change of -0.0962. Fleshy macroalgae cover also declined (CI change of -0.0824), meaning algae increased and the inverted CI dropped.

**2. Which indicators are classified as Stable? Why?**

Coral recruit density (CI change = -0.0008) and reef relief (CI change = +0.0201). Both changes are smaller than their respective SE thresholds, meaning the observed change could be due to measurement variability rather than a real ecological shift.

**3. Why does coral diversity have no opening-year data?**

No coral community transects were conducted at these sites during the 2023 survey campaign. Coral community data was only collected in 2025. Without opening-year values, no change can be calculated, so the interpretation is "Closing only."

**4. The data quality rating for all indicators is Moderate. What would need to change to achieve a Good rating?**

At least 5 matched sites in both the opening and closing years. Hol Chan currently has 4 sites surveyed in both years. Adding one or more survey sites within the reserve boundary would bring the rating to Good.

**5. If the reference level for live coral cover were lowered from 50% to 30%, what would the opening CI become? Would the interpretation change?**

Opening CI = min(7.97 / 30, 1.0) = 0.2657 (instead of 0.1594). Closing CI = min(3.16 / 30, 1.0) = 0.1053. CI change = 0.1053 - 0.2657 = -0.1604. The decline is still large relative to the SE threshold, so the interpretation remains Declining. But the condition indices are higher (closer to 1) because the benchmark is less ambitious.

**Additional context.** A sixth indicator, coral bleaching prevalence, has been added to the pipeline. It uses the same inverted normalization as fleshy macroalgae: CI = max(1 - prevalence / 100, 0.0). The reference level of 100% means that the condition index directly represents the proportion of the reef community not showing bleaching signs.
