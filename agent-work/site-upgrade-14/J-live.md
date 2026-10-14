# Task J: live deployment (human gate)

- **Prerequisites:**
  - R `complete` with `PASS`.
  - The owner's explicit "y" to the preview, with availability within about 30 minutes if the rollback itself fails. A "y" without that availability is "n".
  - If another coordinator has taken over, the four steps in `PLAN.md` "Handover" are done.
- **Read first:** `PLAN.md` "Live preview (J)" and "Approval record (J)"; `CONTRACT.md`.
- **Before the work:** the coordinator writes `results/J-approval.md` under `COORDINATOR.md` "Approval records", records J `in_progress`, and confirms the helper shows `READY`. That label is a handoff only.

## Work

1. **Recheck, seconds before dispatch.** Use the evidence clients, and read the output clean before going on:
   - `origin/main` equals the source; record the tip;
   - the frozen hashes and the recomputed fingerprint;
   - the live page is v1;
   - the `deploy.yml` run IDs and the `github-pages` deployment IDs equal the baseline.

   If anything differs: dispatch nothing, leave J `in_progress`, stop and ask the owner.
2. **Dispatch** `R-dispatch-inputs.json` once, as a tool call of its own. If it errors, or no single new run appears within 2 minutes, never dispatch again; stop and ask the owner.
3. **Wait** as `CONTRACT.md` "Dispatch" sets out: 45 minutes, then cancel and wait up to 10 more minutes. Poll at least every minute. Timestamp the first observation of `completed`; the acceptance window starts there.
4. **Runtime acceptance.** Run checks 1–3 in order with their evidence clients, within the one window, stopping at the first failure. Always read check 4. Evidence that fails a check is never re-read, except the CDN case in check 3. If check 1 or 2 fails, read the live page once anyway, for `liveStateChanged` and V. A wrong run follows `CONTRACT.md` "A wrong run".
5. **On failure, normal path.**
   - Make sure the run is `completed`.
   - Record J `failed` in the manifest and the evidence, with `runtimeAcceptance: "FAIL"` and `liveStateChanged` as `CONTRACT.md` sets out. Give a one-line reason when it is `false`. An unreadable log, step list or deployments list makes it `null`.
   - Tell the owner plainly what is live and what happens next.
6. **On failure, after the post-cancel bound has expired.** Record J `failed` with `runtimeAcceptance: "FAIL"` and `liveStateChanged: null`, and stop. V does not dispatch; the owner decides.

**Cancels.** The only approved cancel is for a run still going after the 45-minute wait. No other cancel is approved. The approval record lists any dated plan clarifications in force.

## If `liveStateChanged: false` is proven

- Do not dispatch V.
- Record V `failed` with "rollback not needed" and the reason, before any merge. K is not recorded and stays blocked.
- Ask the owner how to continue.
- Only after the owner's go-ahead, land the records as `K-reconcile.md` steps 2–4 describe, with a deviation note for the expected `protected_change`.
- End state: "stopped; nothing published, proven".

## Result

`results/J.md`.

## Records

Hand the result content to the coordinator. Only the coordinator commits to `pilot/site-upgrade-14-records`.

## Forbidden

A second dispatch; any other input; any settings change.

## Stop boundary

Stop at the end of this task and hand the result to the coordinator. Do not start another task.
