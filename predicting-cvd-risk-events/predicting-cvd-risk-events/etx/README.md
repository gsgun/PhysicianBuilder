---
description: >-
  This is the Standard Build for ETX\Smartform to emulate an automatic smartlink
  as much as possible
---

# ETX

<figure><img src="../../../.gitbook/assets/image (1).png" alt=""><figcaption></figcaption></figure>

HHS 101281 ASCVDRISK2024

* Smarttext -> ETX 23978

PH IP AMB ASCVD CVD PARENT 23978

* PH IP AMB ASCVD CVD - TIP 24015
*   PH IP AMB ASCVD CVD SMARTLIST 24418

    * ELT 304009997
      * 3 choices Rule for Inclusion Based upon if criteria met
      * PH IP AMB ASCVD CVD OUTPUT PARENT 24700
        * PH IP AMB ASCVD CVD OUTPUT TRUE 23932 + {Charge:304009998}
        * PH IP AMB ASCVD CVD OUTPUT TRUE 23932 + {Charge:304009998}
        * PH IP AMB ASCVD CVD OUTPUT FALSE 23963
          * ELT 304009998
            * 3 choices. Rule for Inclusion Based on what was selected for Charge
              * All ETXs are PH IP AMB ASCVD CVD CHARGE 24348
              * Dynamically Changes based on Rule Output

