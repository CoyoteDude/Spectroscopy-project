#!/usr/bin/env python3
"""
Radiacode Parser Module

Functions to load and process spectra exported from the Radiacode 103 app.

Supported formats (extend as needed):
- CSV with columns: Energy (keV), Counts (or similar)
- Simple two-column text/CSV (energy, counts)
- JSON exports if available from the app

Usage:
    from analysis.radiacode_parser import load_radiacode_spectrum, compute_roi_count_rate

    energy, counts, metadata = load_radiacode_spectrum('my_spectrum.csv')
    net_cps = compute_roi_count_rate(energy, counts, roi=(58, 62), live_time=300)
"""

import numpy as np
import pandas as pd
from pathlib import Path
from typing import Tuple, Dict, Optional, Union


def load_radiacode_spectrum(
    filepath: Union[str, Path],
    energy_col: str = "Energy",
    counts_col: str = "Counts",
    skiprows: int = 0,
    **kwargs
) -> Tuple[np.ndarray, np.ndarray, Dict]:
    """
    Load a Radiacode spectrum from CSV or text file.

    Parameters
    ----------
    filepath : str or Path
        Path to the exported spectrum file.
    energy_col : str
        Name of the energy column (default: 'Energy').
    counts_col : str
        Name of the counts column (default: 'Counts').
    skiprows : int
        Number of header rows to skip.
    **kwargs
        Additional arguments passed to pandas.read_csv().

    Returns
    -------
    energy : np.ndarray
        Energy bins in keV.
    counts : np.ndarray
        Counts per bin.
    metadata : dict
        Any available metadata (filename, total counts, etc.).
    """
    filepath = Path(filepath)
    if not filepath.exists():
        raise FileNotFoundError(f"File not found: {filepath}")

    # Try reading as CSV first
    try:
        df = pd.read_csv(filepath, skiprows=skiprows, **kwargs)
    except Exception:
        # Fallback: try space or tab separated
        df = pd.read_csv(filepath, sep=None, engine="python", skiprows=skiprows, **kwargs)

    # Auto-detect columns if exact names not found
    cols = [c.lower() for c in df.columns]
    if energy_col.lower() not in cols and "energy" in cols:
        energy_col = [c for c in df.columns if "energy" in c.lower()][0]
    if counts_col.lower() not in cols and "count" in cols:
        counts_col = [c for c in df.columns if "count" in c.lower()][0]

    energy = df[energy_col].values.astype(float)
    counts = df[counts_col].values.astype(float)

    metadata = {
        "filename": filepath.name,
        "total_counts": int(counts.sum()),
        "max_energy_keV": float(energy.max()),
        "n_bins": len(energy),
    }

    return energy, counts, metadata


def compute_roi_count_rate(
    energy: np.ndarray,
    counts: np.ndarray,
    roi: Tuple[float, float] = (58.0, 62.0),
    live_time: Optional[float] = None,
    background_cps: float = 0.0,
) -> float:
    """
    Compute net count rate in a region of interest (ROI).

    Parameters
    ----------
    energy : np.ndarray
    counts : np.ndarray
    roi : tuple (low, high) in keV
    live_time : float or None
        If provided, returns counts per second.
    background_cps : float
        Background count rate to subtract.

    Returns
    -------
    net_cps : float
        Net count rate in the ROI (or total net counts if live_time is None).
    """
    mask = (energy >= roi[0]) & (energy <= roi[1])
    roi_counts = counts[mask].sum()

    if live_time and live_time > 0:
        gross_cps = roi_counts / live_time
        net_cps = gross_cps - background_cps
        return max(net_cps, 0.0)
    else:
        return roi_counts


def simple_peak_search(
    energy: np.ndarray,
    counts: np.ndarray,
    prominence: float = 10,
    width: int = 3,
) -> Tuple[np.ndarray, np.ndarray]:
    """
    Simple peak finder using scipy.
    Returns peak energies and heights.
    """
    from scipy.signal import find_peaks

    peaks, properties = find_peaks(counts, prominence=prominence, width=width)
    peak_energies = energy[peaks]
    peak_heights = counts[peaks]
    return peak_energies, peak_heights


if __name__ == "__main__":
    print("Radiacode parser module loaded successfully.")
    print("Use load_radiacode_spectrum() and compute_roi_count_rate().")