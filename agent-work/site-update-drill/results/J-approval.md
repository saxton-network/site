# Task J: owner approval (drill)

On 2026-10-13 the coordinator showed the owner the drill preview in plain language: what changes (the "Last updated" line), the source and fingerprints, the v2 dispatch, the planned failing check, the undo dispatch and when it is skipped, exposure and caching, stop conditions, the retry boundary and the end state. It ended with "This one yes covers both runs (v2 and the undo). Shall I run the drill? y / n". The owner answered `y`.

The approval covers exactly this batch:

- Source: `8f3c310876166dc0cb2864dff3646e18830b1758`
- Frozen batch fingerprint: `d2a53d23b197f1bc5a80e8c95c9970c6508c766798b50df0f4427d6863542726`
- Exactly two dispatches of `deploy.yml` on `main`:
  1. the v2 deploy, `results/R-dispatch-inputs.json` (`sha: 8f3c310876166dc0cb2864dff3646e18830b1758`), SHA-256 `e27030c7cf97b3e82261c33752143f18515a84dfce60e503bdbff5b03d88b175`;
  2. the rollback, only under the condition in `CONTRACT.md` "Rollback (V)": `results/R-rollback-inputs.json` (`sha: 8377801ebd47f8ce1ec96eac9bd807dc5a876273`), SHA-256 `927b8539ce464e5e7cd1c65b1b1d720f9b2ce972f2f2d39ce52744e8e054650a`.

It does not cover a retry of either dispatch, another source or batch, or any settings change.
