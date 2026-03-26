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
    fig, ax = plt.subplots(figsize=(14, 10))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 10)
    ax.axis("off")

    # Title
    ax.text(7, 9.6, "Ocean Accounts: One Framework, Many Policy Uses",
            fontsize=17, ha="center", color=TEAL, fontfamily="Arial", fontweight="bold")

    # ---- TOP: COMPILE ONCE banner ----
    banner_top = FancyBboxPatch((1.0, 8.7), 12.0, 0.55,
                                boxstyle="round,pad=0.08", facecolor=MINT,
                                edgecolor=TEAL, linewidth=1.5)
    ax.add_patch(banner_top)
    ax.text(7, 8.97, "COMPILE ONCE", fontsize=13, ha="center", va="center",
            color=TEAL, fontfamily="Arial", fontweight="bold")

    # Data sources
    sources = [
        (1.8, 8.15, "Satellite"),
        (4.2, 8.15, "Field\nsurveys"),
        (6.6, 8.15, "Government\nstatistics"),
        (9.0, 8.15, "Global\ndatasets"),
        (11.4, 8.15, "Community\nknowledge"),
    ]
    for x, y, t in sources:
        rounded_box(ax, x, y, 2.0, 0.55, t, LIGHT_BLUE, textcolor=BODY, fontsize=7, bold=False)

    # Arrows from sources down to BSU band
    for x, _, _ in sources:
        arrow(ax, x, 7.85, x, 7.45, GREEN)

    # ---- MIDDLE: BSU spatial framework as wide green band ----
    bsu_band = FancyBboxPatch((0.5, 5.05), 13.0, 0.65,
                              boxstyle="round,pad=0.08", facecolor=GREEN,
                              edgecolor=TEAL, linewidth=2.0, alpha=0.95)
    ax.add_patch(bsu_band)
    ax.text(7, 5.37, "SPATIAL DATA FRAMEWORK  (Basic Spatial Units)",
            fontsize=12, ha="center", va="center", color=WHITE,
            fontfamily="Arial", fontweight="bold")

    # ---- ABOVE BSU: ENVIRONMENT domain ----
    ax.text(0.6, 7.2, "ENVIRONMENT", fontsize=9, ha="center", va="center",
            color=TEAL, fontfamily="Arial", fontweight="bold", rotation=90)

    # SEEA-EA chain: EXTENT -> CONDITION -> SERVICES
    rounded_box(ax, 2.5, 6.7, 2.8, 0.8,
                "EXTENT\nEcosystem area (ha)", TEAL, fontsize=8)
    rounded_box(ax, 6.0, 6.7, 2.8, 0.8,
                "CONDITION\nEcosystem health (CI)", TEAL, fontsize=8)
    rounded_box(ax, 9.5, 6.7, 2.8, 0.8,
                "SERVICES\nSupply & Use (SUT)", TEAL, fontsize=8)

    # Horizontal arrows for SEEA-EA logical progression
    arrow(ax, 3.95, 6.7, 4.55, 6.7, GREEN)
    ax.text(4.25, 6.95, "informs", fontsize=6, color=GRAY, fontfamily="Arial", ha="center")
    arrow(ax, 7.45, 6.7, 8.05, 6.7, GREEN)
    ax.text(7.75, 6.95, "informs", fontsize=6, color=GRAY, fontfamily="Arial", ha="center")

    # WASTE & EMISSIONS (orange arrow from economy up to environment)
    rounded_box(ax, 12.3, 6.7, 2.2, 0.8,
                "WASTE &\nEMISSIONS", ORANGE_WARM, fontsize=8)

    # Arrows from environment boxes down to BSU
    for bx in [2.5, 6.0, 9.5, 12.3]:
        arrow(ax, bx, 6.25, bx, 5.75, TEAL + "60")

    # ---- BELOW BSU: ECONOMY & SOCIETY domain ----
    ax.text(0.6, 3.8, "ECONOMY\n&\nSOCIETY", fontsize=8, ha="center", va="center",
            color=BLUE_GRAY, fontfamily="Arial", fontweight="bold", rotation=90)

    # OCEAN ECONOMY (left)
    rounded_box(ax, 3.5, 3.8, 4.0, 0.9,
                "OCEAN ECONOMY (OESA)\nOcean GDP, GVA, employment", BLUE_GRAY, fontsize=8)

    # SOCIAL & GOVERNANCE (right)
    rounded_box(ax, 10.5, 3.8, 4.0, 0.9,
                "SOCIAL & GOVERNANCE\nWellbeing, equity, access", TAN, textcolor=BODY, fontsize=8)

    # Arrows from BSU down to economy/society
    arrow(ax, 4.5, 5.0, 3.5, 4.3, BLUE_GRAY + "60")
    arrow(ax, 9.5, 5.0, 10.5, 4.3, TAN + "60")

    # Economy DEPENDS ON ecosystem services (arrow up from OESA to Services)
    ax.annotate("", xy=(9.0, 6.25), xytext=(4.5, 4.3),
                arrowprops=dict(arrowstyle="-|>", color=BLUE, lw=1.8,
                                connectionstyle="arc3,rad=-0.2"))
    ax.text(5.7, 5.6, "depends on\nservices", fontsize=6.5, color=BLUE,
            fontfamily="Arial", ha="center", style="italic")

    # Economy GENERATES waste/pollution (orange arrow from OESA up to Waste)
    ax.annotate("", xy=(12.3, 6.25), xytext=(5.0, 4.3),
                arrowprops=dict(arrowstyle="-|>", color=ORANGE, lw=1.8,
                                connectionstyle="arc3,rad=-0.25"))
    ax.text(9.8, 5.6, "generates\npollution", fontsize=6.5, color=ORANGE,
            fontfamily="Arial", ha="center", style="italic")

    # Social ENABLES/CONSTRAINS both (horizontal dashed connections)
    ax.annotate("", xy=(5.55, 3.8), xytext=(8.45, 3.8),
                arrowprops=dict(arrowstyle="<|-|>", color=TAN, lw=1.5,
                                linestyle="dashed"))
    ax.text(7.0, 3.45, "enables / constrains", fontsize=6.5, color=TAN,
            fontfamily="Arial", ha="center", style="italic")

    # ---- BOTTOM: REPORT MANY banner ----
    banner_bot = FancyBboxPatch((1.0, 2.05), 12.0, 0.55,
                                boxstyle="round,pad=0.08", facecolor=ORANGE + "20",
                                edgecolor=ORANGE, linewidth=1.5)
    ax.add_patch(banner_bot)
    ax.text(7, 2.32, "REPORT MANY", fontsize=13, ha="center", va="center",
            color=ORANGE, fontfamily="Arial", fontweight="bold")

    # Arrows from economy/society down to report banner
    arrow(ax, 3.5, 3.3, 4.0, 2.65, ORANGE + "50")
    arrow(ax, 10.5, 3.3, 10.0, 2.65, ORANGE + "50")

    # Policy outputs
    outputs = [
        (1.8, 1.3, "SDG 14\nreporting"),
        (4.3, 1.3, "NDC /\nNBSAP"),
        (6.8, 1.3, "Marine spatial\nplanning"),
        (9.3, 1.3, "Blue finance\n& investment"),
        (11.8, 1.3, "National ocean\npolicy"),
    ]
    for x, y, t in outputs:
        rounded_box(ax, x, y, 2.2, 0.65, t, ORANGE, fontsize=8)

    # Arrows from banner to outputs
    for x, _, _ in outputs:
        arrow(ax, x, 2.0, x, 1.67, ORANGE + "70")

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

    # Title and subtitle
    ax.text(7, 9.55, "Where to Start in Ocean Accounts", fontsize=17, ha="center",
            color=TEAL, fontfamily="Arial", fontweight="bold")
    ax.text(7, 9.1, "One integrated framework -- choose your entry point", fontsize=11,
            ha="center", color=GRAY, fontfamily="Arial", style="italic")

    # Top question
    rounded_box(ax, 7, 8.4, 6.0, 0.6,
                "What is your policy priority?", GREEN, fontsize=12)

    # Note box
    note_box = FancyBboxPatch((1.2, 7.35), 11.6, 0.55,
                              boxstyle="round,pad=0.08", facecolor=YELLOW,
                              edgecolor=GRAY, linewidth=1.0, linestyle="--")
    ax.add_patch(note_box)
    ax.text(7, 7.62, "All components share the same spatial foundation (BSUs) and connect to each other.\n"
            "Your starting point depends on your priority, but you are building one integrated system.",
            fontsize=7.5, ha="center", va="center", color=BODY, fontfamily="Arial", style="italic")

    # ---- Central BSU circle ----
    bsu_circle = plt.Circle((7, 4.5), 1.1, facecolor=GREEN, edgecolor=TEAL,
                            linewidth=2.5, alpha=0.9, zorder=5)
    ax.add_patch(bsu_circle)
    ax.text(7, 4.65, "BSU", fontsize=14, ha="center", va="center", color=WHITE,
            fontfamily="Arial", fontweight="bold", zorder=6)
    ax.text(7, 4.3, "Spatial\nFramework", fontsize=7.5, ha="center", va="center", color=WHITE,
            fontfamily="Arial", zorder=6)

    # ---- Group: ENVIRONMENT (top-left, teal) ----
    ax.text(2.8, 6.7, "ENVIRONMENT", fontsize=9, ha="center", color=TEAL,
            fontfamily="Arial", fontweight="bold")

    env_items = [
        (1.5, 5.9, '"Mapping\necosystems?"', "Extent"),
        (2.8, 5.1, '"Measuring\nhealth?"', "Condition"),
        (4.1, 5.9, '"Quantifying\nbenefits?"', "Services"),
    ]
    for x, y, q, label in env_items:
        rounded_box(ax, x, y, 2.0, 0.75, q, TEAL, fontsize=7)
        ax.text(x, y - 0.55, label, fontsize=7, ha="center", color=TEAL,
                fontfamily="Arial", fontweight="bold")
        arrow(ax, 7, 8.05, x, y + 0.42, TEAL + "60")

    # Connect environment group to BSU
    arrow(ax, 3.2, 4.9, 5.9, 4.7, TEAL + "90")
    arrow(ax, 5.9, 4.7, 3.2, 4.9, TEAL + "40")

    # ---- Group: ECONOMY (top-right, blue-gray) ----
    ax.text(11.2, 6.7, "ECONOMY", fontsize=9, ha="center", color=BLUE_GRAY,
            fontfamily="Arial", fontweight="bold")

    rounded_box(ax, 11.2, 5.9, 2.5, 0.75,
                '"Measuring\nocean GDP?"', BLUE_GRAY, fontsize=7)
    ax.text(11.2, 5.35, "OESA / OTSA", fontsize=7, ha="center", color=BLUE_GRAY,
            fontfamily="Arial", fontweight="bold")
    arrow(ax, 7, 8.05, 11.2, 6.32, BLUE_GRAY + "60")

    # Connect economy to BSU
    arrow(ax, 10.0, 5.6, 8.1, 4.7, BLUE_GRAY + "90")
    arrow(ax, 8.1, 4.7, 10.0, 5.6, BLUE_GRAY + "40")

    # ---- Group: PRESSURES (bottom-right, orange) ----
    ax.text(11.2, 3.8, "PRESSURES", fontsize=9, ha="center", color=ORANGE_WARM,
            fontfamily="Arial", fontweight="bold")

    rounded_box(ax, 11.2, 3.1, 2.5, 0.75,
                '"Tracking\npollution?"', ORANGE_WARM, fontsize=7)
    ax.text(11.2, 2.55, "Waste & Emissions", fontsize=7, ha="center", color=ORANGE_WARM,
            fontfamily="Arial", fontweight="bold")

    # Connect pressures to BSU
    arrow(ax, 10.0, 3.4, 8.1, 4.3, ORANGE_WARM + "90")
    arrow(ax, 8.1, 4.3, 10.0, 3.4, ORANGE_WARM + "40")

    # ---- Group: SOCIETY (bottom-left, tan) ----
    ax.text(2.8, 3.8, "SOCIETY", fontsize=9, ha="center", color=TAN,
            fontfamily="Arial", fontweight="bold")

    rounded_box(ax, 2.8, 3.1, 2.5, 0.75,
                '"Understanding\ncommunities?"', TAN, textcolor=BODY, fontsize=7)
    ax.text(2.8, 2.55, "Social & Governance", fontsize=7, ha="center", color=TAN,
            fontfamily="Arial", fontweight="bold")

    # Connect society to BSU
    arrow(ax, 4.2, 3.4, 5.9, 4.3, TAN + "90")
    arrow(ax, 5.9, 4.3, 4.2, 3.4, TAN + "40")

    # ---- Cross-connections between groups (lighter, showing integration) ----
    # Environment <-> Economy
    ax.annotate("", xy=(10.0, 6.0), xytext=(5.1, 5.9),
                arrowprops=dict(arrowstyle="<|-|>", color=GRAY + "50", lw=1.0,
                                linestyle="dotted", connectionstyle="arc3,rad=-0.15"))
    # Economy <-> Pressures
    ax.annotate("", xy=(11.2, 5.1), xytext=(11.2, 3.9),
                arrowprops=dict(arrowstyle="<|-|>", color=GRAY + "50", lw=1.0,
                                linestyle="dotted"))
    # Society <-> Environment
    ax.annotate("", xy=(1.8, 5.1), xytext=(2.5, 3.9),
                arrowprops=dict(arrowstyle="<|-|>", color=GRAY + "50", lw=1.0,
                                linestyle="dotted"))

    # ---- Bottom message ----
    bottom_box = FancyBboxPatch((1.5, 0.5), 11.0, 0.65,
                                boxstyle="round,pad=0.08", facecolor=MINT,
                                edgecolor=TEAL, linewidth=1.2)
    ax.add_patch(bottom_box)
    ax.text(7, 0.82, "All paths lead to integrated ocean accounts that serve multiple policy needs",
            fontsize=9, ha="center", va="center", color=TEAL,
            fontfamily="Arial", fontweight="bold")

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
