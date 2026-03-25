# =============================================================================
# indicator_calculation_annotated.r
# =============================================================================
# PURPOSE: Entry point for the GOAP indicator calculation pipeline. Calculates
# five condition indicators from validated AGRRA data: live coral cover, fleshy
# macroalgae cover, recruit density, coral diversity, and reef relief.
#
# ORIGINAL SOURCE: GOAP-condition-account-belize repository
#
# OVERVIEW OF CHANGES NEEDED:
# - Lines 10-11: The organism taxonomy categories differ between test mode and
#   real data mode, controlled by a conditional. This is fragile because it
#   couples test infrastructure to production logic. A config parameter or
#   lookup table would be more robust.
# - This script produces summary statistics (min, mean, median, max) per year
#   across all sites, but does not produce condition indices. For SEEA EA
#   compliance, additional steps are required: reference levels, normalization
#   to condition indices (0 to 1), spatial aggregation by geographic unit,
#   standard error calculation, and opening/closing change analysis.
# - Year is extracted from survey dates using format(as.Date(Date), "%Y").
#   This works but is less reliable than the batch-to-year lookup available
#   in AGRRA metadata sheet 2, which explicitly maps each batch to a year.
#
# See feedback_report.md for full discussion of what is missing for SEEA EA.
# =============================================================================

# Set boolean for whether test data or AGRRA data should be used ---------------------------
test_on <- FALSE

# Source scripts ---------------------------
source("data_validation.r")

# Set vectors ---------------------------
# [FEEDBACK] CONDITIONAL TAXONOMY CATEGORIES
# The organism category strings differ between test data and real AGRRA data.
# Test data uses simplified category names ("Coral", "Fleshy Macroalgae")
# while real AGRRA exports use hierarchical names ("Calcifiers :: Coral",
# "Algae :: Macro :: Fleshy"). This conditional works but is easy to break
# if new data sources use different naming. A better approach would be a
# config file or lookup table that maps data source to taxonomy categories:
#   taxonomy_config <- list(
#       agrra = list(coral = "Calcifiers :: Coral", algae = "Algae :: Macro :: Fleshy"),
#       test  = list(coral = "Coral", algae = "Fleshy Macroalgae")
#   )
coral_category <- ifelse(test_on == TRUE, "Coral", "Calcifiers :: Coral")
algae_category <- ifelse(test_on == TRUE, "Fleshy Macroalgae", "Algae :: Macro :: Fleshy")

# Prepare data ---------------------------
df_organisms_unique <- df_organisms %>% distinct(Code, Type)
benthic_cover_presence <- df_benthic_cover %>%
    left_join(df_organisms_unique %>% select(Code, Primary_Type = Type), by = c("Organism" = "Code")) %>%
    left_join(df_organisms_unique %>% select(Code, Secondary_Type = Type), by = c("Secondary" = "Code")) %>%
    mutate(
        Coral_Presence = Vectorize(calculate_type_presence)(Primary_Type, Secondary_Type, coral_category),
        Algae_Presence = Vectorize(calculate_type_presence)(Primary_Type, Secondary_Type, algae_category),
        Year = format(as.Date(Date), format = "%Y")
    )

# Calculate live coral cover ---------------------------
benthic_cover_presence_lcc <- benthic_cover_presence %>%
    group_by(Year, Site, Transect) %>%
    mutate(Coral_Cover_Tran = 100 * sum(Coral_Presence) / n()) %>%
    group_by(Year, Site) %>%
    mutate(Coral_Cover_Site = mean(Coral_Cover_Tran))
indicator_lcc <- benthic_cover_presence_lcc %>%
    group_by(Year) %>%
    summarize(
        `Min (Site)` = min(Coral_Cover_Site),
        `Av. (Site)` = mean(Coral_Cover_Site),
        `Median (Site)` = median(Coral_Cover_Site),
        `Max (Site)` = max(Coral_Cover_Site),
        `Min (Transect)` = min(Coral_Cover_Tran),
        `Av. (Transect)` = mean(Coral_Cover_Tran),
        `Median (Transect)` = median(Coral_Cover_Tran),
        `Max (Transect)` = max(Coral_Cover_Tran)
    ) %>%
    mutate(across(-Year, ~ round(.x, 2)))

# [FEEDBACK] OUTPUT IS SUMMARY STATS ONLY
# The indicator_lcc table above summarizes coral cover across all sites and
# transects for each year, but does not retain site-level values needed for:
# - Condition index normalization (CI = value / reference_level)
# - Standard error calculation (SE = sd / sqrt(n))
# - Geographic unit aggregation (mean across sites within an MPA/subregion)
# - Opening/closing comparison (matching sites across years)
# The intermediate benthic_cover_presence_lcc dataframe retains site-level
# values, but the pipeline does not carry these forward into a structured
# output. The SEEA EA extension script (condition_account_seea.r) addresses
# this by keeping site-level indicator values throughout.

# Calculate macroalgae cover ---------------------------
benthic_cover_presence_fma <- benthic_cover_presence %>%
    group_by(Year, Site, Transect) %>%
    mutate(Algae_Cover_Tran = 100 * sum(Algae_Presence) / n()) %>%
    group_by(Year, Site) %>%
    mutate(Algae_Cover_Site = mean(Algae_Cover_Tran))
indicator_fma <- benthic_cover_presence_fma %>%
    group_by(Year) %>%
    summarize(
        `Min (Site)` = min(Algae_Cover_Site),
        `Av. (Site)` = mean(Algae_Cover_Site),
        `Median (Site)` = median(Algae_Cover_Site),
        `Max (Site)` = max(Algae_Cover_Site),
        `Min (Transect)` = min(Algae_Cover_Tran),
        `Av. (Transect)` = mean(Algae_Cover_Tran),
        `Median (Transect)` = median(Algae_Cover_Tran),
        `Max (Transect)` = max(Algae_Cover_Tran)
    ) %>%
    mutate(across(-Year, ~ round(.x, 2)))

# Calculate recruit density ---------------------------
benthic_recruits_rd <- df_recruits %>%
    mutate(Year = format(as.Date(Date), format = "%Y")) %>%
    group_by(Year, Date, Site) %>%
    complete(Transect, Quadrat = 1:4, fill = list(Num = 0, Size = NA_character_)) %>%
    group_by(Year, Date, Site, Transect, Quadrat) %>%
    summarize(
        Recruits = sum(Num, na.rm = TRUE),
        `Small Recruits` = sum(Num[Size == "SR"], na.rm = TRUE),
        `Large Recruits` = sum(Num[Size == "LR"], na.rm = TRUE)
    ) %>%
    group_by(Year, Date, Site) %>%
    summarize( # calculate density per meter
        All = sum(Recruits) / 25,
        Small = sum(`Small Recruits`) / 25,
        Large = sum(`Large Recruits`) / 25
    )

# [FEEDBACK] QUADRAT INDEXING
# The complete() call above fills quadrats 1:4, assuming AGRRA uses 1-based
# quadrat indexing. The actual AGRRA data uses 0-based indexing (quadrats 0
# through 4, giving 5 quadrats per transect). The SEEA EA extension uses
# Quadrat = 0:4 to match the AGRRA export format. Check the raw data to
# confirm which indexing convention applies before running.

indicator_rd <- benthic_recruits_rd %>%
    pivot_longer(cols = 4:6, names_to = "Size", values_to = "Value") %>%
    group_by(Year, Size) %>%
    summarize(
        Min = min(Value),
        `Av.` = mean(Value),
        Median = median(Value),
        Max = max(Value)
    ) %>%
    mutate(across(-Size, ~ round(.x, 2)))

# Calculate live coral diversity ---------------------------
coral_community_cd <- df_coral_community %>%
    mutate(Year = format(as.Date(Date), format = "%Y")) %>%
    filter(!is.na(Organism), Organism != "") %>%
    group_by(Year, Date, Site, Transect, Organism) %>%
    summarize(
        Abundance = n(),
    ) %>%
    group_by(Year, Date, Site, Transect) %>%
    mutate(
        p_i = Abundance / sum(Abundance) # relative abundance
    ) %>%
    summarize(
        Diversity = -sum(p_i * log(p_i), na.rm = TRUE),
        Richness = n_distinct(Organism),
    ) %>%
    group_by(Year, Date, Site) %>%
    summarize(
        Diversity = mean(Diversity, na.rm = TRUE),
        Richness = mean(Richness, na.rm = TRUE),
    )
indicator_cd <- coral_community_cd %>%
    group_by(Year, Site) %>%
    summarize(
        Diversity = mean(Diversity, na.rm = TRUE),
        Richness = mean(Richness, na.rm = TRUE),
    ) %>%
    pivot_longer(
        cols = c(Diversity, Richness),
        names_to = "Metric",
        values_to = "Value"
    ) %>%
    group_by(Year, Metric) %>%
    summarize(
        Min = min(Value, na.rm = TRUE),
        `Av.` = mean(Value, na.rm = TRUE),
        Median = median(Value, na.rm = TRUE),
        Max = max(Value, na.rm = TRUE)
    ) %>%
    mutate(across(where(is.numeric), ~ round(.x, 2)))

# Calculate max relief ---------------------------
fish_relief <- df_fish %>%
    mutate(Year = format(as.Date(Date), format = "%Y")) %>%
    group_by(Year, Site) %>%
    summarize(Relief_Site = mean(Max_Relief, na.rm = TRUE))
indicator_relief <- fish_relief %>%
    group_by(Year) %>%
    summarize(
        `Min (Site)` = min(Relief_Site),
        `Av. (Site)` = mean(Relief_Site),
        `Median (Site)` = median(Relief_Site),
        `Max (Site)` = max(Relief_Site)
    ) %>%
    mutate(across(-Year, ~ round(.x, 2)))

# [FEEDBACK] MISSING SEEA EA STEPS
# This script ends after producing summary statistics per indicator per year.
# The following steps are required to produce a SEEA EA condition account but
# are not implemented here:
#
# 1. Reference levels: Define a benchmark for each indicator (e.g., 50% for
#    coral cover, 2.0 for Shannon H'). See methodology document Section 4.4.
#
# 2. Condition index normalization: For each site, divide the measured value
#    by the reference level (higher-is-better) or compute 1 - value/reference
#    (higher-is-worse). Cap at 0 and 1.
#
# 3. Geographic unit definitions: Assign sites to MPAs, subregions, or other
#    reporting units. The AGRRA metadata does not include an MPA field, so
#    this must be done manually or from coordinates.
#
# 4. Spatial aggregation: Calculate mean and standard error of each indicator
#    across sites within each geographic unit, for each year.
#
# 5. Opening/closing comparison: Match sites across years, compute change in
#    condition index, interpret as Stable/Improving/Declining.
#
# 6. Data quality rating: Assess sample size per geographic unit and assign
#    Good/Moderate/Limited ratings.
#
# These steps are implemented in condition_account_seea.r.
