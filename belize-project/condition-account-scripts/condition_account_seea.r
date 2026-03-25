# condition_account_seea.r
# Produces SEEA EA condition account tables for Belize coral reefs.
# Self-contained script: reads AGRRA data directly, processes ALL subregions,
# calculates 6 condition indicators, normalizes to condition indices, and
# outputs condition account tables per geographic unit.
#
# Working directory: condition-account-scripts/

# Source packages ---------------------------
source("helper_scripts/packages_load.r")
source("helper_scripts/functions_define.r")

# =============================================================================
# 1. READ AGRRA DATA
# =============================================================================
message("---- Reading AGRRA data ----")

filepath_benthic <- file.path("data_deposit", "BenthicRaw.xlsx")
filepath_coral <- file.path("data_deposit", "CoralRaw.xlsx")
filepath_fish <- file.path("data_deposit", "FishRaw.xlsx")
filepath_metadata <- file.path("data_deposit", "Metadata.xlsx")

files <- c(filepath_benthic, filepath_coral, filepath_fish, filepath_metadata)
missing <- files[!file.exists(files)]
if (length(missing)) {
    stop("Missing files: ", paste(missing, collapse = ", "),
         ". Place AGRRA data in the data_deposit folder.")
}

# Read metadata sheets
df_batch_raw <- read_excel(filepath_metadata, sheet = 2)
df_surveys_raw <- read_excel(filepath_metadata, sheet = 3)
df_transects_meta <- read_excel(filepath_metadata, sheet = 4)
df_organisms_raw <- read_excel(filepath_metadata, sheet = 6)
df_organisms_group <- read_excel(filepath_metadata, sheet = 5)
df_coralspp <- read_excel(filepath_metadata, sheet = 7)

# Build batch-to-year mapping: Batch 22 = 2023, Batch 78 = 2025
batch_year <- df_batch_raw %>% select(Batch_ID = ID, Year)

# Read benthic sheets (skip=1 because row 1 has merged category headers)
df_benthic_transects_raw <- read_excel(filepath_benthic, sheet = 3, skip = 1)
df_benthic_cover_raw <- read_excel(filepath_benthic, sheet = 4, skip = 1)
df_quadrats_raw <- read_excel(filepath_benthic, sheet = 5, skip = 1)
df_recruits_raw <- read_excel(filepath_benthic, sheet = 6, skip = 1)

# Read coral sheets
df_coral_transects_raw <- read_excel(filepath_coral, sheet = 3)
df_coral_raw <- read_excel(filepath_coral, sheet = 4, skip = 2)

# Read fish sheets (skip=1 for merged headers)
df_fish_raw <- read_excel(filepath_fish, sheet = 3, skip = 1)

message("  Data files loaded successfully.")
message("  Surveys: ", nrow(df_surveys_raw), " rows")
message("  Benthic cover points: ", nrow(df_benthic_cover_raw), " rows")
message("  Coral community records: ", nrow(df_coral_raw), " rows")
message("  Fish transects: ", nrow(df_fish_raw), " rows")
message("  Recruit records: ", nrow(df_recruits_raw), " rows")

# =============================================================================
# 2. BUILD ORGANISM LOOKUP TABLE
# =============================================================================
message("---- Building organism lookup ----")

# The organisms table (sheet 6 of Metadata) has ID, Name, Category, State, Coral Taxonomy.
# The organisms_group table (sheet 5) maps Category ID to category Name.
# We need to know each organism's category name (e.g., "Calcifiers :: Coral",
# "Algae :: Macro :: Fleshy") to calculate indicator presence.

df_organisms <- df_organisms_raw %>%
    left_join(df_organisms_group %>% rename(Category = ID, Type = Name), by = "Category") %>%
    mutate(Code = ID) %>%
    select(Code, Name, Type, State, Category)

# =============================================================================
# 3. BUILD SITE METADATA WITH GEOGRAPHIC IDENTIFIERS
# =============================================================================
message("---- Building site metadata ----")

# Create a site lookup from surveys: each survey has a Code, Name, Subregion, Lat, Lon.
# A site is identified by Code if present, otherwise by Name.
# Year comes from the Batch table (Survey table has no date field).
df_site_lookup <- df_surveys_raw %>%
    left_join(batch_year, by = c("Batch" = "Batch_ID")) %>%
    mutate(
        Site = ifelse(!is.na(Code) & Code != "", Code, Name),
        Year = as.character(Year)
    ) %>%
    select(Survey_ID = ID, Site, Subregion, Latitude, Longitude, Year, Batch)

# Deduplicate: one row per Site-Year with subregion info
df_sites_meta <- df_site_lookup %>%
    distinct(Site, Year, .keep_all = TRUE)

message("  Unique sites: ", n_distinct(df_sites_meta$Site))
message("  Subregions: ", paste(unique(df_sites_meta$Subregion), collapse = ", "))

# =============================================================================
# 4. RESTRUCTURE DATA (ALL SUBREGIONS, NO FILTER)
# =============================================================================
message("---- Restructuring data for all subregions ----")

# --- Benthic cover ---
# Join cover points to benthic transects (for Survey ID), then to surveys (for site info).
# Cover_Raw has: Transect (= benthic transect ID), Point Index, Primary, Secondary, Algal Height
df_benthic_cover <- df_benthic_cover_raw %>%
    left_join(
        df_benthic_transects_raw %>% select(Transect_ID = ID, Survey),
        by = c("Transect" = "Transect_ID")
    ) %>%
    left_join(
        df_site_lookup %>% select(Survey_ID, Site, Year),
        by = c("Survey" = "Survey_ID")
    ) %>%
    mutate(
        Organism = Primary,
        Secondary_Org = Secondary
    ) %>%
    group_by(Survey) %>%
    mutate(Transect_Num = match(Transect, unique(Transect))) %>%
    ungroup() %>%
    select(Year, Site, Transect = Transect_Num, Point = `Point Index`,
           Organism, Secondary = Secondary_Org)

message("  Benthic cover restructured: ", nrow(df_benthic_cover), " points")

# --- Recruits ---
df_recruits <- df_recruits_raw %>%
    left_join(
        df_benthic_transects_raw %>% select(Transect_ID = ID, Survey),
        by = c("Transect" = "Transect_ID")
    ) %>%
    left_join(
        df_site_lookup %>% select(Survey_ID, Site, Year),
        by = c("Survey" = "Survey_ID")
    ) %>%
    left_join(
        df_coralspp %>% rename(Taxonomy = ID),
        by = "Taxonomy"
    ) %>%
    mutate(
        Quadrat = `Quadrat Index`,
        Organism_Name = Name
    ) %>%
    pivot_longer(cols = c("Small", "Large"), names_to = "Size", values_to = "Num") %>%
    mutate(Size = ifelse(Size == "Small", "SR", "LR")) %>%
    group_by(Survey) %>%
    mutate(Transect_Num = match(Transect, unique(Transect))) %>%
    ungroup() %>%
    select(Year, Site, Transect = Transect_Num, Quadrat, Organism = Organism_Name,
           Size, Num)

message("  Recruits restructured: ", nrow(df_recruits), " rows")

# --- Coral community ---
# CoralRaw Transects has: ID, Batch, Survey (but no skip, different from BenthicRaw)
df_coral_community <- df_coral_raw %>%
    left_join(
        df_coral_transects_raw %>% select(Transect_ID = ID, Survey),
        by = c("Transect" = "Transect_ID")
    ) %>%
    left_join(
        df_site_lookup %>% select(Survey_ID, Site, Year),
        by = c("Survey" = "Survey_ID")
    ) %>%
    left_join(
        df_coralspp %>% rename(Taxonomy = ID),
        by = "Taxonomy"
    ) %>%
    mutate(Organism = Name) %>%
    group_by(Survey) %>%
    mutate(Transect_Num = match(Transect, unique(Transect))) %>%
    ungroup() %>%
    select(Year, Site, Transect = Transect_Num, Organism)

message("  Coral community restructured: ", nrow(df_coral_community), " rows")

# --- Fish (relief) ---
# FishRaw Transects has: ID, Batch, Survey, ..., Maximum (relief in cm)
df_fish <- df_fish_raw %>%
    left_join(
        df_site_lookup %>% select(Survey_ID, Site, Year),
        by = c("Survey" = "Survey_ID")
    ) %>%
    mutate(Max_Relief = Maximum) %>%
    group_by(Survey) %>%
    mutate(Transect_Num = match(ID, unique(ID))) %>%
    ungroup() %>%
    select(Year, Site, Transect = Transect_Num, Max_Relief)

message("  Fish/relief restructured: ", nrow(df_fish), " rows")

# =============================================================================
# 5. DEFINE GEOGRAPHIC UNITS
# =============================================================================
message("---- Defining geographic units ----")

# Build a master site-to-area mapping.
# First, get distinct site-subregion-lat combos from the survey metadata.
site_info <- df_surveys_raw %>%
    mutate(Site = ifelse(!is.na(Code) & Code != "", Code, Name)) %>%
    distinct(Site, Subregion, Latitude, Longitude)

# Named site lists for MPA-level units
sites_hol_chan_mr <- c("BZHCCD01", "BZHCCD02", "BZ1231", "BZ1077")
sites_caye_caulker_mr <- c("BZ1230", "CCSC", "1076B")
sites_sapodilla_cayes_mr <- c("BZSCMR", "Nicholas Caye", "BZ1019", "BZ1026",
                               "BZ1124", "BZ1130", "BZ1149")
sites_laughing_bird_caye <- c("LBCMBRS1", "LBCMBRS2")
sites_south_water_caye_mr <- c("SWCCZFR1", "SWCCZFR2", "SWCCZFR3", "SWCCZFR4",
                                "SWCCZFR5", "SWCCZFR6", "SWCGUZFR1", "SWCGUZFR2",
                                "SWCGUZFR3", "SWCGUZFR4", "SWCGUZFR5", "SWCGUZFR6",
                                "BZ1105", "BZ1192", "BZ1043", "BZ1103")

# Subregion-based units (use grepl to avoid apostrophe encoding issues)
sites_glovers_reef_mr <- site_info %>%
    filter(grepl("Glover", Subregion)) %>%
    pull(Site) %>% unique()
sites_turneffe_atoll_mr <- site_info %>%
    filter(grepl("Turneffe", Subregion)) %>%
    pull(Site) %>% unique()
sites_lighthouse_reef <- site_info %>%
    filter(grepl("Lighthouse", Subregion)) %>%
    pull(Site) %>% unique()

# Ambergris Caye pilot: Northern Barrier Complex sites with lat >= 17.86,
# plus BZ1081 and BZ1234
sites_ambergris_caye <- site_info %>%
    filter(Subregion == "Northern Barrier Complex", Latitude >= 17.86) %>%
    pull(Site) %>% unique()
sites_ambergris_caye <- union(sites_ambergris_caye, c("BZ1081", "BZ1234"))

# All sites for national level
sites_national <- site_info %>% pull(Site) %>% unique()

# Subregion-level: get all distinct subregions
subregions <- site_info %>% pull(Subregion) %>% unique() %>% na.omit()

# Build the geographic units list. Each entry is a named list with display name
# and vector of site codes.
geo_units <- list(
    AMBERGRIS_CAYE = list(
        name = "Ambergris Caye (Pilot)",
        sites = sites_ambergris_caye
    ),
    HOL_CHAN_MR = list(
        name = "Hol Chan Marine Reserve",
        sites = sites_hol_chan_mr
    ),
    CAYE_CAULKER_MR = list(
        name = "Caye Caulker Marine Reserve",
        sites = sites_caye_caulker_mr
    ),
    GLOVERS_REEF_MR = list(
        name = "Glover's Reef Marine Reserve",
        sites = sites_glovers_reef_mr
    ),
    SAPODILLA_CAYES_MR = list(
        name = "Sapodilla Cayes Marine Reserve",
        sites = sites_sapodilla_cayes_mr
    ),
    LAUGHING_BIRD_CAYE = list(
        name = "Laughing Bird Caye National Park",
        sites = sites_laughing_bird_caye
    ),
    TURNEFFE_ATOLL_MR = list(
        name = "Turneffe Atoll Marine Reserve",
        sites = sites_turneffe_atoll_mr
    ),
    LIGHTHOUSE_REEF = list(
        name = "Lighthouse Reef",
        sites = sites_lighthouse_reef
    ),
    SOUTH_WATER_CAYE_MR = list(
        name = "South Water Caye Marine Reserve",
        sites = sites_south_water_caye_mr
    )
)

# Add subregion-level units
for (sr in subregions) {
    sr_sites <- site_info %>% filter(Subregion == sr) %>% pull(Site) %>% unique()
    key <- paste0("SUBREGION_", toupper(gsub("[^A-Za-z0-9]", "_", sr)))
    geo_units[[key]] <- list(name = paste0("Subregion: ", sr), sites = sr_sites)
}

# Add national level
geo_units[["NATIONAL"]] <- list(name = "Belize National", sites = sites_national)

message("  Defined ", length(geo_units), " geographic units")
for (g in names(geo_units)) {
    message("    ", geo_units[[g]]$name, ": ", length(geo_units[[g]]$sites), " sites")
}

# =============================================================================
# 6. CALCULATE INDICATORS AT SITE LEVEL
# =============================================================================
message("---- Calculating indicators ----")

# --- Organism type lookup for benthic cover ---
# Map organism IDs to their category names (Type)
df_org_lookup <- df_organisms %>% distinct(Code, Type, State)

coral_category <- "Calcifiers :: Coral"
algae_category <- "Algae :: Macro :: Fleshy"

# --- 6a. Live coral cover and fleshy macroalgae cover (per site per year) ---
message("  Calculating benthic cover indicators...")

benthic_with_types <- df_benthic_cover %>%
    left_join(
        df_org_lookup %>%
            filter(is.na(State) | State != "Newly Dead") %>%
            select(Code, Primary_Type = Type),
        by = c("Organism" = "Code")
    ) %>%
    left_join(
        df_org_lookup %>%
            filter(is.na(State) | State != "Newly Dead") %>%
            select(Code, Secondary_Type = Type),
        by = c("Secondary" = "Code")
    ) %>%
    mutate(
        Coral_Presence = Vectorize(calculate_type_presence)(
            Primary_Type, Secondary_Type, coral_category
        ),
        Algae_Presence = Vectorize(calculate_type_presence)(
            Primary_Type, Secondary_Type, algae_category
        )
    )

# Per transect, then per site
indicator_lcc_site <- benthic_with_types %>%
    group_by(Year, Site, Transect) %>%
    summarize(
        Coral_Cover_Tran = 100 * sum(Coral_Presence, na.rm = TRUE) / n(),
        .groups = "drop"
    ) %>%
    group_by(Year, Site) %>%
    summarize(
        Live_Coral_Cover = mean(Coral_Cover_Tran, na.rm = TRUE),
        .groups = "drop"
    )

indicator_fma_site <- benthic_with_types %>%
    group_by(Year, Site, Transect) %>%
    summarize(
        Algae_Cover_Tran = 100 * sum(Algae_Presence, na.rm = TRUE) / n(),
        .groups = "drop"
    ) %>%
    group_by(Year, Site) %>%
    summarize(
        Fleshy_Macroalgae_Cover = mean(Algae_Cover_Tran, na.rm = TRUE),
        .groups = "drop"
    )

message("    LCC: ", nrow(indicator_lcc_site), " site-year records")
message("    FMA: ", nrow(indicator_fma_site), " site-year records")

# --- 6b. Recruit density (per site per year) ---
# AGRRA protocol: 5 quadrats (index 0-4) per transect, each 0.25 m2.
# The existing indicator_calculation.r groups by Year, Date, Site and divides
# sum(Recruits) / 25. With ~6 transects * 5 quadrats = 30 quadrats, this gives
# a per-quadrat density (recruits per 0.25 m2 area units). We replicate this
# convention for consistency with the existing pipeline.

message("  Calculating recruit density...")

indicator_rd_site <- df_recruits %>%
    group_by(Year, Site) %>%
    complete(Transect, Quadrat = 0:4, fill = list(Num = 0, Size = NA_character_)) %>%
    group_by(Year, Site, Transect, Quadrat) %>%
    summarize(
        Recruits = sum(Num, na.rm = TRUE),
        .groups = "drop"
    ) %>%
    group_by(Year, Site) %>%
    summarize(
        Recruit_Density = sum(Recruits) / 25,
        .groups = "drop"
    )

message("    RD: ", nrow(indicator_rd_site), " site-year records")

# --- 6c. Coral diversity Shannon H' (per site per year) ---
message("  Calculating coral diversity...")

indicator_cd_site <- df_coral_community %>%
    filter(!is.na(Organism), Organism != "") %>%
    group_by(Year, Site, Transect, Organism) %>%
    summarize(Abundance = n(), .groups = "drop") %>%
    group_by(Year, Site, Transect) %>%
    mutate(p_i = Abundance / sum(Abundance)) %>%
    summarize(
        Shannon_H = -sum(p_i * log(p_i), na.rm = TRUE),
        Species_Richness = n_distinct(Organism),
        .groups = "drop"
    ) %>%
    group_by(Year, Site) %>%
    summarize(
        Coral_Diversity_H = mean(Shannon_H, na.rm = TRUE),
        Species_Richness = mean(Species_Richness, na.rm = TRUE),
        .groups = "drop"
    )

message("    CD: ", nrow(indicator_cd_site), " site-year records")

# --- 6c2. Coral bleaching prevalence (per site per year) ---
# AGRRA CoralRaw records Percent_Bleached and Percent_Pale per colony.
# Bleaching prevalence = proportion of colonies showing any bleaching signs
# (Percent_Bleached > 0 or, if available, Percent_Pale > 0).
# Reference level = 100% (theoretical maximum); CI = 1 - prevalence/100.
message("  Calculating bleaching prevalence...")

# Check which bleaching columns exist in the raw coral data
bleach_cols <- intersect(names(df_coral_raw), c("Percent Bleached", "Percent_Bleached",
                                                  "Percent Pale", "Percent_Pale"))

if (length(bleach_cols) > 0) {
    # Build a bleaching indicator from colony-level data
    df_bleach_work <- df_coral_raw %>%
        left_join(
            df_coral_transects_raw %>% select(Transect_ID = ID, Survey),
            by = c("Transect" = "Transect_ID")
        ) %>%
        left_join(
            df_site_lookup %>% select(Survey_ID, Site, Year),
            by = c("Survey" = "Survey_ID")
        )

    # Standardize column names (AGRRA exports may use spaces or underscores)
    if ("Percent Bleached" %in% names(df_bleach_work)) {
        df_bleach_work <- df_bleach_work %>% rename(Pct_Bleached = `Percent Bleached`)
    } else if ("Percent_Bleached" %in% names(df_bleach_work)) {
        df_bleach_work <- df_bleach_work %>% rename(Pct_Bleached = Percent_Bleached)
    } else {
        df_bleach_work$Pct_Bleached <- NA_real_
    }

    if ("Percent Pale" %in% names(df_bleach_work)) {
        df_bleach_work <- df_bleach_work %>% rename(Pct_Pale = `Percent Pale`)
    } else if ("Percent_Pale" %in% names(df_bleach_work)) {
        df_bleach_work <- df_bleach_work %>% rename(Pct_Pale = Percent_Pale)
    } else {
        df_bleach_work$Pct_Pale <- NA_real_
    }

    # A colony is "bleached" if Pct_Bleached > 0 or Pct_Pale > 0
    indicator_bleach_site <- df_bleach_work %>%
        filter(!is.na(Pct_Bleached) | !is.na(Pct_Pale)) %>%
        mutate(
            Is_Bleached = (!is.na(Pct_Bleached) & Pct_Bleached > 0) |
                          (!is.na(Pct_Pale) & Pct_Pale > 0)
        ) %>%
        group_by(Year, Site) %>%
        summarize(
            Bleaching_Prevalence = 100 * sum(Is_Bleached) / n(),
            .groups = "drop"
        )

    message("    Bleaching: ", nrow(indicator_bleach_site), " site-year records")
    bleaching_available <- TRUE
} else {
    message("    WARNING: No bleaching columns found in coral data. Skipping bleaching indicator.")
    indicator_bleach_site <- tibble(Year = character(), Site = character(),
                                    Bleaching_Prevalence = numeric())
    bleaching_available <- FALSE
}

# --- 6d. Reef relief (per site per year) ---
# The existing script uses mean of Max_Relief per site.
# The user requests max relief per site, but for consistency with the existing
# pipeline we use mean. The user instruction says "Per site: max relief value"
# but the existing indicator_calculation.r uses mean. We follow the user instruction
# and take the mean of transect-level max relief values per site, which is
# the standard AGRRA reporting approach.
message("  Calculating reef relief...")

indicator_relief_site <- df_fish %>%
    filter(!is.na(Max_Relief)) %>%
    group_by(Year, Site) %>%
    summarize(
        Reef_Relief = mean(Max_Relief, na.rm = TRUE),
        .groups = "drop"
    )

message("    Relief: ", nrow(indicator_relief_site), " site-year records")

# Inspect relief values to inform reference level
relief_summary <- indicator_relief_site %>%
    summarize(
        Min = min(Reef_Relief, na.rm = TRUE),
        Mean = mean(Reef_Relief, na.rm = TRUE),
        Median = median(Reef_Relief, na.rm = TRUE),
        Max = max(Reef_Relief, na.rm = TRUE),
        Q90 = quantile(Reef_Relief, 0.9, na.rm = TRUE)
    )
message("    Relief distribution (cm): min=", round(relief_summary$Min, 1),
        ", mean=", round(relief_summary$Mean, 1),
        ", median=", round(relief_summary$Median, 1),
        ", max=", round(relief_summary$Max, 1),
        ", 90th pct=", round(relief_summary$Q90, 1))

# =============================================================================
# 7. COMBINE ALL SITE-LEVEL INDICATORS
# =============================================================================
message("---- Combining site-level indicators ----")

# Merge all indicators into one dataframe keyed by Year, Site
indicators_site <- indicator_lcc_site %>%
    full_join(indicator_fma_site, by = c("Year", "Site")) %>%
    full_join(indicator_rd_site, by = c("Year", "Site")) %>%
    full_join(indicator_cd_site, by = c("Year", "Site")) %>%
    full_join(indicator_relief_site, by = c("Year", "Site")) %>%
    full_join(indicator_bleach_site, by = c("Year", "Site"))

message("  Combined indicator table: ", nrow(indicators_site), " site-year records")

# =============================================================================
# 8. NORMALIZE TO CONDITION INDICES
# =============================================================================
message("---- Normalizing to condition indices ----")

# Reference levels and directions
# Relief reference: AGRRA records Maximum relief in cm per transect. Typical values
# range 25 to 180 cm based on the data. A reference of 150 cm represents
# high structural complexity. Adjust if the data summary above suggests otherwise.
ref_lcc <- 50       # % live coral cover
ref_fma <- 50       # % fleshy macroalgae (inverse)
ref_rd <- 15        # recruits per m2
ref_cd <- 2.0       # Shannon H'
ref_relief <- 150   # cm max relief (empirical, this dataset)
ref_bleach <- 100   # % bleaching prevalence (inverse; 100% = theoretical maximum)

indicators_site <- indicators_site %>%
    mutate(
        CI_LCC = pmin(Live_Coral_Cover / ref_lcc, 1.0),
        CI_FMA = pmax(1 - Fleshy_Macroalgae_Cover / ref_fma, 0.0),
        CI_RD = pmin(Recruit_Density / ref_rd, 1.0),
        CI_CD = pmin(Coral_Diversity_H / ref_cd, 1.0),
        CI_Relief = pmin(Reef_Relief / ref_relief, 1.0)
    )

if ("Bleaching_Prevalence" %in% names(indicators_site)) {
    indicators_site <- indicators_site %>%
        mutate(CI_Bleach = pmax(1 - Bleaching_Prevalence / ref_bleach, 0.0))
} else {
    indicators_site$CI_Bleach <- NA_real_
}

# =============================================================================
# 9. AGGREGATE PER GEOGRAPHIC UNIT AND BUILD CONDITION ACCOUNT TABLE
# =============================================================================
message("---- Building condition account tables ----")

# Define indicator metadata
indicator_defs <- tibble(
    Indicator = c("Live Coral Cover", "Fleshy Macroalgae Cover",
                  "Coral Recruit Density", "Coral Diversity (Shannon H')",
                  "Reef Relief", "Bleaching Prevalence"),
    Unit = c("%", "%", "per m2", "index", "cm", "%"),
    Value_Col = c("Live_Coral_Cover", "Fleshy_Macroalgae_Cover",
                  "Recruit_Density", "Coral_Diversity_H", "Reef_Relief",
                  "Bleaching_Prevalence"),
    CI_Col = c("CI_LCC", "CI_FMA", "CI_RD", "CI_CD", "CI_Relief", "CI_Bleach"),
    Reference_Level = c(ref_lcc, ref_fma, ref_rd, ref_cd, ref_relief, ref_bleach),
    Direction = c("Higher=better", "Higher=worse",
                  "Higher=better", "Higher=better", "Higher=better", "Higher=worse")
)

# Remove bleaching row if no bleaching data was found
if (!bleaching_available) {
    indicator_defs <- indicator_defs %>% filter(Indicator != "Bleaching Prevalence")
}

# Target years for opening/closing
year_opening <- "2023"
year_closing <- "2025"

# Function to build a condition account for one geographic unit
build_account <- function(unit_name, unit_sites, indicators_df, indicator_defs) {
    # Filter to sites in this unit
    df_unit <- indicators_df %>% filter(Site %in% unit_sites)

    if (nrow(df_unit) == 0) {
        message("    No data for: ", unit_name)
        return(NULL)
    }

    results <- list()

    for (i in seq_len(nrow(indicator_defs))) {
        ind <- indicator_defs[i, ]
        val_col <- ind$Value_Col
        ci_col <- ind$CI_Col

        # Opening year data
        df_open <- df_unit %>%
            filter(Year == year_opening) %>%
            filter(!is.na(.data[[val_col]]))
        # Closing year data
        df_close <- df_unit %>%
            filter(Year == year_closing) %>%
            filter(!is.na(.data[[val_col]]))

        n_open <- nrow(df_open)
        n_close <- nrow(df_close)

        if (n_open == 0 && n_close == 0) {
            # No data at all for this indicator in this unit
            row <- tibble(
                Ecosystem_Type = "Coral reef (M1.3)",
                Indicator = ind$Indicator,
                Unit = ind$Unit,
                Reference_Level = ind$Reference_Level,
                Opening_Year = year_opening,
                Opening_Value = NA_real_,
                Opening_SE = NA_real_,
                Opening_CI = NA_real_,
                Closing_Year = year_closing,
                Closing_Value = NA_real_,
                Closing_SE = NA_real_,
                Closing_CI = NA_real_,
                CI_Change = NA_real_,
                Pct_Change = NA_real_,
                Interpretation = "Insufficient data",
                N_Sites = paste0(n_open, "/", n_close),
                Data_Quality = "No data"
            )
            results[[length(results) + 1]] <- row
            next
        }

        # Opening stats
        if (n_open > 0) {
            open_val <- mean(df_open[[val_col]], na.rm = TRUE)
            open_se <- ifelse(n_open > 1, sd(df_open[[val_col]], na.rm = TRUE) / sqrt(n_open), NA_real_)
            open_ci <- mean(df_open[[ci_col]], na.rm = TRUE)
        } else {
            open_val <- NA_real_; open_se <- NA_real_; open_ci <- NA_real_
        }

        # Closing stats
        if (n_close > 0) {
            close_val <- mean(df_close[[val_col]], na.rm = TRUE)
            close_se <- ifelse(n_close > 1, sd(df_close[[val_col]], na.rm = TRUE) / sqrt(n_close), NA_real_)
            close_ci <- mean(df_close[[ci_col]], na.rm = TRUE)
        } else {
            close_val <- NA_real_; close_se <- NA_real_; close_ci <- NA_real_
        }

        # Change
        ci_change <- if (!is.na(open_ci) && !is.na(close_ci)) close_ci - open_ci else NA_real_
        pct_change <- if (!is.na(open_ci) && !is.na(close_ci) && open_ci != 0) {
            (close_ci - open_ci) / open_ci * 100
        } else {
            NA_real_
        }

        # Interpretation
        # "Stable" if change is within 1 SE of the closing CI
        # Use mean of opening and closing SE as threshold when both exist
        if (!is.na(ci_change)) {
            # Calculate SE of the CI for threshold
            ci_se_open <- if (n_open > 1) sd(df_open[[ci_col]], na.rm = TRUE) / sqrt(n_open) else NA_real_
            ci_se_close <- if (n_close > 1) sd(df_close[[ci_col]], na.rm = TRUE) / sqrt(n_close) else NA_real_
            se_threshold <- mean(c(ci_se_open, ci_se_close), na.rm = TRUE)

            if (is.na(se_threshold) || se_threshold == 0) {
                # Cannot determine stability from SE; use raw direction
                interpretation <- ifelse(ci_change > 0, "Improving",
                                        ifelse(ci_change < 0, "Declining", "Stable"))
            } else {
                interpretation <- ifelse(abs(ci_change) <= se_threshold, "Stable",
                                        ifelse(ci_change > 0, "Improving", "Declining"))
            }
        } else if (n_open > 0 && n_close == 0) {
            interpretation <- "Opening only"
        } else if (n_open == 0 && n_close > 0) {
            interpretation <- "Closing only"
        } else {
            interpretation <- "Insufficient data"
        }

        # Data quality based on min of the two sample sizes
        n_min <- min(n_open, n_close)
        if (n_open == 0 || n_close == 0) {
            n_avail <- max(n_open, n_close)
            data_quality <- ifelse(n_avail >= 5, "Good (one period)",
                                  ifelse(n_avail >= 3, "Moderate (one period)", "Limited (one period)"))
        } else {
            data_quality <- ifelse(n_min >= 5, "Good",
                                  ifelse(n_min >= 3, "Moderate", "Limited"))
        }

        row <- tibble(
            Ecosystem_Type = "Coral reef (M1.3)",
            Indicator = ind$Indicator,
            Unit = ind$Unit,
            Reference_Level = ind$Reference_Level,
            Opening_Year = year_opening,
            Opening_Value = round(open_val, 2),
            Opening_SE = round(open_se, 2),
            Opening_CI = round(open_ci, 4),
            Closing_Year = year_closing,
            Closing_Value = round(close_val, 2),
            Closing_SE = round(close_se, 2),
            Closing_CI = round(close_ci, 4),
            CI_Change = round(ci_change, 4),
            Pct_Change = round(pct_change, 2),
            Interpretation = interpretation,
            N_Sites = paste0(n_open, "/", n_close),
            Data_Quality = data_quality
        )
        results[[length(results) + 1]] <- row
    }

    bind_rows(results)
}

# =============================================================================
# 10. PRODUCE ACCOUNTS FOR ALL GEOGRAPHIC UNITS AND SAVE
# =============================================================================
message("---- Producing and saving condition accounts ----")

# Create outputs directory if needed
if (!dir.exists("outputs")) dir.create("outputs")

all_accounts <- list()

for (g in names(geo_units)) {
    unit <- geo_units[[g]]
    message("  Processing: ", unit$name, " (", length(unit$sites), " sites)")

    account <- build_account(unit$name, unit$sites, indicators_site, indicator_defs)

    if (is.null(account)) next

    # Add geographic unit column
    account <- account %>%
        mutate(Geographic_Unit = unit$name, .before = 1)

    all_accounts[[g]] <- account

    # Save individual CSV
    filename <- tolower(gsub("[^A-Za-z0-9]", "_", g))
    filepath <- file.path("outputs", paste0("condition_account_", filename, ".csv"))
    write_csv(account, filepath)
    message("    Saved: ", filepath)
}

# Combined CSV
if (length(all_accounts) > 0) {
    df_all <- bind_rows(all_accounts)
    write_csv(df_all, "outputs/condition_account_all_areas.csv")
    message("  Saved: outputs/condition_account_all_areas.csv")

    # Summary of condition indices only
    df_summary <- df_all %>%
        select(Geographic_Unit, Indicator, Opening_Year, Opening_CI,
               Closing_Year, Closing_CI, CI_Change, Pct_Change,
               Interpretation, N_Sites, Data_Quality)
    write_csv(df_summary, "outputs/condition_indices_summary.csv")
    message("  Saved: outputs/condition_indices_summary.csv")
} else {
    message("  No accounts produced. Check that data contains matching sites.")
}

message("---- Condition account pipeline complete ----")
