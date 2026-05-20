# Shielding Series Protocol

**Experiment Title**: Shielding Effectiveness Measurements with Am-241 (59.5 keV)

**Date**: 
**Experimenter**: 
**Location**: 

## Objective

Quantify the effectiveness of different shielding materials and thicknesses for attenuating 59.54 keV gamma rays from Am-241. Determine approximate half-value layer (HVL) for common materials (lead, aluminum, acrylic, etc.).

## Safety Checklist

- [ ] Background spectrum acquired
- [ ] Source handled with care / tongs
- [ ] Shielding materials inspected for integrity
- [ ] Measurement area clear of unnecessary personnel
- [ ] All metadata recorded

## Equipment

- Radiacode 103 spectrometer
- Am-241 sealed button source
- Shielding samples (Pb sheets of varying thickness, Al plates, acrylic, wood, etc.)
- Digital calipers or micrometer for thickness measurement
- Fixed-distance stand or holder (recommended: 10 cm or 20 cm)
- Notebook / metadata sheet

## Fixed Parameters

| Parameter            | Recommended Value     | Notes                              |
|----------------------|-----------------------|------------------------------------|
| Source-detector distance | 10 cm or 20 cm     | Keep constant across all runs     |
| Geometry             | On-axis, normal incidence | Record if changed                 |
| Live time            | 300 s                 | Adjust for statistics if needed   |
| Background           | Measure before/after series | Use average or session-specific  |

## Materials to Test (Examples)

- Lead (Pb): 0.5 mm, 1 mm, 2 mm, 3 mm
- Aluminum (Al): 2 mm, 5 mm, 10 mm
- Acrylic / PMMA: 5 mm, 10 mm, 20 mm
- Wood or plastic: various thicknesses
- Air (no shielding) as reference

## Procedure

1. Set up detector and source at fixed distance with **no shielding** first.
2. Acquire background spectrum (minimum 5 minutes).
3. Acquire reference spectrum (no shielding) for chosen live time.
4. Insert first shielding sample. Ensure good contact / no gaps.
5. Acquire shielded spectrum.
6. Record exact thickness (use calipers), material, and any notes (e.g., multiple layers).
7. Repeat for all shielding combinations.
8. Periodically re-measure background or no-shield reference.
9. When finished, safely store source.

## Data Recording

Use consistent naming:
`shielding_[material]_[thickness_mm]_[distance]cm_[date]_[time]`

Example filenames:
- `shielding_Pb_1mm_10cm_20260520_1430`
- `shielding_Al_5mm_10cm_20260520_1505`

Record in metadata:
- Material type and exact thickness (mm or g/cm²)
- Transmission = (shielded net CPS) / (unshielded net CPS)
- Calculated linear attenuation coefficient μ if desired

## Analysis Goals

- Plot transmission vs thickness for each material
- Estimate Half-Value Layer (HVL) where transmission = 0.5
- Compare experimental HVL to theoretical values for 59.5 keV
- Assess build-up effects or scatter contribution

## Observations

Note any unexpected behavior (e.g., fluorescence peaks from shielding, poor statistics at high attenuation, positioning sensitivity).

## Safety Notes Specific to Shielding

- Lead shielding: handle carefully, wash hands after use
- Ensure source is never left unshielded unnecessarily
- For very thick shielding, consider secondary radiation (e.g., Pb K X-rays ~75 keV)

---

**Protocol Version**: 1.0
**Created**: May 2026