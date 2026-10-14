# Rollback artifact: git:8377801ebd47f8ce1ec96eac9bd807dc5a876273 (v1)

- **Identity:** `git:8377801ebd47f8ce1ec96eac9bd807dc5a876273`, the commit `site-launch` deployed and `site-update-drill` restored.
- **v1 `site/index.html` SHA-256:** `495b4b2b4e8c25335184fa994716a888bc9f0980b3196eb633110bde18351eb3`.
- **v1 deploy evidence:**
  - `agent-work/site-launch/results/J.md`: run 38410452425, `DEPLOY HEAD=8377801…`, `DEPLOY INDEX_SHA256=495b4b2b…51eb3`, live bytes equal;
  - `agent-work/site-update-drill/results/V.md`: run 38416947644 redeployed v1 with the same `deploy.yml`, and the live bytes equalled v1.
- **Live now:** the baseline in `R-baseline.json` (2026-10-14T04:33:38Z) is v1.
- **Deployable by the same code:** `.github/workflows/deploy.yml`, `scripts/check-site.py`, `scripts/projects.txt` and `scripts/validate.sh` are byte-identical between v1 and the source (only the vendored helper changed). v1 is the fifth commit on the source's first-parent line, and `deploy.yml`'s guard and site check pass for v1 when run locally with `origin/main` at the source (`R.md`).
- **How it is restored:** in task V, one dispatch of `deploy.yml` on `main` with `results/R-rollback-inputs.json`, under the condition in `CONTRACT.md` "Rollback (V)".
