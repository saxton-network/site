# Pilot 7 records independent review

## Scope

- Repository: public `saxton-network/site`
- Source/main baseline: `95914a54336983fc48e286b8e16cb6780076d2f2`
- Records candidate and PR head: `a43e267efda2a313ff4fc71cda75a4ad7d84f9bb`
- Pull request: #4, open against the exact source baseline
- Reviewed all 26 changed paths in `source..candidate`, all under `agent-work/site-upgrade/`, plus the relevant commit metadata, repository rules, workflow specification, evidence-manifest rules, threat model, plan revision 3 and clarification, frozen contract, task files, results, and sanitized runtime observations.

## Verdict

**FINDINGS — do not land the records PR in its present history.**

The records files, evidence chain, frozen batch, status transitions, deployment failure record, and verified rollback are internally consistent. One owner-set site-rule violation in the candidate's commit history blocks the planned merge.

## Finding P7-R1 — prohibited attribution trailers in the PR history

- **Severity:** Medium; merge-blocking site-rule violation.
- **Rule:** `AGENTS.md` says the site rules apply to every commit message and forbids naming email addresses. It also says a site-rule breach is always a defect rather than a threat-model classification question.
- **Evidence:** Eight of the ten commits in `95914a5..a43e267` contain `Co-authored-by` trailers with email addresses and model-like labels. The protected values are deliberately not reproduced here. The two commits after the readiness-freeze record contain no such trailers.
- **Cause in the reviewed records:** `agent-work/site-upgrade/B-review.md` line 4 explicitly says the model should be named in each commit's co-author trailer. Following that instruction necessarily introduces an email-form trailer and conflicts with the repository rule.
- **Why the existing disclosure is insufficient:** `agent-work/site-upgrade/results/V.md` line 47 accurately says the attribution text predates takeover and was not copied into the new messages. The planned local `--no-ff` merge would still add those eight commit messages to `main`, so their inherited status does not make the candidate compliant.
- **Classification:** Site-rule violation; no threat-model item assigned, as required by `AGENTS.md`.
- **Required before landing:** Present a records candidate whose history to be added to `main` contains no prohibited trailers, without deleting or force-rewriting the preserved source history, and independently review the exact replacement candidate. The records task must not direct future commits to encode reviewer identity in commit-message trailers.

## Evidence supporting the rest of the records

- `bash scripts/validate.sh` passes at the detached candidate. The helper reports `J GATED failed`, `V READY complete`, and `K BLOCKED blocked`; the two earlier workflows retain their expected labels.
- Every evidence link in `evidence.json` matches the candidate file bytes. The frozen fingerprint recomputes to `fcbe26fca2a95d6bcc621dbf27dd27b53eef7bc263c06e254f7404b8a2e1f33d`. All frozen configuration and validator hashes match, including both dispatch-input files and `CONTRACT.md`.
- Files changed after the readiness freeze are limited to coordinator state plus the approval, J, and V records. No frozen input, deployment workflow, validator, or deployable page changed.
- The approval record matches the supplied conversation facts: exact source and fingerprint, both input-file hashes, one conditional rollback, the sole 45-minute cancel boundary, no retry/settings/main-push authority, and the combined approval/availability answer.
- Sanitized observations and fresh API reads confirm the pre-dispatch baseline, one v2 dispatch, exact run name/head, successful publishing step, one new Pages deployment, unchanged `main`, and `liveStateChanged: true`. The original required client log read failed, so `J` correctly remains failed and the unperformed v2 live-byte check is not retroactively accepted.
- The authenticated connector can now read the v2 job log and shows the expected v2 source and artifact hash. This later visibility does not rewrite the failed acceptance attempt.
- The rollback recheck matched the frozen rollback input and workflow hashes. Exactly one rollback run succeeded with the expected run name and `main` head. Its decoded log contains the exact v1 source and v1 artifact hash. Fresh live verification returned HTTP 200 with exact v1 bytes, while `main` remained at the reviewed source.
- Fresh GitHub metadata shows both deployment runs completed successfully, the two expected new Pages deployment IDs exist, PR #4 has the exact head/base and 26 files, and the organization repositories named in the records are public. No private repository name was printed or recorded during this review.
- A separate full-history proof with zero inherited `GIT_*` variables showed a non-shallow repository, source ancestry, 26 changed paths all under the workflow directory, and `protected_change` only for `CONTRACT.md`, `R-dispatch-inputs.json`, and `R-rollback-inputs.json`, as allowed after verified rollback.
- The 26 file contents contain no email addresses, model identifiers, IP addresses, common credential patterns, unknown organization-repository references, or unapproved URL hosts. This clean file-content result does not cover the commit-message defect above.
- The records do not claim a merge, retry, successful v2 runtime acceptance, workflow completion, or final reconciliation. They accurately state the end condition as stopped after verified rollback with K blocked.

## Review boundary

Read-only review only. No repository file, ref, pull request, workflow run, deployment, setting, or remote state was changed.
