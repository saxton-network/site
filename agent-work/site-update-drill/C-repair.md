# Task C: repair (conditional)

- **Prerequisites:** B `findings`, already set in the manifest.
- **Branch:** `pilot/site-update-drill-fix`, from the candidate. A finding in the scaffold or contract is repaired on the records branch by the coordinator, before R freezes anything.

## Work

Fix each finding that is in scope or a site-rule violation. v2 must stay content only. The same reviewer re-reviews. For a second round, the coordinator resets C to `pending`.

## Result

`results/C-1.md`, with the repaired candidate commit.

## Records

Hand the result content to the coordinator. Only the coordinator commits to `pilot/site-update-drill-records`; nothing under `agent-work/site-update-drill/` is committed to the implementation branch.

## Stop boundary

Stop at the end of this task and hand the result to the coordinator. Do not start another task.
