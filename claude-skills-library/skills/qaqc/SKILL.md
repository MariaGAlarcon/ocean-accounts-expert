---
name: qaqc
description: Quality assurance and quality control check on any research output. Validates source accuracy, citation integrity, logical consistency, numerical agreement, completeness, and unsupported claims.
user-invocable: true
---

# Quality Assurance / Quality Control

Review this output for quality: **$ARGUMENTS**

## QA/QC Checklist

Run these checks in order. For each, assign: PASS / FLAG / FAIL.

### 1. Source Quality
- [ ] All sources pass source-validator criteria
- [ ] No rejected source types used (blogs, forums, Wikipedia as primary)
- [ ] Evidence hierarchy levels appropriate for claims made
- [ ] Critical claims supported by 2+ independent sources
- [ ] Sources are sufficiently recent for the field

### 2. Citation Integrity
Spawn `citation-checker` agent or check inline:
- [ ] Every in-text citation has a reference list entry
- [ ] Every reference list entry is cited in text
- [ ] APA 7th format is correct
- [ ] No fabricated citations
- [ ] Direct quotes have page numbers

### 3. Numerical Consistency
- [ ] Numbers in Abstract match numbers in Results
- [ ] Sample sizes consistent across Methods, Results, tables
- [ ] Percentages add up correctly
- [ ] Statistics reported correctly (df, p-values, effect sizes)
- [ ] Table/figure values match text descriptions
- [ ] Units are consistent throughout

### 4. Logical Consistency
- [ ] Conclusions follow from the evidence presented
- [ ] No claims that go beyond what the data supports
- [ ] Causal language only used when design supports it
- [ ] Limitations acknowledged appropriately
- [ ] No contradictions between sections

### 5. Completeness
- [ ] All research questions addressed
- [ ] All methods described produce corresponding results
- [ ] All results discussed in Discussion
- [ ] Key terms defined on first use
- [ ] Acronyms expanded on first use

### 6. Unsupported Claims
Scan for statements that lack evidence:
- "Studies show..." without specific citations
- Statistics without attribution
- Broad generalizations without evidence
- "It is well known that..." without reference

### 7. Bias Check
- [ ] Alternative interpretations considered
- [ ] Counter-evidence acknowledged
- [ ] Language is appropriately hedged
- [ ] No cherry-picking of favorable results
- [ ] Limitations are genuine (not pro forma)

## Output Format

```
QA/QC REPORT
=============
Document: [title/description]
Date: [review date]

OVERALL GRADE: [A/B/C/D/F]
  A = Publication ready
  B = Minor revisions needed
  C = Major revisions needed
  D = Significant issues
  F = Fundamental problems

CHECKLIST RESULTS:
  Source Quality:      [PASS/FLAG/FAIL]
  Citation Integrity:  [PASS/FLAG/FAIL]
  Numerical Consistency: [PASS/FLAG/FAIL]
  Logical Consistency: [PASS/FLAG/FAIL]
  Completeness:        [PASS/FLAG/FAIL]
  Unsupported Claims:  [PASS/FLAG/FAIL]
  Bias Check:          [PASS/FLAG/FAIL]

ISSUES FOUND:
1. [CRITICAL] [description + location + fix]
2. [MAJOR] [description + location + fix]
3. [MINOR] [description + location + fix]

STRENGTHS:
- [what's good about this output]
```

## Rules
- Be thorough but fair — not every imperfection is a failure
- Distinguish between CRITICAL (must fix), MAJOR (should fix), MINOR (nice to fix)
- Provide specific fixes, not just complaints
- Check the ENTIRE document, not just a sample
