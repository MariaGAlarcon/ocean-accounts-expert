# Workflow Guide: Social Accounts Prototype Next Steps

This document is a step-by-step guide for the next phase of work on the social accounts prototype. It is designed so that each step can be done by you (Maria), by Claude, or by both together. Each step lists what to do, what tools or skills to use, what the expected output is, and how to verify the result.

---

## Phase 1: Data Audit

**Goal:** Verify which datasets are publicly accessible for Australia and Fiji, and document access conditions.

### Step 1.1: Verify Australian data sources

**What to do:** For each row in the Australia data table in `09-next-steps-country-pilots.md`, check whether the dataset is currently downloadable.

**How to do it:**
1. Open each data portal listed (ABARES, ABS, AIMS, Tourism Research Australia, GBRMPA SELTMP).
2. Search for the specific dataset (e.g., "ABARES Fisheries Statistics" for catch data).
3. Record: (a) is it downloadable? (b) what format? (c) what spatial resolution? (d) any access restrictions?
4. If using Claude: run `/web-research` with the query "Australia [dataset name] open access download" for each source. Allow WebSearch when prompted.

**Expected output:** Updated table in `09-next-steps-country-pilots.md` with a "Verified" column and access notes.

**Verify:** Can you click through and download at least a sample file for each "Yes" entry?

### Step 1.2: Verify Fiji data sources

**What to do:** Same as 1.1 but for Fiji sources (Bureau of Statistics, SPC, FAO, MACBIO).

**How to do it:**
1. Check Fiji Bureau of Statistics website for HIES 2019-20 and Census 2017 data releases.
2. Check SPC Statistics for Development Division for PROCFish outputs.
3. Check FAO FishStatJ for Fiji fisheries data.
4. Search for MACBIO project final reports and datasets (GIZ/IUCN/SPREP).
5. If using Claude: run `/web-research` for each source.

**Expected output:** Updated Fiji table with verified access status.

**Verify:** For each "Yes" entry, confirm you can access or request the data.

### Step 1.3: Organize downloaded data

**What to do:** Create a data folder structure for pilot work.

**How to do it:**
1. Create folders:
   ```
   social-accounts-prototype/
     australia-pilot/
       data_deposit/        (raw data, gitignored)
       data_processed/      (cleaned data for tables)
       tables/              (populated accounting tables)
     fiji-pilot/
       data_deposit/
       data_processed/
       tables/
   ```
2. Add `.gitkeep` files to empty directories.
3. Add `data_deposit/` to `.gitignore` (raw data should not be committed).
4. Download verified datasets into the appropriate `data_deposit/` folder.

**Expected output:** Folder structure ready to receive data.

### Step 1.4: Document data gaps

**What to do:** For each of the 5 ecosystem services, record what data is available and what is missing.

**How to do it:**
1. Use the `/rag-schema` skill to extract key metadata from any downloaded reports or survey documentation.
2. Create a data gap table:

| Service | Data available | Data missing | Workaround |
|---|---|---|---|
| Fish provisioning | Catch data (ABARES), fish consumption (ABS HES) | Subsistence catch disaggregation | Use HIES for Fiji instead |
| ... | ... | ... | ... |

**Expected output:** Data gap table added to each country's pilot folder.

**Skill to use:** `/rag-schema` for extracting metadata from downloaded reports.

---

## Phase 2: First Worked Example (Fish Provisioning)

**Goal:** Populate the distributional supply-use table (File 05 format) for fish provisioning in one country.

### Step 2.1: Choose starting country

**What to do:** Decide whether to start with Australia or Fiji based on data audit results.

**How to do it:**
1. Use `/discuss` to weigh the tradeoffs:
   - Australia: more data, but weaker test of non-market pathways
   - Fiji: stronger conceptual test (subsistence, cultural), but data may need formal requests
2. Decision point: if Fiji HIES microdata requires a formal request, start with Australia using aggregate published data while the request is processed.

**Expected output:** Decision documented in a brief note.

### Step 2.2: Extract fish provisioning data

**What to do:** Pull catch data, consumption data, and employment data into a working spreadsheet or table.

**How to do it:**
1. From fisheries statistics: total catch by species group, commercial vs. recreational.
2. From household survey: fish consumption by income quintile, by location.
3. From labour force data: employment in fishing by gender, formality.
4. Use the `data-extractor` agent if working from PDF reports.

**Expected output:** A working data table with:
- Total fish provisioning (kg/yr) split into commercial and subsistence
- Consumption by household group (Q1 to Q5)
- Employment counts

### Step 2.3: Populate the distributional supply-use table

**What to do:** Fill in the template from File 05 with real numbers.

**How to do it:**
1. Open `05-ecosystem-to-wellbeing-links.md` and use the table at the bottom as the template.
2. Replace placeholder numbers with real data from Step 2.2.
3. Check that row totals match: total household consumption <= total service supply.
4. Save as a new file in the country pilot folder (e.g., `australia-pilot/tables/fish-provisioning-distributional-SUT.md`).

**Expected output:** A populated distributional supply-use table for fish provisioning.

**Skill to use:** Run the `consistency-auditor` agent after populating to check that numbers add up across the table.

### Step 2.4: Trace through to social conditions

**What to do:** Connect the fish provisioning data to social stock indicators.

**How to do it:**
1. From the distributional supply-use table, identify which household groups receive the most fish.
2. Link to food security indicators: fish consumption per capita by quintile vs. WHO recommended levels.
3. Link to material wellbeing: fishing household income by quintile.
4. Link to employment: jobs in fishing sector, informality rate.
5. Document each link with the edge it uses (E9, E10, E5, E6).

**Expected output:** A narrative walkthrough showing how fish provisioning flows through to social conditions, with real numbers at each step.

---

## Phase 3: Non-Market Pathway (Subsistence and Cultural Services)

**Goal:** Test the E10 non-market pathway with subsistence fishing data (ideally Fiji).

### Step 3.1: Extract subsistence fishing data

**What to do:** Pull subsistence catch data disaggregated by household group.

**How to do it:**
1. From Fiji HIES: fish consumption reported as "own production" or "gifted" (not purchased).
2. From SPC PROCFish: community-level catch and effort data for subsistence fishing.
3. Record gleaning data separately (shellfish, seaweed) if available.

**Expected output:** Subsistence fish flow (kg/yr) by income group and location.

### Step 3.2: Test the subsistence boundary resolution

**What to do:** Apply the resolution from File 07 (product in E9, activity in E10) and check if it works.

**How to do it:**
1. Record the physical fish flow in the ecosystem services supply-use table (E9).
2. Record the fishing activity (hours, participants) in the social flows table (E10/FG2).
3. Check: does the total fish in the supply-use table = commercial + subsistence? No double counting?
4. Check: does the total hours in the social flows table include subsistence fishing hours without also counting the fish kg?

**Expected output:** A worked example showing both tables side by side with a note on whether the resolution holds.

### Step 3.3: Cultural services (if data available)

**What to do:** Attempt to populate cultural service indicators for Fiji using qoliqoli or community survey data.

**How to do it:**
1. Search for published data on traditional fishing practices, ceremonies, or customary governance in Fiji.
2. If community-level data exists, populate Table 4c (ecosystem-linked social activities) for one or two activities.
3. If data is not available, document what would be needed and flag as a gap.

**Expected output:** Either a partially populated Table 4c or a documented data gap.

---

## Phase 4: Spatial Analysis (BSU and Coastal Protection)

**Goal:** Test whether household and ecosystem data can be joined at a meaningful spatial unit.

### Step 4.1: Identify spatial units

**What to do:** Map the available spatial units for each data source.

**How to do it:**
1. For Australia: ABS Census SA2 areas, GBRMPA reef monitoring regions, AIMS LTMP sites.
2. For Fiji: Census tikina/district, qoliqoli boundaries, reef monitoring sites.
3. Determine the coarsest common unit where both household and ecosystem data are available.

**Expected output:** A note documenting the spatial resolution for each data source and the recommended common unit.

### Step 4.2: Coastal protection overlay

**What to do:** Overlay reef/mangrove extent data with population/household data.

**How to do it:**
1. Download Allen Coral Atlas or Global Mangrove Watch reef/mangrove extent data for the study area.
2. Download census population data at the finest available spatial unit.
3. Identify households/buildings within the zone of coastal protection (e.g., within 500m of reef or mangrove).
4. Disaggregate by income group if census data supports it.

**Expected output:** An estimate of how many households, by income group, receive coastal protection from reefs and mangroves.

**Skill to use:** `/stat-reasoning` if you need to assess uncertainty in the spatial overlay.

### Step 4.3: Double counting check

**What to do:** For one accounting area, populate all five services and check for double counting.

**How to do it:**
1. With all five services populated, check:
   - Does any physical flow appear in more than one service row?
   - Does any household benefit appear in more than one service column?
   - Does total service use by households exceed total service supply from ecosystems?
2. Document any instances of double counting and how they were resolved.

**Expected output:** A consistency report for the multi-service accounting area.

**Skill to use:** Run the `consistency-auditor` agent across all tables.

---

## Phase 5: Write-Up and Quality Assurance

**Goal:** Produce methodology documentation and run QA checks.

### Step 5.1: Draft methodology document

**What to do:** Write a methodology document for the social accounts pilot, following the GOAP template.

**How to do it:**
1. Use the `research-strategist` agent to scope the document.
2. Use the `section-drafter` agent (or the `/writer` skill) for each section.
3. Convert to GOAP-formatted Word using `python md_to_docx.py`.

**Expected output:** A methodology document in markdown and .docx format.

### Step 5.2: Run QA checks

**What to do:** Validate the pilot outputs for consistency, accuracy, and completeness.

**How to do it:**
1. Run `/qaqc` on each populated table.
2. Run the `consistency-auditor` across all files in the pilot folder.
3. Run the `methodology-reviewer` on the methodology document.
4. Run `/bias-check` on the worked examples to catch cherry-picking or confirmation bias.

**Expected output:** QA report with issues flagged and resolved.

### Step 5.3: Create a policy brief or presentation

**What to do:** Summarize key findings for a non-technical audience.

**How to do it:**
1. Use `/comms-tone` to adapt the tone for a policy audience.
2. Use the `/goap-visual-slides` skill if creating an HTML presentation.
3. Use `/doc-format-qa` to check GOAP formatting compliance.

**Expected output:** A policy brief or presentation summarizing what the pilot demonstrated.

---

## Tracking progress

Use this checklist to track which steps are complete:

- [ ] 1.1 Verify Australian data sources
- [ ] 1.2 Verify Fiji data sources
- [ ] 1.3 Organize data folders
- [ ] 1.4 Document data gaps
- [ ] 2.1 Choose starting country
- [ ] 2.2 Extract fish provisioning data
- [ ] 2.3 Populate distributional supply-use table
- [ ] 2.4 Trace through to social conditions
- [ ] 3.1 Extract subsistence fishing data
- [ ] 3.2 Test subsistence boundary resolution
- [ ] 3.3 Cultural services (if data available)
- [ ] 4.1 Identify spatial units
- [ ] 4.2 Coastal protection overlay
- [ ] 4.3 Double counting check
- [ ] 5.1 Draft methodology document
- [ ] 5.2 Run QA checks
- [ ] 5.3 Create policy brief or presentation
