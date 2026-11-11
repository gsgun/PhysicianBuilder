# Template Configuration — "Modify ADT Transfers [Location]"

The transfer universe for this metric is produced by an existing Reporting
Workbench template, **not** by hand-rolled SQL. This page records the template
verbatim so the build is reproducible. Source: requester (gunasekara), 2026-11-11.

## Template
- **Template name:** `Modify ADT Transfers [Location]`
- **Report Model:** `M24047`
- **Model / criteria ID:** `[100432]`
- **Limits:** maxed out (raise the row limit so the full event set exports).

## Default criteria (verbatim)
| Criterion | Value |
|-----------|-------|
| From — Effective date from | `11/10/2025` |
| Effective date to | `11/9/2026` |
| Use statistical definition of transfer? | Yes |
| Reporting base class | Inpatient OR / Observation |
| Only transfer in? | Yes |
| Include intra-unit transfers? | No |
| Revenue location | RIVERBEND MEDICAL CENTER |

## Where clause (the ICU filter)
```
Where
  Unit: RBMC NT ICU OR RBMC CV ICU
```
**Mechanism:** implemented with criterion **2006 = "Previous Event for the
encounter"** (an *ADD* criterion — it selects an item in the existing record
and links back to a different item), linked to **item 50** (the unit item).
Effect: the report returns every transfer record whose **preceding event was in
an ICU unit** — i.e., **all transfers OUT of the ICU**.

So a returned row = *"a patient was transferred from {RBMC NT ICU, RBMC CV
ICU}"*, and the `From Unit` column on that row is the ICU.

## Export column schema (verbatim, per requester)
| Column | Meaning |
|--------|---------|
| MRN | Patient's medical record number |
| CSN | Patient's contact serial number |
| Name | Patient name (Lastname, Firstname) |
| Attending | Attending provider |
| From Unit | Unit the patient was transferred **from** |
| From Room | Room transferred from |
| From Bed | Bed transferred from |
| From Class | Class abbreviation transferred from |
| From Service | Hospital service abbreviation (from) |
| To Unit | Unit the patient was transferred **to** |
| To Room | Room transferred to |
| To Bed | Bed transferred to |
| To Class | Class abbreviation transferred to |
| To Service | Hospital service abbreviation (to) |
| **Eff Date Time** | The event's effective date/time (the transfer) |
| **Disch Date/Time** | The patient's discharge date and time |
| Patient ID | Internal patient ID for the ADT event |
| DAT | Patient DAT for the ADT event |
| Discharge Provider | Discharge provider name + ID in brackets |

> **Time zone:** PDT (America/Los_Angeles), DST-aware — confirmed by requester.
> The metric normalizes every timestamp to this zone before comparing.

## What the metric consumes
- **Transfer (row key):** `Patient ID`, `CSN`, `Eff Date Time`, `From Unit`, `To Unit`
- **Discharge (same row):** `Disch Date/Time`
- **Dropped (PHI-adjacent / not needed):** `MRN`, `Name`, `Attending`, room/bed/
  class/service, `DAT`, `Discharge Provider`
