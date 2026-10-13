# Task V: after a failed launch

- **Prerequisites:** J `failed`, already set in the manifest.
- **Read first:** `AGENTS.md`, `CONTRACT.md` "Rollback".

## Work

1. **Make sure the deploy run has finished.** If it hasn't, cancel it and wait for it to finish.
2. **Unpublish, if the owner chose it.** Poll `https://saxton-network.github.io/site/` with `curl -sS --compressed '<url>?cb=<nonce>'` until it returns 404, retrying for up to 10 minutes. If it does not, stop and report.
3. **Record the end state:** "stopped after failed launch", with the rollback either "unpublished and verified 404" or "declined by owner".
4. **Land the records.** Run the same records check, secrets and site-rule scan, and records landing as K. The expected `protected_change` is the same as in K.
5. **Record V.** Mark V `complete` before the merge, or `failed` if any verification fails; K stays blocked.

## Result

`results/V.md`.

## Records

Only the coordinator commits to `pilot/site-launch-records`.

## Stop boundary

Stop at the end of this task. A new launch attempt is a new readiness and approval cycle.
