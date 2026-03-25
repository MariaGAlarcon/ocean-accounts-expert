# Ocean Accounts Expert

## Purpose

This repository is a knowledge base and working environment for Ocean Accounting tasks following the SEEA-EA framework and GOAP technical guidance. Use it to assist with:

- Account development (extent, condition, services, monetary valuation)
- Methodology questions and standards interpretation
- Template completion and data pipeline design
- Creating training materials, practitioner guidance, and presentations
- Applying ocean accounting knowledge to country-specific projects

## Repository Structure

```
ocean-accounts-expert/
├── seea-ea-methodology/        # Core SEEA-EA methodology reference
│   ├── 01_framework/           # Tiered assessment framework, data quality
│   ├── 02_extent_accounts/     # Extent measurement, change matrices
│   ├── 03_condition_accounts/  # Condition indicators (coral, mangrove, seagrass, fish, abiotic)
│   ├── 04_service_accounts/    # Provisioning, regulating, cultural services
│   ├── 05_seea_accounting_tables/  # Standard SEEA-EA table formats
│   ├── 06_templates/           # Data flow and methodology templates
│   ├── 07_references/          # Source documents and chunked references
│   └── refs/                   # PDF and docx source files
│
├── standards/                  # International standards (SEEA-CF, SEEA-EA, SNA25, GOAP TG)
│
├── goap-templates/             # GOAP brand templates (Word, PowerPoint, factsheets)
│
├── claude-skills-library/      # Custom skills and agent definitions
│   ├── skills/                 # 18 skills (research, writing, QA, methodology, etc.)
│   └── agents/                 # 13 specialized agents
│
├── belize-project/             # Reference project: Belize coral reef condition accounts
│   ├── condition-account-scripts/  # R pipeline (AGRRA data to SEEA-EA tables)
│   ├── docs/                   # Reports, technical guidance, methodology docs
│   ├── training/               # Workshop materials (facilitator guide, exercises)
│   └── GOAP-condition-account-belize-feedback/  # Pipeline feedback and improvements
│
└── [future project folders]/   # New country or thematic projects go here
```

## How to Use This Repository

### For methodology questions
Consult `seea-ea-methodology/` first. Each subfolder has a README and detailed skill files covering the relevant SEEA-EA accounting domain. Cross-reference with `standards/` for the full text of SEEA-CF, SEEA-EA, SNA25, and GOAP Technical Guidance.

### For new country projects
Use `belize-project/` as the reference implementation. It demonstrates the full workflow from raw field data through R processing to SEEA-EA condition account tables, plus training materials and technical guidance documents. New projects should follow the same pattern: data pipeline, indicator calculation, account tables, reporting, and training.

### For templates and branding
Use `goap-templates/` for GOAP-branded documents. Word templates use the GOAP Report Template. See `belize-project/docs/goap-docx-conventions.md` for table formatting rules (colors, borders, cell padding).

### For document conversion
Convert markdown to GOAP-formatted Word documents using `python md_to_docx.py input.md`. The conversion script is in `belize-project/` and uses the GOAP Report Template from `goap-templates/`.

## Writing Style

All generated text (reports, markdown, captions, table headers, documentation) must read as natural, human-written prose.

- No emojis, em dashes, or en dashes. Use commas, semicolons, colons, or "to" for ranges.
- No curly/smart quotes. Straight quotes only.
- No filler openers: "Certainly", "Great", "Absolutely", "Of course".
- No hedging phrases: "It's worth noting", "Importantly", "It should be noted".
- No AI-signature words: "delve", "leverage", "utilize", "facilitate", "comprehensive", "robust", "cutting-edge", "multifaceted", "streamline", "synergy", "holistic".
- Plain words: "use" not "utilize", "show" not "demonstrate", "about" not "approximately" (unless precision matters).
- Active voice by default. Passive only when the actor is genuinely unknown.
- No rhetorical questions in technical outputs.
- No bullet-point walls. More than 5 bullets should become prose or a table.
- Numerals for measurements and data ("5 m", "12 sites", "3.7%"). Spell out numbers under 10 only in running prose without units.

## Table Formatting (GOAP Standard)

- **Header row**: background #3B9C7B (green), text white, bold, 10 pt Arial
- **First column** (row headers): background #0A5455 (dark teal), text white, bold
- **Data cells**: no background, text #30302F, 10 pt Arial
- **Borders**: 1 pt solid #404040 on all cells
- **Cell padding**: 4 pt space before and after text
- **Numbers**: right-aligned, decimal-aligned within columns, 2 decimal places for indicators

## SEEA-EA Account Types

When building accounts, follow this sequence:

1. **Extent accounts** -- measure area of ecosystem types (opening/closing stock, additions, reductions)
2. **Condition accounts** -- measure ecosystem health using biophysical indicators normalized to reference levels (CI scale 0 to 1)
3. **Ecosystem services accounts** -- measure flows of provisioning, regulating, and cultural services in physical and monetary terms
4. **Monetary valuation** -- value ecosystem assets and services using exchange values consistent with the SNA

Each account type has detailed methodology in `seea-ea-methodology/` and standard table formats in `05_seea_accounting_tables/`.

## Conventions

- New projects go in their own top-level folder (e.g., `belize-project/`, `fiji-project/`)
- Raw data files should be gitignored (use `data_deposit/` pattern with `.gitkeep`)
- Generated outputs should be gitignored unless they are final deliverables
- R scripts use relative paths from their parent folder as working directory
- All .docx files follow GOAP template standards
