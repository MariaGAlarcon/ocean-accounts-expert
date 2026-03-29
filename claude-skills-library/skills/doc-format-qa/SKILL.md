---
name: doc-format-qa
description: Format quality check and fix for Word documents (.docx). Fixes table column widths, page breaks, markdown artifacts, font consistency. Applies GOAP styling conventions. Run on a file or folder of Word docs.
user-invocable: true
---

# Document Format QA

Run formatting quality checks on Word documents: **$ARGUMENTS**

## What This Skill Does

Checks and fixes common formatting issues in .docx files:

1. **Markdown artifacts**: Removes literal `**` bold markers that leaked from markdown-to-docx conversion. Replaces with proper bold formatting.

2. **Table column widths**: Analyzes content length per column and sets proportional widths. Short columns (single letter, numbers) get narrow widths. Long-text columns get proportionally more space. Prevents the "all columns equal width" problem.

3. **Table page breaks**: Prevents tables from splitting awkwardly across pages. Sets `cantSplit` on rows and `keepWithNext` on header + first data rows so the table stays together.

4. **Orphaned titles**: Ensures headings/titles that precede a table stay on the same page as the table (not stranded at the bottom of the previous page).

5. **Font consistency**: Normalizes all body text to Arial 10pt, headings to GOAP sizes (H1=16pt, H2=14pt, H3=12pt).

## How to Use

### On a single file:
```
/doc-format-qa path/to/document.docx
```

### On a folder of Word docs:
```
/doc-format-qa path/to/folder/
```

### On all print notebooks:
```
/doc-format-qa s-s-event-bogor/print-notebooks/
```

## Process

1. Load each .docx file with python-docx
2. Run all 5 checks
3. Fix issues automatically
4. Save the file
5. Report what was found and fixed

The script is idempotent -- safe to run multiple times. A second run on already-fixed files will report "0 files modified."

## Tool

The Python script `format_qa.py` in this folder implements all checks. It requires `python-docx` (`pip install python-docx`).

Usage:
```bash
python format_qa.py path/to/file_or_folder
```

## GOAP Style Reference

When fixing fonts and styles, the skill applies these GOAP conventions:

| Element | Font | Size | Color |
|---------|------|------|-------|
| Body text | Arial | 10pt | #30302F |
| Heading 1 | Arial | 16pt | #0A5455 |
| Heading 2 | Arial | 14pt | #3B9C7B |
| Heading 3 | Arial | 12pt | #0A5455 |
| Table header | Arial | 10pt bold | #FFFFFF on #3B9C7B |
| Table row header | Arial | 10pt bold | #FFFFFF on #0A5455 |
| Table data | Arial | 10pt | #30302F |
| Borders | | | #404040 |

## When to Use This Skill

- After converting markdown to Word with `md_to_docx.py`
- Before sending documents to a printer
- After any bulk document generation
- When you notice formatting issues in Word docs (tables too wide, titles orphaned, etc.)
