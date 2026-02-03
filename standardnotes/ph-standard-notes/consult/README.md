---
description: Framework for both POC and Standaard
---

# Consult

Smartlink to ETX

* [PHIPNOTECONSULTHEADER](phipnoteconsultheader.md)
* [PHNAME](../h-and-p/phname.md)
* [PHDIAG](../h-and-p/phdiag/)
* [PHIPNOTECSAP](phipnotecsap/)
* [PHIPNOTEHPI2](../h-and-p/phipnotehpi2.md)
* [PHIPNOTEHISTORY2](../h-and-p/phipnotehistory2.md)
* [PHIPNOTESVITALSHP2](../h-and-p/phipnotevitalshp2/)



Smartlink Sections

* PHAPBEGIN
* PHHIPBEGIN
* PHOBJBEGIN



Smartlink\SmartBlocks

* PEDSADVANCED
* PHDIAGPOC



TIP Texts

* ETX 22244
* ETX 21693
* ETX 21411
* ETX 22267



```
@PHIPNOTECONSULTHEADER@
@PHAPBEGIN@
@CERMSGREFRESH(89901:22244,,,1)@
@PHNAME@
@PHDIAG@ //@PHDIAGPOC@ = DAN Smartlink
@PHIPNOTECSAP@

@PHHPIBEGIN@ 
@CERMSGREFRESH(89901:21693,,,1)@
@PHIPNOTEHPI2@
@PHIPNOTEHISTORY2@

@PHOBJBEGIN@ 
@CERMSGREFRESH(89901:21411,,,1)@
@PHIPNOTEVITALSHP2@
@PEDSADVANCED@
{Chaperone documentation (Optional):25932}
@CERMSGREFRESH(89901:22267,,,1)@
```
