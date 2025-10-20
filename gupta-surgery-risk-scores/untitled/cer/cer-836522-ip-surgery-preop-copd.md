---
description: Patient Context
---

# CER 836522 IP Surgery PreOp COPD

Build Details

Rule criteria:

1. Patient » Last Flowsheet Value for Patient a < 75 a Flowsheet Row = R PH CC FEV1 %PRED \[15032]
2. Patient » Last Flowsheet Date for Patient a <> "" a Flowsheet Row = R PH CC FEV1 %PRED \[15032] Criteria relationship: And Error message: "FEV1 (Less than 75%): " Patient » Last Flowsheet Value for Patient "(" Patient » Last Flowsheet Date for Patient ")" Description FEV1 < 75%
