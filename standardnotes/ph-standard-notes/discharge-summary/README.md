---
description: Framework for both POC and Standaard
---

# Discharge Summary

Smartlink to ETX

* [PHIPNOTEDCNOTEHEADER](phipnotedcnoteheader.md)
* [PHIPNOTEDCFOLLOWUP2](phipnotedcfollowup2.md)
* [PHIPNOTEDCAP](phipnotedcap.md)
* [PHIPNOTEDCAPPOC](phipnotedcappoc.md)
* [PHIPNOTEDCTIMESPENT2](phipnotedctimespent2.md)
* [PHIPDCTCM](phipdctcm.md)



Smartlink Sections

* PHDISPOBEGIN
* PHOBJBEGIN



Smartlink\SmartBlocks

* PEDSADVANCED



TIP Texts

* ETX 22153
* ETX 21511



```
@PHIPNOTEDCNOTEHEADER@
@CERMSGREFRESH(89901:22153,,,1)@

@PHIPNOTEDCFOLLOWUP2@

@PHIPNOTEDCAP@ //@PHIPNOTEDCAPPOC@

@PHDISPOBEGIN@
@PHIPNOTEDCTIMESPENT2@

@CERMSGREFRESH(89901:21511,,,1)@
@PHOBJBEGIN@
Vitals
@V@
@PEDSADVANCED@

@PHIPDCTCM@
```
