# Contract: site-upgrade

Frozen from task R onward. Changing it after R needs fresh readiness and a new owner approval. Copied from `PLAN.md` "Contract" (revision 3, approved; decision 2(a)).

## Source and live change

- **Deployment authority:** `origin` `refs/heads/main`.
- **The source:** the `main` head that task P fast-forwards to (the commit task B passed).
- **v1 (live now):** `8377801ebd47f8ce1ec96eac9bd807dc5a876273`, `site/index.html` SHA-256 `495b4b2b4e8c25335184fa994716a888bc9f0980b3196eb633110bde18351eb3`.
- **v2 (to go live, decision 2(a)):** `site/index.html` SHA-256 `1f60283e1c442f0fd8e0015787c84febd2b37eabfe83bc9dbea54e7b345f7a35`.
- **The live batch:** one dispatch of `.github/workflows/deploy.yml` on `main` with `agent-work/site-upgrade/results/R-dispatch-inputs.json` (`sha` = the source); and, only under "Rollback (V)", one dispatch with `agent-work/site-upgrade/results/R-rollback-inputs.json` (`sha` = v1).
- **Main freeze:** see `PLAN.md` "Main freeze".

`CONTRACT.md` writes every hash in full.

## Accepted unknowns

- **CDN caching.** A 10-minute retry window covers it. Visitors may see either version for up to about 10 minutes.
- **Pages enablement.** Readiness's 200 baseline and three earlier deploys show it.
- **Runner and action internals.** The live byte comparison covers them. GitHub altering the served bytes is a finding, never a reason to loosen a check.
- **Deployment labels.** GitHub labels a Pages deployment with `main`'s tip, not the deployed input. Only the job log's `DEPLOY HEAD` line and the live bytes are evidence of what is live.

## Dispatch

- **Recheck, seconds before dispatch.** Its output is read clean before dispatching. It covers:
  - `origin/main` equals the source, and its tip is recorded;
  - the frozen hashes and the recomputed fingerprint;
  - the live page is v1;
  - the `deploy.yml` run IDs and the `github-pages` deployment IDs equal the baseline.
- **If the recheck fails:** dispatch nothing, leave J `in_progress`, stop and ask the owner.
- **The dispatch** is a single tool call of its own. If it errors, or no single new run appears within 2 minutes, never dispatch again. Stop and ask the owner.
- **Waiting.** Up to 45 minutes for the run: the job's 20-minute limit does not count queue time.
  - If the run is still running after that, cancel it, then wait up to 10 more minutes for `completed`.
  - If it is still not completed, record J `failed` with `liveStateChanged: null`, and ask the owner.

## Runtime acceptance

Checks 1 and 2 run in order, stopping at the first failure. Check 3 is always read, because it is read-only and V needs it.

1. **The run.**
   - Exactly one new `deploy.yml` run.
   - `head_sha` equals the recorded `main` tip.
   - `run-name` is `Deploy <source>`.
   - Conclusion: success.
   - The log shows `DEPLOY HEAD=<source>` and `DEPLOY INDEX_SHA256=` the frozen `deployableArtifactSha256` (`1f60283e1c442f0fd8e0015787c84febd2b37eabfe83bc9dbea54e7b345f7a35` under decision 2(a)).
2. **The live page.**
   - `curl -sS --compressed 'https://saxton-network.github.io/site/?cb=<nonce>'` returns 200, and the body's SHA-256 equals v2.
   - It is retried every 30 seconds for up to 10 minutes. WebFetch is never used.
3. **`main` is unchanged.**

## A wrong run

Wrong means a wrong `head_sha` or `run-name`, or more than one new run. A Pages run cannot reliably be cancelled in time, so no cancel is attempted. Instead:

1. Wait until the run is `completed`, within the same bounds as "Waiting" (45 minutes, then cancel, then 10 more minutes).
2. Record J `failed` with `runtimeAcceptance: "FAIL"`.
3. Record `liveStateChanged` as below.

## `liveStateChanged` on a failed attempt

It is `false` only when **all** of these hold, with a one-line reason:

- the run is `completed`, with conclusion `failure` or `cancelled`;
- in the job's step list, the `Run actions/deploy-pages@v5.0.1` step has `conclusion: skipped`, or is absent;
- the job log has no deploy-pages output;
- the `github-pages` deployment IDs equal the baseline: no new deployment;
- the live page still returns v1's bytes. This is supporting evidence only, because of the CDN.

Otherwise it is `true`. It is `null` if the step list or the deployments cannot be read, and `null` is treated as `true`.

A run cancelled while still queued has an empty step list and may have no log. An empty step list counts as "absent", and a missing log as "no deploy-pages output", so such a run can meet the `false` proof if the deployment IDs are unchanged.

## Rollback (V)

V runs only after J has failed with `liveStateChanged` not `false`.

1. Make sure the J run is `completed`. If it is still not completed after the post-cancel bound, V does not dispatch. The `pages` concurrency group would queue the rollback behind it, so the order of the two is uncertain. The owner decides.
2. Recheck:
   - the hashes of `R-rollback-inputs.json` and `deploy.yml`;
   - `main`.

   If `main` still equals the source, go on. If `main` moved, go on only if:
   - the move is a proven additive descendant (ancestry from the source, in a non-shallow clone);
   - v1 is still on the first-parent line;
   - `deploy.yml` at the new tip has the frozen hash.

   In that case, record the new tip as V's `head_sha` expectation. Otherwise stop and ask the owner.
3. Dispatch once with `sha` = v1. Never repeat it.
4. Rollback acceptance:
   - exactly one new run;
   - `run-name` `Deploy 8377801ebd47f8ce1ec96eac9bd807dc5a876273`;
   - success, with `head_sha` equal to the expected tip;
   - the log shows `DEPLOY HEAD=8377801…` and `DEPLOY INDEX_SHA256=495b4b2b…51eb3`;
   - the live bytes equal v1, within the 10-minute window;
   - `main` is unchanged since step 2.
5. If the rollback, or its acceptance, fails, stop and tell the owner at once. Their emergency option is GitHub Settings → Pages → "Unpublish site". It takes the whole site offline (404), so it is for an exposure problem, not a content slip. The coordinator schedules one read-only check-in at T+30 minutes for as long as that state lasts.

End state: "stopped after verified rollback". `main` then holds the upgrade and v2, while the site serves v1.

## No rollback needed

When `liveStateChanged: false` is proven:

- V is recorded `failed`, "rollback not needed", and K stays blocked.
- End state: "stopped; nothing published, proven".
- The coordinator asks the owner how to continue.
- The records land through a reviewed PR on the owner's go-ahead, with a deviation note for the expected `protected_change`. A retry after the records land starts again from A and B, because `main` will have moved.

## Retry boundary

- One v2 dispatch, and one rollback dispatch.
- Any retry needs fresh readiness and a new approval.
