# Scaffold review

The reviewer was a separate agent on a different model from the coordinator, the same agent that reviewed `site-launch` from B-2 onward. Its transcript shows only that model.

- **Pass on `f3134f2`: changes, Low only.** Task A may start; the fixes must land before R freezes anything.
  - S1: if v2 never went live, V must not redeploy v1. The contract now limits the rollback dispatch to the case where v2 may have gone live, and V has a "rollback not needed" path.
  - S2: a failed recheck in J or V means no dispatch; J stays `in_progress`, so V cannot become ready.
  - S3: no re-dispatch; if a dispatch call errors or no run appears, re-list for up to 2 minutes, then stop and ask the owner.
  - S4: `J-approval.md` must name the source, the fingerprint, the two approved dispatches and both input files with their hashes.
  - N1 (applied): R runs the deploy guard and site check locally against v1 and the source.
  - N2 (applied): A may add one CSS rule for the new line.
  - N3 (not applied): `PLAN.md`'s unauthenticated visibility probe is the known drift; the task files govern.
- **Confirmed:** v1 is the first parent of `main` and stays on the first-parent line after P; the frozen batch covers every live input and passes the helper's path rules; V becomes ready only after J `failed`; K is never ready; no private names, emails or IPs.
- **Applied in the next commit** on the records branch. The reviewer re-checks them in B.
