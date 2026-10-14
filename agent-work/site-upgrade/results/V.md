# Task V: rollback and verification

Performed by the coordinator on 2026-10-14 under `results/J-approval.md`, which covers this one conditional rollback dispatch.

**Rollback acceptance: PASS. End state: stopped after verified rollback.**

Original records landing is blocked by independent-review finding P7-R1. A clean replacement records branch is prepared for re-review by the same independent reviewer and separate owner approval; no replacement review pass or merge is claimed. The rollback acceptance remains PASS.

## Why rollback was required

J failed its required deployment-log check with `Forbidden`; its publishing step had succeeded and Pages deployment 7057104677 was new. `liveStateChanged: true`. J run 38513237296 had completed before V. The failed attempt is preserved in `results/J.md`; it is not changed to a pass by later evidence.

## Recheck before dispatch (2026-10-14T04:50:04Z)

- Direct main ref: `95914a54336983fc48e286b8e16cb6780076d2f2`, still the approved source and V's expected `head_sha`.
- J run: `completed`.
- `results/R-rollback-inputs.json`: SHA-256 `927b8539ce464e5e7cd1c65b1b1d720f9b2ce972f2f2d39ce52744e8e054650a`, matching the frozen file and approval.
- `deploy.yml` at main: SHA-256 `45fd739663807a7cf325c18ecb57b31ff20decf1d4b61a9a05155a12e800073e`, matching the frozen hash.
- A non-shallow local proof with inherited `GIT_*` variables removed confirmed v1 on main's first-parent line.
- The deploy run list had exactly four IDs: 38410452425, 38416735077, 38416947644, 38513237296.

## Dispatch

One standalone `gh api --method POST` call to `repos/saxton-network/site/actions/workflows/deploy.yml/dispatches`, with `ref=main` and `inputs[sha]=8377801ebd47f8ce1ec96eac9bd807dc5a876273`, exited 0 at 2026-10-14T04:50:08Z. These are exactly the frozen rollback input file's values. No second rollback dispatch or cancel was made.

## Rollback acceptance

- Exactly one new run: [38513444503](https://github.com/saxton-network/site/actions/runs/38513444503), taking the total from four to five. Checked at 2026-10-14T04:50:35Z.
- Run name: `Deploy 8377801ebd47f8ce1ec96eac9bd807dc5a876273`.
- `head_sha`: `95914a54336983fc48e286b8e16cb6780076d2f2`, the expected main tip.
- Attempt 1: reported completed and successful, with `updated_at` 04:50:29Z. Job 115686886735 succeeded.
- The session's authenticated GitHub connection successfully fetched that job's decoded log. The output lines were `DEPLOY HEAD=8377801ebd47f8ce1ec96eac9bd807dc5a876273` and `DEPLOY INDEX_SHA256=495b4b2b4e8c25335184fa994716a888bc9f0980b3196eb633110bde18351eb3`. Only these sanitized output values are recorded.
- Live page: `curl -sS --compressed` with a unique query value at 2026-10-14T04:50:55Z, first try, HTTP 200, body SHA-256 `495b4b2b4e8c25335184fa994716a888bc9f0980b3196eb633110bde18351eb3` (v1).
- Direct main ref at that same check remained `95914a54336983fc48e286b8e16cb6780076d2f2`.

The owner was told promptly that rollback was verified. No emergency settings change or scheduled failure check-in was needed. Main holds the upgrade and v2 while the site serves v1. No retry is approved or planned; the owner decides how to continue. K stays blocked.

## Records divergence

Against records head `7076e620cb598c9f1537cf4f62634a4167bdf4dd` before the J/V results, a non-shallow proof with every inherited `GIT_*` variable removed used `GIT_GRAFT_FILE=/dev/null`, `--no-replace-objects`, and `core.commitGraph=false`:

- `merge-base --is-ancestor 95914a54336983fc48e286b8e16cb6780076d2f2 7076e620cb598c9f1537cf4f62634a4167bdf4dd` exited 0.
- `diff --no-renames --no-relative --ignore-submodules=none --name-only -z` listed 24 paths, all under `agent-work/site-upgrade/`.
- `classify_divergence` with the frozen configuration, validator and installed-script paths returned `protected_change`. The protected changed paths were exactly `CONTRACT.md`, `results/R-dispatch-inputs.json` and `results/R-rollback-inputs.json` under this workflow directory. These are the frozen configuration records allowed after verified rollback, not changed deployment code or validators.
- The J/V results add two paths, making 26 paths in the proposed records PR. Its description carries a fresh proof against its committed head; any other protected path stops landing.

## Secrets and privacy

The earlier file-content scan covered the 26 proposed records files and the messages added since takeover. No secret patterns, email or IP addresses, model identifiers, or private repository references were found in that scope. Two lexical matches in the plan and readiness result are ordinary prose describing a negative test, not repository references. All nine URLs were checked in context; their hosts are the public GitHub and site hosts, and the named repositories were freshly confirmed public through the authenticated connection. No raw log response, temporary access URL, credential, or private name is recorded.

The subsequent independent review found P7-R1: prohibited attribution trailers in eight inherited records commits would reach main through the proposed merge. Their age does not cure the site-rule violation, and the original records history must not land. The failed review is preserved in `results/records-review-1.md`. A replacement branch starts at the exact source and carries the records as a file snapshot, with the review instruction corrected. Its exact committed candidate still needs a fresh secrets and privacy scan and review by the same independent reviewer before the owner is asked to approve landing.

## Records landing boundary

Rollback acceptance remains PASS. The first V record is marked `failed` at the records-review stage because of P7-R1; the second V attempt is a records-only repair, `in_progress` pending re-review, not another rollback dispatch. V will be recorded `complete` before any merge because records cannot prove their own merge. Original PR #4 is blocked, and the clean replacement is prepared for the same reviewer and the owner's separate go-ahead. Its changes are limited to `agent-work/site-upgrade/`. No replacement review pass or merge is claimed. Landing uses a local `git merge --no-ff`, pushed as a fast-forward of an asserted literal commit, followed by an API check that the PR is merged and fresh main/live checks. Those later facts are reported outside these records.

## Pilot observation

The CLI deployment-log read failed after a redirect, while the session's authenticated GitHub connection could read deployment logs. This did not justify weakening acceptance or retrying J: the failed attempt was preserved and the approved rollback was performed. No vendored file, validator, deployment workflow, or frozen input was changed.
