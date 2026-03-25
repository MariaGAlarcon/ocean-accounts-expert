# Templates for SEEA EA Projects

This folder contains reusable templates for ecosystem accounting projects to copy and adapt.

## Contents

### `template_data_flow_condition_to_services.md`

**Purpose:** Template for mapping condition account outputs to ecosystem service account inputs; identifying data gaps and establishing linkages.

**Use when:**
- Starting to plan ecosystem service accounts after completing condition accounts
- Need to identify which services can use your condition data
- Planning data acquisition priorities
- Integrating condition and service modules in your project

**What's included:**
- 9-part framework covering condition outputs, service inputs, coverage analysis, missing data strategy, implementation phases
- All placeholders [BRACKETED] for easy find-and-replace
- Worked example (Madagascar coral reef project) for reference

**How to use:**
1. Copy to your project's docs folder
2. Follow `TEMPLATE_INSTRUCTIONS.md` (see below)
3. Populate each section with your project data
4. Use as living document during integration planning

**Outputs:** Integration plan with timelines, data acquisition priorities, and service account roadmap

**Example:** See `../Madagascar/docs/data_flow_condition_to_services.md` in the AFRICA — accounts project

---

### `TEMPLATE_INSTRUCTIONS.md`

**Purpose:** Step-by-step guide for using the data flow template.

**Covers:**
- How to find and replace placeholders
- Section-by-section instructions with examples
- Common pitfalls to avoid
- Quality assurance checklist
- Reference to worked example project

**Read this first** before starting the data flow template.

---

## Other Recommended Templates (To Be Created)

The following templates would be useful additions to this folder:

### 1. **Condition Account Template** (Planned)
- Project-specific condition measurement checklist
- Field survey data sheet template (CSV format)
- Data quality assessment form
- Reference level justification template

### 2. **Service Valuation Template** (Planned)
- Service-specific data collection form
- Market price survey template
- Willingness-to-pay survey instrument
- Cost-benefit analysis template

### 3. **SEEA EA Account Table Templates** (Planned)
- Condition account table (blank CSV with headers)
- Extent account table (blank CSV with headers)
- Service account table (physical + monetary)
- Supply and use table (cross-sector summary)

### 4. **Project Metadata Template** (Planned)
- Project description (ecosystem, scope, accounting period)
- Data provider contacts
- Reference level sources (literature, local data, models)
- Data quality documentation
- Tiered assessment justification

---

## How to Copy and Adapt a Template

### Step 1: Copy to Your Project

```bash
# Copy the template to your project folder
cp template_data_flow_condition_to_services.md /path/to/your/project/docs/
```

### Step 2: Read Instructions

Open `TEMPLATE_INSTRUCTIONS.md` and follow the step-by-step guide.

### Step 3: Find and Replace

Use your text editor to replace all [BRACKETED PLACEHOLDERS]:

**Common replacements:**
- `[PROJECT]` → Your project name
- `[ECOSYSTEM TYPE]` → e.g., "Coral reef (M1.3)"
- `[YEAR]` → Opening and closing years
- `[X sites]` → Your survey design
- `[SERVICE NAME]` → e.g., "Fisheries Nursery"

### Step 4: Populate Each Section

Work through the document systematically:
1. Part 1: Condition account outputs (use your actual data)
2. Part 2: Service requirements (refer to 04_service_accounts/ skills)
3. Parts 3–8: Mapping and planning

### Step 5: Validate

Run the QA checklist at the end of the template before finalizing.

---

## Worked Example: Madagascar Coral Reef Project

**File location:** `/Users/z5238824/Documents/GitHub/AFRICA - accounts/Madagascar/docs/data_flow_condition_to_services.md`

**What it shows:**
- All placeholders filled with real Madagascar coral reef project data
- Specific condition account outputs (fish biomass 1,928.9 kg/ha, richness 55 spp., COTS 6.7 ind/ha)
- Linkages to 3 ecosystem services (Nursery 70%, Provisioning 50%, Recreation 40%)
- Concrete data acquisition leads and timelines
- Three implementation phases with specific tasks

**Use this as a reference** when populating your own template.

---

## Integration with Other Folders

- **01_framework/**: Review tiered assessment before starting template (influence your valuation method choices)
- **02_extent_accounts/**: Your extent data inform service supply calculations (extent × per-ha rate)
- **03_condition_accounts/**: Your condition outputs populate Part 1 of this template
- **04_service_accounts/**: Service requirements documented in skills; map to your data in this template
- **05_seea_accounting_tables/**: Once you complete this template, use its outputs to structure service tables

---

## Common Questions About Templates

**Q: Can I modify the template structure?**
A: Yes. These are starting points, not rigid requirements. Adapt as needed for your ecosystem and services.

**Q: What if my project doesn't fit the template sections?**
A: The framework is flexible. Add/remove sections as needed; document why you diverged.

**Q: Should I share my completed template with others?**
A: Yes! Share it as a worked example for your ecosystem/region. It becomes a reference for future projects.

**Q: How often should I update the template?**
A: Monthly during planning phase; quarterly during implementation; archive at project end as documentation.

**Q: Can I translate the template to local languages?**
A: Yes. Create localized versions for your team and stakeholders.

---

## Template Development Roadmap

| Template | Priority | Status | Estimated Completion |
|----------|----------|--------|----------------------|
| Data flow (Condition → Services) | High | ✅ Complete | 2026-03-04 |
| Condition account table (CSV) | High | 🟡 Planned | Q2 2026 |
| Service valuation checklist | Medium | 🟡 Planned | Q2 2026 |
| SEEA EA account templates | Medium | 🟡 Planned | Q2 2026 |
| Project metadata form | Medium | 🟡 Planned | Q3 2026 |
| Satellite data processing workflow | Low | 🟡 Planned | Q3 2026 |

---

## Best Practices

✅ **Do:**
- Start with a template rather than blank pages
- Populate systematically (don't skip sections)
- Reference worked examples when stuck
- Document assumptions explicitly
- Share completed templates for feedback
- Archive final versions as project documentation

❌ **Don't:**
- Use templates without reading instructions
- Leave placeholders unfilled
- Skip the QA checklist
- Assume the template fits your project perfectly (adapt as needed)
- Forget to cite data sources and reference levels

---

## Submitting New Templates

If you develop a useful template for your project, consider contributing it back to the Accounting bot repository:

1. Generalize it (remove project-specific values)
2. Add placeholder markers [LIKE THIS]
3. Create an instructions guide
4. Worked example (filled-in version of your template)
5. Submit as pull request or contact repository maintainers

**New templates strengthen the entire ecosystem accounting community!**

---

**Related:** UN SEEA EA (2021), GOAP methodology, ecosystem accounting best practices guides
