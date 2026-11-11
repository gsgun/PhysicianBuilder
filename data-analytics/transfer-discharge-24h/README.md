# Discharges Within 24 Hours of Transfer

Inpatient operational metric: **how many discharges occur within 24 hours of an
out-of-ICU transfer**. Requested by **Jaime Fair** (Riverbend).

## How it works
The Reporting Workbench template **`Modify ADT Transfers [Location]`**
(Report Model **M24047**, ID **[100432]**) yields one row per transfer out of
`RBMC NT ICU` / `RBMC CV ICU`, each row carrying both the transfer time
(`Eff Date Time`) and the same-encounter discharge time (`Disch Date/Time`).
The 24h clock is a **same-row comparison** (PDT):

```
delta = Disch Date/Time − Eff Date Time    count if 0 <= delta <= 24 h
```

**Multi-transfer rule:** group by encounter (Patient ID + CSN) and keep the
transfer **closest to discharge**; count each encounter once.

The ICU filter lives **inside the template** (criterion 2006 "Previous Event
for the encounter" → item 50 = unit). See `docs/template-config.md`.

## Pipeline
```
data/<template export>.xls|.csv   (raw; gitignored)
  → src/clean.py      structural clean (parse+PDT, drop display cols, ICU re-check)
  → src/metric.py     window + closest-to-discharge dedup + counts/by_day
  → output/summary.json · matches.csv · by_day.csv
```

## Run it
- **Notebook:** `notebooks/run_metric.ipynb` (interactive; same core).
- **CLI:** `python3 -m src.pipeline --input data/<export> --config config/metric.yaml --out output/`
- **Power BI / Jupyter guide:** `GUIDE.md`.

## Quick test
```
python3 -m unittest discover -s tests -v
python3 -m src.pipeline --input tests/fixtures/sample_transfer_events.csv --config config/metric.yaml --out output/
```

## Status
🏗 Build complete and verified on synthetic data (16/16 tests green; dedup +
PDT + notebook all exercised). **Next: drop the real `.xls` export into `data/`
and produce the first real-period number.** Remaining decision: count
encounters (current) vs unique patients (`docs/metric-definition.md §5`).

## Docs
- `GUIDE.md` — Power BI vs Jupyter run guide
- `docs/template-config.md` — the RWB template, verbatim
- `docs/adt-event-taxonomy.md` — criterion 2006→50 mechanism (transfers out of ICU)
- `docs/metric-definition.md` — spec, exclusions, dedup rule, open questions
- `docs/rwb-datasource.md` — confirmed datasource slots
- `BUILD-DESIGN.md` — architecture
