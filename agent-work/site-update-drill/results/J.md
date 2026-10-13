# Task J: live deployment (drill)

- `drill: true`
- Approval: `results/J-approval.md`, for source `8f3c310876166dc0cb2864dff3646e18830b1758` and frozen batch `d2a53d23b197f1bc5a80e8c95c9970c6508c766798b50df0f4427d6863542726`.

**Runtime acceptance: FAIL, matching the expected-failure signature.**

## Recheck before dispatch (2026-10-13T14:49:41Z)

- `git ls-remote origin refs/heads/main` = the source; this is the recorded `main` tip.
- `deploy.yml` runs: only 38410452425 (v1).
- Every frozen hash matches the R record: `deploy.yml` and the three validators at `origin/main`; the four `results/R-*` files and `CONTRACT.md` on the records branch.
- Live baseline: status 200, SHA-256 `495b4b2b…51eb3` (v1).

## Dispatch

One `run_workflow` call for `deploy.yml` on `main` with `sha: 8f3c310876166dc0cb2864dff3646e18830b1758`, answered `204 No Content` (about 14:49:50Z). No other dispatch was made.

## Check 1: the run — PASS

- Exactly one new run: 38416735077 (the list went from 1 run to 2).
- `head_sha` = `8f3c310…`, the recorded `main` tip. `run-name` = `Deploy 8f3c310876166dc0cb2864dff3646e18830b1758`.
- Conclusion `success`; job 115363064206 and every step `success`. `Run actions/deploy-pages@v5.0.1` started 14:50:01Z and ended 14:50:17Z.
- Job log: `HEAD is now at 8f3c310`, `PASS: site check (2 repositories listed)`, `DEPLOY HEAD=8f3c310876166dc0cb2864dff3646e18830b1758`, `DEPLOY INDEX_SHA256=1f60283e1c442f0fd8e0015787c84febd2b37eabfe83bc9dbea54e7b345f7a35` (equal to `R-expected-sha256.txt`). The archive held only `./index.html`; `pages_build_version` = the source.

## Check 2a: v2 is live — PASS

`curl -sS --compressed 'https://saxton-network.github.io/site/?cb=<nonce>'` at 2026-10-13T14:50:43Z, first try: status 200, SHA-256 `1f60283e1c442f0fd8e0015787c84febd2b37eabfe83bc9dbea54e7b345f7a35`, equal to `R-expected-sha256.txt`.

## Check 2b (injected): FAIL, as designed

The same body's SHA-256 compared once with `R-expected-sha256-INJECTED.txt` (64 zeros): not equal. No retry.

## Check 3: `main` — PASS

`git ls-remote origin refs/heads/main` after the checks = `8f3c310…`, unchanged.

## Outcome

- 1, 2a and 3 passed; 2b failed; the live bytes equal v2 exactly. **This matches the expected-failure signature.**
- J is recorded `failed` with `runtimeAcceptance: "FAIL"`. The run had completed, so nothing was cancelled.
- The v2 run reached `deploy-pages`, so the rollback dispatch is approved (`CONTRACT.md` "Rollback (V)").
