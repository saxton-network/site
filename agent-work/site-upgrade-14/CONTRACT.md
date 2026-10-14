# Contract: site-upgrade-14

Frozen from task R onward. Changing it after R needs fresh readiness and a new owner approval. Copied from `PLAN.md` "Contract" (revision 2 as the owner approved it).

## Source and live change

- **Deployment authority:** `origin` `refs/heads/main`.
- **The source:** the `main` head that task P fast-forwards to (the commit task B passed).
- **v1 (live now):** `8377801ebd47f8ce1ec96eac9bd807dc5a876273`, `site/index.html` SHA-256 `495b4b2b4e8c25335184fa994716a888bc9f0980b3196eb633110bde18351eb3`.
- **v2 (to go live):** `site/index.html` SHA-256 `1f60283e1c442f0fd8e0015787c84febd2b37eabfe83bc9dbea54e7b345f7a35`.
- **The live batch:** one dispatch of `.github/workflows/deploy.yml` on `main` with `agent-work/site-upgrade-14/results/R-dispatch-inputs.json` (`sha` = the source); and, only under "Rollback (V)", one dispatch with `agent-work/site-upgrade-14/results/R-rollback-inputs.json` (`sha` = v1).
- **Main freeze:** see `PLAN.md` "Main freeze".

`CONTRACT.md` writes every hash in full.

## Accepted unknowns

- **CDN caching.** Visitors may see either version for up to about 10 minutes.
- **Runner and action internals.** The live byte comparison covers them. GitHub altering the served bytes is a finding, never a reason to loosen a check.
- **Deployment labels.** GitHub labels a Pages deployment with `main`'s tip, not the deployed input. Only the job log's `DEPLOY` lines and the live bytes are evidence of what is live.

## Evidence clients

This table is decided before approval and proven at readiness. The connection is the session's authenticated GitHub connection. `curl` goes through the session's network proxy, which authenticates it as the same account, so it is a different program and request path, not a different identity.

| Check | Item | Primary | Fallback |
| --- | --- | --- | --- |
| Run | Run list, `head_sha`, `run-name`, conclusion | connection | `curl` (Actions API) |
| Run | Job-step list | connection | `curl` (Actions API) |
| Run | Job log `DEPLOY HEAD` and `DEPLOY INDEX_SHA256` lines | connection (job logs) | `curl` (job-logs API), only if R proves it; otherwise none |
| Live | Page bytes and status | `curl --compressed` with a cache-busting query | none (never a tool that converts HTML to text) |
| Live | `github-pages` deployment IDs | `curl` (deployments API) | none |
| Refs | `refs/heads/main` | `git ls-remote` | `curl` (git refs API) |
| Readiness | Validate CI status on the source | connection | `curl` (Actions API) |
| Readiness | Listed repositories' `private` and `visibility` | connection | `curl` (repos API) |
| Action | The dispatch (v2 or rollback) and any cancel | connection (Actions run-trigger tool) | none; an error is never retried |

The rules:

- **When the fallback is used.** Only when the primary returns no evidence: an error, a timeout, or the item not yet visible.
- **When both are read.** They must agree, and a disagreement is a FAIL.
- **No other substitutes.** No other client stands in for a missing read.

## Dispatch

- **Recheck, seconds before dispatch.** Its output is read clean before dispatching. It covers:
  - `origin/main` equals the source, and its tip is recorded;
  - the frozen hashes and the recomputed fingerprint;
  - the live page is v1;
  - the `deploy.yml` run IDs and the `github-pages` deployment IDs equal the baseline.
- **If the recheck fails:** dispatch nothing, leave J `in_progress`, stop and ask the owner.
- **The dispatch** is a single tool call of its own. If it errors, or no single new run appears within 2 minutes, never dispatch again; stop and ask the owner.
- **Waiting.** Wait up to 45 minutes for the run, because the job's 20-minute limit does not count queue time.
  - If the run is still running after that, cancel it, then wait up to 10 more minutes for `completed`.
  - If it is still not completed, record J `failed` with `liveStateChanged: null`, and ask the owner.

## Runtime acceptance

There is one acceptance window: 10 minutes. It starts at the coordinator's first observation that the run is `completed`, which J.md timestamps, and the coordinator polls at least every minute while waiting. Checks 1–3 run in order and stop at the first failure. Check 4 is always read. If check 1 or 2 fails, the live page is still read once. That read is not counted as acceptance; it supports `liveStateChanged` and V.

**Retry rules within the window:**

- **No evidence.** A read that returned no evidence (an error, a timeout, or not yet visible) may be repeated with the same client, or with its fallback.
- **Failing evidence.** Evidence that fails a check is a FAIL and is never re-read to get a different answer. The one exception is check 3, the live page, where a 200 with v1's exact bytes means "not yet visible" because of the CDN.
- **Window ends.** If there is still no evidence when the window ends, the check fails.
- **Late evidence.** Evidence obtained after a check has failed never turns it into a pass.
- **No second dispatch.** A repeated read is never a reason to dispatch again.

**The checks:**

1. **The run.**
   - Exactly one new `deploy.yml` run.
   - `head_sha` equals the recorded `main` tip.
   - `run-name` is `Deploy <source>`.
   - Conclusion: success.
2. **The log.** It shows `DEPLOY HEAD=<source>`, and `DEPLOY INDEX_SHA256=` the frozen `deployableArtifactSha256` (`1f60283e1c442f0fd8e0015787c84febd2b37eabfe83bc9dbea54e7b345f7a35`).
   - **What counts.** The evidence is the output lines `DEPLOY HEAD=<40 hex>` and `DEPLOY INDEX_SHA256=<64 hex>`, not the `echo` command lines.
   - **How it is read.** It is read with a line limit large enough for the whole log.
   - **No evidence.** A log that is empty, or whose first lines (the job header, for example `Complete job name:`) are missing, so the read was truncated. The log is final, because the run is `completed`.
   - **FAIL.** A complete log that lacks the lines, or has other values.
3. **The live page.** `curl -sS --compressed 'https://saxton-network.github.io/site/?cb=<nonce>'` is read every 30 seconds:
   - a 200 whose body's SHA-256 equals v2 is a PASS;
   - a 200 with v1's bytes is "not yet visible";
   - any other 200 body is a FAIL;
   - a non-200 status is no evidence.
4. **`main` is unchanged** (`git ls-remote`).

## A wrong run

A wrong run has a wrong `head_sha` or `run-name`, or there is more than one new run. No cancel is attempted, because a Pages run cannot reliably be cancelled in time. Instead:

1. Wait until the run is `completed`, within the "Waiting" bounds.
2. Record J `failed` with `runtimeAcceptance: "FAIL"`.
3. Record `liveStateChanged` as below.

## `liveStateChanged` on a failed attempt

It is `false` only when all of these hold, with a one-line reason:

- the run is `completed`, with conclusion `failure` or `cancelled`;
- in the job-step list, the `Run actions/deploy-pages@v5.0.1` step is `skipped` or absent;
- the job log has no deploy-pages output;
- the `github-pages` deployment IDs equal the baseline;
- the live page still returns v1's bytes (supporting evidence only).

Otherwise it is `true`. It is `null` if the step list, the deployments or the job log cannot be read (an error, a timeout or `Forbidden`), or the clients disagree, and `null` is treated as `true`. A repeated read is never used to reach `false`.

A run cancelled while queued has an empty step list and may have no log. An empty step list counts as "absent". A log counts as "missing", and so as "no deploy-pages output", only when the step list is empty and the API reports no log (a 404 or an empty body), never because a read failed.

## Rollback (V)

V runs only after J has failed with `liveStateChanged` not `false`.

1. Make sure the J run is `completed`. If it is still not completed after the post-cancel bound, V does not dispatch; the owner decides.
2. Recheck the hashes of `R-rollback-inputs.json` and `deploy.yml`, and `main`.
   - If `main` still equals the source, go on.
   - If `main` moved, go on only if all of these hold, recording the new tip as V's `head_sha` expectation:
     - the move is a proven additive descendant;
     - v1 is still on the first-parent line;
     - `deploy.yml` has the frozen hash.
   - Otherwise stop and ask the owner.
3. Dispatch once with `sha` = v1, and never repeat it.
4. Rollback acceptance uses the same evidence clients and window rules, with v1 in place of v2:
   - exactly one new run;
   - `run-name` `Deploy 8377801ebd47f8ce1ec96eac9bd807dc5a876273`;
   - success, with the expected `head_sha`;
   - the log shows `DEPLOY HEAD=8377801…` and `DEPLOY INDEX_SHA256=495b4b2b…51eb3`;
   - the live bytes equal v1. For the live page:
     - a 200 whose body equals v1 is a PASS;
     - a 200 with v2's exact bytes is "not yet visible";
     - any other 200 body is a FAIL;
     - a non-200 status is no evidence;
   - `main` is unchanged.
5. If the rollback or its acceptance fails, stop and tell the owner at once. Their emergency option is GitHub Settings → Pages → "Unpublish site". It takes the whole site offline (404), so it is for an exposure problem, not a content slip. The coordinator schedules one read-only check-in at T+30 minutes for as long as that state lasts.

End state: "stopped after verified rollback".

## No rollback needed

When `liveStateChanged: false` is proven:

- V is recorded `failed`, with "rollback not needed", and K stays blocked.
- The end state is "stopped; nothing published, proven".
- The coordinator asks the owner how to continue.
- The records land through a reviewed PR on the owner's go-ahead, with a deviation note for the expected `protected_change`.
- A retry after the records land starts again from A and B, because `main` will have moved. The owner chooses whether to land the records before or after a retry.

## Retry boundary

- One v2 dispatch and one rollback dispatch.
- Any retry needs fresh readiness and a new approval, and J's status is reset to `pending` when that cycle starts.
