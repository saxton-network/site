# Task R: release readiness

- **Prerequisites:** B `passed`, P `complete`.
- **Read first:** `AGENTS.md`, `PLAN.md` "Readiness", `CONTRACT.md`.
- **Read-only** with respect to `main`, Pages and settings.

## Checks

- **Source and gate:**
  - `origin/main` equals the source (`gitDivergence` `identical: true`);
  - Validate CI is green on the source;
  - `bash scripts/validate.sh` passes at the source in a clean worktree.
- **Listed repositories are public:** an unauthenticated GET of each returns 200 with `private: false`.
- **Baseline:** the live page status, fetched with `curl -sS --compressed '<url>?cb=<nonce>'`. Before launch it is "status 404" only.
- **Pages enablement:** recorded as accepted unknown 2, with the owner's confirmation.

## Frozen batch

- `deploymentSourceSha`: the source.
- `deployableArtifactSha256`: the SHA-256 of `site/index.html` at the source.
- `deploymentConfiguration`:
  - `.github/workflows/deploy.yml`
  - `agent-work/site-launch/results/R-dispatch-inputs.json`
- `validators`, at the source:
  - `scripts/check-site.py`
  - `scripts/validate.sh`
  - `scripts/agent-task.py`
- `installedScripts`: none.
- `rollbackArtifact`: identity `pages-unpublished-404`, provenance `agent-work/site-launch/results/R-rollback.md`.
- `deploymentTargets`: `https://saxton-network.github.io/site`, with mode `null`.

## Result

`results/R.md`, `R-dispatch-inputs.json`, `R-rollback.md`.

## Records

Hand the result content to the coordinator. Only the coordinator commits to `pilot/site-launch-records`; nothing under `agent-work/site-launch/` is committed to the implementation branch.

## Forbidden

Dispatching, changing `main`, changing settings.

## Stop boundary

Stop at the end of this task and hand the result to the coordinator. Do not start another task.
