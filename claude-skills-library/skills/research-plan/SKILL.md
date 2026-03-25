---
name: research-plan
description: Create a structured research plan with research questions, scope, methodology, timeline, and deliverables. Use at the start of any research project to define scope and approach.
user-invocable: true
disable-model-invocation: true
---

# Research Plan Generator

Create a structured research plan for: **$ARGUMENTS**

## Process

### Step 1: Discuss Before Planning
Before creating anything, discuss with the human:
- What is the core research question or problem?
- Who is the intended audience?
- What is the expected output format? (paper, report, brief, presentation)
- What are the constraints? (timeline, word count, scope limits)
- Are there specific methodological preferences?

### Step 2: Spawn Research Strategist
Once scope is agreed, spawn the `research-strategist` agent with:
```
State: {
  topic: [agreed topic],
  audience: [target],
  format: [output type],
  constraints: [limits]
}
```

### Step 3: Present the Protocol
Present the research strategist's protocol to the human for review:
- Research questions (primary + secondary)
- In-scope vs. out-of-scope boundaries
- Recommended methodology with justification
- Key literature streams to cover
- Inclusion/exclusion criteria for sources
- Expected deliverables
- Identified risks

### Step 4: Iterate
Revise based on human feedback until approved. Then produce the final plan document:

```markdown
# Research Plan: [Title]

## 1. Background & Rationale
[Why this research matters]

## 2. Research Questions
- **RQ1 (Primary):** [question]
- **RQ2:** [question]
- **RQ3:** [question]

## 3. Scope
### In Scope
[what's included]
### Out of Scope
[what's excluded]

## 4. Methodology
[approach with justification]

## 5. Source Strategy
- **Inclusion criteria:** [what sources to use]
- **Exclusion criteria:** [what to reject]
- **Databases:** [where to search]
- **Evidence threshold:** [minimum quality level]

## 6. Deliverables
[list of outputs with format and word count]

## 7. Timeline
[phased timeline]

## 8. Risks & Mitigations
[identified risks and how to address them]
```

### Step 5: Save
Write the approved plan to the project directory as `research-plan.md`.

## Rules
- ALWAYS discuss before creating the plan
- Get explicit approval before finalizing
- The plan is a living document — it can be updated as research progresses
- Flag when scope is too broad or too narrow
