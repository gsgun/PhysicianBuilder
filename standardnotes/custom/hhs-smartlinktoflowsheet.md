---
description: 'Reference:'
---

# HHS SmartlinkToFlowsheet

[Charge Triggering ](https://galaxy.epic.com/?#Browse/page=1!68!50!207747\&from=Galaxy-Redirect)

Admin Notes

Charge Triggering via HHS

Parameters input:\
ValueID for Charge

1 Prolonged Services

2 Critical Care

3 Office Outpatient

4 1st Hospital

5 Prolonged Services



{% code overflow="wrap" %}
```
s inst=$$time^%Zelibb(),val=params,floID=6081,fltID=624,empID=$$getidout^elibEALIB1($$zgUserID^elibEALIBG(),"EMP") d SetFloValAry^JFSAPI3(.floValAry,patID,patDAT,fltID,floID,"",inst+(val*5),empID,val) d storeSetup^JVITAL20(patID,patDAT,fltID,0,"","",.floValAry) s V(0)=1,V(1)=inpID_" x "_inst_" "_val
```
{% endcode %}

<figure><img src="../../.gitbook/assets/image (19).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (20).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (21).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (22).png" alt=""><figcaption></figcaption></figure>
