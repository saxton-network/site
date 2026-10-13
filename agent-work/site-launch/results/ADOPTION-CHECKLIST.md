# Hidden adoption checklist (bootstrap of saxton-network/site)

Written by the coordinator before the bootstrap builder starts, from Workflow at `3d38b27749aa0d5ed4cd751ffe64a4359f4f330a` (its README "Quick start", AGENTS.md, and agent-work/ docs). The builder never sees this file. The bootstrap reviewer grades the PR against it. Each item is PASS, FAIL or N/A, with a one-line reason.

## Copied files

1. These files are copied byte for byte from Workflow at `3d38b27`:
   - `agent-work/README.md`, `agent-work/WORKFLOW-SPEC.md`, `agent-work/COORDINATOR.md`, `agent-work/EVIDENCE-MANIFEST.md` and `agent-work/RESULT-TEMPLATE.md`;
   - `scripts/agent-task.py`;
   - `docs/THREAT-MODEL.md`;
   - `docs/agent-worktrees.md`, because `COORDINATOR.md` cites it.

   Any edit to a copied file is listed in `ADOPTION.md` with its reason.
2. `ADOPTION.md` records each copied file's source path, source commit and SHA-256, and the hashes are correct.
3. Workflow's `scripts/validate-repository.sh`, `scripts/check-release-version.sh`, `scripts/tests/`, `.github/workflows/release.yml`, `docs/PILOT-HISTORY.md` and the pilot directories are **not** copied. If one is, `ADOPTION.md` gives a reason.
4. Nothing else from Workflow is copied silently.

## AGENTS.md

5. It keeps every Workflow rule in substance:
   - preserve work;
   - the three states (working, authoritative, deployed);
   - approval before live mutation, with a bounded preview;
   - the secrets rule;
   - the repository-native workflow rules;
   - deployment pinned to the reviewed source;
   - the verification rule.
6. It defines this repository's deployment authority as `authority_remote = "origin"`, `authority_ref = "refs/heads/main"`, and names the live change as a GitHub Pages deploy of an exact commit on `main`.
7. It states the site rule: only public repositories are listed. It names no private repository, host, address, person or email.
8. It does not keep Workflow's own sentence about releasing Workflow through `release.yml`; that sentence is Workflow's own. If it does, this is a FAIL.

## Validation

9. `scripts/validate.sh` exists and is executable or run with `bash`, and fails on error (`set -e` or equivalent). It:
   - verifies every hash in `ADOPTION.md`;
   - skips a missing `scripts/check-site.py` with a printed note;
   - runs `python3 scripts/agent-task.py <id> --all` for each `agent-work/<id>/manifest.toml`, accepting zero workflow directories.
10. `.github/workflows/validate.yml` runs `scripts/validate.sh` on push and pull request, has read-only permissions, and pins its actions to exact tags.
11. `bash scripts/validate.sh` passes on the PR head.

## Site placeholder

12. `site/` contains only `index.html`, a placeholder with no script, external resource or link to anything outside `https://github.com/saxton-network/`.
13. There is no `deploy.yml` yet.

## Repository hygiene

14. There is no secret, token, personal email, private repository name or infrastructure detail anywhere.
15. Every commit's author and committer are the no-reply identity.
16. The PR's changes sit on one branch descending from the root commit, with no merge from elsewhere.

## Ambiguity log

17. `ADOPTION.md` has an "Ambiguities" section listing every place where the docs were unclear or incomplete for a newcomer, each with what the builder chose.

    Expected at least:
    - the Quick start names `scripts/validate-repository.sh` without saying to copy it, and the script is Workflow-specific;
    - which files make up "the workflow control files" is not listed.

    Missing either is not a FAIL, but it is noted as a weakness of the log.
