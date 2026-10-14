# Task B: independent review

- **Prerequisites:** A `complete`.
- **Reviewer:** a separate agent pinned to a different model from the builder (named in each commit's co-author trailer). The coordinator checks the observed model in the reviewer's own transcript every round and records it in words in `results/B-n.md`; a same-model review is a deviation, not independence.
- **Read first:** `AGENTS.md`, `docs/THREAT-MODEL.md` (the new version, including "Guard validators"), `agent-work/WORKFLOW-SPEC.md`, `PLAN.md`, `CONTRACT.md`, the candidate diff from `ae90609`.

## Review

1. **Upgrade correctness.** Each vendored file equals both the published alpha.13 ZIP (digest `e520b61c…d5d4`) and `git show 84d826a:<path>`; the tag peels to `84d826a`; `ADOPTION.md` rows and hashes are right, its history kept, its Upgrades section accurate and prose-only.
2. **Nothing else changed.** Only the five vendored files and `ADOPTION.md`. `site/index.html`, `scripts/check-site.py`, `scripts/projects.txt`, `scripts/validate.sh` and `.github/workflows/deploy.yml` are byte-identical to `ae90609`.
3. **Site rules and privacy.** No private names, hosts, people or emails in the new vendored text or `ADOPTION.md`; both listed repositories still public (authenticated `private`/`visibility` read; record the channel). Note: the threat model's guard-validator rule concerns a guard missing crafted content; the site's rule that a content breach is always a defect still holds.
4. **Helper and contract.** With the alpha.13 helper, the existing workflows' labels are unchanged; `CONTRACT.md` is sound.

Classify each finding against the threat model or as a site-rule violation, with severity. Verdict `passed` or `findings`. If not clean after two repair rounds, the run stops.

## Evidence

A `passed` record carries `deploymentSourceSha` equal to the latest candidate.

## Result

`results/B-1.md`, and `B-2.md` after a repair.

## Records

Hand the result content to the coordinator. Only the coordinator commits to `pilot/site-upgrade-records`.

## Forbidden

Editing anything; dispatching; commenting on GitHub.

## Stop boundary

Stop at the end of this task and hand the result to the coordinator. Do not start another task.
