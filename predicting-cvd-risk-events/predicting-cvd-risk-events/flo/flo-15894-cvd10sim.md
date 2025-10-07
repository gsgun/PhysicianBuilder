---
description: CVD10 Sim Code. Row Type Custom Formula Value Type Numeric Context Overtime
---

# FLO 15894 CVD10SIM

```
// M:xM:x
p={15853;;0}
a=patID
b=patDAT
h=+$$evalRule^elibHULIB22(835299,a,b)
s=+$$evalRule^elibHULIB22(835300,a,b)
a1=+$$getMessage^S2LPP3(835308,,0,a,b)
sb=+$$getMessage^S2LPP3(835298,,0,a,b)
tc1=$zabs($$lastResultsFrComp^LRESULT("CHOL",1,1,a))
tcc=$$sumMultSelect^JCUSTFORM1({15846;;0})
tc=$s(tcc>0:tcc,1:tc1)
hd1=$zabs($$lastResultsFrComp^LRESULT("HDL",1,1,a))
hdc=$$sumMultSelect^JCUSTFORM1({15848;;0})
hd=$s(hdc>0:hdc,1:hd1)
s=$s(hdc>0:1,1:s)
d1=+$$evalRule^elibHULIB22(835302,a,b)
dc={15842;;3}
d=$s(dc=1:1,dc=0:0,1:d1)
sm1=+$$evalRule^elibHULIB22(835309,a,b)
smc={15887;;3}
sm=$s(smc=1:1,smc=0:0,1:sm1)
hx1=+$$getMessage^S2LPP3(835306,,0,a,b)
hx1=$s(hx1=1:0,1:1)
hxc={15832;;3}
hx=$s(hxc=1:0,hxc=0:1,1:hx1)
sx1=+$$evalRule^elibHULIB22(835421,a,b)
sxc={15815;;4}
sx=$s(sxc=1:1,sxc=2:0,sxc=3:3,1:sx1)
gf={15855;;0}
a2=$s((a1>=30)&(a1<=79):((a1-55)/10),1:0)
a3=$s((a1>=30)&(a1<=79):a1,1:0)
t2=$s((tc>=130)&(tc<=320):((tc-hd)*0.02586)-3.5,1:0)
hd2=$s((hd>=20)&(hd<=100):((hd*0.02586)-1.3)/0.3,1:0)
sb2=$s((sb>=90)&(sb<=200):sb,1:0)
g=$s((gf>=15)&(gf<=150):gf,1:0)
ns=$s(sb2<=110:(sb2-110)/20,1:0)
xs=$s(sb2>110:(sb2-130)/20,1:-1)
ng=$s(g<=60:(g-60)/-15,1:0)
xg=$s(g>60:(g-90)/-15,1:2)
sum=$s(sx=1:(((a2*0.719883)+(t2*0.1176967)-(hd2*0.151185)-(ns*0.0835358)+(xs*0.3592852)+(d*0.8348585)+(sm*0.4831078)+(ng*0.4864619)+(xg*0.0397779)+(h*0.2265309)-(s*0.0592374)-(xs*h*0.0395762)+(t2*s*0.0844423)-(a2*t2*0.0567839)+(a2*hd2*0.0325692)-(a2*xs*0.1035985)-(a2*d*0.2417542)-(a2*sm*0.0791142)-(a2*ng*0.1671492)-(3.819975))),sx=0:((a2*0.7099847)+(t2*0.1658663)-(hd2*0.1144285)-(ns*0.2837212)+(xs*0.3239977)+(d*0.7189597)+(sm*0.3956973)+(ng*0.3690075)+(xg*0.0203619)+(h*0.2036522)-(s*0.0865581)-(xs*h*0.0322916)+(t2*s*0.114563)-(a2*t2*0.0300005)+(a2*hd2*0.0232747)-(a2*xs*0.0927024)-(a2*d*0.2018525)-(a2*sm*0.0970527)-(a2*ng*0.1217081)-(3.500655)),1:0)
check=+$zabs((sx-3)*a3*t2*hd2*sb2*g*hx)
x=$s(check>0:(2.71828**sum)/(1+(2.71828**sum))*100,1:null)
```
