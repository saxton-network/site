# Task K: final reconciliation

- **Prerequisites:** J `complete` with `runtimeAcceptance` `PASS`.

## Work

1. Verify: `main` equals the source, or is a proven additive descendant classified as `COORDINATOR.md` requires (stop if not); the live page bytes equal v2.
2. Secrets and privacy scan of the records (no private names, hosts, people, emails; no tokens).
3. Records PR (only `agent-work/site-upgrade/`) with a divergence proof run with no inherited `GIT_*` variables. `classify_divergence` is expected to report `protected_change` only for `CONTRACT.md` and the frozen `results/R-*` files; any other protected path stops the landing.
4. After independent review and the owner's go-ahead, land it with a local `git merge --no-ff` pushed as a fast-forward, per `COORDINATOR.md` "Commands that move refs". Verify through the API that GitHub marks the PR merged; if not, close it with a comment naming the merge commit.

Record K `complete` before the merge; report the merge and a fresh check of `main` and the live page afterwards.

## Result

`results/K.md`.

## Records

Hand the result content to the coordinator. Only the coordinator commits to `pilot/site-upgrade-records`.

## Stop boundary

Stop at the end of this task and hand the result to the coordinator. Do not start another task.
