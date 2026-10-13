# Contract: site-update-drill

Frozen from task R onward. Changing it after R needs fresh readiness and a new owner approval.

This workflow is a **drill**. Its live acceptance is designed to fail on purpose, so that the rollback path runs for real. The injected fault is a declared exception, as Workflow's spec requires for a deliberate failure.

## Source and authority

- **Deployment authority:** `origin` `refs/heads/main`, as `AGENTS.md` declares.
- **v1:** `8377801ebd47f8ce1ec96eac9bd807dc5a876273`, deployed by `site-launch` (run 38410452425). Its `site/index.html` SHA-256 is `495b4b2b4e8c25335184fa994716a888bc9f0980b3196eb633110bde18351eb3`.
- **The source (v2):** the exact commit task B passes, fast-forwarded onto `main` by task P.
- **v2 is content only.** Between v1 and v2 only `site/index.html` and records under `agent-work/` change. `.github/`, `scripts/` and every other file stay byte-identical, so the rollback runs the same deploy code as v1's launch.
- **Main freeze:** from P until the records land in V, nothing else moves `main`. Records stay on `pilot/site-update-drill-records`.

## Live batch

The owner's single approval covers exactly two dispatches of `.github/workflows/deploy.yml` on `main`:

1. **The v2 deploy:** input `sha` = the source, frozen in `results/R-dispatch-inputs.json`.
2. **The rollback deploy,** run by the coordinator in task V after J fails: input `sha` = v1, frozen in `results/R-rollback-inputs.json`.

No other dispatch, input or settings change is covered.

## Runtime acceptance (J)

Checks 1, 2a and 2b run in order, stopping at the first failure. Check 3 is read afterwards in every case, because it is read-only and V needs it.

1. **The run.**
   - Exactly one new `deploy.yml` run.
   - `head_sha` equals the `main` tip recorded at the pre-dispatch recheck.
   - `run-name` is `Deploy <source>`.
   - Conclusion: success.
   - The job log shows `HEAD` = the source and the hash in `results/R-expected-sha256.txt`.
2. **The live page.** `curl -sS --compressed 'https://saxton-network.github.io/site/?cb=<nonce>'`.
   - **2a.** Retry every 30 seconds for up to 10 minutes until it returns 200 with a body whose SHA-256 equals `results/R-expected-sha256.txt` (the real v2 hash). This proves v2 really went live.
   - **2b (injected).** Compare that same body's SHA-256 once with `results/R-expected-sha256-INJECTED.txt` (64 zeros). It fails at once, with no retry.
3. **`main`** is unchanged.

WebFetch is never used for acceptance, because it returns converted text, not bytes.

**Expected-failure signature:** 1 and 2a pass, 2b fails, 3 passes, and the live bytes equal v2 exactly. J is then recorded `failed` with `runtimeAcceptance: "FAIL"`, and the drill continues to V. Anything else is a real failure: it is recorded the same way, the rollback runs under the condition in "Rollback (V)", and the drill verdict says what differed.

## Rollback (V)

- **Identity:** `git:8377801ebd47f8ce1ec96eac9bd807dc5a876273`, provenance `results/R-rollback-v1.md`.
- **When the rollback dispatch is approved:** only if v2 may have gone live, that is, the v2 run reached its `deploy-pages` step (whatever its outcome) or the live bytes differ from v1. If the v2 run never reached `deploy-pages` and the live page still equals v1, nothing changed: V dispatches nothing, records "rollback not needed" with V `failed` and the drill verdict FAIL, and asks the owner how to continue; the records land only after the owner decides. The approval does not cover a rollback dispatch in that case.
- **Action:** after the v2 run has finished, one dispatch of `deploy.yml` on `main` with the frozen `results/R-rollback-inputs.json`.
- **Rollback acceptance**, in order:
  - exactly one new run after the v2 run, with `run-name` `Deploy 8377801ebd47f8ce1ec96eac9bd807dc5a876273`, conclusion success, and `head_sha` equal to the `main` tip;
  - the job log shows `HEAD` = v1 and v1's `index.html` hash;
  - the live page, fetched as in check 2, returns 200 with SHA-256 equal to v1's hash, retried every 30 seconds for up to 10 minutes;
  - `main` is unchanged.
- **Retry boundary:** one rollback dispatch. If it, or its acceptance, fails, the coordinator stops and asks the owner. The owner can unpublish the site (Settings → Pages → Unpublish site) if exposure is a concern; v2 is ordinary public content.
- **End state:** "stopped after verified rollback". `main` holds v2 while the live page shows v1. Bringing the live page back to `main` is a later, normal deploy with its own approval.
- **Records.** V lands the records on `main` after independent review and the owner's go-ahead. The records add the frozen files under `agent-work/site-update-drill/`, an expected `protected_change`.

## Accepted unknowns

1. **CDN caching.** Covered by the 10-minute retry windows. Ordinary visitors may see an older page for up to about 10 minutes, including after the rollback.
2. **Whether Pages is enabled.** Confirmed by the owner for `site-launch`, and proven by its successful deploy; not re-read here.
3. **The runner and Pages action internals.** Covered by the live byte comparison.
4. **GitHub altering the served bytes.** If it does, 2a or the rollback acceptance fails. That is a finding, never a reason to loosen a check.

## Retry boundary

One v2 dispatch and one rollback dispatch. Any retry needs fresh readiness and a new approval. After J fails, the helper keeps J `GATED` until a new readiness record exists.
