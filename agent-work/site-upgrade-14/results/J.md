# Task J: live deployment

Performed by the coordinator on 2026-10-14, under `results/J-approval.md`. There was no handover.

**Runtime acceptance: PASS.** Every check passed on its first read with its primary client. No read was repeated and no fallback was needed.

- Source: `dfaa7cb863da02c204b34c4e05d90d9f9660fe97`
- Frozen batch fingerprint: `82cfa32b80c6ada17cab1535b04c645544c4a3b69a0c1d66575b7b623d39e0cb`

## Recheck, 08:17:11Z–08:17:14Z, read clean before dispatch

- **`main`:** `git ls-remote` and `curl` (git refs API) both show `main` = the source, so the recorded tip is `dfaa7cb…`.
- **Frozen batch:** every frozen configuration and validator hash, and the deployable artifact, match. The fingerprint recomputed with the source helper equals the approved one.
- **Live page:** 200, v1's bytes.
- **`deploy.yml` runs:** 5, with the baseline IDs, both through `curl` and through the connection (latest 38513444503).
- **`github-pages` deployments:** 5, with the baseline IDs.

## Dispatch

One `run_workflow` call for `deploy.yml` on `main`, with input `sha: dfaa7cb863da02c204b34c4e05d90d9f9660fe97`, the frozen input file's value. GitHub returned 204. No second dispatch or cancel was made.

## Waiting

- One new run, 38534046073, was queued by 08:17:24Z.
- It was polled every 5 seconds.
- First observation of `completed`: **08:17:50Z**. The acceptance window ran from then to 08:27:50Z.

## Runtime acceptance

1. **The run: PASS** (connection).
   - Exactly one new `deploy.yml` run: the list went from 5 to 6.
   - `head_sha` `dfaa7cb…` equals the recorded tip.
   - `run-name` is `Deploy dfaa7cb863da02c204b34c4e05d90d9f9660fe97`.
   - It ran 08:17:19Z–08:17:47Z and concluded `success`.
2. **The log: PASS** (connection, job 115752507874, line limit 2000).
   - The log is complete: 376 lines, with the job header `Complete job name:` present.
   - The output lines, not the `echo` command lines, are `DEPLOY HEAD=dfaa7cb863da02c204b34c4e05d90d9f9660fe97` and `DEPLOY INDEX_SHA256=1f60283e1c442f0fd8e0015787c84febd2b37eabfe83bc9dbea54e7b345f7a35`. These are the source and the frozen v2 hash.
3. **The live page: PASS.** At 08:18:10Z, the first read, `curl -sS --compressed 'https://saxton-network.github.io/site/?cb=<nonce>'` returned 200. The body's SHA-256 was `1f60283e…7a35`, v2, showing "Last updated 13 October 2026."
4. **`main` unchanged: PASS.** At 08:18:11Z, `git ls-remote` still showed `dfaa7cb…`.

## Observations

- The deploy run took 28 seconds. The live page showed v2 20 seconds after the run completed.
- The deploy-log read that failed in Pilot 7 worked through the named primary client on the first read. Readiness had proven both that client and the `curl` fallback.
