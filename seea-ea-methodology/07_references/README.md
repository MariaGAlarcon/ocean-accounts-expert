# References & Case Studies

This folder contains reference materials, case study documentation, and supporting information for ecosystem accounting implementation.

## Contents

### `rnf_bcaf_chunks.md`

**Source:** RNF BCAF (Restore Natural Forests — Blue Carbon Accounting Framework) project, Central Java, Indonesia

**Purpose:** Real-world case study showing complete SEEA EA implementation for mangrove and seagrass ecosystems.

**What's documented:**
- Project scope (Laamu Atoll, Maldives or Central Java, Indonesia regional accounting)
- Extent measurement (mangrove area decline, seagrass area changes over 2 years)
- Condition accounts (mangrove biomass, seagrass shoot density)
- Service accounts:
  - Carbon sequestration (permanent forest plots, biomass monitoring)
  - Wild fish provisioning (fisheries catch data integration)
  - Coastal protection (reef extent and wave attenuation)
- Economic valuation (SCC for carbon, market prices for fish, replacement costs)
- Tiered assessment justification (Tier 2 on feasibility, Tier 1–2 on accuracy)
- Lessons learned and limitations

**Use for:**
- Understanding real SEEA EA implementation workflow
- Reference parameter values (NCP rates, market prices, reference levels)
- Troubleshooting common data gaps and analytical decisions
- Template for regional accounting project structure
- Case study examples for training and proposal writing

**Key findings from RNF BCAF:**
- 13 permanent forest plots (0.1 ha each) in mangroves
- Annual carbon sequestration: 24,227 Mg C (88,831 Mg CO₂e)
- Valuation: IDR 13.3 billion annual value using domestic carbon market pricing
- Data quality challenges: High plot-to-plot variability, allometric uncertainty, SOC measurement limitations
- Recommendation: Future work should stratify by forest quality class before applying single average sequestration rate

---

### `refs/` Subdirectory

Contains additional reference documents:

#### `endheri_report_chunks.md`
Case study documentation from EnDHeRI project (possibly environmental data or heritage-related accounting project).

**[Details to be added as file is reviewed]**

#### `ncaves_valuation_chunks.md`
Excerpts from NCAVES (Natural Capital Accounting and Valuation of Ecosystem Services) reference documentation.

**Contains:**
- Monetary valuation frameworks and methodologies
- Tiered valuation approaches (Tier 1–3)
- NCAVES categories for provisioning, regulating, and cultural services
- Reference case studies and parameter values
- Value transfer and benefit transfer methodologies

**Use for:**
- Understanding monetization approaches for ecosystem services
- Reference parameter values from similar ecosystems/regions
- Justifying value type choices (market vs. non-market)
- Tiered methodology selection guidance

---

## How to Use These References

### For Project Planning
1. Read the relevant case study (RNF BCAF if working with mangrove/seagrass carbon)
2. Note key parameter values (NCP rates, market prices, reference levels)
3. Identify similar ecosystems and data approaches
4. Adapt methodologies to your context

### For Data Acquisition
1. Review which data sources were used in case studies
2. Estimate effort and cost for your project scope
3. Identify gaps in available data for your ecosystem
4. Plan data collection or value transfer from reference studies

### For Valuation Method Selection
1. Review NCAVES documentation for methodological options
2. Compare Tier 1 (simple) vs. Tier 2 (complex) vs. Tier 3 (research)
3. Match to your project budget and data availability
4. Reference case studies for parameter values

### For Quality Assurance
1. Use case study limitations to anticipate your own
2. Reference tiered assessments to justify accuracy claims
3. Document data quality decisions following case study examples
4. Create sensitivity analyses using ranges from reference studies

---

## Key Parameter Values from Case Studies

### Carbon Sequestration (Mangrove)
**Source:** RNF BCAF, Central Java

| Metric | Value | Notes |
|--------|-------|-------|
| Forest basal area (healthy) | >25 m²/ha | Intact mangroves |
| Net Carbon Production (NCP) | 17.23 Mg CO₂/ha/yr | Literature value; local plots: range 15–20 |
| Above-ground biomass (intact) | >150 Mg/ha | Depends on age and species composition |
| Annual sequestration (per hectare) | ~5–8 Mg C/ha/yr | Accounts for AGB + BGB + soil carbon |

### Valuation
**Source:** RNF BCAF, Central Java

| Method | Value | Notes |
|--------|-------|-------|
| Social Cost of Carbon (SCC) | USD 51–185/Mg CO₂ | Range: IWG conservative to EPA updated |
| Domestic carbon market (IDXCarbon) | IDR 150,000/tCO₂e | Indonesia-specific; market prices vary by compliance instrument |
| Valuation range (annual, per hectare) | USD 260–1,520/ha/yr | Depends on SCC choice and local discount rates |

### Wild Fish Provisioning
**Source:** Coastal fisheries data from case studies

| Parameter | Typical Range | Notes |
|-----------|---------------|-------|
| Market price (coastal fish) | USD 2–6/kg | Varies by species, quality, market |
| Catch per unit effort (CPUE) | Highly variable | Document for your fishery |
| Nursery habitat premium (LRR) | Coral reef: 31%, Seagrass: 13% | Literature meta-analysis estimates |

---

## How to Contribute New Case Studies

If you complete an ecosystem accounting project, consider documenting it as a case study for this folder:

### Documentation Structure

1. **Project Overview** (1–2 pages)
   - Geographic scope
   - Ecosystem types
   - Accounting period
   - Key stakeholders

2. **Methods Summary** (2–4 pages)
   - Extent measurement approach
   - Condition indicator selection
   - Service account methodology
   - Data sources and availability

3. **Results** (2–3 pages)
   - Extent account (with figures/maps)
   - Condition account (with graphs)
   - Service account summary (physical + monetary)
   - Economic significance

4. **Lessons Learned** (1–2 pages)
   - Data quality challenges
   - Methodological decisions and justifications
   - What worked well
   - What would you do differently?

5. **Reference Parameters** (1 page)
   - Key values (sequestration rates, prices, reference levels)
   - Data sources and citations
   - Uncertainty ranges

6. **Tiered Assessment Justification** (1 page)
   - Feasibility tier by sub-procedure
   - Accuracy tier by sub-procedure
   - Binding constraints identified
   - Pathway to upgrade methods

### Submission Process

1. Write up following structure above
2. Anonymize or get consent if project is confidential
3. Cite all references and data sources
4. Create markdown file: `[project_name]_case_study.md`
5. Submit as pull request or contact repository maintainers
6. Engage with community for feedback and improvement

---

## Related Reference Documents (External)

These authoritative sources support ecosystem accounting implementation:

### UN SEEA EA (2021)
- *System of Environmental-Economic Accounting — Ecosystem Accounting*
- Freely available from UN Statistics Division
- Essential foundation for all projects
- Chapter 5: Condition Accounts
- Chapter 6: Service Accounts

### CICES v5.1
- Common International Classification of Ecosystem Services
- Hierarchical classification: Section → Division → Group → Class
- Used to standardize service identification
- [https://cices.eu/](https://cices.eu/)

### GOAP (Global Outcomes on Environmental Accounting)
- Freely available training materials and technical guidance
- Links SEEA EA to SDG monitoring
- Regional workshops and webinars

### NCAVES
- Natural Capital Accounting and Valuation of Ecosystem Services
- Focus on monetary valuation methodologies
- Case studies from multiple regions
- Economic theory and practice guidance

### SEEA-CF
- System of Environmental-Economic Accounting — Central Framework
- Integrates ecosystem accounting with national accounting
- Supply and use tables
- Asset accounts

### Ecosystem-Specific Resources

**Coral Reefs:**
- AIMS (Australian Institute of Marine Science) Long-Term Monitoring Programme
- WCS Reef Resilience monitoring protocols
- CORDIO East Africa reports

**Mangroves:**
- FAO Global Mangrove Alliance resources
- IFRO (International Forestry Resources and Organizations) forest inventory standards
- Carbon measurement protocols

**Seagrass:**
- UNEP Seagrass Conservation Initiative
- SEAGRASS project (EU-funded, Mediterranean and Baltic)

---

## Accessing Reference Documents

### UN SEEA EA (2021)
**Website:** https://unstats.un.org/unsd/envaccounting/seea/
**How to access:** Free PDF download from UN Statistics Division

### CICES v5.1
**Website:** https://cices.eu/
**How to access:** Free online classification browser and downloadable documentation

### GOAP
**Website:** https://www.unep-wcmc.org/ (host organization)
**How to access:** Training materials, webinars, and country project documentation

### NCAVES
**Access:** Contact UNEP or World Bank environmental accounting programmes
**Key publications:** Available through academic databases and institutional repositories

---

## Quick Reference: Which Document for Which Question?

| Question | Reference |
|----------|-----------|
| How do I measure mangrove carbon? | RNF BCAF case study + NCAVES valuation sections |
| What reference levels should I use? | Case studies + skills documentation (03_condition_accounts/) |
| How do I value ecosystem services? | NCAVES valuation chunks + case study economics |
| What data quality challenges might I face? | Case study lessons learned sections |
| How do I choose Tier 1 vs. Tier 2 methods? | 01_framework/tiered_assessment_framework.md + case studies |
| What are typical costs/timelines? | Case study project planning sections |

---

## Building Your Reference Library

### Recommended Reading Order

1. **Start:** UN SEEA EA (2021) Chapter 1–2 (foundation)
2. **Then:** This folder's case studies (real-world examples)
3. **Apply:** 01_framework/ + 02–04_accounts/ skills (methods)
4. **Deepen:** NCAVES documentation (valuation theory)
5. **Validate:** GOAP technical guidance (quality assurance)

### For Different Roles

**Project Manager:**
→ Case studies (timeline, scope, budget planning)
→ Tiered assessment framework (quality vs. cost trade-offs)

**Field Researcher:**
→ Condition account skills (measurement methods)
→ Case study field protocols
→ Data quality assessment framework

**Data Analyst:**
→ Service account skills (calculation methods)
→ NCAVES valuation approaches
→ Case study parameter values

**Policymaker:**
→ Case study key findings and economic significance
→ SEEA EA overview (Chapter 1)
→ Valuation reference values for policy analysis

---

**This folder will grow as new case studies and reference documents are added. Check back regularly for updates!**

---

**Last updated:** 2026-03-04
**Maintained by:** Accounting bot repository
**Contributions welcome:** Submit case studies or reference materials as pull requests
