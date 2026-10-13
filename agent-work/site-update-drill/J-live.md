# Task J: live deployment (human gate, drill)

- **Prerequisites:**
  - R `complete` with `PASS`;
  - the owner's explicit "y" to the concrete preview, which covers the v2 dispatch and the one rollback dispatch.
- **Read first:** `AGENTS.md`, `PLAN.md` "Live previews", `CONTRACT.md`.
- **The preview states:** the source and fingerprint; that this is a drill and the declared injected fault with its expected-failure signature; both dispatches; the effects and exposure (v2 is public for a few minutes; caches may show either version for up to about 10 minutes); the checks; the stop conditions; the rollback; the retry boundary; and the end state (`main` holds v2 while the site shows v1).
- The coordinator records the approval in `results/J-approval.md` (`in_progress`) and confirms the helper shows `READY`. That label is a handoff only. `J-approval.md` names the source and the frozen batch fingerprint, states that exactly two dispatches are approved (the v2 deploy, and the rollback only under the condition in `CONTRACT.md` "Rollback (V)"), and lists `R-dispatch-inputs.json` and `R-rollback-inputs.json` with their SHA-256 hashes.

## Work

1. **Recheck:**
   - `origin/main` equals the source, and record its tip;
   - the IDs of the existing `deploy.yml` runs;
   - the frozen file hashes;
   - the live page baseline (v1).

   **If any recheck fails** (`main` moved, a frozen hash differs, the live page is not v1): dispatch nothing, leave J `in_progress`, stop and ask the owner. J is never recorded `failed` without a dispatch, because that would make V ready.
2. **Dispatch** exactly `R-dispatch-inputs.json`, once. Never re-dispatch. If the call does not answer `204`, or no new run appears, re-list the runs for up to 2 minutes; if there is still no single new run, stop and ask the owner. If the new run's `run-name` or `head_sha` is wrong, cancel it, wait for it to finish, and go to step 4.
3. **Runtime acceptance:** checks 1, 2a and 2b of `CONTRACT.md`, stopping at the first failure; then read check 3. Compare the outcome with the expected-failure signature.
4. **Stop.** Make sure the run is `completed`; if not, cancel it and wait. Record J `failed` with `runtimeAcceptance: "FAIL"`, and whether the failure matched the signature.

## Result

`results/J.md`, containing `drill: true`, the approval reference, the rechecks, the run ID and `head_sha`, each check's outcome, and whether the failure matched the signature.

## Records

Hand the result content to the coordinator. Only the coordinator commits to `pilot/site-update-drill-records`; nothing under `agent-work/site-update-drill/` is committed to the implementation branch.

## Forbidden

- A second v2 dispatch, or any other input.
- Recording J `complete`.
- Changing settings.

## Stop boundary

Stop at the end of this task and hand the result to the coordinator. Do not start another task.
