# Task R: release readiness

Performed by the coordinator on 2026-10-13. Read-only with respect to `main`, Pages and settings.

**Verdict: PASS**

- Source: `8377801ebd47f8ce1ec96eac9bd807dc5a876273`
- Frozen batch fingerprint: `23142a14e4f5434621d9362c31934b0c4519e8f7240fc7e333cce12885eed71a`, computed with `batch_fingerprint` from `scripts/agent-task.py` at the source

## Checks

| Check | Result |
| --- | --- |
| `origin/main` equals the source | PASS. After `git fetch origin`, `git --no-replace-objects -c core.commitGraph=false rev-parse origin/main` (every inherited `GIT_*` variable removed) printed the source. `gitDivergence` is `identical: true`. |
| `validate.sh` at the source | PASS. Run in a clean detached worktree at the source; exit 0, with `PASS: site check (2 repositories listed)` and `PASS: repository validation`. |
| Validate CI on the source | PASS. Run 38406646291 (push to `main`, `head_sha` = source), conclusion `success`. Also run 38406090715 on `pilot/site-launch-fix`. |
| Listed repositories are public | PASS. Channel: the session's authenticated GitHub connection (`search_repositories` for the organisation, full repository objects). `saxton-network/workflow`: `private: false`, `visibility: public`. `saxton-network/chudley`: `private: false`, `visibility: public`. |
| No earlier deploy runs | PASS. `deploy.yml` has zero runs, so the J run is the first. |
| Baseline | `curl -sS --compressed 'https://saxton-network.github.io/site/?cb=<nonce>'` at 2026-10-13T13:39:28Z: status 404. Nothing is published. |
| Pages enablement | Accepted unknown 2. The owner turned on Source "GitHub Actions" and confirmed it with a screenshot (`pages-enable.md`). |
| Tools | Run read: proven (`actions_list`, `actions_get`). Dispatch and cancel: `actions_run_trigger` with `run_workflow` and `cancel_workflow_run` is present in this session's GitHub connection; neither was exercised, as both act on live state. Unpublish: no tool; the owner does it. |
| Local git | `git version 2.43.0`. |

## Frozen batch

- `deploymentSourceSha`: `8377801ebd47f8ce1ec96eac9bd807dc5a876273`
- `deployableArtifactSha256`: `495b4b2b4e8c25335184fa994716a888bc9f0980b3196eb633110bde18351eb3`, which is `site/index.html` at the source, the only file the deploy publishes
- `deploymentConfiguration`:
  - `.github/workflows/deploy.yml` (at the source) `45fd739663807a7cf325c18ecb57b31ff20decf1d4b61a9a05155a12e800073e`
  - `agent-work/site-launch/results/R-dispatch-inputs.json` (records branch) `927b8539ce464e5e7cd1c65b1b1d720f9b2ce972f2f2d39ce52744e8e054650a`
  - `agent-work/site-launch/CONTRACT.md` (records branch) `e05c5dd7f929ce60ec4fb4a839991453048d95bde14b131a26c52f3bfd5d1e1b`
- `validators` (at the source):
  - `scripts/check-site.py` `98bd656dd3d8c22341cc18ce6e4e9d209dc418583f1bc1b58e08d18fd5e0a2d5`
  - `scripts/validate.sh` `f9f79783f5b37cf776cad75328a65d954fb814c26f4e2443ad590c5027e80472`
  - `scripts/agent-task.py` `c7f5e5ed29334f0b991cf183cc5ba9e013bff2b49c099cd2c9d7aa8e09d00655`
- `installedScripts`: none
- `rollbackArtifact`: `pages-unpublished-404`, provenance `R-rollback.md`
- `deploymentTargets` (mode `null`): `https://saxton-network.github.io/site`

## Plan note

`PLAN.md` "Readiness" says an unauthenticated GET proves a repository public. `R-readiness.md`, written later after the session proxy returned 403 for an unauthenticated read, allows an authenticated read of the `private`/`visibility` field. This check followed the task file.
