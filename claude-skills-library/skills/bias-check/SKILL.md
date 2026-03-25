---
name: bias-check
description: Detect cognitive biases, methodological biases, logical fallacies, and integrity issues in research outputs. Checks for confirmation bias, p-hacking, HARKing, cherry-picking, and more.
user-invocable: true
---

# Bias Detection

Scan for biases in: **$ARGUMENTS**

## Spawn the `bias-detector` agent for comprehensive analysis.

For quick inline checks, scan for these categories:

## Quick Bias Checklist

### Cognitive Biases
- [ ] **Confirmation bias**: Only supporting evidence cited? Counter-arguments missing?
- [ ] **Anchoring**: Over-reliance on first or most prominent source?
- [ ] **Availability**: Only using easily found/memorable studies?
- [ ] **Authority bias**: Accepting claims because of who, not evidence?
- [ ] **Framing**: Results presented in only one way (e.g., only relative risk, not absolute)?

### Methodological Biases
- [ ] **Selection bias**: Non-random or biased sampling?
- [ ] **Survivorship bias**: Only analyzing successes?
- [ ] **Publication bias**: Only positive/significant results cited?
- [ ] **Measurement bias**: Instruments validated? Inter-rater reliability?
- [ ] **Observer bias**: Researcher expectations influencing data?

### Statistical Red Flags
- [ ] **p-hacking**: p-values clustering just below .05?
- [ ] **HARKing**: Hypotheses suspiciously matching results?
- [ ] **Cherry-picking**: Unexplained data exclusions? Convenient subgroups?
- [ ] **Multiple comparisons**: Many tests without correction?
- [ ] **Overfitting**: Too many predictors for sample size?

### Logical Fallacies
- [ ] **Correlation ≠ causation**: Causal claims from correlational data?
- [ ] **Ecological fallacy**: Group findings applied to individuals?
- [ ] **Circular reasoning**: Conclusion assumed in premise?
- [ ] **Straw man**: Opposing views misrepresented?
- [ ] **Hasty generalization**: Broad claims from limited data?

## For Each Bias Found:
```
Bias: [name]
Type: [cognitive/methodological/statistical/logical]
Location: [where in the document]
Evidence: [what triggered the flag]
Severity: [Low/Medium/High]
Fix: [how to address it]
```

## Important
- Flag potential biases, don't accuse — use language like "potential" and "consider"
- Some biases are inherent to study design and can only be acknowledged, not eliminated
- The goal is awareness and transparency, not perfection
