---
description: Patient Context
---

# CER 836520 IP Sur PreOp Risk Smartlist

Build Details

Rule criteria:

1. Patient » Flowsheet: Value a <> "" a Flowsheet Row = R PH IP SUR PREOP RISK PNA POSTOP \[15818]; Return Type = Last Value \[1]; Encounters to Search = Current Encounter \[0]; Lookback Start = Arrival \[1]; Lookback End = Now \[3]; Data Type = Numeric \[2]
2. Patient » Flowsheet: Value a <> "" a Flowsheet Row = R PH IP SUR PREOP RESPIRATORY POST OP \[16025]; Return Type = Last Value \[1]; Encounters to Search = Current Encounter \[0]; Lookback Start = Arrival \[1]; Lookback End = Now \[3]; Data Type = Numeric \[2]
3. Patient » Flowsheet: Value a <> "" a Flowsheet Row = R PH IP SUR PREOP RISK CARDIAC PREOP \[16026]; Return Type = Last Value \[1]; Encounters to Search = Current Encounter \[0]; Lookback Start = Arrival \[1]; Lookback End = Now \[3]; Data Type = Numeric \[2]
4. Patient » Last Flowsheet Date for Patient a = T a Flowsheet Row = R PH IP SUR PREOP RISK CARDIAC PREOP \[16026] Criteria relationship: (1 or 2 or 3) and 4 Error message: Patient » Last Flowsheet Date for Patient
