# Ocean Accounting Clinic -- Facilitator Toolkit

## Clinic Schedule

| Day | Time | Focus |
|-----|------|-------|
| Day 2 | 11:15-12:00 | Pt.1: Hands-on account creation (Asia & Pacific) |
| Day 2 | 13:00-14:00 | Pt.1: Hands-on account creation (Africa & others) |
| Day 3 | 09:10-10:30 | Pt.2: Policy implications and brief development |
| Day 3 | 10:45-12:00 | Pt.2: Policy brief development (continued) |

## How to use this toolkit

### Step 1: Triage the participant

Ask three questions:

1. **What account type do you want to build?**
   - Extent (mapping ecosystem areas and changes)
   - Condition (measuring ecosystem health)
   - Ecosystem services (quantifying benefits to people)
   - "I don't know yet" --> use the diagnostic tool

2. **What data do you have?**
   - No data at all
   - Global/open datasets only (satellite, Allen Coral Atlas, Global Mangrove Watch)
   - National/regional data (government statistics, monitoring programs)
   - Site-level field data (surveys, transects, catch records)

3. **What is your policy question?**
   - This determines which account type is most useful and how to frame outputs

### Step 2: Direct them to the right pathway

| They want... | They have... | Go to... |
|-------------|-------------|----------|
| Extent account | No data | `extent/` Pathway A (global datasets) |
| Extent account | Satellite imagery or maps | `extent/` Pathway B (classification) |
| Condition account | No field data | `condition/` Pathway A (remote sensing proxies) |
| Condition account | Field survey data | `condition/` Pathway B (indicator calculation) |
| Services account | No data | `services/` Pathway A (value transfer) |
| Services account | Catch data, visitor stats, etc. | `services/` Pathway B (primary valuation) |
| Don't know | Any | `resources/diagnostic-tool.md` to scope priorities |

### Step 3: Walk through the guide with them

Each account type folder contains:
- **Slides** -- walkthrough presentation to go through with the fellow
- **Step-by-step guide** -- detailed instructions for each pathway
- **Exercise** -- hands-on calculation they can do during the clinic
- **Template** -- spreadsheet structure they fill with their data

## Folder structure

```
day-2/clinic/
├── README.md                       <-- you are here
├── clinic_facilitator_guide.docx
│
├── extent/                         # Ecosystem extent accounts
│   ├── extent-slides.md
│   ├── extent-guide.md
│   ├── extent-exercise.md
│   └── extent_account_template.xlsx
│
├── condition/                      # Ecosystem condition accounts
│   ├── condition-slides.md
│   ├── condition-guide.md
│   ├── condition-exercise.md
│   ├── condition_account_template.xlsx
│   └── condition_exercise.xlsx
│
├── services/                       # Ecosystem services (Part A physical + Part B monetary)
│   ├── services-slides.md
│   ├── services-guide.md
│   ├── services-exercise.md
│   ├── services_account_template.xlsx
│   └── services_exercise.xlsx
│
├── diagrams/                       # Pipeline diagrams (PNG)
│   ├── diagram_overview.png
│   ├── diagram_extent_pipeline.png
│   ├── diagram_condition_pipeline.png
│   ├── diagram_services_pipeline.png
│   └── diagram_triage.png
│
├── slides/                         # GOAP HTML presentation slides
│   ├── slide_overview_pipeline.html
│   ├── slide_extent_pipeline.html
│   ├── slide_condition_pipeline.html
│   ├── slide_services_pipeline.html
│   └── slide_examples_logic_chains.html
│
├── resources/                      # Reference materials
│   └── diagnostic-tool.md
│
└── [future account types]/         # Add as needed:
    # economic/                     # Ocean economy satellite accounts
    # social/                       # Social ocean accounts
    # governance/                   # Governance accounts
```

## What to print

See `../../printing/` folder for print-ready GOAP Word documents:
- Clinic triage card (1 per facilitator)
- Extent, condition, and services exercise sheets (15 each)
- Station signs for Day 1

Excel templates and HTML slides are shared digitally.
