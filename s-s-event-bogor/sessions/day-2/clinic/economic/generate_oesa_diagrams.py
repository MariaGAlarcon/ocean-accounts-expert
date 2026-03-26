#!/usr/bin/env python3
"""Generate GOAP-styled pipeline diagram for OESA."""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
from pathlib import Path

TEAL = "#0A5455"
GREEN = "#3B9C7B"
MINT = "#D4EEE5"
BODY = "#30302F"
GRAY = "#717171"
WHITE = "#FFFFFF"
BLUE = "#66A3B5"
LIGHT_BLUE = "#B5D0D6"
TAN = "#B59F81"
LIGHT_TAN = "#F9F5F0"
ORANGE = "#E76F51"


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


def save_fig(fig, path):
    fig.savefig(str(path), dpi=200, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"  Created: {path}")


def diagram_oesa_pipeline(outdir):
    fig, ax = plt.subplots(figsize=(12, 8))
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 8)
    ax.axis("off")

    ax.text(6, 7.7, "OESA Compilation Pipeline", fontsize=18, ha="center",
            color=TEAL, fontfamily="Arial", fontweight="bold")
    ax.text(6, 7.3, "7 Steps: From National Accounts to Ocean Economy", fontsize=11,
            ha="center", color=GRAY, fontfamily="Arial")

    # Steps in two rows
    steps_top = [
        (1.5, 5.8, "1. DEFINE\nSCOPE", "Geographic +\neconomic boundaries", LIGHT_BLUE, BODY),
        (4.0, 5.8, "2. CLASSIFY\nACTIVITIES", "Map industries to\n6 ocean groups", LIGHT_BLUE, BODY),
        (6.5, 5.8, "3. SELECT\nFRAMEWORK", "Anchor to\nSupply-Use Tables", LIGHT_BLUE, BODY),
        (9.5, 5.8, "4. ESTIMATE\nPARTIALS", "Ocean share of\nmixed industries", TAN, WHITE),
    ]

    steps_bottom = [
        (2.5, 3.5, "5. COMPILE\nINDICATORS", "Output, IC, GVA\nEmployment", GREEN, WHITE),
        (6.0, 3.5, "6. DATA\nINTEGRATION", "Reconcile to SUT\nNo double counting", GREEN, WHITE),
        (9.5, 3.5, "7. VALIDATE\nRESULTS", "Compare benchmarks\nDocument assumptions", GREEN, WHITE),
    ]

    for x, y, title, desc, color, tc in steps_top:
        rounded_box(ax, x, y, 2.2, 1.0, title, color, tc, fontsize=9)
        ax.text(x, y - 0.7, desc, ha="center", va="center", fontsize=7,
                color=GRAY, fontfamily="Arial")

    for x, y, title, desc, color, tc in steps_bottom:
        rounded_box(ax, x, y, 2.2, 1.0, title, color, tc, fontsize=9)
        ax.text(x, y - 0.7, desc, ha="center", va="center", fontsize=7,
                color=GRAY, fontfamily="Arial")

    # Arrows top row
    arrow(ax, 2.7, 5.8, 2.8, 5.8, BLUE)
    arrow(ax, 5.2, 5.8, 5.3, 5.8, BLUE)
    arrow(ax, 7.7, 5.8, 8.3, 5.8, BLUE)

    # Arrow down from step 4 to step 5
    arrow(ax, 9.5, 5.0, 3.5, 4.05, GREEN)

    # Arrows bottom row
    arrow(ax, 3.7, 3.5, 4.8, 3.5, GREEN)
    arrow(ax, 7.2, 3.5, 8.3, 3.5, GREEN)

    # Output section
    rounded_box(ax, 6, 1.5, 9, 1.2,
                "OESA OUTPUT TABLES\n"
                "Gross Output | Intermediate Consumption | GVA | Employment\n"
                "by 6 ocean economy groups | Ocean GDP as % of national GDP",
                TEAL, WHITE, fontsize=9)
    arrow(ax, 9.5, 2.85, 8, 2.15, TEAL)

    # Sectors sidebar
    ax.text(0.3, 1.5, "6 Sectors:", fontsize=8, color=TEAL, fontfamily="Arial",
            fontweight="bold", va="center")
    sectors = ["Living\nresources", "Marine\nminerals", "Ship\nbuilding",
               "Marine\nconstruction", "Marine\ntransport", "Coastal\ntourism"]
    for i, s in enumerate(sectors):
        ax.text(0.3, 1.0 - i * 0.35, s, fontsize=6, color=BODY,
                fontfamily="Arial", va="center")

    save_fig(fig, outdir / "diagram_oesa_pipeline.png")


def diagram_oesa_vs_seea(outdir):
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 6)
    ax.axis("off")

    ax.text(6, 5.7, "OESA vs SEEA-EA: Two Sides of Ocean Accounts", fontsize=16,
            ha="center", color=TEAL, fontfamily="Arial", fontweight="bold")

    # Left: OESA
    rounded_box(ax, 3, 3.2, 4.8, 3.5, "", LIGHT_BLUE, BODY, fontsize=1)
    ax.text(3, 4.7, "Ocean Economy (OESA)", fontsize=13, ha="center",
            color=TEAL, fontfamily="Arial", fontweight="bold")
    oesa_items = [
        "Based on: SNA (national accounts)",
        "Measures: Market-based GDP contribution",
        "Key indicator: Gross Value Added",
        "Sectors: Fisheries, minerals, transport...",
        "Question: How big is the ocean economy?",
    ]
    for i, item in enumerate(oesa_items):
        ax.text(1.2, 4.1 - i * 0.45, item, fontsize=8, color=BODY,
                fontfamily="Arial", va="center")

    # Right: SEEA
    rounded_box(ax, 9, 3.2, 4.8, 3.5, "", MINT, BODY, fontsize=1)
    ax.text(9, 4.7, "Ecosystem Accounts (SEEA-EA)", fontsize=13, ha="center",
            color=TEAL, fontfamily="Arial", fontweight="bold")
    seea_items = [
        "Based on: SEEA (environmental accounting)",
        "Measures: Ecosystem health + non-market value",
        "Key indicator: Condition Index (0-1)",
        "Accounts: Extent, Condition, Services",
        "Question: How healthy is the ocean?",
    ]
    for i, item in enumerate(seea_items):
        ax.text(7.2, 4.1 - i * 0.45, item, fontsize=8, color=BODY,
                fontfamily="Arial", va="center")

    # Center arrows
    ax.annotate("", xy=(5.6, 3.2), xytext=(6.4, 3.2),
                arrowprops=dict(arrowstyle="<->", color=GREEN, lw=2))
    ax.text(6, 3.6, "complement\neach other", ha="center", va="center",
            fontsize=8, color=GREEN, fontfamily="Arial", fontweight="bold")

    # Bottom insight
    rounded_box(ax, 6, 0.7, 10, 0.8,
                "Together: OESA shows what the ocean contributes to the economy.\n"
                "SEEA-EA shows what the economy depends on from the ocean.",
                TEAL, WHITE, fontsize=9)

    save_fig(fig, outdir / "diagram_oesa_vs_seea.png")


if __name__ == "__main__":
    outdir = Path(__file__).parent
    print("Generating OESA diagrams...")
    diagram_oesa_pipeline(outdir)
    diagram_oesa_vs_seea(outdir)
    print("Done!")
