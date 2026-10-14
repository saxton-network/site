# Agent task result: site-upgrade / A

- **Candidate:** `95914a54336983fc48e286b8e16cb6780076d2f2` on `pilot/site-upgrade-impl`, a child of `ae90609`.
- **Builder:** the coordinator's model, acting as builder. Review is by a different model.

## Source checks

- `workflow-v0.1.0-alpha.13.zip` downloaded from the published release: SHA-256 `e520b61c3c48572b73001d333b2c79499e33b3e5c19f34988d5be2f3e191d5d4`, equal to the expected digest.
- `git ls-remote` shows `refs/tags/v0.1.0-alpha.13` at `84d826a40b8f8567439ab15eb270a1a752f92a82` with no peeled line (a lightweight tag).
- Every vendored file copied from the unpacked ZIP is byte-identical to `git show 84d826a:<path>`.

## Files

| Path | Before | After |
| --- | --- | --- |
| `agent-work/WORKFLOW-SPEC.md` | `6f902673…861f50b` | `7ba45449…a8f1ffc` |
| `agent-work/COORDINATOR.md` | `9123a28c…177e33d` | `7a9c98d9…0a143f04` |
| `agent-work/EVIDENCE-MANIFEST.md` | `0fd36155…e76735c46` | `c43b0120…fe514242` |
| `docs/THREAT-MODEL.md` | `c9553193…86f4eb4ef` | `132d933a…e061bf80fb1` |
| `scripts/agent-task.py` | `c7f5e5ed…9d00655` | `67fa523b…138f4434` |

`agent-work/README.md`, `agent-work/RESULT-TEMPLATE.md` and `docs/agent-worktrees.md` are byte-identical to the earlier copies.

`ADOPTION.md`:

- The header keeps the adoption at `3d38b27` and adds the upgrade.
- All eight rows keep the four-column form, with commit `84d826a`; the five changed rows have their new hashes.
- `docs/ADOPTING.md` is added to "Files not copied", and the reason for the pilot-history row is updated.
- A prose "Upgrades" section records the source checks, the file changes and the procedure. It also sorts the 21 ambiguities into answered (1, 2, 3, 4, 5, 7, 9, 11, 16, 17, 20, 21), partly answered (6, 10) and not answered (8, 12, 13, 14, 15, 18, 19), and records the row-format difference.

`git diff --name-only ae90609 95914a5` lists only `ADOPTION.md` and the five changed files. `site/index.html` is unchanged: SHA-256 `1f60283e1c442f0fd8e0015787c84febd2b37eabfe83bc9dbea54e7b345f7a35`, v2.

## Checks

- `bash scripts/validate.sh` passes with the new helper: 8 hashes, the site check, and all three manifests. The labels for `site-launch` and `site-update-drill` are unchanged.
- Validate CI run 38511384398 on the candidate: success.

## Finding during the task

The plan said ambiguity 7 no longer applies; it does still apply, but is now answered. This is recorded as a dated plan clarification.
