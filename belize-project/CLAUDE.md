# Belize Ocean Accounts

## Project Overview

This repository calculates **coral reef condition accounts** for Belize using the SEEA EA (System of Environmental-Economic Accounting — Ecosystem Accounting) framework. Raw field data comes from AGRRA (Atlantic and Gulf Rapid Reef Assessment) surveys provided by Wilbert. The R pipeline processes this data into six condition indicators that feed into standardized SEEA EA condition account tables. The ecosystem type is photic coral reefs, classified as M1.3 under the IUCN Global Ecosystem Typology.

## Repository Structure

```
belize-ocean-accounts/
├── condition-account-scripts/   # R pipeline (copied from GOAP-condition-account-belize)
│   ├── indicator_calculation.r  # Entry point — runs full pipeline
│   ├── data_validation.r        # Validates restructured data
│   ├── data_restructuring.r     # Converts AGRRA exports → GOAP format
│   ├── helper_scripts/          # packages_load.r, functions_define.r, data_test_load.r
│   ├── data_deposit/            # Place raw AGRRA .xlsx files here
│   ├── data_dummy/              # Test data (3 Excel templates)
│   └── outputs/                 # Generated validation reports & indicator tables
│
└── seea-ea-methodology/         # Reference methodology (copied from accounting-bot-copy)
    ├── 03_condition_accounts/   # Key: skill_condition_biotic_coral.md
    ├── 05_seea_accounting_tables/  # SEEA EA table formats
    └── ...                      # Framework, extent, services, templates, references
```

## R Pipeline Workflow

**Execution chain:**
```
indicator_calculation.r
  └─ sources data_validation.r
       └─ sources data_restructuring.r (or data_test_load.r if test_on=TRUE)
            └─ sources packages_load.r + functions_define.r
```

**Working directory requirement:** All R scripts must be run with `condition-account-scripts/` as the working directory. They use relative paths (`data_deposit/`, `helper_scripts/`, etc.).

### Pipeline Steps

1. **data_restructuring.r** — Reads 4 AGRRA Excel files from `data_deposit/` (`BenthicRaw.xlsx`, `CoralRaw.xlsx`, `FishRaw.xlsx`, `Metadata.xlsx`), extracts 11 sheets, and transforms them into standardized dataframes: `df_sites`, `df_benthic_cover`, `df_recruits`, `df_invertebrates`, `df_coral_community`, `df_fish`, `df_organisms`.

2. **data_validation.r** — Validates each dataframe against expected schemas: column completeness, value ranges (depth 0–20m, temp 25–35°C, lat 16–18.99°N, lon -88.99–-87°W), enumerated values (site codes, MPA names, organism codes), date/time formats. Writes `outputs/validation_report.txt`.

3. **indicator_calculation.r** — Calculates five condition indicators from validated data:
   - **Live Coral Cover (LCC)** — % coral in benthic point-intercept (co-dominated points weighted 0.5)
   - **Fleshy Macroalgae Cover (FMA)** — % fleshy macroalgae (same method as LCC)
   - **Recruit Density (RD)** — coral recruits per 25 m² quadrat (small/large categories)
   - **Coral Diversity (CD)** — Shannon diversity index + species richness per transect
   - **Reef Relief (RR)** — maximum reef relief height (cm) per site

   The extended SEEA EA pipeline (`condition_account_seea.r`) adds a sixth indicator:
   - **Bleaching Prevalence (BP)** — % of coral colonies showing bleaching or paling signs

### Test Mode

Set `test_on <- TRUE` at the top of `indicator_calculation.r` to run the pipeline with dummy data from `data_dummy/` instead of real AGRRA files. This is useful for verifying the scripts work.

**Important:** When `test_on` is TRUE vs FALSE, the organism taxonomy lookup categories differ:
- Test mode: `coral_category <- "Coral"`, `algae_category <- "Fleshy Macroalgae"`
- Real data: `coral_category <- "Calcifiers :: Coral"`, `algae_category <- "Algae :: Macro :: Fleshy"`

## Key Technical Notes

- **Subregion filter:** `data_restructuring.r` filters all data to `Subregion == "Northern Barrier Complex"`. This may need adjusting depending on the actual AGRRA data coverage.
- **Site codes:** Validation expects these codes: `{MXRCK, BZ1077, BZ1079, BZ1081, BZ1230, BZ1231, BZHCCD01, BZHCCD02, CCSC, BZ1229, 1076B}`. Real AGRRA data may contain different codes — update the validation list accordingly.
- **MPA names:** Expected: `{None, BCMR, HCMR, CCMR, TAMR, GRMR, SWCMR, GSSCMR, LBCMR, SCMR, PHMR, HMCNM}`.
- **R packages required:** tidyverse, readxl, knitr (auto-installed by `packages_load.r`).
- **Recruit density:** 4 quadrats per transect, each 25 m²; missing quadrats are filled with 0 counts.
- **Coral diversity:** Shannon index H = -Σ(pᵢ × log(pᵢ)) calculated per transect, averaged per site.

## SEEA EA Condition Account Output

The final output is a condition account table in SEEA EA format:

| Ecosystem Type | Indicator | Reference Level | Opening Value | Opening CI | Closing Value | Closing CI | Change |
|---|---|---|---|---|---|---|---|
| Coral reef (M1.3) | Live coral cover | 50% | measured | value/ref | measured | value/ref | delta |

**Normalization:**
- Higher-is-better indicators: `CI = measured / reference` (e.g., coral cover)
- Higher-is-worse indicators: `CI = 1 - (measured / reference)` (e.g., macroalgae, bleaching)
- Scale: 0 (degraded) to 1 (reference condition)

## Methodology Reference

The `seea-ea-methodology/` folder contains detailed guidance. Key files:
- `03_condition_accounts/skill_condition_biotic_coral.md` — Coral reef condition methodology
- `05_seea_accounting_tables/skill_condition_opening_closing_seea_account.md` — Account table format
- `01_framework/tiered_assessment_framework.md` — Tier 1–3 assessment levels

## Conventions

- Do not modify the source repositories (`GOAP-condition-account-belize`, `accounting-bot-copy`) — only work within this repo.
- AGRRA data files go in `condition-account-scripts/data_deposit/` and are gitignored.
- Generated outputs in `condition-account-scripts/outputs/` are gitignored.
- All indicator summary statistics are rounded to 2 decimal places.

## Writing Style

All generated text (reports, markdown, captions, table headers, documentation) must read as natural, human-written prose.

- No emojis, em dashes, or en dashes. Use commas, semicolons, colons, or "to" for ranges.
- No curly/smart quotes. Straight quotes only.
- No filler openers: "Certainly", "Great", "Absolutely", "Of course".
- No hedging phrases: "It's worth noting", "Importantly", "It should be noted", "As previously mentioned".
- No AI-signature words: "delve", "leverage", "utilize", "facilitate", "comprehensive", "robust", "cutting-edge", "multifaceted", "streamline", "synergy", "holistic".
- Plain words: "use" not "utilize", "show" not "demonstrate", "about" not "approximately" (unless precision matters).
- Active voice by default. Passive only when the actor is genuinely unknown.
- No blank paragraphs for spacing. Use margin/spacing settings instead.
- No rhetorical questions in technical outputs.
- No bullet-point walls. More than 5 bullets should become prose or a table.
- Numerals for measurements and data ("5 m", "12 sites", "3.7%"). Spell out numbers under 10 only in running prose without units.

## Document Outputs

- All .docx files follow GOAP template standards.
- For full formatting spec (colors, typography, page layout), see `docs/goap-docx-conventions.md`.
- Convert markdown to Word using `python md_to_docx.py input.md`.
- The conversion script uses the GOAP Report Template at `Templates/GOAP Templates/GOAP Word templates/GOAP-REPORT TEMPLATE.docx`.

### Table Formatting Rules

Tables are the most failure-prone element. Follow these rules exactly:

- **Borders**: 1 pt solid, color #404040 (dark gray) on all cell borders.
- **Cell padding**: 4 pt space before and 4 pt space after text in each cell (top and bottom).
- **Header row**: background fill #3B9C7B (green), text white (#FFFFFF), bold, 10 pt Arial.
- **First column** (row headers): background fill #0A5455 (dark teal), text white (#FFFFFF), bold.
- **Data cells**: no background fill (white), text #30302F, 10 pt Arial, left-aligned for text, right-aligned for numbers.
- **Header-to-header borders**: #2C745B (darker green) between major header sections.
- **No heavy outer border** on table edges, or minimal 0.5 pt #404040.
- **Column width**: distribute evenly unless content requires otherwise. Numeric columns can be narrower.
- **Decimal alignment**: align numeric values on the decimal point within a column.
- **Merged cells**: use sparingly, only for category grouping headers spanning multiple columns.
