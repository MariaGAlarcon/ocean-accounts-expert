# Accounting Bot: SEEA EA Ecosystem Accounting Methodology Repository

A comprehensive, open-source repository for implementing UN System of Environmental-Economic Accounting — Ecosystem Accounting (SEEA EA) in coastal and marine ecosystems.

## What Is This Repository?

**Accounting Bot** provides methodology, skills, and templates for measuring and valuing ecosystem services across three core account types:

1. **Extent Accounts** — How much ecosystem exists? (area/hectares)
2. **Condition Accounts** — How healthy is it? (0–1 index relative to reference level)
3. **Service Accounts** — What benefits does it provide? (physical supply and monetary value)

This is a **toolkit for practitioners**, not a single case study. It supports projects across diverse coastal/marine ecosystems (coral reefs, mangroves, seagrass, estuaries, etc.).

---

## Repository Structure

The repository is organized into **7 thematic folders**, each with its own README:

```
Accounting bot/
├── 01_framework/                          # Foundational guidance
│   ├── README.md
│   ├── tiered_assessment_framework.md     # Feasibility & accuracy tiers
│   └── skill_data_quality_assessment.md   # Data governance
│
├── 02_extent_accounts/                    # Ecosystem area measurement
│   ├── README.md
│   ├── skill_extent_measurement.md        # How to measure ecosystem extent
│   ├── skill_extent_data_pipeline.md      # Satellite data processing
│   └── skill_extent_change_matrix_seea_account.md  # Extent transitions & SEEA format
│
├── 03_condition_accounts/                 # Ecosystem health indicators
│   ├── README.md
│   ├── skill_condition_measurement.md     # General framework
│   ├── skill_condition_abiotic.md         # Water quality, sediment, oxygen
│   ├── skill_condition_biotic_coral.md    # Coral reefs
│   ├── skill_condition_biotic_seagrass.md # Seagrass meadows
│   ├── skill_condition_biotic_mangrove.md # Mangrove forests
│   └── skill_condition_biotic_fish_invert.md  # Fish & invertebrate communities
│
├── 04_service_accounts/                   # Ecosystem service valuation
│   ├── README.md
│   ├── skill_services_measurement.md      # General framework
│   ├── skill_services_provisioning.md     # Wild fish, wood/fuel
│   ├── skill_services_regulating.md       # Nursery, carbon, coastal protection, sediment
│   └── skill_services_cultural.md         # Recreation, gleaning, cultural
│
├── 05_seea_accounting_tables/             # Formal account table formats
│   ├── README.md
│   └── skill_condition_opening_closing_seea_account.md  # Condition account table format
│   [Planned: Extent tables, Service tables, Supply & Use tables]
│
├── 06_templates/                          # Reusable templates for projects
│   ├── README.md
│   ├── template_data_flow_condition_to_services.md  # Integration planning template
│   └── TEMPLATE_INSTRUCTIONS.md           # How to use templates
│   [Planned: Condition tables, Service valuation, Account templates]
│
└── 07_references/                         # Case studies and reference materials
    ├── README.md
    ├── rnf_bcaf_chunks.md                 # Case study: Mangrove carbon accounting
    └── refs/
        ├── endheri_report_chunks.md       # Project documentation
        └── ncaves_valuation_chunks.md     # Monetary valuation reference

```

---

## Quick Start

### By Role

**🏢 Project Manager — Planning an ecosystem accounting project?**
1. Read: `01_framework/tiered_assessment_framework.md` (scope & cost decisions)
2. Read: `06_templates/TEMPLATE_INSTRUCTIONS.md` (project integration planning)
3. Review: Case studies in `07_references/` (timeline & budget estimates)
4. **Output:** Project plan with tiered method choices and data requirements

**🔬 Field Researcher — Collecting ecosystem condition data?**
1. Choose your ecosystem: coral reef, mangrove, seagrass, fish community, abiotic
2. Read: `03_condition_accounts/skill_condition_[TYPE].md` (field methods)
3. Read: `01_framework/skill_data_quality_assessment.md` (QA/QC procedures)
4. **Output:** Field survey data ready for analysis and account compilation

**📊 Data Analyst — Calculating condition or service indicators?**
1. Read: `03_condition_accounts/skill_condition_measurement.md` (general framework)
2. Read: `04_service_accounts/skill_services_measurement.md` (service framework)
3. Choose service: provisioning, regulating, or cultural
4. Read: `04_service_accounts/skill_services_[TYPE].md` (specific calculations)
5. **Output:** Calculated indicators and SEEA EA account values

**💼 Policymaker — Using accounts for decisions?**
1. Read: `06_templates/template_data_flow_condition_to_services.md` (project integration overview)
2. Review: Case studies in `07_references/` (real-world examples & key findings)
3. Refer to: Account folders for method transparency and limitations
4. **Output:** Evidence-based policy analysis with documented uncertainties

---

## Key Features

✅ **Comprehensive Coverage**
- Extent, condition, and service accounts all addressed
- Multiple ecosystem types (coral, mangrove, seagrass, fish communities, etc.)
- Multiple valuation approaches (Tier 1–3) for different budget/capacity constraints

✅ **Aligned with International Standards**
- UN SEEA EA (2021) framework
- CICES v5.1 ecosystem service classification
- SEEA-CF supply and use table format

✅ **Practical Guidance**
- Step-by-step SOPs for common procedures
- Real-world case studies with lessons learned
- Data quality frameworks and tiered assessments

✅ **Reusable Templates**
- Copy-paste templates for your project
- Integration planning tools
- Account table templates (expanding)

✅ **Open Source**
- All materials freely available
- Built on best practices from global partnerships
- Contributions welcome from the community

---

## Using This Repository

### For a New Project

**Step 1: Plan (Weeks 1–2)**
1. Copy `06_templates/template_data_flow_condition_to_services.md`
2. Follow instructions in `06_templates/TEMPLATE_INSTRUCTIONS.md`
3. Identify which accounts you'll develop (extent, condition, services)
4. Review case studies for timeline and cost estimates

**Step 2: Design (Weeks 3–8)**
1. Read relevant skills: `01_framework/`, `02_extent_accounts/`, `03_condition_accounts/`
2. Choose methods and justify tier choices
3. Design data collection protocols
4. Document reference levels and valuation approach

**Step 3: Implement (Weeks 9+)**
1. Collect/process extent data (satellite, GIS)
2. Conduct field surveys for condition (using measurement SOPs)
3. Gather economic data (fisheries, tourism, prices)
4. Compile into SEEA EA account tables using `05_seea_accounting_tables/` format

**Step 4: Report (Final phase)**
1. Compile accounts in SEEA EA format
2. Document data quality, uncertainties, and tier assessments
3. Create supply and use table (cross-sector summary)
4. Share findings and lessons learned

### For Individual Analysis

Each folder has its own README describing:
- Contents and use cases
- Quick reference tables
- Integration with other folders
- Common questions and answers

**Start with the folder README** that matches your task:
- Planning? → `01_framework/README.md`
- Measuring extent? → `02_extent_accounts/README.md`
- Measuring condition? → `03_condition_accounts/README.md`
- Valuing services? → `04_service_accounts/README.md`
- Writing SEEA tables? → `05_seea_accounting_tables/README.md`
- Integrating accounts? → `06_templates/README.md`
- Learning from case studies? → `07_references/README.md`

---

## Case Study Reference: Maldives Natural Capital Accounts

**Note:** This repository originally documented the **Maldives Natural Capital Accounts (Laamu Atoll)** project. That specific project documentation is available in `07_references/` and used as a worked example throughout.

**Project Overview:**
- **Location:** Laamu Atoll, Maldives
- **Ecosystems:** Coral reefs (6,692 ha), seagrass (4,220 ha), mangroves (4.8 ha)
- **Accounting period:** 2020
- **Key results:**
  - Wild fish provisioning: 28.6 metric tons/year
  - Carbon sequestration: 3,485 metric tons/year
  - Coastal protection: 33 km of protected coastline
  - Tourism contribution: 44.3% of Laamu spend linked to coral reefs

**Use as reference for:**
- Parameter values (carbon rates, market prices, reference levels)
- Methods documentation and tiered assessment justification
- Real-world implementation timeline and challenges
- Lessons learned from operational ecosystem accounting

---

## Ecosystem Coverage

| Ecosystem Type | Extent | Condition | Service | Documentation |
|---|---|---|---|---|
| **Coral Reefs** | ✅ | ✅ (biotic_coral.md) | ✅ (provisioning, regulating, cultural) | Comprehensive |
| **Mangroves** | ✅ | ✅ (biotic_mangrove.md) | ✅ (provisioning, regulating, cultural) | Comprehensive |
| **Seagrass** | ✅ | ✅ (biotic_seagrass.md) | ✅ (provisioning, regulating, cultural) | Comprehensive |
| **Fish Communities** | ⚠️ | ✅ (biotic_fish_invert.md) | ✅ (provisioning, regulating) | Good |
| **Invertebrate Communities** | ⚠️ | ✅ (biotic_fish_invert.md) | ⚠️ | Developing |
| **Abiotic Indicators** | N/A | ✅ (abiotic.md) | ⚠️ | Good |

---

## Key Concepts

### Ecosystem Accounts

**Extent Account:** How much ecosystem?
- Measured in hectares or km²
- Changes tracked (degradation, recovery, conversion)
- Spatial extent maps in GIS format

**Condition Account:** How healthy?
- Measured on 0–1 scale
- Normalized to reference level
- Opening and closing year values
- Change magnitude (improving/stable/declining)

**Service Account:** What benefits?
- Measured in physical units (kg/yr, Mg/yr, visitors/yr, m³/yr)
- Valued in monetary units (USD/yr, local currency)
- Aggregated by ecosystem type and sector
- Supply and use tables (cross-sector summary)

### Tiered Approach

All methods documented with three tiers:

- **Tier 1** — Simple, lower cost, Tier 1 accuracy
- **Tier 2** — Intermediate complexity and cost, Tier 2 accuracy
- **Tier 3** — Complex, higher cost, Tier 3 accuracy

Choose based on available budget, data, and capacity. Document your choice transparently.

---

## Key Standards and References

- **UN SEEA EA (2021)** — System of Environmental-Economic Accounting — Ecosystem Accounting
- **CICES v5.1** — Common International Classification of Ecosystem Services
- **SEEA-CF** — System of Environmental-Economic Accounting — Central Framework
- **GOAP** — Global Ocean Accounts Partnership (training and technical guidance)
- **NCAVES** — Natural Capital Accounting and Valuation of Ecosystem Services

---

## Contributing

We welcome contributions! Ways to help:

1. **Share case studies** from your projects → `07_references/`
2. **Develop missing templates** (extent table, service table, metadata forms)
3. **Add regional parameter values** (carbon rates, market prices for your biogeographic region)
4. **Improve documentation** with local language translations or worked examples
5. **Report issues or suggest improvements** via pull requests or issues

**Contribution process:**
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/my-contribution`)
3. Commit with clear messages
4. Submit pull request with description
5. Engage with reviewers for feedback

---

## Support and Questions

- **Getting started?** → Read `01_framework/README.md`
- **Stuck on a specific task?** → Check the relevant folder's README
- **Want to learn from examples?** → Review `07_references/rnf_bcaf_chunks.md`
- **Need more guidance?** → Refer to UN SEEA EA (2021) and GOAP technical materials

---

## License

This repository is provided under [specify license, typically CC-BY or CC-BY-NC-SA]. Refer to LICENSE file for details.

---

## Partners and Acknowledgments

This repository synthesizes methodology and experience from multiple organizations:

- **Global Ocean Accounts Partnership (GOAP)** — UNSW Sydney, Australia
- **UN Environment Programme (UNEP)** — Environmental accounting support
- **United Nations Statistics Division (UNSD)** — SEEA EA framework stewards
- **Global Environment Facility (GEF)** — Funding and technical partnerships
- **World Bank** — NCAVES and ecosystem accounting resources
- **WCMC (World Conservation Monitoring Centre)** — Biodiversity data and methods

---

## Citation

If you use materials from this repository, please cite:

> Accounting Bot Contributors (2026). *SEEA EA Ecosystem Accounting Methodology Repository*. Retrieved from [repository URL]

For specific skills or case studies, cite the original authors as documented within each file.

---

## Roadmap

**Completed (Q1 2026):**
- ✅ Extent measurement and GIS processing skills
- ✅ Condition measurement for all major coastal ecosystems
- ✅ Service account methodologies (provisioning, regulating, cultural)
- ✅ Data quality and tiered assessment frameworks
- ✅ Data flow integration template
- ✅ Repository reorganization into thematic folders

**In Progress (Q2–Q3 2026):**
- 🟡 Service table templates (CSV format)
- 🟡 Supply and use table format and guidance
- 🟡 Additional case studies (tropical, temperate, polar)
- 🟡 Regional parameter databases (carbon rates, market prices by region)

**Planned (Q4 2026 onwards):**
- 🔵 Automation tools (R/Python scripts for account compilation)
- 🔵 Interactive dashboards for account visualization
- 🔵 Multi-language translations (Spanish, French, Bahasa Indonesia)
- 🔵 Integration with global biodiversity and SDG platforms

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-03-04 | Initial repository reorganization into 7 thematic folders with comprehensive READMEs |
| 0.9 | 2025-02-28 | Original Maldives Natural Capital Accounts project repository |

---

**Last updated:** 2026-03-04
**Maintained by:** Accounting Bot Contributors
**Questions?** Open an issue or contact the repository maintainers
