# Task K: final reconciliation

- **Prerequisites:** J `complete` with `runtimeAcceptance` `PASS`.

## Work

1. **Verify:**
   - `main` equals the deployed source;
   - the live page bytes still equal the frozen hash.
2. **Secrets and site-rule check** of the records.
3. **Land the records.** Open the records PR (only `agent-work/site-launch/`), with divergence proof.
   - After independent review and the owner's go-ahead, land it on `main` with a merge commit built locally (`git merge --no-ff`), pushed as a fast-forward.
   - The helper is expected to report `protected_change` only for `agent-work/site-launch/results/R-dispatch-inputs.json`; any other protected path stops the landing.
   - Verify through the API that GitHub marks the PR merged; if it does not, close the PR with a comment naming the merge commit.
   - Then check `main` again; report that merge and check after them, outside the records.

## Result

`results/K.md`.

## Records

Hand the result content to the coordinator. Only the coordinator commits to `pilot/site-launch-records`; nothing under `agent-work/site-launch/` is committed to the implementation branch.

## Stop boundary

Stop at the end of this task and hand the result to the coordinator. Do not start another task.
