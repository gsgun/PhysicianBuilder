# Pattern: FLO Custom Formula (MUMPS) Library

**When to use:** computed values on flowsheet rows (risk scores, derived vitals).

## Helper catalog (proven in this fleet)

| Helper | Purpose | Used in |
|---|---|---|
| `$$evalRule^elibHULIB22(<cerId>,patID,patDAT)` | run a CER inside a formula, returns boolean | [FLO 15821 ASCVD10](../../predicting-cvd-risk-events/predicting-cvd-risk-events/flo/flo-15821-ascvd10.md) |
| `$$getMessage^S2LPP3(<cerId>,,0,patID,patDAT)` | fetch a CER's numeric/message output | FLO 15821 (age, SBP, Hx) |
| `$$lastResultsFrComp^LRESULT("<base>",1,1,patID)` | last lab by base name | `$$lastResultsFrComp^LRESULT("CHOL",1,1,patID)` |
| `$$sumMultSelect^JCUSTFORM1({<smartformRow>;;0})` | read multi-select smartform row | [FLO 16026 Cardiac PreOp](../../gupta-surgery-risk-scores/untitled/flo/flo-16026-cardiac-preop.md) |
| `$$zCalcAge^%Zefnlii(+$h,$$getn^elibEAnLIB(...))` | age from birthdate EPT | FLO 16026 |
| `+$$zabs(...)` | numeric coercion wrapper (blank→0 semantics) | everywhere |

## Structural template (risk score FLO)

```
M:x
# 1. pull inputs (smartform, labs, rules)
asa=$$sumMultSelect^JCUSTFORM1({15988;;0})
cre=+$zabs(+$$lastResultsFrComp^LRESULT("CREAT",1,1,patID))
age=+$$zCalcAge^%Zefnlii(...)
# 2. per-input normalization (each $s maps input→coefficient)
fun1=$s(fun=2:0.65,fun=3:1.03,fun=1:0,1:0)
# 3. sum of coefficients + constant; logistic transform
sum=age+fun1+asa1+cre1+typ1-5.25
risk=((2.71828**sum)/(1+(2.71828**sum)))*100
risk=$normalize(risk,2)
# 4. NULL GUARD: if any required input missing → null, never 0
chk=fun*typ*asa
x=$s(chk=0:null,1:risk)
```

## Hard rules

- **Null guard on the final line** (`x=$s(chk=0:null,1:risk)`): a missing input must render blank, never a false 0% risk.
- **Range-clamp every lab input** before it enters the coefficient sum (ASCVD10: `tc2=$s((tc>=130)&(tc<=320):...,1:0)`).
- **Completeness check as product** of multi-select flags (`chk=fun*typ*asa`) — zero if any is 1/missing; use XOR-free logic.
- Cite the source publication in the ETX output line, not in the formula.
