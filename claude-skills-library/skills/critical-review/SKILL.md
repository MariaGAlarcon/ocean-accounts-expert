---
name: critical-review
description: Structured critical appraisal of a research paper, report, or argument. Uses CASP, STROBE, CONSORT checklists per study type. Evaluates methodology, evidence strength, bias, and generalizability.
user-invocable: true
disable-model-invocation: true
---

# Critical Review

Critically appraise: **$ARGUMENTS**

## Process

### Step 1: Identify Study Type
Determine the appropriate appraisal framework:

| Study Type | Checklist |
|-----------|-----------|
| Randomized trial | CONSORT + Cochrane RoB 2 |
| Observational (cohort/case-control) | STROBE + Newcastle-Ottawa |
| Cross-sectional | STROBE (adapted) |
| Qualitative | CASP Qualitative |
| Systematic review | PRISMA + AMSTAR 2 |
| Mixed methods | MMAT |
| Economic evaluation | CHEERS |
| Diagnostic accuracy | STARD |

### Step 2: Apply Checklist

#### CASP Generic Questions (applicable to all):
1. Was there a clear statement of the aims?
2. Is the methodology appropriate?
3. Was the research design appropriate to address the aims?
4. Was the recruitment strategy appropriate?
5. Was the data collected in a way that addressed the research issue?
6. Has the relationship between researcher and participants been adequately considered?
7. Have ethical issues been taken into consideration?
8. Was the data analysis sufficiently rigorous?
9. Is there a clear statement of findings?
10. How valuable is the research?

#### Additional for Quantitative:
- Sample size justified?
- Appropriate statistical tests used?
- Effect sizes and confidence intervals reported?
- Confounders identified and controlled?
- Results clinically/practically significant?

#### Additional for Qualitative:
- Reflexivity addressed?
- Data saturation discussed?
- Participant quotes support interpretations?
- Negative/deviant cases discussed?
- Transferability considered?

### Step 3: Assess Evidence Strength

| Dimension | Rating | Justification |
|-----------|--------|---------------|
| Internal validity | [Strong/Moderate/Weak] | [reason] |
| External validity | [Strong/Moderate/Weak] | [reason] |
| Methodology rigor | [Strong/Moderate/Weak] | [reason] |
| Analysis quality | [Strong/Moderate/Weak] | [reason] |
| Reporting quality | [Strong/Moderate/Weak] | [reason] |

### Step 4: Run Bias Detection
Apply the bias-check criteria to the specific paper.

### Step 5: Produce the Appraisal

```markdown
# Critical Appraisal: [Paper Title]
*Author(s), Year, Journal*

## Summary
[2-3 sentence summary of what the paper does and finds]

## Strengths
1. [strength with specific reference]
2. [strength]
3. [strength]

## Weaknesses
1. [weakness with specific reference and why it matters]
2. [weakness]
3. [weakness]

## Methodology Assessment
[Detailed evaluation using the appropriate checklist]

## Evidence Strength
[Rating table from Step 3]

## Bias Assessment
[Key biases identified]

## Applicability
- **To your research:** [how relevant is this to your work]
- **Generalizability:** [can findings be applied beyond the study context]
- **Recency:** [is this still current given field developments]

## Overall Verdict
**Quality:** [High / Moderate / Low]
**Recommend including in research:** [Yes / Yes with caveats / No]
**Key caveat:** [the most important limitation to note if citing this paper]
```

## Rules
- Be fair — every study has limitations; the question is whether they matter
- Distinguish between fatal flaws and acceptable limitations
- Consider the study in the context of when it was conducted
- Evaluate the paper on its own terms first, then against external standards
- The human decides whether to include/exclude — you provide the assessment
