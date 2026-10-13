# Task K: final reconciliation

## Final refs and live state (checked 2026-10-13T14:07:53Z, after runtime acceptance)

- `origin/main` = `8377801ebd47f8ce1ec96eac9bd807dc5a876273`, the deployed source.
- `curl -sS --compressed 'https://saxton-network.github.io/site/?cb=<nonce>'`: status 200, body SHA-256 `495b4b2b4e8c25335184fa994716a888bc9f0980b3196eb633110bde18351eb3`, the frozen hash.
- `deploy.yml` has exactly one run, 38410452425 (`results/J.md`).

The main freeze ends when the records land.

## Secrets and site-rule check

- The records were scanned for GitHub tokens (`ghp_`, `gho_`, `ghu_`, `ghs_`, `ghr_`, `github_pat_`), private-key blocks, bearer tokens and AWS key IDs: none.
- Email addresses: none, other than the no-reply commit trailer identity. IP addresses: none.
- Private repository names: the records and the branch's commit messages were checked against the organisation's private repositories through the authenticated connection. The only match is an ordinary English word in the copied adoption checklist, not a reference to a repository. No private name is printed here.
- The records hold no response bodies beyond public run metadata and log lines.

## Records divergence from the deployed source

Run with no inherited `GIT_*` variables, against the records head before this file (`38af7150e76724a68d45f13776527c3a38b2de5e`):

- `GIT_GRAFT_FILE=/dev/null git --no-replace-objects -c core.commitGraph=false -c advice.graftFileDeprecated=false merge-base --is-ancestor 8377801… 38af715…` exited 0.
- `git --no-replace-objects -c core.commitGraph=false diff --no-renames --no-relative --ignore-submodules=none --name-only -z 8377801… 38af715…` lists 32 paths, all under `agent-work/site-launch/`.
- This commit adds `results/K.md`, so the records PR changes 33 paths, all under `agent-work/site-launch/`. The PR description carries the check on its final head.
- `classify_divergence`, with the frozen batch's configuration and validator paths as protected inputs, returns `protected_change`. The only protected paths are `CONTRACT.md` and `results/R-dispatch-inputs.json`, as `K-reconcile.md` expects: these files document the batch, and the page is already published from the source, so the records change no deployment input.

## Records PR

The records PR from `pilot/site-launch-records` to `main` is reviewed independently, then landed by the coordinator on the owner's go-ahead with a local `git merge --no-ff` pushed as a fast-forward, after which `main` is rechecked. The merge and that recheck come after this file, so they are reported in the coordinator session and visible in the merge commit. Record K's `complete` status covers work steps 1–2 and the divergence proof only.

## Gate behaviour observed

| When | Helper | Expected |
| --- | --- | --- |
| Before readiness | J `GATED` | yes |
| After R `PASS` | J `PREVIEW` | yes |
| After the approval record | J `READY` | yes |
| After J complete with `runtimeAcceptance` `PASS` | J `DONE`, K `READY` | yes |
| Repair needed three times | C `READY` after each reset to `pending`, `BLOCKED` once `complete` and B `passed` | yes |
| No failed launch | V `BLOCKED` | yes |

## Batched Low findings

- F8 (`results/B-4.md`): the site check joins decoded text with spaces, so a name split by inline tags, or written with rarer look-alikes, still passes. Out of scope as deliberate tampering; left for a later reviewed update.
