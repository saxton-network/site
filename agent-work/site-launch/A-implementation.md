# Task A: implementation

- **Prerequisites:** none.
- **Base:** the current `main` tip, `3da96f0555ea6484ab7630654af0fc1f6ec90ceb`. **Branch:** `pilot/site-launch-impl`, in its own worktree.
- **Read first:** `AGENTS.md` (the site rules), `PLAN.md` ("The project"), `CONTRACT.md`.

## Work

1. **`site/index.html` (v1).** A landing page titled "Saxton Network" that lists `saxton-network/workflow` and `saxton-network/chudley`, each with its GitHub description and a link to `https://github.com/saxton-network/<repo>`. Plain HTML with inline CSS, and nothing the site rules forbid. `site/` holds only this file.
2. **`scripts/projects.txt`.** The listed repositories, one per line.
3. **`scripts/check-site.py`.** Fails unless:
   - there is no `<script>`, event-handler attribute, `javascript:` URL, `<link>`, `<img>`, `<iframe>`, `<object>`, `<embed>`, media element, `url(` or `@import`;
   - every `href` is `https://github.com/saxton-network/<repo>`;
   - the listed repositories exactly match `scripts/projects.txt`;
   - `site/` holds only `index.html`.

   It does not claim full HTML validation.
4. **`scripts/validate.sh`.** Make a missing `check-site.py` a failure (bootstrap review F3).
5. **`.github/workflows/deploy.yml`,** as `PLAN.md` specifies:
   - trigger `workflow_dispatch`, with a `sha` input passed through `env`;
   - checks that `sha` is 40 lowercase hex characters and on `origin/main`'s first-parent history (`fetch-depth: 0`); this was tightened from "ancestor of or equal to" by repair C-1 (F3);
   - checks out `sha`, requires `site/` to hold only `index.html`, and runs the site check;
   - echoes `HEAD` and the SHA-256 of `site/index.html` to the job log and the run summary;
   - `run-name: Deploy <sha>`;
   - permissions `contents: read`, `pages: write`, `id-token: write`;
   - `environment: github-pages`;
   - `concurrency: {group: pages, cancel-in-progress: false}`;
   - actions pinned to exact release tags, each confirmed to exist with `git ls-remote`.

## Validation

- `bash scripts/validate.sh` passes.
- The site check fails on at least one fixture per rule.
- `deploy.yml` parses as YAML.
- Validate CI is green on the pushed candidate.

## Result

`results/A.md`: the candidate commit, changed paths, the action tags with their `ls-remote` evidence, and the checks.

## Records

Hand the result content to the coordinator. Only the coordinator commits to `pilot/site-launch-records`; nothing under `agent-work/site-launch/` is committed to the implementation branch.

## Forbidden

- Any vendored Workflow file.
- Deploying or dispatching anything.
- Changing GitHub settings.

## Stop boundary

Stop at the end of this task and hand the result to the coordinator. Do not start another task.
