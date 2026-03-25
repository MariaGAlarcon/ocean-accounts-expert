---
name: web-research
description: Execute web searches with strict source quality criteria. Prioritizes government, institutional, and peer-reviewed sources. Rejects unverified sites. Use for any online information gathering.
user-invocable: true
---

# Web Research with Source Quality Control

Research topic: **$ARGUMENTS**

## Source Priority Hierarchy

When searching the web, prioritize sources in this strict order:

### Tier 1 — Always Preferred
- **Government sources**: .gov, .gov.au, .gov.uk, official statistical offices
- **Intergovernmental organizations**: UN agencies, World Bank, OECD, WHO, FAO, IPCC
- **Peer-reviewed journals**: accessed via PubMed, Google Scholar, Semantic Scholar

### Tier 2 — Acceptable
- **University/research institutions**: .edu, .ac.uk, research institute websites
- **Established professional bodies**: national academies, professional associations
- **Reputable news with named sources**: for current events ONLY (Reuters, AP, BBC)

### Tier 3 — Use with Caution (flag explicitly)
- **Preprints**: arXiv, SSRN, bioRxiv — label as "not peer-reviewed"
- **Reports from credible NGOs**: WWF, IUCN, Pew Research — check methodology
- **Technical documentation**: official docs for tools and software

### REJECT — Never Use as Sources
- Personal blogs and opinion sites
- Forums (Reddit, Quora, Stack Exchange) — as primary sources
- Wikipedia — as a primary source (acceptable to find original references)
- Commercial sites selling products/services
- AI-generated content aggregators
- Social media posts
- Sites with no identifiable author or institution
- Sites that don't cite their own sources

## Search Strategy

### For Academic/Scientific Topics:
1. Search Google Scholar or Semantic Scholar first
2. Search PubMed for health/bio/environmental topics
3. Search specific databases relevant to the field
4. Use government statistical databases for data
5. Forward/backward citation tracking on key papers

### For Policy/Data Topics:
1. Search official government databases first
2. Check intergovernmental organization repositories
3. Search for official statistics and datasets
4. Supplement with peer-reviewed analysis

### Search Execution:
- Use specific search operators: `site:.gov`, `filetype:pdf`, date ranges
- Search with multiple query formulations
- Prefer recent sources (last 5 years) unless foundational
- When a source cites a statistic, trace it to the ORIGINAL source

## For Every Source Found, Validate:
1. **Who published it?** (institutional credibility)
2. **When?** (recency)
3. **Is it peer-reviewed?** (quality control)
4. **Does it cite its own sources?** (evidence-based)
5. **Is it the PRIMARY source?** (not a summary of someone else's work)

## Output Format
Present findings with full source attribution:
```
**Finding:** [what was found]
**Source:** [Author/Org (Year). Title. Publisher/Journal. URL]
**Evidence Level:** [Tier 1/2/3]
**Peer-reviewed:** [Yes/No]
```

## Core Rule
**If you cannot find a credible source for a claim, say "I could not verify this" rather than using a low-quality source.** No source is better than a bad source.
