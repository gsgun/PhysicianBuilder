# Pattern: Composite Rule Composition

**When to use:** a clinical determination requires 2+ sub-conditions (e.g., SIRS = temp AND (WBC OR HR OR RR)).

## Canonical pattern

1. Build each sub-condition as its own CER (leaf rules).
2. Parent rule references children via **`Patient » Patient Rule Error Message a <> ""`** against the child rule id — true when the child fires.
3. Compose with the Criteria relationship string (explicit boolean expression).

### Example — SIRS inclusion (`CER 836523 IP Surgery PreOP SIRS`)

```
((1 or 2) and ((5 or 6 or 7) or 3 or 5))
or (3 and ((1 or 2) or 4 or (5 or 6 or 7)))
or (4 and ((1 or 2) or 3 or (5 or 6 or 7)))
or ((5 or 6 or 7) and ((1 or 2) or 3 or 4))
```

where 1/2 = temp >38.3 / <36, 3 = HR>90, 4 = RR>20, 5/6/7 = WBC <4 / >12 / bands.

Source: [gupta-surgery-risk-scores/untitled/cer/cer-836523-ip-surgery-preop-sirs/README.md](../../gupta-surgery-risk-scores/untitled/cer/cer-836523-ip-surgery-preop-sirs/README.md)

## Variant: flowsheet-populated composite (no sub-rules)

Parent reads FLO values directly when children would be trivial:

```
Patient » Flowsheet: Value <> "" a Flowsheet Row = R PH IP SUR PREOP RISK PNA POSTOP [15818]
  Return Type = Last Value; Encounters to Search = Current Encounter;
  Lookback Start = Arrival; Lookback End = Now; Data Type = Numeric
Criteria relationship: (1 or 2 or 3) and 4
```

row 4 = `Last Flowsheet Date` freshness guard (ensures the panel actually ran this encounter).

Source: [cer-836520-ip-sur-preop-risk-smartlist.md](../../gupta-surgery-risk-scores/untitled/cer/cer-836520-ip-sur-preop-risk-smartlist.md)

## Guardrails

- Always include a **freshness/completeness row** (last-flo-date, review-instant) so a stale prior-encounter value can't satisfy a current-encounter rule.
- Keep criteria relationships human-readable in the doc: map every row number to its clinical meaning (the SIRS README does this in the description field).
- Leaf rules should carry their own error message text — the parent's tip text inherits it (see [etx-composition](../smarttools/etx-composition.md)).
