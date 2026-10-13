# Workflow adoption record

This repository adopts the Workflow framework from the public repository `saxton-network/workflow` at commit `3d38b27749aa0d5ed4cd751ffe64a4359f4f330a`. The adoption followed Workflow's README "Quick start" and the documents it references, reading only the files exported from that commit.

`bash scripts/validate.sh` verifies every hash in the table below against the files in this repository.

## Copied files

Each file was copied byte for byte. None was modified. The path in this repository equals the source path.

| Path in this repository | Source path | Source commit | SHA-256 |
| --- | --- | --- | --- |
| `agent-work/README.md` | `agent-work/README.md` | `3d38b27749aa0d5ed4cd751ffe64a4359f4f330a` | `bfe51802bb33e9f2a01ac548a5c4974e367ab674050cd0afc0e44a9f1aef6c45` |
| `agent-work/WORKFLOW-SPEC.md` | `agent-work/WORKFLOW-SPEC.md` | `3d38b27749aa0d5ed4cd751ffe64a4359f4f330a` | `6f902673789f276d93a28676b64221b5a105cbfbf539e76dcf9121629861f50b` |
| `agent-work/COORDINATOR.md` | `agent-work/COORDINATOR.md` | `3d38b27749aa0d5ed4cd751ffe64a4359f4f330a` | `9123a28cf74160190c761bafba51a37ad226577b0fca5b11e38ed4881177e33d` |
| `agent-work/RESULT-TEMPLATE.md` | `agent-work/RESULT-TEMPLATE.md` | `3d38b27749aa0d5ed4cd751ffe64a4359f4f330a` | `9c8dd149d8ef51cccffad24b77da746248aa9a739e5cf2a8fdd4b46d92fd585b` |
| `agent-work/EVIDENCE-MANIFEST.md` | `agent-work/EVIDENCE-MANIFEST.md` | `3d38b27749aa0d5ed4cd751ffe64a4359f4f330a` | `0fd361552cffe2ace79c6163664baaf37a39b9f3041f74ff8442a40e76735c46` |
| `docs/THREAT-MODEL.md` | `docs/THREAT-MODEL.md` | `3d38b27749aa0d5ed4cd751ffe64a4359f4f330a` | `c95531933c0f4fb0eb6012a4dc7b3a59d4e7c2a3dd906105a2b115686f4eb4ef` |
| `docs/agent-worktrees.md` | `docs/agent-worktrees.md` | `3d38b27749aa0d5ed4cd751ffe64a4359f4f330a` | `9fb51de1c35e0ad98d00a3ce6a58bb3d66b9f5c351ab0685c1031b55ab9189d1` |
| `scripts/agent-task.py` | `scripts/agent-task.py` | `3d38b27749aa0d5ed4cd751ffe64a4359f4f330a` | `c7f5e5ed29334f0b991cf183cc5ba9e013bff2b49c099cd2c9d7aa8e09d00655` |

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
| `docs/PILOT-HISTORY.md`, `agent-work/pilot-rollback-drill/` | Referenced by Workflow docs but not present in the export, so they could not be copied (see Ambiguities). |

## Ambiguities

Places where the Workflow documentation was unclear, incomplete or contradictory for a newcomer, and what was done.

1. **Which files are "the workflow control files".** Quick start step 1 says "Copy or vendor the workflow control files" without listing them. The README layout lists every file in the repository, including ones only meaningful to Workflow itself. *Chosen:* copy the files that the operating rules and protocol documents tell agents to read or use (see "Why these files"), and nothing that only serves Workflow's own development or releases.
2. **"Copy" versus "vendor", and provenance.** Nothing says how to pin the copied version, record provenance, detect local edits, or upgrade later. *Chosen:* this file records source commit and SHA-256 per file; `scripts/validate.sh` fails on any drift; `AGENTS.md` says how to update.
3. **Quick start step 5 runs a script adopters may not have.** It says to run `bash scripts/validate-repository.sh`, but that script depends on Workflow's test suite, `examples/` and `check-release-version.sh`, and the docs do not say whether an adopter should copy it, adapt it, or write its own. *Chosen:* not copied; `scripts/validate.sh` is this repository's gate.
4. **Quick start step 3 conflicts with the approval lifecycle.** Step 3 says to create `agent-work/<workflow-id>/PLAN.md`, a manifest and task files, while `WORKFLOW-SPEC.md` says a workflow may be compiled only after a plan, an independent plan review and user approval. No plan for this site has been approved inside this repository. *Chosen:* no workflow directory was created; `scripts/validate.sh` handles zero manifests. The first workflow will be compiled once its plan is approved.
5. **Extend or replace `AGENTS.md`.** Workflow's `AGENTS.md` says adopters should "extend this file", but its first sentence ("This repository contains a reusable multi-agent workflow framework") is false in an adopter, and its deployment paragraph says to replace it. *Chosen:* new introduction, Workflow's general rules kept word for word, deployment paragraph replaced, and repository-specific sections added.
6. **The threat model is Workflow's, not the adopter's.** `AGENTS.md` requires every finding to be classified against `docs/THREAT-MODEL.md`, and says out-of-scope findings are recorded, not fixed. That document only covers Workflow's gates and helper, lists open findings from Workflow's own pull requests, and says it was "approved by the repository owner" (Workflow's owner). A site defect, such as a page naming a private repository, fits none of its in-scope items, so read literally it would be "recorded, not fixed". Nothing says whether adopters should copy it, write their own, or how the owner approves one. *Chosen:* copied unchanged (it still governs the vendored helper), and `AGENTS.md` states that a site-rule breach is always a defect to fix and is reported as a site-rule violation. The owner should decide whether to approve a site-specific threat model.
7. **Documents referenced but not available.** `README.md` and `docs/THREAT-MODEL.md` cite `docs/PILOT-HISTORY.md`; `docs/RELEASING.md` cites `agent-work/pilot-rollback-drill/` as a worked rollback example. Neither is in the export. *Chosen:* not copied. The vendored `docs/THREAT-MODEL.md` therefore contains a dangling reference to `docs/PILOT-HISTORY.md`; it was left as is because copied files are not modified. Nothing in this adoption depends on that history.
8. **`/workflow` is never defined.** `WORKFLOW-SPEC.md` describes "the repository convention behind `/workflow`" and says "`/workflow` may capture the approved plan", but no command, skill or file by that name is shipped or explained. *Chosen:* treated as the coordinator's instruction-driven compile step described in `agent-work/README.md`; nothing was created for it.
9. **Python version requirement is undocumented.** The helper needs Python 3.11 or newer (`tomllib`); only the source code says so. *Chosen:* recorded here; CI uses Python 3.12, as Workflow's own CI does.
10. **Action pins.** Workflow's CI pins `actions/checkout@v7.0.1` and `actions/setup-python@v6.0.0` by release tag. Tags can be moved; the docs do not discuss pinning by commit SHA. *Chosen:* the same exact release tags, as instructed. Their existence and targets were not checked, because this adoption did not access GitHub.
11. **CI triggers.** Workflow's CI runs on pushes to any branch, on pull requests only into `main`, and on manual dispatch. This repository's requirement is every push and every pull request. *Chosen:* push to any branch and every pull request, no manual dispatch; read-only `contents: read`, no persisted credentials.
12. **Worktree root.** `COORDINATOR.md` says manual worktrees use "a repository-ignored worktree root" but names no directory and ships no ignore rule for one. *Chosen:* nothing added now; this adoption ran in an isolated worktree outside the repository directory. A workflow that needs an in-repository worktree root should add the ignore rule first.
13. **Preflight fetch.** `docs/agent-worktrees.md` says to fetch required remotes before work. This adoption was not allowed to contact GitHub. *Chosen:* local read-only preflight only (branch, remotes, worktrees, status, starting commit). Freshness of `origin/main` was not verified.
14. **Workflow version.** The spec says new workflows "may" use `workflow_version = 3` but documents no version 2 schema. *Chosen:* future workflows here should use version 3.
15. **Terminology.** The README says `<workflow-id>`, manifests use the key `phase`, and the helper's argument is called `phase`. They are the same thing; `scripts/validate.sh` passes the directory name.
16. **How the adoption itself is reviewed.** The docs describe review inside a compiled workflow, plus a "durable review record" (one pull-request comment) for review outside one. They do not say which applies to the adoption commit that installs Workflow. *Chosen:* this adoption is ordinary builder work and needs an independent reviewer and that pull-request comment before it reaches `main`.
17. **Site rules versus commit metadata.** The owner's rule says the repository must never name people or emails, but the mandated commit identity and `Co-Authored-By` trailer contain an email address, and the starter commit already in history carries a personal author name and email address that differ from the mandated identity. The docs give no guidance. *Chosen:* the mandated identity and trailers were used as instructed and treated as owner-approved; the existing starter commit was not rewritten, because the operating rules forbid discarding history or force-pushing. The rule is applied to file content, commit messages and branch names. The owner should decide whether the starter commit's author metadata is acceptable. This file deliberately does not repeat that name or address.
18. **Placeholder addresses in vendored docs.** `agent-work/EVIDENCE-MANIFEST.md` and `docs/THREAT-MODEL.md` contain example values such as a loopback IPv4 address, an IPv6 documentation-range address, `\\server\share` and `https://host`. *Chosen:* treated as generic placeholders, not names of real hosts or addresses, so the files were copied unchanged. `AGENTS.md` says so explicitly.
19. **Naming the source repository.** Provenance requires naming `saxton-network/workflow`. Its own README calls it "the public repository" and describes public releases; its visibility was not checked live. *Chosen:* named here on that basis. If it is not public, this file must be changed.
20. **Pages deployment in Workflow's model.** The docs are written around host and release deployments. For GitHub Pages they do not say what the deployable artifact, rollback artifact, or `deploymentTargets` entry should be. One concrete trap: the accepted destination format forbids a trailing separator, so the site URL must be written `https://saxton-network.github.io/site`, not `https://saxton-network.github.io/site/`; `mode` would be `null`. *Chosen:* nothing yet, since the deploy workflow is out of scope; this is left for the first deployment workflow's plan and contract.
21. **Settings as live changes.** `agent-work/EVIDENCE-MANIFEST.md` mentions forge settings only as observed readiness inputs and does not say whether changing them (for example, enabling Pages) is a live change. *Chosen:* `AGENTS.md` treats changing GitHub Pages or other GitHub settings as a live change that needs a bounded preview and explicit approval.
