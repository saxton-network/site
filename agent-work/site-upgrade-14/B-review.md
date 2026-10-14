# Task B: independent review

- **Prerequisites:** A `complete`.
- **Reviewer:** a separate agent pinned to a different model from the builder.
  - The coordinator checks the observed model in the reviewer's own transcript every round, and records independence in words in `results/B-n.md`.
  - A same-model review is a deviation, not independence.
  - Keep model names and IDs, personal names and email addresses out of repository content.
- **Read first:**
  - `AGENTS.md`, including "Commit metadata" and the reworded "Git identity";
  - `ADOPTION.md`, including the decisions recorded under "Ambiguities", such as 17;
  - `docs/THREAT-MODEL.md`, `agent-work/WORKFLOW-SPEC.md`, `PLAN.md` and `CONTRACT.md`;
  - the candidate diff from `16c3631`.

## Review

1. **Upgrade correctness.**
   - Each vendored file equals both the published alpha.14 ZIP (digest `1b87fa4a…8355`) and `git show 02c771a:<path>`.
   - The tag is lightweight at `02c771a`.
   - The `ADOPTION.md` rows and hashes are right, its history is kept, and its Upgrades entry is accurate and prose-only.
   - No stale `84d826a` remains in it, except in history text.
2. **Nothing else changed.** Workflow's own `AGENTS.md` is unchanged between `84d826a` and `02c771a`, so the site's `AGENTS.md` takes no vendored-rule change.
   - Only the five vendored files, `ADOPTION.md` and `AGENTS.md` changed.
   - The `AGENTS.md` change is exactly the decision 2(a) text.
   - `site/index.html`, `scripts/check-site.py`, `scripts/projects.txt`, `scripts/validate.sh` and `.github/workflows/deploy.yml` are byte-identical to `16c3631`.
3. **Site rules and privacy.**
   - The new text names no private names, hosts, people or emails.
   - The candidate's commits use only the mandated identity and the trailers the "Commit metadata" exemption allows.
   - Both listed repositories are still public (an authenticated `private`/`visibility` read; record the channel).
4. **The helper.** With the alpha.14 helper, the labels of the existing `site-launch`, `site-update-drill` and `site-upgrade` workflows are unchanged from the alpha.13 helper.
5. **`CONTRACT.md`.** It is sound, including the evidence-client table and the window rules.

Classify each finding against the threat model, or as a site-rule violation, with a severity. Verdict: `passed` or `findings`. If it is not clean after two repair rounds, the run stops.

## Evidence

A `passed` record carries `deploymentSourceSha` equal to the latest candidate.

## Result

`results/B-1.md`, and `B-2.md` after a repair.

## Records

Hand the result content to the coordinator. Only the coordinator commits to `pilot/site-upgrade-14-records`.

## Forbidden

Editing anything; dispatching; commenting on GitHub.

## Stop boundary

Stop at the end of this task and hand the result to the coordinator. Do not start another task.
