# GOAP Visual Slides Skill

**Version:** 1.1  
**Last Updated:** March 25, 2026  
**Language:** English (with Spanish support)  
**Purpose:** Transform text content, data, and complex information into visually appealing, interactive HTML slides using the GOAP (Global Ocean Accounts Partnership) design system.

---

## Overview

This skill transforms static content into **production-grade HTML presentations** optimized for 16:9 landscape format. It combines data visualization, visual hierarchy, consistent GOAP branding, and readability-first principles to create slides that work equally well on projectors, screens, and mobile devices.

**Core Philosophy:** Form follows function. Every visual choice—color, size, spacing, layout—must serve the story being told.

---

## GOAP Design System

### Color Palette

| Role | Color Name | Hex Value | Primary Use |
|------|-----------|-----------|------------|
| Primary Dark | Teal | `#0A5455` | Titles, primary text, main accents |
| Secondary Dark | Dark Green | `#19383B` | Bold backgrounds, strong emphasis |
| Base | White | `#FFFFFF` | Primary background |
| Accent 1 | Sea Green | `#3B9C7B` | Highlights, left borders, success indicators |
| Accent 2 | Blue-Gray | `#66A3B5` | Secondary accents, dividers, supporting info |
| Accent 3 | Tan/Beige | `#B59F81` | Warm accents, challenges, alternatives |
| Accent 4 | Light Blue | `#B5D0D6` | Soft backgrounds, subtle emphasis |
| Accent 5 | Light Green | `#5EB593` | Positive indicators, success, completion |
| Text Secondary | Dark Gray | `#545353` | Body text, secondary information |

**Color Principle:** Colors encode meaning. Assign them thematically:
- 🟢 Sea Green = primary/success/go-forward
- 🔵 Blue-Gray = secondary/supporting/information
- 🟤 Tan = caution/challenge/alternative approach
- 💙 Light Blue = soft/gentle/background

### Typography

| Element | Size | Weight | Color | Notes |
|---------|------|--------|-------|-------|
| Slide Title (h1) | 42px | Bold (500) | #0A5455 | Dominates slide, maximum visibility |
| Section Header (h2) | 17px | Bold (500) | #0A5455 | Clear visual hierarchy |
| Body Text | 14px | Regular (400) | #545353 | Main content, readable from distance |
| Label/Caption | 13px | Regular (400) | #545353 | Supporting information |
| **MINIMUM SIZE** | **12px** | Regular | Any | Absolute floor; accessibility critical |
| **NEVER USE** | **Below 12px** | N/A | N/A | Unreadable on projection, fails WCAG |

**Font Stack:** Arial, sans-serif (consistent, professional, universally available)

**Line Height:**
- Body text: 1.4–1.6 (breathing room)
- Headers: 1.2 (tighter, acceptable)
- Title: 1.1 (stands alone)

### Layout & Spacing

| Property | Standard | Notes |
|----------|----------|-------|
| Aspect Ratio | 16:9 (Landscape) | Always horizontal |
| Max Width | 1400px | Scales to any screen size |
| Padding (Slide) | 2rem sides, 1.5rem top/bottom | Standard container padding |
| Gap Between Sections | 1.5–2rem | Visual separation without cramming |
| Card Padding | 1.2–1.3rem | Internal spacing within boxes |
| Border Radius | 4px (details), 6px (major) | Flat modern aesthetic |
| Border Left (Accent) | 5px solid (color) | Primary visual indicator for cards |

**Golden Rule:** When in doubt, add more whitespace. Cramped design = amateur hour.

---

## Readability Standards (NON-NEGOTIABLE)

### Font Size Minimums

These are **absolute minimums.** Never go below:

```
Title .................... 42px (slide title only)
Section Headers .......... 17px (subsection headers)
Body Text ................ 14px (main content, bullets)
Labels/Captions .......... 13px (supporting, annotations)
ABSOLUTE FLOOR ........... 12px (used sparingly, last resort)
FORBIDDEN ................ Below 12px (accessibility failure)
```

### Contrast & Readability

✅ **Good Contrast (Readable):**
- Dark text (#0A5455, #545353) on light background (#FFFFFF, #fafaf9)
- Light text (#FFFFFF) on dark background (#0A5455, #19383B)
- Bold text (#0A5455) on soft colored background (#E8F3F5, #B5D0D6)

❌ **Bad Contrast (Unreadable):**
- Gray text (#545353) on light gray background
- Dark text on dark background
- Light text on white/very light background

### Words Per Line (Content Density)

| Context | Max Words | Reason |
|---------|-----------|--------|
| Slide Title | 10 words | 42px is large; long titles wrap awkwardly |
| Section Header | 7–8 words | 17px still sizable; avoid overflow |
| Body Bullet | 10–12 words | Scannable; prevents wall-of-text |
| Caption/Label | 5–6 words | Brief, supporting, focused |

**Principle:** Fewer words, bigger font. If using 11px or 12px, you have too much text. Delete, split to another slide, or move to handout.

### Device Readability Test

Before finalizing, ask yourself:

- ✓ Can it be read from 3 meters away? (back of room)
- ✓ Can it be read on a projector screen? (no squinting)
- ✓ Is font size ≥14px for body text?
- ✓ Are icons/visuals ≥24px (inline), ≥48px (standalone)?
- ✓ Is there generous padding (1.3–2rem) around content?
- ✓ Do text and background have high contrast?

If you answer "no" to any, redesign.

---

## Slide Patterns & Templates

### Pattern 1: Side-by-Side Comparison
**Use When:** Contrasting concepts, before/after, problem/solution, pros/cons

**Structure:**
```
LEFT COLUMN              RIGHT COLUMN
────────────────────────────────────────
Title (Concept A)        Title (Concept B)
border-left 5px          border-left 5px
(color 1)                (color 2)
────────────────────────────────────────
Content                  Content
```

**Colors:** Left = #3B9C7B, Right = #66A3B5 (or other accent pairs)

**Code Template:**
```html
<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 2rem;">
  <div style="border-left: 5px solid #3B9C7B; padding: 1.3rem; background: #fafaf9;">
    <div style="font-size: 17px; font-weight: bold; color: #0A5455;">Concept A</div>
    <!-- Content here -->
  </div>
  <div style="border-left: 5px solid #66A3B5; padding: 1.3rem; background: #fafaf9;">
    <div style="font-size: 17px; font-weight: bold; color: #0A5455;">Concept B</div>
    <!-- Content here -->
  </div>
</div>
```

**Examples:**
- Current State vs. Future State
- Challenges vs. Solutions
- Region A vs. Region B
- Traditional Approach vs. New Approach

---

### Pattern 2: Numbered Process / Sequential Steps
**Use When:** Workflows, procedures, implementation roadmaps, timelines with stages

**Structure:**
```
① Step 1 → ② Step 2 → ③ Step 3 → ④ Step 4
Description  Description  Description  Description
```

**Code Template:**
```html
<div style="display: flex; flex-direction: column; gap: 1rem;">
  <div style="display: flex; gap: 0.8rem; align-items: flex-start;">
    <div style="width: 28px; height: 28px; background: #0A5455; color: white; 
                border-radius: 50%; text-align: center; line-height: 28px; 
                font-weight: bold; flex-shrink: 0;">1</div>
    <div>
      <div style="font-weight: bold; color: #0A5455; font-size: 16px;">Step Title</div>
      <div style="font-size: 13px; color: #545353; line-height: 1.4;">Description</div>
    </div>
  </div>
  <!-- Repeat for steps 2, 3, 4... -->
</div>
```

**Examples:**
- Encuesta → Compilación → Presentación → Impacto (GOAP process)
- Data Collection → Validation → Analysis → Publication
- Capacity Building Journey (Stage 1, 2, 3, etc.)

---

### Pattern 3: Multi-Column Categories
**Use When:** Organizing many items by region/type/category; regional breakdowns

**Structure:**
```
COLUMN 1        COLUMN 2        COLUMN 3
────────────────────────────────────────
Category A      Category B      Category C
Item 1          Item 1          Item 1
Item 2          Item 2          Item 2
Item 3          Item 3          Item 3
```

**Code Template:**
```html
<div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 1.5rem;">
  <div style="border-left: 5px solid #3B9C7B; padding: 1.3rem; background: #fafaf9;">
    <div style="font-size: 17px; font-weight: bold; color: #0A5455; 
                text-transform: uppercase; border-bottom: 2px solid rgba(10,84,85,0.2); 
                padding-bottom: 0.6rem;">Category A</div>
    <div style="margin-top: 0.8rem; display: flex; flex-direction: column; gap: 0.5rem;">
      <div style="font-size: 14px; color: #0A5455; font-weight: bold;">Item 1</div>
      <div style="font-size: 13px; color: #545353;">Detail</div>
    </div>
  </div>
  <!-- Repeat for columns 2, 3 -->
</div>
```

**Examples:**
- LAC Countries by Region (Latin America | Caribbean | Regional)
- Ocean Accounts Components (Environmental | Economic | Social)
- Implementation Status (Completed | In Progress | Planned)

---

### Pattern 4: Key Finding / Highlight Box
**Use When:** Critical insights, summaries, call-to-action, main takeaway

**Structure:**
```
┌─────────────────────────────────────┐
│  BOLD STATEMENT / KEY MESSAGE       │
│  (larger, centered, color gradient) │
│                                     │
│  Supporting explanation or context  │
│  (secondary text, clear but quiet)  │
└─────────────────────────────────────┘
```

**Code Template:**
```html
<div style="background: linear-gradient(to right, #E8F3F5, #F9F5F0); 
            border: 2px solid #66A3B5; border-radius: 6px; padding: 1.3rem;">
  <div style="font-size: 16px; font-weight: bold; color: #0A5455; margin-bottom: 0.6rem;">
    KEY INSIGHT
  </div>
  <div style="font-size: 14px; color: #545353; line-height: 1.5;">
    Detailed explanation or insight
  </div>
</div>
```

**Examples:**
- "LAC is not a passive consumer but an active contributor to global standards"
- "Institutional barriers matter more than technical sophistication"
- "One survey, many uses: Report once, use everywhere"

---

### Pattern 5: Timeline / Progress Visualization
**Use When:** Project roadmaps, milestones, schedule, progress tracking, evolution over time

**Structure:**
```
AUG 2023        NOV 2024        APR 2025        OCT 2025        FEB 2026        JUN 2026
   ⭕ ────────── ⭕ ────────── ⭕ ────────── ⭕ ────────── ⭕ ────────── ⭕
Workshop      MOU Signed     Fellows Train    MRV Integ.   WE ARE HERE   Completion
```

**Code Template:**
```html
<div style="display: grid; grid-template-columns: repeat(6, 1fr); gap: 1rem; margin: 2rem 0;">
  <div style="text-align: center;">
    <div style="width: 24px; height: 24px; background: #3B9C7B; 
                border-radius: 50%; margin: 0 auto 0.5rem;"></div>
    <div style="font-size: 12px; font-weight: bold; color: #0A5455;">Aug 2023</div>
    <div style="font-size: 11px; color: #545353;">Workshop</div>
  </div>
  <!-- Repeat for other milestones; highlight current with #B59F81 -->
</div>
```

**Examples:**
- Belize Ocean Accounts Project timeline
- Implementation phases (Aug 2023 → Jun 2026)
- Quarterly milestones with status updates

---

### Pattern 6: Data Cards / Metrics
**Use When:** Presenting statistics, key numbers, before-and-after comparisons, benchmarks

**Structure:**
```
┌─────────────┐  ┌─────────────┐  ┌─────────────┐
│   LABEL     │  │   LABEL     │  │   LABEL     │
│             │  │             │  │             │
│    123      │  │    19        │  │    11       │
│  Initiatives│  │   Countries │  │   Regions   │
└─────────────┘  └─────────────┘  └─────────────┘
```

**Code Template:**
```html
<div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 1rem;">
  <div style="background: #fafaf9; border-left: 5px solid #3B9C7B; padding: 1.2rem; border-radius: 4px;">
    <div style="font-size: 12px; color: #545353; text-transform: uppercase; margin-bottom: 0.5rem;">Label</div>
    <div style="font-size: 28px; font-weight: bold; color: #0A5455;">123</div>
    <div style="font-size: 13px; color: #545353; margin-top: 0.5rem;">Context/unit</div>
  </div>
  <!-- Repeat for other metrics -->
</div>
```

**Examples:**
- "19 initiatives across 11 countries"
- "31–133 million people employed"
- "3,000+ million people fed"

---

### Pattern 7: Nested Hierarchy (Complex Information)
**Use When:** Breakdown of complex concepts with main points and supporting details

**Structure:**
```
MAIN CONCEPT (Large, Bold)
  → Sub-concept 1 (Medium)
     • Detail (Small)
     • Detail (Small)
  → Sub-concept 2 (Medium)
     • Detail (Small)
```

**Code Template:**
```html
<div style="border-left: 5px solid #3B9C7B; padding: 1.3rem; background: #fafaf9;">
  <div style="display: flex; flex-direction: column; gap: 0.8rem;">
    <div>
      <div style="font-size: 16px; font-weight: bold; color: #0A5455;">Main Point 1</div>
      <div style="margin-left: 0.6rem; margin-top: 0.4rem; display: flex; flex-direction: column; gap: 0.4rem;">
        <div style="font-size: 14px; color: #545353;">• Sub-point</div>
        <div style="font-size: 14px; color: #545353;">• Sub-point</div>
      </div>
    </div>
  </div>
</div>
```

**Examples:**
- Challenges breakdown (Data Gaps → Spatial coverage, Temporal continuity)
- Support mechanisms with details (Communities of Practice → Lessons exchange, Training)

---

### Pattern 8: Icon + Statement Cards (ICON-HEAVY)
**Use When:** Benefits, features, key messages; **minimal text, maximum impact**

**Structure:**
```
[ICON]      [ICON]      [ICON]      [ICON]
  48px        48px        48px        48px
   
Bold        Bold        Bold        Bold
Statement   Statement   Statement   Statement
(18px)      (18px)      (18px)      (18px)

Small descriptor or context (optional, 12px max)
```

**Code Template:**
```html
<div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 1.5rem;">
  <div style="text-align: center; padding: 1.5rem;">
    <div style="font-size: 48px; margin-bottom: 1rem;">✓</div>
    <div style="font-size: 18px; font-weight: bold; color: #0A5455;">Data Sovereignty</div>
    <div style="font-size: 12px; color: #545353; margin-top: 0.5rem;">Control your data</div>
  </div>
  <!-- Repeat for other benefits -->
</div>
```

**Examples:**
- Four key benefits (✓ Sovereignty, 💰 Investment, 🌍 Impact, 📈 Growth)
- Five success factors with icons
- Three pillars with visual emphasis

**Readability:** Icon (48px) + Title (18px bold) + Optional descriptor (12px) = Clean, scannable, visually appealing

---

### Pattern 9: Circular / Radial Organization
**Use When:** Central concept with surrounding components; hub-and-spoke model

**Structure:**
```
            ┌─────────────┐
            │   CONCEPT   │
            │   (CENTER)  │
            └─────────────┘
                   │
    ┌──────────────┼──────────────┐
    │              │              │
 [Item 1]      [Item 2]       [Item 3]
    │              │              │
    └──────────────┼──────────────┘
```

**Code Template:**
```html
<div style="position: relative; width: 400px; height: 400px; margin: 0 auto;">
  <!-- Center Circle -->
  <div style="position: absolute; top: 50%; left: 50%; width: 100px; height: 100px;
              transform: translate(-50%, -50%); background: #0A5455; 
              border-radius: 50%; display: flex; align-items: center; 
              justify-content: center; color: white; font-weight: bold; font-size: 20px;">
    CORE
  </div>
  <!-- Surrounding items positioned in circle -->
  <div style="position: absolute; top: 20px; left: 50%; transform: translateX(-50%);
              text-align: center; width: 100px;">
    <div style="font-size: 24px; margin-bottom: 0.5rem;">🌿</div>
    <div style="font-size: 13px; font-weight: bold; color: #0A5455;">Environmental</div>
  </div>
  <!-- Repeat for other positions (top-right, bottom-right, bottom, bottom-left, left) -->
</div>
```

**Examples:**
- Ocean Accounts at center with 5–6 surrounding dimensions
- GOAP as hub with supporting institutions
- Core concept with stakeholder groups

---

### Pattern 10: Big Number + Context (VISUAL IMPACT)
**Use When:** Highlighting statistics, shocking facts, key metrics that deserve emphasis

**Structure:**
```
    [HUGE NUMBER - 72px Bold]
           
        Descriptor (24px)
        
    Context or supporting detail (16px)
```

**Code Template:**
```html
<div style="background: linear-gradient(to right, #E8F3F5, #F9F5F0); 
            border: 2px solid #66A3B5; border-radius: 6px; padding: 2rem;
            text-align: center;">
  <div style="font-size: 72px; font-weight: bold; color: #0A5455; line-height: 1;">
    19
  </div>
  <div style="font-size: 24px; color: #0A5455; margin: 0.5rem 0; font-weight: bold;">
    Initiatives
  </div>
  <div style="font-size: 16px; color: #545353;">
    Across 11 countries in LAC
  </div>
</div>
```

**Examples:**
- "19 Initiatives" (across 11 countries)
- "3,000+ Million" (people fed by marine protein)
- "65 Global Initiatives" (in ocean accounting)

**Impact:** Large number draws eye, supporting text provides context, gradient background provides emphasis without being garish.

---

## Presentation Balance: When to Use What

A **strong presentation balances**:
- 50% Text-heavy content (Patterns 1–7) for detail, explanation, methodology
- 30% Icon-heavy content (Patterns 8–10) for impact, benefits, summary
- 20% Visual/data content (Patterns 5–6) for progress, milestones, statistics

### Example Presentation Structure (15-slide deck)

**Opening (2 slides)**
1. Title slide (minimal text, strong visual)
2. Context/Problem (Pattern 1: Side-by-side, problem statement)

**Problem & Opportunity (3 slides)**
3. Current challenges (Pattern 7: Nested hierarchy)
4. Why it matters (Pattern 10: Big number + context)
5. Global context (Pattern 3: Multi-column regions)

**Solution & Components (4 slides)**
6. What is ocean accounting? (Pattern 4: Highlight box + explanation)
7. Key pillars/dimensions (Pattern 9: Radial + 3 concepts)
8. Implementation process (Pattern 2: 4-step numbered flow)
9. Benefits showcase (Pattern 8: 4 icon cards, minimal text)

**Global Progress & LAC Focus (3 slides)**
10. Global stocktake (Pattern 5: Timeline or Pattern 6: Data cards)
11. LAC implementation (Pattern 3: Multi-column by country)
12. Success factors (Pattern 8: 5 benefits with icons)

**Call to Action & Next Steps (2 slides)**
13. How to participate (Pattern 2: Process steps)
14. Survey/engagement (Pattern 4: Key message + CTA)

15. Thank you / Contact (minimal, strong visual)

---

## Decision Tree: Which Pattern to Use?

```
START: I have content to visualize

├─ Is it a COMPARISON? → Use Pattern 1 (Side-by-Side)
│
├─ Is it SEQUENTIAL? (steps, process, timeline)
│  ├─ With milestones? → Use Pattern 5 (Timeline)
│  └─ With steps? → Use Pattern 2 (Numbered Process)
│
├─ Do I have MANY ITEMS in CATEGORIES?
│  ├─ By region/type? → Use Pattern 3 (Multi-Column)
│  └─ Organized hierarchically? → Use Pattern 7 (Nested Hierarchy)
│
├─ Do I have KEY STATISTICS or METRICS?
│  ├─ Single big number? → Use Pattern 10 (Big Number + Context)
│  └─ Multiple comparable numbers? → Use Pattern 6 (Data Cards)
│
├─ Is this a CRITICAL MESSAGE?
│  └─ → Use Pattern 4 (Highlight Box)
│
├─ Do I want VISUAL IMPACT with MINIMAL TEXT?
│  ├─ Benefits/features with icons? → Use Pattern 8 (Icon Cards)
│  ├─ Central concept + surrounding ideas? → Use Pattern 9 (Radial)
│  └─ → Keep text ≤13px, icons ≥48px
│
└─ DONE: Apply GOAP colors, enforce ≥14px body text, add whitespace
```

---

## How to Request a Slide from Claude

**Effective Request Format:**

```
I need a slide showing [main concept] with:
- [Key information 1]
- [Key information 2]
- [Optional: specific style preference]
- **Enforce:** All text ≥14px, readable from distance

Example: "Create a slide showing the 4 benefits of ocean accounts with icons, 
minimal text (keep statements to 2–3 words), and large readable fonts (14px+). 
Make it visually appealing, not text-heavy."
```

**Request Examples:**

**For Text-Heavy Content:**
```
Create a slide explaining the 4 main challenges in SEEA implementation:
1. Data gaps (with details)
2. Technical capacity (with details)
3. Governance fragmentation (with details)
4. Financial sustainability (with details)
Use Pattern 3 or 7, enforce 14px+ minimum, use #3B9C7B for emphasis.
```

**For Icon-Heavy Content:**
```
Create a visually appealing slide showing 4 key benefits with:
- One icon per benefit (✓, 💰, 🌍, 📈)
- Bold statement (18px) per benefit
- Short descriptor (12px) optional
- Minimal text, maximum impact
Use Pattern 8, center layout, GOAP colors.
```

**For Data Visualization:**
```
Create a slide showing LAC ocean accounts progress:
- 19 initiatives across 11 countries
- Breakdown by region (Latin America, Caribbean, Regional)
- Types of institutions involved
Use Pattern 6 (data cards) or Pattern 3 (multi-column), 
enforce readability, use gradient background for emphasis.
```

---

## Creating Visual Appeal Without Text

### Techniques for Impact:

**1. Color & Shape:**
```html
<!-- Use color + shape to indicate importance, not just text -->
<div style="display: flex; gap: 1rem; align-items: center;">
  <div style="width: 5px; height: 50px; background: #0A5455;"></div>
  <div style="font-size: 18px; font-weight: bold; color: #0A5455;">Critical Point</div>
</div>
```

**2. Progress/Completion Bars:**
```html
<div style="background: #E8F3F5; height: 10px; border-radius: 4px; overflow: hidden;">
  <div style="background: #3B9C7B; height: 100%; width: 75%;"></div>
</div>
<div style="font-size: 14px; color: #545353; margin-top: 0.5rem; font-weight: bold;">75% Complete</div>
```

**3. Icon Hierarchy:**
```
LARGE ICON (48–72px)
├─ Bold Title (18–20px)
└─ Optional: Short context (12–13px)
```

**4. Whitespace as Design:**
- Generous padding (1.3–2rem) = professional, breathable
- Cramped content = amateur, hard to read
- Each visual element should have room to "breathe"

**5. Color Contrast for Emphasis:**
- Teal (#0A5455) on light (#FFFFFF) = strong, readable
- Tan (#B59F81) on light tan (#F9F5F0) = subtle, soft
- Use contrast strategically to guide the eye

---

## Readability Checklist

**Before publishing ANY slide:**

- [ ] **Title is 42px?** (largest element)
- [ ] **Section headers are 17px+?** (clear visual hierarchy)
- [ ] **Body text is 14px+?** (readable from distance)
- [ ] **Labels are 13px+?** (still legible)
- [ ] **ZERO text below 12px?** (never—accessibility fail)
- [ ] **Line height is 1.4–1.6 for body?** (breathing room)
- [ ] **Text color contrast is 4.5:1 or higher?** (WCAG AA standard)
- [ ] **Max 10–12 words per bullet line?** (scannable, not dense)
- [ ] **Slide readable from 3 meters away?** (test mentally or physically)
- [ ] **Icons are ≥24px (inline) or ≥48px (standalone)?** (visible)
- [ ] **Padding is 1.3–2rem around content?** (not cramped)
- [ ] **Only 2–3 accent colors used?** (not chaotic)
- [ ] **Whitespace supports the design?** (breathing room, not wasted space)

---

## HTML Base Template

Start with this foundation for every slide:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Slide Title</title>
  <style>
    * {
      margin: 0;
      padding: 0;
      box-sizing: border-box;
    }
    body {
      font-family: Arial, sans-serif;
      background: #f5f5f5;
      padding: 1.5rem;
      color: #333;
    }
    .slide-container {
      width: 100%;
      max-width: 1400px;
      margin: 0 auto;
      background: #FFFFFF;
      padding: 2rem 2.5rem;
      border-radius: 8px;
      min-height: 620px;
      display: flex;
      flex-direction: column;
      box-shadow: 0 2px 12px rgba(0,0,0,0.08);
    }
    .title-section {
      border-bottom: 4px solid #0A5455;
      padding-bottom: 0.8rem;
      margin-bottom: 1.5rem;
    }
    .title-section h1 {
      font-size: 42px;
      font-weight: bold;
      color: #0A5455;
      line-height: 1.1;
      margin: 0;
    }
    /* Add specific styles for your content below */
  </style>
</head>
<body>
  <div class="slide-container">
    <div class="title-section">
      <h1>Your Slide Title Here</h1>
    </div>
    <!-- Your content here -->
  </div>
</body>
</html>
```

---

## Key Principles (Remember These)

1. **Form Follows Function:** Every design choice should serve the story.
2. **Readability First:** 14px minimum for body text, always.
3. **Color Encodes Meaning:** Don't use colors randomly; assign them thematically.
4. **Less Text, More Visual:** When in doubt, show more and say less.
5. **Balance:** Mix detailed slides with visual impact slides.
6. **Whitespace is Design:** Cramped = amateur; generous spacing = professional.
7. **Test on Projection:** A slide that looks good on your monitor might be unreadable on a wall.
8. **Icon-Heavy ≠ No-Text:** Labels and context are still important; just keep them brief.
9. **Consistency Matters:** Stick to GOAP colors, typography, spacing throughout.
10. **Accessibility Counts:** High contrast, large fonts, simple language benefits everyone.

---

## Version History

- **v1.0** (March 25, 2026) — Initial GOAP Visual Slides skill with 7 core patterns, complete color system, typography guidelines, and transformation workflow
- **v1.1** (March 25, 2026) — Added Patterns 8–10 (icon-heavy), comprehensive readability guidelines, font size minimums, visual appeal techniques, presentation balance guidance, and request format examples

---

## Contact & Feedback

Questions about a pattern? Unsure which to use? Claude can help you choose the right approach based on your content.

**When requesting a slide:**
- Describe your main message (one sentence)
- Share the key information to visualize
- Mention any style preferences
- Request enforcement of readability standards (≥14px)

---

*Last Updated: March 25, 2026*  
*Designed for GOAP presentations in English and Spanish*  
*Optimized for 16:9 landscape format*
