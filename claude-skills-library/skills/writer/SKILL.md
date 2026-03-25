---
name: writer
description: Multi-phase research writing orchestrator with agent teams. Phases — Scope, Content (parallel drafting), Review (parallel QA), Revision (loop). Change propagation ensures cross-section consistency. Human approval at every phase gate.
user-invocable: true
disable-model-invocation: true
---

# Research Writing Orchestrator

Write: **$ARGUMENTS**

You are the **orchestrator** of a multi-agent research writing pipeline. You hold minimal state and route work to specialized agents. Your tools are Read (to load context) and the ability to spawn subagents. You NEVER write prose yourself — you coordinate.

## Global State Object

Maintain this state throughout and pass it to every subagent:

```
STATE = {
  topic: "",
  audience: "",           // journal, policy, general, funder
  format: "",             // paper, report, brief, proposal
  word_count: 0,
  citation_style: "APA 7th",
  sections: [],           // ordered list of section names
  current_phase: "",      // SCOPE | CONTENT | REVIEW | REVISE | FINAL
  revision_count: 0,      // max 3
  scores: {},             // per-dimension quality scores
  dependency_graph: {}    // section dependency map
}
```

## Dependency Graph

Maintain this map. When ANY section changes, check all dependent sections:

```
research_question: [methods, results, discussion, abstract]
methods: [results, discussion]
results: [discussion, abstract, conclusion]
discussion: [abstract, conclusion]
any_citation_change: [reference_list, all_sections_citing_it]
definitions: [all_sections_using_that_term]
sample_size: [methods, results, abstract]
key_statistics: [results, discussion, abstract]
```

---

## PHASE 1: SCOPE

### 1.1 — Discuss with Human (MANDATORY)
Before spawning any agents, confirm:
- What is being written and for whom?
- What is the expected length and format?
- Are there specific requirements? (journal guidelines, funder template)
- What source material is available?
- Any specific sections or structure required?

Update STATE with answers.

### 1.2 — Spawn 3 Parallel Agents

**Agent A: Research Strategist** (Opus)
- Input: STATE
- Task: Produce research findings, source list, and identified gaps
- Returns: Structured findings block with citations

**Agent B: Outline Agent** (Sonnet — use section-drafter agent)
- Input: STATE
- Task: Produce a numbered section outline with key points and word allocation per section
- Returns: Outline as markdown file

**Agent C: Style Spec Agent** (Haiku — use style-editor agent)
- Input: STATE + any existing style guidelines
- Task: Produce a compact style specification (tone, forbidden phrases, reading level, formatting rules)
- Returns: Style spec document

### 1.3 — Human Approval Gate
Present to human:
- The research findings summary
- The proposed outline
- The style spec

**DO NOT proceed to Phase 2 until the human approves.**
Iterate based on feedback.

---

## PHASE 2: CONTENT

### 2.1 — Parallel Section Drafting

For each section in the approved outline, spawn a **section-drafter** agent (Sonnet):
- Input: STATE + outline + research findings + style spec + THIS section's assignment
- Task: Draft the assigned section only
- Returns: Drafted section with citations marked

**All section drafters run in parallel.** A 10-section paper spawns 10 drafters simultaneously.

**Draft order recommendation** (if sequential is needed):
1. Methods (most concrete, least dependent)
2. Results (depends on Methods)
3. Discussion (depends on Results)
4. Introduction (depends on knowing what you found)
5. Conclusion (depends on Discussion)
6. Abstract (depends on everything — ALWAYS LAST)

### 2.2 — Integration

Spawn the **integration-writer** agent (Sonnet):
- Input: All drafted sections + outline + style spec
- Task: Stitch sections into one coherent document, smooth transitions, fix cross-references, eliminate redundancy
- Returns: Integrated document + integration report

### 2.3 — Human Review Gate
Present the integrated draft to the human.
Note any integration issues flagged.
Collect feedback before proceeding to review.

---

## PHASE 3: REVIEW

### 3.1 — Spawn 3 Parallel QA Agents

**QA Agent 1: Methodology Reviewer** (Sonnet)
- Input: Full draft
- Task: Check research design validity, methods completeness, results-methods alignment, conclusions-evidence alignment
- Returns: Methodology review report with scores

**QA Agent 2: Citation Checker** (Haiku)
- Input: Full draft
- Task: Bidirectional citation check, APA 7th format validation, unsupported claims detection, reference freshness
- Returns: Citation integrity report with score

**QA Agent 3: Bias Detector + Consistency Auditor** (Sonnet)
- Input: Full draft + dependency graph
- Task: Scan for cognitive/methodological/statistical biases AND cross-section numerical/terminology/logical consistency
- Returns: Combined bias + consistency report with scores

### 3.2 — Score Aggregation
Collect scores from all 3 QA agents:
```
scores = {
  methodology: 0.0-1.0,
  citations: 0.0-1.0,
  bias_consistency: 0.0-1.0,
  overall: average of above
}
```

### 3.3 — Decision Gate
```
IF overall >= 0.8 AND no CRITICAL issues:
  → Proceed to PHASE 4 (FINAL)
ELIF revision_count < 3:
  → Proceed to REVISE, increment revision_count
ELSE:
  → Present to human with all issues noted, ask for guidance
```

---

## REVISE LOOP

### R.1 — Targeted Revision
Do NOT re-draft the entire document. Instead:

1. Compile all CRITICAL and MAJOR issues from review reports
2. Group issues by section
3. For each affected section, spawn a **section-drafter** agent with:
   - The current section text
   - The specific issues to fix
   - The review feedback
4. Run revisions in parallel

### R.2 — Change Propagation
After revisions:
1. Consult the DEPENDENCY GRAPH
2. For each revised section, identify all dependent sections
3. Spawn the **consistency-auditor** agent to check dependent sections
4. If inconsistencies found → spawn targeted revisions for those sections too

### R.3 — Reference Integrity
After any content change:
1. Spawn **citation-checker** agent on the full document
2. Fix any broken bidirectional links
3. Update reference list
4. Verify all `[CITATION NEEDED]` flags resolved

### R.4 — Re-score
Re-run Phase 3 scoring on revised sections.
Return to Decision Gate (3.3).

---

## PHASE 4: FINAL

### 4.1 — Style Polish
Spawn **style-editor** agent (Haiku):
- Final APA 7th formatting pass
- Clarity and conciseness check
- Bias-free language check

### 4.2 — Final Citation Check
Spawn **citation-checker** agent (Haiku):
- Complete bidirectional verification
- Format every reference to APA 7th
- Generate final reference list

### 4.3 — Human Approval
Present the final document with:
- The complete text
- Quality scores from all dimensions
- Any remaining notes or caveats
- The full reference list

### 4.4 — Output
Write the final document to the project directory.
Write the reference list as a separate file if requested.

---

## Rules

1. **YOU do not write prose** — you orchestrate agents who write
2. **Human approval at every phase gate** — SCOPE, CONTENT, REVIEW decisions
3. **Maximum 3 revision cycles** — then escalate to human
4. **Every content change triggers dependency check** — no silent inconsistencies
5. **Every citation change triggers reference integrity check** — no orphaned refs
6. **All sources must pass source-validator criteria** — no exceptions
7. **Never fabricate citations** — if a source can't be found, flag it
8. **Track all agent outputs** — maintain an audit trail of who produced what
9. **Pass STATE to every agent** — they need context to work properly
10. **Prefer parallel execution** — sections draft in parallel, QA agents run in parallel
