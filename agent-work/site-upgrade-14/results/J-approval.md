# Task J: owner approval

This record follows `agent-work/COORDINATOR.md` "Approval records". The approval was given in chat, so this record is the coordinator's own account of it. The platform offers no link or identifier for the owner's message.

- **When:** 2026-10-14, after readiness `PASS` (`results/R.md`), in the coordinator session that ran readiness. There was no handover.
- **Preview shown:** a plain-language preview that covered:
  - **the change for visitors:** the "Last updated" line appears;
  - **exposure:** v2 has been public before;
  - **`main`:** it already holds the upgrade, and a "no" leaves v1 live;
  - **the batch:** the one v2 deploy and the conditional v1 redeploy, each with its input-file fingerprint, and the batch fingerprint;
  - **the checks:** the named evidence tools and their backups, proven at readiness, including the deploy-log read;
  - **the 10-minute rule:** a read outage fails the check and rolls back even a correct deploy;
  - **time and caching;**
  - **handover:** the handover rule;
  - **the emergency option:** Unpublish, with its exact path and effect;
  - **limits:** the retry limit and the freeze;
  - **the four end states;**
  - **two readiness observations:** the missing visibility fallback for one listed repository, and a reworded phrase.
- **Question asked:** "Approve, and can you be reached within about 30 minutes if the rollback itself fails? (y/n)"
- **Answer, as given:** `y`. It answers both parts of the question: approval, and availability within about 30 minutes.

## Approved batch

- Source: `dfaa7cb863da02c204b34c4e05d90d9f9660fe97`
- Frozen batch fingerprint: `82cfa32b80c6ada17cab1535b04c645544c4a3b69a0c1d66575b7b623d39e0cb`

## Approved actions

1. **The v2 deploy.** One dispatch of `.github/workflows/deploy.yml` on `main` with `agent-work/site-upgrade-14/results/R-dispatch-inputs.json` (`sha` = the source), SHA-256 `f6af6225636679fff5e515ff5757aeba168843b5b92eb565d39cbe2332381427`.
2. **The v1 redeploy, if needed.** One dispatch with `agent-work/site-upgrade-14/results/R-rollback-inputs.json` (`sha` = `8377801ebd47f8ce1ec96eac9bd807dc5a876273`), SHA-256 `927b8539ce464e5e7cd1c65b1b1d720f9b2ce972f2f2d39ce52744e8e054650a`. It is approved only under `CONTRACT.md` "Rollback (V)", and never when `liveStateChanged: false` is proven.
3. **A cancel,** only for a run still going after the 45-minute wait. No other cancel is approved.

## Not covered

- A retry, of any kind.
- Another source or batch.
- Any settings change, including Unpublish, which is the owner's own action.
- Merging the records PR.
- The Workflow history PR.

## Clarifications in force

None. `PLAN.md` "Clarifications" has no dated entries.
