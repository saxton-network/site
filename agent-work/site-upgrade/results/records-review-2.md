# Pilot 7 records independent re-review

## Scope and independence

- Source/main baseline: `95914a54336983fc48e286b8e16cb6780076d2f2`
- Repaired records candidate: `0d109095623e1ec9712e56f5144fb673a2f91792`
- Reviewed all 28 added paths, the complete source-to-candidate history and commit metadata, the seven file differences from the failed candidate, coordinator state, frozen inputs, evidence hashes, repository rules, and the repair handoff.
- The same independent, read-only reviewer that reported P7-R1 performed this re-review. The repair was prepared by a separate repair role and integrated by the coordinator. Reviewer independence was re-established from runtime metadata; identifying details are intentionally omitted from repository records.

## Verdict

**PASS.** P7-R1 is resolved for the exact repaired candidate. No new site-rule or in-scope threat-model finding was found.

## Resolution of P7-R1

- The candidate contains exactly one commit above the source, and that commit's parent is the exact source. The failed candidate and its records history are not ancestors of the repaired candidate; they remain preserved separately for provenance.
- The replacement commit uses the configured repository identity. Its message contains no attribution trailer, email address, or model identifier.
- `B-review.md` no longer instructs contributors to put reviewer identity in commit-message trailers. It now requires generic independence wording and explicitly keeps identifying and attribution details out of repository content and messages.
- The plan contains a dated records-only substitution clarification. It identifies the preserved original history, the exact-source replacement, unchanged frozen bytes, same-reviewer requirement, lack of live authority, and separate owner approval still required for landing.
- `results/V.md` preserves rollback acceptance PASS and the stopped-after-verified-rollback outcome while recording P7-R1 as the original landing blocker. It distinguishes failed V attempt 1 at records review from V attempt 2, which is a records-only repair and not another deployment or rollback dispatch.
- The failed first review is preserved byte for byte in `results/records-review-1.md`. The separate repair handoff is preserved in `results/records-repair-1.md`, followed by a coordinator integration note.

P7-R1 was a site-rule violation rather than a threat-model classification. The repaired history and corrected instruction remove the violation from the exact candidate proposed for landing.

## Verification

- The clone is non-shallow. A proof run with no inherited `GIT_*` variables confirmed source ancestry, exclusion of the failed records history, one commit above source, and 28 changed paths all under `agent-work/site-upgrade/`.
- Divergence classification is the expected `protected_change`. The only protected changed paths are `CONTRACT.md`, `R-dispatch-inputs.json`, and `R-rollback-inputs.json` under the workflow directory.
- `CONTRACT.md`, `R.md`, and every `results/R-*` file are byte-identical to the failed candidate. All frozen configuration and validator hashes match. The frozen fingerprint recomputes exactly to `fcbe26fca2a95d6bcc621dbf27dd27b53eef7bc263c06e254f7404b8a2e1f33d`.
- Every indexed evidence hash matches the committed bytes. The original J failure, `liveStateChanged: true`, rollback acceptance PASS, and K blocked state remain intact.
- Manifest state is `J = failed`, `V = in_progress`, and `K = blocked`, appropriate while this exact re-review awaits coordinator recording. Evidence marks V attempt 1 failed at records review and V attempt 2 as `recordsOnlyRepair: true` and `in_progress`; no further live action is represented or authorized.
- `bash scripts/validate.sh` passes. The helper reports J GATED/failed, V READY/in_progress, and K BLOCKED/blocked, with the earlier workflows retaining their expected labels.
- The focused scan covered all 28 record files and the complete new commit message. It found no credential patterns, email addresses, IP addresses, model identifiers, private repository references, or unexpected URL hosts. The two lexical matches are the documented ordinary negative-control prose.
- Fresh remote state still has `main` at the exact source. Fresh live verification returned HTTP 200 with exact v1 bytes.

## Review boundary

This was a read-only re-review. No repository file, index, branch, ref, pull request, workflow run, deployment, setting, or remote state was changed. Landing remains subject to the coordinator's final exact-head record and the owner's separate approval.
