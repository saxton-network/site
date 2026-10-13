# Task V: rollback and verification

- **Prerequisites:** J `failed`, already set in the manifest.
- **Read first:** `AGENTS.md`, `CONTRACT.md` "Rollback (V)".
- **Performed by the coordinator**, under the approval in `results/J-approval.md`, which covers this one dispatch.

## Work

1. **Make sure the v2 run has finished.** If it hasn't, cancel it and wait for it to finish.
2. **Decide whether a rollback is needed** (`CONTRACT.md` "Rollback (V)"). Whether the v2 run reached `deploy-pages` is read from its job's step list (`actions_list` `list_workflow_jobs`): the step `Run actions/deploy-pages@v5.0.1` has a `started_at`. If it never started and the live page still equals v1, dispatch nothing: record "rollback not needed", V `failed` and the drill verdict FAIL with what differed, and ask the owner how to continue. K stays blocked, and the records land only after the owner decides.
3. **Recheck:** `origin/main` equals the source; the hashes of `R-rollback-inputs.json` and `deploy.yml` equal the frozen ones and the ones in `J-approval.md`; record the `deploy.yml` run IDs. If any recheck fails, dispatch nothing, stop and ask the owner.
4. **Dispatch** exactly `R-rollback-inputs.json`, once. Never re-dispatch. If the call does not answer `204`, or no new run appears, re-list the runs for up to 2 minutes; if there is still no single new run, stop and ask the owner.
5. **Rollback acceptance,** as `CONTRACT.md` lists it, stopping at the first failure. On a failure, record V `failed`, stop and ask the owner; K stays blocked.
6. **Drill verdict:** PASS only if J matched the expected-failure signature and the rollback acceptance passed.
7. **Records divergence.** Prove the records descend from the source, list their changed paths with the documented commands (no inherited `GIT_*` variables), and run `classify_divergence` with the frozen batch's paths. Expect `protected_change` only for the frozen files under `agent-work/site-update-drill/` (`CONTRACT.md` and the `results/R-*` files); any other protected path stops the landing.
8. **Secrets and site-rule check** of the records.
9. **Land the records.** Open the records PR (only `agent-work/site-update-drill/`). After independent review and the owner's go-ahead, land it on `main` with a local `git merge --no-ff`, pushed as a fast-forward. Verify through the API that GitHub marks the PR merged; if not, close it with a comment naming the merge commit.
10. **Record V `complete` before the merge,** because records cannot prove their own merge. Report the merge commit and a fresh check of `main` and the live page afterwards, outside the records.

## Result

`results/V.md`: the rechecks, the rollback run, each acceptance check, the drill verdict, the divergence proof and the records PR.

## Records

Only the coordinator commits to `pilot/site-update-drill-records`.

## Forbidden

- A second rollback dispatch, or any other input.
- Changing settings.
- Merging the records PR without review and the owner's go-ahead.

## Stop boundary

Stop at the end of this task and hand the result to the coordinator. Do not start another task.
