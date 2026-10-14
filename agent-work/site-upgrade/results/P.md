# Task P: authority promotion

Performed by the coordinator on 2026-10-14, under the approved plan (non-force fast-forward of `main`). The main freeze starts here.

## Gates

All in a clone of the site repository, under `set -euo pipefail`, with `SHA=95914a54336983fc48e286b8e16cb6780076d2f2`, the `deploymentSourceSha` of B-1 (`passed`).

- **First attempt: stopped at gate 0.** The clone was shallow, so `git rev-parse --is-shallow-repository` printed `true` and the gate exited before anything moved. This is the gate working as intended. The clone was completed with `git fetch --unshallow origin` and every gate was run again from gate 0.
- **Second and third runs: all passed.** The last run came immediately before the push:
  - gate 0: not shallow; `SHA` equals B-1's literal;
  - gate 1: `git fetch origin main`; `origin/main` = `ae90609244b36f306f924bf5470f21d8cf202bb2` (also confirmed by `git ls-remote`);
  - gate 2: the hardened `merge-base --is-ancestor ae90609… "$SHA"` exited 0;
  - gate 3: `8377801ebd47f8ce1ec96eac9bd807dc5a876273` appears once on `SHA`'s first-parent line.
- **Inherited `GIT_*` variables.** The gate runs above inherited the container's `GIT_*` variables: a CA path, an askpass helper, terminal-prompt and editor settings, and three `GIT_CONFIG_*` entries (`credential.interactive` and two `url.<base>.insteadOf` rewrites). None of them changes object lookup or ancestry. To meet the task's "no inherited `GIT_*` variables" rule, the local proofs were run again after the push with every `GIT_*` variable removed (`env -u` for each; a count of `GIT_*` variables inside printed 0), git 2.43.0:
  - `is-shallow-repository`: `false`;
  - the hardened `merge-base --is-ancestor ae90609… 95914a5…`: exit 0;
  - `8377801` count on the first-parent line: 1;
  - first-parent line: `95914a5 ae90609 8f3c310 d28afc4 8377801`;
  - `git log --oneline ae90609..95914a5`: one commit, `95914a5` (task A).

  The objects are immutable, so the result is the same as before the push; the order is recorded here as it happened.

## Validate CI on the candidate

Run 38511384398 (push, `pilot/site-upgrade-impl`, `head_sha` = the candidate): `success`.

## Push

A separate command, after the gates, with the literal SHA:

```
$ git push origin 95914a54336983fc48e286b8e16cb6780076d2f2:refs/heads/main
   ae90609..95914a5  95914a54336983fc48e286b8e16cb6780076d2f2 -> main
EXIT=0
```

A fast-forward, no force.

## After the push

- `git ls-remote origin refs/heads/main` = `95914a54336983fc48e286b8e16cb6780076d2f2`.
- Validate CI on `main`: run 38511817666, `head_sha` = the candidate, conclusion `success`. No deploy run was started: the deploy workflow runs only on dispatch, and the live page is still v1.
- As a separate step, `95914a5` was merged into `pilot/site-upgrade-records` without force (merge commit `98bafd4`), with no conflict. The helper there is now the alpha.13 helper: SHA-256 `67fa523bd62cf21ad53d969460074982baff1f5b5e1312a086b953e0138f4434`. `bash scripts/validate.sh` passes on that commit.
