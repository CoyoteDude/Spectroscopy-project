# Analysis Directory

This folder is for data processing, visualization, and statistical analysis scripts.

## Recommended Tools

- Python 3 + pandas, numpy, matplotlib, scipy
- Jupyter notebooks for interactive exploration
- Optional: lmfit or scipy for peak fitting on spectra

## Suggested Workflow

1. Load raw or processed spectrum data
2. Perform background subtraction
3. Define ROI around the 59.54 keV Am-241 photopeak
4. Calculate net count rate
5. Plot count rate vs. distance (linear + log-log)
6. Fit models (inverse square + exponential attenuation)
7. Compare shielding transmission

## Example Script Ideas (to be added)

- `load_spectrum.py` — parser for Radiacode export formats
- `plot_distance_curve.py` — generate publication-quality figures
- `shielding_analysis.py` — calculate half-value layer (HVL)
- `spectral_comparison.ipynb` — overlay multiple spectra

## Current Status

Starter scripts and example notebooks will be added as experiments progress.

If you have existing analysis code from previous measurements, feel free to contribute it here.