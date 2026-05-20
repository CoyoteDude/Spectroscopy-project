# Spectroscopy Project

**Radiation Detection Experiments with Radiacode 103 and Am-241 Source**

Experimental investigation of gamma radiation detection efficiency, count rates, and spectral characteristics as functions of source-detector distance, geometry, and shielding.

**Repository Status**: Active development — initial structure and documentation.

## Overview

This repository documents systematic experiments using the **Radiacode 103** portable gamma spectrometer and a sealed **Am-241** button source (primarily the 59.54 keV gamma emission). The goal is to quantify how detection performance changes with:

- Source-to-detector distance
- Source-detector geometry / orientation
- Shielding materials and thicknesses (lead, aluminum, plastic, concrete, etc.)
- Collimation and scattering effects

These measurements provide practical insights into radiation detection principles, inverse square law validation, shielding effectiveness, and real-world spectrometer performance.

## Objectives

- Measure count rate vs. distance and compare to theoretical expectations (inverse square law + air attenuation)
- Characterize spectral changes (photopeak position, Compton continuum, escape peaks) with distance and shielding
- Evaluate shielding effectiveness of common materials for 59.5 keV gammas
- Assess geometry effects (point source vs. extended, angle dependence)
- Develop reproducible protocols and data analysis workflows
- Generate high-quality educational data and visualizations

## Safety Considerations

> **Important**: This experiment uses a sealed radioactive source (Am-241). Always follow ALARA principles (As Low As Reasonably Achievable).

- Handle the Am-241 button only with appropriate tools or tongs when necessary
- Maintain maximum practical distance during measurements
- Use shielding when appropriate
- Do not ingest, inhale, or bring the source near the body for extended periods
- Follow all local regulations and institutional radiation safety guidelines
- Record background measurements before and after each session
- Never attempt to open or modify the sealed source

This repository focuses on **educational and scientific documentation**. All procedures emphasize safety and responsible practices.

## Experimental Setup

### Equipment
- Radiacode 103 gamma spectrometer (with appropriate software/app for data export)
- Sealed Am-241 button source
- Measuring tape / ruler for precise distances
- Shielding materials (Pb sheets, Al, acrylic, wood, etc.)
- Stands, holders, or optical rail for reproducible geometry
- Notebook or digital logging for metadata

### Key Variables
- Distance (cm)
- Angle / orientation
- Shielding type and thickness (mm or g/cm²)
- Measurement live time / real time
- Background subtraction

## Methods & Protocols

Detailed step-by-step protocols are maintained in the `/protocols/` directory.

A general workflow:

1. Perform background measurement in the experimental location
2. Position source and detector at defined distance/geometry
3. Acquire spectrum for fixed live time
4. Record metadata (distance, shielding, temperature, etc.)
5. Export spectrum/data from Radiacode software
6. Process and analyze (count rate in ROI, spectral features)
7. Repeat for systematic variations

See `protocols/experiment-template.md` for a reusable template.

## Data Management

Data is organized under `/data/`:

- `raw/` — Original exported files from the spectrometer
- `processed/` — Cleaned, background-subtracted, or analyzed data
- `metadata/` — JSON/CSV logs of experimental conditions

A data dictionary and notes are in `data/README.md`.

**Recommendation**: Use consistent naming (e.g., `distance_10cm_shield_Pb_2mm_YYYYMMDD_HHMM.spx` or similar) and always record full metadata.

## Analysis & Visualization

Analysis scripts and notebooks live in `/analysis/`.

Planned / suggested analyses:
- Count rate vs. distance plots (linear and log scales)
- Validation of inverse square law
- Photopeak efficiency vs. distance/shielding
- Spectral overlay comparisons
- Shielding half-value layer (HVL) estimation for Am-241

Python (pandas, matplotlib, scipy) or Jupyter notebooks are recommended. Example starter scripts will be added.

## Repository Structure

```
Spectroscopy-project/
├── README.md
├── LICENSE
├── .gitignore
├── protocols/
│   ├── experiment-template.md
│   └── ...
├── data/
│   ├── raw/
│   ├── processed/
│   └── README.md
├── analysis/
│   └── README.md
├── references/
│   └── README.md
└── assets/          # Images, spectra screenshots, diagrams
```

## Getting Started

1. Clone the repository
2. Review the README and safety notes
3. Explore `/protocols/` for experiment templates
4. Add your measurement data to `/data/raw/`
5. Document new protocols or analysis in the appropriate folders

## Future Directions

- Add Jupyter notebooks for automated analysis and plotting
- Include example spectra and processed datasets
- Develop simple interactive visualization (possible Streamlit or Observable)
- Expand to other sources or detector types
- Integrate with broader radiation education resources

## Contributing

This is currently a personal experimental documentation project, but contributions, suggestions, or forks are welcome. Open an issue or pull request for:
- Protocol improvements
- Analysis code
- Additional shielding materials or geometries
- Documentation enhancements

## License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

Educational and scientific use is encouraged. When sharing or adapting, please provide appropriate attribution.

## References & Resources

- Radiacode 103 documentation and software
- Am-241 decay data (59.54 keV gamma, ~35.9% yield)
- Radiation detection textbooks (e.g., Knoll, *Radiation Detection and Measurement*)
- Inverse square law and shielding principles

---

*Repository initialized May 2026. Actively expanding with experimental data and analysis.*