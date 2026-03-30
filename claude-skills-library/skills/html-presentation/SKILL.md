---
name: html-presentation
description: Create beautiful, visually diverse HTML presentations using the GOAP design system. Self-contained HTML slides that can be presented in a browser or converted to PDF. Each slide uses a different visual pattern for maximum engagement.
user-invocable: true
---

# HTML Presentation Creator

Create a presentation about: **$ARGUMENTS**

## Overview

This skill creates **production-grade HTML slide presentations** that:
- Look beautiful and professional (GOAP design system)
- Use a different visual pattern for each slide (no two slides look the same)
- Work in any browser (no software installation needed)
- Convert cleanly to PDF for printing or sharing
- Are self-contained (one HTML file, no external dependencies)

---

## The Workflow

```
1. Content outline     →  What do you want to say? (bullet points per slide)
2. Claude creates HTML →  One .html file with all slides styled
3. Present or convert  →  Open in browser OR convert to PDF
```

### Step 1: Give Claude your content

Tell Claude:
- The topic and audience
- The number of slides (aim for 10-15)
- For each slide: the title and 3-5 key points
- Any specific visual preferences ("I want a diagram here", "show this as a comparison")

### Step 2: Claude creates the HTML

Claude generates a single self-contained .html file with:
- Inline CSS (no external stylesheets)
- 16:9 aspect ratio (1400px max-width)
- GOAP color palette and typography
- A different visual pattern per slide
- Print-friendly CSS for PDF conversion

### Step 3: Present or convert

**Option A: Present directly in browser (recommended)**
1. Open the .html file in Chrome
2. Press **Ctrl + Cmd + F** (Mac) or **F11** (Windows) for fullscreen
3. Scroll down to advance between slides
4. Press **Esc** to exit fullscreen

**Option B: Convert to PDF and present as slideshow**
1. Open the .html file in Chrome
2. Press **Cmd + P** (Mac) or **Ctrl + P** (Windows) to print
3. Change destination to "Save as PDF"
4. Set layout to **Landscape**
5. Save
6. Open the PDF in Preview (Mac) → **View → Slideshow** → use arrow keys

**Option C: Convert to PDF using command line (automated)**
```bash
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" \
    --headless --disable-gpu --no-sandbox \
    --print-to-pdf="output.pdf" \
    --no-pdf-header-footer \
    "file:///path/to/slides.html"
```

---

## How to Request a Presentation

### Minimal request:
```
Create a presentation about ocean accounts for a policy audience. 10 slides.
```

### Good request:
```
Create an HTML presentation about ocean accounts for a policy audience.
12 slides covering:
1. Title slide
2. Why ocean accounts matter
3. The three domains (environment, economy, society)
4. What extent accounts measure (with example)
5. What condition accounts measure (with CI scale visual)
6. Ecosystem services (supply and use)
7. Ocean economy (OESA)
8. How accounts connect to SDG 14
9. Country examples
10. How to get started
11. Resources and next steps
12. Thank you / contact

Use the GOAP visual slides design system. Make each slide visually distinct.
```

### Great request (best results):
```
Create an HTML presentation for the Ocean Accounting Clinic.
Audience: early-career professionals from Global South countries.
13 slides.

Slide 1: Title -- "From Ocean Accounts to Policy Action" (use bold teal gradient)
Slide 2: What you leave with -- 2 icon cards (Message Box + Policy Brief)
Slide 3: Science-policy gap -- side-by-side comparison (scientists vs policymakers)
Slide 4: Policy landscape -- 6 data cards with icons (actors, networks, institutions...)
Slide 5: Know your audience -- 4 audience cards with questions
...

Use GOAP design system. Each slide should use a different visual pattern.
Include @media print CSS for PDF conversion.
```

---

## Visual Patterns Available

Each slide should use a different pattern. Here are the 10 GOAP patterns:

| # | Pattern | Best for | Example |
|---|---------|----------|---------|
| 1 | **Side-by-side** | Comparisons, before/after, pros/cons | Science vs policy thinking |
| 2 | **Numbered process** | Steps, workflows, sequences | 7-step compilation process |
| 3 | **Multi-column** | Categories, regions, groupings | 3 account domains |
| 4 | **Highlight box** | Key messages, quotes, call-to-action | "Compile once, report many" |
| 5 | **Timeline** | Milestones, roadmaps, schedules | Event agenda |
| 6 | **Data cards** | Statistics, metrics, key numbers | 6 policy elements |
| 7 | **Nested hierarchy** | Complex concepts with sub-points | Account type details |
| 8 | **Icon cards** | Benefits, features, deliverables | Workshop outputs |
| 9 | **Radial/hub** | Central concept with connections | BSU framework |
| 10 | **Big number** | Impactful statistics | "2.74% of GDP" |

### Pattern selection guide:

```
Is it a COMPARISON?           → Pattern 1 (side-by-side)
Is it SEQUENTIAL (steps)?     → Pattern 2 (numbered process)
Do you have CATEGORIES?       → Pattern 3 (multi-column)
Is it a KEY MESSAGE?          → Pattern 4 (highlight box)
Do you have KEY NUMBERS?      → Pattern 6 (data cards) or Pattern 10 (big number)
Is it VISUAL IMPACT needed?   → Pattern 8 (icon cards)
Is it a CENTRAL CONCEPT?      → Pattern 9 (radial)
```

For full pattern details and code templates, see the **goap-visual-slides** skill.

---

## Technical Specifications

### HTML Structure
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <style>
    /* All CSS inline -- no external files */
    .slide {
      max-width: 1400px;
      aspect-ratio: 16/9;
      /* ... GOAP styles */
    }
    @media print {
      @page { size: A4 landscape; margin: 10mm; }
      .slide { page-break-after: always; }
    }
  </style>
</head>
<body>
  <div class="slide"><!-- Slide 1 --></div>
  <div class="slide"><!-- Slide 2 --></div>
  <!-- ... -->
</body>
</html>
```

### GOAP Color Palette
| Role | Hex | Use |
|------|-----|-----|
| Teal | `#0A5455` | Titles, primary accents |
| Green | `#3B9C7B` | Highlights, success, table headers |
| Blue-gray | `#66A3B5` | Secondary accents |
| Tan | `#B59F81` | Warm accents, challenges |
| Body text | `#545353` | Main text |
| White | `#FFFFFF` | Backgrounds |
| Dark green | `#19383B` | Bold backgrounds |

### Typography
| Element | Size | Weight |
|---------|------|--------|
| Slide title | 36-42px | Bold |
| Section header | 20-24px | Bold |
| Body text | 16-18px | Regular |
| Label/caption | 13-14px | Regular |
| MINIMUM | 12px | -- |
| NEVER | Below 12px | -- |

### Print CSS (always include)
```css
@media print {
  @page { size: A4 landscape; margin: 10mm; }
  body { background: white !important; }
  .slide {
    width: 100% !important;
    max-width: 100% !important;
    aspect-ratio: auto !important;
    box-shadow: none !important;
    page-break-after: always;
    page-break-inside: avoid;
  }
  * { -webkit-print-color-adjust: exact !important; }
}
```

---

## Quality Checklist

Before presenting, verify:

- [ ] All text readable from 3 metres (no text below 14px for body)
- [ ] Each slide uses a different visual pattern (no two identical layouts)
- [ ] GOAP colors applied consistently (teal titles, green accents)
- [ ] No slide has more than ~50 words of body text (it is a slide, not a document)
- [ ] Tables have max 5-6 rows (convert larger tables to visual cards)
- [ ] Key messages are visually prominent (highlight boxes, big numbers)
- [ ] Slide count is 10-15 (enough to cover content, not so many it drags)
- [ ] @media print CSS is included for PDF conversion
- [ ] File is self-contained (no external CSS, images, or fonts)
- [ ] Works in Chrome fullscreen (Ctrl+Cmd+F on Mac)

---

## Related Skills

| Skill | When to use |
|-------|------------|
| **goap-visual-slides** | Detailed reference for the 10 visual patterns with code templates |
| **pptx-format-qa** | If you need PowerPoint format instead of HTML |
| **doc-format-qa** | For Word document handouts that accompany the presentation |
| **comms-tone** | To adapt writing style for different audiences (policy, academic, lay) |

---

## Examples Created with This Approach

These presentations in the ocean-accounts-expert repo were created using this skill:

| File | Slides | Topic |
|------|--------|-------|
| `policy-brief-slides.html` | 13 | Policy brief writing workshop |
| `slide_overview_pipeline.html` | 1 | Ocean accounts framework overview |
| `slide_services_pipeline.html` | 2 | Ecosystem services pipeline + use tables |
| `visual_diagnostic_flowchart.html` | 2 | Clinic triage + full OA framework |
| `visual_policy_connections.html` | 2 | Accounts to policy connections |
| `visual_output_poster.html` | 2 | All account outputs poster |
| `visual_normalization_cheatsheet.html` | 1 | Condition index formula reference |
| `visual_tier_comparison.html` | 1 | Tier 1/2/3 data comparison |
| `visual_data_sources_card.html` | 1 | Global open datasets reference |
| `slide_example_account_tables.html` | 3 | Filled SEEA-EA table examples |
| `slide_oesa_pipeline.html` | 1 | OESA 7-step compilation |
| `slide_oesa_vs_seea.html` | 1 | OESA and SEEA-EA comparison |

---

## Version History

- **v1.0** (March 30, 2026) -- Initial skill covering complete workflow from content to presentation, with pattern selection guide, technical specs, presenting instructions (Mac/Chrome), PDF conversion, and quality checklist.
