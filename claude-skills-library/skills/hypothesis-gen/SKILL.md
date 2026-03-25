---
name: hypothesis-gen
description: Generate and refine research hypotheses from literature gaps. Applies falsifiability checks, novelty scoring, and competing hypothesis generation. Use after lit-map to formulate testable questions.
user-invocable: true
disable-model-invocation: true
---

# Hypothesis Generation

Generate research hypotheses for: **$ARGUMENTS**

## Prerequisites
This skill works best after running `/lit-map` to identify gaps. If no lit-map exists, discuss the research context with the human first.

## Process

### Step 1: Review Available Evidence
- Read the literature map (if available)
- Identify the specific gaps and debates that could generate hypotheses
- Discuss with the human which gaps are most interesting/feasible

### Step 2: Generate Candidate Hypotheses
For each promising gap, generate 2-3 candidate hypotheses.

For each hypothesis, provide:

```markdown
### Hypothesis [N]: [Statement]

**Type:** [Directional / Non-directional / Null]
**Based on:** [Which gap or debate from the lit-map]

**Falsifiability Check:**
- Can this be disproven? [Yes/No — if No, revise]
- What evidence would falsify it? [specific]
- What evidence would support it? [specific]

**Novelty Assessment:**
- Has this been tested before? [Yes/Partially/No]
- If partially: what's different about this formulation?
- Novelty score: [Low/Medium/High]

**Feasibility Assessment:**
- Data requirements: [what data is needed]
- Methodology: [how would you test this]
- Resources needed: [time, access, tools]
- Feasibility score: [Low/Medium/High]

**Competing Hypotheses:**
- Alternative explanation 1: [different hypothesis for the same phenomenon]
- Alternative explanation 2: [another alternative]
- How to distinguish: [what test would differentiate between them]
```

### Step 3: Rank and Discuss
Present hypotheses ranked by a combined score:
- **Priority = Novelty x Feasibility x Importance**
- Discuss with the human which to pursue
- Refine wording based on feedback

### Step 4: Formalize
Write the approved hypothesis/hypotheses in formal academic language:
- Specific, measurable, testable
- Connected to the theoretical framework
- Clear independent and dependent variables identified

## Rules
- ALWAYS generate competing hypotheses — avoid confirmation bias from the start
- A hypothesis that cannot be falsified is not a hypothesis — revise it
- The human makes the final decision on which hypotheses to pursue
- Flag when a hypothesis requires resources beyond what's likely available
- Never present a single hypothesis as "the answer" — research is about testing, not confirming
