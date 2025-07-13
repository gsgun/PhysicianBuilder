---
description: ETX for PH Standard Notes
---

# Standard Note ETX

Parent Text and Parent Rule evaluate if Child A or Child B are true

* If Parent True, then Parent Text is run
  * Determines which Child is True and returns respective ETX

Parent Tip Text: @CERMSG(836408:24604,,,1)@



**CER Rule 836408**&#x20;

**Rule: IP ED Admission Med Rec Parent**

Logic: Or

1. IP ED Admission Med Rec Review Not Done \[836363]
2. IP ED Admission Med Rec PTA Unrec \[836344]



**ETX** [**24604**](etx-24604.md)

**ETX: PH IP ED ADMISSION MED REC - PARENT**



ETX Containing Parent Tip Text:

ETX 22220 PHIPNOTEHPAPCRITCAREPOC\
ETX 22361 PHIPNOTEHEADERCRITICALCARE\
ETX 22718 PHIPNOTEHEADERHOSPITALIST\
ETX 23044 PHIPNOTEHPAPCRITCARE\
ETX 23532 PHIPNOTEHPAPHOSPITALIST\
ETX 23535 PHIPNOTEHPAPHOSPITALISTPOC
