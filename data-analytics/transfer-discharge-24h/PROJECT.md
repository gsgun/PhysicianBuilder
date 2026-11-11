# PROJECT: Discharges Within 24 Hours of Transfer

Requested by **Jaime Fair** (inpatient operations / throughput, Riverbend).
Owner: gunasekara. Lives in `PhysicianBuilder/data-analytics/transfer-discharge-24h/`.

## Question
How many inpatient discharges occur within 24 hours of a transfer — scoped to
**out-of-ICU transfers** (`RBMC NT ICU`, `RBMC CV ICU`), Riverbend, base class
Inpatient OR / Observation, effective period 11/10/2025 – 11/9/2026.

## Data source
RWB template **`Modify ADT Transfers [Location]`** (Model **M24047**, ID
**[100432]**), criteria recorded verbatim in `docs/template-config.md`. The
export carries `Eff Date Time` + `Disch Date/Time` on the same row → the 24h
clock is a same-row comparison. Confirmed: **PDT**, same-encounter discharge,
**closest-to-discharge dedup** per encounter.

## Deliverable shape (all built)
1. Metric definition + exclusions + dedup rule (`docs/metric-definition.md`).
2. Template config + criterion mechanism (`docs/template-config.md`,
   `docs/adt-event-taxonomy.md`).
3. Cleaner for the raw export, PDT-normalized (`src/clean.py`) — .xls/.xlsx/.csv.
4. Metric core, same-row + dedup, unit-tested (`src/metric.py`).
5. Pipeline: export → clean → counts + daily series (`src/pipeline.py`).
6. Jupyter notebook (`notebooks/run_metric.ipynb`) + Power BI/Jupyter guide (`GUIDE.md`).
7. Reference SQL projections (`sql/02_24h_flag.sql`, `sql/03_daily_rollup.sql`).

## Scope guard
Operations/throughput BI metric — not a CDS rule, no alerting. Deterministic
for a fixed config (`config/metric.yaml`).

## Definition of Done
- [x] Metric core + dedup implemented + unit-tested (16/16 green).
- [x] Template criteria + column schema recorded verbatim.
- [x] Cleaner handles the real export shape (.xls/.xlsx/.csv), PDT-normalized.
- [x] Notebook + Power BI/Jupyter guide.
- [ ] Real template export dropped into `data/` → first real-period run.
- [ ] Hand-counted sample (n≈15) reconciled against the output.
- [ ] Decide denominator: encounters (current) vs unique patients.
