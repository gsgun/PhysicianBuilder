---
description: Design Language
---

# Build Design

Build: Integrate into Standard Notes as Tip Texts

* Limitations: Tip Texts are not dynamic and triggered by static events



Design Language

* Standard Note ETX
*   CERSG to evaluate Parent ETX

    * If false, does not create line break
    * If true, then returns a smarttext that contains a CERSMGR - Rule Driven with Parent\Child


* Example
  * Standard Note ETX - PHIPNOTEHEADERHOSPITALIST \[22718]
    * @CERMSG(836408:24604,,,1)@
      * Parent ETX - PH IP ED ADMISSION MED REC - PARENT \[24604]
      * CER - IP ED Admission Med Rec Parent \[836408]
        * @CERMSGREFRESH(836363:24605;836344:24606,1,,1)@ //First Line True
          * Output Text - PH IP ED ADMISSION MED REC - REVIEW STATUS - TIP \[[24605](../../admission-med-rec-tip-text/admission-med-rec/etx/)]
          * CER - Rule: IP ED Admission Med Rec Review Not Done \[836363]
          * Output Text - PH IP ED ADMISSION MED REC - UNREC MEDS - TIP \[[24606](../../admission-med-rec-tip-text/admission-med-rec/etx/)]
          * CER - Rule: IP ED Admission Med Rec PTA Unrec \[836344]

