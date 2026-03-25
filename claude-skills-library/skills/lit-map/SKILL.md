---
name: lit-map
description: Map the structure of a research field — identify concept clusters, citation networks, research gaps, active debates, and understudied intersections. Use before deep literature review.
user-invocable: true
disable-model-invocation: true
---

# Literature Mapping

Map the research landscape for: **$ARGUMENTS**

## Process

### Step 1: Define the Field Boundaries
Discuss with the human:
- What is the core topic/field?
- How broad or narrow should the map be?
- Are there specific sub-topics to prioritize?
- What time period should the map cover?

### Step 2: Systematic Search
Spawn the `literature-searcher` agent to find key papers across:
- PubMed, Google Scholar, Semantic Scholar
- Target: 20-50 key papers that represent the field structure

### Step 3: Source Validation
Run all found sources through the `source-validator` agent criteria.

### Step 4: Build the Map

Produce a structured literature map:

```markdown
# Literature Map: [Topic]
*Generated: [date]*

## 1. Field Overview
[2-3 paragraph summary of the research landscape]

## 2. Concept Clusters
### Cluster A: [Theme Name]
- **Key papers:** [3-5 citations]
- **Core argument:** [what this stream says]
- **Methodological approach:** [how they study it]
- **Maturity:** [Emerging / Established / Mature / Declining]

### Cluster B: [Theme Name]
[same structure]

### Cluster C: [Theme Name]
[same structure]

## 3. Seminal Works
[Papers that MUST be cited — foundational to the field]

## 4. Active Debates
### Debate 1: [Topic]
- **Position A:** [argument + key proponents]
- **Position B:** [counter-argument + key proponents]
- **Current status:** [who's winning, or unresolved]

## 5. Research Gaps
### Gap 1: [Description]
- **What's missing:** [specific question not adequately addressed]
- **Why it matters:** [significance]
- **Feasibility:** [could this be studied? how?]

## 6. Methodological Trends
- **Dominant methods:** [what most studies use]
- **Emerging methods:** [new approaches gaining traction]
- **Methodological gaps:** [approaches not yet applied]

## 7. Temporal Trends
- **Key shifts:** [how the field has evolved]
- **Recent surge areas:** [topics with increasing publication rates]
- **Declining areas:** [topics losing attention]

## 8. Key Journals & Venues
[Where this research is published]
```

### Step 5: Visualize
Use the `diagram-maker` agent to create:
- A concept map showing cluster relationships
- A timeline of key publications
- A gap matrix (themes × methods)

### Step 6: Review with Human
Present the map for feedback. Iterate as needed.

## Rules
- This is a MAP, not a review — breadth over depth
- Flag areas where your knowledge may be incomplete
- Distinguish between "no research exists" and "I couldn't find research"
- Include contradictory findings — don't smooth over disagreements
- All sources must pass source-validator criteria
