# Template: Data Flow — Condition Accounts → Ecosystem Service Accounts
## SEEA EA Integration Framework

**Purpose:** Map condition account outputs to ecosystem service account inputs, identify coverage gaps, and establish data linkages for any coastal/marine ecosystem accounting project.

**Framework:** UN SEEA EA Sections 5 (Condition) and 6 (Services)
**Target users:** Project managers implementing SEEA EA accounting in coastal/marine ecosystems

---

## How to Use This Template

1. **Copy this file** to your project's documentation folder
2. **Replace all [BRACKETED] placeholders** with your project-specific values
3. **Update service-specific sections** based on your ecosystem type(s)
4. **Reference companion skills** (`skill_condition_*.md` and `skill_services_*.md`) from the Accounting bot repo
5. **Update as new data becomes available** — this is a living document for integration planning

---

## Executive Summary

Your **condition accounts produce [CONDITION TYPE] metrics** that directly feed into:

1. [SERVICE 1] — Input coverage: [X]%
2. [SERVICE 2] — Input coverage: [X]%
3. [SERVICE 3] — Input coverage: [X]%

**Gap:** Your condition accounts lack:
- [MISSING DATA TYPE 1]
- [MISSING DATA TYPE 2]
- [MISSING DATA TYPE 3]

---

## Part 1: Condition Account Outputs

### Current Outputs by Ecosystem

**Ecosystem Asset:** [ECOSYSTEM TYPE CODE, e.g., M1.3 Coral reef]
**Survey coverage:** [X sites, Y transects/sampling units]
**Accounting period:** [YEAR] – [YEAR]
**Spatial extent:** [X hectares / square km]

### 1a. [PRIMARY INDICATOR GROUP] — Indicators

| Indicator | Unit | Reference Level | Mean (Year 1) | Range | Notes |
|-----------|------|-----------------|---------------|-------|-------|
| **[INDICATOR 1]** | [UNIT] | [REF] | [VALUE] | [MIN–MAX] | [NOTES] |
| **[INDICATOR 2]** | [UNIT] | [REF] | [VALUE] | [MIN–MAX] | [NOTES] |
| **[INDICATOR 3]** | [UNIT] | [REF] | [VALUE] | [MIN–MAX] | [NOTES] |

**Available sub-categories:**
- [CATEGORY A] ([X]%)
- [CATEGORY B] ([X]%)
- [CATEGORY C] ([X]%)

### 1b. [SECONDARY INDICATOR GROUP] — Indicators

| Indicator | Unit | Measured Value (Mean Year 1) | Notes |
|-----------|------|---------------------------|-------|
| **[INDICATOR 1]** | [UNIT] | [VALUE] | [NOTES] |
| **[INDICATOR 2]** | [UNIT] | [VALUE] | [NOTES] |

### 1c. Output Files

**Raw values:**
- `[output_file_1.csv]` — [description]
- `[output_file_2.csv]` — [description]

**SEEA EA condition account:**
- `[output_file_3.csv]` — [description]

**Temporal scope:**
- Opening year: [YEAR]
- Closing year: [YEAR]
- Coverage: [single period / multi-year trend]

---

## Part 2: Ecosystem Service Account Input Requirements

### Service 1: [SERVICE NAME]

**SEEA EA Section:** [SECTION]
**CICES Class:** [CLASS]
**Providing ecosystems:** [ECOSYSTEM TYPES]

#### Inputs Required

| Input | Source | Your Condition Account | Gap? | Notes |
|-------|--------|------------------------|------|-------|
| **[REQUIRED INPUT 1]** | [TYPE: Condition/External/Literature] | [✅/❌] [SOURCE IF AVAILABLE] | YES/NO | [BRIEF NOTE] |
| **[REQUIRED INPUT 2]** | [TYPE] | [✅/❌] | YES/NO | [BRIEF NOTE] |
| **[REQUIRED INPUT 3]** | [TYPE] | [✅/❌] | YES/NO | [BRIEF NOTE] |

#### Calculation (Simplified)

```
[Simplified formula showing how inputs combine to produce service value]

Example: Service value = Input A × Input B × Adjustment factor
```

**Your action:**
1. [ACTION 1]
2. [ACTION 2]
3. [ACTION 3]

---

### Service 2: [SERVICE NAME]

**SEEA EA Section:** [SECTION]
**CICES Class:** [CLASS]
**Providing ecosystems:** [ECOSYSTEM TYPES]

#### Inputs Required

| Input | Source | Your Condition Account | Gap? | Notes |
|-------|--------|------------------------|------|-------|
| **[REQUIRED INPUT 1]** | [TYPE] | [✅/❌] | YES/NO | [BRIEF NOTE] |
| **[REQUIRED INPUT 2]** | [TYPE] | [✅/❌] | YES/NO | [BRIEF NOTE] |

#### How Your Condition Data Add Value

[Narrative explanation of how condition metrics support service valuation — e.g., ecosystem health informs productivity, biodiversity enhances attractiveness, etc.]

**Your action:**
1. [ACTION 1]
2. [ACTION 2]

---

### Service 3: [SERVICE NAME]

[Repeat structure above for additional services]

---

## Part 3: Data Linkages and Coverage Matrix

### Summary: Which Service Accounts Can Use Your Condition Data?

| Service Account | Data Coverage | Linkage Strength | Next Steps |
|-----------------|---------------|-----------------|----|
| **[SERVICE 1]** | [%] | [STRONG/MEDIUM/WEAK] | [ACTION ITEMS] |
| **[SERVICE 2]** | [%] | [STRONG/MEDIUM/WEAK] | [ACTION ITEMS] |
| **[SERVICE 3]** | [%] | [STRONG/MEDIUM/WEAK] | [ACTION ITEMS] |
| **[SERVICE 4]** | [%] | [STRONG/MEDIUM/WEAK] | [ACTION ITEMS] |

---

## Part 4: Detailed Data Mapping Tables

### 4a. [SERVICE NAME] — Input Checklist

```
CONDITION ACCOUNT INPUTS:
├── [INPUT STATUS: ✅/⚠️/❌] [INPUT NAME]     → [DATA SOURCE]
├── [INPUT STATUS] [INPUT NAME]              → [DATA SOURCE]
│
EXTERNAL INPUTS REQUIRED:
├── [INPUT STATUS] [INPUT NAME]              → [DATA SOURCE]
├── [INPUT STATUS] [INPUT NAME]              → [DATA SOURCE]
└── [INPUT STATUS] [INPUT NAME]              → [DATA SOURCE]

CALCULATION PATHWAY:
   [Input 1] × [Input 2] × [Factor] = [Output]
   [Example calculation with placeholder values]
```

**Data file to create:**
`[output_folder]/[service_name]_input.csv`

| Column A | Column B | Column C | Column D | Column E | Notes |
|----------|----------|----------|----------|----------|-------|
| [HEADER] | [HEADER] | [HEADER] | [HEADER] | [HEADER] | [HEADER] |
| [EXAMPLE] | [EXAMPLE] | [EXAMPLE] | [EXAMPLE] | [EXAMPLE] | [EXAMPLE] |

---

### 4b. [SERVICE NAME] — Input Checklist

[Repeat structure above for additional services]

---

## Part 5: Missing Data and Acquisition Strategy

### Priority 1: Critical for Multiple Services

| Missing Data | Why Needed | Service(s) | Acquisition Method | Timeline |
|--------------|-----------|-----------|-------------------|----------|
| **[DATA TYPE]** | [REASON] | [SERVICES] | [METHOD] | [TIMEFRAME] |
| **[DATA TYPE]** | [REASON] | [SERVICES] | [METHOD] | [TIMEFRAME] |

### Priority 2: Service-Specific Data

| Missing Data | Why Needed | Service(s) | Acquisition Method | Timeline |
|--------------|-----------|-----------|-------------------|----------|
| **[DATA TYPE]** | [REASON] | [SERVICE] | [METHOD] | [TIMEFRAME] |
| **[DATA TYPE]** | [REASON] | [SERVICE] | [METHOD] | [TIMEFRAME] |

### Priority 3: Complementary Ecosystem Data

| Missing Data | Why Needed | Service(s) | Acquisition Method | Timeline |
|--------------|-----------|-----------|-------------------|----------|
| **[DATA TYPE]** | [REASON] | [SERVICES] | [METHOD] | [TIMEFRAME] |

---

## Part 6: Recommended Implementation Pathway

### Phase 1: Immediate ([TIMEFRAME])

**Goal:** [PRIMARY GOAL FOR PHASE 1]

1. ✅ **[TASK 1]**
   - Output: `[filename.csv]`
   - Timeline: [X weeks]

2. ⚠️ **[TASK 2]**
   - Contact: [WHO TO CONTACT]
   - Output: `[filename.csv]`
   - Timeline: [X weeks]

3. ✅ **[TASK 3]**
   - Use: [WHAT TO USE IT FOR]
   - Output: `[filename.csv]`
   - Timeline: [X weeks]

### Phase 2: Medium-Term ([TIMEFRAME])

**Goal:** [PRIMARY GOAL FOR PHASE 2]

1. ⚠️ **[TASK 1]**
   - Contact: [WHO TO CONTACT]
   - Output: `[filename.csv]`
   - Timeline: [X weeks]

2. ⚠️ **[TASK 2]**
   - Contact: [WHO TO CONTACT]
   - Output: `[filename.csv]`
   - Timeline: [X weeks]

### Phase 3: Integration ([TIMEFRAME])

**Goal:** [PRIMARY GOAL FOR PHASE 3]

1. **[SERVICE NAME] Account**
   - Inputs: [LIST]
   - Output: SEEA EA service account (physical + monetary)

2. **[SERVICE NAME] Account**
   - Inputs: [LIST]
   - Output: SEEA EA service account (physical + monetary)

---

## Part 7: Template Files to Create

### Output 1: [Service Name] Service Input

**File:** `[project_folder]/03_outputs/[service_name]_input.csv`

```csv
[COLUMN HEADERS FROM YOUR CONDITION ACCOUNT]
[EXAMPLE DATA ROW]
```

### Output 2: [Service Name] Distribution

**File:** `[project_folder]/03_outputs/[data_type]_distribution.csv`

```csv
[COLUMN HEADERS]
[EXAMPLE DATA ROW]
```

### Output 3: [Service Name] Proxy Index

**File:** `[project_folder]/03_outputs/[service_name]_proxy.csv`

```csv
[COLUMN HEADERS]
[EXAMPLE DATA ROW]
```

---

## Part 8: Data Dictionary

### Condition Account Indicators → Service Account Inputs

| Condition Indicator | Unit | Service Account Use | Conversion/Notes |
|-------------------|------|-------------------|------------------|
| [INDICATOR] | [UNIT] | [SERVICE(S)] | [HOW IT'S USED] |
| [INDICATOR] | [UNIT] | [SERVICE(S)] | [HOW IT'S USED] |
| [INDICATOR] | [UNIT] | [SERVICE(S)] | [HOW IT'S USED] |

---

## Part 9: Quality Assurance Checklist

- [ ] All condition account outputs documented with units and reference levels
- [ ] Service input requirements cross-checked against skills documentation
- [ ] Coverage matrix completed for all planned services
- [ ] Missing data acquisition leads identified and contacted
- [ ] Timeline realistic given available resources
- [ ] Template CSV files created with headers and example rows
- [ ] Phase 1 tasks assigned to specific team members
- [ ] Companion condition skills linked and reviewed
- [ ] Data dictionary validated against actual condition outputs
- [ ] Document reviewed with project manager and data providers

---

## References

### Companion Skills (Accounting Bot Repository)
- `skill_condition_[TYPE].md` — [Ecosystem type] condition methodology
- `skill_services_[TYPE].md` — [Service type] service methodology
- `skill_services_measurement.md` — General services measurement overview

### SEEA EA Framework
- UN (2021). *System of Environmental-Economic Accounting — Ecosystem Accounting*. New York: United Nations.

### Project-Specific References
- [REFERENCE 1]
- [REFERENCE 2]

---

**How to maintain this document:**
- Update coverage percentages as new data becomes available
- Add completed acquisitions to the "Missing Data" sections
- Cross-reference to finalized service accounts as they are completed
- Review quarterly during implementation phases

**Next Review:** [DATE]
**Owner:** [PROJECT NAME]
**Last updated:** [DATE]
