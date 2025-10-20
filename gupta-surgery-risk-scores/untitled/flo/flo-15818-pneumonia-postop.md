---
description: Custom Formula/String Type
---

# FLO 15818 Pneumonia PostOp

```
M:x
cpd=$$sumMultSelect^JCUSTFORM1({15994;;0})
asa=$$sumMultSelect^JCUSTFORM1({15988;;0})
fun=$$sumMultSelect^JCUSTFORM1({15989;;0})
smk=$$sumMultSelect^JCUSTFORM1({15992;;0})
sep=$$sumMultSelect^JCUSTFORM1({15890;;0})
typ=$$sumMultSelect^JCUSTFORM1({15993;;0})
age=+$$zCalcAge^%Zefnlii(+$h,$$getn^elibEAnLIB(""EPT"",patID,1,""100;1""))
age=age*0.0144
cpd1=$s(cpd=2:0,cpd=1:-.4553,1:0)
fun1=$s(fun=2:0.7653,fun=3:0.9400,fun=1:0,1:0)
asa1=$s(asa=1:-3.0225,asa=2:-1.6057,asa=3:-0.4915,asa=4:0.0123,asa=5:0,1:0)
sep1=$s(sep=1:0,sep=2:-0.0842,sep=3:0.1048,sep=4:-0.7641,1:0)
smk1=$s(smk=2:0,smk=1:-0.4306,1:0)
typ1=$s(typ=1:-0.8470,typ=2:0.7178,typ=3:-0.6282,typ=4:0.6841,typ=5:-2.3318,typ=6:0.1382,typ=7:-0.3665,typ=8:1.0660,typ=9:-0.3951,typ=10:0,typ=11:0.6169,typ=12:-0.0872,typ=13:-0.4101,typ=14:-0.5415,typ=15:0.4021,typ=16:-0.4519,typ=17:-0.5075,typ=18:-0.5672,typ=19:0.8901,typ=20:-1.4760,typ=21:0.1076,1:0)
sum=age+cpd1+fun1+asa1+sep1+smk1+typ1-2.8977
chk=cpd*asa*sep*smk*typ*fun
risk=((2.71828**sum)/(1+(2.71828**sum)))*100
risk=$normalize(risk,2)
x=$s(chk=0:null,1:risk)
```
