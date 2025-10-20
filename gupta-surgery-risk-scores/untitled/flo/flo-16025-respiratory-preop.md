---
description: Custom Formula/String Type
---

# FLO 16025 Respiratory PreOp

```
M:x
asa=$$sumMultSelect^JCUSTFORM1({15988;;0})
emr=$$sumMultSelect^JCUSTFORM1({15995;;0})
fun=$$sumMultSelect^JCUSTFORM1({15989;;0})
sep=$$sumMultSelect^JCUSTFORM1({15890;;0})
typ=$$sumMultSelect^JCUSTFORM1({15993;;0})
fun1=$s(fun=2:0.7678,fun=3:1.4046,fun=1:0,1:0)
asa1=$s(asa=2:-2.0008,asa=3:-0.6201,asa=4:0.2441,asa=5:0,asa=1:-3.5265,1:0)
sep1=$s(sep=1:0,sep=2:0.2752,sep=3:0.9035,sep=4:-.784,1:0)
emr1=$s(emr=2:0,emr=1:-.5739,1:0)
typ1=$s(typ=1:-1.353,typ=2:1.0781,typ=3:-1.0112,typ=4:0.7336,typ=5:-2.6462,typ=6:0.2744,typ=7:.106,typ=8:.9694,typ=9:-.5668,typ=10:0,typ=11:.5737,typ=12:-.5271,typ=13:-1.2431,typ=14:-.8577,typ=15:.2416,typ=16:-.2389,typ=17:-.3206,typ=18:-.5220,typ=19:.6715,typ=20:-2.0080,typ=21:.3093,1:0)
sum=fun1+asa1+sep1+emr1+typ1-1.7397
chk=fun*asa*sep*emr*typ
risk=((2.71828**sum)/(1+(2.71828**sum)))*100
risk=$normalize(risk,2)
x=$s(chk=0:null,1:risk)
```
