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
BLUE_GRAY = "#5B7B8A"
ORANGE_WARM = "#D4845A"
TAN = "#B8A07E"


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
    fig, ax = plt.subplots(figsize=(14, 9))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 9)
    ax.axis("off")

    # Title
    ax.text(7, 8.6, "Ocean Accounts: The Complete Framework", fontsize=17, ha="center",
            color=TEAL, fontfamily="Arial", fontweight="bold")

    # Data sources (top)
    sources = [
        (1.8, 7.6, "Satellite\nimagery"),
        (4.6, 7.6, "Field\nsurveys"),
        (7.4, 7.6, "Government\nstatistics"),
        (10.2, 7.6, "Global\ndatasets"),
        (12.6, 7.6, "Community\nknowledge"),
    ]
    for x, y, t in sources:
        rounded_box(ax, x, y, 2.0, 0.7, t, LIGHT_BLUE, textcolor=BODY, fontsize=8, bold=False)

    # Spatial framework
    rounded_box(ax, 7, 6.4, 12.5, 0.6,
                "Spatial Data Framework: Basic Spatial Units (BSU grid)", GREEN, fontsize=10)

    # Arrows: data sources to spatial framework
    for x, _, _ in sources:
        arrow(ax, x, 7.2, min(x, 12), 6.75, GREEN)

    # Arrows: spatial framework down to account rows
    for tx in [2.5, 7.0, 11.5, 2.5, 7.0, 11.5]:
        arrow(ax, 7, 6.05, tx, 5.55 if tx in [2.5, 7.0, 11.5] else 4.0, TEAL + "50")

    # ---- Row 1: SEEA-EA accounts (green) ----
    ax.text(0.6, 5.55, "SEEA-EA", fontsize=8, ha="center", va="center", color=GREEN,
            fontfamily="Arial", fontweight="bold", rotation=90)

    rounded_box(ax, 2.5, 5.2, 3.5, 0.9,
                "EXTENT ACCOUNTS\nEcosystem area (ha)\nOpening / Closing", TEAL, fontsize=8)
    rounded_box(ax, 7.0, 5.2, 3.5, 0.9,
                "CONDITION ACCOUNTS\nEcosystem health (CI 0-1)\nIndicators / Reference", TEAL, fontsize=8)
    rounded_box(ax, 11.5, 5.2, 3.5, 0.9,
                "SERVICE ACCOUNTS\nSupply + Use tables\nPhysical / Monetary (SUT)", TEAL, fontsize=8)

    # Horizontal arrows between SEEA-EA accounts
    arrow(ax, 4.35, 5.2, 5.15, 5.2, GREEN)
    arrow(ax, 8.85, 5.2, 9.65, 5.2, GREEN)
    ax.text(4.75, 5.55, "extent\ninforms\ncondition", fontsize=5.5, color=GRAY,
            fontfamily="Arial", ha="center")
    ax.text(9.25, 5.55, "condition\ninforms\nservices", fontsize=5.5, color=GRAY,
            fontfamily="Arial", ha="center")

    # ---- Row 2: Other frameworks ----
    rounded_box(ax, 2.5, 3.6, 3.5, 0.9,
                "OCEAN ECONOMY (OESA)\nSNA framework\nOcean GDP, GVA", BLUE_GRAY, fontsize=8)
    rounded_box(ax, 7.0, 3.6, 3.5, 0.9,
                "WASTE & EMISSIONS\nSEEA-CF\nPollution flows, plastics", ORANGE_WARM, fontsize=8)
    rounded_box(ax, 11.5, 3.6, 3.5, 0.9,
                "SOCIAL & GOVERNANCE\nGOAP\nWellbeing, equity, access", TAN, textcolor=BODY, fontsize=8)

    ax.text(0.6, 3.6, "Other\nframeworks", fontsize=7, ha="center", va="center", color=GRAY,
            fontfamily="Arial", fontweight="bold", rotation=90)

    # Arrows: spatial framework to Row 2
    arrow(ax, 4.0, 6.05, 2.5, 4.1, BLUE_GRAY + "60")
    arrow(ax, 7.0, 6.05, 7.0, 4.1, ORANGE_WARM + "60")
    arrow(ax, 10.0, 6.05, 11.5, 4.1, TAN + "60")

    # Arrows: spatial framework to Row 1
    arrow(ax, 4.0, 6.05, 2.5, 5.7, TEAL + "60")
    arrow(ax, 7.0, 6.05, 7.0, 5.7, TEAL + "60")
    arrow(ax, 10.0, 6.05, 11.5, 5.7, TEAL + "60")

    # ---- Policy outputs (bottom) ----
    ax.text(7, 2.55, "Policy Applications", fontsize=11, ha="center", color=ORANGE,
            fontfamily="Arial", fontweight="bold")

    outputs = [
        (1.8, 1.6, "SDG 14\nreporting"),
        (4.3, 1.6, "NDC / NBSAP\nintegration"),
        (6.8, 1.6, "Marine spatial\nplanning"),
        (9.3, 1.6, "Blue finance\n& investment"),
        (11.8, 1.6, "National ocean\npolicy"),
    ]
    for x, y, t in outputs:
        rounded_box(ax, x, y, 2.2, 0.7, t, ORANGE, fontsize=8)

    # Arrows from all 6 accounts to policy bar
    for ax_x in [2.5, 7.0, 11.5]:
        for ox, _, _ in outputs:
            arrow(ax, ax_x, 4.7 if ax_x == 7.0 else 3.1, ox, 2.0, ORANGE + "30")
    # Stronger arrows from Row 1
    for ox, _, _ in outputs:
        arrow(ax, 7, 3.1, ox, 2.0, ORANGE + "50")

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
    fig, ax = plt.subplots(figsize=(13, 11))
    ax.set_xlim(0, 13)
    ax.set_ylim(0, 11)
    ax.axis("off")

    ax.text(6.5, 10.6, "Ecosystem Services Account Pipeline", fontsize=17, ha="center",
            color=TEAL, fontfamily="Arial", fontweight="bold")

    # Inputs
    inputs = [
        (2, 9.6, "Extent\naccounts\n(ha)"),
        (5, 9.6, "Condition\naccounts\n(CI)"),
        (8.5, 9.6, "Economic &\nsocial data"),
        (11.5, 9.6, "Literature\nrates & prices"),
    ]
    for x, y, t in inputs:
        rounded_box(ax, x, y, 2.2, 0.8, t, LIGHT_BLUE, textcolor=BODY, fontsize=8, bold=False)

    # Service types
    services = [
        (1.8, 7.6, "PROVISIONING\nFish catch\nWood/fuel", GREEN),
        (5.5, 7.6, "REGULATING\nCarbon sequestration\nCoastal protection\nNursery habitat", GREEN),
        (9.5, 7.6, "CULTURAL\nRecreation/tourism\nGleaning/subsistence", GREEN),
    ]
    for x, y, t, c in services:
        rounded_box(ax, x, y, 2.8, 1.1, t, c, fontsize=8)

    # Arrows from inputs to services
    for ix, iy, _ in inputs:
        for sx, sy, _, _ in services:
            if abs(ix - sx) < 5.5:
                arrow(ax, ix, iy - 0.45, sx, sy + 0.6, GREEN + "80")

    # Valuation methods
    ax.text(6.5, 6.4, "Valuation Methods", fontsize=11, ha="center",
            color=TEAL, fontfamily="Arial", fontweight="bold")

    methods = [
        (1.5, 5.6, "Resource rent\nRevenue - Costs"),
        (4.0, 5.6, "Social cost\nof carbon\n(SCC x Mg CO2)"),
        (6.5, 5.6, "Replacement\ncost"),
        (9.0, 5.6, "Direct\nexpenditure"),
        (11.5, 5.6, "Value\ntransfer"),
    ]
    for x, y, t in methods:
        rounded_box(ax, x, y, 2.0, 0.75, t, MINT, textcolor=BODY, fontsize=7, bold=False)

    # Arrows from services to methods
    for sx, sy, _, _ in services:
        for mx, my, _ in methods:
            if abs(sx - mx) < 3.5:
                arrow(ax, sx, sy - 0.6, mx, my + 0.4, GRAY + "60")

    # ---- Supply tables ----
    rounded_box(ax, 3.5, 4.2, 5.5, 0.7,
                "Physical Supply Table\nkg/yr, Mg CO2/yr, visitors/yr", TEAL, fontsize=8)
    rounded_box(ax, 10, 4.2, 4.5, 0.7,
                "Monetary Supply Table\nUSD/yr by service and ecosystem", TEAL, fontsize=8)

    for mx, my, _ in methods:
        if mx < 6:
            arrow(ax, mx, my - 0.4, 3.5, 4.6, TEAL + "80")
        else:
            arrow(ax, mx, my - 0.4, 10, 4.6, TEAL + "80")

    # ---- USE tables (new) ----
    rounded_box(ax, 3.5, 2.8, 5.5, 0.8,
                "USE TABLES\nWho benefits: fisheries, tourism,\nhouseholds, govt, global", GREEN, fontsize=8)
    rounded_box(ax, 10, 2.8, 4.5, 0.8,
                "Monetary Use Table\nUSD/yr by user and service", GREEN, fontsize=8)

    arrow(ax, 3.5, 3.8, 3.5, 3.25, TEAL)
    arrow(ax, 10, 3.8, 10, 3.25, TEAL)

    # ---- Integrated SUT ----
    rounded_box(ax, 6.5, 1.6, 9, 0.7,
                "INTEGRATED SUT (SEEA EA Table 7.1)\nSupply + Use, Physical + Monetary", TEAL, fontsize=9)

    arrow(ax, 3.5, 2.35, 4.5, 2.0, TEAL)
    arrow(ax, 10, 2.35, 8.5, 2.0, TEAL)

    # ---- Policy ----
    rounded_box(ax, 6.5, 0.4, 10, 0.55,
                "Policy: blue finance, NDCs, MPA justification, blue economy strategy",
                ORANGE, fontsize=8)
    arrow(ax, 6.5, 1.2, 6.5, 0.7, ORANGE)

    save_fig(fig, outdir / "diagram_services_pipeline.png")


# =========================================================================
# 5. TRIAGE DECISION TREE
# =========================================================================
def diagram_triage(outdir):
    fig, ax = plt.subplots(figsize=(14, 10))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 10)
    ax.axis("off")

    ax.text(7, 9.6, "Clinic Triage: Which Account Type?", fontsize=17, ha="center",
            color=TEAL, fontfamily="Arial", fontweight="bold")

    # Start
    rounded_box(ax, 7, 8.7, 5.5, 0.6,
                "What is your policy question?", GREEN, fontsize=11)

    # ---- Group 1: SEEA-EA (teal) ----
    ax.text(4.0, 7.65, "SEEA-EA", fontsize=9, ha="center", color=TEAL,
            fontfamily="Arial", fontweight="bold")

    q1 = [
        (1.5, 6.8, '"How much\necosystem\ndo we have?"', BLUE),
        (4.0, 6.8, '"How healthy\nis our\necosystem?"', BLUE),
        (6.5, 6.8, '"What benefits\ndo people\nget from it?"', BLUE),
    ]
    for x, y, t, c in q1:
        rounded_box(ax, x, y, 2.2, 0.85, t, c, fontsize=8)
        arrow(ax, 7, 8.35, x, 7.28, BLUE + "80")

    a1 = [
        (1.5, 5.5, "EXTENT\nACCOUNT", TEAL),
        (4.0, 5.5, "CONDITION\nACCOUNT", TEAL),
        (6.5, 5.5, "SERVICES\nACCOUNT", TEAL),
    ]
    for x, y, t, c in a1:
        rounded_box(ax, x, y, 2.2, 0.7, t, c, fontsize=9)
    for i in range(3):
        arrow(ax, q1[i][0], q1[i][1] - 0.48, a1[i][0], a1[i][1] + 0.4, TEAL)

    # ---- Group 2: SNA / OESA (blue-gray) ----
    ax.text(9.5, 7.65, "SNA / Economy", fontsize=9, ha="center", color=BLUE_GRAY,
            fontfamily="Arial", fontweight="bold")

    q2 = [
        (9.0, 6.8, '"How big is\nthe ocean\neconomy?"', BLUE_GRAY),
        (11.5, 6.8, '"What does\ntourism\ncontribute?"', BLUE_GRAY),
    ]
    for x, y, t, c in q2:
        rounded_box(ax, x, y, 2.2, 0.85, t, c, fontsize=8)
        arrow(ax, 7, 8.35, x, 7.28, BLUE_GRAY + "80")

    a2 = [
        (9.0, 5.5, "OESA\nACCOUNT", BLUE_GRAY),
        (11.5, 5.5, "OTSA\nACCOUNT", BLUE_GRAY),
    ]
    for x, y, t, c in a2:
        rounded_box(ax, x, y, 2.2, 0.7, t, c, fontsize=9)
    for i in range(2):
        arrow(ax, q2[i][0], q2[i][1] - 0.48, a2[i][0], a2[i][1] + 0.4, BLUE_GRAY)

    # ---- Group 3: SEEA-CF / Waste (orange) ----
    q3_x, q3_y = 3.5, 4.3
    rounded_box(ax, q3_x, q3_y, 2.8, 0.85,
                '"What pollution\nenters the ocean?"', ORANGE_WARM, fontsize=8)
    arrow(ax, 7, 8.35, q3_x, q3_y + 0.48, ORANGE_WARM + "60")
    rounded_box(ax, q3_x, 3.1, 2.2, 0.7, "WASTE &\nEMISSIONS", ORANGE_WARM, fontsize=9)
    arrow(ax, q3_x, q3_y - 0.48, q3_x, 3.5, ORANGE_WARM)

    ax.text(q3_x, 4.95, "SEEA-CF", fontsize=8, ha="center", color=ORANGE_WARM,
            fontfamily="Arial", fontweight="bold")

    # ---- Group 4: GOAP / Social (tan) ----
    q4_x, q4_y = 8.5, 4.3
    rounded_box(ax, q4_x, q4_y, 2.8, 0.85,
                '"Who benefits?\nWho is affected?"', TAN, textcolor=BODY, fontsize=8)
    arrow(ax, 7, 8.35, q4_x, q4_y + 0.48, TAN + "80")
    rounded_box(ax, q4_x, 3.1, 2.2, 0.7, "SOCIAL &\nGOVERNANCE", TAN, textcolor=BODY, fontsize=9)
    arrow(ax, q4_x, q4_y - 0.48, q4_x, 3.5, TAN)

    ax.text(q4_x, 4.95, "GOAP", fontsize=8, ha="center", color=TAN,
            fontfamily="Arial", fontweight="bold")

    # ---- Data pathway cards (bottom) ----
    ax.text(7, 2.05, "What data do you have?", fontsize=12, ha="center",
            color=GREEN, fontfamily="Arial", fontweight="bold")

    data_opts = [
        (2.5, 1.0, "No data\n\nPathway A\n(Global datasets,\nvalue transfer)", YELLOW, BODY),
        (7.0, 1.0, "Some data\n\nPathway A/B\n(Mix of global\nand local)", MINT, BODY),
        (11.5, 1.0, "Field / local data\n\nPathway B\n(Primary analysis)", GREEN, WHITE),
    ]
    for x, y, t, fc, tc in data_opts:
        rounded_box(ax, x, y, 3.0, 1.3, t, fc, textcolor=tc, fontsize=8, bold=False)

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
