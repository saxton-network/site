# Rollback artifact: git:8377801ebd47f8ce1ec96eac9bd807dc5a876273 (v1)

- **Identity:** `git:8377801ebd47f8ce1ec96eac9bd807dc5a876273`, the commit `site-launch` deployed.
- **v1 `site/index.html` SHA-256:** `495b4b2b4e8c25335184fa994716a888bc9f0980b3196eb633110bde18351eb3`.
- **v1 deploy evidence:** `agent-work/site-launch/results/J.md` (run 38410452425, `DEPLOY HEAD=8377801…`, `DEPLOY INDEX_SHA256=495b4b2b…51eb3`, live bytes equal). The live baseline in `R.md` (2026-10-13T14:24:17Z) is still v1.
- **Deployable by the same code:** `.github/workflows/deploy.yml` and every script are byte-identical between v1 and the source. v1 is the third commit on the source's first-parent line, and `deploy.yml`'s guard and site check pass for v1 when run locally with `origin/main` at the source (`R.md`).
- **How it is restored:** in task V, one dispatch of `deploy.yml` on `main` with `results/R-rollback-inputs.json`, under the condition in `CONTRACT.md` "Rollback (V)".
