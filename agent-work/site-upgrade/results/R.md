# Task R: release readiness

Performed by the coordinator on 2026-10-14. Read-only with respect to `main`, Pages and settings.

**Verdict: PASS**

- Source: `95914a54336983fc48e286b8e16cb6780076d2f2` (task A's candidate, passed by B-1, promoted by P)
- Frozen batch fingerprint: `fcbe26fca2a95d6bcc621dbf27dd27b53eef7bc263c06e254f7404b8a2e1f33d`, computed with `batch_fingerprint` from `scripts/agent-task.py` at the source (SHA-256 read from the file: `67fa523bd62cf21ad53d969460074982baff1f5b5e1312a086b953e0138f4434`)

## Checks

| Check | Result |
| --- | --- |
| `origin/main` equals the source | PASS. In a fresh, non-shallow clone from GitHub (40 commits on `origin/main`), `git --no-replace-objects -c core.commitGraph=false rev-parse origin/main`, with every inherited `GIT_*` variable removed, printed the source. `gitDivergence` is `identical: true`. |
| `validate.sh` at the source | PASS. Clean detached worktree at the source (empty `git status --short`); `PASS: repository validation`. |
| Validate CI on the source | PASS. Run 38511817666 (push to `main`, `head_sha` = source) and run 38511384398 (`pilot/site-upgrade-impl`), both `success`. |
| Content only, apart from the upgrade | PASS. `deploy.yml` `45fd7396…0073e`, `check-site.py` `98bd656d…0a2d5`, `projects.txt` `4bca413c…f949f7` and `validate.sh` `f9f79783…80472` are byte-identical at v1 and the source. `git diff --name-only 8377801 95914a5`, outside `agent-work/`, lists `ADOPTION.md`, `docs/THREAT-MODEL.md`, `scripts/agent-task.py` (the upgrade) and `site/index.html` (v1 to v2). |
| v2 page | PASS. `site/index.html` at the source: `1f60283e1c442f0fd8e0015787c84febd2b37eabfe83bc9dbea54e7b345f7a35`, decision 2(a). |
| Rollback proven (local guard) | PASS. In the same full clone, with `origin/main` fetched at the source, a script mirroring `deploy.yml`'s steps (40-hex check; fetch of `main`; `git rev-list --first-parent origin/main \| grep -qx`; detached checkout; `site/` holds only `index.html`; `check-site.py`; the two `DEPLOY` lines), run under `bash -e` like the runner's default shell: v1 exit 0 with `DEPLOY HEAD=8377801…` and `DEPLOY INDEX_SHA256=495b4b2b…51eb3`; the source exit 0 with `DEPLOY HEAD=95914a5…` and `DEPLOY INDEX_SHA256=1f60283e…f7a35`. Negative control: `07236894c4a6f5609861176f678deb34baff996e`, a commit from the merged `site-update-drill` records side branch, is reachable from `main` but not on its first-parent line; it was rejected with exit 1 ("not on main's first-parent history"). |
| Records branch contains the source | PASS. On `pilot/site-upgrade-records` at `76ebfcd`, non-shallow, every inherited `GIT_*` variable removed, `GIT_GRAFT_FILE=/dev/null git --no-replace-objects -c core.commitGraph=false merge-base --is-ancestor 95914a5… HEAD` exited 0. |
| Listed repositories are public | PASS. Channel: the session's authenticated GitHub connection (`search_repositories`, full objects, both repositories in `scripts/projects.txt` returned). `saxton-network/workflow` and `saxton-network/chudley`: `private: false`, `visibility: public`. |
| Baseline: live page | `curl -sS --compressed 'https://saxton-network.github.io/site/?cb=<nonce>'` at 2026-10-14T04:33:38Z: status 200, SHA-256 `495b4b2b4e8c25335184fa994716a888bc9f0980b3196eb633110bde18351eb3` (v1). |
| Baseline: deploy runs | `deploy.yml` has 3 runs: 38410452425 (v1 launch), 38416735077 (v2 drill), 38416947644 (v1 rollback). |
| Baseline: deployments | `GET /repos/saxton-network/site/deployments?environment=github-pages&per_page=100`, unauthenticated (the repository is public): 3 deployments, 7040675239, 7041742077, 7041777317. Their `sha` labels are `main`'s tip at dispatch, as `CONTRACT.md` "Accepted unknowns" says. |
| Pages enablement | Accepted unknown, shown in practice by the 200 baseline and the three earlier runs. |
| Local git | `git version 2.43.0`. |

`R-baseline.json` holds the baseline values.

## Frozen batch

- `deploymentSourceSha`: `95914a54336983fc48e286b8e16cb6780076d2f2`
- `deployableArtifactSha256`: `1f60283e1c442f0fd8e0015787c84febd2b37eabfe83bc9dbea54e7b345f7a35`, `site/index.html` at the source
- `deploymentConfiguration`: `.github/workflows/deploy.yml` (at the source); `results/R-dispatch-inputs.json`, `results/R-rollback-inputs.json` and `CONTRACT.md` (records branch, committed in `76ebfcd` before hashing). Hashes in `evidence.json`.
- `validators` (at the source): `scripts/check-site.py`, `scripts/projects.txt`, `scripts/validate.sh`, `scripts/agent-task.py`
- `installedScripts`: none
- `rollbackArtifact`: `git:8377801ebd47f8ce1ec96eac9bd807dc5a876273`, provenance `results/R-rollback-v1.md`
- `deploymentTargets` (mode `null`): `https://saxton-network.github.io/site`
