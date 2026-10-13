# Contract: site-launch

Frozen from task R onward. Changing it after R needs fresh readiness and a new owner approval.

## Source and authority

- **Deployment authority:** `origin` `refs/heads/main`, as `AGENTS.md` declares.
- **The source:** the exact commit task B passes, fast-forwarded onto `main` by task P.
- **Main freeze:** from P until K, nothing else moves `main`. Records stay on `pilot/site-launch-records`.

## Live batch

One dispatch of `.github/workflows/deploy.yml` on `main`, with input `sha` set to the source. The exact inputs are frozen in `agent-work/site-launch/results/R-dispatch-inputs.json`.

Turning on GitHub Pages is a separate live change that the owner performs, with its own preview and approval, before this batch.

## Runtime acceptance

The checks run in order:

1. **The run.**
   - Exactly one new `deploy.yml` run.
   - `head_sha` equals the `main` tip recorded at the pre-dispatch recheck.
   - `run-name` is `Deploy <source>`.
   - Conclusion: success.
   - The job log shows `HEAD` = the source and the frozen `site/index.html` hash.
2. **The live page.**
   - `curl -sS --compressed 'https://saxton-network.github.io/site/?cb=<nonce>'` returns 200.
   - The SHA-256 of the body equals the frozen `deployableArtifactSha256`.
   - Retry every 30 seconds for up to 10 minutes.
3. **`main`** is unchanged.

WebFetch is never used for acceptance, because it returns converted text, not bytes.

## Accepted unknowns

1. **CDN caching.** Covered by the 10-minute retry window. Ordinary visitors may see older content for up to about 10 minutes.
2. **Whether Pages is enabled.** It cannot be read without a token, so the owner confirms it. If it is off, the deploy fails at the environment step and nothing goes live; that run is still a failed attempt.
3. **The runner and Pages action internals.** Covered by the live byte comparison.
4. **GitHub altering the served bytes.** If it does, acceptance fails. That is a finding, never a reason to loosen the check.

## Rollback

- **Identity:** `pages-unpublished-404`.
- **If anything fails:**
  1. The coordinator stops and records J `failed` with `runtimeAcceptance: "FAIL"`.
  2. It shows the owner the live hash, the status, and what differs.
  3. **The owner decides** whether to unpublish (Settings → Pages → Unpublish site). If they do, task V polls until the page returns 404.
- **End state:** "stopped after failed launch", with the rollback recorded as either "unpublished and verified 404" or "declined by owner".
- **Records.** Task V lands the records, as in Pilot 4 of Workflow. A content mistake that exposes nothing is fixed later by a new reviewed update.

## Retry boundary

One dispatch. A retry needs fresh readiness and a new approval. After a failed attempt the helper keeps J `GATED` until a new readiness record exists.
