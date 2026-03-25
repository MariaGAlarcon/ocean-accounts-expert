---
name: source-validator
description: Evaluate source credibility using evidence hierarchy, recency, citation impact, and institutional authority. Use when any external source needs quality assessment before inclusion in research.
user-invocable: true
---

# Source Validation

You are now in source validation mode. Every source presented must be rigorously evaluated before it can be included in any research output.

## Load the Source Validator Agent

Spawn the `source-validator` agent to evaluate sources. Pass it:
- The source(s) to evaluate
- The research context (topic, field, evidence standards required)

## Quick Validation (inline, no agent spawn)

For fast checks within conversation, apply this decision tree:

### Domain Check
- **ACCEPT**: .gov, .edu, .ac.uk, .org (established institutions), peer-reviewed journals, official databases (PubMed, Scopus, WoS)
- **CAUTION**: Preprints (arXiv, SSRN, bioRxiv) — flag as non-peer-reviewed
- **REJECT**: Personal blogs, forums, Reddit, Wikipedia (as primary), commercial sites, content farms, AI-generated aggregator sites, social media posts

### Evidence Hierarchy
```
Level 1: Systematic reviews & meta-analyses (STRONGEST)
Level 2: Randomized controlled trials
Level 3: Cohort studies / Government institutional data
Level 4: Case-control studies
Level 5: Cross-sectional studies
Level 6: Case reports
Level 7: Expert opinion / editorials
Level 8: Grey literature
```

### Recency & Impact
- Prefer sources from the last 5 years
- Foundational/seminal works exempt from recency requirements
- For statistics: use the most recent available dataset
- Higher citation count preferred (but recent papers naturally have fewer)

### Predatory Journal Red Flags
- No identifiable editorial board
- Rapid acceptance (<2 weeks from submission)
- Aggressive solicitation emails
- Article processing charges without transparent peer review
- Journal name similar to a reputable journal

## Output for Each Source
```
Source: [citation]
Evidence Level: [1-8]
Domain: [ACCEPT/CAUTION/REJECT]
Peer-reviewed: [Yes/No/Preprint]
Recency: [Year — OK/FLAGGED]
VERDICT: [INCLUDE / INCLUDE WITH CAVEAT / EXCLUDE]
```

## Core Rule
When in doubt, EXCLUDE. It is always better to have fewer, stronger sources than many questionable ones. Triangulate critical claims with 2+ independent sources.
