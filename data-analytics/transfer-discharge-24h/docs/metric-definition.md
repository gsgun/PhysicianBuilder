# Metric Definition — Discharges Within 24 Hours of Transfer

**Version:** 0.3 (template-driven, same-row, dedup + PDT) · **Requested by:** Jaime Fair
· **Owner:** gunasekara · **Facility:** Riverbend Medical Center

## 1. Question
> How many inpatient discharges occur within 24 hours of a transfer?

Scoped to **out-of-ICU transfers** (from `RBMC NT ICU` or `RBMC CV ICU`),
Riverbend, base class Inpatient OR / Observation, period **11/10/2025 –
11/9/2026** (the template's effective window).

## 2. Precise definition
The template export yields **one row per out-of-ICU transfer**, each carrying
both `Eff Date Time` (transfer) and `Disch Date/Time` (the **same encounter's**
discharge) on the same row.

For each row, compute (in **PDT / America/Los_Angeles**):
```
delta = Disch Date/Time − Eff Date Time
```
A row qualifies if `0 <= delta <= 24 hours`.

### Multi-transfer rule (requester-confirmed)
A patient can have several out-of-ICU transfers in one encounter
(e.g. ICU → floor → ICU → floor). Group rows by **encounter (Patient ID + CSN)**
and keep the **transfer closest to discharge** (minimum delta; tie-break latest
`eff_ts`). Count each **encounter** once. `dedup_rule` is configurable
(`closest_to_discharge` default, `count_all`, `earliest`).

### Headline outputs
- `encounters_total` — distinct encounters (Patient ID + CSN) in the period
- `discharges_within_window` — encounters with a closest qualifying transfer
  where `0 <= delta <= 24h`
- `rate` — `discharges_within_window / encounters_total`
- daily series keyed on discharge date

## 3. Exclusions & edge rules
| rule | where | default |
|------|-------|---------|
| Transfers not from the two ICU units | template + clean + metric (safety) | excluded |
| Intra-unit (same-unit) transfers | template (`Include intra-unit? = No`) + metric | excluded |
| `Disch Date/Time` earlier than `Eff Date Time` | clean + metric | excluded |
| `delta > 24h` | metric | excluded |
| `delta` exactly 24h | metric | **included** (boundary inclusive) |
| Missing/unparseable timestamp | clean | dropped (reported) |
| Time zone | clean | **PDT** (America/Los_Angeles), DST-aware — confirmed |

## 4. Reproducibility
Deterministic for a fixed `config/metric.yaml` + the template criteria above.
The template config is recorded verbatim in `docs/template-config.md`; the
Python core (`src/metric.py`) is the reference and the SQL
(`sql/02_24h_flag.sql`) is a projection of it — on disagreement the core wins.

## 5. Open questions
1. ~~Time zone~~ — **PDT (America/Los_Angeles)** confirmed.
2. ~~`Disch Date/Time` scope~~ — **same encounter** confirmed.
3. ~~Multiple transfers per encounter~~ — **keep closest to discharge** confirmed.
4. **Denominator intent** — current build counts **encounters** (Patient ID + CSN).
   If Jaime wants **unique patients** instead (a patient with two admissions
   could appear twice), that is a one-line change (dedup on `patient_id`).

## 6. Verification plan
1. Run the template export for the period → `data/`.
2. `python3 -m src.pipeline --input data/<export> --config config/metric.yaml --out output/`
3. Hand-count a 15-row sample; reconcile against `output/summary.json`.
4. Commit the period's `output/summary.json` + `by_day.csv` as the first real run.
