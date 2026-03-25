#!/usr/bin/env python3
"""Generate GOAP-styled pipeline diagrams for the clinic."""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
from pathlib import Path
import numpy as np

# ---- GOAP Colors ----
TEAL = "#0A5455"
GREEN = "#3B9C7B"
MINT = "#D4EEE5"
BODY = "#30302F"
GRAY = "#717171"
WHITE = "#FFFFFF"
YELLOW = "#FFF2CC"
BLUE = "#0077B6"
ORANGE = "#E76F51"
PURPLE = "#7B2D8E"
LIGHT_BLUE = "#B5D0D6"


def rounded_box(ax, x, y, w, h, text, facecolor, textcolor=WHITE, fontsize=9, bold=True):
    box = FancyBboxPatch((x - w/2, y - h/2), w, h,
                         boxstyle="round,pad=0.1", facecolor=facecolor,
                         edgecolor=BODY, linewidth=1.2)
    ax.add_patch(box)
    weight = "bold" if bold else "normal"
    ax.text(x, y, text, ha="center", va="center", fontsize=fontsize,
            color=textcolor, fontfamily="Arial", fontweight=weight, wrap=True)


def arrow(ax, x1, y1, x2, y2, color=GRAY):
    ax.annotate("", xy=(x2, y2), xytext=(x1, y1),
                arrowprops=dict(arrowstyle="-|>", color=color, lw=1.5))


def arrow_label(ax, x1, y1, x2, y2, label="", color=GRAY):
    arrow(ax, x1, y1, x2, y2, color)
    mx, my = (x1 + x2) / 2, (y1 + y2) / 2
    if label:
        ax.text(mx + 0.15, my, label, fontsize=7, color=GRAY, fontfamily="Arial",
                va="center")


def save_fig(fig, path):
    fig.savefig(str(path), dpi=200, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"  Created: {path}")


# =========================================================================
# 1. OVERVIEW: Ocean Accounts Pipeline
# =========================================================================
def diagram_overview(outdir):
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 6)
    ax.axis("off")
    ax.set_aspect("equal")

    # Title
    ax.text(6, 5.6, "Ocean Accounts Pipeline", fontsize=16, ha="center",
            color=TEAL, fontfamily="Arial", fontweight="bold")

    # Data sources (top)
    sources = [
        (1.5, 4.5, "Satellite\nimagery"),
        (4.0, 4.5, "Field\nsurveys"),
        (6.5, 4.5, "Government\nstatistics"),
        (9.0, 4.5, "Global\ndatasets"),
        (11.0, 4.5, "Community\nknowledge"),
    ]
    for x, y, t in sources:
        rounded_box(ax, x, y, 1.8, 0.7, t, LIGHT_BLUE, textcolor=BODY, fontsize=8, bold=False)

    # Spatial framework
    rounded_box(ax, 6, 3.3, 10.5, 0.6, "Spatial Data Framework: Basic Spatial Units (BSU grid)", GREEN, fontsize=9)

    # Three account types
    rounded_box(ax, 2.5, 2.1, 3.2, 0.8, "EXTENT ACCOUNTS\nEcosystem area (ha)\nOpening / Closing", TEAL, fontsize=8)
    rounded_box(ax, 6.0, 2.1, 3.2, 0.8, "CONDITION ACCOUNTS\nEcosystem health (CI 0-1)\nIndicators / Reference", TEAL, fontsize=8)
    rounded_box(ax, 9.5, 2.1, 3.2, 0.8, "SERVICE ACCOUNTS\nBenefits to people\nPhysical / Monetary", TEAL, fontsize=8)

    # Arrows: data sources to spatial framework
    for x, _, _ in sources:
        arrow(ax, x, 4.1, x if x < 9 else 9, 3.65, GREEN)

    # Spatial framework to accounts
    arrow(ax, 3.5, 2.95, 2.5, 2.55, TEAL)
    arrow(ax, 6.0, 2.95, 6.0, 2.55, TEAL)
    arrow(ax, 8.5, 2.95, 9.5, 2.55, TEAL)

    # Horizontal arrows between accounts
    arrow(ax, 4.2, 2.1, 4.3, 2.1, GREEN)
    arrow(ax, 7.7, 2.1, 7.8, 2.1, GREEN)

    # Labels on horizontal arrows
    ax.text(4.25, 2.45, "extent informs\ncondition", fontsize=6, color=GRAY, fontfamily="Arial", ha="center")
    ax.text(7.75, 2.45, "condition informs\nservices", fontsize=6, color=GRAY, fontfamily="Arial", ha="center")

    # Policy outputs (bottom)
    outputs = [
        (2.0, 0.7, "SDG 14\nreporting"),
        (4.5, 0.7, "NDC / NBSAP\nintegration"),
        (7.0, 0.7, "Marine spatial\nplanning"),
        (9.5, 0.7, "Blue finance\n& investment"),
    ]
    for x, y, t in outputs:
        rounded_box(ax, x, y, 2.0, 0.65, t, ORANGE, fontsize=8)

    # Arrow from accounts to policy
    for ox, oy, _ in outputs:
        arrow(ax, 6.0, 1.65, ox, 1.05, ORANGE)

    ax.text(6, 1.35, "Policy applications", fontsize=9, ha="center", color=ORANGE,
            fontfamily="Arial", fontweight="bold")

    save_fig(fig, outdir / "diagram_overview.png")


# =========================================================================
# 2. EXTENT ACCOUNT PIPELINE
# =========================================================================
def diagram_extent(outdir):
    fig, ax = plt.subplots(figsize=(10, 7))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 7)
    ax.axis("off")

    ax.text(5, 6.7, "Extent Account Pipeline", fontsize=16, ha="center",
            color=TEAL, fontfamily="Arial", fontweight="bold")

    # Pathway A (left)
    ax.text(2.5, 6.15, "Pathway A: No data (Tier 1)", fontsize=10, ha="center",
            color=BLUE, fontfamily="Arial", fontweight="bold")

    steps_a = [
        (2.5, 5.5, "Global datasets\nAllen Coral Atlas\nGlobal Mangrove Watch"),
        (2.5, 4.3, "Define accounting\narea boundary"),
        (2.5, 3.1, "Clip & extract\nextent per\necosystem type"),
        (2.5, 1.9, "Extent account\ntable (ha)"),
    ]
    for x, y, t in steps_a:
        fc = LIGHT_BLUE if y > 4 else GREEN if y > 2 else TEAL
        tc = BODY if y > 4 else WHITE
        rounded_box(ax, x, y, 2.8, 0.75, t, fc, tc, fontsize=8)
    for i in range(len(steps_a) - 1):
        arrow(ax, steps_a[i][0], steps_a[i][1] - 0.4, steps_a[i+1][0], steps_a[i+1][1] + 0.4, GREEN)

    # Pathway B (right)
    ax.text(7.5, 6.15, "Pathway B: Own data (Tier 2)", fontsize=10, ha="center",
            color=PURPLE, fontfamily="Arial", fontweight="bold")

    steps_b = [
        (7.5, 5.5, "Satellite imagery\n(Sentinel-2, Pleiades)\n+ Ground truth"),
        (7.5, 4.3, "Preprocessing\n(atmospheric, glint,\nwater column correction)"),
        (7.5, 3.1, "Classification\n(SAM / Random Forest)\n+ Accuracy assessment"),
        (7.5, 1.9, "Extent account\ntable + Change\nmatrix"),
    ]
    for x, y, t in steps_b:
        fc = LIGHT_BLUE if y > 4 else GREEN if y > 2 else TEAL
        tc = BODY if y > 4 else WHITE
        rounded_box(ax, x, y, 2.8, 0.75, t, fc, tc, fontsize=8)
    for i in range(len(steps_b) - 1):
        arrow(ax, steps_b[i][0], steps_b[i][1] - 0.4, steps_b[i+1][0], steps_b[i+1][1] + 0.4, GREEN)

    # Output
    rounded_box(ax, 5, 0.6, 6, 0.65,
                "SEEA EA Extent Account: Opening / Additions / Reductions / Closing (ha)",
                TEAL, fontsize=9)
    arrow(ax, 2.5, 1.5, 4, 0.95, TEAL)
    arrow(ax, 7.5, 1.5, 6, 0.95, TEAL)

    save_fig(fig, outdir / "diagram_extent_pipeline.png")


# =========================================================================
# 3. CONDITION ACCOUNT PIPELINE
# =========================================================================
def diagram_condition(outdir):
    fig, ax = plt.subplots(figsize=(10, 8))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 8)
    ax.axis("off")

    ax.text(5, 7.7, "Condition Account Pipeline", fontsize=16, ha="center",
            color=TEAL, fontfamily="Arial", fontweight="bold")

    # Top: data sources
    ax.text(2.5, 7.15, "Pathway A: No field data", fontsize=10, ha="center",
            color=BLUE, fontfamily="Arial", fontweight="bold")
    ax.text(7.5, 7.15, "Pathway B: Field surveys", fontsize=10, ha="center",
            color=PURPLE, fontfamily="Arial", fontweight="bold")

    # Pathway A
    a_steps = [
        (2.5, 6.4, "Remote sensing proxies\nSST, DHW, Chlorophyll-a\nAllen Coral Atlas"),
        (2.5, 5.2, "Literature reference\nlevels & benchmarks"),
        (2.5, 4.0, "Qualitative condition\nassessment\n(low confidence)"),
    ]
    for x, y, t in a_steps:
        fc = LIGHT_BLUE if y > 5.5 else MINT if y > 4.5 else GREEN
        tc = BODY if y > 4.5 else WHITE
        rounded_box(ax, x, y, 2.8, 0.8, t, fc, tc, fontsize=8)
    for i in range(len(a_steps) - 1):
        arrow(ax, a_steps[i][0], a_steps[i][1] - 0.45, a_steps[i+1][0], a_steps[i+1][1] + 0.45, GREEN)

    # Pathway B
    b_steps = [
        (7.5, 6.4, "Field survey data\nUVC, quadrats, transects\nMonitoring programs"),
        (7.5, 5.2, "Select indicators\n& set reference levels"),
        (7.5, 4.0, "Normalize to CI (0-1)\nHigher-is-better: V/Ref\nHigher-is-worse: 1-(V/Ref)"),
        (7.5, 2.8, "Aggregate across sites\nMean CI, SE, 95% CI"),
    ]
    for x, y, t in b_steps:
        fc = LIGHT_BLUE if y > 5.5 else MINT if y > 4.5 else GREEN
        tc = BODY if y > 4.5 else WHITE
        rounded_box(ax, x, y, 2.8, 0.8, t, fc, tc, fontsize=8)
    for i in range(len(b_steps) - 1):
        arrow(ax, b_steps[i][0], b_steps[i][1] - 0.45, b_steps[i+1][0], b_steps[i+1][1] + 0.45, GREEN)

    # Converge
    rounded_box(ax, 5, 1.5, 7, 0.8,
                "SEEA EA Condition Account\nIndicator | Reference | Opening CI | Closing CI | Change",
                TEAL, fontsize=9)
    arrow(ax, 2.5, 3.55, 3.5, 1.95, TEAL)
    arrow(ax, 7.5, 2.35, 6.5, 1.95, TEAL)

    # Example indicators
    ax.text(5, 0.5, "Example: Coral cover CI = 0.40  |  Macroalgae CI = 0.50  |  Fish biomass CI = 0.36",
            fontsize=8, ha="center", color=GRAY, fontfamily="Arial", style="italic")

    save_fig(fig, outdir / "diagram_condition_pipeline.png")


# =========================================================================
# 4. SERVICES ACCOUNT PIPELINE
# =========================================================================
def diagram_services(outdir):
    fig, ax = plt.subplots(figsize=(12, 8))
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 8)
    ax.axis("off")

    ax.text(6, 7.7, "Ecosystem Services Account Pipeline", fontsize=16, ha="center",
            color=TEAL, fontfamily="Arial", fontweight="bold")

    # Inputs
    inputs = [
        (2, 6.8, "Extent\naccounts\n(ha)"),
        (5, 6.8, "Condition\naccounts\n(CI)"),
        (8, 6.8, "Economic &\nsocial data"),
        (11, 6.8, "Literature\nrates & prices"),
    ]
    for x, y, t in inputs:
        rounded_box(ax, x, y, 2.2, 0.8, t, LIGHT_BLUE, textcolor=BODY, fontsize=8, bold=False)

    # Service types
    services = [
        (1.5, 4.8, "PROVISIONING\nFish catch\nWood/fuel", GREEN),
        (4.5, 4.8, "REGULATING\nCarbon sequestration\nCoastal protection\nNursery habitat", GREEN),
        (8.0, 4.8, "CULTURAL\nRecreation/tourism\nGleaning/subsistence", GREEN),
    ]
    for x, y, t, c in services:
        rounded_box(ax, x, y, 2.8, 1.1, t, c, fontsize=8)

    # Arrows from inputs to services
    for ix, iy, _ in inputs:
        for sx, sy, _, _ in services:
            if abs(ix - sx) < 5:
                arrow(ax, ix, iy - 0.45, sx, sy + 0.6, GREEN + "80")

    # Valuation methods
    ax.text(6, 3.6, "Valuation Methods", fontsize=11, ha="center",
            color=TEAL, fontfamily="Arial", fontweight="bold")

    methods = [
        (1.5, 2.8, "Resource rent\nRevenue - Costs"),
        (4.0, 2.8, "Social cost\nof carbon\n(SCC x Mg CO2)"),
        (6.5, 2.8, "Replacement\ncost"),
        (9.0, 2.8, "Direct\nexpenditure"),
        (11.0, 2.8, "Value\ntransfer"),
    ]
    for x, y, t in methods:
        rounded_box(ax, x, y, 1.9, 0.75, t, MINT, textcolor=BODY, fontsize=7, bold=False)

    # Arrows
    for sx, sy, _, _ in services:
        for mx, my, _ in methods:
            if abs(sx - mx) < 3.5:
                arrow(ax, sx, sy - 0.6, mx, my + 0.4, GRAY + "60")

    # Output tables
    rounded_box(ax, 3.5, 1.3, 5.5, 0.7,
                "Physical Supply Table\nkg/yr, Mg CO2/yr, visitors/yr", TEAL, fontsize=8)
    rounded_box(ax, 9, 1.3, 4.5, 0.7,
                "Monetary Supply Table\nUSD/yr by service and ecosystem", TEAL, fontsize=8)

    for mx, my, _ in methods:
        if mx < 6:
            arrow(ax, mx, my - 0.4, 3.5, 1.7, TEAL + "80")
        else:
            arrow(ax, mx, my - 0.4, 9, 1.7, TEAL + "80")

    # Policy
    rounded_box(ax, 6, 0.3, 8, 0.5,
                "Policy: blue finance, NDCs, MPA justification, blue economy strategy",
                ORANGE, fontsize=8)
    arrow(ax, 3.5, 0.9, 5, 0.6, ORANGE)
    arrow(ax, 9, 0.9, 7, 0.6, ORANGE)

    save_fig(fig, outdir / "diagram_services_pipeline.png")


# =========================================================================
# 5. TRIAGE DECISION TREE
# =========================================================================
def diagram_triage(outdir):
    fig, ax = plt.subplots(figsize=(10, 7))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 7)
    ax.axis("off")

    ax.text(5, 6.7, "Clinic Triage: Which Account Type?", fontsize=16, ha="center",
            color=TEAL, fontfamily="Arial", fontweight="bold")

    # Start
    rounded_box(ax, 5, 5.8, 4.5, 0.6,
                "What is your policy question?", GREEN, fontsize=10)

    # Branch questions
    branches = [
        (1.8, 4.5, "How much\necosystem\ndo we have?", BLUE),
        (5.0, 4.5, "How healthy\nis our\necosystem?", BLUE),
        (8.2, 4.5, "What benefits\ndo people\nget from it?", BLUE),
    ]
    for x, y, t, c in branches:
        rounded_box(ax, x, y, 2.2, 0.8, t, c, fontsize=8)
    arrow(ax, 3.5, 5.45, 1.8, 4.95, BLUE)
    arrow(ax, 5, 5.45, 5, 4.95, BLUE)
    arrow(ax, 6.5, 5.45, 8.2, 4.95, BLUE)

    # Account types
    accounts = [
        (1.8, 3.2, "EXTENT\nACCOUNT", TEAL),
        (5.0, 3.2, "CONDITION\nACCOUNT", TEAL),
        (8.2, 3.2, "SERVICES\nACCOUNT", TEAL),
    ]
    for x, y, t, c in accounts:
        rounded_box(ax, x, y, 2.2, 0.7, t, c, fontsize=9)
    for i in range(3):
        arrow(ax, branches[i][0], branches[i][1] - 0.45, accounts[i][0], accounts[i][1] + 0.4, TEAL)

    # Data check
    ax.text(5, 2.3, "What data do you have?", fontsize=11, ha="center",
            color=GREEN, fontfamily="Arial", fontweight="bold")

    data_opts = [
        (2, 1.5, "No data\n\nPathway A\n(Global datasets,\nvalue transfer)", YELLOW, BODY),
        (5, 1.5, "Some data\n\nPathway A/B\n(Mix of global\nand local)", MINT, BODY),
        (8, 1.5, "Field / local data\n\nPathway B\n(Primary analysis)", GREEN, WHITE),
    ]
    for x, y, t, fc, tc in data_opts:
        rounded_box(ax, x, y, 2.4, 1.1, t, fc, textcolor=tc, fontsize=7, bold=False)

    save_fig(fig, outdir / "diagram_triage.png")


# =========================================================================
# MAIN
# =========================================================================
def main():
    outdir = Path(__file__).parent
    print("Generating pipeline diagrams...")

    diagram_overview(outdir)
    diagram_extent(outdir)
    diagram_condition(outdir)
    diagram_services(outdir)
    diagram_triage(outdir)

    print("\nDone! All diagrams in:", outdir)


if __name__ == "__main__":
    main()
