---
name: pptx-format-qa
description: Format quality check and fix for PowerPoint presentations (.pptx). Fixes font sizes, table readability, font consistency, and applies GOAP presentation styling. Run on a file or folder of .pptx files.
user-invocable: true
---

# PowerPoint Format QA

Run formatting quality checks on PowerPoint presentations: **$ARGUMENTS**

## What This Skill Does

Checks and fixes common formatting issues in .pptx files for presentation readability:

1. **Font size minimums**: Ensures all text is readable from the back of a room.
   - Slide titles: minimum 28pt (target 36pt)
   - Body text: minimum 16pt (target 18pt)
   - Table cells: minimum 12pt (target 14pt)
   - Labels/captions: minimum 11pt
   - NEVER below 10pt for any text

2. **Table readability**: Flags tables that are too dense for slides.
   - Tables with >6 rows or >5 columns are flagged
   - Table text below 12pt is auto-increased
   - Recommendation: convert dense tables to visual cards

3. **Font consistency**: Normalizes all text to Arial.

4. **GOAP color check**: Reports if GOAP brand colors are applied.
   - Teal (#0A5455) for titles
   - Green (#3B9C7B) for accents and table headers
   - Body text (#545353 or #30302F)

## How to Use

### Check and fix a single file:
```
/pptx-format-qa path/to/presentation.pptx
```

### Check a folder:
```
/pptx-format-qa path/to/folder/
```

## GOAP Presentation Style Reference

Based on the GOAP Visual Slides skill:

| Element | Size | Color | Notes |
|---------|------|-------|-------|
| Slide title | 36-42pt | #0A5455 (teal) | Bold, dominates slide |
| Section header | 24-28pt | #0A5455 | Clear hierarchy |
| Body text | 16-18pt | #545353 | Readable from distance |
| Table header | 14pt bold | White on #3B9C7B | GOAP green background |
| Table cell | 12-14pt | #30302F | Minimum for readability |
| Caption/label | 11-13pt | #545353 | Supporting only |

### Readability Test
Before presenting, check:
- Can text be read from 3 metres away?
- Are font sizes >= 16pt for body text?
- Do tables have <= 6 rows visible?
- Is there generous whitespace (not cramped)?

## Tool

The Python script `format_pptx.py` implements all checks. Requires `python-pptx` (`pip install python-pptx`).

```bash
python format_pptx.py presentation.pptx
python format_pptx.py presentations/ --recursive
```
