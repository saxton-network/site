# Task R: release readiness

- **Prerequisites:** B `passed`, P `complete` (and `main` merged into the records branch).
- **Read-only** with respect to `main`, Pages and settings. All gate checks use the alpha.13 helper at the source.

## Checks

As `PLAN.md` "Readiness checks (R)":

- source equals `origin/main` (non-shallow, no inherited `GIT_*`); `validate.sh` passes at the source in a clean worktree; Validate CI green;
- `deploy.yml`, `check-site.py`, `projects.txt` and `validate.sh` byte-identical between v1 and the source;
- `deploy.yml`'s guard and site check, run locally in a full clone with `origin/main` at the source, pass for v1 and the source; a merged side-branch commit is rejected;
- both listed repositories public (authenticated `private`/`visibility`; channel recorded);
- baseline: live page 200 with v1's SHA-256; the `deploy.yml` run IDs; the `github-pages` deployment IDs;
- `site/index.html` at the source hashes to `1f60283e1c442f0fd8e0015787c84febd2b37eabfe83bc9dbea54e7b345f7a35` (decision 2(a));
- the records branch, after P's merge, contains the source: `merge-base --is-ancestor <source> <records head>` exits 0;
- record `gitDivergence` with `identical: true` and `authoritySha` = `otherSha` = the source; read the helper's SHA-256 from the file (expected `67fa523b…4434`), never type it.

## Frozen batch

Exactly as `PLAN.md` lists it, with `scripts/projects.txt` among the validators, validators hashed at the source, and the `agent-work/site-upgrade/results/R-*` files committed before hashing. Record the helper SHA-256 (`67fa523b…4434`). Fingerprint with `batch_fingerprint` from the source helper.

## Result

`results/R.md`, `R-dispatch-inputs.json`, `R-rollback-inputs.json`, `R-rollback-v1.md`, `R-baseline.json`.

## Records

Hand the result content to the coordinator. Only the coordinator commits to `pilot/site-upgrade-records`.

## Forbidden

Dispatching; changing `main` or settings.

## Stop boundary

Stop at the end of this task and hand the result to the coordinator. Do not start another task.
