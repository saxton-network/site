# Task P: authority promotion

- **Prerequisites:** B `passed` for the exact candidate; Validate CI is green on it.

## Work

1. **Fetch and prove ancestry.** `git fetch origin`, then prove the candidate descends from `origin/main`, with no inherited `GIT_*` variables:
   `GIT_GRAFT_FILE=/dev/null git --no-replace-objects -c core.commitGraph=false -c advice.graftFileDeprecated=false merge-base --is-ancestor <origin/main> <candidate>`
2. **Fast-forward.** `git push origin <candidate>:refs/heads/main`, never with force.
3. **Verify.** `git ls-remote origin refs/heads/main` equals the candidate.

## Result

`results/P.md`.

## Records

Hand the result content to the coordinator. Only the coordinator commits to `pilot/site-launch-records`; nothing under `agent-work/site-launch/` is committed to the implementation branch.

## Forbidden

Force pushes, merge commits on `main`, rebases. If the push is refused or `main` moved, stop.

## Stop boundary

Stop at the end of this task and hand the result to the coordinator. Do not start another task.
