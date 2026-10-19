# Task K: final reconciliation

- **Prerequisites:** J `complete` with `runtimeAcceptance` `PASS`.

## Work

1. **Verify,** with the evidence clients. K's reads come after acceptance: a read that returns no evidence stops K and is reported.
   - `main` equals the source, or is a proven additive descendant classified as `COORDINATOR.md` requires. Stop if it is neither.
   - The live page bytes equal v2.
2. **Secrets and privacy scan** of the records: no private names, hosts, people or emails, and no tokens.
3. **Records PR,** adding only `agent-work/site-upgrade-14/`, with a divergence proof run with no inherited `GIT_*` variables.
   - `classify_divergence` is expected to report `protected_change` only for `CONTRACT.md` and the frozen `results/R-*` files. Any other protected path stops the landing.
   - The independent records review also checks that commit identities and trailers are only those the "Commit metadata" exemption allows.
4. **Land it** after independent review and the owner's go-ahead:
   - a local `git merge --no-ff` under the no-reply identity, pushed as a fast-forward under `COORDINATOR.md` "Commands that move refs";
   - never GitHub's merge API;
   - verify through the API that GitHub marks the PR merged. If it does not, close the PR with a comment naming the merge commit.

Record K `complete` before the merge. Report the merge, and a fresh check of `main` and the live page, afterwards.

## Result

`results/K.md`.

## Records

Hand the result content to the coordinator. Only the coordinator commits to `pilot/site-upgrade-14-records`.

## Stop boundary

Stop at the end of this task and hand the result to the coordinator. Do not start another task.
