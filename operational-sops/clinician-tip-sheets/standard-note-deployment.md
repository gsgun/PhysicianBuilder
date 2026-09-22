# Tip Sheet: Standard Note Deployment Lessons

Distilled from the 1/13–1/19 standard-notes deployment break-fix sequence.
Source: [standardnotes/ph-standard-notes/deployment.md](../../standardnotes/ph-standard-notes/deployment.md)

## What broke, in order

| Day | Incident | Root pattern |
|---|---|---|
| 1/14 | Copy Last Sections "Lookback" failed to find changed sections | feature behavior changed by the modular build itself — test the *interaction*, not the feature |
| 1/15 | Error in SDE Name CER rule | name/identity rules are brittle to whole-encounter scope |
| 1/16 | Breakfix: CER rule re-scoped to whole encounter | scope (admission vs encounter) is the #1 silent bug axis |
| 1/18 | Copy Last Section restricted to User Only | default behavior too aggressive → demote to explicit user action |
| 1/19 | Hospice note bugs | edge case note types need their own test pass |

## Standing rules (adopt for every future deploy)

1. **Document in real time** — not at the end of the deploy.
2. **Test in SUP TST with a debug test script** before go-live (see [bugs-to-do/test-script.md](../../standardnotes/ph-standard-notes/bugs-to-do/test-script.md)).
3. **Spend time trying to break it** — hospice/POC/surgical edge note types before standard ones.
4. Prefer **User-Only** for destructive/lookback features until proven.
5. Rollout cadence: mid-day deploy window + same-day breakfix path (this sequence averaged ~1 incident/day for 7 days — budget for it).
