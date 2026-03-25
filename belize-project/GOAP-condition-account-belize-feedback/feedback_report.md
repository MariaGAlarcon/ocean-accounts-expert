# Feedback on GOAP Belize Coral Condition Account Scripts

## 1. Purpose

The GOAP condition account scripts (`data_restructuring.r`, `data_validation.r`, `indicator_calculation.r`, and supporting helper scripts) were developed to process AGRRA (Atlantic and Gulf Rapid Reef Assessment) field survey data from Belize into five coral reef condition indicators. These scripts formed the calculation engine for the Belize coral reef condition accounts produced under the Global Ocean Accounts Partnership.

The scripts processed four AGRRA Excel export files (BenthicRaw.xlsx, CoralRaw.xlsx, FishRaw.xlsx, Metadata.xlsx) covering 169 survey sites across six subregions of the Belize Barrier Reef system. This feedback describes how the scripts performed when applied to real AGRRA data and what extensions were required to produce formal SEEA EA condition account tables.

## 2. What Worked Well

The following components worked correctly on real AGRRA data and required no modification.

**Co-dominance weighting function.** The `calculate_type_presence()` function in `functions_define.r` (lines 10 to 20) correctly assigns weighted presence scores for benthic cover observations where two organisms share a substrate point. The logic handles all four cases (sole primary, co-dominant same type, co-dominant different type, absent) and was reused without changes in the extended pipeline.

**AGRRA Excel sheet reading logic.** The `read_excel()` calls in `data_restructuring.r` (lines 17 to 31) correctly identify which sheets to read and where to apply `skip = 1` to handle AGRRA's merged header rows. The sheet numbering and skip values matched the actual AGRRA export format.

**Benthic cover calculation.** The live coral cover and fleshy macroalgae cover calculations in `indicator_calculation.r` (lines 15 to 62) correctly apply the co-dominance weighting, aggregate from point level to transect level to site level, and produce percentage cover values. The formulas match the AGRRA protocol.

**Coral diversity calculation.** The Shannon diversity index calculation (lines 93 to 131) correctly computes H' = -sum(p_i * log(p_i)) per transect, then averages across transects per site. Species richness is tracked alongside diversity.

**Package management.** The `packages_load.r` script auto-installs missing packages, which simplifies setup for new users. The dependency list (tidyverse, knitr, readxl) is minimal and appropriate.

**Validation framework.** The validation functions (`check_completeness`, `check_grouping`, `check_range`, `check_date`, `check_time`) in `functions_define.r` are well-structured and produce clear, actionable messages. The validation report output is useful for diagnosing data quality issues.

## 3. What Needed Adapting

The table below summarizes areas where the original scripts were too rigid for processing the full AGRRA dataset across all subregions.

| Issue | Script | Lines | Problem | How it was resolved |
|---|---|---|---|---|
| Hardcoded subregion filter | `data_restructuring_annotated.r` | 43, 58, 79, 98, 118, 140 | Six `filter(Subregion == "Northern Barrier Complex")` calls discard all data outside this one subregion. The full AGRRA dataset covers 6 subregions and 169 sites. | The SEEA EA extension script removed all subregion filters and processes the entire dataset. Geographic filtering is applied later when building accounts per geographic unit. |
| Hardcoded site code list | `data_validation_annotated.r` | 43 | `values_site_codes` contains 11 codes specific to the Northern Barrier Complex pilot. Any site not in this list triggers a validation failure. The real dataset has 169 unique sites. | Site codes were derived dynamically from the data: `values_site_codes <- unique(df_sites$Site)`. This validates internal consistency (all downstream tables reference sites that exist in the sites table) without rejecting legitimate new sites. |
| Hardcoded MPA name list | `data_validation_annotated.r` | 44 | `values_mpa_names` is validated against `df_sites$MPA_Management`, but that column is set to NA in `data_restructuring.r`. The check passes vacuously. | MPA assignments were handled separately in the SEEA EA extension using coordinate-based and name-based matching. The validation check was not needed. |
| Year extraction from dates | `indicator_calculation_annotated.r` | 21 | Year is extracted from survey dates using `format(as.Date(Date), "%Y")`. This works for most cases but misses the explicit batch-to-year mapping available in AGRRA metadata sheet 2. | The SEEA EA extension uses the Batch table (metadata sheet 2) to map each survey to a year. This is more reliable because some surveys span December/January boundaries, and the batch assignment reflects the intended campaign year. |
| Recruit density quadrat indexing | `indicator_calculation_annotated.r` | 68 | The `complete()` call fills quadrats 1 through 4 (1-based indexing). The actual AGRRA export uses 0-based indexing with quadrats 0 through 4, giving 5 quadrats per transect. | The SEEA EA extension uses `Quadrat = 0:4` to match the AGRRA export format. |
| Summary-only output | `indicator_calculation_annotated.r` | 30 to 42, 50 to 62, etc. | Indicator outputs are aggregated to year-level summary statistics (min, mean, median, max across all sites). Site-level values, which are needed for normalization and geographic aggregation, are not retained as a structured output. | The SEEA EA extension retains site-level indicator values in a combined dataframe (`indicators_site`) keyed by Year and Site, which feeds into normalization and aggregation. |

## 4. What Was Missing for SEEA EA Accounts

The original scripts calculate raw indicator values but stop short of producing SEEA EA condition accounts. The following components were required and implemented in the extension script (`condition_account_seea.r`).

**Reference levels.** SEEA EA condition accounts normalize each indicator to a 0 to 1 scale by comparing measured values against a reference level representing healthy or pre-degradation condition. The original scripts have no reference level definitions. Five reference levels were established from peer-reviewed Caribbean literature (see `docs/methodology_coral_condition_accounts.md`, Section 4.4).

**Condition index normalization.** For each site and indicator, the measured value is divided by the reference level (higher-is-better indicators) or computed as 1 - value/reference (higher-is-worse indicators), capped at 0 and 1. This step converts raw measurements to comparable condition indices.

**Geographic unit definitions.** Sites must be grouped into reporting units (MPAs, subregions, national) for aggregation. The AGRRA metadata does not include an MPA field. The SEEA EA extension defines geographic units by manually assigning sites to MPAs using coordinate proximity, site code prefixes, and site names.

**Spatial aggregation with uncertainty.** For each geographic unit, the mean and standard error of each indicator are calculated across sites. The standard error propagates to the condition index as SE_CI = SE_measured / reference_level.

**Opening/closing comparison.** The condition account compares two time periods (opening year 2023, closing year 2025). Change is classified as Stable, Improving, or Declining based on whether the absolute change in condition index exceeds one standard error.

**Data quality rating.** Each geographic unit receives a quality rating based on the number of matched sites: Good (5 or more), Moderate (3 to 4), or Limited (2 or fewer).

## 5. Recommendations

The following changes would make the GOAP scripts more reusable for future AGRRA campaigns and for other countries adapting this pipeline.

1. **Make the subregion filter a configurable parameter.** Add a variable at the top of `data_restructuring.r` (e.g., `target_subregion <- NULL` for all, or `"Northern Barrier Complex"` for the pilot) and apply it conditionally in each filter call. This avoids 6 separate hardcoded filters and lets users process any subset of the data without editing the script body. See `data_restructuring_annotated.r`, lines 43, 58, 79, 98, 118, 140.

2. **Derive site codes and MPA names from the data.** Replace the hardcoded `values_site_codes` and `values_mpa_names` vectors in `data_validation.r` (lines 43 to 44) with dynamic lookups from the restructured data. For site codes: `values_site_codes <- unique(df_sites$Site)`. This validates internal consistency without rejecting new sites. For MPA names: either populate the MPA field upstream or remove the check.

3. **Add a batch-to-year lookup from metadata sheet 2.** The AGRRA metadata includes a Batch table with explicit Year values per batch. Reading this table and joining it to surveys by Batch ID produces more reliable year assignments than extracting years from survey dates. This is especially relevant when surveys span a December/January boundary.

4. **Retain site-level indicator values as a structured output.** The current pipeline aggregates indicators to year-level summaries and discards site-level detail. Adding a step that writes a site-level CSV (Year, Site, Live_Coral_Cover, Fleshy_Macroalgae_Cover, Recruit_Density, Coral_Diversity_H, Reef_Relief) would make it straightforward to add normalization and aggregation as a downstream step without rewriting the indicator calculations.

5. **Replace the test_on conditional taxonomy with a config parameter.** The `ifelse(test_on == TRUE, "Coral", "Calcifiers :: Coral")` pattern on lines 10 to 11 of `indicator_calculation.r` ties production logic to test infrastructure. A taxonomy config table or parameter file would separate these concerns and make it easier to adapt the scripts for AGRRA exports from other countries that may use different category naming conventions.

6. **Confirm quadrat indexing convention before running.** The `complete()` call in the recruit density calculation should use `Quadrat = 0:4` for standard AGRRA exports (0-based) or `Quadrat = 1:4` for the GOAP template format (1-based). Document which convention applies and make it a parameter.

7. **Document what is in scope and out of scope.** The original scripts are clearly designed to calculate indicators, not to produce condition accounts. Adding a comment block at the end of `indicator_calculation.r` noting that normalization, aggregation, and account table assembly are separate steps would set expectations for anyone extending the pipeline.

## 6. Key Indicator Additions for SEEA EA Alignment

The current pipeline calculates five indicators from AGRRA data. The SEEA EA coral reef condition framework identifies several additional standard indicators that the AGRRA dataset can support. These should be prioritized for future accounting periods.

**Coral bleaching prevalence.** The CoralRaw data includes colony-level bleaching and paling percentages. Bleaching prevalence (proportion of colonies showing bleaching signs) is a standard SEEA EA indicator that tracks thermal stress. It was not included in the original pipeline because the coral community data was used only for diversity calculations. An extension to the pipeline has been added in `condition_account_seea.r` to calculate this indicator. Reference level: 100% (theoretical maximum, inverted normalization).

**Fish biomass.** The FishRaw data includes species, size, and count records from visual census transects. Fish biomass is a core SEEA EA biotic condition indicator and a direct input to fisheries provisioning and reef recreation service accounts. Calculating biomass requires applying published length-weight relationships (e.g., Bohnsack and Harper 1988, FishBase allometric parameters) to convert recorded fish lengths to biomass estimates. This conversion introduces additional uncertainty but is standard practice in Caribbean reef assessments.

**Dead coral cover.** The benthic point-intercept data distinguishes live coral from "Newly Dead" coral using the organism state field. Dead coral cover could be calculated using the same co-dominance weighting method as live coral cover, filtering for the "Newly Dead" state instead. This indicator tracks recent mortality distinct from the longer-term signal captured by live coral cover decline.

**Other AGRRA variables.** Coral disease prevalence (recorded alongside bleaching), invertebrate counts (lobster, conch, sea urchins from FishRaw), and turf algae cover (from benthic data) are all available. Invertebrate indicators connect to provisioning service accounts (lobster and conch fisheries). Turf algae and crustose coralline algae (CCA) cover provide more nuanced information about reef substrate dynamics than fleshy macroalgae alone.
