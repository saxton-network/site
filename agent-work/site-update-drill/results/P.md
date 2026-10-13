# Task P: authority promotion

Performed by the coordinator on 2026-10-13, under the approved plan (non-force fast-forward of `main`).

## Before the push

- `git fetch origin`; `origin/main` = `d28afc431f80347c15f32483fbe936ccedce9727` (the landed `site-launch` records).
- Candidate: `8f3c310876166dc0cb2864dff3646e18830b1758`, the commit B-1 passed. Validate CI run 38411804568 on it: success.
- Ancestry, with every inherited `GIT_*` variable removed (git 2.43.0): `GIT_GRAFT_FILE=/dev/null git --no-replace-objects -c core.commitGraph=false -c advice.graftFileDeprecated=false merge-base --is-ancestor d28afc4… 8f3c310…` exited 0. `git log --oneline d28afc4..8f3c310` lists one commit, the candidate.

## Push

```
$ git push origin 8f3c310876166dc0cb2864dff3646e18830b1758:refs/heads/main
   d28afc4..8f3c310  8f3c310876166dc0cb2864dff3646e18830b1758 -> main
```

A fast-forward, no force. `git ls-remote origin refs/heads/main` = the candidate.

## First-parent check (step 2): run, but not as a gate

- The coordinator ran step 2 as `git rev-list --first-parent <candidate> | grep -qx <v1>` in the same `set -o pipefail` shell, joined to its `echo` with `&&`, and the push followed on its own line. Under `pipefail` the pipeline returned 141 (SIGPIPE: `grep -q` exits on the first match and `rev-list` is killed writing the rest), so the check printed nothing and did not stop the push. The push was therefore not gated on step 2. That is a coordinator procedure error.
- Re-run without the pipe straight after: `git rev-list --first-parent 8f3c310…` lists `8f3c310`, `d28afc4`, then `8377801…` (v1) at position 3. v1 is on the first-parent line, so the step would have passed. B-1 had also proven it independently with the deploy guard itself.
- Pilot finding: `grep -q` after a pipe is not reliable under `pipefail`. `deploy.yml` uses the same pattern, but its step runs under `bash -e` without `pipefail` (shown as `shell: /usr/bin/bash -e {0}` in the v1 run log), so it is unaffected; if `pipefail` were ever turned on, it would fail closed, never open.

The main freeze is in effect from this point until the records land in V.
