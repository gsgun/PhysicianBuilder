# Glossary

- **RWB** — Reporting Workbench; the Epic reporting source for ADT data.
- **Transfer (row)** — one row of the template export: a transfer whose
  **preceding** event was in an ICU unit (`From Unit` = that ICU). Produced by
  criterion 2006 ("Previous Event for the encounter") linked to item 50 (unit).
- **Eff Date Time** — the transfer's effective timestamp (the clock's start).
- **Disch Date/Time** — the same-encounter discharge timestamp (the clock's end).
- **Same-row model** — both timestamps live on one export row, so the metric is
  `delta = Disch − Eff` per row (no cross-event join).
- **Encounter (CSN)** — Epic contact serial number; with `Patient ID` it is the
  encounter key used for multi-transfer grouping.
- **Closest-to-discharge dedup** — within an encounter, keep the transfer with
  the smallest `delta` (tie-break: latest `eff_ts`); count the encounter once.
- **Window** — the max `delta` (default 24 h) for a transfer to count.
- **Statistical transfer** — the transfer definition the template uses
  (`Use statistical definition of transfer? = Yes`).
- **Intra-unit transfer** — a transfer whose from- and to-unit are the same
  unit; excluded by the template and re-checked in code.
- **PDT** — Pacific Daylight Time / America/Los_Angeles; the source time zone of
  the export, and the zone all comparisons are normalized to (DST-aware).
- **Clean (structural)** — parse timestamps (PDT), drop display-only columns
  (MRN/Name/rooms/beds/classes/services/DAT/Discharge Provider), drop rows with
  unparseable timestamps or `disch < eff`.
- **Reference implementation** — `src/metric.py` is authoritative; the SQL
  (`sql/02_24h_flag.sql`) is a projection and must agree with it.
