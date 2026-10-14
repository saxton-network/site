# Task R: release readiness

Performed by the coordinator on 2026-10-14. Read-only with respect to `main`, Pages and settings. All gate checks use the alpha.14 helper at the source.

**Verdict: PASS**

- Source: `dfaa7cb863da02c204b34c4e05d90d9f9660fe97`
- Frozen batch fingerprint: `82cfa32b80c6ada17cab1535b04c645544c4a3b69a0c1d66575b7b623d39e0cb`, computed with `batch_fingerprint` from `scripts/agent-task.py` at the source. Its SHA-256, read from the file, is `8ec1b22cd97d10e1873ed9dfa83a37fa58f036914452f1af6508564215748f3c`.

## Checks

| Check | Result |
| --- | --- |
| `origin/main` equals the source | PASS. Fresh, non-shallow clone. Every inherited `GIT_*` variable was removed; a count inside printed 0. `git --no-replace-objects -c core.commitGraph=false rev-parse origin/main` printed the source. `gitDivergence` is `identical: true`. |
| `validate.sh` at the source | PASS, in a clean detached worktree (empty `git status --porcelain`). |
| Validate CI on the source | PASS. Run 38533146185 (push to `main`, `head_sha` = source) is `success`. The connection read it; `curl` read the same and agrees. |
| Deploy code unchanged since v1 | PASS. These four files are byte-identical at v1 and the source: `deploy.yml` `45fd7396…0073e`, `check-site.py` `98bd656d…0a2d5`, `projects.txt` `4bca413c…f949f7` and `validate.sh` `f9f79783…80472`. |
| v2 | PASS. `site/index.html` at the source: `1f60283e1c442f0fd8e0015787c84febd2b37eabfe83bc9dbea54e7b345f7a35`. |
| Rollback proven (local guard) | PASS. A script mirroring `deploy.yml`'s steps ran under `bash -e` in the same full clone, with `origin/main` at the source. v1 exits 0, giving `DEPLOY HEAD=8377801…` and `DEPLOY INDEX_SHA256=495b4b2b…51eb3`. The source exits 0, giving `DEPLOY HEAD=dfaa7cb…` and `DEPLOY INDEX_SHA256=1f60283e…f7a35`. The negative check `07236894c4a6f5609861176f678deb34baff996e`, a merged side-branch commit, is rejected with exit 1. |
| Records branch contains the source | PASS. With no inherited `GIT_*`, the hardened `merge-base --is-ancestor dfaa7cb… <records head>` exits 0. |
| Listed repositories are public | PASS through the connection (organisation repository search, full objects): `saxton-network/workflow` and `saxton-network/chudley` both show `private: false`, `visibility: public`. `curl` agrees for the workflow repository. For the other repository, the session's proxy refuses `curl` API reads outside this session's repository scope (403). That fallback is recorded as "no fallback", as the plan allows. |
| Evidence access | PASS. Every acceptance row has a working primary and fallback; see below. |
| Dispatch client | The connection's Actions run-trigger tool, for dispatch and cancel, is available and was not used. The connection acts as the owner's GitHub account, the account that made the earlier dispatches. |
| Baseline | The live page at 2026-10-14T08:10:50Z returns 200 with SHA-256 `495b4b2b…51eb3` (v1). There are 5 `deploy.yml` runs and 5 `github-pages` deployments; their IDs are in `R-baseline.json`. |
| Local git | `git version 2.43.0`. |

## Evidence access (on run 38513444503 and the live page)

| Item | Primary | Fallback | Agree |
| --- | --- | --- | --- |
| Run: `head_sha`, `run-name`, conclusion | connection: `95914a5…`, `Deploy 8377801…`, `success` | `curl` (Actions API): the same | yes |
| Run list | connection: 5 runs | `curl`: 5 runs, same IDs | yes |
| Job-step list | connection: 12 steps; `Run actions/deploy-pages@v5.0.1` `success` | `curl`: the same | yes |
| Job log `DEPLOY` lines | connection (job logs, line limit 2000): 372 lines, header `Complete job name:` present, output lines `DEPLOY HEAD=8377801…` and `DEPLOY INDEX_SHA256=495b4b2b…` | `curl` (job-logs API, one redirect, HTTP 200): 372 lines, the same header and output lines | yes |
| Live page bytes and status | `curl --compressed` with a cache-busting query: 200, v1 | none | — |
| `github-pages` deployment IDs | `curl` (deployments API): 5 | none | — |
| `refs/heads/main` | `git ls-remote`: `dfaa7cb…` | `curl` (git refs API): `dfaa7cb…` | yes |
| Validate CI on the source | connection: run 38533146185 `success` | `curl`: the same | yes |

- **Authentication.** The connection is the session's authenticated GitHub connection. `curl` goes through the session's proxy, which authenticates it as the same account: `/user` returns the same login, the rate limit is 15,000 per hour, and 14,985 requests remained. So the fallback is a different program and request path, not a different identity.
- **404 is evidence.** A missing job log answers 404 through `curl`.
- **What was kept.** Only the two `DEPLOY` output values were kept from the logs. No token, header, redirect URL or raw log is recorded.

## Frozen batch

- `deploymentSourceSha`: `dfaa7cb863da02c204b34c4e05d90d9f9660fe97`
- `deployableArtifactSha256`: `1f60283e1c442f0fd8e0015787c84febd2b37eabfe83bc9dbea54e7b345f7a35`
- `deploymentConfiguration`:
  - `.github/workflows/deploy.yml`, read at the source: `45fd7396…0073e`
  - `results/R-dispatch-inputs.json`: `f6af6225…381427`
  - `results/R-rollback-inputs.json`: `927b8539…4650a`
  - `CONTRACT.md`: `fac424c9…74276a`

  The last three are on the records branch and were committed in `84b73f4` before hashing. The full hashes are in `evidence.json`.
- `validators`, read at the source: `scripts/check-site.py`, `scripts/projects.txt`, `scripts/validate.sh` and `scripts/agent-task.py`
- `installedScripts`: none
- `rollbackArtifact`: `git:8377801ebd47f8ce1ec96eac9bd807dc5a876273`, provenance `results/R-rollback-v1.md`
- `deploymentTargets`: `https://saxton-network.github.io/site`, mode `null`
