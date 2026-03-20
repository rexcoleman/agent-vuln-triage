#!/usr/bin/env python3
"""Generate FP-19 report figures from experiment results."""
import json
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

INPUT_DIR = Path("outputs/experiments")
OUT_DIRS = [Path("blog/images"), Path("outputs/figures")]

def ensure_dirs():
    for d in OUT_DIRS:
        d.mkdir(parents=True, exist_ok=True)

def save(fig, name):
    for d in OUT_DIRS:
        fig.savefig(d / f"{name}.png", dpi=150, bbox_inches="tight")
    print(f"  Saved: {name}.png")

def fig_e1():
    with open(INPUT_DIR / "e1_results.json") as f:
        data = json.load(f)["results"]
    methods = ["agent", "epss", "cvss", "random"]
    labels = ["LLM Agent", "EPSS", "CVSS", "Random"]
    colors = ["#2563eb", "#16a34a", "#ea580c", "#9ca3af"]
    means, stds = [], []
    for m in methods:
        vals = [data[s][m]["p10"] for s in data]
        means.append(np.mean(vals))
        stds.append(np.std(vals))
    fig, ax = plt.subplots(figsize=(8, 5))
    bars = ax.bar(labels, [m*100 for m in means], yerr=[s*100 for s in stds],
                  capsize=5, color=colors, alpha=0.8)
    ax.set_ylabel("Precision@10 (%)")
    ax.set_title("Vulnerability Triage: Agent vs Baselines\n(CISA KEV ground truth, 5 seeds)")
    ax.set_ylim(0, 115)
    for bar, mean in zip(bars, means):
        ax.text(bar.get_x() + bar.get_width()/2., bar.get_height() + 2,
                f"{mean*100:.0f}%", ha="center", va="bottom", fontweight="bold")
    ax.grid(axis="y", alpha=0.3)
    save(fig, "e1_precision_comparison")
    plt.close()

def fig_e2():
    with open(INPUT_DIR / "e2_results.json") as f:
        data = json.load(f)["results"]
    levels = ["minimal", "exploit", "full"]
    labels = ["CVE Only", "+ Exploit DB", "+ Vendor Advisory"]
    colors = ["#9ca3af", "#2563eb", "#16a34a"]
    means = [data[l]["p10_mean"]*100 for l in levels]
    stds = [data[l]["p10_std"]*100 for l in levels]
    fig, ax = plt.subplots(figsize=(7, 5))
    bars = ax.bar(labels, means, yerr=stds, capsize=5, color=colors, alpha=0.8)
    ax.set_ylabel("Precision@10 (%)")
    ax.set_title("Effect of Enrichment Data on Agent Triage\n(5 seeds)")
    ax.set_ylim(0, 115)
    for bar, mean in zip(bars, means):
        ax.text(bar.get_x() + bar.get_width()/2., bar.get_height() + 2,
                f"{mean:.0f}%", ha="center", va="bottom", fontweight="bold")
    ax.grid(axis="y", alpha=0.3)
    save(fig, "e2_enrichment_ablation")
    plt.close()

def main():
    ensure_dirs()
    print("Generating FP-19 figures...")
    fig_e1()
    fig_e2()
    print("Done.")

if __name__ == "__main__":
    main()
