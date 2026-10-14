# Plan: upgrade `saxton-network/site` to Workflow v0.1.0-alpha.14 and put v2 live (Pilot 9)

Status: revision 2, approved by the owner on 2026-10-14 with owner decisions 1–5; decision 2 is (a), reword the site's "Git identity" rule. Revision 2 applies plan-review round 1 (M1–M5, L1–L8, N1–N5); round 2 approved it, and its optional L9 and N6 are folded in as clarifications that make the plan stricter. It is modelled on the approved Pilot 7 plan (`agent-work/site-upgrade/PLAN.md` in the site repository). Differences are called out.

## Goal

1. **Upgrade the site again.** Move the site's vendored Workflow files from `v0.1.0-alpha.13` (`84d826a`) to `v0.1.0-alpha.14` (`02c771a`), following `docs/ADOPTING.md` section 2. This is the second upgrade, and the first using an adopter guide that already carries the Pilot 7 lessons.
2. **Put v2 live.** `main` holds v2, the page with the "Last updated" line, but the site still serves v1, because Pilot 7's acceptance failed on a log read and the correct deploy was rolled back. One reviewed deploy of the upgraded `main` head publishes v2.
3. **Use Pilot 7's lesson where it hurt.**
   - Decide before approval which tool reads each piece of acceptance evidence, above all the deploy job log.
   - Prove at readiness that each tool can read it.

Where the procedure, the helper or the docs get in the way, that is a pilot finding: recorded and reported, not patched during the run.

## What changes

### The upgrade (task A)

**Five vendored files change.** They are copied byte for byte from the published `workflow-v0.1.0-alpha.14.zip`, whose digest `1b87fa4a7034e58efaf0c8479b93bb82d4d3bad2c8fb3b467da4f27627d98355` is checked on download. Each copy is also checked against `git show 02c771a:<path>`:

- `agent-work/WORKFLOW-SPEC.md`
- `agent-work/COORDINATOR.md`
- `agent-work/RESULT-TEMPLATE.md`
- `docs/THREAT-MODEL.md`
- `scripts/agent-task.py` (new SHA-256 `8ec1b22cd97d10e1873ed9dfa83a37fa58f036914452f1af6508564215748f3c`)

**Three are byte-identical in alpha.14:** `agent-work/README.md`, `agent-work/EVIDENCE-MANIFEST.md` and `docs/agent-worktrees.md`. Only the source commit in their rows changes.

**`ADOPTION.md`:**

- **The header** keeps the history: adopted at `3d38b27`, upgraded to alpha.13 (`84d826a`), then to alpha.14 (`02c771a`).
- **The rows.** All eight keep the four-column form with source commit `02c771a`, and the five changed rows get their new hashes.
- **"Upgrades".** This prose section gains a second entry. It records:
  - the ZIP digest, and that the tag `v0.1.0-alpha.14` is lightweight at `02c771a`;
  - that the copies equal both the ZIP and the commit;
  - which ambiguities alpha.14 newly answers, if any. `docs/ADOPTING.md` now says where owner decisions go and how to name the commit identity, which bears on ambiguity 17. It also says to keep a working gate's row form, which bears on the row-format note, and asks readiness to prove the client that reads the deploy evidence (section 7).
- **"Copied files" prose.** Its sentence naming the release commit of every row changes from `84d826a` to `02c771a`. No stale `84d826a` remains except in history text.

  As before, no hash sits in a table row that starts with a backtick.

**`AGENTS.md` (owner decision 2).** Only if the owner approves, the site's "Git identity" rule is reworded as `docs/ADOPTING.md` now advises, naming no person or address:

> **Git identity.** Agents commit only as the mandated no-reply commit identity (the one the "Commit metadata" bullet exempts), never as a personal identity. Whoever takes over checks `git config user.name` and `user.email` against this rule before the first commit; if they do not match, stop and ask the owner. Agents make merges into `main` locally under that identity and push them; agents do not use GitHub's merge button or merge API, because those author the merge as the owner's account. This rule binds agents, not the owner's own actions. Existing history is not rewritten.

The history already holds commits this rule would not allow an agent to make: merges made through GitHub (such as site PR #6) and the Pilot 7 records commits under a personal identity. Nothing is rewritten.

**Nothing else changes:**

- `site/index.html` stays v2, SHA-256 `1f60283e1c442f0fd8e0015787c84febd2b37eabfe83bc9dbea54e7b345f7a35`. The date line keeps "Last updated 13 October 2026", the owner's earlier choice: the content has not changed since then.
- `scripts/check-site.py`, `scripts/projects.txt`, `scripts/validate.sh` and `.github/workflows/deploy.yml`.
- The existing workflow records.

### The live change (task J)

One dispatch of `deploy.yml` with `sha` = the upgraded `main` head. The live page changes from v1 (`495b4b2b4e8c25335184fa994716a888bc9f0980b3196eb633110bde18351eb3`) to v2.

## Deployment authority

`origin` `refs/heads/main`, as the site's `AGENTS.md` declares. The deploy guard accepts only commits on `main`'s first-parent line. Today v1 (`8377801`) is seventh on that line (`16c3631`, `a3aa6b4`, `95914a5`, `ae90609`, `8f3c310`, `d28afc4`, `8377801`), and a fast-forward keeps it on that line.

## Task graph (workflow ID `site-upgrade-14`)

| Task | Kind | What it does | Depends on |
| --- | --- | --- | --- |
| A | implementation | On `pilot/site-upgrade-14-impl`, from `main` at `16c363137b52093fcd014ee00d8c4a8ca570e658`, do the upgrade above (and the `AGENTS.md` wording only under decision 2). `bash scripts/validate.sh` passes with the new helper, and Validate CI is green. | — |
| B | independent_review | A separate reviewer, pinned to a different model from the builder and checked every round. It checks five things:<br>(1) each vendored file equals the ZIP and `git show 02c771a:<path>`, and the tag is lightweight at `02c771a`;<br>(2) only the vendored files, `ADOPTION.md` and (under decision 2) `AGENTS.md` changed, while `site/index.html`, `check-site.py`, `projects.txt`, `validate.sh` and `deploy.yml` are byte-identical to `16c3631`;<br>(3) site rules and privacy, including that both listed repositories are still public. The briefing lists the decisions recorded in `ADOPTION.md`, including ambiguity 17, and the "Commit metadata" exemption in `AGENTS.md`;<br>(4) the existing workflows' helper labels, compared before and after;<br>(5) `CONTRACT.md`.<br>Verdict `passed` or `findings`. | A complete |
| C | repair (conditional) | Fixes B's findings on `pilot/site-upgrade-14-fix`, and the same reviewer re-reviews. A further round resets B to `findings` and C to `pending`. Stop after two rounds. | B findings |
| P | authority_promotion | In a non-shallow clone, `if ! …; then exit 1; fi` gates prove three things: `main` is still `16c3631`, the candidate descends from it, and v1 stays on the candidate's first-parent line. Then a separate push of the asserted literal SHA fast-forwards `main`, and the remote ref is verified. | B passed |
| R | release_readiness | Read-only checks and the frozen batch, below. | B passed, P complete |
| J | live_deployment (human gate) | The owner's y/n, one dispatch, and runtime acceptance. | R complete |
| V | other, `required_status = {J = "failed"}` | The coordinator's rollback, its acceptance, and the records. Not ready when J records `liveStateChanged: false`. | J failed |
| K | final_reconciliation | Verify the refs and the live page, and land the records. | J complete with runtime acceptance PASS |

**Records branch and helper.**

- The scaffold is compiled on `pilot/site-upgrade-14-records`, based on `16c3631`, before A. It is reviewed independently, and the scaffold review checks every version, SHA, run count, deployment count, workflow ID and branch name against this plan (Pilot 8 finding 1).
- That base has the alpha.13 helper, so the scaffold is validated with both the alpha.13 and the alpha.14 helper (from a scratch copy).
- After P, the coordinator merges the source into the records branch (non-force) before R. From then on every gate check uses the alpha.14 helper.
- R reads the helper's SHA-256 from the file (expected `8ec1b22c…748f3c`).

**Commit identity.** Before the first commit on each branch, the coordinator checks `git config user.name` and `user.email` against the no-reply identity (`COORDINATOR.md` Startup step 10). Every merge into the site's `main` is made locally under that identity and pushed. GitHub's merge API is not used.

**Handover.** If a different coordinator takes over before J, it:

1. checks `git config user.name` and `user.email` against `AGENTS.md` before any commit;
2. re-proves every row of the evidence-client table with its own tools, and records it;
3. shows the preview again before asking the question;
4. runs its own pre-dispatch recheck.

Until all four are done, J is not dispatched.

## Main freeze

Nothing else merges into the site's `main` from P until one of these happens:

- J's runtime acceptance passes;
- V verifies a rollback;
- after a proven `liveStateChanged: false`, the owner says how to continue.

The freeze is by agreement. A breach is detected by the pre-dispatch recheck, the run's `head_sha` check, and acceptance check 4.

## Readiness checks (R)

- **Source.**
  - `origin/main` equals the source, in a non-shallow clone with no inherited `GIT_*` variables.
  - `validate.sh` passes at the source in a clean worktree.
  - Validate CI is green on the source.
- **Content only, apart from the upgrade.** Between v1 and the source, `deploy.yml`, `check-site.py`, `projects.txt` and `validate.sh` are byte-identical.
- **Rollback proven.**
  - `deploy.yml`'s guard and site check run locally, in a full clone with `origin/main` at the source.
  - They pass for v1 and for the source.
  - A commit from a merged side branch is rejected.
- **Listed repositories are still public.** This is read from the authenticated `private` and `visibility` fields.
- **Evidence access (new).** R proves every read in the contract's "Evidence clients" table, with its primary client and, where it has one, its fallback, on the latest earlier deploy run (38513444503, the v1 rollback) and the live page:
  - the run, its `run-name` and its job steps;
  - the job log's `DEPLOY HEAD` and `DEPLOY INDEX_SHA256` lines, read through the connection, and, if it works, through `curl` from the job-logs API;
  - the `github-pages` deployment list;
  - the live page bytes;
  - `main`.

  - **Both clients.** For every item with a fallback, R reads both clients and records that they agree. A 404 counts as evidence, not as an error.
  - **Dispatch client.** R checks that the connection's dispatch and cancel tool is available and permitted, without dispatching.
  - **What cannot be proven.** Any read R cannot prove is a stop condition, except a fallback that does not work. That is recorded as "no fallback" before approval.
  - **Authentication.** R records how each client authenticates.
  - **What is recorded.** Records name the client and the kind of identity (the session's account) only. Tokens, headers, redirect or signed URLs and raw log bodies are never recorded, only the two `DEPLOY` output values.
- **Baseline.**
  - The live page: status 200, SHA-256 = v1.
  - The `deploy.yml` run list: 5 runs today.
  - The `github-pages` deployment IDs: 5 today.
- **Frozen batch.**
  - **Source:** the candidate, after P.
  - **`deployableArtifactSha256`:** `site/index.html` at the source.
  - **`deploymentConfiguration`:**
    - `.github/workflows/deploy.yml`;
    - `agent-work/site-upgrade-14/results/R-dispatch-inputs.json` (`sha` = source);
    - `agent-work/site-upgrade-14/results/R-rollback-inputs.json` (`sha` = `8377801ebd47f8ce1ec96eac9bd807dc5a876273`);
    - `agent-work/site-upgrade-14/CONTRACT.md`.
  - **`validators`, at the source:**
    - `scripts/check-site.py`;
    - `scripts/projects.txt`;
    - `scripts/validate.sh`;
    - `scripts/agent-task.py`.
  - **`installedScripts`:** none.
  - **`rollbackArtifact`:** `git:8377801ebd47f8ce1ec96eac9bd807dc5a876273`, provenance `agent-work/site-upgrade-14/results/R-rollback-v1.md`.
  - **`deploymentTargets`:** `https://saxton-network.github.io/site`, mode `null`.

## Contract (`CONTRACT.md`)

`CONTRACT.md` writes every hash in full.

### Accepted unknowns

- **CDN caching.** Visitors may see either version for up to about 10 minutes.
- **Runner and action internals.** The live byte comparison covers them. GitHub altering the served bytes is a finding, never a reason to loosen a check.
- **Deployment labels.** GitHub labels a Pages deployment with `main`'s tip, not the deployed input. Only the job log's `DEPLOY` lines and the live bytes are evidence of what is live.

### Evidence clients

This table is decided before approval and proven at readiness. The connection is the session's authenticated GitHub connection. `curl` goes through the session's network proxy, which authenticates it as the same account, so it is a different program and request path, not a different identity.

| Check | Item | Primary | Fallback |
| --- | --- | --- | --- |
| Run | Run list, `head_sha`, `run-name`, conclusion | connection | `curl` (Actions API) |
| Run | Job-step list | connection | `curl` (Actions API) |
| Run | Job log `DEPLOY HEAD` and `DEPLOY INDEX_SHA256` lines | connection (job logs) | `curl` (job-logs API), only if R proves it; otherwise none |
| Live | Page bytes and status | `curl --compressed` with a cache-busting query | none (never a tool that converts HTML to text) |
| Live | `github-pages` deployment IDs | `curl` (deployments API) | none |
| Refs | `refs/heads/main` | `git ls-remote` | `curl` (git refs API) |
| Readiness | Validate CI status on the source | connection | `curl` (Actions API) |
| Readiness | Listed repositories' `private` and `visibility` | connection | `curl` (repos API) |
| Action | The dispatch (v2 or rollback) and any cancel | connection (Actions run-trigger tool) | none; an error is never retried |

The rules:

- **When the fallback is used.** Only when the primary returns no evidence: an error, a timeout, or the item not yet visible.
- **When both are read.** They must agree, and a disagreement is a FAIL.
- **No other substitutes.** No other client stands in for a missing read.

### Dispatch

- **Recheck, seconds before dispatch.** Its output is read clean before dispatching. It covers:
  - `origin/main` equals the source, and its tip is recorded;
  - the frozen hashes and the recomputed fingerprint;
  - the live page is v1;
  - the `deploy.yml` run IDs and the `github-pages` deployment IDs equal the baseline.
- **If the recheck fails:** dispatch nothing, leave J `in_progress`, stop and ask the owner.
- **The dispatch** is a single tool call of its own. If it errors, or no single new run appears within 2 minutes, never dispatch again; stop and ask the owner.
- **Waiting.** Wait up to 45 minutes for the run, because the job's 20-minute limit does not count queue time.
  - If the run is still running after that, cancel it, then wait up to 10 more minutes for `completed`.
  - If it is still not completed, record J `failed` with `liveStateChanged: null`, and ask the owner.

### Runtime acceptance

There is one acceptance window: 10 minutes. It starts at the coordinator's first observation that the run is `completed`, which J.md timestamps, and the coordinator polls at least every minute while waiting. Checks 1–3 run in order and stop at the first failure. Check 4 is always read. If check 1 or 2 fails, the live page is still read once. That read is not counted as acceptance; it supports `liveStateChanged` and V.

**Retry rules within the window:**

- **No evidence.** A read that returned no evidence (an error, a timeout, or not yet visible) may be repeated with the same client, or with its fallback.
- **Failing evidence.** Evidence that fails a check is a FAIL and is never re-read to get a different answer. The one exception is check 3, the live page, where a 200 with v1's exact bytes means "not yet visible" because of the CDN.
- **Window ends.** If there is still no evidence when the window ends, the check fails.
- **Late evidence.** Evidence obtained after a check has failed never turns it into a pass.
- **No second dispatch.** A repeated read is never a reason to dispatch again.

**The checks:**

1. **The run.**
   - Exactly one new `deploy.yml` run.
   - `head_sha` equals the recorded `main` tip.
   - `run-name` is `Deploy <source>`.
   - Conclusion: success.
2. **The log.** It shows `DEPLOY HEAD=<source>`, and `DEPLOY INDEX_SHA256=` the frozen `deployableArtifactSha256` (`1f60283e1c442f0fd8e0015787c84febd2b37eabfe83bc9dbea54e7b345f7a35`).
   - **What counts.** The evidence is the output lines `DEPLOY HEAD=<40 hex>` and `DEPLOY INDEX_SHA256=<64 hex>`, not the `echo` command lines.
   - **How it is read.** It is read with a line limit large enough for the whole log.
   - **No evidence.** A log that is empty, or whose first lines (the job header, for example `Complete job name:`) are missing, so the read was truncated. The log is final, because the run is `completed`.
   - **FAIL.** A complete log that lacks the lines, or has other values.
3. **The live page.** `curl -sS --compressed 'https://saxton-network.github.io/site/?cb=<nonce>'` is read every 30 seconds:
   - a 200 whose body's SHA-256 equals v2 is a PASS;
   - a 200 with v1's bytes is "not yet visible";
   - any other 200 body is a FAIL;
   - a non-200 status is no evidence.
4. **`main` is unchanged** (`git ls-remote`).

### A wrong run

A wrong run has a wrong `head_sha` or `run-name`, or there is more than one new run. No cancel is attempted, because a Pages run cannot reliably be cancelled in time. Instead:

1. Wait until the run is `completed`, within the "Waiting" bounds.
2. Record J `failed` with `runtimeAcceptance: "FAIL"`.
3. Record `liveStateChanged` as below.

### `liveStateChanged` on a failed attempt

It is `false` only when all of these hold, with a one-line reason:

- the run is `completed`, with conclusion `failure` or `cancelled`;
- in the job-step list, the `Run actions/deploy-pages@v5.0.1` step is `skipped` or absent;
- the job log has no deploy-pages output;
- the `github-pages` deployment IDs equal the baseline;
- the live page still returns v1's bytes (supporting evidence only).

Otherwise it is `true`. It is `null` if the step list, the deployments or the job log cannot be read (an error, a timeout or `Forbidden`), or the clients disagree, and `null` is treated as `true`. A repeated read is never used to reach `false`.

A run cancelled while queued has an empty step list and may have no log. An empty step list counts as "absent". A log counts as "missing", and so as "no deploy-pages output", only when the step list is empty and the API reports no log (a 404 or an empty body), never because a read failed.

### Rollback (V)

V runs only after J has failed with `liveStateChanged` not `false`.

1. Make sure the J run is `completed`. If it is still not completed after the post-cancel bound, V does not dispatch; the owner decides.
2. Recheck the hashes of `R-rollback-inputs.json` and `deploy.yml`, and `main`.
   - If `main` still equals the source, go on.
   - If `main` moved, go on only if all of these hold, recording the new tip as V's `head_sha` expectation:
     - the move is a proven additive descendant;
     - v1 is still on the first-parent line;
     - `deploy.yml` has the frozen hash.
   - Otherwise stop and ask the owner.
3. Dispatch once with `sha` = v1, and never repeat it.
4. Rollback acceptance uses the same evidence clients and window rules, with v1 in place of v2:
   - exactly one new run;
   - `run-name` `Deploy 8377801ebd47f8ce1ec96eac9bd807dc5a876273`;
   - success, with the expected `head_sha`;
   - the log shows `DEPLOY HEAD=8377801…` and `DEPLOY INDEX_SHA256=495b4b2b…51eb3`;
   - the live bytes equal v1. For the live page:
     - a 200 whose body equals v1 is a PASS;
     - a 200 with v2's exact bytes is "not yet visible";
     - any other 200 body is a FAIL;
     - a non-200 status is no evidence;
   - `main` is unchanged.
5. If the rollback or its acceptance fails, stop and tell the owner at once. Their emergency option is GitHub Settings → Pages → "Unpublish site". It takes the whole site offline (404), so it is for an exposure problem, not a content slip. The coordinator schedules one read-only check-in at T+30 minutes for as long as that state lasts.

End state: "stopped after verified rollback".

### No rollback needed

When `liveStateChanged: false` is proven:

- V is recorded `failed`, with "rollback not needed", and K stays blocked.
- The end state is "stopped; nothing published, proven".
- The coordinator asks the owner how to continue.
- The records land through a reviewed PR on the owner's go-ahead, with a deviation note for the expected `protected_change`.
- A retry after the records land starts again from A and B, because `main` will have moved. The owner chooses whether to land the records before or after a retry.

### Retry boundary

- One v2 dispatch and one rollback dispatch.
- Any retry needs fresh readiness and a new approval, and J's status is reset to `pending` when that cycle starts.

## Approval record (J)

`agent-work/site-upgrade-14/results/J-approval.md` follows `COORDINATOR.md` "Approval records". It records:

- when the preview was shown, the question, and the owner's answer as given;
- that the platform offers no message link;
- the source and the fingerprint;
- the approved actions:
  - the v2 dispatch, with `R-dispatch-inputs.json` and its hash;
  - the rollback dispatch, with `R-rollback-inputs.json` and its hash, only under "Rollback (V)";
  - a cancel, only for a run still going after 45 minutes;
- that no other cancel is approved;
- what the approval does not cover;
- that it is the coordinator's own account of a chat approval;
- any dated plan clarifications in force.

## Live preview (J), in plain language

- **What changes for visitors.** The "Last updated" line appears. The upgrade itself is invisible to them.
- **Not new exposure.** v2 was public during Pilot 5's drill and during Pilot 7's run.
- **`main` already holds the upgrade before the answer.** A "no" leaves the site on v1, which is a valid end state: "owner declined".
- **Time.** About 1–2 minutes normally. The worst case is roughly 70 minutes.
- **Caching.** Visitors may see either version for about 10 minutes.
- **The evidence tools, decided in advance.** If the tools cannot read the evidence within the 10-minute window, that counts as a failure and the coordinator rolls back to v1, even if v2 was correct. Readiness proves the tools first, including the deploy-log read that failed in Pilot 7.
- **The owner only answers.** The coordinator does the rollback if one is needed.
- **A handover.** If another coordinator takes over before the deploy, it re-proves the tools, shows this preview again and rechecks before doing anything.
- **The batch.** The two possible dispatches, the source, the fingerprint, the checks and the stop conditions.
- **The emergency option.** Unpublish, with its exact path and what it does.
- **The retry boundary and the freeze.**
- **The end states.** Complete; stopped after verified rollback; stopped with nothing published, proven; owner declined.
- **Clarifications.** Any plan clarifications in force.

The question is: "Approve, and can you be reached within about 30 minutes if the rollback itself fails? (y/n)". A "y" without that availability counts as "n".

## Records

`agent-work/site-upgrade-14/` is kept on `pilot/site-upgrade-14-records`.

**The site records PR**, opened in K or V:

- It adds only that directory.
- It has a divergence proof with no inherited `GIT_*` variables. The expected `protected_change` is exactly `CONTRACT.md` and the frozen `results/R-*` files.
- It has a secrets and privacy scan.
- Any protected path other than `CONTRACT.md` and the `results/R-*` files stops the landing.
- It is reviewed independently. The records review also checks that commit messages and authors contain only the mandated identity and the trailers the "Commit metadata" exemption allows (Pilot 7's P7-R1).
- The task (K or V) is recorded `complete` before the merge, because records cannot prove their own merge. The merge commit and fresh checks of `main` and the live page are reported afterwards, outside the records.
- It lands on the owner's go-ahead: a local `--no-ff` merge under the no-reply identity, pushed as a fast-forward under the ref-move rules, and never through GitHub's merge API.
- The API must then show the PR as merged. If it does not, the coordinator closes the PR with a comment naming the merge commit.

**A short Workflow PR** then adds a "Pilot 9" entry to `docs/PILOT-HISTORY.md`. It is reviewed, and landed the same way on the owner's go-ahead.

## Owner decisions

1. Approve this plan.
2. The site's "Git identity" rule:
   - (a) reword it as shown under "What changes" (recommended): agents use only the no-reply identity, a handover checks it, and agents merge locally. GitHub's own merge button puts your account name and email into the public history, which the site's own rule forbids for agents. Nothing already in the history is rewritten;
   - (b) leave it as it is.
3. A freeze on the site's `main` from P until runtime acceptance passes, a rollback is verified, or the owner says how to continue.
4. The coordinator may redeploy v1 itself as the rollback, under the same approval.
5. The acceptance read rules, in plain words: each piece of proof is read by one named tool. Where a second tool is listed, it is used only if the first gives no answer. If no tool can read a proof within 10 minutes, the deploy is treated as failed and the old page is put back, even if the new page was fine.
6. Later:
   - the y/n on the live preview;
   - the go-ahead for the site records PR;
   - the go-ahead for the Workflow history PR;
   - the go-ahead for a repair, only if B finds anything.

## Stop conditions

- B is not clean after two repair rounds.
- CI is red on the candidate.
- The release ZIP's digest does not match, or the copies differ from `02c771a`.
- `main` moves unexpectedly.
- Readiness is not `PASS`, including any required evidence read it cannot prove.
- The helper shows an unexpected gate state.
- Any dispatch or acceptance stop condition above.

## Expected helper behaviour (alpha.14 helper)

| When | Expected |
| --- | --- |
| Before R | J `GATED` |
| After R `PASS` | J `PREVIEW` |
| After the approval record | J `READY` (a handoff only) |
| On success | J `DONE`, K `READY` |
| On failure with `liveStateChanged` `true` or `null` | J `GATED`, V `READY`, K never ready |
| On failure with `liveStateChanged: false` | V not ready; its task view says no rollback is needed |
| J's manifest status `failed` | J `GATED`, with the matching message |
| After a failed recheck (J left `in_progress`) | J may still show `READY`; not a finding |
| The existing `site-launch`, `site-update-drill` and `site-upgrade` workflows | The same labels as with the alpha.13 helper |

## Clarifications

Dated entries go here, as in the Pilot 7 plan:

- a stricter check, or an equal or stronger proof, is recorded before the task runs;
- the next independent review checks it;
- the next owner preview lists it.

Anything weaker or wider, or anything that changes the live batch, needs a revised plan and a new approval.

## Out of scope

- Changing the page's content.
- Site finding F8(b), which the owner left as is.
- Changes to deploy code, the threat model or the spec during the run.
