# GUIDE — Run the metric yourself: Power BI vs Jupyter

Everything below assumes you are in `PhysicianBuilder/data-analytics/transfer-discharge-24h/`.

## What you gave me (locked in)
- **Timezone:** PDT (America/Los_Angeles — UTC−8 winter / −7 summer; DST applies)
- **Disch Date/Time:** same encounter as the transfer
- **Multi-transfer rule:** when a patient has more than one out-of-ICU transfer
  on a stay, keep **the transfer closest to discharge** (tie-break: latest).
- **Tooling:** you're used to Power BI; open to Jupyter. Both paths are built.

## Path A — Power BI (your usual flow)
1. Run the RWB template (`Modify ADT Transfers [Location]`, M24047 [100432]),
   export .xls → save into `data/` (gitignored).
2. Power BI: **Get Data → Excel** → `data/<your_export>.xls`.
3. Recreate the metric measure using the logic in `sql/02_24h_flag.sql`
   (`delta = Disch − Eff`; keep `0 ≤ delta ≤ 24`; dedup to closest-to-discharge).
4. Optional: load `output/by_day.csv` as a second query for the daily trend.

## Path B — Jupyter (the built path)
```bash
cd ~/workspace/PhysicianBuilder/data-analytics/transfer-discharge-24h
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
jupyter lab
```
Open `notebooks/run_metric.ipynb`, run top-to-bottom. It calls the same
`src/metric.py` core as the CLI, so numbers cannot diverge from the verified path.

## Shared components
| layer | file | role |
|------|------|------|
| Core logic | `src/metric.py` | `0 ≤ Disch−Eff ≤ 24h`; closest-to-discharge dedup; by_day |
| Cleaning | `src/clean.py` | .xls/.xlsx/.csv → `transfer_events.csv`; drops display cols; PDT-normalized |
| Notebook | `notebooks/run_metric.ipynb` | interactive run, filter, chart, iterate with Jaime |
| SQL projection | `sql/02_24h_flag.sql` | same-row flag + headline, mirrors the core |
| Tests | `tests/test_metric.py` | guards the dedup + window rules (must stay green) |
| Config | `config/metric.yaml` | window, units, PDT zone, dedup rule |

## Guardrail
The Python core is authoritative; Power BI/DAX and the notebook are projections
of it. If a number differs, reconcile to `src/metric.py` and fix the projection.
