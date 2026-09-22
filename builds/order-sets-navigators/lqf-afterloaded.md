# Pattern: LQF AfterLoaded Logic

**When to use:** smartform that pre-populates from a flowsheet row / another data source instead of N hand-rolled rules.

## Canonical example — Surgery PreOp ASA (LQF 1366)

- Form: `Surgery Operative Risk Score`, bound to flowsheet template `647 PH T IP SUR PREOP RISK`.
- **AfterLoaded** step reads the Prior ASA flowsheet row (from Anesthesia Pre-Procedure evaluation) and sets the ASA list choice.

Trade-off (as documented in the build): *easier than one rule per ASA value*; cost is **group-template bloat**.

Source: [gupta-surgery-risk-scores/untitled/lqf-1366/logic.md](../../gupta-surgery-risk-scores/untitled/lqf-1366/logic.md), XML: [lqf-1366/xml.md](../../gupta-surgery-risk-scores/untitled/lqf-1366/xml.md)

## Pairing

An LQF popup is launched from a tip via `epicact:ER_FLOWSHEET_POPUP,RunParams:LQFID=<id>,CUSTOM=1` — see [epicact-links](epicact-links.md).

## Checklist

- AfterLoaded must be idempotent (re-opened forms must not clobber user edits).
- Smartform list choices map to a ListCUI (e.g. `15988` for ASA) — keep CUI ids in the build doc.
- Formula rows that consume the smartform use `$$sumMultSelect^JCUSTFORM1({<row>;;0})` — see [flo-formulas](../smarttools/flo-formulas.md).
