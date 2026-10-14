# Task A: upgrade the vendored Workflow files

- **Prerequisites:** none.
- **Base:** `16c363137b52093fcd014ee00d8c4a8ca570e658` (`main`).
- **Branch:** `pilot/site-upgrade-14-impl`, in its own worktree. Before the first commit, check `git config user.name` and `user.email` against `AGENTS.md`.
- **Read first:** `AGENTS.md`, `ADOPTION.md`, `PLAN.md` "What changes", and Workflow's `docs/ADOPTING.md` sections 2 and 3.

## Work

1. **Download the release.** Download `workflow-v0.1.0-alpha.14.zip` from the published release. Its SHA-256 must be `1b87fa4a7034e58efaf0c8479b93bb82d4d3bad2c8fb3b467da4f27627d98355`. Confirm that the tag `v0.1.0-alpha.14` is a lightweight ref at `02c771a7c7d71e2303c186d0c150e903a524e949`.
2. **Copy the eight vendored files** from the unpacked ZIP. Each must also equal `git show 02c771a:<path>`.
   - Five are expected to change: `agent-work/WORKFLOW-SPEC.md`, `agent-work/COORDINATOR.md`, `agent-work/RESULT-TEMPLATE.md`, `docs/THREAT-MODEL.md` and `scripts/agent-task.py`.
   - The other three are expected to be byte-identical.
3. **Update `ADOPTION.md`** as `PLAN.md` describes:
   - the header keeps the history (`3d38b27`, then alpha.13, then alpha.14);
   - all eight rows, in the four-column form, carry commit `02c771a…` and the new hashes;
   - the "Copied files" sentence names `02c771a`;
   - "Upgrades" gains a second, prose-only entry. No backticked 64-hex value may appear in a table row that starts with a backtick.
4. **Reword the "Git identity" bullet in `AGENTS.md`** to exactly the text in `PLAN.md` (decision 2(a)).
5. **Change nothing else.** `site/index.html` stays v2.

## Validation

- `bash scripts/validate.sh` passes with the new helper, including the three existing workflows.
- `git diff --name-only 16c3631 <candidate>` lists only the five vendored files, `ADOPTION.md` and `AGENTS.md`.
- Validate CI is green on the pushed candidate.

## Result

`results/A.md`: the candidate, the ZIP and tag checks, the changed paths with old and new hashes, and the checks.

## Records

Hand the result content to the coordinator. Only the coordinator commits to `pilot/site-upgrade-14-records`.

## Forbidden

- Any file other than the eight vendored files, `ADOPTION.md` and `AGENTS.md`.
- Deploying or dispatching.
- Changing settings.

## Stop boundary

Stop at the end of this task and hand the result to the coordinator. Do not start another task.
