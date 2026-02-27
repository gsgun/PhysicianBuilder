---
description: For migration of changes and troubleshooting
---

# Test Script

1. When new changes are made in POC to ETX
   1. Make new contacts
   2. Keep in one ticket
2.  One Ticket goes to TST for Test Script

    1. Keep either POC or SUP clean and open to do the debugging


3. Script for dual environment comparion
   1. Open a note in a new patient
   2. Select Service
      1. Main services include: Hospitalist, Critical Care, Cardiology, Pediatrics, Surgery
      2. Hospice is special and shouldn't have any real issues
   3. Insert Smarttext
      1. Preview load each of the Standard Note Smarttexts
         1. Standard and POC for each of the Note Types (8 in total)
         2. Compare TST to SUP\POC Preview&#x20;
            1. Dual Screen
            2. Preview and Loaded should be the same, so don't necessarily need to load
         3. Identify any bugs, errors, or discrepancies
            1. Do not change\fix in real time
            2. create notes&#x20;
      2. Check Name loading
         1. ???
4. Bug\Fix
   1. Change in SUP to try to fix
   2. Create new contact in POC to back migrate
