---
description: 'Reference:'
---

# HHS CASECONVERT

[IRIS Objectscript Reference](https://docs.intersystems.com/irislatest/csp/docbook/DocBook.UI.Page.cls?KEY=RCOS_fzconvert)

Admin Notes

Displays Case Change for Rule Error Message Outputs

Parameters input:\
RuleID,number

Example:\
RuleIDLastName,1\
Output:\
SMITH

Number:\
1=ALL CAPS\
2=lower case\
3=Only first letter of first word is capitalized\
4=First Letter Capitalized In Each Word



{% code overflow="wrap" %}
```
n x,ruleid,case,output s ruleid=$p(params,",",1),case=$p(params,",",2),output=$$getMessage^S2LPP3(ruleid,,0,patid,patdat),case=$s(case=1:"U",case=2:"L",case=3:"S",1:"W"),x=$zconvert(output,case),V(0)=1,V(1)=x
```
{% endcode %}

{% code overflow="wrap" %}
```
n x,ruleid,case,output /declare variables
s /set command
ruleid=$p(params,",",1)  /params is input parameters which are RULEID,NUMBERFORCASE
case=$p(params,",",2)    /Case selection
output=$$getMessage^S2LPP3(ruleid,,0,patid,patdat)  /Output message for the RuleID
case=$s(case=1:"U",case=2:"L",case=3:"S",1:"W")     /Convert to Selected Case
x=$zconvert(output,case)                            /ZCONVERT Objectscript Function

V(0)=1  /number of lines in array
V(1)=x  /call first line for output
```
{% endcode %}

<figure><img src="../../.gitbook/assets/image (18).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (16).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (17).png" alt=""><figcaption></figcaption></figure>
