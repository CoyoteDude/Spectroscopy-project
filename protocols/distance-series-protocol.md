# Distance Series Protocol

**Experiment Title**: Systematic Count Rate vs Distance Measurements (Am-241 + Radiacode 103)

**Date**: 
**Experimenter**: 
**Location**: 

## Objective

Measure how net count rate and spectral features change with source-to-detector distance. Validate inverse square law behavior and quantify air attenuation effects for 59.54 keV gammas.

## Safety Checklist

- [ ] Background measurement performed in the exact experimental location
- [ ] Source handled safely (tongs or remote positioning preferred)
- [ ] Clear path between source and detector (no accidental shielding)
- [ ] All distances measured accurately with tape or ruler
- [ ] Live time chosen for good statistics at largest distance

## Equipment

- Radiacode 103 spectrometer
- Am-241 sealed button source
- Non-conductive stand or optical rail for reproducible positioning
- Measuring tape / digital caliper
- Notebook or digital form for metadata

## Recommended Parameters

| Parameter              | Suggested Value          | Rationale                              |
|------------------------|--------------------------|----------------------------------------|
| Distance range         | 5 cm – 100 cm            | Covers strong signal to low statistics |
| Distance steps         | 5 cm (near), 10 cm (far) | Good resolution near source            |
| Live time per point    | 300 s                    | Balance between time and statistics    |
| Geometry               | On-axis, source facing detector | Minimize angular effects            |
| Background             | Measure at start + end   | Average or use session-specific        |

## Procedure

1. Choose a low-background location and mark the detector position.
2. Acquire a background spectrum (minimum 5–10 min).
3. Place the Am-241 source at the first (closest) distance.
4. Acquire spectrum for the chosen live time.
5. Record exact distance, live/real time, temperature, and any notes.
6. Move source to next distance (use marks or rail for reproducibility).
7. Repeat acquisition for all distances.
8. At the end, re-acquire background to check stability.
9. Safely store the source.

## Data Naming Convention

`distance_[XX]cm_[live]s_[YYYYMMDD]_[HHMM]`

Examples:
- `distance_10cm_300s_20260520_1420`
- `distance_50cm_300s_20260520_1605`

## Metadata to Record

- Exact distance (cm) from source center to detector face
- Live time and real time
- Background file used
- Any observed anomalies (vibration, temperature drift, source positioning difficulty)

## Analysis Recommendations

- Use `compute_roi_count_rate()` from `analysis/radiacode_parser.py` with ROI ≈ (58, 62) keV
- Plot net CPS vs distance (linear and log-log scales)
- Fit inverse square law: CPS = a / r²
- Check for deviations at very short or very long distances
- Compare photopeak position and width across distances (scattering effects)

## Expected Behavior

- Strong inverse square dependence at short distances
- Slight additional attenuation from air at longer distances
- Possible increase in Compton continuum relative to photopeak at larger distances

## Variations to Consider Later

- Different source orientations
- With/without light shielding
- Collimated vs open geometry

---

**Protocol Version**: 1.0
**Created**: May 2026