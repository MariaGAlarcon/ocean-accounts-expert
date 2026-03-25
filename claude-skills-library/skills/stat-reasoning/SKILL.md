---
name: stat-reasoning
description: Statistical analysis guidance — test selection, assumption checking, effect size interpretation, power analysis, and pitfall detection. Use when choosing or evaluating statistical methods.
user-invocable: true
---

# Statistical Reasoning

Analyze: **$ARGUMENTS**

## Spawn the stat-reasoner agent for complex analyses.

For quick guidance within conversation, use this framework:

## Test Selection Quick Reference

### Comparing Groups
| Situation | Parametric | Non-parametric |
|-----------|-----------|---------------|
| 2 independent groups | Independent t-test | Mann-Whitney U |
| 2 paired groups | Paired t-test | Wilcoxon signed-rank |
| 3+ independent groups | One-way ANOVA | Kruskal-Wallis |
| 3+ repeated measures | RM-ANOVA | Friedman |
| 2+ factors | Factorial ANOVA | — |

### Relationships
| Situation | Test |
|-----------|------|
| 2 continuous variables | Pearson r (or Spearman rho) |
| 2 categorical variables | Chi-square |
| Predicting continuous outcome | Linear regression |
| Predicting binary outcome | Logistic regression |
| Predicting counts | Poisson / Negative binomial |
| Time-to-event | Cox regression |

## Before ANY Test, Check:
1. **Normality** — Shapiro-Wilk (n<50) or Q-Q plot
2. **Variance homogeneity** — Levene's test
3. **Independence** — study design
4. **Sample size** — adequate for the test?
5. **Outliers** — identified and handled?

## Always Report:
- The test statistic with degrees of freedom
- Exact p-value (not just "p<.05")
- Effect size with interpretation
- Confidence intervals
- Sample size

## APA Reporting Templates:
- t-test: *t*(df) = X.XX, *p* = .XXX, *d* = X.XX
- ANOVA: *F*(df1, df2) = X.XX, *p* = .XXX, η² = .XX
- Correlation: *r*(df) = .XX, *p* = .XXX
- Chi-square: χ²(df, *N* = XXX) = X.XX, *p* = .XXX

## Red Flags to Watch For:
- p-values clustering just below .05
- No effect sizes reported
- Multiple comparisons without correction
- Large sample + tiny effect presented as important
- Causal language from correlational design
- "Marginally significant" (p = .06-.10)
