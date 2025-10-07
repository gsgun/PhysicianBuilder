---
description: EGFR SOGI. Row Type Custom Formula Value Type Numeric Context Overtime
---

# FLO 15855 EGFR

```
// M:x
p={15817;;0}
sex1=+$$evalRule^elibHULIB22(835421,patID,patDAT)
sexc={15815;;4}
sex=$s(sexc=1:1,sexc=2:0,sexc=3:3,1:sex1)
age=+$$zCalcAge^%Zefnlii(+$h,$$getn^elibEAnLIB(""EPT"",patID,1,""100;1""))
cr=+$zabs(+$$lastResultsFrComp^LRESULT("CREAT",1,1,patID))
gf=$s((sex=1)&(cr'=0):142*($s(cr>=0.7:1,1:cr/.7)**(-0.241))*($s(cr<0.7:1,1:cr/.7)**(-1.2))*(0.9938**age)*1.012,(sex=0)&(cr'=0):142*($s(cr>=0.9:1,1:cr/.9)**(-0.302))*($s(cr<0.9:1,1:cr/.9)**(-1.2))*(0.9938**age),1:0)
x=$s(age>=18:gf,1:0)
```
