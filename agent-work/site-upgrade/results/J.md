# Task J: live deployment

Performed by the coordinator on 2026-10-14 under the owner's approval in `results/J-approval.md`.

**Runtime acceptance: FAIL.** The required deployment log could not be retrieved: the read request returned `Forbidden` after GitHub's redirect. Raw response details and temporary access URLs are deliberately omitted. This is an acceptance failure, not a successful deployment claim.

- Source: `95914a54336983fc48e286b8e16cb6780076d2f2`.
- Frozen batch fingerprint: `fcbe26fca2a95d6bcc621dbf27dd27b53eef7bc263c06e254f7404b8a2e1f33d`.

## Recheck before dispatch (2026-10-14T04:47:40Z)

- Direct main ref equalled the source; the records ref equalled approval commit `7076e620cb598c9f1537cf4f62634a4167bdf4dd`.
- All frozen file hashes and linked evidence hashes matched. The alpha.13 helper recomputed the frozen fingerprint and showed J `READY`.
- Live page: `curl -sS --compressed` with a unique query value, HTTP 200, SHA-256 `495b4b2b4e8c25335184fa994716a888bc9f0980b3196eb633110bde18351eb3` (v1).
- Deploy run IDs: 38410452425, 38416735077, 38416947644.
- Pages deployment IDs: 7040675239, 7041742077, 7041777317. Both lists exactly matched the frozen baseline.

## Dispatch

One standalone `gh api --method POST` call to `repos/saxton-network/site/actions/workflows/deploy.yml/dispatches`, with `ref=main` and `inputs[sha]=95914a54336983fc48e286b8e16cb6780076d2f2`, exited 0 at 2026-10-14T04:47:46Z. These are exactly the frozen input file's values. No second dispatch or cancel was made.

## Runtime acceptance

1. **The run: FAIL at the required log read.** Exactly one new run, [38513237296](https://github.com/saxton-network/site/actions/runs/38513237296), appeared within two minutes. Its `head_sha` was the source, its run name was `Deploy 95914a54336983fc48e286b8e16cb6780076d2f2`, and attempt 1 was reported completed and successful, with `updated_at` 04:48:07Z. Job 115686252596 succeeded. Reading its deployment log failed with `Forbidden`, so the required `DEPLOY HEAD=` and `DEPLOY INDEX_SHA256=` output lines could not be accepted. Stop at the first failed check.
2. **Live v2 bytes: not checked**, because check 1 failed. No claim is made that v2 passed live acceptance.
3. **Main: PASS.** Direct ref read at 2026-10-14T04:48:38Z still equalled the source.

## Whether live state changed

`liveStateChanged: true`. Fresh reads at 2026-10-14T04:49:09Z confirmed that the run was completed and successful, its `Run actions/deploy-pages@v5.0.1` step succeeded (04:47:58Z–04:48:04Z), and Pages deployment 7057104677 had been added. Publishing may have changed the live page; the proof that nothing published is unavailable.

The owner was told immediately that acceptance failed, that v2 may have published, and that the approved rollback would follow its recheck. V runs under the same approval. No retry of J is authorized.
