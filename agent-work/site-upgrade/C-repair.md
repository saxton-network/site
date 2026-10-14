# Task C: repair (conditional)

- **Prerequisites:** B `findings`, set in the manifest before dispatch.
- **Branch:** `pilot/site-upgrade-fix`, from the candidate.

## Work

Fix each in-scope finding; never edit a vendored file except by re-copying it from the release. The same reviewer re-reviews. For a second round, the coordinator sets B back to `findings` and C back to `pending` in the same records commit. If B is not clean after two rounds, stop and report to the owner.

## Result

`results/C-n.md` with the repaired candidate.

## Records

Hand the result content to the coordinator. Only the coordinator commits to `pilot/site-upgrade-records`.

## Stop boundary

Stop at the end of this task and hand the result to the coordinator. Do not start another task.
