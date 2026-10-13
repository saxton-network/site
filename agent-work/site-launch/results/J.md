# Task J: live deployment

Performed by the coordinator on 2026-10-13 under the owner's approval in `J-approval.md`, for source `8377801ebd47f8ce1ec96eac9bd807dc5a876273` and frozen batch `23142a14e4f5434621d9362c31934b0c4519e8f7240fc7e333cce12885eed71a`.

**Runtime acceptance: PASS**

## Recheck before dispatch (2026-10-13T14:05:57Z)

- `git ls-remote origin refs/heads/main` = the source; this is the recorded `main` tip.
- `deploy.yml` had zero runs.
- Frozen hashes all match `R.md`: `deploy.yml`, `check-site.py`, `validate.sh`, `agent-task.py` and `site/index.html` at `origin/main`; `R-dispatch-inputs.json` and `CONTRACT.md` on the records branch.
- Live baseline: status 404.

## Dispatch

One `run_workflow` call for `deploy.yml` on `main` with `sha: 8377801ebd47f8ce1ec96eac9bd807dc5a876273`, answered `204 No Content` at about 2026-10-13T14:06:02Z. No other dispatch was made.

## Check 1: the run — PASS

- Exactly one new `deploy.yml` run: 38410452425 (run number 1; the list went from 0 runs to 1).
- `head_sha` = `8377801ebd47f8ce1ec96eac9bd807dc5a876273`, the recorded `main` tip.
- `run-name` = `Deploy 8377801ebd47f8ce1ec96eac9bd807dc5a876273`.
- Conclusion `success`; job `deploy` (115341097044) and every step `success`.
- Job log: `HEAD is now at 8377801`, `PASS: site check (2 repositories listed)`, `DEPLOY HEAD=8377801ebd47f8ce1ec96eac9bd807dc5a876273`, `DEPLOY INDEX_SHA256=495b4b2b4e8c25335184fa994716a888bc9f0980b3196eb633110bde18351eb3`. The archive held only `./index.html`. deploy-pages reported success with `pages_build_version` = the source.

## Check 2: the live page — PASS

`curl -sS --compressed 'https://saxton-network.github.io/site/?cb=<nonce>'` at 2026-10-13T14:07:05Z, first try: status 200, body SHA-256 `495b4b2b4e8c25335184fa994716a888bc9f0980b3196eb633110bde18351eb3`, equal to `deployableArtifactSha256`.

## Check 3: `main` — PASS

`git ls-remote origin refs/heads/main` after acceptance = `8377801ebd47f8ce1ec96eac9bd807dc5a876273`, unchanged.

## Observations

- `actions/upload-pages-artifact@v5.0.0` uses `actions/upload-artifact` by commit `bbbca2dd…`; the runner's git was 2.55.0 and Python 3.12.15.
- No rollback was needed. V stays unused.
