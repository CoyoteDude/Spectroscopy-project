#!/usr/bin/env python3
"""
plot_count_rate_vs_distance.py

Basic starter script for analyzing radiation detection experiments
with Am-241 and Radiacode 103.

Features:
- Simulated example data (easy to replace with real measurements)
- Background subtraction
- Net count rate calculation
- Plotting: linear and log-log count rate vs distance
- Simple inverse square law fitting
- Shielding transmission example

Usage:
    python plot_count_rate_vs_distance.py

Requirements:
    pip install numpy pandas matplotlib scipy
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# ============================================================
# EXAMPLE DATA (Replace with your real measurements)
# ============================================================

# Simulated data for demonstration (no shielding)
data = {
    "distance_cm": [5, 10, 15, 20, 30, 40, 50],
    "gross_counts": [45200, 11800, 5400, 3100, 1450, 820, 530],
    "live_time_s": [300] * 7,
    "background_cps": 0.8,   # average background count rate
}

df = pd.DataFrame(data)
df["gross_cps"] = df["gross_counts"] / df["live_time_s"]
df["net_cps"] = df["gross_cps"] - df["background_cps"]

print("Example DataFrame:")
print(df)

# ============================================================
# ANALYSIS FUNCTIONS
# ============================================================

def inverse_square(x, a):
    """Simple inverse square model: cps = a / x^2"""
    return a / (x ** 2)

def fit_inverse_square(distance, net_cps):
    """Fit inverse square model to data."""
    popt, pcov = curve_fit(inverse_square, distance, net_cps, p0=[net_cps[0] * distance[0]**2])
    return popt[0]

# ============================================================
# PLOTTING
# ============================================================

def plot_results(df, fit_a=None):
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))

    # Linear scale
    ax1 = axes[0]
    ax1.plot(df["distance_cm"], df["net_cps"], "o-", label="Measured net CPS", markersize=8)
    if fit_a is not None:
        x_fit = np.linspace(df["distance_cm"].min(), df["distance_cm"].max(), 200)
        ax1.plot(x_fit, inverse_square(x_fit, fit_a), "--", label=f"Inverse square fit (a={fit_a:.1f})")
    ax1.set_xlabel("Distance (cm)")
    ax1.set_ylabel("Net Count Rate (cps)")
    ax1.set_title("Count Rate vs Distance (Linear)")
    ax1.legend()
    ax1.grid(True, alpha=0.3)

    # Log-log scale
    ax2 = axes[1]
    ax2.loglog(df["distance_cm"], df["net_cps"], "o-", label="Measured net CPS", markersize=8)
    if fit_a is not None:
        x_fit = np.linspace(df["distance_cm"].min(), df["distance_cm"].max(), 200)
        ax2.loglog(x_fit, inverse_square(x_fit, fit_a), "--", label="Inverse square fit")
    ax2.set_xlabel("Distance (cm)")
    ax2.set_ylabel("Net Count Rate (cps)")
    ax2.set_title("Count Rate vs Distance (Log-Log)")
    ax2.legend()
    ax2.grid(True, alpha=0.3, which="both")

    plt.tight_layout()
    plt.savefig("count_rate_vs_distance.png", dpi=300, bbox_inches="tight")
    print("Plot saved as count_rate_vs_distance.png")
    plt.show()


# ============================================================
# MAIN
# ============================================================

if __name__ == "__main__":
    # Fit inverse square model
    fit_a = fit_inverse_square(df["distance_cm"].values, df["net_cps"].values)
    print(f"\nFitted constant a = {fit_a:.2f} (for model: cps = a / r²)")

    # Generate plots
    plot_results(df, fit_a=fit_a)

    print("\nAnalysis complete. Replace the example data with your real measurements.")
    print("Tip: Export your Radiacode data to CSV and load with pd.read_csv()")