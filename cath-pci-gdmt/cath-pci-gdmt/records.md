---
description: Nomenclature
---

# Records

CER Rules

IP ED Admission Med Rec

1. Parent                                                                     836408
2. PTA Unrec                                                              836344&#x20;
3. Review Not Done                                                  836363
4. Review Done + PTA Meds                                  836339  &#x20;
5. Review - Pharmacist Complete                        836362&#x20;
6. Review - Pharmacy Tech Complete                 836361
7. Review - RN Complete                                        836339



ETX

PH IP ED ADMISSION MED REC

1. Parent                                                                   24604
2. [Review Status - TIP](../../admission-med-rec-tip-text/admission-med-rec/etx/)                                           24605
3. [Unrec Meds - TIP](../../admission-med-rec-tip-text/admission-med-rec/etx/)                                               24606  &#x20;



HFP

Custom Properties&#x20;

INI: ADT,EPT, ORD, IEV&#x20;

1. C\_ADT EVENTS
   1.      Reverse Index Look Up
   2. INI ADT
      1. Item 60 - Patient
2. C\_IEV EVENTS
   1. New Group
   2. Reverse Index Look Up
   3. INI IEV
      1. Item 1640 - Related ADT Event ID
3. C\_IEV PATIENT CSN
   1. Item 28 - Patient CSN
4. C\_Event Type
   1. Item 21 - Type
5. C\_IP ORDREC ADMISSION STATUS
   1. Group 30 - Event Type
   2. Item 1500 - IP ORDREC ADMISSION STATUS
6. C\_IP REC SUMMARY
   1. Group 1700
   2. Item 1700 - IP REC SUMMARY - ORDER ID
7. C\_IP REC SUMMARY - ORDER ID
   1. Item 1700 Order ID
8. C\_IP REC SUMMARY - NEEDED RECONCILIATION
   1. Item 1710 IP REC SUMMARY - NEEDED RECONCILIATION?
9. C\_IP REC SUMMARY - WAS RECONCILED
   1. Item 1720 IP REC SUMMARY - WAS RECONCILED?
10. C\_CANCELLATION STATUS
    1. INI ORD
    2. Item 604 Cancel Status
11. C\_GENERIC NAME
    1. INI Orders
       1. Group Medications
       2. INI ERX
       3. Item 114 Simple Generic Name
