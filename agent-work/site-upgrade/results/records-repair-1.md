# Pilot 7 records repair handoff

Prepared on 2026-10-14 by the separate repair role for P7-R1. This is a repair handoff, not an independent review verdict or landing approval.

## Workspace and boundary

- Isolated standalone full clone: `/workspace/site-records-repair`.
- Branch: `pilot/site-upgrade-records-clean`.
- HEAD and intended parent for the coordinator's first replacement commit: `95914a54336983fc48e286b8e16cb6780076d2f2`.
- Public origin: `https://github.com/saxton-network/site.git`.
- Original `/workspace/site` remained clean at preserved candidate `a43e267efda2a313ff4fc71cda75a4ad7d84f9bb`; original branch/history and PR #4 were not modified.
- No commit, staging, push, PR mutation, merge, deploy dispatch, cancel, settings change, history rewrite, or Git identity change was performed.

## Snapshot and exact owned modifications

Copied exactly 26 files under `agent-work/site-upgrade/` from immutable blobs at `a43e267efda2a313ff4fc71cda75a4ad7d84f9bb`, verified byte for byte before editing. No original records commits or parents were made part of the replacement branch. Relative to that snapshot, the only changes are:

1. `B-review.md`: removed the co-author-trailer instruction; retained separate-reviewer independence and required generic wording with no model identifiers, personal names, email addresses or attribution trailers in content/messages.
2. `PLAN.md`: added the dated post-V clarification for records-only branch substitution, original history/PR preservation, exact-source parent, unchanged frozen batch, historical branch references, same-reviewer requirement, and separate owner landing approval.
3. `results/V.md`: retained rollback acceptance PASS and the stopped-after-verified-rollback outcome; made P7-R1 a landing blocker; preserved the failed review; described the clean replacement as awaiting exact-candidate scan, same-reviewer review and owner approval. It does not claim replacement review PASS or merge.
4. `results/records-review-1.md`: exact copy of `/workspace/scratch/pilot7-records-review.md`, preserving the independent failed review.

Current SHA-256 values:

- `agent-work/site-upgrade/B-review.md`: `8ff51a410186c1b4cc7d142e617a64ef91020c7cf4f6589f400dca7974425aee`
- `agent-work/site-upgrade/PLAN.md`: `353df73aad13ffab870be3667239207e21c61af62fb6e7e2c6cfbfe95f808bab`
- `agent-work/site-upgrade/results/V.md`: `6259c5cdd365469dba3ad21fc4a13da5c0d2cf15254d0b4d72192eeffc751c5b`
- `agent-work/site-upgrade/results/records-review-1.md`: `d0700faae5bac9e75fab2c612f89014257e0a5ec596e8463d65c53786de24afd`

## Fresh checks

- The public repository metadata reported `private: false` and `visibility: public`. Direct remote main read matched the exact source. The clean clone then fetched public main and asserted that same SHA.
- Before snapshot edits, `bash scripts/validate.sh` passed at the clean exact source.
- After the repair, `bash scripts/validate.sh` passed. The helper also exited 0 and showed J GATED/failed, V READY/complete and K BLOCKED/blocked. These labels do not authorize any action.
- The clone is non-shallow and standalone. Local ancestry/object proofs removed every inherited `GIT_*` variable, disabled replacement objects and commit-graph use, and explicitly set the graft file to `/dev/null`. HEAD and the clean branch both equal the source, source ancestry succeeds, and there are zero commits above source. The eventual replacement commit parent remains for the coordinator to prove after committing.
- All source files, including site content, vendored files, validators and deployment workflow, are byte-identical to source.
- `manifest.toml` and `evidence.json` remain exact original bytes. Historical execution branch names were not rewritten.
- `CONTRACT.md` and all five readiness files (`R.md`, `R-baseline.json`, `R-dispatch-inputs.json`, `R-rollback-inputs.json`, `R-rollback-v1.md`) remain exact original bytes.
- Every frozen deployment-configuration and validator SHA-256 and the page hash match. The helper recomputed fingerprint `fcbe26fca2a95d6bcc621dbf27dd27b53eef7bc263c06e254f7404b8a2e1f33d`.
- All 27 records files passed a focused pattern check for common credentials, email addresses, IPv4 addresses and model identifiers. No protected values were printed. This check is not a substitute for the coordinator's final secrets/privacy scan or independent review.

## Gate interruption and remaining coordinator work

The first local-clone bootstrap stopped at an explicit gate because local cloning did not copy the original remote-tracking `origin/main` ref. No branch or records edits had occurred. Only the isolated clone's origin URL was then set to the public remote and main was fetched; the exact-source gate passed before branch creation and baseline validation. An exploratory read also tried a nonexistent `R-frozen-batch.json`; the actual frozen batch was read from `evidence.json`. No repository-validation gate failed.

The existing evidence index still has the old V result hash, deliberately unchanged because shared evidence/status are coordinator-owned. The coordinator must update the index and any required review/repair status records, run the final integration gate and secrets/privacy scan, commit with the configured identity and no prohibited trailers, prove the literal candidate's parent and history, and send that exact candidate back to the SAME independent reviewer. The original failed report remains a failed report. Landing still requires a bounded owner preview and explicit go-ahead for the exact replacement batch.

Stopped at the assigned repair boundary with all edits uncommitted.

## Coordinator integration

The first V record retains rollback acceptance PASS but is marked failed at the records-review stage, with P7-R1 and the failed review linked. A second V record is a records-only repair attempt on the clean branch, not another rollback or deployment. Its status is in_progress until the same reviewer accepts the exact replacement. The original records branch and its commits remain preserved, while the new branch adds one clean snapshot above the source. The coordinator updated only workflow records and their evidence hashes. No live action or main ref change is authorized by this repair.
