# Task V: rollback and verification

Performed by the coordinator on 2026-10-13, under `results/J-approval.md`, which covers this one rollback dispatch.

**Rollback acceptance: PASS. Drill verdict: PASS.**

## 1–2. The v2 run and whether a rollback was needed

- The v2 run 38416735077 had `completed` (`success`) before V started; nothing was cancelled.
- Its step `Run actions/deploy-pages@v5.0.1` started at 14:50:01Z, and check 2a had read v2's exact bytes live. So v2 had gone live, and the rollback dispatch was approved (`CONTRACT.md` "Rollback (V)").

## 3. Recheck before dispatch (2026-10-13T14:51:09Z)

- `git ls-remote origin refs/heads/main` = `8f3c310…`, the source.
- `results/R-rollback-inputs.json` SHA-256 `927b8539…4650a`, equal to the frozen hash and the one in `J-approval.md`.
- `deploy.yml` at `main` SHA-256 `45fd7396…0073e`, equal to the frozen hash.
- `deploy.yml` runs: 38410452425 (v1 launch) and 38416735077 (v2).

## 4. Dispatch

One `run_workflow` call for `deploy.yml` on `main` with `sha: 8377801ebd47f8ce1ec96eac9bd807dc5a876273`, answered `204 No Content` (about 14:51:17Z). No other dispatch was made.

## 5. Rollback acceptance — PASS

- Exactly one new run: 38416947644 (the list went from 2 runs to 3). `run-name` = `Deploy 8377801ebd47f8ce1ec96eac9bd807dc5a876273`. Conclusion `success`; job 115363804680 and every step `success`.
- `head_sha` = `8f3c310…`, equal to the `main` tip, as the contract requires (the run executes `main`'s workflow file and checks out the input).
- Job log: `PASS: site check (2 repositories listed)`, `DEPLOY HEAD=8377801ebd47f8ce1ec96eac9bd807dc5a876273`, `DEPLOY INDEX_SHA256=495b4b2b4e8c25335184fa994716a888bc9f0980b3196eb633110bde18351eb3` (v1's hash). The archive held only `./index.html`.
- Live page: `curl -sS --compressed 'https://saxton-network.github.io/site/?cb=<nonce>'` at 2026-10-13T14:51:49Z, first try: status 200, SHA-256 `495b4b2b4e8c25335184fa994716a888bc9f0980b3196eb633110bde18351eb3`, equal to v1.
- `main` after acceptance = `8f3c310…`, unchanged.

## 6. Drill verdict — PASS

- J matched the expected-failure signature (`results/J.md`): 1, 2a and 3 passed, 2b failed, and the live bytes equalled v2.
- The rollback restored v1 byte for byte, through one dispatch of the same deploy code, within the approved batch.
- **End state: "stopped after verified rollback".** `main` holds v2 (`8f3c310`) while the live page shows v1. Bringing the live page back to `main` is a later, normal deploy with its own approval. K stays blocked.

## Observation

`actions/deploy-pages` labels the deployment with `pages_build_version` = `GITHUB_SHA`, which for a dispatch is `main`'s tip, not the input. Both the v2 deployment and this rollback are labelled `8f3c310…`, although the rollback serves v1. GitHub's deployment list therefore cannot tell which commit is live; only the job log's `DEPLOY HEAD` line and the live bytes can. For v1's launch the two happened to be equal.

## 7. Records divergence from the source

Run with no inherited `GIT_*` variables, against the records head before this file (`ef6ee4bd567d392b1af61f622f6881d183a9be67`):

- `GIT_GRAFT_FILE=/dev/null git --no-replace-objects -c core.commitGraph=false -c advice.graftFileDeprecated=false merge-base --is-ancestor 8f3c310… ef6ee4b…` exited 0.
- `git --no-replace-objects -c core.commitGraph=false diff --no-renames --no-relative --ignore-submodules=none --name-only -z 8f3c310… ef6ee4b…` lists 26 paths, all under `agent-work/site-update-drill/`.
- This commit adds `results/V.md`, so the records PR changes 27 paths, all under that directory. The PR description carries the check on its final head.
- `classify_divergence`, with the frozen batch's configuration and validator paths, returns `protected_change`. The protected paths are exactly `CONTRACT.md` and the four frozen `results/R-*` files, as `V-rollback.md` expects; they document the batch, and both dispatches have already run.

## 8. Secrets and site-rule check

- No GitHub tokens, private-key blocks, bearer tokens or AWS key IDs; no email or IP addresses.
- Private repository names, checked through the authenticated connection: the only match is the ordinary English word in "negative control" in `R.md`. No private name is printed here.

## 9–10. Records landing

V is recorded `complete` here, before the merge, because records cannot prove their own merge. The records PR from `pilot/site-update-drill-records` is reviewed independently, then landed by the coordinator on the owner's go-ahead with a local `git merge --no-ff` pushed as a fast-forward. The merge commit and a fresh check of `main` and the live page are reported afterwards, outside the records.
