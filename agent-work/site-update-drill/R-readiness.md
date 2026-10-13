# Task R: release readiness

- **Prerequisites:** B `passed`, P `complete`.
- **Read first:** `AGENTS.md`, `PLAN.md` "Readiness" and "Workflow 2", `CONTRACT.md`.
- **Read-only** with respect to `main`, Pages and settings.

## Checks

- **Source and gate:**
  - `origin/main` equals the source (`gitDivergence` `identical: true`);
  - Validate CI is green on the source;
  - `bash scripts/validate.sh` passes at the source in a clean worktree.
- **Content only:** `git diff --name-only 8377801ebd47f8ce1ec96eac9bd807dc5a876273 <source>` lists only `site/index.html` and paths under `agent-work/`; `.github/workflows/deploy.yml` and every validator hash equal v1's.
- **v1 deployable:** v1 is on the source's first-parent history.
- **Listed repositories are public:** read each repository's `private`/`visibility` field from GitHub's API. An authenticated call is fine. A 403 from the session proxy, or any response without that field, is a failed probe, never a pass. Record the channel used.
- **Baseline:** the live page, fetched with `curl -sS --compressed '<url>?cb=<nonce>'`: status 200 and SHA-256 equal to v1's hash. The `deploy.yml` run list (only run 38410452425 expected).
- **Injected fault, proven locally:** the real v2 hash and the injected value (64 zeros) differ, and the live baseline (v1) equals neither.

## Frozen batch

- `deploymentSourceSha`: the source.
- `deployableArtifactSha256`: the SHA-256 of `site/index.html` at the source.
- `deploymentConfiguration`:
  - `.github/workflows/deploy.yml`
  - `agent-work/site-update-drill/results/R-dispatch-inputs.json`
  - `agent-work/site-update-drill/results/R-rollback-inputs.json`
  - `agent-work/site-update-drill/results/R-expected-sha256.txt`
  - `agent-work/site-update-drill/results/R-expected-sha256-INJECTED.txt`
  - `agent-work/site-update-drill/CONTRACT.md`
- `validators`, at the source:
  - `scripts/check-site.py`
  - `scripts/validate.sh`
  - `scripts/agent-task.py`
- `installedScripts`: none.
- `rollbackArtifact`: identity `git:8377801ebd47f8ce1ec96eac9bd807dc5a876273`, provenance `agent-work/site-update-drill/results/R-rollback-v1.md` (v1's `index.html` SHA-256 and v1's deploy evidence).
- `deploymentTargets`: `https://saxton-network.github.io/site`, with mode `null`.

## Result

`results/R.md` and the frozen files above.

## Records

Hand the result content to the coordinator. Only the coordinator commits to `pilot/site-update-drill-records`; nothing under `agent-work/site-update-drill/` is committed to the implementation branch.

## Forbidden

Dispatching, changing `main`, changing settings.

## Stop boundary

Stop at the end of this task and hand the result to the coordinator. Do not start another task.
