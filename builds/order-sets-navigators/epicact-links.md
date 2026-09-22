# Pattern: EpicAct Link Catalog

**When to use:** deep-linking notes/tips to reports, navigators, or order entry.

## Syntax

```
epicact:<ACTION>,RunParams:<params>          (plain)
epicact:<ACTION>,RunParamsURLEncoded:<params> (URL-encoded)
```

Placeholders: `#PATIENTID#`, `#CONTACTDAT#`.

## Proven catalog

| Link | EpicAct | Source |
|---|---|---|
| Med Dispense Report | `AC_REPORT_VIEWER_FLOATING,RunParams:MR_REPORTS\|\|5^#PATIENTID#^4080000001^#CONTACTDAT#` | [admission-med-rec epicact](../../admission-med-rec-tip-text/admission-med-rec/epicact.md) |
| Med Rec Status PTA | `AC_REPORT_VIEWER_FLOATING,RunParams:MR_REPORTS\|\|5^#PATIENTID#^3040000021^#CONTACTDAT#` | id. |
| Admission PTA Med Rec (order entry, jump to review section) | `IP_ORDREC_ADMISSION_SPLITTER,RunParamsURLEncoded:TEMPLATE=IP_ORDREC_ADMISSION_TEMPLATE\|\|TOC=0\|\|STARTUPSECTION=IP_ORDREC_ADMISSION_SXS_REVIEW_SECTION` | id. |
| FLO popup (LQF-driven) | `ER_FLOWSHEET_POPUP,RunParams:LQFID=1366,CUSTOM=1` | [gupta epicact](../../gupta-surgery-risk-scores/untitled/epicact.md) |

## Rules

- Report-viewer links: `MR_REPORTS||5^#PATIENTID#^<reportId>^#CONTACTDAT#` — the only varying token is the report id.
- Non-modal report windows → `RunParams`; anything with `|` in free text → `RunParamsURLEncoded`.
- Keep one `epicact.md` per build folder; this catalog is the extraction layer.
