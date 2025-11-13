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
2. [Review Status - TIP](etx/)                                           24605
3. [Unrec Meds - TIP](etx/)                                               24606  &#x20;



HFP

Custom Properties&#x20;

INI: ADT,EPT, ORD, IEV&#x20;

1. C\_IEV EVENTS

&#x20;a. New Group

Reverse Index Look Up

a. Item C\_IEV PATIENT CSN

1.
   1. Item 28 - Patient CSN
2. C\_Event Type
   1. Item 21 - Type
3. C\_IP ORDREC ADMISSION STATUS
   1. Group 30 - Event Type
   2. Item 1500 - IP ORDREC ADMISSION STATUS
4. C\_IP REC SUMMARY
   1. Group 1700
   2. Item 1700 - IP REC SUMMARY - ORDER ID
5. C\_IP REC SUMMARY - ORDER ID
   1. Item 1700 Order ID
6. C\_IP REC SUMMARY - NEEDED RECONCILIATION
   1. Item 1710 IP REC SUMMARY - NEEDED RECONCILIATION?
7. C\_IP REC SUMMARY - WAS RECONCILED
   1. Item 1720 IP REC SUMMARY - WAS RECONCILED?
8. C\_CANCELLATION STATUS
   1. INI ORD
   2. Item 604 Cancel Status
9. C\_GENERIC NAME
   1. INI Orders
      1. Group Medications
      2. INI ERX
      3. Item 114 Simple Generic Name
