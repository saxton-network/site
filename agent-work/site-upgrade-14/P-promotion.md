# Task P: authority promotion

- **Prerequisites:** B `passed` for the exact candidate; Validate CI green on it.

## Work

Work under `COORDINATOR.md` "Commands that move refs", in a non-shallow clone. Inherited `GIT_*` variables are removed for the local proofs. Run every gate under `set -euo pipefail`, with `SHA` set to the full literal `deploymentSourceSha` of B's latest `passed` record (after any repair round). Each gate exits before anything moves.

**Gates:**

0. Check that the clone is not shallow and that `SHA` is set to that literal:

   ```
   if [ "$(git rev-parse --is-shallow-repository)" != false ]; then exit 1; fi
   if [ -z "$SHA" ] || [ "$SHA" != <B's passed deploymentSourceSha, full literal> ]; then exit 1; fi
   ```
1. Check that `main` has not moved:

   ```
   git fetch origin main
   if [ "$(git rev-parse origin/main)" != 16c363137b52093fcd014ee00d8c4a8ca570e658 ]; then exit 1; fi
   ```
2. Check that the candidate descends from `main`:

   ```
   if ! GIT_GRAFT_FILE=/dev/null git --no-replace-objects -c core.commitGraph=false -c advice.graftFileDeprecated=false merge-base --is-ancestor 16c363137b52093fcd014ee00d8c4a8ca570e658 "$SHA"; then exit 1; fi
   ```
3. Check that v1 stays on the candidate's first-parent line:

   ```
   if [ "$(git rev-list --first-parent "$SHA" | grep -cx 8377801ebd47f8ce1ec96eac9bd807dc5a876273)" != 1 ]; then exit 1; fi
   ```

**Then:**

4. Only after every gate above has passed, push as a separate command, with the full literal SHA and never with force: `git push origin <SHA literal>:refs/heads/main`. Check its exit status.
5. Verify that `git ls-remote origin refs/heads/main` equals the SHA.
6. As a separate step, not chained to the push, merge `main` into `pilot/site-upgrade-14-records` (non-force), so that later gate checks use the alpha.14 helper. Stop on any conflict or failure.

## Result

`results/P.md`.

## Records

Hand the result content to the coordinator. Only the coordinator commits to `pilot/site-upgrade-14-records`.

## Forbidden

Force pushes, merge commits on `main`, rebases. If the push is refused or `main` moved, stop.

## Stop boundary

Stop at the end of this task and hand the result to the coordinator. Do not start another task.
