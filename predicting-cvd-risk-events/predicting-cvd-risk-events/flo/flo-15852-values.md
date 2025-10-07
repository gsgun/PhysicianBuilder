---
description: Values Row Type Custom Formula Value Type String Context Overtime
---

# FLO 15852 VALUES

{% code overflow="wrap" %}
```
// M:x
p={15817;;0}
hx1=+$$getMessage^S2LPP3(835306,,0,patID,patDAT)
hx1=$s(hx1=1:0,1:1)
hxc={15832;;3}
hx=$s(hxc=1:0,hxc=0:1,1:hx1)
hxs=$s(hx=0:" History of ASCVD ",1:" No history of ASCVD, ")
age=+$$getMessage^S2LPP3(835308,,0,patID,patDAT)
tc=+$zabs(+$$lastResultsFrComp^LRESULT("CHOL",1,1,patID))
hd=+$zabs(+$$lastResultsFrComp^LRESULT("HDL",1,1,patID))
gf={15855;;0}
sb=+$$getMessage^S2LPP3(835298,,0,patID,patDAT)
dm1=+$$evalRule^elibHULIB22(835302,patID,patDAT)
dmc={15816;;3}
dm=$s(dmc=1:1,dmc=0:0,1:dm1)
dms=$s(dm=1:"Hx of DM, ",1:"No Hx of DM, ")
sm1=+$$evalRule^elibHULIB22(835309,patID,patDAT)
smc={15841;;3}
sm=$s(smc=1:1,smc=0:0,1:sm1)
sms=$s(sm=1:"Current Smoker, ",1:"Not a smoker, ")
sex1=+$$evalRule^elibHULIB22(835421,patID,patDAT)
sexc={15815;;4}
sex=$s(sexc=1:1,sexc=2:0,sexc=3:3,1:sex1)
sexs=$s(sex=1:"Female, ",sex=0:"Male, ",1:" Sex-Logic ")
htn=+$$evalRule^elibHULIB22(835299,patID,patDAT)
htns=$s(htn=1:"HTN Rx, ",1:"No HTN Rx, ")
stn=+$$evalRule^elibHULIB22(835300,patID,patDAT)
stns=$s(stn=1:" Statin Rx, ",1:" No Statin Rx, ")
bm=$$getMessage^S2LPP3(835297,,0,patID,patDAT)
age2=$s((age>=30)&(age<=79):age,1:0)
tc2=$s((tc>=130)&(tc<=320):tc,1:0)
hd2=$s((hd>=20)&(hd<=100):hd,1:0)
sb2=$s((sb>=90)&(sb<=200):sb,1:0)
gf2=$s((gf>=15)&(gf<=150):gf,1:0)
ascvd10={15821;;0}
x=$s(ascvd10=0:"Does not meet criteria due to:"_$s(hx=0:" History of ASCVD ",1:$c(5))_$s(sex=3:sexs,1:$c(5))_$s(age2=0:" Age: "_age,1:$c(5))_$s(tc2=0:" TCL: "_tc,1:$c(5))_$s(hd2=0:" HDL: "_hd,1:$c(5))_$s(sb2=0:" SBP: "_sb,1:$c(5))_$s((gf2=0)&(sex'=3):" eGFR: "_gf,1:$c(5)),1:hxs_dms_sms_sexs_htns_stns_"Age: "_age2_", TCL: "_tc2_", HDL: "_hd2_", SBP: "_sb2_", eGFR: "_gf2_", BMI: "_bm)
```
{% endcode %}
