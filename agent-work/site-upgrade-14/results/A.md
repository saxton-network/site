# Agent task result: site-upgrade-14 / A

- **Candidate:** `dfaa7cb863da02c204b34c4e05d90d9f9660fe97` on `pilot/site-upgrade-14-impl`, a child of `16c3631`.
- **Builder:** the coordinator's model, acting as builder. Review is done by a different model.
- **Identity:** checked before the commit; the commit uses the mandated no-reply identity.

## Source checks

- **The ZIP.** `workflow-v0.1.0-alpha.14.zip` was downloaded from the published release. Its SHA-256 is `1b87fa4a7034e58efaf0c8479b93bb82d4d3bad2c8fb3b467da4f27627d98355`, equal to the expected digest.
- **The tag.** `git ls-remote` shows `refs/tags/v0.1.0-alpha.14` at `02c771a7c7d71e2303c186d0c150e903a524e949` with no peeled line, so it is a lightweight tag.
- **The files.** Every vendored file copied from the unpacked ZIP is byte-identical to `git show 02c771a:<path>`.

## Files

| Path | Before | After |
| --- | --- | --- |
| `agent-work/WORKFLOW-SPEC.md` | `7ba45449…3a8f1ffc` | `3c3b24ed…84df9097` |
| `agent-work/COORDINATOR.md` | `7a9c98d9…0a143f04` | `1ac891f2…b0591336` |
| `agent-work/RESULT-TEMPLATE.md` | `9c8dd149…92fd585b` | `680df22f…6492f694` |
| `docs/THREAT-MODEL.md` | `132d933a…1bf80fb1` | `7ac9c1a5…577cf533` |
| `scripts/agent-task.py` | `67fa523b…138f4434` | `8ec1b22c…15748f3c` |

`agent-work/README.md`, `agent-work/EVIDENCE-MANIFEST.md` and `docs/agent-worktrees.md` are byte-identical to the earlier copies.

`ADOPTION.md`:

- **Header:** it keeps the history (`3d38b27`, alpha.13) and adds alpha.14.
- **Rows and "Copied files":** all eight rows keep the four-column form with commit `02c771a`, and the five changed rows have their new hashes. The "Copied files" sentence names `02c771a`.
- **Upgrades:** a second prose entry records the source checks, the file changes, the `AGENTS.md` change, and notes on ambiguity 17, the row format and evidence access.
- **Stale references:** `84d826a` remains only in the history text (the header and the first Upgrades entry).

`AGENTS.md`: the "Git identity" bullet is replaced with the decision 2(a) text, byte for byte as quoted in `PLAN.md`. Nothing else in the file changed.

`git diff --name-only 16c3631 dfaa7cb` lists exactly the five vendored files, `ADOPTION.md` and `AGENTS.md`. `site/index.html` is unchanged at v2, SHA-256 `1f60283e1c442f0fd8e0015787c84febd2b37eabfe83bc9dbea54e7b345f7a35`.

## Checks

- `bash scripts/validate.sh` passes with the new helper. That covers the 8 hashes, the site check and all four manifests. The labels of the three earlier workflows are unchanged.
- Validate CI run 38532711153 on the candidate: success.
