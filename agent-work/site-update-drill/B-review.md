# Task B: independent review

- **Prerequisites:** A `complete`.
- **Reviewer:** a separate agent on a different model from the builder. It records its independence in words.
- **Read first:**
  - `AGENTS.md`, `docs/THREAT-MODEL.md`, `agent-work/WORKFLOW-SPEC.md`;
  - `PLAN.md`, `CONTRACT.md`;
  - the candidate diff from `main`.

## Review

1. **The candidate.**
   - The diff from the base changes only `site/index.html`; `.github/` and `scripts/` are byte-identical to v1.
   - Every site rule holds, including a privacy read: nothing private, no person, no contact details.
   - The site check passes on Python 3.11, 3.12 and 3.13.
   - The listed repositories are still public: read each repository's `private`/`visibility` field from GitHub's API. An authenticated call is fine. A 403 or a response without that field is a failed probe, never a pass. Record the channel used.
2. **The drill contract.**
   - The injected fault cannot pass by accident, and cannot hide a real failure: check 2a must prove v2 is live before 2b fails.
   - The rollback restores exactly v1, through the same deploy code, within the approved batch.
   - v1 stays on `main`'s first-parent history, so `deploy.yml` accepts it.
   - Stop conditions, retry boundaries and the end state are unambiguous.
3. **Classification.** Classify each finding against the threat model, or as a site-rule violation, with a severity.

## Evidence

A `passed` record carries `deploymentSourceSha` equal to the latest candidate: A's `candidateSha`, or the latest repair (C) record's `candidateSha` after a repair.

## Result

`results/B-1.md`, and `B-2.md` after a repair.

## Records

Hand the result content to the coordinator. Only the coordinator commits to `pilot/site-update-drill-records`; nothing under `agent-work/site-update-drill/` is committed to the implementation branch.

## Forbidden

Editing anything; deploying or dispatching.

## Stop boundary

Stop at the end of this task and hand the result to the coordinator. Do not start another task.
