# Pattern: Lab Value Rules + Search Period Filters

**When to use:** a rule threshold on a lab (WBC > 12, Temp bands) that must respect an admission-anchored lookback window.

## Canonical form

```
Patient » Lab Stats Value a > 12
  a Base Names = WBC; Common Names = WBC;
  Search Period Filter Rule = PH IP Admission (ED Arrival Date T-1) [835933];
  Unit = K/uL; Include Null Unit? = No;
  Statistic = Maximum; Include Unsuccessful Attempts? = No
Error message: " WBC (K/uL): " Patient » Lab Stats Value
```

Source: [cer-835506-ip-sepsis-wbc-greater-than-12/README.md](../../gupta-surgery-risk-scores/untitled/cer/cer-836523-ip-surgery-preop-sirs/cer-835506-ip-sepsis-wbc-greater-than-12/README.md)

## Search Period Filter rules (the reusable part)

Recurring anchor pair, defined once and referenced by every lab rule:

| Anchor rule | Definition | Use |
|---|---|---|
| `PH IP Admission (Encounter Date) [835934]` | encounter admission date | default anchor |
| `PH IP Admission (ED Arrival Date T-1) [835933]` | `Earliest Date Rule = 835934; Earliest Data Source = Use Default from External Data Manager [20]; Relative Earliest Date = y/m/d-1` | captures ED labs drawn before formal IP admission |

Source: [cer-835933-ph-ip-admission-ed-arrival-date-t-1.md](../../gupta-surgery-risk-scores/untitled/cer/cer-836523-ip-surgery-preop-sirs/cer-835506-ip-sepsis-wbc-greater-than-12/cer-835933-ph-ip-admission-ed-arrival-date-t-1.md)

**Reuse rule:** never re-implement the window inline in a lab rule — reference the shared filter rule so a window change is one edit.

## Checkpoints

- `Statistic` = Maximum/Minimum must match the clinical intent (WBC <4 needs Minimum; WBC >12 needs Maximum).
- Pin `Unit` + `Include Null Unit? = No` — unit drift silently breaks thresholds.
- Error message should be human-readable tip text, not a criteria dump.
