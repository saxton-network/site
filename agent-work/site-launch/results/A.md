# Agent task result: site-launch / A

- **Candidate commit:** `082505507cc98965972aceaef278a9e84f267b3b` on `pilot/site-launch-impl`.
- **Base:** `3da96f0555ea6484ab7630654af0fc1f6ec90ceb` (`main`).
- **Builder:** the coordinator session's agent.

## Changed paths

- `site/index.html`: v1, SHA-256 `495b4b2b4e8c25335184fa994716a888bc9f0980b3196eb633110bde18351eb3`.
- `scripts/projects.txt`
- `scripts/check-site.py`
- `scripts/validate.sh`: the site check is now required.
- `.github/workflows/deploy.yml`

## Action tags

Each tag was confirmed to exist with `git ls-remote --tags` on 2026-10-13:

| Action | Tag |
| --- | --- |
| `actions/checkout` | `v7.0.1` |
| `actions/setup-python` | `v6.0.0` |
| `actions/configure-pages` | `v6.0.0` (latest release tag) |
| `actions/upload-pages-artifact` | `v5.0.0` (latest) |
| `actions/deploy-pages` | `v5.0.1` (latest) |

## Checks

| Check | Result |
| --- | --- |
| `bash scripts/validate.sh` | PASS: 8 vendored hashes, site check with 2 repositories listed, no manifests on this branch. |
| The site check rejects one bad fixture per rule | PASS. All 14 rejected: script, event handler, `javascript:` URL, `<link>`, `<img>`, `<iframe>`, CSS `url(`, `@import`, inline-style `url(`, external link, unlisted repository, `projects.txt` mismatch, extra file in `site/`, meta refresh. The unchanged page passes. |
| A missing `check-site.py` fails the gate | PASS |
| `deploy.yml` parses as YAML | PASS |
| Validate CI on the candidate | PASS: run 38403816295, `head_sha` = candidate, conclusion `success`. |

## Not proven here

Whether the Pages actions work together, and whether the deploy itself succeeds, cannot be shown without deploying. Runtime acceptance (J) covers both.
