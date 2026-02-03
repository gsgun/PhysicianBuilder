---
description: HHS PHNAMEPROMPT [101417] to ETX PHNAMEFALSE [24816]
---

# PHNAMEPROMPT

ETX:

@PHNAME@



SDE

PH IP PATIENT PROMPT \[PHORDERS#002]

* Note Context
* Yes



Override

If IP Hospital Course Name SDE True \[836752] = PHNAMETRUE \[25036]

Rule criteria:

1. Patient » Note SmartData Value By Note Type a = 1 a Note Types = Progress Notes \[1]; SmartData Element = PHORDERS#002; Search Admission? = Yes \[1] Error message: Patient » Note SmartData Value By Note Type
