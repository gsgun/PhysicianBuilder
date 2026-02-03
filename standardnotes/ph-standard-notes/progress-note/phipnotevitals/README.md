---
description: HHS PHIPNOTEVITALS [100717] to ETX PHIPNOTEVITALS [21130]
---

# \*\*\*PHIPNOTEVITALS

ETX:

Vitals (Most recent)\
T: @LAST24HRWODATE(6)@ BP: @LAST24HRWODATE(5)@ HR: @LAST24HRWODATE(8)@\
RR: @LAST24HRWODATE(9)@ SpO2: @FLOWDATETIME28HR(10:last:1)@\
O2 Rate: @FLOWDATETIME28HR(250026:last:1)@\
@FLOWDATETIME28HR(3040150391:last:1)@

Wt: @LAST24HRWODATE(14)@ @FLOW(11)@ BMI:@BMI@\
@24HRWTCHANGE@



Override

If Cardiology   = [PHIPNOTEVITALSCARDIO ](phipnotevitalscardio.md)\[22736]

If Surgery        = [PHIPNOTEVITALSSURG ](phipnotevitalssurg.md)\[24762]

If Critical Care = [PHIPNOTEVITALSCRITICALCARE ](../../h-and-p/phipnotevitalshp2/phipnotevitalscriticalcare.md)\[20766]
