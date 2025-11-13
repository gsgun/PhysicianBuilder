---
description: CVA10 Sim Code. Row Type Custom Formula Value Type Numeric Context Overtime
---

# FLO 15844 CVA10SIM

```
// M:x
p={15853;;0}
a=patID
b=patDAT
h1=+$$evalRule^elibHULIB22(835299,a,b)
s=+$$evalRule^elibHULIB22(835300,a,b)
a1=+$$getMessage^S2LPP3(835308,,0,a,b)
sbc=$$sumMultSelect^JCUSTFORM1({15848;;0})
sbb=+$$getMessage^S2LPP3(835298,,0,a,b)
sb=$s(sbc>0:110,1:sbb)
h=$s(sbc>0:0,1:h1)
tc1=$zabs($$lastResultsFrComp^LRESULT("CHOL",1,1,a))
tcc=$$sumMultSelect^JCUSTFORM1({15846;;0})
tc=$s(tcc>0:130,1:tc1)
hd1=$zabs($$lastResultsFrComp^LRESULT("HDL",1,1,a))
hd=$s(tcc>0:100,1:hd1)
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
sum=$s(sx=1:(((a2*0.7939329)+(t2*0.0305239)-(hd2*0.1606857)-(ns*0.2394003)+(xs*0.3600781)+(d*0.8667604)+(sm*0.5360739)+(ng*0.6045917)+(xg*0.0433769)+(h*0.3151672)-(s*0.1477655)-(xs*h*0.0663612)+(t2*s*0.1197879)-(a2*t2*0.0819715)+(a2*hd2*0.0306769)-(a2*xs*0.0946348)-(a2*d*0.27057)-(a2*ng*0.1637806)-(a2*sm*0.078715)-(3.307728))),sx=0:((a2*0.7688528))+(t2*0.0736174)-(hd2*0.0954431)-(ns*0.4347345)+(xs*0.3362658)+(d*0.7692857)+(sm*0.4386871)+(ng*0.5378979)+(xg*0.0164827)+(h*0.288879)-(s*0.1337349)-(xs*h*0.0475924)+(t2*s*0.150273)-(a2*t2*0.0517874)+(a2*hd2*0.0191169)-(a2*xs*0.1049477)-(a2*d*0.2251948)-(a2*ng*0.1543702)-(a2*sm*0.0895067)-(3.031168),1:0)
check=+$Zabs((sx-3)*a3*t2*hd2*sb2*g*hx)
x=$s(check>0:(2.71828**sum)/(1+(2.71828**sum))*100,1:null)
```
