# ROADMAP: Discharges Within 24 Hours of Transfer

## Phase 0 — Seed (done)
- [x] Metric core (same-row model), cleaner, pipeline, tests
- [x] Closest-to-discharge dedup + PDT normalization (16/16 tests green)
- [x] Jupyter notebook + Power BI/Jupyter guide

## Phase 1 — Wire RWB (done 2026-11-11)
- [x] Template `Modify ADT Transfers [Location]` (M24047 [100432]) captured verbatim
- [x] Criteria: statistical transfer=Yes, base class Inpatient OR/Obs,
      only-transfer-in=Yes, intra-unit=No, Riverbend, 11/10/2025–11/9/2026
- [x] ICU filter mechanism: criterion 2006 (Previous Event) → item 50 (unit)
- [x] Export column schema (19 columns) recorded
- [x] Confirmed: timezone PDT, same-encounter discharge, dedup=closest-to-discharge

## Phase 2 — Validate (next)
- [ ] Run the template export for the period → `data/`
- [ ] `python3 -m src.pipeline --input data/<export> ...` → first real run
- [ ] Hand-count n≈15 rows; reconcile against `output/summary.json`
- [ ] Decide denominator: encounters (current) vs unique patients

## Phase 3 — Rollout
- [ ] Commit the period's `summary.json` + `by_day.csv` as the baseline
- [ ] Refresh cadence agreed with Jaime Fair
- [ ] Optional: dashboard card (count + rate + trend)
