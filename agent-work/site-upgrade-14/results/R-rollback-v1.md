# Rollback artifact: git:8377801ebd47f8ce1ec96eac9bd807dc5a876273 (v1)

- **Identity:** `git:8377801ebd47f8ce1ec96eac9bd807dc5a876273`. This is the commit `site-launch` deployed, and the one `site-update-drill` and `site-upgrade` restored.
- **v1's `site/index.html` SHA-256:** `495b4b2b4e8c25335184fa994716a888bc9f0980b3196eb633110bde18351eb3`.
- **Latest v1 deploy evidence:** run 38513444503 (`site-upgrade` V). Its job log, read in this readiness through both the connection and `curl`, shows `DEPLOY HEAD=8377801…` and `DEPLOY INDEX_SHA256=495b4b2b…51eb3`. The live baseline in `R-baseline.json` (2026-10-14T08:10:50Z) is v1.
- **Deployable by the same code:**
  - `.github/workflows/deploy.yml`, `scripts/check-site.py`, `scripts/projects.txt` and `scripts/validate.sh` are byte-identical between v1 and the source.
  - v1 is eighth on the source's first-parent line.
  - `deploy.yml`'s guard and site check pass for v1 when run locally with `origin/main` at the source (`R.md`).
- **How it is restored:** in task V, by one dispatch of `deploy.yml` on `main` with `results/R-rollback-inputs.json`, under the condition in `CONTRACT.md` "Rollback (V)".
