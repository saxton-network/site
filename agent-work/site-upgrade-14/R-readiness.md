# Task R: release readiness

- **Prerequisites:** B `passed`; P `complete`, with `main` merged into the records branch.
- **Read-only** with respect to `main`, Pages and settings. All gate checks use the alpha.14 helper at the source.

## Checks

As `PLAN.md` "Readiness checks (R)" lists them:

- **The source.**
  - It equals `origin/main` (non-shallow clone, no inherited `GIT_*`).
  - `validate.sh` passes at the source in a clean worktree.
  - Validate CI is green.
- **Deploy code unchanged since v1.** `deploy.yml`, `check-site.py`, `projects.txt` and `validate.sh` are byte-identical between v1 and the source.
- **The local guard proof.** `deploy.yml`'s guard and site check are run locally, in a full clone with `origin/main` at the source. They pass for v1 and for the source. A merged side-branch commit is rejected.
- **Listed repositories.** Both are public, read through the authenticated `private`/`visibility` fields.
- **Evidence access.** Every row of `CONTRACT.md` "Evidence clients" is proven, on deploy run 38513444503 (the v1 rollback) and the live page:
  - the primary client is read;
  - the fallback is read too, where the table lists one, and the two must agree;
  - a 404 counts as evidence;
  - a fallback that does not work is recorded as "no fallback".
  
  Record how each client authenticates. Check that the dispatch and cancel tool is available, without using it. Record only client names, the identity kind and the two `DEPLOY` output values; never record tokens, headers, signed URLs or raw logs.
- **The baseline.**
  - The live page: 200, with v1's SHA-256.
  - The `deploy.yml` run IDs: 5 runs.
  - The `github-pages` deployment IDs: 5.
- **v2.** `site/index.html` at the source hashes to `1f60283e1c442f0fd8e0015787c84febd2b37eabfe83bc9dbea54e7b345f7a35`.
- **The records branch.** After P's merge, it contains the source: `merge-base --is-ancestor <source> <records head>` exits 0.
- **`gitDivergence`.** Record it with `identical: true`, and `authoritySha` = `otherSha` = the source.
- **The helper.** Read its SHA-256 from the file, never type it. The expected value is `8ec1b22c…748f3c`.

## Frozen batch

Freeze the batch exactly as `PLAN.md` lists it:

- `scripts/projects.txt` is among the validators, and the validators are hashed at the source;
- the `agent-work/site-upgrade-14/results/R-*` files are committed before hashing;
- the fingerprint is computed with `batch_fingerprint` from the source helper.

## Result

- `results/R.md`
- `R-dispatch-inputs.json`
- `R-rollback-inputs.json`
- `R-rollback-v1.md`
- `R-baseline.json`

## Records

Hand the result content to the coordinator. Only the coordinator commits to `pilot/site-upgrade-14-records`.

## Forbidden

Dispatching; changing `main` or settings.

## Stop boundary

Stop at the end of this task and hand the result to the coordinator. Do not start another task.
