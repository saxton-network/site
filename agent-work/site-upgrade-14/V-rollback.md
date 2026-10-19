# Task V: rollback and verification

- **Prerequisites:** J `failed` with `liveStateChanged` not `false`.
- **Performed by the coordinator** under `results/J-approval.md`. The approval covers this one dispatch, under the conditions in `CONTRACT.md` "Rollback (V)".

## Work

Follow `CONTRACT.md` "Rollback (V)" steps 1–5 exactly, with its evidence clients:

1. **The J run is completed.** If it is not, do not dispatch; the owner decides.
2. **The recheck,** including the conditions for a `main` that has moved.
3. **One dispatch** of `R-rollback-inputs.json`.
4. **Rollback acceptance,** including the live-page rule: v1 is a PASS, and v2 means "not yet visible".
5. **On failure,** stop and tell the owner; Unpublish is their emergency option. Schedule a read-only check-in at T+30 minutes for as long as that state lasts.

Then the records:

- **Divergence proof,** with no inherited `GIT_*` variables. The expected `protected_change` is exactly `CONTRACT.md` and the frozen `results/R-*` files. Any other protected path stops the landing.
- **Secrets and privacy scan.**
- **Records PR,** adding only `agent-work/site-upgrade-14/`.
- **Independent review,** including commit identities and trailers.
- **The owner's go-ahead.**
- **Landing:** a local `--no-ff` merge under the no-reply identity, under `COORDINATOR.md` "Commands that move refs". Never GitHub's merge API.

Record V `complete` before the merge. Report the merge and a fresh check afterwards. End state: "stopped after verified rollback".

If any verification fails, record V `failed`, stop and report. K stays blocked.

## Result

`results/V.md`.

## Records

Hand the result content to the coordinator. Only the coordinator commits to `pilot/site-upgrade-14-records`.

## Forbidden

- A second rollback dispatch.
- Any other input.
- Settings changes.
- Merging without review and the owner's go-ahead.

## Stop boundary

Stop at the end of this task and hand the result to the coordinator. Do not start another task.
