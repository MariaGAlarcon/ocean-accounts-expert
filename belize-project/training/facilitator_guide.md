# Compiling Coral Reef Condition Accounts: Workshop Guide

## Slide 1: Title

**Compiling Coral Reef Condition Accounts for Belize**

A practical workshop on turning field survey data into SEEA EA condition account tables.

*Speaker notes:* Welcome participants. This session teaches the steps between raw indicator values (produced by the R pipeline from AGRRA data) and the final condition account table. By the end, participants will be able to compile an account for any marine protected area or subregion.

## Slide 2: What is a condition account?

A condition account records the state of an ecosystem at two points in time.

For each indicator:

1. Measure a value at the opening year (e.g., 2023) and the closing year (e.g., 2025).
2. Compare each value against a reference level that represents a healthy reef.
3. The ratio gives a condition index between 0 and 1.
4. The change between periods tells us if the reef is improving, stable, or declining.

*Speaker notes:* Emphasize that the condition index is relative to the reference level, not absolute. A CI of 0.16 for coral cover means the reef has 16% of the healthy baseline. This makes different indicators comparable on the same 0 to 1 scale.

## Slide 3: The three steps

| Step | What you do | Input | Output |
|---|---|---|---|
| 1. Normalize | Convert each site value to a condition index | Site-level indicator values + reference levels | Condition index per site (0 to 1) |
| 2. Aggregate | Calculate mean and standard error across sites | Site-level CIs within a geographic unit | Geographic unit mean, SE, and CI |
| 3. Assemble | Build the condition account table | Opening and closing aggregates | SEEA EA table with change and interpretation |

*Speaker notes:* Draw this as a flow diagram on the board. The R pipeline handles everything up to producing site-level indicator values. This workshop covers what comes after.

## Slide 4: The six indicators

| Indicator | What it measures | Reference level | Direction |
|---|---|---|---|
| Live coral cover | % of reef with living coral | 50% | Higher is better |
| Fleshy macroalgae cover | % of reef with fleshy algae | 50% | Higher is worse |
| Coral recruit density | Juvenile corals per m2 | 15 per m2 | Higher is better |
| Coral diversity (H') | Shannon species diversity | 2.0 | Higher is better |
| Reef relief | Vertical reef height in cm | 150 cm | Higher is better |
| Coral bleaching prevalence | % of colonies with bleaching signs | 100% | Higher is worse |

*Speaker notes:* Explain that "higher is worse" for macroalgae means more algae = worse condition. The reference level of 50% represents near-total algal dominance. All other indicators follow "higher is better" logic. Bleaching prevalence uses the same inverted logic as macroalgae: more bleaching = worse condition. The reference of 100% is the theoretical maximum, so the CI directly tells you what proportion of the reef community is not bleaching.

## Slide 5: Normalization formulas

**For higher-is-better indicators:**

Condition Index = min(measured value / reference level, 1.0)

**For higher-is-worse indicators (macroalgae and bleaching):**

Condition Index = max(1 - measured value / reference level, 0.0)

The min() caps at 1.0 so values above the reference do not exceed 1. The max() prevents negative values.

*Speaker notes:* Write both formulas on the board. Explain the cap: if a site has 60% coral cover against a 50% reference, the CI is 1.0, not 1.2. We are measuring "how close to reference," not "how much above."

## Slide 6: Guided example, live coral cover

Let us work through one site together.

**Site BZHCCD01, Hol Chan Marine Reserve, 2023.**

Live coral cover = 8.55%. Reference level = 50%.

CI = min(8.55 / 50, 1.0) = min(0.171, 1.0) = **0.17**

This means the site has 17% of the reference coral cover.

*Speaker notes:* Ask participants to calculate this on paper or a calculator. Wait for them to get the answer before showing it. Ask: "Is this a healthy reef?" (No, it is far below the reference.)

## Slide 7: Guided example, macroalgae (inverted)

Same site, same year.

Fleshy macroalgae cover = 28.63%. Reference level = 50%.

CI = max(1 - 28.63 / 50, 0.0) = max(1 - 0.5726, 0.0) = **0.43**

This means the site is 43% of the way toward a reef free of macroalgae dominance.

*Speaker notes:* Walk through the inversion carefully. A reef with 0% macroalgae would score CI = 1.0 (best). A reef at 50% macroalgae scores CI = 0.0 (worst). At 28.63%, we are somewhere in between. Ask participants: "Would a higher macroalgae percentage give a higher or lower CI?" (Lower.)

## Slide 8: Aggregation

For each geographic unit, calculate the mean and standard error across sites.

**Mean** = sum of site values / N

**Standard error (SE)** = standard deviation / sqrt(N)

**SE of the condition index** = SE of the measured value / reference level

*Speaker notes:* If the audience is not comfortable with standard deviation, explain it as "how spread out the values are." The SE tells us how confident we are in the mean. With more sites, the SE gets smaller and our estimate gets more precise.

## Slide 9: Change and interpretation

**Absolute change** = Closing CI - Opening CI

**Percent change** = (change / Opening CI) x 100

**Interpretation rules:**

1. Calculate the SE threshold = average of opening and closing SE of the CI.
2. If the absolute change is smaller than the SE threshold: **Stable** (the change could be noise).
3. If the change is positive and exceeds the threshold: **Improving**.
4. If the change is negative and exceeds the threshold: **Declining**.

*Speaker notes:* The SE threshold is a simple way to distinguish real change from measurement noise. With only 4 sites, the SE is relatively large, so small changes will be classified as Stable. This is conservative, which is appropriate for policy use.

## Slide 10: Data quality rating

| Minimum sites (opening or closing) | Rating |
|---|---|
| 5 or more | Good |
| 3 to 4 | Moderate |
| 1 to 2 | Limited |

If data exists for only one period, append "(one period)" to the rating.

*Speaker notes:* Hol Chan has 4 sites in both years, so the rating will be Moderate. To reach Good, at least 5 matched sites are needed. This motivates expanding the survey network.

## Slide 11: Exercise time

You will now build a condition account for Hol Chan Marine Reserve using real survey data.

You have:

1. A printed handout with instructions and blank tables.
2. An Excel workbook with the site-level data pre-loaded.

Work through the handout first (pen and paper for the first indicator), then complete the rest in Excel.

You have 40 minutes. We will compare answers afterward.

*Speaker notes:* Circulate during the exercise. Common mistakes to watch for: forgetting to invert macroalgae, dividing by the wrong reference level, using population SD instead of sample SD. Encourage participants to check their CI values are between 0 and 1.

## Slide 12: Review

Show the answer key. Walk through each indicator.

**Discussion questions:**

1. Which indicator showed the largest decline at Hol Chan?
2. Why is coral diversity reported as "Closing only"?
3. What would improve the data quality rating from Moderate to Good?
4. If the reference level for coral cover were changed from 50% to 30%, how would the condition index change?

*Speaker notes:* For question 4, recalculate together: CI = min(8.02/30, 1.0) = 0.27 instead of 0.16. The reference level choice matters; this is why documenting the source and rationale is part of the methodology.

## Slide 13: Looking Ahead

**What comes next for Belize condition accounts**

Building on these five core indicators, future accounting periods should add:

1. Coral bleaching prevalence (code already added to the pipeline; validates against colony-level data)
2. Fish biomass (requires size-to-biomass conversion; connects directly to fisheries service accounts)
3. Dead coral cover (calculable from existing benthic data; tracks recent mortality)

These indicators connect condition accounts to ecosystem service accounts: fish biomass feeds fisheries and tourism valuations, bleaching prevalence tracks climate risk across all reef services, and dead coral cover signals acute degradation events.

The condition accounts are also designed to link with reef extent accounts (from satellite-derived reef maps) to produce complete ecosystem asset characterizations under SEEA EA.

*Speaker notes:* Emphasize that the accounts are not a one-off exercise. Each new survey campaign extends the time series and strengthens the change analysis. The five indicators established here form the foundation; the additional indicators and the extent linkage build toward a complete natural capital account for Belize's reefs.
