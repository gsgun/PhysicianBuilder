# Transfer-identification mechanism (criterion 2006 → item 50)

This metric does **not** classify raw HL7 ADT codes — the Reporting Workbench
template `Modify ADT Transfers [Location]` (Report Model M24047, ID `[100432]`)
does that for us. This page records *how the template picks out "transfers out
of the ICU"* so the logic can be audited and re-implemented if the template
changes.

## The key criterion: 2006 "Previous Event for the encounter"
- **Type:** an **ADD** criterion. You select an item in the existing record,
  then it links back to a *different* item in the record.
- **Item 2006** = the record for the **previous event for this encounter**
  (the event immediately preceding the one on the current row).
- **Item 50** = the **unit** item. Linking 2006 → 50 pulls the unit of the
  *preceding* event onto the current row.
- **Filter:** `Unit (of previous event) ∈ {RBMC NT ICU, RBMC CV ICU}`.

## Result
The report returns rows where the **preceding** event's unit is an ICU unit ⇒
**every transfer FROM the ICU**. On such a row, `From Unit` = the ICU (that's
the unit the patient left), and `Eff Date Time` = the transfer's effective time.

## Why this is the right universe for the 24h question
"Discharges within 24h of transfer" is most meaningful for **out-of-ICU**
transfers (ICU → step-down/floor), which is exactly what the `Where Unit` +
criterion-2006→50 combination yields. Intra-unit moves are excluded by the
template (`Include intra-unit transfers? = No`), and statistical transfers are
included (`Use statistical definition of transfer? = Yes`).

> If the ask later broadens to *any* in-stay transfer (not just ICU), change
> the `From Unit` filter in the template — the Python/SQL here is unchanged
> (it reads `From Unit` / `Eff Date Time` / `Disch Date/Time` regardless).
