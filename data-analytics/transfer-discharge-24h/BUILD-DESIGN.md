# BUILD-DESIGN: Discharges Within 24 Hours of Transfer

## 1. Metric

**Name:** `dch_within_24h_of_transfer` · **Requested by:** Jaime Fair · **Site:** Riverbend

**Definition:** the Reporting Workbench template `Modify ADT Transfers
[Location]` (Model M24047, ID `[100432]`) yields **one row per out-of-ICU
transfer**, each carrying `Eff Date Time` (transfer) and `Disch Date/Time`
(same-encounter discharge) on the **same row**. The metric is:

```
delta = Disch Date/Time − Eff Date Time          (PDT / America/Los_Angeles)
count an ENCOUNTER once if it has a transfer with 0 <= delta <= 24 h,
using the transfer CLOSEST to discharge (multi-transfer rule)
```

| output | meaning |
|--------|---------|
| `total_rows` | export rows after structural clean |
| `encounters_total` | distinct encounters (Patient ID + CSN) |
| `transfers_qualifying` | rows passing the window before dedup |
| `discharges_within_window` | encounters with a qualifying transfer after dedup (headline) |
| `rate` | within / encounters |
| `by_day` | daily `(encounters, within, rate)` keyed on discharge date |

## 2. Data model (what the code consumes)

### Raw (template export) — one row per transfer
```
MRN, CSN, Name, Attending,
From Unit, From Room, From Bed, From Class, From Service,
To Unit, To Room, To Bed, To Class, To Service,
Eff Date Time, Disch Date/Time, Patient ID, DAT, Discharge Provider
```
The ICU filter (`From Unit ∈ {RBMC NT ICU, RBMC CV ICU}`) is enforced **inside
the template** via criterion **2006 (Previous Event for the encounter) → item
50 (unit)** — see `docs/adt-event-taxonomy.md` and `docs/template-config.md`.

### Cleaned (`src/clean.py` → `transfer_events.csv`)
```
patient_id, csn, visit_id, from_unit, to_unit, eff_ts, disch_ts, delta_hours
```
Clean = parse both timestamps (naive wall-clock assumed PDT; aware values
converted to America/Los_Angeles), drop `MRN/Name/Attending/room/bed/class/
service/DAT/Discharge Provider`, drop rows with missing/unparseable timestamps
or `disch < eff`, and (optionally) pre-trim to the window. **`visit_id =
PatientID|CSN`** = the encounter key (Epic contact serial); a row with no CSN
falls back to `PatientID|<eff>`.

## 3. Pipeline
```
data/<export>.xls|.csv  (raw template export; gitignored)
   │  src/clean.py  — structural clean (parse + PDT, drop display cols, ICU re-check)
   ▼
output/transfer_events.csv
   │  src/metric.py — window + closest-to-discharge dedup + counts/by_day
   ▼
output/summary.json · matches.csv · by_day.csv
```
Run: `python3 -m src.pipeline --input data/<export> --config config/metric.yaml --out output/`
Notebook: `notebooks/run_metric.ipynb` (same core; interactive).

## 4. Qualification + dedup rules (single source: `src/metric.py`)
Qualification per row:
1. `disch_ts >= eff_ts`
2. `delta >= min_delta_hours` (default 0)
3. `delta <= window_hours` (default 24)
4. not same-unit (`from_unit != to_unit` when `exclude_same_location`)
5. `from_unit ∈ cfg.from_units` (safety re-check of the template's ICU filter)

Dedup per encounter (requester rule):
6. group by `visit_id`; keep the **transfer closest to discharge** (min delta;
   tie-break latest `eff_ts`); count the encounter once.
   `dedup_rule` options: `closest_to_discharge` (default), `count_all`, `earliest`.

SQL (`sql/02_24h_flag.sql`) mirrors these line-for-line (ROW_NUMBER on the
encounter partition). **On disagreement the Python core wins.**

## 5. Tunables (`config/metric.yaml`)
`window_hours` (24), `min_delta_hours` (0), `dedup_rule`
(`closest_to_discharge`), `timezone` (`America/Los_Angeles`), `from_units`
(two ICUs), `exclude_same_location` (true), `max_back_date_hours` (null).

## 6. Open items
`docs/metric-definition.md §5` — remaining question: whether the headline
should be **encounters** (current) or **unique patients** (a patient with two
admissions could appear twice). Everything else (timezone, same-encounter
discharge, dedup grain) is confirmed.

## 7. Files
| file | role |
|------|------|
| `GUIDE.md` | Power BI vs Jupyter run guide |
| `docs/template-config.md` | the RWB template, verbatim (criteria + Where + columns) |
| `docs/adt-event-taxonomy.md` | criterion 2006→50 mechanism |
| `docs/metric-definition.md` | authoritative spec + exclusions + open questions |
| `docs/rwb-datasource.md` | confirmed slots + remaining `[FROM RWB …]` items |
| `src/clean.py` | raw export → cleaned rows (structural + PDT) |
| `src/metric.py` | window + dedup logic (reference, unit-tested) |
| `src/pipeline.py` | CLI: export → clean → metric → outputs |
| `notebooks/run_metric.ipynb` | interactive run/chart |
| `sql/01_template_m24047.sql` | the template as a documented "query" |
| `sql/02_24h_flag.sql` | same-row 24h flag + headline (reference projection) |
| `sql/03_daily_rollup.sql` | daily series |
| `tests/` | stdlib unittest; fixture = synthetic template-style export |
