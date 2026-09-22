# Pattern: ADT / Event-Driven Rules

**When to use:** "this hasn't happened yet" alerts (med rec not done, order not cancelled) — state checks against C_ADT / C_IEV event objects rather than lab/lab-value lookback.

## Canonical form — Admission Med Rec (CER 836339)

```
Logic: AND
1. C_IEV Patient CSN = Current Admission Contact Serial Number        (scoping to this admission)
2. C_Event Type = IP ADMISSION RECONCILIATION [35000]                 (event exists)
3. C_IP Rec Summary - Needed Reconciliation = Yes [1]
4. C_IP Rec Summary - Was Reconciled = No [0]
5. C_IP Rec Summary - Order ID » C_Cancellation Status ≠ Cancellation Done [2]
Return Message: ... Medications » C_Generic Name » Title
```

Source: [admission-med-rec-tip-text/admission-med-rec/cer/cer-836339.md](../../admission-med-rec-tip-text/admission-med-rec/cer/cer-836339.md)

## Design points

- **Row 1 is the scoping row** — always bind event rows to the current CSN, otherwise prior-encounter events leak in.
- **Return Message as data channel:** the rule returns a list (generic medication names) consumed by ETX tip text. Rules that *report* should return content, not just a boolean.
- **Role-split child rules:** complete-status is decomposed per role (Pharmacist `836362`, Pharmacy Tech `836361`, RN `836342`), then OR-composed in a `Review Not Done` parent — keeps per-role behavior independent.

## Known bug class (lesson)

BPA/rules fired on **location only, not patient class** (HF ED BPA, ticket #3112568) → fix pattern: add a patient-class/user-property restriction row to the parent.

Source: [to-do/heart-failure-ed-bug.md](../../to-do/heart-failure-ed-bug.md)
