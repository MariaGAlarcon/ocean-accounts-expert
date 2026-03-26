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

    # COMPILE ONCE banner
    box(ax, 7, 8.1, 5, 0.4, "COMPILE ONCE", GREEN, fontsize=12)

    # BSU FOUNDATION (wide bar under compile once)
    bsu = FancyBboxPatch((0.8, 7.1), 12.4, 0.55,
                         boxstyle="round,pad=0.05", facecolor=GREEN, edgecolor="none")
    ax.add_patch(bsu)
    ax.text(7, 7.38, "Shared Spatial Framework: Basic Spatial Units (BSUs)",
            fontsize=10, ha="center", color=WHITE, fontfamily="Arial", fontweight="bold")

    # THREE EQUAL DOMAIN COLUMNS
    col_w = 3.8
    col_h = 4.2
    col_y = 2.6
    gap = 0.3

    # Column 1: ENVIRONMENT (teal)
    c1_x = 0.9
    env = FancyBboxPatch((c1_x, col_y), col_w, col_h,
                         boxstyle="round,pad=0.1", facecolor=MINT,
                         edgecolor=TEAL, linewidth=1.5)
    ax.add_patch(env)
    ax.text(c1_x + col_w/2, col_y + col_h - 0.3, "ENVIRONMENT",
            fontsize=13, ha="center", color=TEAL, fontfamily="Arial", fontweight="bold")
    ax.text(c1_x + col_w/2, col_y + col_h - 0.65, "Ecosystems and their value",
            fontsize=8, ha="center", color=GRAY, fontfamily="Arial")

    # SEEA-EA components inside environment column
    box(ax, c1_x + col_w/2, col_y + 2.6, 3.2, 0.55, "EXTENT\nEcosystem area (ha)", TEAL, fontsize=8)
    box(ax, c1_x + col_w/2, col_y + 1.8, 3.2, 0.55, "CONDITION\nEcosystem health (CI 0-1)", TEAL, fontsize=8)
    box(ax, c1_x + col_w/2, col_y + 1.0, 3.2, 0.55, "SERVICES\nSupply + Use tables (SUT)", TEAL, fontsize=8)
    box(ax, c1_x + col_w/2, col_y + 0.25, 3.2, 0.4, "WASTE & EMISSIONS\nPollution flows to ocean", ORANGE, fontsize=7)

    # Arrows within environment column (vertical chain)
    arrow_down(ax, c1_x + col_w/2, col_y + 2.25, col_y + 2.15, TEAL)
    arrow_down(ax, c1_x + col_w/2, col_y + 1.45, col_y + 1.35, TEAL)

    # Column 2: ECONOMY (blue-gray)
    c2_x = c1_x + col_w + gap
    eco = FancyBboxPatch((c2_x, col_y), col_w, col_h,
                         boxstyle="round,pad=0.1", facecolor="#E8EEF2",
                         edgecolor=BLUE_GRAY, linewidth=1.5)
    ax.add_patch(eco)
    ax.text(c2_x + col_w/2, col_y + col_h - 0.3, "ECONOMY",
            fontsize=13, ha="center", color=TEAL, fontfamily="Arial", fontweight="bold")
    ax.text(c2_x + col_w/2, col_y + col_h - 0.65, "Ocean economic activity",
            fontsize=8, ha="center", color=GRAY, fontfamily="Arial")

    box(ax, c2_x + col_w/2, col_y + 2.6, 3.2, 0.55, "OCEAN ECONOMY (OESA)\nOcean GDP, GVA, employment", BLUE_GRAY, fontsize=8)
    box(ax, c2_x + col_w/2, col_y + 1.8, 3.2, 0.55, "OCEAN TOURISM (OTSA)\nCoastal tourism contribution", BLUE_GRAY, fontsize=8)

    ax.text(c2_x + col_w/2, col_y + 0.6, "Depends on ecosystem\nservices and condition",
            fontsize=8, ha="center", color=GRAY, fontfamily="Arial", style="italic")
    ax.text(c2_x + col_w/2, col_y + 0.15, "Generates waste and\npressures on ecosystems",
            fontsize=8, ha="center", color=ORANGE, fontfamily="Arial", style="italic")

    # Column 3: SOCIETY (tan)
    c3_x = c2_x + col_w + gap
    soc = FancyBboxPatch((c3_x, col_y), col_w, col_h,
                         boxstyle="round,pad=0.1", facecolor=LIGHT_TAN,
                         edgecolor=TAN, linewidth=1.5)
    ax.add_patch(soc)
    ax.text(c3_x + col_w/2, col_y + col_h - 0.3, "SOCIETY",
            fontsize=13, ha="center", color=TEAL, fontfamily="Arial", fontweight="bold")
    ax.text(c3_x + col_w/2, col_y + col_h - 0.65, "People and governance",
            fontsize=8, ha="center", color=GRAY, fontfamily="Arial")

    box(ax, c3_x + col_w/2, col_y + 2.6, 3.2, 0.55, "SOCIAL ACCOUNTS\nWellbeing, livelihoods, equity", TAN, fontsize=8)
    box(ax, c3_x + col_w/2, col_y + 1.8, 3.2, 0.55, "GOVERNANCE\nInstitutions, access, rights", TAN, fontsize=8)

    ax.text(c3_x + col_w/2, col_y + 0.6, "Enables and constrains\nboth environment and economy",
            fontsize=8, ha="center", color=GRAY, fontfamily="Arial", style="italic")

    # REPORT MANY banner
    box(ax, 7, 1.8, 5, 0.4, "REPORT MANY", ORANGE, fontsize=12)
    arrow_down(ax, 7, 2.55, 2.05, ORANGE)

    # Policy boxes
    policies = ["SDG 14", "NDC /\nNBSAP", "Marine spatial\nplanning",
                "Blue finance", "National ocean\npolicy"]
    for i, p in enumerate(policies):
        x = 1.5 + i * 2.8
        box(ax, x, 1.0, 2.3, 0.55, p, ORANGE, fontsize=8)

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
