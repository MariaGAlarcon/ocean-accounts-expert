---
name: systematic-review
description: Generate and execute PRISMA-compliant systematic review protocols. Covers search strategy, screening, data extraction, risk of bias assessment, and evidence synthesis. Use for formal literature reviews.
user-invocable: true
disable-model-invocation: true
---

# Systematic Review Protocol

Topic: **$ARGUMENTS**

## Process

### Step 1: Define the Protocol (DISCUSS FIRST)

Agree with the human on:

#### Research Question (use PICO/SPIDER framework)
**For quantitative reviews (PICO):**
- **P**opulation: Who/what is being studied?
- **I**ntervention/Exposure: What is being done or examined?
- **C**omparison: What is the alternative?
- **O**utcome: What is being measured?

**For qualitative reviews (SPIDER):**
- **S**ample: Who?
- **P**henomenon of **I**nterest: What?
- **D**esign: How was it studied?
- **E**valuation: What outcomes?
- **R**esearch type: Qualitative/quantitative/mixed?

#### Inclusion/Exclusion Criteria
| Criterion | Include | Exclude |
|-----------|---------|---------|
| Study design | [types] | [types] |
| Population | [characteristics] | [characteristics] |
| Intervention | [types] | [types] |
| Outcome | [measures] | [measures] |
| Date range | [from-to] | [outside range] |
| Language | [languages] | [others] |
| Publication type | [types] | [grey lit?] |

### Step 2: Search Strategy
Spawn the `literature-searcher` agent with the protocol.

**Required databases** (minimum 3):
- PubMed/MEDLINE
- Google Scholar or Semantic Scholar
- At least one field-specific database

**Search string documentation:**
- Full Boolean search string for each database
- MeSH terms / controlled vocabulary used
- Filters applied

### Step 3: Screening

#### Title/Abstract Screening
For each result, apply inclusion/exclusion criteria:
- INCLUDE: Meets all inclusion criteria
- EXCLUDE: Fails any criterion (record WHICH criterion)
- UNCERTAIN: Proceed to full-text review

#### Full-Text Screening
- Read full text of included + uncertain results
- Apply criteria again with full information
- Record exclusion reasons

### Step 4: Data Extraction
Spawn the `data-extractor` agent with extraction template.

Standard extraction fields:
- Study characteristics (author, year, country, design)
- Participant characteristics (N, demographics)
- Intervention/exposure details
- Outcome measures and results
- Risk of bias indicators
- Funding and conflicts of interest

### Step 5: Risk of Bias Assessment

**For RCTs:** Use Cochrane Risk of Bias tool (RoB 2)
- Randomization process
- Deviations from intended interventions
- Missing outcome data
- Measurement of the outcome
- Selection of the reported result

**For observational studies:** Use Newcastle-Ottawa Scale (NOS)
- Selection (4 items)
- Comparability (1 item)
- Outcome/Exposure (3 items)

**For qualitative studies:** Use CASP Qualitative Checklist
- Clear research aims?
- Appropriate methodology?
- Appropriate research design?
- Appropriate recruitment strategy?
- Appropriate data collection?
- Relationship between researcher and participants?
- Ethical considerations?
- Rigorous data analysis?
- Clear findings?
- Valuable research?

### Step 6: Evidence Synthesis

**Narrative synthesis** (always):
- Organize findings by theme or outcome
- Note patterns across studies
- Identify heterogeneity and possible explanations

**Meta-analysis** (if appropriate):
- Only if studies are sufficiently homogeneous
- Report: effect size, confidence interval, I² heterogeneity
- Create forest plot specification (via `diagram-maker`)
- Assess publication bias (funnel plot)

### Step 7: PRISMA Flow Diagram
Spawn `diagram-maker` agent to create the PRISMA flow diagram with actual numbers.

### Step 8: Produce the Review
Structure the output following PRISMA 2020 checklist:
1. Title
2. Abstract (structured)
3. Introduction (rationale, objectives)
4. Methods (protocol, search strategy, selection, extraction, synthesis)
5. Results (study selection, characteristics, risk of bias, synthesis)
6. Discussion (summary, limitations, implications)
7. References

### Step 9: PRISMA-trAIce Compliance
Since AI assisted this review, include transparency statement:
- Which steps were AI-assisted
- Which were human-verified
- What AI tools were used
- Limitations of AI assistance

## Rules
- Document EVERY decision for reproducibility
- The human must approve the protocol before searching begins
- The human must verify screening decisions for borderline cases
- NEVER fabricate study results or citations
- Flag when too few studies exist for meaningful synthesis
- All sources must pass source-validator criteria
