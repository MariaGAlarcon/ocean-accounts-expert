---
name: rag-schema
description: Extract structured knowledge from documents into queryable reference schemas. Supports PICO extraction, methodology summaries, and key findings databases. Use when processing source documents for research.
user-invocable: true
---

# RAG Schema Extraction

Extract structured knowledge from: **$ARGUMENTS**

## Process

### Step 1: Identify Document Type
Determine which extraction template to use:
- **Research paper** → Template A (General Research) or Template B (PICO)
- **Report/policy document** → Template D (Policy)
- **Methods paper** → Template C (Methodology)
- **Multiple documents** → Batch extraction with cross-reference table

### Step 2: Spawn Data Extractor
Spawn the `data-extractor` agent with:
- The document(s) to process
- The selected template type
- Any specific fields the human wants to prioritize

### Step 3: Extract

#### Template A: General Research Extraction
```
Source ID | Citation | Design | Setting | Population | N | Key Finding | Effect Size | Quality
```

#### Template B: PICO Extraction
```
Source ID | Population | Intervention | Comparison | Outcome | Results | Study Type
```

#### Template C: Methodology Extraction
```
Source ID | Approach | Framework | Sampling | Data Collection | Analysis | Rigor Measures
```

#### Template D: Policy Extraction
```
Source ID | Organization | Date | Scope | Key Recommendations | Evidence Base | Data Points
```

### Step 4: Build Knowledge Base
Organize extracted data into a queryable structure:

```markdown
# Knowledge Base: [Topic]
*Sources processed: [N]*
*Last updated: [date]*

## Source Index
| ID | Citation | Type | Quality |
|----|----------|------|---------|
| S1 | Author (Year) | RCT | High |
| S2 | Author (Year) | Cohort | Medium |

## Key Findings
### Theme 1: [Theme Name]
- Finding: [description] (S1, S3)
- Finding: [description] (S2)
- **Consensus:** [agreement level]

### Theme 2: [Theme Name]
[same structure]

## Contradictions & Debates
- S1 claims X, but S4 found Y. Possible explanation: [reason]

## Data Points
| Metric | Value | Source | Year | Context |
|--------|-------|--------|------|---------|
| [metric] | [value] | S1 | 2023 | [notes] |

## Gaps
- [What's not covered by these sources]
```

### Step 5: Validate
- Flag any extracted data marked as `[NOT REPORTED]` or `[AMBIGUOUS]`
- Cross-check statistics between sources
- Note when sources disagree on the same metric

## Rules
- Extract ONLY what is in the document — never infer or fabricate
- Use direct quotes with page numbers for key claims
- Preserve original units and terminology
- The knowledge base is a living document — new sources can be added
- Always note the extraction date and source access date
