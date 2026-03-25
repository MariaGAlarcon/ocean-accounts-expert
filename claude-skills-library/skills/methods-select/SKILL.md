---
name: methods-select
description: Select and justify appropriate research methodology. Decision tree for study design, sampling, analysis, and threats to validity. Use after hypothesis formulation.
user-invocable: true
disable-model-invocation: true
---

# Methodology Selection

Select methodology for: **$ARGUMENTS**

## Process

### Step 1: Understand the Research Question
Discuss with the human:
- What type of question? (descriptive, comparative, causal, exploratory)
- What are the key variables? (IV, DV, controls, mediators, moderators)
- What is the unit of analysis? (individual, group, organization, country)
- What constraints exist? (time, budget, access, ethics)

### Step 2: Study Design Decision Tree

```
Question Type?
├── Descriptive ("What is X?")
│   ├── Quantitative → Survey / Cross-sectional study
│   ├── Qualitative → Case study / Ethnography / Phenomenology
│   └── Mixed → Sequential or concurrent design
│
├── Comparative ("Is X different from Y?")
│   ├── Can you randomize? → YES → Experimental (RCT)
│   ├── Can you randomize? → NO
│   │   ├── Can you measure before/after? → Quasi-experimental
│   │   └── One time point only → Cross-sectional comparative
│   └── Comparing across contexts → Comparative case study
│
├── Causal ("Does X cause Y?")
│   ├── Can you manipulate X? → YES → Experimental
│   ├── Can you manipulate X? → NO
│   │   ├── Longitudinal data available? → Panel / cohort study
│   │   └── Cross-sectional only → Correlational (acknowledge limitation)
│   └── Natural experiment available? → Natural experiment / DID
│
└── Exploratory ("What's going on with X?")
    ├── Little prior research → Grounded theory
    ├── Understanding experiences → Phenomenology
    ├── Understanding processes → Case study / Process tracing
    └── Building theory → Abductive analysis
```

### Step 3: Present Options
For each viable design, present:

```markdown
### Option [N]: [Design Name]

**Strengths:**
- [strength 1]
- [strength 2]

**Limitations:**
- [limitation 1]
- [limitation 2]

**Data Requirements:**
- Sample: [type, size, access]
- Instruments: [surveys, interviews, observations]
- Duration: [data collection timeline]

**Threats to Validity:**
- Internal: [specific threats]
- External: [generalizability limits]
- Construct: [measurement concerns]

**Sampling Strategy:**
- Recommended: [probability/non-probability method]
- Minimum N: [based on power analysis or saturation]
- Recruitment: [how to access participants/data]

**Analysis Approach:**
- Primary: [statistical test or qualitative method]
- Software: [recommended tools]

**Feasibility:** [High/Medium/Low given constraints]
```

### Step 4: Discuss Tradeoffs
Present a comparison table:
| Criterion | Option A | Option B | Option C |
|-----------|----------|----------|----------|
| Internal validity | | | |
| External validity | | | |
| Feasibility | | | |
| Cost/Time | | | |
| Data availability | | | |

### Step 5: Formalize
Once the human decides, produce a methods section outline ready for the writer skill.

## Rules
- ALWAYS present at least 2 options — methodology is a choice, not a given
- Be honest about tradeoffs — no design is perfect
- Match the method to the question, not the other way around
- Flag when the research question needs reformulation to be answerable
- The human makes the final decision
