# Extent Accounts

This folder contains skills for measuring and accounting ecosystem extent (area/coverage) using satellite imagery, field surveys, and GIS analysis.

## Contents

### `skill_extent_measurement.md`
**Purpose:** Comprehensive SOP for measuring ecosystem extent (area) across coastal/marine ecosystems.

**Ecosystems covered:**
- Photic coral reefs (M1.3, M1.2)
- Mangrove forests (T2.1, T2.2)
- Seagrass meadows (M2.1, M2.2)
- Kelp forests, salt marshes, estuaries (others)

**Key topics:**
- Data sources (Sentinel-2, Landsat, Planet Labs, SRTM, aerial photography)
- Spectral classification approaches (automated vs. manual)
- Ground truthing procedures
- Accuracy assessment and uncertainty quantification
- Change detection methods
- Output: extent accounts in hectares

**Use when:**
- Starting ecosystem accounting project and need to define accounting area
- Updating extent estimates seasonally or annually
- Assessing extent change over the accounting period

---

### `skill_extent_data_pipeline.md`
**Purpose:** End-to-end data pipeline for ingesting, processing, and validating satellite imagery for extent measurement.

**Covers:**
- Data acquisition (where to download, cloud processing vs. local)
- Preprocessing (atmospheric correction, cloud masking, mosaicking)
- Classification (object detection, spectral indices, validation)
- GIS processing (vector/raster ops, area calculation)
- Quality control and metadata documentation
- Python/R workflow examples

**Use when:**
- Setting up automated or semi-automated extent measurement workflow
- Troubleshooting satellite data processing issues
- Planning computational requirements (cloud vs. local processing)

---

### `skill_extent_change_matrix_seea_account.md`
**Purpose:** Structured format for extent change accounting (transition matrix) in SEEA EA format.

**Topics:**
- Ecosystem type transitions (e.g., intact → degraded → converted)
- Transition matrix structure (opening extent × transitions × closing extent)
- Change drivers (anthropogenic vs. natural)
- Accounting period reconciliation
- Outputs: SEEA EA extent account table

**Use when:**
- Documenting how extent changed over accounting period
- Linking extent change to condition and service changes
- Preparing formal SEEA EA extent account table for reporting

---

## Workflow: From Data to SEEA EA Extent Account

```
1. Define accounting area
   └─ Use: skill_extent_measurement.md (Section 1)

2. Acquire satellite data
   └─ Use: skill_extent_data_pipeline.md (Section 2)

3. Classify ecosystem types
   └─ Use: skill_extent_measurement.md (Sections 3–4)
   └─ Use: skill_extent_data_pipeline.md (Sections 3–5)

4. Assess accuracy
   └─ Use: skill_extent_measurement.md (Section 5)

5. Calculate change
   └─ Use: skill_extent_change_matrix_seea_account.md (Sections 1–2)

6. Produce SEEA EA extent account
   └─ Use: skill_extent_change_matrix_seea_account.md (Section 3)
```

---

## Key Decisions You'll Face

| Decision | Guidance |
|----------|----------|
| **Satellite sensor choice** | Sentinel-2 (free, 10m, global) vs. Planet Labs (daily, 3m, commercial) vs. aerial photo (high res, local) — see skill_extent_measurement.md Section 2 |
| **Classification method** | Automated (Tier 2, faster) vs. manual digitization (Tier 3, more accurate) — see skill_extent_data_pipeline.md Section 3 |
| **Transition categories** | How finely do you split ecosystem states? (e.g., intact vs. degraded vs. converted) — see skill_extent_change_matrix_seea_account.md Section 1 |
| **Ground truthing extent** | How many field points to validate? (budget vs. accuracy) — see skill_extent_measurement.md Section 5 |

---

## Integration with Condition & Service Accounts

- **Condition accounts** (03_condition_accounts/): Extent defines the spatial scope; use satellite-derived extent polygons to stratify condition sampling
- **Service accounts** (04_service_accounts/): Service supply (kg/yr, visitors/yr, USD/yr) is multiplied by extent to calculate per-hectare or total values
- **SEEA Accounting tables** (05_seea_accounting_tables/): Extent change is the opening row; condition/service follow as dependent accounts

---

## Quick Reference: File Comparison

| Document | Scope | Detail Level | Best For |
|----------|-------|-------------|----------|
| skill_extent_measurement.md | All coastal/marine ecosystems | Comprehensive (50+ pages) | Choosing methods, implementing classification, accuracy assessment |
| skill_extent_data_pipeline.md | Satellite data processing | Technical/applied (30+ pages) | Setting up automated workflows, troubleshooting processing issues |
| skill_extent_change_matrix_seea_account.md | SEEA EA accounting format | Formal accounting (20+ pages) | Documenting transitions, producing extent account tables |

---

## Common Questions

**Q: Can I use older satellite data (Landsat archive) for historical extent?**
A: Yes. See skill_extent_measurement.md Section 2 (Historical data availability and limitations).

**Q: What resolution (meters) do I need for extent mapping?**
A: Depends on ecosystem type and patch size. For coral reefs: 10m Sentinel-2 typical; for mangroves: 3–5m recommended; see skill_extent_measurement.md Section 3.

**Q: How do I handle clouds or sensor errors in satellite data?**
A: See skill_extent_data_pipeline.md Section 2 (Cloud masking, gap-filling approaches).

**Q: Should extent transitions track degradation pathways?**
A: Yes, recommended. See skill_extent_change_matrix_seea_account.md Section 1 (Transition categories).

---

**Related:** UN SEEA EA (2021) Chapter 4, GOAP methodology, Copernicus Climate Data Store, Planet Labs API documentation
