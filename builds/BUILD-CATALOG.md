# Build Catalog — Deployed Builds & Component IDs

Cross-build inventory. Source of truth remains each build's GitBook folder; this is the lookup index.

| Build | Folder | FLO | CER (root) | ETX (root) | LQF |
|---|---|---|---|---|---|
| ASCVD/CVD 2024 Risk | [predicting-cvd-risk-events/](../predicting-cvd-risk-events/predicting-cvd-risk-events/README.md) | 15821 ASCVD10, 16404 ASCVD30, 15833 CVD10, 16403 CVD30, 15834 HF10, 15837 CHD10, 15835 CVA10, 15852 VALUES/HF, 15894/15909/15844/15881 *SIM, 15855 EGFR | 835299 HTN, 835300 STN, 835308 AGE, 835309 SMOKER, 835306 HxASCVD, 835421 SEX-LOGIC, 835298 SBP, 835302 DM, 835297 BMI | 23978 PARENT, 23932 OUTPUT TRUE, 24700 OUTPUT PARENT, 24418 SMARTLIST, 24348 CHARGE, 24015 TIP | LQF 1366-adj XML |
| Gupta NSQIP Risk | [gupta-surgery-risk-scores/](../gupta-surgery-risk-scores/untitled/README.md) | 16026 Cardiac PreOp, 16025 Respiratory PostOp, 15818 Pneumonia PostOp, 15902 Prior ASA | 836520 Smartlist, 836529 ASA, 836522 COPD, 836523 SIRS (leaves 835519/520/522/523/507/506/508; anchors 835933/835934) | 24725 PARENT (+HHS 101358), 24726 OUTPUT, 24626 TIP | 1366 (AfterLoaded ASA) |
| Admission Med Rec | [admission-med-rec-tip-text/](../admission-med-rec-tip-text/admission-med-rec/README.md) | — | 836339 Done+PTA, 836342 RN, 836361 PTech, 836362 Pharm, 836363 NotDone, 836344 PTA-Unrec, 836408 Parent | 24604 PARENT, 24605 REVIEW-STATUS TIP, 24606 UNREC-MEDS TIP | — |
| CathPCI GDMT | [cath-pci-gdmt/](../cath-pci-gdmt/cath-pci-gdmt/README.md) | — | 836339/836342/836344/836361/836362/836363/836408 (shared w/ Med Rec) | 24604/24605/24606 (shared w/ Med Rec) | — |
| PH Standard Notes | [standardnotes/ph-standard-notes/](../standardnotes/ph-standard-notes/README.md) | — | (SDE Name rule, service-abbrev 1360588) | 22718 PHIPNOTEHEADERHOSPITALIST + service tree | — |

**Shared-component notes**
- Admission Med Rec and CathPCI GDMT share the same CER/ETX id set — treat 8363xx/2460x as a **shared service**, not two builds.
- Search-period anchors 835933/835934 are the fleet's canonical admission-window pair (see [cer-rules/lab-value-rules.md](cer-rules/lab-value-rules.md)).
