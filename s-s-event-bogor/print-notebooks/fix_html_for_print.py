#!/usr/bin/env python3
"""Add print-friendly CSS to all HTML slides so they print correctly to PDF.

Injects @media print and @page rules that:
- Set landscape orientation
- Scale content to fit within the page
- Remove shadows and backgrounds
- Ensure no content is cut off
"""

from pathlib import Path
import re

PRINT_CSS = """
    /* Print-friendly styles */
    @page {
      size: A4 landscape;
      margin: 10mm;
    }
    @media print {
      body {
        background: white !important;
        display: block !important;
        padding: 0 !important;
        min-height: auto !important;
      }
      .slide-container, .slide {
        width: 100% !important;
        max-width: 100% !important;
        min-height: auto !important;
        height: auto !important;
        aspect-ratio: auto !important;
        box-shadow: none !important;
        border-radius: 0 !important;
        padding: 15px 20px !important;
        margin: 0 !important;
        page-break-inside: avoid;
        overflow: visible !important;
        transform: none !important;
      }
      .slide-container::before, .slide::before {
        display: none !important;
      }
      /* Scale down fonts slightly for print */
      h1, .title { font-size: 28px !important; }
      h2 { font-size: 18px !important; }
      body, p, td, th, li, div { font-size: 11px !important; }
      table { font-size: 10px !important; page-break-inside: avoid; }
      /* Ensure colors print */
      * { -webkit-print-color-adjust: exact !important; print-color-adjust: exact !important; }
      /* Page breaks between slides */
      .slide-container + .slide-container, .slide + .slide, .page-break { page-break-before: always; }
    }
"""


def fix_html_file(filepath):
    """Inject print CSS into an HTML file."""
    text = filepath.read_text(encoding="utf-8")

    # Check if already has print CSS
    if "@page" in text and "landscape" in text:
        return False

    # Inject before closing </style> tag
    if "</style>" in text:
        text = text.replace("</style>", PRINT_CSS + "\n  </style>", 1)
    elif "</head>" in text:
        text = text.replace("</head>", f"<style>{PRINT_CSS}</style>\n</head>", 1)

    filepath.write_text(text, encoding="utf-8")
    return True


def main():
    base = Path("/Users/mariaalarcon/GitHub/ocean-accounts-expert/s-s-event-bogor")

    html_dirs = [
        base / "sessions/day-2/clinic/slides",
        base / "sessions/day-2/clinic/visuals",
        base / "sessions/day-2/clinic/economic",
        base / "sessions/day-2/clinic/examples",
        base / "sessions/day-3/clinic-policy",
    ]

    fixed = 0
    for d in html_dirs:
        if not d.exists():
            continue
        for f in d.glob("*.html"):
            if "resources" in str(f):
                continue
            if fix_html_file(f):
                print(f"  Fixed: {f.relative_to(base)}")
                fixed += 1
            else:
                print(f"  Already OK: {f.relative_to(base)}")

    print(f"\nFixed {fixed} HTML files")


if __name__ == "__main__":
    main()
