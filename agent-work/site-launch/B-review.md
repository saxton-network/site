# Task B: independent review

- **Prerequisites:** A `complete`.
- **Reviewer:** a separate agent on a different model from the builder. It records its independence in words.
- **Read first:**
  - `AGENTS.md`, `docs/THREAT-MODEL.md`, `agent-work/WORKFLOW-SPEC.md`;
  - `PLAN.md`, `CONTRACT.md`;
  - the candidate diff from `main`.

## Review

1. **The page.** Every site rule, including a privacy read:
   - nothing private, no person, no contact details;
   - the listed repositories are public now, checked by an unauthenticated GET.
2. **`check-site.py`.** It must discriminate: run mutants and bad fixtures.
3. **`deploy.yml`.**
   - the input checks, including the ancestry check and injection safety;
   - checkout of exactly `sha`;
   - the `site/` rule;
   - the log evidence;
   - permissions, environment and concurrency;
   - that the pinned action tags exist.
4. **`validate.sh`.** A missing `check-site.py` now fails.
5. **Classification.** Classify each finding against the threat model, or as a site-rule violation, with a severity.

## Evidence

A `passed` record carries `deploymentSourceSha` equal to A's `candidateSha`.

## Result

`results/B-1.md`, and `B-2.md` after a repair.

## Records

Hand the result content to the coordinator. Only the coordinator commits to `pilot/site-launch-records`; nothing under `agent-work/site-launch/` is committed to the implementation branch.

## Forbidden

Editing anything; deploying or dispatching.

## Stop boundary

Stop at the end of this task and hand the result to the coordinator. Do not start another task.
