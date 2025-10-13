---
description: SmartText
---

# ETX

Build: Alert clinicians for Verification and Reconciliation Status

* Gap analysis ideal to determine where the break is in the system to optimize workflow
* PTA medications are imported from SureScripts?
  * Verification by RN, Pharmacy Tech, or Pharmacists
* Reconciliation by Admitters or Rounding Physicians
* Delays from OSH Transfers or ICU
* Utilize :1 ELT as Disappearing Tip Text

**Parent Text - PH IP ED ADMISSION MED REC - PARENT \[**[**24604**](../../../admission-med-rec-tip-text/admission-med-rec/etx/etx-24604.md)**]**

@CERMSGREFRESH(836363:24605;836344:24606,1,,1)@

**Child Text - PH IP ED ADMISSION MED REC - REVIEW STATUS - TIP \[**[**24605**](../../../admission-med-rec-tip-text/admission-med-rec/etx/etx-24605.md)**]**

{PTA Medications Unreviewed\
@CERMSGREFRESH(836362;836361;836342;836363,1)@ //Rule Returns Last Verification Date\
Please contact Pharmacy, RN to complete verify medications\
[**Med Dispense** **Med Rec Status PTA** **Admission PTA Med Rec**](../../../admission-med-rec-tip-text/admission-med-rec/epicact.md) **:1}**

**Child Text - PH IP ED ADMISSION MED REC - UNREC MEDS - TIP \[**[**24606**](../../../admission-med-rec-tip-text/admission-med-rec/etx/etx-24606.md)**]**

{PTA Medications Unreconciled\
@CERMSGREFRESH(836362;836361;836342;836363,1)@\
@CERMSGREFRESH(836339)@\
[Med Dispense Med Rec Status PTA Admission PTA Med Rec](../../../admission-med-rec-tip-text/admission-med-rec/epicact.md) :1}

