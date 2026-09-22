# Pattern: ETX Message-Driven Composition

**When to use:** dynamic tip text in standard notes / smartlists that must re-evaluate when upstream state changes.

## Vocabulary

| Macro | Role | Example |
|---|---|---|
| `@CERMSG(<cer>:<etx>,,,1)@` | parent ETX gated by a CER; no output if false | `@CERMSG(836408:24604,,,1)@` in PHIPNOTEHEADERHOSPITALIST [22718] |
| `@CERMSGREFRESH(<cerA>:<etxA>;<cerB>:<etxB>,1,,1)@` | parent ETX containing multiple rule→output pairs; re-evaluates on refresh | `@CERMSGREFRESH(836363:24605;836344:24606,1,,1)@` |
| `@LASTFLOWMOD2(<flo>)@` | last flowsheet value inline in output text | `Risk ... is @LASTFLOWMOD2(16026)@%` |
| `{<label>:<listChoiceId>}` | smartlist choice picker in ETX | `{Step 2 - Select Choice from List ASCVD CVD:30409997}` |
| `$p($p($$getMessage^S2LPP3(<id>,,0,id,dat),"PREFIX",2),"SUFFIX",1)` | fetch a CER's *message* (not boolean) as tip text | Medical Readiness for Discharge via 1360838 |

Sources:
- [admission-med-rec build-design.md](../../admission-med-rec-tip-text/admission-med-rec/build-design.md)
- [etx-24604.md](../../admission-med-rec-tip-text/admission-med-rec/etx/etx-24604.md), [etx-24726 output](../../gupta-surgery-risk-scores/untitled/etx/etx-24726-ph-ip-sur-pre-op-risk-score-output.md), [etx-24418 smartlist](../../predicting-cvd-risk-events/predicting-cvd-risk-events/etx/etx-ph-ip-amb-ascvd-cvd-smartlist-24418.md)

## The 3-layer contract (standard notes)

```
Standard Note ETX  (e.g. PHIPNOTEHEADERHOSPITALIST [22718])
  └─ @CERMSG(parentCER:parentETX,,,1)@
       └─ parent ETX: @CERMSGREFRESH(childA:outA;childB:outB,1,,1)@
            ├─ child CER A  →  output ETX A
            └─ child CER B  →  output ETX B
```

Rules:
- **If parent CER false → no line break, no output** (silent is success).
- Formatting (bold/spaces) lives in the **output ETX only**; the gating ETX stays logic-only.
- Tip texts are **static-trigger** — they refresh on the events Epic wires to the note, not continuously.
