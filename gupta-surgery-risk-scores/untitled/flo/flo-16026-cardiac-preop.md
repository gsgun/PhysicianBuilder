---
description: Custom Formula/String Type
---

# FLO 16026 Cardiac PreOp

```
M:x
asa=$$sumMultSelect^JCUSTFORM1({15988;;0})
fun=$$sumMultSelect^JCUSTFORM1({15989;;0})
typ=$$sumMultSelect^JCUSTFORM1({15993;;0})
cre=+$zabs(+$$lastResultsFrComp^LRESULT("CREAT",1,1,patID))
age=+$$zCalcAge^%Zefnlii(+$h,$$getn^elibEAnLIB(""EPT"",patID,1,""100;1""))
age=age*0.02
fun1=$s(fun=2:0.65,fun=3:1.03,fun=1:0,1:0)
asa1=$s(asa=2:-3.29,asa=3:-1.92,asa=4:-0.95,asa=5:0,asa=1:-5.17,1:0)
cre1=$s(cre=0:-.1,cre>1.5:.61,1:0)
typ1=$s(typ=1:-.16,typ=2:1.6,typ=3:-.25,typ=4:1.40,typ=5:-1.61,typ=6:1.01,typ=7:.71,typ=8:1.39,typ=9:.59,typ=10:0,typ=11:1.14,typ=12:.18,typ=13:.76,typ=14:.80,typ=15:1.13,typ=16:.86,typ=17:.54,typ=18:.21,typ=19:.40,typ=20:-1.09,typ=21:-.26,1:0)
sum=age+fun1+asa1+cre1+typ1-5.25
risk=((2.71828**sum)/(1+(2.71828**sum)))*100
risk=$normalize(risk,2)
chk=fun*typ*asa
x=$s(chk=0:null,1:risk)
```
