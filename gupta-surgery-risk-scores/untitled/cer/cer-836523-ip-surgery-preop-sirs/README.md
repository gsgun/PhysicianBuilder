---
description: Patient Context
---

# CER 836523 IP Surgery PreOP SIRS

Build Details

Rule criteria:

1. Patient » Patient Rule Error Message a <> "" a Patient Rule = IP SEPSIS Temp > 38.3 \[835519]
2. Patient » Patient Rule Error Message a <> "" a Patient Rule = IP SEPSIS Temp < 36 \[835520]
3. Patient » Patient Rule Error Message a <> "" a Patient Rule = IP SEPSIS HR > 90 \[835522]
4. Patient » Patient Rule Error Message a <> "" a Patient Rule = IP SEPSIS RR > 20 \[835523]
5. Patient » Patient Rule Error Message a <> "" a Patient Rule = IP SEPSIS WBC < 4 \[835507]
6. Patient » Patient Rule Error Message a <> "" a Patient Rule = IP SEPSIS WBC > 12 \[835506]
7. Patient » Patient Rule Error Message a <> "" a Patient Rule = IP SEPSIS Bands \[835508] Criteria relationship: ((1 or 2) and ((5 or 6 or 7) or 3 or 5)) or (3 and ((1 or 2) or 4 or (5 or 6 or 7))) or (4 and ((1 or 2) or 3 or (5 or 6 or 7))) or ((5 or 6 or 7) and ((1 or 2) or 3 or 4)) Error message: "SIRS True" Description SIRs Inclusion Rule
