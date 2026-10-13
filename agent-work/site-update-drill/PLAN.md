# Pilot plan: `saxton-network/site`, a first real project run through Workflow

Status: revision 3, approved by the owner on 2026-10-13 with all recommended decisions. This is the identical copy for `site-update-drill`; the `site-launch` copy differs only in this line. Where the "Owner clarifications during the run" at the end differ from the text above, the clarifications govern.

## Goal

Run Workflow, for the first time, on a project other than itself: a new, one-page public website. This tests three things the two pilots inside `saxton-network/workflow` could not:

1. **Adoption by a newcomer.** A fresh agent sets up Workflow in a new repository using only Workflow's README and docs, and logs every ambiguity.
2. **A deployment with a live target.** A GitHub Pages site, where runtime acceptance compares the live page's bytes with the reviewed source.
3. **A rollback the coordinator performs itself.** A drill makes the second deploy fail on purpose, and the coordinator restores the first version by redeploying it.

Findings are recorded in the site repository's records. At the end, a `docs/PILOT-HISTORY.md` entry in `saxton-network/workflow` lands through a reviewed PR. Nothing in Workflow is patched during the run.

## The project

- **Repository:** `saxton-network/site`. It is public, because Pages on a private repository needs a paid plan, and has no license file, like `workflow`. The coordinator creates it through the GitHub connection.
- **Live page:** `https://saxton-network.github.io/site/`. In Workflow evidence the destination is written `https://saxton-network.github.io/site`, because the accepted format has no trailing slash.
- **Content:** `site/index.html`, a landing page titled "Saxton Network". It lists the organisation's public repositories, `saxton-network/workflow` and `saxton-network/chudley`, each with its GitHub description and a link. No other repository is named anywhere in the site repository.
  - The exact v1 text is in the bootstrap PR, for the reviewer to read.
  - `site/` holds only `index.html`.
- **Deploy workflow:** `.github/workflows/deploy.yml`.
  - Trigger: `workflow_dispatch` only, so there is never a deploy on push.
  - Input: one `sha`, passed through `env`. It must be 40 lowercase hex characters and an ancestor of, or equal to, `origin/main` (`fetch-depth: 0`, then `git merge-base --is-ancestor`). Otherwise the run fails before uploading anything.
  - Run setup:
    - `run-name: Deploy <sha>`
    - `permissions: contents: read, pages: write, id-token: write`
    - `environment: github-pages`
    - `concurrency: {group: pages, cancel-in-progress: false}`
  - Steps, in order:
    1. Check out exactly `sha`.
    2. Fail unless `site/` contains only `index.html`.
    3. Run the site check.
    4. Echo `git rev-parse HEAD` and the SHA-256 of `site/index.html` to the job log, read later through the job-logs tool, and also to the run summary.
    5. Upload `site/` and deploy.
  - Actions are pinned to exact release tags, which the builder verifies exist.
  - **Known fact:** Pages records the run's `GITHUB_SHA`, which is the `main` tip at dispatch, not the `sha` input. The `deploy.yml` that runs is always `main`'s. Proof of what was deployed is therefore the `run-name`, the job log, and the live bytes.
- **Checks:**
  - `scripts/check-site.py` fails unless:
    - there is no `<script>`, `<link>`, `<img>`, `<iframe>`, `url(` or `@import`;
    - every `href` is `https://github.com/saxton-network/<repo>`;
    - the listed repositories exactly match `scripts/projects.txt`.

    It does not claim full HTML validation.
  - `scripts/validate.sh` runs:
    - the site check;
    - a check that every adopted Workflow file still has the hash recorded in `ADOPTION.md`;
    - `python3 scripts/agent-task.py <workflow> --all` for each workflow directory.
  - `.github/workflows/validate.yml` runs `validate.sh` on every push and pull request.
- **Commit identity.** All commits use the coordinator's no-reply identity; builder agents run with `GIT_AUTHOR_*` and `GIT_COMMITTER_*` set to it. GitHub's merge button is never used, so no personal email enters the history.
  - **Creating the repository.** The coordinator creates it with no initial commit, then pushes the root commit with git. A commit made through the GitHub connection would carry the owner's account identity.
  - **Moving `main`.** `main` moves only by non-force pushes that fast-forward it (`git push origin <sha>:refs/heads/main`), after a fresh fetch and an ancestry check. The remote ref is verified afterwards.
  - **Promotions.** Each workflow's A branch starts from the current `main` tip, so promotion (P) is a pure fast-forward.
  - **Records.** Records cannot fast-forward, because `main` moved at P. They land by a merge commit built locally under the no-reply identity (`git merge --no-ff` of the records branch into `main`). That merge descends from `main`, so pushing it is still a fast-forward. The changed-paths proof is recorded.
  - **PR status.** GitHub is expected to mark a PR merged once its head is reachable from `main`. The coordinator verifies this through the API; if not, it closes the PR with a comment pointing at the merge commit.

## Bootstrap, before any workflow: adoption by a newcomer

1. **Checklist first.** Before the builder starts, the coordinator writes a hidden adoption checklist: what a correct adoption must contain, based on Workflow's docs. The builder never sees it; the reviewer uses it.
2. **Build.** A fresh builder agent may read exactly these files of Workflow: `README.md`, the five `agent-work/*.md` docs, `docs/THREAT-MODEL.md` and `docs/agent-worktrees.md`. It is not given `docs/PILOT-HISTORY.md` or any pilot records. It also gets the instruction "adopt Workflow into this new repository for a GitHub Pages site whose deployment authority is `origin` `refs/heads/main`", and the site requirements above. It is given no pilot records. On a branch it creates:
   - `AGENTS.md`;
   - the adopted files;
   - `ADOPTION.md`, recording each copied file's source path in `saxton-network/workflow` at `3d38b27`, its SHA-256, and every ambiguity hit;
   - `scripts/validate.sh`, which skips a missing `check-site.py` with a printed note and accepts zero workflow directories;
   - `validate.yml`;
   - a placeholder `site/index.html`.

   It does not create `deploy.yml` yet.
3. **Adopted set:**
   - `agent-work/` `README.md`, `WORKFLOW-SPEC.md`, `COORDINATOR.md`, `EVIDENCE-MANIFEST.md` and `RESULT-TEMPLATE.md`;
   - `scripts/agent-task.py`;
   - `docs/THREAT-MODEL.md` and `docs/agent-worktrees.md`;
   - optionally `examples/deployment/manifest.toml`.

   Workflow's own `validate-repository.sh` and tests are not copied, because they are Workflow-specific. The README's Quick start names that script without saying to copy it; this is recorded as a finding.
4. **Review.** An independent reviewer, on a different model from the builder, checks the PR against the checklist and the threat model. The review is recorded as one PR comment ("Durable review records").
5. **Merge.** After the owner's go-ahead, the coordinator fast-forwards `main` to the reviewed commit. That commit is `phase_baseline` for `site-launch`.

## Workflow 1: `site-launch` (deploy v1)

| Task | Kind | What it does |
| --- | --- | --- |
| A | implementation | On branch `pilot/site-launch-impl`, builds the real `site/index.html`, `scripts/projects.txt`, `check-site.py` and `deploy.yml`. |
| B | independent_review | Different-model reviewer. Includes a privacy read of the page and the repository: no private names, infrastructure or personal details. |
| C | repair (conditional) | Fixes B's findings; the same reviewer re-reviews. |
| P | authority_promotion | Non-force fast-forward of `main` to the reviewed commit; verify the remote ref afterwards. |
| R | release_readiness | Read-only checks and the frozen batch (below). |
| J | live_deployment (human gate) | Owner y/n; one dispatch; runtime acceptance. |
| K | final_reconciliation | Verifies refs and live state; lands the records by fast-forward after review and the owner's go-ahead. |

**Rollback for v1:** the owner unpublishes Pages (Settings → Pages → Unpublish site), and the coordinator polls until the page returns 404. Unpublishing is only for an exposure problem; a content mistake is fixed by a new reviewed update. Rollback identity: `pages-unpublished-404`.

## Workflow 2: `site-update-drill` (deploy v2, fail on purpose, restore v1)

Modelled on Pilot 4.

| Task | Kind | What it does |
| --- | --- | --- |
| A | implementation | v2: adds a "Last updated" line. |
| B | independent_review | Different-model reviewer: the change, plus the drill contract. |
| C | repair (conditional) | Fixes B's findings; the same reviewer re-reviews. |
| P | authority_promotion | Fast-forward `main` to v2. |
| R | release_readiness | As below, plus the local proof of the injected fault. |
| J | live_deployment (human gate) | Deploy v2; acceptance fails on the injected check; stop; record J `failed`. |
| V | other, `required_status = {J = "failed"}` | **The coordinator's rollback:** one dispatch of `deploy.yml` with `sha = <v1>`. It then verifies the live bytes equal v1, records the drill verdict, and lands the records. |
| K | final_reconciliation | Declared, never ready. The workflow ends "stopped after verified rollback". |

- **Injected fault, a declared exception as Workflow's spec requires.**
  - Readiness freezes two expectations: the correct SHA-256 of v2's `index.html`, and an injected one of 64 zeros. It proves locally that they differ.
  - Acceptance check 2 is split in two:
    - **2a:** poll for up to 10 minutes until the live hash equals the correct v2 hash. This proves v2 really went live.
    - **2b:** compare the live hash once with the injected value. It fails at once, with no retry.
  - **Expected-failure signature:** 1 and 2a pass, 2b fails, and the live bytes equal v2 exactly. Anything else is a real failure; the rollback still runs.
- **The rollback dispatch is part of the approved batch.**
  - `agent-work/site-update-drill/results/R-rollback-inputs.json` (ref `main`, `sha = <v1>`) is frozen in `deploymentConfiguration`.
  - `rollbackArtifact` is identity `git:<v1 sha>`, with provenance `agent-work/site-update-drill/results/R-rollback-v1.md` holding v1's `index.html` SHA-256 and v1's deploy evidence.
  - The rollback has a retry boundary of one dispatch. If it fails, the coordinator stops and asks the owner.
- **v2's change is content only.** It touches only `site/index.html`. `deploy.yml`, `scripts/` and `check-site.py` stay byte-identical to v1, so the rollback runs the same deploy code that v1's launch did.
- **Rollback acceptance (V).**
  - Exactly one new run, with run-name `Deploy <v1>`.
  - The run log shows `HEAD` = v1 and v1's `index.html` hash.
  - `head_sha` equals the `main` tip.
  - The live bytes' SHA-256 equals v1's hash, polled for up to 10 minutes.
  - `main` is unchanged.
- **End state.**
  - `main` holds v2 while the live page shows v1. This is expected after a drill and is recorded.
  - The records then land on `main` as an expected `protected_change`, which the spec allows after a verified rollback.
  - Bringing the live page back to `main` is a later, normal deploy with its own approval.

## Readiness (R), for both workflows

- **Source:**
  - `origin/main` equals the source;
  - Validate CI is green on the source;
  - `validate.sh` passes at the source.
- **Listed repositories are public:** an unauthenticated GET of each listed repository returns 200 with `private: false`.
- **Baseline:** the live page's status, and for an existing page its SHA-256, fetched with `curl -sS --compressed '<url>?cb=<nonce>'`. Before launch the baseline is "status 404" only; the 404 page's bytes are not stable.
- **Accepted unknown: whether Pages is enabled.** Pages enablement cannot be read without a token, so the owner confirms it.
  - If Pages is not enabled, the deploy fails at the environment step and nothing goes live.
  - That run is still a failed attempt and needs fresh readiness.
- **Frozen batch:**
  - the source SHA;
  - `deployableArtifactSha256`, the SHA-256 of `site/index.html` at the source;
  - `deploymentConfiguration`: `.github/workflows/deploy.yml` (its hash must equal the hash at `main`'s tip at dispatch) and the frozen `agent-work/<workflow>/results/R-*.json` input files;
  - validators, at the source: `check-site.py`, `validate.sh`, `agent-task.py`;
  - `rollbackArtifact`;
  - target `https://saxton-network.github.io/site`, with mode `null`.
- **Records stay off `main` during the live window.** Records live only on `pilot/<workflow>-records` and reach `main` once, in K or V, after acceptance or a verified rollback. Immediately before dispatch the coordinator rechecks that `main` is unchanged since R.

## Runtime acceptance (J)

1. **The run:** exactly one new `deploy.yml` run, with `head_sha` equal to the `main` tip recorded at the pre-dispatch recheck, `run-name` `Deploy <source>`, and conclusion success. Its job log shows `HEAD` = the source and the frozen `index.html` hash.
2. **The live bytes:** `curl -sS --compressed 'https://saxton-network.github.io/site/?cb=<nonce>'` returns 200, and the SHA-256 of the body equals the frozen hash.
   - The coordinator retries every 30 seconds for up to 10 minutes, for CDN propagation.
   - WebFetch is never used, because it returns converted text, not bytes.
3. **`main` is unchanged.**

Acceptance proves what the origin serves. Ordinary visitors may see a cached older page for up to about 10 minutes, including after a rollback. The preview's exposure line says so.

## Live previews

Each live batch gets its own plain-language preview and y/n. For the drill, the same approval covers the v2 dispatch and the one rollback dispatch.

The preview states:

- the source and fingerprint;
- the exact dispatch(es);
- the effects;
- the exposure: a public page, which anyone may cache;
- the checks;
- the stop conditions;
- the rollback;
- the retry boundary: one dispatch each. A retry needs fresh readiness and a new approval.

## Coordinator rules (no owner decision needed)

- Adopt from `saxton-network/workflow` at `3d38b27`. Releasing `v0.1.0-alpha.13` is a separate, later choice.
- Reviewers are a different model from the builder, recorded in words.
- The fresh builder for the bootstrap gets no pilot records and no hints.

## Owner decisions

1. Approve this plan.
2. Let the coordinator create the public repository `saxton-network/site`.
3. **Turn on Pages once, when asked.** This comes after the bootstrap merge and before the first live preview:
   - go to Settings → Pages → "Build and deployment" → Source, and choose "GitHub Actions";
   - then tell the coordinator what the Source dropdown shows. GitHub's exact wording is not frozen.
4. **Approve a deliberate drill in workflow 2.** v2 is briefly public, then the coordinator restores v1. The site then shows v1 while `main` holds v2, until a later normal deploy.
5. **Answer y/n for each live batch:** the launch, and the drill (v2 plus its rollback).
6. **Give a go-ahead to merge each records PR.** That covers the site's two records PRs and the `PILOT-HISTORY` PR in `workflow`.

## Out of scope

- A custom domain.
- JavaScript.
- Automatic deploys.
- Fetching the project list automatically.
- Changes to Workflow itself during the run.

## Owner clarifications during the run

- **Repository creation.** The GitHub connection was refused permission to create repositories in the organisation, so the owner created `saxton-network/site`. GitHub added a starter commit with a README. The owner chose to keep it, so `phase_baseline` history starts from that commit, not a coordinator root commit.
- **Commit metadata.** The owner confirmed that their own name and contact details appearing in commit metadata are fine, because they are already public. The repository's content rules are unchanged: no file, page or record names private repositories, hosts, people or contact details. `main` still moves only by fast-forward to reviewed commits, which is how Workflow pins the deployed source.

- **Deploy guard tightened.** Repair C-1 (finding F3) made `deploy.yml` accept only commits on `main`'s first-parent history, which is stricter than "an ancestor of, or equal to, `origin/main`" above. The rollback to v1 in `site-update-drill` still passes: v1 stays on `main`'s first-parent line.
