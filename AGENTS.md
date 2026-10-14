# Agent operating rules

This repository is the Saxton Network public website: one landing page, served by GitHub Pages at https://saxton-network.github.io/site/. It uses the Workflow multi-agent framework. The vendored Workflow files, their source commit and their SHA-256 hashes are listed in `ADOPTION.md`.

The general rules below are Workflow's operating rules. The sections "Deployment authority", "Site rules", "Vendored Workflow files" and "Repository gate" are specific to this repository.

## Preserve work

- Inspect branch, remotes, worktrees, and git status before editing.
- Preserve concurrent work. Never reset, clean, force-checkout, or discard unrelated changes.
- Use one branch and isolated worktree per mutating agent unless an equivalent isolated workspace already exists.
- Never force-push to erase divergence or discard unique commits.

## Separate repository states

Keep these concepts distinct:

- **Working:** a change exists on a working or collaboration ref.
- **Authoritative:** the configured deployment-authority ref contains the accepted source.
- **Deployed:** that exact reviewed source was applied live and passed runtime acceptance.

Do not infer one state from another.

## Approval

Repository-only implementation may follow an approved plan without repeated approval prompts.

Before any live state mutation, require a bounded preview and explicit human approval for that exact batch. The preview should identify the source, effects, commands or script, exposure, verification, stop conditions, rollback, and retry boundary.

A helper status, evidence record, plan approval, or previous approval does not authorize a different live batch.

## Secrets

Never commit or place in evidence credentials, bearer tokens, private keys, runtime secret files, or raw secret-bearing response bodies. Use sanitized evidence references instead.

## Repository-native workflows

- Read agent-work/WORKFLOW-SPEC.md and agent-work/COORDINATOR.md.
- The coordinator owns shared workflow status and evidence.json.
- Child agents stop at their task boundary.
- Builders and independent reviewers remain separate roles.
- Findings go to a separate repair role and back to the same reviewer.
- Do not silently weaken a frozen contract or safety boundary.
- Reviewers classify each finding against docs/THREAT-MODEL.md. Out-of-scope findings are recorded, not fixed, unless the owner changes that document.
- The repository owner approves scope, releases, and live changes. Code review is done by agents independent of the builder, preferably a different model or vendor; the owner is not asked to review code.

`docs/THREAT-MODEL.md` is Workflow's own threat model, vendored unchanged; it covers the Workflow gates and helper. A breach of the "Site rules" below is not a threat-model classification question: it breaks an owner-set repository rule and is always a defect to fix. Reviewers report it as a site-rule violation and name the rule. A site-specific threat model needs the owner's approval before it replaces or extends this arrangement.

## Deployment authority

An adopting repository must define its deployment authority. Workflow v3 records it in the deployment table as authority_remote and authority_ref.

For this repository, the live change is a GitHub Pages deployment of one exact commit on `main`, performed by a manually dispatched GitHub Actions workflow. That deploy workflow is `.github/workflows/deploy.yml`; changing it is a reviewed repository change, and every dispatch of it is a live change. The deployment authority is `authority_remote = "origin"`, `authority_ref = "refs/heads/main"`: the site is deployed only from the exact independently reviewed commit at `main`. Changing the repository's GitHub Pages or other GitHub settings is also a live change and needs its own bounded preview and explicit approval.

Deployment must remain pinned to the exact independently reviewed authoritative source. A known additive descendant may wait for final reconciliation only after object, ancestry, and changed-path proof and only when protected deployment inputs are unchanged. Unknown or destructive divergence stops mutation.

## Site rules

These rules were set by the owner. They apply to every file, commit message, branch name, task file, result and evidence record in this repository, not only to the published page.

- **Never name private repositories, hosts, addresses, people or emails.** The only repositories that may be named are the organisation's public repositories. Whether a repository is public is a mutable fact: check it fresh before naming it. Placeholder values in vendored Workflow documentation (loopback and documentation-range addresses, generic names such as `server` or `host`) are not names of real private hosts.
  - **Commit metadata.** The mandated commit identity and its `Co-Authored-By` and session trailers are exempt from this rule. Everything else in a commit message, and all file content and branch names, stays under it. This is the owner's decision recorded in `ADOPTION.md` (ambiguity 17), written here so reviewers apply it.
- **The page lists only the organisation's public repositories.**
- **Plain HTML with inline CSS.** No JavaScript in any form (no `<script>` element, no event-handler attribute, no `javascript:` URL).
- **No external resources.** The page loads nothing from anywhere: no external stylesheet, font, image, frame, media or other fetched URL.
- **Links only inside `https://github.com/saxton-network/`.** Every link target starts with that prefix.
- **`site/` is the published directory.** It contains only `index.html` unless the owner approves a change to this rule.
- **Git identity.** Commits use the identity already configured for this repository. Do not change `user.name` or `user.email`, and do not commit as any other identity.

## Vendored Workflow files

- Do not edit a vendored Workflow file. If a change is unavoidable, record the change and the reason in `ADOPTION.md` and update its recorded hash in the same commit.
- Updating Workflow means copying files from a newer exact upstream commit and recording that commit and the new hashes in `ADOPTION.md`.

## Repository gate

`bash scripts/validate.sh` is the repository gate, and CI runs it on every push and pull request. It verifies the vendored file hashes, runs `scripts/check-site.py` when it exists, and validates every `agent-work/<workflow-id>/manifest.toml`. A passing gate is repository evidence only; it is not proof of what GitHub Pages is serving.

## Verification

No agent may claim complete, fixed, passing, ready, deployed, or reconciled without fresh evidence for the exact candidate or state being described.

Repository CI is not proof of live deployment behavior. Mutable host, network, remote-ref, permission, and runtime facts require fresh checks when they matter.
