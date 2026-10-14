# Task J: live deployment (human gate)

- **Prerequisites:** R `complete` with `PASS`; the owner's explicit "y" to the preview, with availability within about 30 minutes if the rollback itself fails ("y" without it is "n").
- **Read first:** `PLAN.md` "Live preview (J)" and "Approval record (J)", `CONTRACT.md`.
- The coordinator writes `results/J-approval.md` per `COORDINATOR.md` "Approval records", records J `in_progress`, and confirms the helper shows `READY` (a handoff only).

## Work

1. **Recheck, seconds before dispatch, read clean first:** `origin/main` equals the source (record the tip); frozen hashes and the recomputed fingerprint; live page is v1; `deploy.yml` run IDs and `github-pages` deployment IDs equal the baseline. If anything differs: dispatch nothing, leave J `in_progress`, stop and ask the owner.
2. **Dispatch** `R-dispatch-inputs.json` once, as a tool call of its own. If it errors or no single new run appears within 2 minutes, never dispatch again; stop and ask the owner.
3. **Wait** per `CONTRACT.md` "Dispatch" (45 minutes; then cancel and up to 10 more minutes).
4. **Runtime acceptance:** checks 1 and 2 in order, stopping at the first failure; always read check 3. A wrong run follows `CONTRACT.md` "A wrong run".
5. **On failure:** run `completed` first; record J `failed` with `runtimeAcceptance: "FAIL"` and `liveStateChanged` per `CONTRACT.md` (one-line reason when `false`); tell the owner plainly what is live and what happens next.

## If `liveStateChanged: false` is proven

Do not dispatch V. Record V `failed` with "rollback not needed" and the reason; K stays blocked. Ask the owner how to continue. Land the records as `K-reconcile.md` steps 2–4 describe, with a deviation note for the expected `protected_change`. End state: "stopped; nothing published, proven".

## Result

`results/J.md`.

## Records

Hand the result content to the coordinator. Only the coordinator commits to `pilot/site-upgrade-records`.

## Forbidden

A second dispatch; any other input; any settings change.

## Stop boundary

Stop at the end of this task and hand the result to the coordinator. Do not start another task.
