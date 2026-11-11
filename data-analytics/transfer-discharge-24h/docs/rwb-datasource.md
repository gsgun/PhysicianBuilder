# RWB Datasource — status

Status: **wired** (requester supplied the template, column schema, timezone,
discharge scope and dedup rule on 2026-11-11).

## Confirmed
| item | value |
|------|-------|
| Template | `Modify ADT Transfers [Location]`, Report Model `M24047`, ID `[100432]` |
| Period | effective `11/10/2025` → `11/9/2026` |
| Statistical transfer | Yes |
| Base class | Inpatient OR / Observation |
| Only transfer in | Yes |
| Intra-unit transfers | No |
| Revenue location | RIVERBEND MEDICAL CENTER |
| ICU filter (Where) | `Unit ∈ {RBMC NT ICU, RBMC CV ICU}` via criterion 2006 (Previous Event for encounter) → item 50 |
| Transfer time column | `Eff Date Time` |
| Discharge time column | `Disch Date/Time` — **same encounter** |
| Patient keys | `Patient ID`, `CSN` (CSN = encounter key) |
| Units | `From Unit` (ICU), `To Unit` (destination) |
| Timezone | **PDT** (America/Los_Angeles) |
| Export format | `.xls` (pipeline also accepts `.xlsx`/`.csv`) |
| Multi-transfer rule | keep the transfer **closest to discharge** per encounter |

## Remaining decision (not a data unknown)
- **Denominator:** count **encounters** (current) vs **unique patients**. If a
  patient has two admissions in the period they currently count twice. Say the
  word and I'll switch to unique-patient dedup (one-line change).

## Data handling / PHI
- The raw export (with `MRN`, `Name`, etc.) lives under `data/` (gitignored).
- The cleaned `transfer_events.csv` carries only `Patient ID` / `CSN` / units /
  timestamps — still PHI-adjacent, also gitignored (`output/`).
- Fixtures use synthetic IDs. No PHI is ever committed.
