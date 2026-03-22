---
description: 'Reference:'
---

# HHS SmartlinkToFlowsheet

[Charge Triggering ](https://galaxy.epic.com/?#Browse/page=1!68!50!207747\&from=Galaxy-Redirect)

Admin Notes

Charge Triggering via HHS

Parameters input:\
ValueID for Charge

1

2

3

4

5

6

7

8







{% code overflow="wrap" %}
```
s inst=$$time^%Zelibb(),val=params,floID=6081,fltID=624,empID=$$getidout^elibEALIB1($$zgUserID^elibEALIBG(),"EMP") d SetFloValAry^JFSAPI3(.floValAry,patID,patDAT,fltID,floID,"",$$time^%Zelibb(),empID,val) d storeSetup^JVITAL20(patID,patDAT,fltID,0,"","",.floValAry) s V(0)=1,V(1)="Success"
```
{% endcode %}

{% code overflow="wrap" %}
```
```
{% endcode %}

<figure><img src="../../.gitbook/assets/image (18).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (16).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (17).png" alt=""><figcaption></figcaption></figure>
