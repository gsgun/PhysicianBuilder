---
description: ASCVD10 Code.  Row Type Custom Formula Value Type Numeric Context Overtime
---

# FLO 15821 ASCVD10

```
M:x
p={15817;;0}
htn=+$$evalRule^elibHULIB22(835299,patID,patDAT)
stn=+$$evalRule^elibHULIB22(835300,patID,patDAT)
age=+$$getMessage^S2LPP3(835308,,0,patID,patDAT)
sb=+$$getMessage^S2LPP3(835298,,0,patID,patDAT)
tc=+$zabs(+$$lastResultsFrComp^LRESULT("CHOL",1,1,patID))
hd=+$zabs(+$$lastResultsFrComp^LRESULT("HDL",1,1,patID))
dm1=+$$evalRule^elibHULIB22(835302,patID,patDAT)
dmc={15816;;3}
dm=$s(dmc=1:1,dmc=0:0,1:dm1)
sm1=+$$evalRule^elibHULIB22(835309,patID,patDAT)
smc={15841;;3}
sm=$s(smc=1:1,smc=0:0,1:sm1)
hx1=+$$getMessage^S2LPP3(835306,,0,patID,patDAT)
hx1=$s(hx1=1:0,1:1)
hxc={15832;;3}
hx=$s(hxc=1:0,hxc=0:1,1:hx1)
sex1=+$$evalRule^elibHULIB22(835421,patID,patDAT)
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
sum=$s(sex=1:(((age2*0.719883)+(tc2*0.1176967)-(hd2*0.151185)-(minsb*0.0835358)+(maxsb*0.3592852)+(dm*0.8348585)+(sm*0.4831078)+(mingf*0.4864619)+(maxgf*0.0397779)+(htn*0.2265309)-(stn*0.0592374)-(maxsb*htn*0.0395762)+(tc2*stn*0.0844423)-(age2*tc2*0.0567839)+(age2*hd2*0.0325692)-(age2*maxsb*0.1035985)-(age2*dm*0.2417542)-(age2*sm*0.0791142)-(age2*mingf*0.1671492)-(3.819975))),sex=0:((age2*0.7099847)+(tc2*0.1658663)-(hd2*0.1144285)-(minsb*0.2837212)+(maxsb*0.3239977)+(dm*0.7189597)+(sm*0.3956973)+(mingf*0.3690075)+(maxgf*0.0203619)+(htn*0.2036522)-(stn*0.0865581)-(maxsb*htn*0.0322916)+(tc2*stn*0.114563)-(age2*tc2*0.0300005)+(age2*hd2*0.0232747)-(age2*maxsb*0.0927024)-(age2*dm*0.2018525)-(age2*sm*0.0970527)-(age2*mingf*0.1217081)-(3.500655)),1:0)
check=+$zabs((sex-3)*age3*tc2*hd2*sb2*gf2*hx)
x=$s(check>0:(2.71828**sum)/(1+(2.71828**sum))*100,1:0)
```
