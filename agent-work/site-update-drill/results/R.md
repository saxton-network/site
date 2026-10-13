# Task R: release readiness

Performed by the coordinator on 2026-10-13. Read-only with respect to `main`, Pages and settings.

**Verdict: PASS**

- Source (v2): `8f3c310876166dc0cb2864dff3646e18830b1758`
- Frozen batch fingerprint: `d2a53d23b197f1bc5a80e8c95c9970c6508c766798b50df0f4427d6863542726`, computed with `batch_fingerprint` from `scripts/agent-task.py` at the source

## Checks

| Check | Result |
| --- | --- |
| `origin/main` equals the source | PASS. After `git fetch origin`, `git --no-replace-objects -c core.commitGraph=false rev-parse origin/main` (every inherited `GIT_*` variable removed) printed the source. `gitDivergence` is `identical: true`. |
| `validate.sh` at the source | PASS. Clean detached worktree at the source (empty `git status --short`); `PASS: repository validation`. |
| Validate CI on the source | PASS. Run 38412926225 (push to `main`, `head_sha` = source) and run 38411804568 (`pilot/site-update-drill-impl`), both `success`. |
| Content only | PASS. `git diff --name-only 8377801 8f3c310`, outside `agent-work/`, lists only `site/index.html`. `deploy.yml` `45fd7396…0073e`, `check-site.py` `98bd656d…0a2d5`, `validate.sh` `f9f79783…80472` and `agent-task.py` `c7f5e5ed…00655` are identical at v1 and the source. |
| v1 deployable | PASS. In a fresh, non-shallow clone with `origin/main` fetched from GitHub (`8f3c310`, 28 commits), `deploy.yml`'s guard (40-hex check; `git rev-list --first-parent origin/main \| grep -qx`; checkout; `site/` holds only `index.html`; `check-site.py`) passes for v1 (`HEAD=8377801…`, index `495b4b2b…51eb3`) and for the source (`HEAD=8f3c310…`, index `1f60283e…f7a35`). Negative control: `d907b5d`, from the merged records side branch, is rejected. A first attempt from the session's shallow clone could not see the history and failed; it was not a real result. |
| Listed repositories are public | PASS. Channel: the session's authenticated GitHub connection (`search_repositories` for the organisation, full objects, 22 of 22 read). `saxton-network/workflow` and `saxton-network/chudley`: `private: false`, `visibility: public`. |
| Deploy runs | `deploy.yml` has one run, 38410452425 (v1). |
| Baseline | `curl -sS --compressed 'https://saxton-network.github.io/site/?cb=<nonce>'` at 2026-10-13T14:24:17Z: status 200, SHA-256 `495b4b2b4e8c25335184fa994716a888bc9f0980b3196eb633110bde18351eb3` (v1). |
| Injected fault, local proof | PASS. Expected v2 hash `1f60283e…f7a35` ≠ injected `0000…0000` (64 zeros); the v1 baseline equals neither. So 2a can pass only on real v2 bytes and 2b fails on any real page. |
| Pages enablement | Accepted unknown 2, proven in practice by run 38410452425. |
| Local git | `git version 2.43.0`. |

## Frozen batch

- `deploymentSourceSha`: `8f3c310876166dc0cb2864dff3646e18830b1758`
- `deployableArtifactSha256`: `1f60283e1c442f0fd8e0015787c84febd2b37eabfe83bc9dbea54e7b345f7a35`, `site/index.html` at the source
- `deploymentConfiguration`: `.github/workflows/deploy.yml` (at the source); `results/R-dispatch-inputs.json`, `results/R-rollback-inputs.json`, `results/R-expected-sha256.txt`, `results/R-expected-sha256-INJECTED.txt` and `CONTRACT.md` (records branch). Hashes in `evidence.json`.
- `validators` (at the source): `scripts/check-site.py`, `scripts/validate.sh`, `scripts/agent-task.py`
- `installedScripts`: none
- `rollbackArtifact`: `git:8377801ebd47f8ce1ec96eac9bd807dc5a876273`, provenance `results/R-rollback-v1.md`
- `deploymentTargets` (mode `null`): `https://saxton-network.github.io/site`
