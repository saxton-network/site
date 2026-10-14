# Task A: upgrade the vendored Workflow files

- **Prerequisites:** none.
- **Base:** `ae90609244b36f306f924bf5470f21d8cf202bb2` (`main`). **Branch:** `pilot/site-upgrade-impl`, in its own worktree.
- **Read first:** `AGENTS.md`, `ADOPTION.md`, `PLAN.md` "What changes", Workflow's `docs/ADOPTING.md` section 2.

## Work

1. Download `workflow-v0.1.0-alpha.13.zip` from the published release; its SHA-256 must be `e520b61c3c48572b73001d333b2c79499e33b3e5c19f34988d5be2f3e191d5d4`. Confirm the tag `v0.1.0-alpha.13` peels to `84d826a40b8f8567439ab15eb270a1a752f92a82`.
2. Copy the eight vendored files from the unpacked ZIP. Each must also equal `git show 84d826a:<path>`. Expected: five change (`agent-work/WORKFLOW-SPEC.md`, `agent-work/COORDINATOR.md`, `agent-work/EVIDENCE-MANIFEST.md`, `docs/THREAT-MODEL.md`, `scripts/agent-task.py`), three are byte-identical.
3. Update `ADOPTION.md` as `PLAN.md` describes: header keeps the adoption history; all eight rows in the four-column form with commit `84d826a…` and the new hashes; `docs/ADOPTING.md` added to "Files not copied", the `docs/PILOT-HISTORY.md` reason updated; a prose-only "Upgrades" section (no backticked 64-hex value in a table row starting with a backtick).
4. Change nothing else. `site/index.html` stays v2 (decision 2(a)).

## Validation

- `bash scripts/validate.sh` passes with the new helper, including both existing workflows.
- `git diff --name-only ae90609 <candidate>` lists only the five vendored files and `ADOPTION.md`.
- Validate CI is green on the pushed candidate.

## Result

`results/A.md`: the candidate, the ZIP and tag checks, the changed paths with old and new hashes, and the checks.

## Records

Hand the result content to the coordinator. Only the coordinator commits to `pilot/site-upgrade-records`.

## Forbidden

Any file other than the eight vendored files and `ADOPTION.md`; deploying or dispatching; changing settings.

## Stop boundary

Stop at the end of this task and hand the result to the coordinator. Do not start another task.
