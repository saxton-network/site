# Bootstrap: adoption of Workflow (before this workflow)

- **Repository.** The owner created `saxton-network/site`, because the GitHub connection may not create organisation repositories. GitHub added a starter commit, `aaa38c8`, which the owner chose to keep.
- **Checklist.** Before the builder started, the coordinator wrote a hidden adoption checklist (`ADOPTION-CHECKLIST.md`, 17 items).
- **Builder.** A fresh agent that had not seen Workflow before. It was given:
  - an export of `saxton-network/workflow` at `3d38b27`, without the pilot records or `docs/PILOT-HISTORY.md`;
  - the site requirements.

  It produced commits `4222aac` and `f2cc21a`, and an ambiguity log of 21 entries in `ADOPTION.md`.
- **Review 1, on `f2cc21a`: findings.** The reviewer was a separate agent on a different model from the builder.
  - All 17 checklist items PASS. Item 15 was applied to the PR's commits; the owner's starter commit `aaa38c8` carries the owner's own identity, accepted under the plan's Owner clarifications.
  - F1 (Medium): `validate.sh` skipped hash rows it could not parse.
  - F2, F3 and F5 (Low).
  - F4 (informational, out of scope).
- **Repair, in `3da96f0`.** Done by the coordinator as the separate repair role.
- **Review 2: passed.** The review record is one comment on PR #1.
- **Merge.** On the owner's go-ahead, `main` was fast-forwarded from `aaa38c8` to `3da96f0` (ancestry proven first). GitHub marked PR #1 merged. `3da96f0` is `phase_baseline` for this workflow.
