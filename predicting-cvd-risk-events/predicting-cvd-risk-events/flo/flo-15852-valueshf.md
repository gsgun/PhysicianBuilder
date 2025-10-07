---
description: ValuesHF Row Type Custom Formula Value Type String Context Overtime
---

# FLO 15852 VALUESHF

```
//M:x
p={15817;;0}
bm=$$getMessage^S2LPP3(835297,,0,patID,patDAT)
bm2=$s((bm>=18.5)&(bm<40):bm,1:0)
hf10={15834;;2}
x=$s((hf10=0)&(bm2=0):"Does not meet criteria for 10 year Heart Failure due to: BMI "_bm,1:" ")
```
