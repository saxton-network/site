# Plan: upgrade `saxton-network/site` to Workflow v0.1.0-alpha.13 and put v2 live (Pilot 7)

Status: revision 3, approved by the owner on 2026-10-14 with owner decisions 1–4; decision 2 is (a): keep "Last updated 13 October 2026". It applies the independent plan review's findings SP1–SP15 over two rounds; the second round approved. The reviewer was a separate, read-only agent; the model observed in its transcript differs from the coordinator's.

## Goal

1. **The first real upgrade of an adopter.** Move the site's vendored Workflow files from `3d38b27` to `v0.1.0-alpha.13` (`84d826a`), following `docs/ADOPTING.md` section 2. The copies are taken from the published release ZIP and also compared with `git show 84d826a:<path>`.
2. **Bring the live page back in line with `main`.** `main` holds v2, the page with the "Last updated" line, while the site still serves v1 after the drill. One reviewed deploy of the upgraded `main` head publishes v2.

This is also the first use, in an adopter repository, of the rules alpha.13 ships:

- approval records;
- commands that move refs;
- plan clarifications;
- the pre-dispatch recheck and dispatch-error rules;
- `liveStateChanged`.

The guard-validator rule in the threat model is now in force here too, but this run does not touch `check-site.py`. It is exercised only if a reviewer raises a guard finding. The site's batched F8 is the kind of finding that rule classes as out of scope. The rule does not change the site's own rule that a breach of a content rule is always a defect: the guard rule concerns a guard missing crafted content, not content that breaks the rules.

Where the procedure, the helper or the docs get in the way, that is a pilot finding: recorded and reported, not patched during the run.

## What changes

### The upgrade (task A)

**Five vendored files change.** They are copied byte for byte from the published `workflow-v0.1.0-alpha.13.zip` (digest `e520b61c3c48572b73001d333b2c79499e33b3e5c19f34988d5be2f3e191d5d4`, checked on download) and also checked against `git show 84d826a:<path>`:

- `agent-work/WORKFLOW-SPEC.md`
- `agent-work/COORDINATOR.md`
- `agent-work/EVIDENCE-MANIFEST.md`
- `docs/THREAT-MODEL.md`
- `scripts/agent-task.py` (new SHA-256 `67fa523bd62cf21ad53d969460074982baff1f5b5e1312a086b953e0138f4434`)

**Three files are byte-identical in alpha.13:** `agent-work/README.md`, `agent-work/RESULT-TEMPLATE.md` and `docs/agent-worktrees.md`. Only the source commit in their rows changes.

**`ADOPTION.md`:**

- **History kept.** The header keeps the adoption history: "adopted at `3d38b27`, upgraded to `v0.1.0-alpha.13` (`84d826a`)".
- **Rows.** All eight rows keep the site's four-column form, with the source commit `84d826a`. The five changed rows get their new SHA-256.
- **Files not copied.** `docs/ADOPTING.md` is added, as an adopter's guide on Workflow's own don't-copy list. The reason given for not copying `docs/PILOT-HISTORY.md` is updated.
- **A new "Upgrades" section**, in prose. No hash in it sits in a table row that starts with a backtick, because `validate.sh` would read such a row as a malformed hash row. It records:
  - the step from `3d38b27`;
  - the release ZIP digest;
  - that the tag peels to `84d826a`;
  - that the copies equal both the ZIP and the commit;
  - which of the original 21 ambiguities alpha.13's `docs/ADOPTING.md` now answers, and which remain. For example, ambiguity 7 (a dangling reference) no longer applies.
  - a pilot finding: `ADOPTING.md` shows a three-column row, while this site's gate requires its four-column form.

**Nothing else changes:**

- `AGENTS.md`: Workflow's general rules are unchanged between the two commits.
- `site/index.html`: still v2, SHA-256 `1f60283e1c442f0fd8e0015787c84febd2b37eabfe83bc9dbea54e7b345f7a35`.
- `scripts/check-site.py`, `scripts/projects.txt`, `scripts/validate.sh` and `.github/workflows/deploy.yml`.
- The existing workflow records.

**The reviewer's trial confirmed:**

- `validate.sh` fails on the five drifted hashes until `ADOPTION.md` is updated, then passes.
- The old and new helpers give byte-identical output for the site's two existing workflows.

### The live change (task J)

One dispatch of `deploy.yml` with `sha` = the upgraded `main` head. The live page changes from v1 (`495b4b2b4e8c25335184fa994716a888bc9f0980b3196eb633110bde18351eb3`) to v2.

**The page's date line is the owner's choice (decision 2):**

- **(a) Keep it (recommended).** It stays "Last updated 13 October 2026", which is when the page's content last changed.
- **(b) Change it to the date task A runs (UTC).** This is a content change. It gets the site check and the same review as the upgrade; B reviews the page diff against exactly that one line. If the deploy would fall on a later day, the owner is asked again. Under 2(b), "v2" below means `site/index.html` at the source, and its hash replaces `1f60283e…` wherever that hash appears.

## Deployment authority

`origin` `refs/heads/main`, as the site's `AGENTS.md` declares. The deploy guard accepts only commits on `main`'s first-parent line. v1 (`8377801`) is fourth on that line today (`ae90609`, `8f3c310`, `d28afc4`, `8377801`), and a fast-forward keeps it there.

## Task graph (workflow ID `site-upgrade`)

| Task | Kind | What it does | Depends on |
| --- | --- | --- | --- |
| A | implementation | On `pilot/site-upgrade-impl`, from `main` at `ae90609`, do the upgrade above; plus the date line, under decision 2(b) only. `bash scripts/validate.sh` must pass with the new helper, and Validate CI must be green. | — |
| B | independent_review | A separate reviewer, pinned to a different model from the builder and checked every round. It checks four things. (1) Each vendored file equals both the ZIP and `git show 84d826a:<path>`, and the tag peels to `84d826a`. (2) Only the vendored files and `ADOPTION.md` changed (plus the date line under 2(b)). `check-site.py`, `projects.txt`, `validate.sh` and `deploy.yml` are byte-identical to `ae90609`. (3) Site rules and privacy, including that both listed repositories are still public, read from the authenticated `private` and `visibility` fields. The briefing covers the guard-validator rule versus the site's content rule. (4) The existing workflows' helper labels are unchanged, and `CONTRACT.md` is sound. Verdict `passed` or `findings`. | A complete |
| C | repair (conditional) | Fixes B's findings on `pilot/site-upgrade-fix`, and the same reviewer re-reviews. A further round resets B to `findings` and C to `pending`. Stop after two rounds. | B findings |
| P | authority_promotion | In a non-shallow clone, an explicit `if ! …; then exit 1; fi` gate proves ancestry, and that v1 stays on the candidate's first-parent line. Then a push of an asserted literal SHA fast-forwards `main`, and the remote ref is verified. | B passed |
| R | release_readiness | Read-only checks and the frozen batch, below. | B passed, P complete |
| J | live_deployment (human gate) | The owner's y/n, one dispatch, and runtime acceptance. | R complete |
| V | other, `required_status = {J = "failed"}` | The coordinator's rollback, its acceptance, and the records. It is not ready when J records `liveStateChanged: false`. | J failed |
| K | final_reconciliation | Verify the refs and the live page, and land the records. | J complete with runtime acceptance PASS |

**Records branch and helper.**

- The scaffold is compiled on `pilot/site-upgrade-records`, based on `ae90609`, before A.
- Because that base still has the old helper, the scaffold is validated with both the old helper and the alpha.13 helper, run from a scratch copy. The scaffold review says which it used.
- After P, the coordinator merges the source into the records branch (non-force) before R. From then on, every gate check uses the alpha.13 helper at the source.
- R records the helper's SHA-256 as `67fa523b…4434`.
- The records then descend from the source, as the K/V divergence proof needs.

## Main freeze

Nothing else merges into the site's `main` from P until one of these:

- J's runtime acceptance passes;
- V verifies a rollback;
- after a proven `liveStateChanged: false`, the owner says how to continue.

The freeze is by agreement. A breach is detected by the pre-dispatch recheck, the run's `head_sha` check, and acceptance check 3.

## Readiness checks (R)

- **Source.**
  - `origin/main` equals the source, in a non-shallow clone with no inherited `GIT_*` variables.
  - `validate.sh` passes at the source in a clean worktree.
  - Validate CI is green on the source.
- **Content-only, apart from the upgrade.** Between v1 and the source, `deploy.yml`, `check-site.py`, `projects.txt` and `validate.sh` are byte-identical.
- **Rollback proven.**
  - `deploy.yml`'s guard and site check are run locally, in a full clone with `origin/main` at the source.
  - They must pass for v1 and for the source.
  - A negative control, a commit from a merged side branch, must be rejected.
- **Listed repositories are still public**, from the authenticated `private` and `visibility` fields.
- **Baseline.**
  - The live page: status 200, SHA-256 = v1.
  - The `deploy.yml` run list: 3 runs.
  - The `github-pages` deployment IDs (`GET /repos/saxton-network/site/deployments?environment=github-pages`): 3 today.
- **Frozen batch.**
  - **Source:** the candidate.
  - **`deployableArtifactSha256`:** `site/index.html` at the source.
  - **`deploymentConfiguration`:**
    - `.github/workflows/deploy.yml`
    - `agent-work/site-upgrade/results/R-dispatch-inputs.json` (`sha` = source)
    - `agent-work/site-upgrade/results/R-rollback-inputs.json` (`sha` = `8377801ebd47f8ce1ec96eac9bd807dc5a876273`)
    - `agent-work/site-upgrade/CONTRACT.md`
  - **`validators`, at the source:**
    - `scripts/check-site.py`
    - `scripts/projects.txt`
    - `scripts/validate.sh`
    - `scripts/agent-task.py`
  - **`installedScripts`:** none.
  - **`rollbackArtifact`:** `git:8377801ebd47f8ce1ec96eac9bd807dc5a876273`, provenance `agent-work/site-upgrade/results/R-rollback-v1.md`.
  - **`deploymentTargets`:** `https://saxton-network.github.io/site`, mode `null`.

## Contract (`CONTRACT.md`)

`CONTRACT.md` writes every hash in full.

### Accepted unknowns

- **CDN caching.** A 10-minute retry window covers it. Visitors may see either version for up to about 10 minutes.
- **Pages enablement.** Readiness's 200 baseline and three earlier deploys show it.
- **Runner and action internals.** The live byte comparison covers them. GitHub altering the served bytes is a finding, never a reason to loosen a check.
- **Deployment labels.** GitHub labels a Pages deployment with `main`'s tip, not the deployed input. Only the job log's `DEPLOY HEAD` line and the live bytes are evidence of what is live.

### Dispatch

- **Recheck, seconds before dispatch.** Its output is read clean before dispatching. It covers:
  - `origin/main` equals the source, and its tip is recorded;
  - the frozen hashes and the recomputed fingerprint;
  - the live page is v1;
  - the `deploy.yml` run IDs and the `github-pages` deployment IDs equal the baseline.
- **If the recheck fails:** dispatch nothing, leave J `in_progress`, stop and ask the owner.
- **The dispatch** is a single tool call of its own. If it errors, or no single new run appears within 2 minutes, never dispatch again. Stop and ask the owner.
- **Waiting.** Up to 45 minutes for the run: the job's 20-minute limit does not count queue time.
  - If the run is still running after that, cancel it, then wait up to 10 more minutes for `completed`.
  - If it is still not completed, record J `failed` with `liveStateChanged: null`, and ask the owner.

### Runtime acceptance

Checks 1 and 2 run in order, stopping at the first failure. Check 3 is always read, because it is read-only and V needs it.

1. **The run.**
   - Exactly one new `deploy.yml` run.
   - `head_sha` equals the recorded `main` tip.
   - `run-name` is `Deploy <source>`.
   - Conclusion: success.
   - The log shows `DEPLOY HEAD=<source>` and `DEPLOY INDEX_SHA256=` the frozen `deployableArtifactSha256` (`1f60283e1c442f0fd8e0015787c84febd2b37eabfe83bc9dbea54e7b345f7a35` under decision 2(a)).
2. **The live page.**
   - `curl -sS --compressed 'https://saxton-network.github.io/site/?cb=<nonce>'` returns 200, and the body's SHA-256 equals v2.
   - It is retried every 30 seconds for up to 10 minutes. WebFetch is never used.
3. **`main` is unchanged.**

### A wrong run

Wrong means a wrong `head_sha` or `run-name`, or more than one new run. A Pages run cannot reliably be cancelled in time, so no cancel is attempted. Instead:

1. Wait until the run is `completed`, within the same bounds as "Waiting" (45 minutes, then cancel, then 10 more minutes).
2. Record J `failed` with `runtimeAcceptance: "FAIL"`.
3. Record `liveStateChanged` as below.

### `liveStateChanged` on a failed attempt

It is `false` only when **all** of these hold, with a one-line reason:

- the run is `completed`, with conclusion `failure` or `cancelled`;
- in the job's step list, the `Run actions/deploy-pages@v5.0.1` step has `conclusion: skipped`, or is absent;
- the job log has no deploy-pages output;
- the `github-pages` deployment IDs equal the baseline: no new deployment;
- the live page still returns v1's bytes. This is supporting evidence only, because of the CDN.

Otherwise it is `true`. It is `null` if the step list or the deployments cannot be read, and `null` is treated as `true`.

A run cancelled while still queued has an empty step list and may have no log. An empty step list counts as "absent", and a missing log as "no deploy-pages output", so such a run can meet the `false` proof if the deployment IDs are unchanged.

### Rollback (V)

V runs only after J has failed with `liveStateChanged` not `false`.

1. Make sure the J run is `completed`. If it is still not completed after the post-cancel bound, V does not dispatch. The `pages` concurrency group would queue the rollback behind it, so the order of the two is uncertain. The owner decides.
2. Recheck:
   - the hashes of `R-rollback-inputs.json` and `deploy.yml`;
   - `main`.

   If `main` still equals the source, go on. If `main` moved, go on only if:
   - the move is a proven additive descendant (ancestry from the source, in a non-shallow clone);
   - v1 is still on the first-parent line;
   - `deploy.yml` at the new tip has the frozen hash.

   In that case, record the new tip as V's `head_sha` expectation. Otherwise stop and ask the owner.
3. Dispatch once with `sha` = v1. Never repeat it.
4. Rollback acceptance:
   - exactly one new run;
   - `run-name` `Deploy 8377801ebd47f8ce1ec96eac9bd807dc5a876273`;
   - success, with `head_sha` equal to the expected tip;
   - the log shows `DEPLOY HEAD=8377801…` and `DEPLOY INDEX_SHA256=495b4b2b…51eb3`;
   - the live bytes equal v1, within the 10-minute window;
   - `main` is unchanged since step 2.
5. If the rollback, or its acceptance, fails, stop and tell the owner at once. Their emergency option is GitHub Settings → Pages → "Unpublish site". It takes the whole site offline (404), so it is for an exposure problem, not a content slip. The coordinator schedules one read-only check-in at T+30 minutes for as long as that state lasts.

End state: "stopped after verified rollback". `main` then holds the upgrade and v2, while the site serves v1.

### No rollback needed

When `liveStateChanged: false` is proven:

- V is recorded `failed`, "rollback not needed", and K stays blocked.
- End state: "stopped; nothing published, proven".
- The coordinator asks the owner how to continue.
- The records land through a reviewed PR on the owner's go-ahead, with a deviation note for the expected `protected_change`. A retry after the records land starts again from A and B, because `main` will have moved.

### Retry boundary

- One v2 dispatch, and one rollback dispatch.
- Any retry needs fresh readiness and a new approval.

## Approval record (J)

`agent-work/site-upgrade/results/J-approval.md` follows `COORDINATOR.md` "Approval records". It states:

- when the preview was shown, the question, and the owner's answer as given;
- a message link, where the platform offers one; otherwise a statement that it offers none;
- the source and the fingerprint;
- the approved actions:
  1. the v2 dispatch, with `R-dispatch-inputs.json` and its hash;
  2. the rollback dispatch, with `R-rollback-inputs.json` and its hash, only under the conditions in "Rollback (V)";
  3. a cancel, only for a run still going after 45 minutes;
- that no other cancel is approved;
- what the approval does not cover;
- that it is the coordinator's own account of a chat approval;
- any dated plan clarifications in force.

## Live preview (J), in plain language

The preview tells the owner:

- **What changes for visitors:** the "Last updated" line appears. The upgrade itself is invisible to them.
- **v2 is not new exposure (decision 2(a)):** it was public for about a minute during the drill. Under 2(b), the date line is new content.
- **`main` already holds v2 and the upgrade before the answer,** because P runs first. A "no" leaves the site on v1 with `main` ahead. That is a valid end state, "owner declined".
- **Effort and time:** about 1 to 2 minutes normally. The worst case, with a stuck run, a cancel and then a rollback, is roughly 70 minutes. The owner only answers; the coordinator does the rollback if needed.
- **Caching:** visitors may see v1 or v2 for about 10 minutes.
- **The two possible dispatches**, the source and the fingerprint, the checks, and the stop conditions.
- **The emergency option:** Unpublish, with the exact path and what it does.
- **The retry boundary and the freeze.**
- **The end states:** complete; stopped after verified rollback; stopped with nothing published, proven; owner declined.
- **Any plan clarifications** in force.

The question: "Approve, and can you be reached within about 30 minutes if the rollback itself fails? (y/n)". A "y" without that availability counts as "n".

## Records

`agent-work/site-upgrade/` is kept on `pilot/site-upgrade-records`.

**The site records PR**, opened in K or V:

- It adds only that directory.
- Its divergence proof runs with no inherited `GIT_*` variables. The expected `protected_change` is exactly `CONTRACT.md` and the frozen `results/R-*` files; any other protected path stops the landing.
- It has a secrets and privacy scan.
- The task is recorded `complete` before the merge, because records cannot prove their own merge. The merge commit and a fresh check of `main` and the live page are reported afterwards, outside the records.
- It is reviewed independently and landed on the owner's go-ahead: a local `--no-ff` merge, pushed as a fast-forward under the ref-move rules. The API must show the PR merged; if it does not, the coordinator closes the PR with a comment naming the merge commit.

**A short Workflow PR** then adds a "Pilot 7" entry to Workflow's `docs/PILOT-HISTORY.md`. It is reviewed and merged on the owner's go-ahead.

## Owner decisions

1. Approve this plan.
2. The date line:
   - (a) keep "Last updated 13 October 2026" (recommended); or
   - (b) change it to the deploy date, reviewed with the upgrade.
3. A freeze on the site's `main` from P until runtime acceptance passes, a rollback is verified, or the owner says how to continue.
4. The coordinator may redeploy v1 itself as the rollback, under the same approval.
5. Later:
   - the y/n on the live preview;
   - the go-ahead for the site records PR;
   - the go-ahead for the Workflow history PR;
   - the go-ahead for a repair, only if B finds anything.

## Stop conditions

- B is not clean after two repair rounds.
- CI is red on the candidate.
- The release ZIP's digest does not match, or the copies differ from `84d826a`.
- `main` moves unexpectedly.
- Readiness is not `PASS`.
- The helper shows an unexpected gate state.
- Any dispatch or acceptance stop condition above.

## Expected helper behaviour (alpha.13 helper)

| When | Expected |
| --- | --- |
| Before R | J `GATED` |
| After R `PASS` | J `PREVIEW` |
| After the approval record | J `READY` (a handoff only) |
| On success | J `DONE`, K `READY` |
| On failure with `liveStateChanged` `true` or `null` | J `GATED`, V `READY`, K never ready |
| On failure with `liveStateChanged: false` | V not ready; its task view says no rollback is needed |
| After a failed recheck (J left `in_progress`) | J may still show `READY`; not a finding |
| The existing `site-launch` and `site-update-drill` workflows | Labels as before |

## Clarifications

- **2026-10-14, during task A (a correction, nothing weakened).** "What changes" says ambiguity 7 (a dangling reference) "no longer applies". In fact the alpha.13 threat model still mentions `docs/PILOT-HISTORY.md`. What changed is that `docs/ADOPTING.md` now says such references point back to Workflow. `ADOPTION.md`'s Upgrades section therefore lists 7 as answered, not as gone. The next independent review (B) checks this, and the next owner preview lists it.
- **2026-10-14, after V (records-only branch substitution).** Independent records review P7-R1 blocks landing the original records history because it contains prohibited attribution trailers. The original `pilot/site-upgrade-records` branch, its history and PR #4 are preserved. The replacement `pilot/site-upgrade-records-clean` starts at exact source `95914a54336983fc48e286b8e16cb6780076d2f2` and receives a clean file snapshot of the records, without importing the original records commits or rewriting history. This changes only the records branch used for landing: the frozen batch and its fingerprint, `CONTRACT.md`, and every `results/R-*` file remain untouched. Branch references in `manifest.toml` and `evidence.json` remain accurate historical execution records. The same independent reviewer must review the exact replacement candidate; landing still needs the owner's separate go-ahead for that exact batch. This substitution does not authorize a retry or another live change.

## Out of scope

- Changing the page's content, beyond decision 2(b).
- Fixing the batched Low findings: site F8, and Workflow B1–B4.
- Changes to deploy code.
- Changes to the threat model or spec during the run.
