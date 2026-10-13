# Task J: live deployment (human gate)

- **Prerequisites:**
  - R `complete` with `PASS`;
  - Pages turned on by the owner, under its own approval;
  - the owner's explicit "y" to the concrete preview.
- **Read first:** `AGENTS.md`, `PLAN.md` "Live previews", `CONTRACT.md`.
- The coordinator records the approval in `results/J-approval.md` (`in_progress`) and confirms the helper shows `READY`. That label is a handoff only.

## Work

1. **Recheck:**
   - `origin/main` equals the source, and record its tip;
   - the frozen file hashes;
   - the live page baseline.
2. **Dispatch** exactly the frozen inputs. Find the single new run. If its `run-name` or `head_sha` is wrong, cancel it and stop.
3. **Runtime acceptance:** checks 1–3 of `CONTRACT.md`, stopping at the first failure.
4. **On failure:** record J `failed` with `runtimeAcceptance: "FAIL"`, and follow the contract's rollback.

## Result

`results/J.md`.

## Records

Hand the result content to the coordinator. Only the coordinator commits to `pilot/site-launch-records`; nothing under `agent-work/site-launch/` is committed to the implementation branch.

## Forbidden

- A second dispatch.
- Any other input.
- Changing settings.

## Stop boundary

Stop at the end of this task and hand the result to the coordinator. Do not start another task.
