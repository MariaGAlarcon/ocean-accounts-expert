# Consistency Audit: Tuvana Social Accounts

**Audit date:** 2026-04-22
**Scope:** All tables in ideal-pilot/ (country profile, tables 01 through 04)
**Method:** Cross-reference all numbers across files, test accounting identities, check for double counting

---

## Results summary

| Check | Tests | Pass | Fail | Partial |
|---|---|---|---|---|
| Supply = Use identities | 4 | 3 | 0 | 1 |
| Double counting (subsistence) | 3 | 2 | 1 | 0 |
| Cross-BSU flow consistency | 2 | 1 | 1 | 0 |
| Stock identities | 3 | 3 | 0 | 0 |
| Cross-domain consistency | 4 | 1 | 2 | 1 |
| Terminology | 1 | 1 | 0 | 0 |
| **Total** | **17** | **11** | **4** | **2** |

---

## 1. Supply = Use identity (service totals)

### Fish provisioning

- Table 01 total supply: 6,421 tonnes
- Table 02 total use (household + non-HH): BSU-2 shows 505 t (302 HH + 203 non-HH), BSU-6 shows 460 t (455 HH + 5 non-HH), BSU-1 shows 25 t (17 HH + 8 non-HH)
- National identity stated in table 02: 6,421 supply = 3,820 HH + 2,601 non-HH = 6,421

**PASS.** National-level identity holds. Not all BSUs have individual use tables, so BSU-level verification is incomplete but the three shown are internally consistent.

### Gleaning

- Table 01 total supply: 100,000 kg (sum of shellfish 77,900 + sea cucumber 13,000 + seaweed 9,100 = 100,000)
- Table 02 does not have a separate gleaning use table (gleaning use table is in table 03 by gender instead)
- Table 03 total gleaning by gender: female 68,500 + male 19,400 + children 8,600 = 96,500 kg
- Table 03 note says "(exc. BSU-1,3)" suggesting BSU-1 (200 kg) and BSU-3 (3,300 kg) are excluded
- 96,500 + 200 + 3,300 = 100,000 kg

**PASS.** Identity holds when exclusion note is accounted for.

### Coastal protection

- Table 01 total protected buildings: 2,853
- Table 02 total protected buildings: 780 + 660 + 560 + 440 + 413 = 2,853

**PASS.** Identity holds exactly.

### Cultural hours

- Table 01 total cultural hours: 16,150
- Table 02 (table U5) age breakdown: youth 3,150 + adults 8,350 + elders 3,350 = 14,850
- Table U5 note says "(exc. BSU-3,4)" meaning BSU-3 (600) and BSU-4 (1,000) are excluded
- 14,850 + 600 + 1,000 = 16,450, but table 01 says 16,150

**PARTIAL PASS.** 300-hour discrepancy. The five displayed BSUs in table U5 sum to: BSU-5 (5,000) + BSU-6 (4,400) + BSU-7 (3,700) + BSU-2 (1,200) + BSU-1 (250) = 14,550. Adding excluded BSU-3 (600) + BSU-4 (1,000) = 16,150, which matches table 01. The error is in the U5 "All BSUs" row which says 16,150 but the age breakdown sums to 14,850, not 14,550. **Recommendation:** Correct the age breakdown totals in table U5 to sum to 14,550, or adjust individual age figures to match.

---

## 2. Double counting check (subsistence fish)

### Fish recorded once in supply-use table?

- Table 01: subsistence reef fish = 1,428 tonnes (by BSU)
- Table 02: subsistence fish appears in use tables as "Subsistence (own catch)" rows
- BSU-2 subsistence: 180 t. BSU-6 subsistence: 370 t. BSU-1 subsistence: 1.1 t.
- No duplicate entries found in other tables for the same physical fish

**PASS.** Physical fish recorded once.

### Activity recorded once in social flows table?

- Table 03: subsistence fishing = 151,900 hours/yr nationally
- Table 02 double counting check section cites "142,800 hours" for subsistence fishing
- Table 03 states 151,900 hours

**FAIL.** Tables 02 and 03 disagree on subsistence fishing hours (142,800 vs 151,900). The 9,100-hour gap likely reflects an earlier draft number that was not updated in table 02. **Recommendation:** Update table 02 double counting check to reference 151,900 hours (the figure from table 03).

### Food security derived, not independently counted?

- Table 04 fish consumption per capita is presented as a stock indicator (78 kg/yr for BSU-6)
- This is not also counted as a service flow; it is an outcome indicator in the social stocks table
- No double counting between service flow (tonnes) and consumption indicator (kg/capita)

**PASS.** Consumption indicator is a derived outcome, not an independent flow.

---

## 3. Cross-BSU flow consistency

### Do cross-BSU flows balance?

Table 02 lists these transfers:
- BSU-2 to BSU-1: 120 t (market)
- BSU-5 to BSU-1: 35 t (market + gifts)
- BSU-6 to BSU-1: 28 t (market + gifts)
- BSU-8 to BSU-1: 180 t (tuna processing)
- BSU-8 to export: 3,800 t

Total outflows from BSU-8: 180 + 3,800 = 3,980 t. BSU-8 supply (table 01): 4,200 t. Unaccounted: 220 t (likely sold to other BSUs or domestic markets not listed).

Total inflows to BSU-1: 120 + 35 + 28 + 180 = 363 t. BSU-1 own supply: 25 t. Total available in BSU-1: 388 t.

**PARTIAL PASS.** Flows are internally consistent (no outflow exceeds source supply) but not complete. A full reconciliation table showing all inter-BSU transfers would close the gaps. **Recommendation:** Add a complete cross-BSU fish flow matrix showing where all 6,421 tonnes end up.

### Does BSU-1 consumption match inflows?

Table 02 BSU-1 total use: 25 t (17 HH + 8 non-HH). But this appears to count only BSU-1's own supply (25 t), not the inflows (363 t from other BSUs).

**FAIL.** BSU-1 use table should reflect total consumption in BSU-1 (own catch + imports from other BSUs), not just own-supply. The 17 tonnes of household consumption in BSU-1 is far too low for a city of 68,000 people (implies 0.25 kg/capita/yr, vs 12 kg/capita/yr stated in table 04). **Recommendation:** Revise BSU-1 use table to include fish imported from other BSUs. Total BSU-1 household consumption should be approximately 68,000 x 12 kg = 816 tonnes.

---

## 4. Stock identities (opening + change = closing)

### Cooperative membership (table 04)

- National opening: 1,085
- Additions: 95
- Reductions: 25
- Closing: 1,155
- Check: 1,085 + 95 - 25 = 1,155

**PASS.** Identity holds exactly.

### FLMMA/MPA institutional capital (table 04)

- Co-management agreements: opening 4, additions 2, reductions 0, closing 6. Check: 4 + 2 - 0 = 6.
- MPAs: opening 3, additions 1, reductions 0, closing 4. Check: 3 + 1 - 0 = 4.
- MPA coverage: opening 12%, closing 15%. Change +3pp. Consistent.

**PASS.** All institutional capital stock identities hold.

### Social activity change account (table 03, table F3)

- BSU-6 subsistence fishing: 40,000 + 1,200 - 3,200 = 38,000. Check: 40,000 - 2,000 = 38,000.
- BSU-6 gleaning: 16,200 + 500 - 1,850 = 14,850. Check: 16,200 - 1,350 = 14,850.
- BSU-5 coastal monitoring: 1,800 + 600 - 0 = 2,400. Check: 1,800 + 600 = 2,400.
- BSU-7 traditional ceremonies: 22 + 0 - 2 = 20. Check: 22 - 2 = 20.

**PASS.** All activity change identities hold.

---

## 5. Cross-domain consistency

### Fish consumption per capita vs supply-use totals

BSU-6: table 04 says 78 kg/capita/yr. Population: 5,500. Implied total: 429 tonnes.
Table 02 BSU-6 household use: 455 tonnes. Per capita: 455,000 kg / 5,500 = 82.7 kg.
Table 04 says 78 kg. Discrepancy: 4.7 kg/capita (6%).

**FAIL.** BSU-6 fish per capita (78 kg in table 04) does not match the supply-use table (455 t / 5,500 pop = 82.7 kg). **Recommendation:** Reconcile by either adjusting table 04 to 83 kg/capita or adjusting table 02 household use to ~429 tonnes.

BSU-2: table 04 says 48 kg/capita/yr. Population: 12,000. Implied total: 576 tonnes.
Table 02 BSU-2 household use: 302 tonnes. Per capita: 302,000 kg / 12,000 = 25.2 kg.
Discrepancy: 22.8 kg (48 vs 25.2).

**FAIL.** Large discrepancy for BSU-2. The supply-use table shows 302 t of household consumption, implying 25 kg/capita, but the social stocks table says 48 kg/capita. This gap could be explained by fish imported from other BSUs (BSU-2 is a fishing community that also receives fish from the market), but those inflows are not documented. **Recommendation:** Either add inflow data to BSU-2 use table or adjust table 04 to match.

### Employment vs activity hours

Country profile: "Agriculture and fishing employ 35% of the rural workforce."
Table 03: total subsistence fishing hours (151,900) + gleaning hours (49,980) = 201,880 hours nationally.
Rural population: ~74,000 (BSU-2 through BSU-7). Assuming 50% working age (37,000), at 2,000 hrs/yr full-time, this implies ~100 FTE in subsistence fishing/gleaning.
Country profile does not specify total rural employment, so a full reconciliation is not possible.

**NOT FULLY TESTABLE.** Directionally consistent but cannot verify precisely without explicit employment counts by BSU.

### Reef condition in table 04 vs country profile

Country profile condition table: BSU-6 coral CI 0.71, fish biomass CI 0.75.
Table 04 dashboard: BSU-6 reef CI 0.71, fish biomass CI 0.75.

**PASS.** Condition indices are consistent across files.

---

## 6. Terminology consistency

Scanned all five files for key terms: BSU, ecosystem asset, qoliqoli, condition index, supply-use, E9, E10, FG1, FG2, SG2, SG3.

All terms are used consistently across files. No instances of conflicting definitions or naming.

**PASS.**

---

## Issues to fix (priority order)

| # | Issue | Severity | Location | Fix |
|---|---|---|---|---|
| 1 | BSU-1 use table counts only own catch (25 t), not imports from other BSUs | High | Table 02, BSU-1 section | Add imported fish; total HH consumption should be ~816 t |
| 2 | BSU-2 fish per capita: 48 kg (table 04) vs 25 kg implied by table 02 | High | Tables 02 and 04 | Reconcile: add inflows or adjust per-capita figure |
| 3 | BSU-6 fish per capita: 78 kg (table 04) vs 83 kg from table 02 | Medium | Tables 02 and 04 | Align to one consistent figure |
| 4 | Subsistence fishing hours: 142,800 (table 02) vs 151,900 (table 03) | Medium | Table 02 double counting section | Update table 02 to 151,900 |
| 5 | Cultural hours age breakdown sums to 14,850 but BSU sums to 14,550 | Low | Table 02, table U5 | Correct age-group figures |
| 6 | Cross-BSU flow matrix incomplete (220 t from BSU-8 unaccounted) | Low | Table 02 | Add complete inter-BSU transfer matrix |

---

## Overall assessment

The Tuvana social accounts demonstrate that accounting identities can hold for social data. Stock identities (opening + change = closing) pass all tests. National-level supply = use identities pass for all services. The failures are in cross-BSU reconciliation and cross-domain alignment -- the same challenges that real-world ecosystem accounts face when linking spatial data to household surveys at different resolutions.

The most important fix is #1: BSU-1 (the urban area) needs to show fish consumption from imports, not just own catch. Urban communities consume fish produced in other BSUs. This is a fundamental accounting requirement: the use table must record where consumption happens, not where production happens. The supply table records production by BSU; the use table records consumption by BSU. The cross-BSU flow matrix reconciles the two.
