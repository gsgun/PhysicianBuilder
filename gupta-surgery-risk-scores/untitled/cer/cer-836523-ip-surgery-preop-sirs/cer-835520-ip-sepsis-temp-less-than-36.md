---
description: Patient
---

# CER 835520 IP SEPSIS Temp < 36

Rule criteria:

1. Patient » Flowsheet: Value a < 96.8 a Flowsheet Row = TEMPERATURE \[6]; Return Type = Minimum Value \[10]; Encounters to Search = Current Encounter \[0]; Lookback Start = Arrival \[1]; Lookback End = Now \[3]; Data Type = Numeric \[2]
2. Patient » Flowsheet: Value a <> "" a Flowsheet Row = TEMPERATURE \[6]; Return Type = Minimum Value \[10]; Encounters to Search = Current Encounter \[0]; Lookback Start = Arrival \[1]; Lookback End = Now \[3]; Data Type = Numeric \[2] Criteria relationship: And Error message: " Temp: " Patient » Flowsheet: Value
