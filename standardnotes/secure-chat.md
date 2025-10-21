---
description: ICU Test Templates
---

# ETX 24815 PHICUSTDTEST



```
@PHIPNOTEHEADERBASE@
@CERMSGREFRESH(89901:21186,,,1)@
Principal problem: @PRINCIPALPROBLEM@
@CERMSGREFRESH(836450:22355,,,1)@
@PHHOSPITALCOURSEBEGIN@
@CERMSG(836752:24816)@@PHHOSPITALCOURSETEXT@***
@PH24HOURBEGIN@ 
•	***

@DIAGPOC@
Feeding: {Feeding plan:25520}
Thromboprophylaxis: {Thromboprophylaxis plan:25523}
Ulcer prophylaxis: {Ulcer prophylaxis plan:25524}
Glycemic: {Glycemic plan:25525}
{Disposition (Optional):25828}

@CERMSG(836120:24263)@
Code status: @RRCODESTATUS@@ACPLINK@

@PHIPACPBEGIN@
Surrogate Decision Maker/family updates: ***
Patient preferences or limitations on interventions: ***
@PHIPACPEND@
@CERMSG(836407:24667,,,1)@

@PHSUBBEGIN@
@PHIPNOTECC@ 
Hospital day: @IPLENGTHOFSTAY@
***

@PHOBJBEGIN@ 
@CERMSGREFRESH(89901:21411,,,1)@
@PHIPNOTEVITALS@
@PHIPNOTEPHYSICALEXAM@
@CERMSGREFRESH(89901:22267,,,1)@
@CERMSGREFRESH(89901:21207,,,1)@

```
