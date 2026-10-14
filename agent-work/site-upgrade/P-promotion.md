# Task P: authority promotion

- **Prerequisites:** B `passed` for the exact candidate; Validate CI green on it.

## Work

Under `COORDINATOR.md` "Commands that move refs", in a non-shallow clone (`git rev-parse --is-shallow-repository` prints `false`), with no inherited `GIT_*` variables for the local proofs:

1. `git fetch origin`; assert `origin/main` is `ae90609…`.
2. `if ! GIT_GRAFT_FILE=/dev/null git --no-replace-objects -c core.commitGraph=false -c advice.graftFileDeprecated=false merge-base --is-ancestor <origin/main> <candidate>; then exit 1; fi`
3. `if [ "$(git rev-list --first-parent <candidate> | grep -cx 8377801ebd47f8ce1ec96eac9bd807dc5a876273)" != 1 ]; then exit 1; fi`
4. Push the asserted literal SHA: `git push origin <candidate>:refs/heads/main`, never with force.
5. Verify `git ls-remote origin refs/heads/main` equals the candidate.
6. Merge `main` into `pilot/site-upgrade-records` (non-force) so later gate checks use the alpha.13 helper.

## Result

`results/P.md`.

## Records

Hand the result content to the coordinator. Only the coordinator commits to `pilot/site-upgrade-records`.

## Forbidden

Force pushes, merge commits on `main`, rebases. If the push is refused or `main` moved, stop.

## Stop boundary

Stop at the end of this task and hand the result to the coordinator. Do not start another task.
