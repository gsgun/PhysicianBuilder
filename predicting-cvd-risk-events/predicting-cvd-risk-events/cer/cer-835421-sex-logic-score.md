---
description: Patient Context
---

# CER 835421 SEX LOGIC SCORE

IP CVDR SEX LOGIC SCORE \[835421] Context: Patient Score Rules \[34001] Returns: Numeric Build Details

Rule Rule criteria:

1. Patient » Reliably Determinable Patient Sex = 1 then result is 1
2. Patient » Reliably Determinable Patient Sex = 2 then result is 0
3. Constant » Always One = 1 then result is 3 Criteria relationship: First true line

