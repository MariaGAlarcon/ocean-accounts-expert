#!/usr/bin/env python3
"""Generate CLEAN overview and triage diagrams. Simple layouts, no mess."""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
from pathlib import Path

# GOAP Colors
TEAL = "#0A5455"
GREEN = "#3B9C7B"
MINT = "#D4EEE5"
BODY = "#30302F"
GRAY = "#717171"
WHITE = "#FFFFFF"
LIGHT_BLUE = "#B5D0D6"
BLUE_GRAY = "#66A3B5"
TAN = "#B59F81"
LIGHT_TAN = "#F5EFE6"
ORANGE = "#E76F51"
LIGHT_ORANGE = "#FDEEE9"
LIGHT_GREEN = "#E8F5E9"


def box(ax, x, y, w, h, text, color, textcolor=WHITE, fontsize=10, bold=True):
    """Draw a clean rounded box with centered text."""
    b = FancyBboxPatch((x - w/2, y - h/2), w, h,
                       boxstyle="round,pad=0.08", facecolor=color,
                       edgecolor="none", linewidth=0)
    ax.add_patch(b)
    weight = "bold" if bold else "normal"
    ax.text(x, y, text, ha="center", va="center", fontsize=fontsize,
            color=textcolor, fontfamily="Arial", fontweight=weight,
            linespacing=1.3)


def arrow_down(ax, x, y1, y2, color=GRAY):
    """Simple downward arrow."""
    ax.annotate("", xy=(x, y2), xytext=(x, y1),
                arrowprops=dict(arrowstyle="-|>", color=color, lw=1.5))


def arrow_right(ax, x1, x2, y, color=GRAY):
    """Simple rightward arrow."""
    ax.annotate("", xy=(x2, y), xytext=(x1, y),
                arrowprops=dict(arrowstyle="-|>", color=color, lw=1.5))


def save(fig, path):
    fig.savefig(str(path), dpi=200, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"  Created: {path}")


# =========================================================================
# OVERVIEW: Clean 4-level layout
# =========================================================================
def diagram_overview(outdir):
    fig, ax = plt.subplots(figsize=(14, 9))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 9)
    ax.axis("off")

    # TITLE
    ax.text(7, 8.7, "Ocean Accounts: One Framework, Many Policy Uses",
            fontsize=18, ha="center", color=TEAL, fontfamily="Arial", fontweight="bold")

    # LEVEL 1: COMPILE ONCE + data sources
    box(ax, 7, 8.0, 6, 0.5, "COMPILE ONCE", GREEN, fontsize=13)

    sources = ["Satellite\nimagery", "Field\nsurveys", "Government\nstatistics",
               "Global\ndatasets", "Community\nknowledge"]
    for i, s in enumerate(sources):
        x = 2.0 + i * 2.5
        box(ax, x, 7.2, 2.0, 0.55, s, LIGHT_BLUE, textcolor=BODY, fontsize=8, bold=False)
        arrow_down(ax, x, 7.45, 7.75, GREEN)

    # LEVEL 2: THE FRAMEWORK (one big container)
    # Outer container
    container = FancyBboxPatch((0.5, 2.8), 13, 4.0,
                               boxstyle="round,pad=0.15", facecolor="#F8FAFA",
                               edgecolor=TEAL, linewidth=2)
    ax.add_patch(container)
    ax.text(7, 6.55, "OCEAN ACCOUNTS FRAMEWORK", fontsize=12, ha="center",
            color=TEAL, fontfamily="Arial", fontweight="bold")

    # BSU band in the middle of the container
    bsu = FancyBboxPatch((1.0, 4.55), 12, 0.5,
                         boxstyle="round,pad=0.05", facecolor=GREEN,
                         edgecolor="none")
    ax.add_patch(bsu)
    ax.text(7, 4.8, "Shared Spatial Framework: Basic Spatial Units (BSUs)",
            fontsize=10, ha="center", color=WHITE, fontfamily="Arial", fontweight="bold")

    # Top row: SEEA-EA ecological accounts (above BSU)
    box(ax, 2.5, 5.7, 3.0, 0.7, "EXTENT\nEcosystem area (ha)", TEAL, fontsize=9)
    box(ax, 6.0, 5.7, 3.0, 0.7, "CONDITION\nEcosystem health (CI)", TEAL, fontsize=9)
    box(ax, 9.8, 5.7, 3.4, 0.7, "SERVICES\nSupply + Use (SUT)", TEAL, fontsize=9)
    box(ax, 12.5, 5.7, 1.8, 0.7, "WASTE\nEmissions", ORANGE, fontsize=8)

    # Arrows: extent → condition → services
    arrow_right(ax, 4.1, 4.4, 5.7, TEAL)
    arrow_right(ax, 7.6, 7.9, 5.7, TEAL)
    ax.text(4.25, 5.95, "informs", fontsize=7, color=GRAY, ha="center", fontfamily="Arial")
    ax.text(7.75, 5.95, "informs", fontsize=7, color=GRAY, ha="center", fontfamily="Arial")

    # Bottom row: Economy + Society (below BSU)
    box(ax, 3.5, 3.6, 4.5, 0.7, "OCEAN ECONOMY (OESA)\nOcean GDP, GVA, employment", BLUE_GRAY, fontsize=9)
    box(ax, 9.5, 3.6, 4.5, 0.7, "SOCIAL & GOVERNANCE\nWellbeing, equity, access", TAN, fontsize=9)

    # Simple vertical connectors from BSU to rows (no crossing)
    for x in [2.5, 6.0, 9.8, 12.5]:
        arrow_down(ax, x, 5.25, 5.05, GREEN)
    for x in [3.5, 9.5]:
        arrow_down(ax, x, 4.5, 4.05, GREEN)

    # LEVEL 3: REPORT MANY
    box(ax, 7, 2.1, 6, 0.5, "REPORT MANY", ORANGE, fontsize=13)

    # Arrow from framework to report many
    arrow_down(ax, 7, 2.75, 2.4, ORANGE)

    # LEVEL 4: Policy boxes
    policies = ["SDG 14\nreporting", "NDC /\nNBSAP", "Marine spatial\nplanning",
                "Blue finance\n& investment", "National ocean\npolicy"]
    for i, p in enumerate(policies):
        x = 1.5 + i * 2.8
        box(ax, x, 1.1, 2.3, 0.65, p, ORANGE, fontsize=8)

    save(fig, outdir / "diagram_overview.png")


# =========================================================================
# TRIAGE: Clean 2x2 grid layout
# =========================================================================
def diagram_triage(outdir):
    fig, ax = plt.subplots(figsize=(12, 9))
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 9)
    ax.axis("off")

    # TITLE
    ax.text(6, 8.7, "Where to Start in Ocean Accounts?",
            fontsize=18, ha="center", color=TEAL, fontfamily="Arial", fontweight="bold")
    ax.text(6, 8.3, "One integrated framework -- choose your entry point",
            fontsize=11, ha="center", color=GRAY, fontfamily="Arial")

    # TOP: Policy priority question
    box(ax, 6, 7.5, 8, 0.6, "What is your policy priority?", GREEN, fontsize=13)

    # 2x2 GRID of account groups
    # Top-left: ENVIRONMENT
    env_bg = FancyBboxPatch((0.5, 4.4), 5.0, 2.5,
                            boxstyle="round,pad=0.1", facecolor=MINT,
                            edgecolor=TEAL, linewidth=1.5)
    ax.add_patch(env_bg)
    ax.text(3.0, 6.6, "ENVIRONMENT", fontsize=11, ha="center",
            color=TEAL, fontfamily="Arial", fontweight="bold")
    ax.text(3.0, 6.25, "Ecosystems and their value", fontsize=8,
            ha="center", color=GRAY, fontfamily="Arial")

    box(ax, 1.4, 5.3, 1.4, 0.55, "EXTENT\nArea (ha)", TEAL, fontsize=7)
    box(ax, 3.0, 5.3, 1.4, 0.55, "CONDITION\nHealth (CI)", TEAL, fontsize=7)
    box(ax, 4.6, 5.3, 1.4, 0.55, "SERVICES\nSupply+Use", TEAL, fontsize=7)
    # Arrows: extent → condition → services
    ax.annotate("", xy=(2.25, 5.3), xytext=(2.15, 5.3),
                arrowprops=dict(arrowstyle="-|>", color=WHITE, lw=1.2))
    ax.annotate("", xy=(3.85, 5.3), xytext=(3.75, 5.3),
                arrowprops=dict(arrowstyle="-|>", color=WHITE, lw=1.2))

    # Top-right: ECONOMY
    eco_bg = FancyBboxPatch((6.5, 4.4), 5.0, 2.5,
                            boxstyle="round,pad=0.1", facecolor="#E8EEF2",
                            edgecolor=BLUE_GRAY, linewidth=1.5)
    ax.add_patch(eco_bg)
    ax.text(9.0, 6.6, "ECONOMY", fontsize=11, ha="center",
            color=TEAL, fontfamily="Arial", fontweight="bold")
    ax.text(9.0, 6.25, "Ocean GDP and tourism", fontsize=8,
            ha="center", color=GRAY, fontfamily="Arial")

    box(ax, 8.0, 5.3, 2.2, 0.7, "OESA\nOcean GDP, GVA", BLUE_GRAY, fontsize=8)
    box(ax, 10.2, 5.3, 1.6, 0.7, "OTSA\nTourism", BLUE_GRAY, fontsize=8)

    # Bottom-left: PRESSURES
    prs_bg = FancyBboxPatch((0.5, 1.5), 5.0, 2.5,
                            boxstyle="round,pad=0.1", facecolor=LIGHT_ORANGE,
                            edgecolor=ORANGE, linewidth=1.5)
    ax.add_patch(prs_bg)
    ax.text(3.0, 3.7, "PRESSURES", fontsize=11, ha="center",
            color=TEAL, fontfamily="Arial", fontweight="bold")
    ax.text(3.0, 3.35, "What enters the ocean", fontsize=8,
            ha="center", color=GRAY, fontfamily="Arial")

    box(ax, 3.0, 2.4, 3.5, 0.7, "WASTE & EMISSIONS\nWater, solid waste, air", ORANGE, fontsize=8)

    # Bottom-right: SOCIETY
    soc_bg = FancyBboxPatch((6.5, 1.5), 5.0, 2.5,
                            boxstyle="round,pad=0.1", facecolor=LIGHT_TAN,
                            edgecolor=TAN, linewidth=1.5)
    ax.add_patch(soc_bg)
    ax.text(9.0, 3.7, "SOCIETY", fontsize=11, ha="center",
            color=TEAL, fontfamily="Arial", fontweight="bold")
    ax.text(9.0, 3.35, "Who benefits? Who is affected?", fontsize=8,
            ha="center", color=GRAY, fontfamily="Arial")

    box(ax, 9.0, 2.4, 3.5, 0.7, "SOCIAL & GOVERNANCE\nWellbeing, equity, access", TAN, WHITE, fontsize=8)

    # CENTER: BSU circle connecting all 4
    circle = plt.Circle((6, 4.4), 0.5, facecolor=GREEN, edgecolor=TEAL, linewidth=2)
    ax.add_patch(circle)
    ax.text(6, 4.4, "BSU\nSpatial\nData", fontsize=7, ha="center", va="center",
            color=WHITE, fontfamily="Arial", fontweight="bold")

    # Simple lines from BSU to each quadrant (no arrows, just connections)
    for (x, y) in [(3.0, 4.4), (9.0, 4.4), (3.0, 4.4), (9.0, 4.4)]:
        pass  # The colored backgrounds touching the center already show connection

    # Arrows from question to groups
    arrow_down(ax, 3.0, 7.15, 6.95, TEAL)
    arrow_down(ax, 9.0, 7.15, 6.95, BLUE_GRAY)

    # BOTTOM MESSAGE
    box(ax, 6, 0.6, 10, 0.6,
        "All connected through shared spatial data. Compile once, report to many policies.",
        TEAL, fontsize=10)

    save(fig, outdir / "diagram_triage.png")


def main():
    outdir = Path("/Users/mariaalarcon/GitHub/ocean-accounts-expert/s-s-event-bogor/sessions/day-2/clinic/diagrams")
    print("Generating clean diagrams...")
    diagram_overview(outdir)
    diagram_triage(outdir)

    # Copy to notebooks
    import shutil
    nb = Path("/Users/mariaalarcon/GitHub/ocean-accounts-expert/s-s-event-bogor/print-notebooks")
    d3 = Path("/Users/mariaalarcon/GitHub/ocean-accounts-expert/s-s-event-bogor/sessions/day-3/clinic-policy")

    shutil.copy(outdir / "diagram_overview.png", nb / "00-overview/02-overview-pipeline.png")
    shutil.copy(outdir / "diagram_triage.png", nb / "00-overview/01-triage-flowchart.png")
    shutil.copy(outdir / "diagram_overview.png", d3 / "diagram_overview.png")
    shutil.copy(outdir / "diagram_triage.png", d3 / "diagram_triage.png")
    print("Copied to notebooks and day-3")
    print("Done!")


if __name__ == "__main__":
    main()
