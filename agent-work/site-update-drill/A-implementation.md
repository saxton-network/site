# Task A: implementation

- **Prerequisites:** none.
- **Base:** the current `main` tip, `d28afc431f80347c15f32483fbe936ccedce9727`. **Branch:** `pilot/site-update-drill-impl`, in its own worktree.
- **Read first:** `AGENTS.md` (the site rules), `PLAN.md` ("Workflow 2"), `CONTRACT.md`.

## Work

1. **`site/index.html` (v2).** Add one line after the project list: `Last updated 13 October 2026.`, in a `<p>` with inline CSS matching the page's muted text. Nothing else on the page changes.
2. **Nothing else.** v2 is content only: `.github/`, `scripts/` and every other file stay byte-identical to v1 (`CONTRACT.md` "Source and authority").

## Validation

- `bash scripts/validate.sh` passes, including the site check.
- `git diff --name-only <base> <candidate>` lists only `site/index.html`.
- Validate CI is green on the pushed candidate.

## Result

`results/A.md`: the candidate commit, the changed path, the new `index.html` SHA-256, the diff of the page, and the checks.

## Records

Hand the result content to the coordinator. Only the coordinator commits to `pilot/site-update-drill-records`; nothing under `agent-work/site-update-drill/` is committed to the implementation branch.

## Forbidden

- Any file other than `site/index.html`.
- Any vendored Workflow file.
- Deploying or dispatching anything.
- Changing GitHub settings.

## Stop boundary

Stop at the end of this task and hand the result to the coordinator. Do not start another task.
