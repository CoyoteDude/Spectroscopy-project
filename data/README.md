# Data Directory

This folder contains all experimental data and metadata.

## Structure

```
data/
├── raw/           # Original exports from Radiacode software (.spx, .csv, images, etc.)
├── processed/     # Background-subtracted, normalized, or analyzed data
├── metadata/      # JSON, CSV, or Markdown logs of experimental conditions
└── README.md
```

## File Naming Convention (Recommended)

`[experiment]_[variable]_[value]_[shield]_[YYYYMMDD]_[HHMM]`

Examples:
- `distance_5cm_noshield_20260520_1430`
- `shield_Pb_3mm_distance_10cm_20260520_1515`
- `geometry_45deg_20260521_0900`

## Metadata to Record

For every measurement, capture:
- Exact distance (cm)
- Geometry / angle
- Shielding material and thickness (or "none")
- Live time and real time
- Background file used for subtraction
- Temperature / environmental conditions
- Any notes on positioning or anomalies

## Data Dictionary

| Field              | Description                                      | Example          |
|--------------------|--------------------------------------------------|------------------|
| distance_cm       | Source-to-detector distance                      | 10.0             |
| shielding         | Material and thickness                           | Pb_2mm           |
| angle_deg         | Source angle relative to detector axis           | 0                |
| live_time_s       | Spectrometer live time                           | 300              |
| total_counts      | Gross counts in spectrum                         | 12450            |
| roi_counts        | Counts in region of interest (59.5 keV peak)     | 8720             |
| background_file   | Filename of background spectrum                  | bg_20260520_1400 |

## Best Practices

- Never modify raw files — work on copies in `processed/`
- Always include a background measurement for each session
- Use consistent units (cm, mm, seconds)
- Consider adding a simple CSV or JSON metadata file alongside spectra
- For large campaigns, consider scripting ingestion with Python

## Placeholder Files

Empty directories are preserved with `.gitkeep` files.