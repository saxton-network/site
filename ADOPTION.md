# Workflow adoption record

This repository adopts the Workflow framework from the public repository `saxton-network/workflow` at commit `3d38b27749aa0d5ed4cd751ffe64a4359f4f330a`. The adoption followed Workflow's README "Quick start" and the documents it references, reading only the files exported from that commit. It was upgraded to release `v0.1.0-alpha.13` (commit `84d826a40b8f8567439ab15eb270a1a752f92a82`) on 2026-10-14, and then to release `v0.1.0-alpha.14` (commit `02c771a7c7d71e2303c186d0c150e903a524e949`) the same day; see "Upgrades".

`bash scripts/validate.sh` verifies every hash in the table below against the files in this repository.

## Copied files

Each file was copied byte for byte. None was modified. The path in this repository equals the source path. Since the upgrade to alpha.14, every row names the release commit `02c771a`.

| Path in this repository | Source path | Source commit | SHA-256 |
| --- | --- | --- | --- |
| `agent-work/README.md` | `agent-work/README.md` | `02c771a7c7d71e2303c186d0c150e903a524e949` | `bfe51802bb33e9f2a01ac548a5c4974e367ab674050cd0afc0e44a9f1aef6c45` |
| `agent-work/WORKFLOW-SPEC.md` | `agent-work/WORKFLOW-SPEC.md` | `02c771a7c7d71e2303c186d0c150e903a524e949` | `3c3b24edc4f3f7ff33b9208321763b37ae35d4641bd16a062c071f8184df9097` |
| `agent-work/COORDINATOR.md` | `agent-work/COORDINATOR.md` | `02c771a7c7d71e2303c186d0c150e903a524e949` | `1ac891f268865b76c789bc7ef46ddd56e3b33eb662bdb2d40852a83eb0591336` |
| `agent-work/RESULT-TEMPLATE.md` | `agent-work/RESULT-TEMPLATE.md` | `02c771a7c7d71e2303c186d0c150e903a524e949` | `680df22f358aad7c062a14e1964200d9281857625b64ccda6e8717806492f694` |
| `agent-work/EVIDENCE-MANIFEST.md` | `agent-work/EVIDENCE-MANIFEST.md` | `02c771a7c7d71e2303c186d0c150e903a524e949` | `c43b012044c18058d99c1d5c1b194174c23e5e9a8fcdaf5a8b34a2a2fe514242` |
| `docs/THREAT-MODEL.md` | `docs/THREAT-MODEL.md` | `02c771a7c7d71e2303c186d0c150e903a524e949` | `7ac9c1a5c7920f4a2dbd2ee92051d3f6724116dba8b207c3ac86590b577cf533` |
| `docs/agent-worktrees.md` | `docs/agent-worktrees.md` | `02c771a7c7d71e2303c186d0c150e903a524e949` | `9fb51de1c35e0ad98d00a3ce6a58bb3d66b9f5c351ab0685c1031b55ab9189d1` |
| `scripts/agent-task.py` | `scripts/agent-task.py` | `02c771a7c7d71e2303c186d0c150e903a524e949` | `8ec1b22cd97d10e1873ed9dfa83a37fa58f036914452f1af6508564215748f3c` |

Why these files:

- `agent-work/README.md`, `WORKFLOW-SPEC.md`, `COORDINATOR.md`: the protocol. `AGENTS.md` tells every agent to read the spec and the coordinator contract, and the README holds the task-agent contract.
- `agent-work/RESULT-TEMPLATE.md`, `agent-work/EVIDENCE-MANIFEST.md`: the result and evidence formats the spec and coordinator contract require.
- `docs/THREAT-MODEL.md`: `AGENTS.md` requires reviewers to classify findings against it.
- `docs/agent-worktrees.md`: `COORDINATOR.md` requires following it.
- `scripts/agent-task.py`: the read-only helper the Quick start uses to validate manifests; `scripts/validate.sh` runs it. It needs Python 3.11 or newer.

## Files written for this repository

These are not copies and have no recorded hash: `AGENTS.md` (Workflow's `AGENTS.md`, adapted), `ADOPTION.md`, `scripts/validate.sh`, `.github/workflows/validate.yml`, `site/index.html`. `README.md` is the pre-existing starter file and was left unchanged.

## Files not copied

| Source path | Reason |
| --- | --- |
| `AGENTS.md` | Not copied verbatim: Quick start step 2 says to define repository rules and deployment authority in it, and its own text says an adopting repository replaces the deployment paragraph. This repository's `AGENTS.md` keeps Workflow's general rules word for word and adds its own sections. |
| `README.md` | Describes the Workflow project itself; this repository keeps its own README. |
| `CONTRIBUTING.md` | Rules for contributing to Workflow, not for this site. |
| `.gitignore` | Workflow's Python cache ignores; nothing in this repository needs it yet. |
| `docs/DESIGN.md` | Background rationale; no procedure depends on it. Available at the source commit. |
| `docs/AGENT-LIFECYCLE-AND-OBSERVABILITY.md` | Forward-looking requirements the current helper does not implement; no procedure depends on it. |
| `docs/RELEASING.md` | Workflow's own GitHub-release process. This repository's live change is a Pages deployment, not a release. |
| `examples/README.md`, `examples/deployment/manifest.toml`, `examples/nondeployment/manifest.toml` | Illustrative manifests with placeholder commits. `WORKFLOW-SPEC.md` already contains a complete non-deployment example and the deployment-table fragment. They can be read at the source commit when the first deployment workflow is compiled. |
| `scripts/validate-repository.sh` | Workflow's own gate: it runs Workflow's test suite, validates `examples/`, and checks Workflow release tags. Replaced here by `scripts/validate.sh`. |
| `scripts/check-release-version.sh` | Checks Workflow release-tag names; this repository does not publish releases. |
| `scripts/tests/test_agent_workflow.py` | Workflow's regression suite for the helper. The helper is pinned here by SHA-256 to the exact upstream commit, whose own CI runs this suite; re-running it here would test Workflow, not this site. |
| `.github/workflows/validate.yml` | Runs Workflow's gate. Replaced by this repository's own `validate.yml`, which uses the same action versions. |
| `.github/workflows/release.yml` | Publishes Workflow releases; not this repository's live change. |
| `docs/PILOT-HISTORY.md`, `agent-work/pilot-*/` | Workflow's own pilot history and records. They were not in the original export; since alpha.13, Workflow's `docs/ADOPTING.md` lists them as not to be copied, and says references to them in copied files point back to Workflow. |
| `docs/ADOPTING.md` | New in alpha.13: Workflow's guide for adopters, which it does not list among the files to copy. It is read at the source. |

## Upgrades

**2026-10-14: from `3d38b27` to `v0.1.0-alpha.13`.**

- **Source.** The files were copied from the published release asset `workflow-v0.1.0-alpha.13.zip`, whose SHA-256 was checked on download as e520b61c3c48572b73001d333b2c79499e33b3e5c19f34988d5be2f3e191d5d4. The release tag `v0.1.0-alpha.13` is a lightweight tag at `84d826a40b8f8567439ab15eb270a1a752f92a82`, and every copied file is byte-identical to the file at that commit.
- **What changed.** Five files changed: `agent-work/WORKFLOW-SPEC.md`, `agent-work/COORDINATOR.md`, `agent-work/EVIDENCE-MANIFEST.md`, `docs/THREAT-MODEL.md` and `scripts/agent-task.py`. Three are byte-identical to the earlier copies: `agent-work/README.md`, `agent-work/RESULT-TEMPLATE.md` and `docs/agent-worktrees.md`. Workflow's `AGENTS.md` did not change between the two commits, so this repository's `AGENTS.md` is unchanged.
- **Procedure.** Workflow's `docs/ADOPTING.md` section 2: copy from the newer commit, update every row, and review the change like any other.
- **The ambiguities below, against alpha.13.**
  - Answered by `docs/ADOPTING.md`: 1, 2, 3, 4, 5, 7, 9, 11, 16, 17, 20 and 21. On 7: the copied threat model still mentions `docs/PILOT-HISTORY.md`, and the guide now says such references point back to Workflow.
  - Partly answered: 6, where the guide covers local threat models and when a guard review stops, but the copied threat model still describes only Workflow; and 10, where the guide allows exact tags or commit SHAs without choosing.
  - Not answered: 8, 12, 13, 14, 15, 18 and 19.
- **Row format.** `docs/ADOPTING.md` shows a three-column provenance row. This repository keeps its four-column form, with the source path, because `scripts/validate.sh` requires it. Hash values for the upgrade are kept out of other table rows, because the gate reads any table row starting with a backtick as a provenance row.

**2026-10-14: from `v0.1.0-alpha.13` to `v0.1.0-alpha.14`.**

- **Source.** The files were copied from the published release asset `workflow-v0.1.0-alpha.14.zip`, whose SHA-256 was checked on download as 1b87fa4a7034e58efaf0c8479b93bb82d4d3bad2c8fb3b467da4f27627d98355. The release tag `v0.1.0-alpha.14` is a lightweight tag at `02c771a7c7d71e2303c186d0c150e903a524e949`, and every copied file is byte-identical to the file at that commit.
- **What changed.** Five files changed: `agent-work/WORKFLOW-SPEC.md`, `agent-work/COORDINATOR.md`, `agent-work/RESULT-TEMPLATE.md`, `docs/THREAT-MODEL.md` and `scripts/agent-task.py`. Three are byte-identical to the earlier copies: `agent-work/README.md`, `agent-work/EVIDENCE-MANIFEST.md` and `docs/agent-worktrees.md`. Workflow's `AGENTS.md` did not change between the two commits.
- **This repository's `AGENTS.md`.** By the owner's decision (workflow `site-upgrade-14`, decision 2(a)), the "Git identity" rule now names the identity agents use without naming anyone, requires a check after a handover, and keeps merges local, as alpha.14's `docs/ADOPTING.md` section 3 advises. The commit-metadata decision of ambiguity 17 already sits next to the naming rule in `AGENTS.md`.
- **Procedure.** Workflow's `docs/ADOPTING.md` section 2, as before.
- **The ambiguities below, against alpha.14.** The lists above are unchanged, with three notes:
  - 17 is now answered more fully: the guide says to write such a decision next to the rule in `AGENTS.md`, and to name the commit identity without naming a person;
  - the row-format note is now covered by the guide, which says to keep a working gate's row form;
  - the guide's section 7 now asks readiness to prove the client that reads a deploy's evidence, which the `site-upgrade-14` workflow does.

## Ambiguities

Places where the Workflow documentation was unclear, incomplete or contradictory for a newcomer, and what was done.

1. **Which files are "the workflow control files".** Quick start step 1 says "Copy or vendor the workflow control files" without listing them. The README layout lists every file in the repository, including ones only meaningful to Workflow itself. *Chosen:* copy the files that the operating rules and protocol documents tell agents to read or use (see "Why these files"), and nothing that only serves Workflow's own development or releases.
2. **"Copy" versus "vendor", and provenance.** Nothing says how to pin the copied version, record provenance, detect local edits, or upgrade later. *Chosen:* this file records source commit and SHA-256 per file; `scripts/validate.sh` fails on any drift; `AGENTS.md` says how to update.
3. **Quick start step 5 runs a script adopters may not have.** It says to run `bash scripts/validate-repository.sh`, but that script depends on Workflow's test suite, `examples/` and `check-release-version.sh`, and the docs do not say whether an adopter should copy it, adapt it, or write its own. *Chosen:* not copied; `scripts/validate.sh` is this repository's gate.
4. **Quick start step 3 conflicts with the approval lifecycle.** Step 3 says to create `agent-work/<workflow-id>/PLAN.md`, a manifest and task files, while `WORKFLOW-SPEC.md` says a workflow may be compiled only after a plan, an independent plan review and user approval. No plan for this site has been approved inside this repository. *Chosen:* no workflow directory was created; `scripts/validate.sh` handles zero manifests. The first workflow will be compiled once its plan is approved.
5. **Extend or replace `AGENTS.md`.** Workflow's `AGENTS.md` says adopters should "extend this file", but its first sentence ("This repository contains a reusable multi-agent workflow framework") is false in an adopter, and its deployment paragraph says to replace it. *Chosen:* new introduction, Workflow's general rules kept word for word, deployment paragraph replaced, and repository-specific sections added.
6. **The threat model is Workflow's, not the adopter's.** `AGENTS.md` requires every finding to be classified against `docs/THREAT-MODEL.md`, and says out-of-scope findings are recorded, not fixed. That document only covers Workflow's gates and helper, lists open findings from Workflow's own pull requests, and says it was "approved by the repository owner" (Workflow's owner). A site defect, such as a page naming a private repository, fits none of its in-scope items, so read literally it would be "recorded, not fixed". Nothing says whether adopters should copy it, write their own, or how the owner approves one. *Chosen:* copied unchanged (it still governs the vendored helper), and `AGENTS.md` states that a site-rule breach is always a defect to fix and is reported as a site-rule violation. The owner should decide whether to approve a site-specific threat model.
7. **Documents referenced but not available.** `README.md` and `docs/THREAT-MODEL.md` cite `docs/PILOT-HISTORY.md`; `docs/RELEASING.md` cites `agent-work/pilot-rollback-drill/` as a worked rollback example. Neither was in the export the builder was given; the plan deliberately left them out, although both exist in Workflow at that commit. *Chosen:* not copied. The vendored `docs/THREAT-MODEL.md` therefore contains a dangling reference to `docs/PILOT-HISTORY.md`; it was left as is because copied files are not modified. Nothing in this adoption depends on that history.
8. **`/workflow` is never defined.** `WORKFLOW-SPEC.md` describes "the repository convention behind `/workflow`" and says "`/workflow` may capture the approved plan", but no command, skill or file by that name is shipped or explained. *Chosen:* treated as the coordinator's instruction-driven compile step described in `agent-work/README.md`; nothing was created for it.
9. **Python version requirement is undocumented.** The helper needs Python 3.11 or newer (`tomllib`); only the source code says so. *Chosen:* recorded here; CI uses Python 3.12, as Workflow's own CI does.
10. **Action pins.** Workflow's CI pins `actions/checkout@v7.0.1` and `actions/setup-python@v6.0.0` by release tag. Tags can be moved; the docs do not discuss pinning by commit SHA. *Chosen:* the same exact release tags, as instructed. The builder did not check them; the independent reviewer confirmed both tags exist (`refs/tags/v7.0.1` and `refs/tags/v6.0.0`).
11. **CI triggers.** Workflow's CI runs on pushes to any branch, on pull requests only into `main`, and on manual dispatch. This repository's requirement is every push and every pull request. *Chosen:* push to any branch and every pull request, no manual dispatch; read-only `contents: read`, no persisted credentials.
12. **Worktree root.** `COORDINATOR.md` says manual worktrees use "a repository-ignored worktree root" but names no directory and ships no ignore rule for one. *Chosen:* nothing added now; this adoption ran in an isolated worktree outside the repository directory. A workflow that needs an in-repository worktree root should add the ignore rule first.
13. **Preflight fetch.** `docs/agent-worktrees.md` says to fetch required remotes before work. This adoption was not allowed to contact GitHub. *Chosen:* local read-only preflight only (branch, remotes, worktrees, status, starting commit). Freshness of `origin/main` was not verified.
14. **Workflow version.** The spec says new workflows "may" use `workflow_version = 3` but documents no version 2 schema. *Chosen:* future workflows here should use version 3.
15. **Terminology.** The README says `<workflow-id>`, manifests use the key `phase`, and the helper's argument is called `phase`. They are the same thing; `scripts/validate.sh` passes the directory name.
16. **How the adoption itself is reviewed.** The docs describe review inside a compiled workflow, plus a "durable review record" (one pull-request comment) for review outside one. They do not say which applies to the adoption commit that installs Workflow. *Chosen:* this adoption is ordinary builder work and needs an independent reviewer and that pull-request comment before it reaches `main`.
17. **Site rules versus commit metadata.** The owner's rule says the repository must never name people or emails, but the mandated commit identity and `Co-Authored-By` trailer contain an email address, and the starter commit already in history carries a personal author name and email address that differ from the mandated identity. The docs give no guidance. *Chosen:* the mandated identity and trailers were used as instructed and treated as owner-approved; the existing starter commit was not rewritten, because the operating rules forbid discarding history or force-pushing. The rule is applied to file content, commit messages and branch names. The owner has since confirmed that the starter commit's author metadata is acceptable. This file deliberately does not repeat that name or address.
18. **Placeholder addresses in vendored docs.** `agent-work/EVIDENCE-MANIFEST.md` and `docs/THREAT-MODEL.md` contain example values such as a loopback IPv4 address, an IPv6 documentation-range address, `\\server\share` and `https://host`. *Chosen:* treated as generic placeholders, not names of real hosts or addresses, so the files were copied unchanged. `AGENTS.md` says so explicitly.
19. **Naming the source repository.** Provenance requires naming `saxton-network/workflow`. Its own README calls it "the public repository" and describes public releases; the builder did not check its visibility live; the independent reviewer confirmed it answers an unauthenticated `git ls-remote`. *Chosen:* named here on that basis. If it is not public, this file must be changed.
20. **Pages deployment in Workflow's model.** The docs are written around host and release deployments. For GitHub Pages they do not say what the deployable artifact, rollback artifact, or `deploymentTargets` entry should be. One concrete trap: the accepted destination format forbids a trailing separator, so the site URL must be written `https://saxton-network.github.io/site`, not `https://saxton-network.github.io/site/`; `mode` would be `null`. *Chosen:* nothing yet, since the deploy workflow is out of scope; this is left for the first deployment workflow's plan and contract.
21. **Settings as live changes.** `agent-work/EVIDENCE-MANIFEST.md` mentions forge settings only as observed readiness inputs and does not say whether changing them (for example, enabling Pages) is a live change. *Chosen:* `AGENTS.md` treats changing GitHub Pages or other GitHub settings as a live change that needs a bounded preview and explicit approval.
