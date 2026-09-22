# RFC-001: ED Discharge Navigator Access for WE-Rule Discharges to SNF

**Status:** draft
**Author:** gsgun (via clinical-informatics workbench)
**Source:** [to-do/discharge-navigator-for-ed-we-rule.md](../../to-do/discharge-navigator-for-ed-we-rule.md)

## 1. Clinical Rationale
Emergency-Department Work-Queue (WE) patients discharged to **SNF** cannot access the Discharge Navigator. Current workaround: hospitalist is consulted purely to place orders — a throughput and handoff-integrity gap (discharge orders bypass the standardized navigator path).

## 2. Problem Statement
The ED WE rule's order-availability scope excludes the Discharge Navigator. This forces a consult round-trip for a task the ED team should own, and loses the navigator's standardized discharge-order integrity (meds, follow-up, transport).

## 3. Proposed Change
Extend the ED WE rule's available orders to include the Discharge Navigator for **SNF discharges only** (not home, not acute).

## 4. Technical Bounds
- **Component type:** ED WE rule order-scope configuration (no new CER/ETX/FLO).
- **Scope guard:** SNF destination only. Home-discharge and acute-transfer paths must remain unchanged.
- **Validation surface:** order availability per destination; no rule-evaluation change (no SmartList/CER impact expected).

## 5. Validation Matrix (synthetic)
| Case | Patient | Expected |
|---|---|---|
| SNF discharge, ED WE rule | MRN 999000101, TEST-DOE, JOHN, Encounter Day 2 | Discharge Navigator available in ED WE |
| Home discharge, ED WE rule | MRN 999000102 | Discharge Navigator **not** available (unchanged) |
| Acute transfer, ED WE rule | MRN 999000103 | Discharge Navigator **not** available (unchanged) |
| Non-ED inpatient | MRN 999000104 | Discharge Navigator available per existing inpatient path (unchanged) |

## 6. Governance & DoD
- [ ] Confirm the WE rule's order-scope mechanism with the ED informatics / charge-nurse workflow owner (mentorship-questions open item).
- [ ] Staging validation of the 4-case matrix with synthetic patients.
- [ ] P&T / Governance sign-off before production.
- **DoD:** SNF discharges from ED WE reach the Discharge Navigator with no consult round-trip; all 4 matrix cases pass; no regression on home/acute paths.

## 7. Open Questions
- Is the SNF destination determined at order time (destination field) or only at transport? The scope guard depends on this.
- Should the navigator's discharge orders inherit ED-specific overrides, or the standard inpatient set?

## 8. References
- [to-do/discharge-navigator-for-ed-we-rule.md](../../to-do/discharge-navigator-for-ed-we-rule.md)
- [to-do/hospital-course-gold-star.md](../../to-do/hospital-course-gold-star.md) (discharge/transition-of-care adjacency)
