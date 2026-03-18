---
description: ASCVD30 Code.  Row Type Custom Formula Value Type Numeric Context Overtime
---

# FLO 16404 ASCVD30

```
M:x
p={15817;;0}
z=patID
v=patDAT
htn=+$$evalRule^elibHULIB22(835299,patID,v)
stn=+$$evalRule^elibHULIB22(835300,z,v)
age=+$$getMessage^S2LPP3(835308,,0,z,v)
sb=+$$getMessage^S2LPP3(835298,,0,z,v)
tc=+$zabs(+$$lastResultsFrComp^LRESULT("CHOL",1,1,z))
hd=+$zabs(+$$lastResultsFrComp^LRESULT("HDL",1,1,z))
dm1=+$$evalRule^elibHULIB22(835302,z,v)
dmc={15816;;3}
dm=$s(dmc=1:1,dmc=0:0,1:dm1)
sm1=+$$evalRule^elibHULIB22(835309,z,v)
smc={15841;;3}
sm=$s(smc=1:1,smc=0:0,1:sm1)
hx1=+$$getMessage^S2LPP3(835306,,0,z,v)
hx1=$s(hx1=1:0,1:1)
hxc={15832;;3}
hx=$s(hxc=1:0,hxc=0:1,1:hx1)
sex1=+$$evalRule^elibHULIB22(835421,z,v)
sexc={15815;;4}
sex=$s(sexc=1:1,sexc=2:0,sexc=3:3,1:sex1)
gf={15855;;0}
age2=$s((age>=30)&(age<=79):((age-55)/10),1:0)
age3=$s((age>=30)&(age<=79):age,1:0)
tc2=$s((tc>=130)&(tc<=320):((tc-hd)*0.02586)-3.5,1:0)
hd2=$s((hd>=20)&(hd<=100):((hd*0.02586)-1.3)/0.3,1:0)
sb2=$s((sb>=90)&(sb<=200):sb,1:0)
gf2=$s((gf>=15)&(gf<=150):gf,1:0)
minsb=$s(sb2<=110:(sb2-110)/20,1:0)
maxsb=$s(sb2>110:(sb2-130)/20,1:-1)
mingf=$s(gf2<=60:(gf2-60)/-15,1:0)
maxgf=$s(gf2>60:(gf2-90)/-15,1:2)
sum=$s(sex=1:(((age2*.4669202)-(.0893118*(age2**2))+(tc2*.1256901)-(hd2*.1542255)-(minsb*0.0018093)+(maxsb*0.322949)+(dm*0.6296707)+(sm*0.268292)+(mingf*0.100106)+(maxgf*0.0499663)+(htn*0.1875292)+(stn*0.0152476)-(maxsb*htn*0.0276123)+(tc2*stn*0.0736147)-(age2*tc2*0.0521962)+(age2*hd2*0.0316918)-(age2*maxsb*0.1046101)-(age2*dm*0.2727793)-(age2*sm*0.1530907)-(age2*mingf*0.1299149)-(1.974074))),sex=0:((age2*0.3994099)-(.0937484*(age2**2))+(tc2*0.1744643)-(hd2*0.120203)-(minsb*0.0665117)+(maxsb*0.2753037)+(dm*0.4790257)+(sm*0.1782635)-(mingf*0.0218789)+(maxgf*0.0602553)+(htn*0.1421182)+(stn*0.0135996)-(maxsb*htn*0.0218265)+(tc2*stn*0.1013148)-(age2*tc2*0.0312619)+(age2*hd2*0.020673)-(age2*maxsb*0.0920935)-(age2*dm*0.2159947)-(age2*sm*0.1548811)-(age2*mingf*0.0712547)-(1.736444)),1:0)
check=+$zabs((sex-3)*age3*tc2*hd2*sb2*gf2*hx)
x=$s(check>0:(2.71828**sum)/(1+(2.71828**sum))*100,1:0)
```
