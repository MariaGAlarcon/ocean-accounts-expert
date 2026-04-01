# Accounting Consistency: Do the Numbers Add Up?

This document analyses whether social accounts can maintain proper accounting identities -- the fundamental requirement for any account to be more than a dashboard of indicators. It draws on lessons from existing SEEA-EA accounts (extent, condition, services) and tests each against the social domain.

---

## What makes an account an account?

An account is not just a collection of indicators. It has three defining features:

1. **Accounting identity:** A mathematical relationship that must hold (e.g., Opening + Additions - Reductions = Closing)
2. **Double entry:** Every flow is recorded as both a supply and a use (who provides it, who receives it)
3. **Consistency across domains:** The same flow appears with the same value in connected accounts (e.g., fish provisioning in the ecosystem services account equals fish catch recorded in the economic supply-use table)

If social accounts lack these properties, they are indicator systems, not accounts. Indicator systems are useful but they do not integrate with the SNA or SEEA in the way that proper accounts do.

---

## Test 1: Stock identity (Opening + Net Change = Closing)

### Where it holds well

**Institutional capital (Table 3c):**

| Item | MPA plans | Co-management agreements | Fisheries mgmt plans |
|---|---|---|---|
| Opening stock | 4 | 3 | 2 |
| + Additions | 1 (new plan designated) | 2 (new agreements signed) | 1 (new plan adopted) |
| - Reductions | 0 | 0 | 0 |
| = Closing stock | 5 | 5 | 3 |

This works exactly as extent accounts work for area. The units are countable, the additions and reductions are identifiable events, and the identity is exact.

**Other countable stocks:**
- Fishing cooperative memberships: Opening 450 + 35 new - 12 lapsed = 473 Closing
- Recognized customary governance practices: Opening 8 + 1 new recognition = 9 Closing
- Community partnerships: Opening 12 + 3 new - 1 dissolved = 14 Closing

**Assessment:** Strong accounting identity. These are directly analogous to ecosystem extent.

### Where it holds approximately

**Human capital -- fish consumption per capita:**

| | Q1 | Q2 | Q3 | Q4 | Q5 | All |
|---|---|---|---|---|---|---|
| Opening (kg/yr) | 38 | 42 | 44 | 40 | 36 | 42 |
| Change | -3 | -2 | -1 | +1 | +2 | -0.6 |
| Closing (kg/yr) | 35 | 40 | 43 | 41 | 38 | 41.4 |

The identity holds numerically: 42 - 0.6 = 41.4. But unlike extent accounts, the "additions" and "reductions" are not discrete events -- they are net measured changes. We cannot decompose the change in Q1 consumption (-3 kg) into "fish became less available" versus "prices increased" versus "dietary preferences shifted" from the account alone.

**Assessment:** Identity holds as arithmetic but lacks the decomposition power of extent change matrices. This is closer to the condition account pattern (where CI changes are measured but not fully decomposed).

### Where it is problematic

**Social capital -- trust index:**

| | Opening | Closing | Change |
|---|---|---|---|
| Trust between communities and government | 5.2 | 5.6 | +0.4 |
| Cooperation levels | 6.1 | 5.8 | -0.3 |

The identity (5.2 + 0.4 = 5.6) holds trivially. But what does it mean? Can we say trust "increased by 0.4 units"? The index is ordinal, not ratio-scale -- a change from 5.2 to 5.6 may not represent the same real-world change as a move from 2.0 to 2.4. There are no additive "units of trust" in the way there are hectares of reef.

**Assessment:** Accounting identity is formally satisfied but lacks substantive meaning. The SEEA-EA condition index has the same issue -- a CI of 0.36 vs 0.44 is meaningful only in reference to the underlying biophysical measurement. For social indices, the underlying measurement is less well-defined.

**Recommendation:** Report index-based social stocks as measured values at opening and closing, with change and confidence interval. Do not attempt to decompose into additions and reductions. This parallels the condition account treatment.

### Summary: Stock identity

| Stock type | Identity holds? | Decomposable? | Analogous to |
|---|---|---|---|
| Countable institutional capital (plans, agreements, licences) | Yes, exactly | Yes (new, expired, revoked) | Extent accounts |
| Countable human/social capital (memberships, partnerships) | Yes, exactly | Yes (joined, left) | Extent accounts |
| Rate indicators (%, per capita) | Yes, arithmetically | Partially (numerator/denominator tracked) | Condition accounts |
| Index indicators (trust, satisfaction, connectedness) | Yes, trivially | No (ordinal scale, no discrete events) | Condition accounts (weakest form) |

---

## Test 2: Flow identity (Supply = Use)

### Where it holds well

**Social activities in hours:**

Example: Community fisheries management meetings

| | Fishing HH | Tourism HH | Other coastal | Total |
|---|---|---|---|---|
| **Supply (hours provided)** | 1,600 | 200 | 600 | 2,400 |
| **Use (hours received as benefit)** | 1,200 | 400 | 800 | 2,400 |
| | (governance voice) | (resource access security) | (community benefit) | |

Supply = Use = 2,400 hours. The identity holds because every hour supplied by a participant is an hour of governance activity that benefits someone. The allocation to "use" groups is a judgment call (who benefits from governance meetings?) but the total identity is preserved.

**Assessment:** Strong supply-use identity for hours-based activities, analogous to ecosystem services physical supply-use tables.

### Where it requires careful allocation

**Unpaid household labour: Childcare enabling ocean work**

| | Female (fishing HH) | Male (fishing HH) | Other | Total |
|---|---|---|---|---|
| **Supply (hours provided)** | 10,500 | 1,500 | 0 | 12,000 |

Who "uses" these hours? Options:
- **The children** (direct care recipients): 12,000 hours of childcare received
- **The fishing household** (household production): 12,000 hours enabling 8,000 person-days of fishing
- **The fishing industry** (economic enablement): 12,000 hours supporting industry output

Each attribution is valid but they describe different things. If we allocate all 12,000 hours to "children," the supply-use identity holds but misses the economic enablement function. If we allocate to "fishing industry," we cross the SNA production boundary.

**Recommendation:** Primary allocation to the household (consistent with SNA treatment of unpaid household work). Note the economic enablement in a memo item, not in the use table itself. This parallels how ecosystem services accounts handle intermediate services -- the nursery service is allocated to the final beneficiary (fish provisioning), not double-counted.

### Where the identity breaks

**Joint production activities:**

A traditional fishing trip is simultaneously:
- Cultural practice: 4 hours
- Knowledge transfer: 4 hours
- Food provisioning: 4 hours
- Recreation: 4 hours

Total clock time: 4 hours. Total allocated time: 16 hours. The supply-use identity breaks if we allocate to multiple categories.

**Options:**

| Approach | Supply | Use | Identity | Problem |
|---|---|---|---|---|
| A. Primary purpose | 4 hours to "cultural" | 4 hours | Holds | Misses multi-functionality |
| B. Equal split | 1 hr each to 4 categories | 4 hrs total | Holds | Arbitrary split |
| C. Full recording | 4 hrs in each category | 16 hrs total | Breaks (16 != 4) | Double counting |
| D. Matrix approach | 4 hrs, tagged with multiple purposes | 4 hrs, allocated by purpose | Holds if purposes sum to 1 | Complex but accurate |

**Recommendation:** Approach D (matrix with proportional allocation). Record the 4 hours with proportional weights: 40% cultural, 25% knowledge, 25% provisioning, 10% recreation. Supply = 4 hours total. Use = 1.6 + 1.0 + 1.0 + 0.4 = 4.0 hours. Identity holds.

This is analogous to how SNA handles multi-product establishments: output is allocated to product categories proportionally, not duplicated.

---

## Test 3: Cross-domain consistency

### Between social accounts and economic accounts (SNA)

| Social account item | SNA counterpart | Must be equal? | Alignment mechanism |
|---|---|---|---|
| Fishing household income (material wellbeing indicator) | Household sector income from fishing (SNA income account) | Yes | Same survey source, same definitions |
| Employment in ocean sectors (employment indicator) | Employment by industry (SNA labour account) | Yes | Same ISIC classifications (via TG-1.1) |
| Fish consumption per capita (food security indicator) | Household final consumption of fish (SNA use table) | Yes (market fish); No (subsistence) | Market fish from SNA; subsistence from separate survey |
| Unpaid household labour hours | SNA satellite account for unpaid work (if compiled) | Yes | Same time-use survey source |

**Assessment:** Market-based indicators can and should be drawn directly from SNA, ensuring exact consistency. Non-market indicators (subsistence, unpaid labour) require separate data sources but should use the same population definitions and classifications.

### Between social accounts and ecosystem accounts (SEEA-EA)

| Social account item | Ecosystem account counterpart | Consistency requirement |
|---|---|---|
| Fish consumption by quintile | Fish provisioning service supply | Sum of consumption across quintiles <= Total service supply |
| Gleaning hours by community | Seagrass extent and condition by BSU | Gleaning hours should correlate with seagrass condition in matched BSUs |
| Coastal protection beneficiaries | Coastal protection service value | Number of protected households consistent with spatial extent of protection |
| Ecosystem-linked social activities | Ecosystem condition index | Activities dependent on ecosystem should respond to condition changes over time |

**Assessment:** Cross-domain consistency is feasible for physical quantities (kg of fish, number of buildings) but harder for index-based measures. The strongest test is: does the sum of household-level ecosystem service use equal the total ecosystem service supply from the services account?

---

## Test 4: Lessons from existing accounts

### What transfers from extent accounts

| Extent account feature | Social account analogue | Transfer works? |
|---|---|---|
| Area-based stocks (ha) | Countable stocks (agreements, memberships) | Yes |
| Change matrix (ecosystem A to ecosystem B) | Transition matrix (household moves from Q1 to Q2) | Yes, but requires panel data |
| Managed vs natural change | Policy-driven vs demographic change | Partially (attribution harder) |
| Spatial units (BSUs) | Census/administrative units | Yes, if geocoded |

### What transfers from condition accounts

| Condition account feature | Social account analogue | Transfer works? |
|---|---|---|
| Biophysical indicators normalized to 0-1 CI | Social indicators normalized to reference level | Partially (some have reference levels, many do not) |
| Reference levels (pristine, undisturbed) | Reference levels (SDG targets, WHO thresholds) | Weaker (aspirational vs biophysical baseline) |
| Opening-closing comparison | Opening-closing comparison | Yes |
| Uncertainty propagation (SE, CI) | Uncertainty (survey sampling error) | Yes, same statistical methods |

### What transfers from services supply-use tables

| Services SUT feature | Social account analogue | Transfer works? |
|---|---|---|
| Physical supply = physical use | Hours supplied = hours used | Yes |
| Ecosystem type x service type matrix | Household group x activity type matrix | Yes |
| Monetary valuation | Monetary valuation of social activities | Possible but TG-3.5 avoids it |
| Intermediate vs final services | Enabling vs direct activities | Not well defined |

### What does NOT transfer

| Feature | Why it does not transfer |
|---|---|
| Ecosystem asset valuation (NPV of future service flows) | No agreed method for valuing social capital as an asset |
| Depletion accounting (stock loss from overuse) | Social capital can be depleted (trust erosion) but measurement is not robust enough for depletion accounts |
| Spatial continuity (every BSU has an ecosystem type) | Not every household has ocean-related social activity |
| Species-level indicators | No equivalent unit of "social biodiversity" |

---

## Overall assessment: Are social accounts feasible as proper accounts?

| Accounting requirement | Feasibility for social accounts | Strength |
|---|---|---|
| Stock identity (opening + change = closing) | Feasible for countable stocks; approximate for rates; formal-only for indices | Medium to strong |
| Flow identity (supply = use) | Feasible for hours-based activities with careful allocation rules | Strong |
| Cross-domain consistency with SNA | Feasible for market-based indicators drawn from the same surveys | Strong |
| Cross-domain consistency with SEEA-EA | Feasible for physical quantities; challenging for indices | Medium |
| Double-entry recording | Feasible for supply-use tables; not applicable to all stock indicators | Medium |
| Spatial integration | Feasible if household data can be geocoded to BSUs | Conditional |

### Verdict

Social accounts can satisfy accounting identities for a substantial subset of their indicators -- specifically the countable institutional stocks and the hours-based activity flows. These are the components that should be prioritized for pilot implementation because they genuinely integrate with the SNA and SEEA-EA.

The index-based indicators (trust, satisfaction, connectedness) are better treated as condition-style supplementary measures that accompany the accounts but do not participate in the accounting identities. This is honest and avoids forcing an accounting structure onto data that does not support it.

The strongest contribution of the social accounts framework is the **distributional supply-use table** (from File 05) -- extending the ecosystem services supply-use table with household disaggregation. This requires no new accounting identity; it simply disaggregates an existing one. If a country already compiles ecosystem services supply-use tables and household income surveys, the distributional table can be produced by linking the two.

---

## Recommended priority for pilot implementation

Based on accounting strength:

| Priority | Component | Why |
|---|---|---|
| 1 | Distributional supply-use table (File 05) | Extends existing accounts; no new identity needed; highest policy value |
| 2 | Institutional capital opening/closing account (Table 3c) | Strong identity; countable; data mostly from government records |
| 3 | Social activity supply table -- hours (Table 4a) | Strong identity; requires time-use data but structure is clear |
| 4 | Human capital opening/closing account (Table 3a) | Medium identity; relies on existing health/census/survey data |
| 5 | Social activity use table (Table 4b) | Requires allocation judgments but identity holds |
| 6 | Ecosystem-linked activity table (Table 4c) | Most innovative but most data-demanding |
| 7 | Social capital account (Table 3b) | Weakest identity; index-based; useful as supplementary measures |

---

## Open questions for further work

1. **Can social stocks be aggregated?** Ecosystem condition accounts aggregate multiple biophysical indicators into a composite CI (sometimes). Could human capital indicators be aggregated into a "human capital condition index"? The MPI (Multidimensional Poverty Index) does something similar. Is MPI-style aggregation compatible with accounting principles?

2. **Monetary valuation of social activities:** SNA satellite accounts value unpaid household work at replacement cost (what it would cost to hire someone) or opportunity cost (what the person could earn instead). Should the hours in Table 4a be valued this way? This would create a monetary social supply-use table that could be directly compared to the ecosystem services monetary table.

3. **Depletion of social capital:** Ecosystem accounts record depletion when extraction exceeds regeneration. Can the same concept apply to social capital? If trust is eroded faster than it is rebuilt, is that "social capital depletion"? How would this appear in the accounts?

4. **Panel data requirement:** Tracking household transitions across quintiles (the social equivalent of extent change matrices) requires panel survey data, which is rare. Is the change account (Table 4d) feasible without panel data, or does it require repeated cross-sections?

5. **Production boundary decisions:** Some social activities are inside the SNA production boundary (subsistence fishing as production for own final use) and some are outside (beach cleanup volunteering). The classification affects which edge (E9 or E10) the flow is assigned to. Should social accounts use the SNA production boundary or a broader boundary? TG-3.5 uses FG2 (broader), but this creates a classification inconsistency with the SNA.
