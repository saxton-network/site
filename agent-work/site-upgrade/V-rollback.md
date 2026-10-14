# Task V: rollback and verification

- **Prerequisites:** J `failed` with `liveStateChanged` not `false`.
- **Performed by the coordinator** under `results/J-approval.md`, which covers this one dispatch under the conditions in `CONTRACT.md` "Rollback (V)".

## Work

Follow `CONTRACT.md` "Rollback (V)" steps 1–5 exactly: the J run completed (if not, do not dispatch; the owner decides); the recheck, including the `main`-moved conditions; one dispatch of `R-rollback-inputs.json`; rollback acceptance; on failure, stop, tell the owner (Unpublish is their emergency option) and schedule a read-only T+30-minute check-in while that state lasts.

Then the records: divergence proof with no inherited `GIT_*` variables (expected `protected_change` exactly `CONTRACT.md` and the frozen `results/R-*` files, which the spec allows after a verified rollback; any other protected path stops the landing), secrets and privacy scan, records PR (only `agent-work/site-upgrade/`), independent review, the owner's go-ahead, landing per `COORDINATOR.md` "Commands that move refs". Record V `complete` before the merge; report the merge and a fresh check afterwards. End state: "stopped after verified rollback".

If any verification fails, record V `failed`, stop and report; K stays blocked.

## Result

`results/V.md`.

## Records

Hand the result content to the coordinator. Only the coordinator commits to `pilot/site-upgrade-records`.

## Forbidden

A second rollback dispatch; any other input; settings changes; merging without review and the owner's go-ahead.

## Stop boundary

Stop at the end of this task and hand the result to the coordinator. Do not start another task.
