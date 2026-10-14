# Task P: authority promotion

- **Prerequisites:** B `passed` for the exact candidate; Validate CI green on it.

## Work

Under `COORDINATOR.md` "Commands that move refs", in a non-shallow clone (`git rev-parse --is-shallow-repository` prints `false`), with no inherited `GIT_*` variables for the local proofs:

Gates, each exiting before anything moves (run under `set -euo pipefail`, with `SHA` set to the full literal `deploymentSourceSha` of B's latest `passed` record, after any repair round):

0. `if [ "$(git rev-parse --is-shallow-repository)" != false ]; then exit 1; fi`
   `if [ -z "$SHA" ] || [ "$SHA" != <B's passed deploymentSourceSha, full literal> ]; then exit 1; fi`
1. `git fetch origin`; `if [ "$(git rev-parse origin/main)" != ae90609244b36f306f924bf5470f21d8cf202bb2 ]; then exit 1; fi`
2. `if ! GIT_GRAFT_FILE=/dev/null git --no-replace-objects -c core.commitGraph=false -c advice.graftFileDeprecated=false merge-base --is-ancestor <origin/main> "$SHA"; then exit 1; fi`
3. `if [ "$(git rev-list --first-parent "$SHA" | grep -cx 8377801ebd47f8ce1ec96eac9bd807dc5a876273)" != 1 ]; then exit 1; fi`
4. Only after every gate above has passed, as a separate command with the full literal SHA: `git push origin "$SHA":refs/heads/main`, never with force. Check its exit status.
5. Verify `git ls-remote origin refs/heads/main` equals `$SHA`.
6. As a separate step, not chained to the push: merge `main` into `pilot/site-upgrade-records` (non-force) so later gate checks use the alpha.13 helper. Stop on any conflict or failure.

## Result

`results/P.md`.

## Records

Hand the result content to the coordinator. Only the coordinator commits to `pilot/site-upgrade-records`.

## Forbidden

Force pushes, merge commits on `main`, rebases. If the push is refused or `main` moved, stop.

## Stop boundary

Stop at the end of this task and hand the result to the coordinator. Do not start another task.
