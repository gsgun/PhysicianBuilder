# Pattern: Standard-Note Tip Texts

**When to use:** one-liner dynamic hints embedded in note headers/sections.

## Recipe

1. Build (or reuse) a CER whose **Error Message** is the human tip sentence.
2. Pull it in the ETX with the message getter:

```
$zconvert($$getMessage^S2LPP3(<cerId>,,0,id,dat),"T")
```

`"T"` capitalizes the first letter. Source: [standardnotes/tip-texts.md](../../standardnotes/tip-texts.md) (service-abbreviation tip via CER 1360588).

3. Gate the whole line with `@CERMSG(...)@` so it disappears when not applicable.

## Example (from backlog)

`"Medical Readiness for Discharge: " + VTE Prophylaxis plan` via message 1360838 — see [to-do/medical-readiness-for-discharge.md](../../to-do/medical-readiness-for-discharge.md).

## Gotchas

- Tip texts refresh on **note events**, not on rule evaluation — don't promise real-time.
- Long tips bloat note headers; keep to ≤1 line, defer detail to a SmartLink.
- `EPT-INP-Item 200000` sticky-note tip text renders oddly — known cosmetic issue, tracked in [to-do/mentorship-questions.md](../../to-do/mentorship-questions.md).
