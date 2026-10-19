# Task P: authority promotion

Performed by the coordinator on 2026-10-14, under the approved plan: a non-force fast-forward of `main`. The main freeze starts here.

## Gates

All gates ran in a non-shallow clone under `set -euo pipefail`, with `SHA=dfaa7cb863da02c204b34c4e05d90d9f9660fe97`, the `deploymentSourceSha` of B-1 (`passed`). The local proofs ran with every inherited `GIT_*` variable removed. Every gate passed on the first run:

- gate 0: the clone is not shallow, and `SHA` equals B-1's literal;
- gate 1: after `git fetch origin main`, `origin/main` is `16c363137b52093fcd014ee00d8c4a8ca570e658`;
- the implementation branch is still at `SHA`;
- gate 2: `GIT_GRAFT_FILE=/dev/null git --no-replace-objects -c core.commitGraph=false merge-base --is-ancestor 16c3631… "$SHA"` exits 0;
- gate 3: `8377801ebd47f8ce1ec96eac9bd807dc5a876273` appears once on the first-parent line of `SHA`. That line is `dfaa7cb 16c3631 a3aa6b4 95914a5 ae90609 8f3c310 d28afc4 8377801`.

## Push

A separate command, run after the gates, with the literal SHA:

```
$ git push origin dfaa7cb863da02c204b34c4e05d90d9f9660fe97:refs/heads/main
   16c3631..dfaa7cb  dfaa7cb863da02c204b34c4e05d90d9f9660fe97 -> main
EXIT=0
```

This was a fast-forward, with no force.

## After the push

- `git ls-remote origin refs/heads/main` returns `dfaa7cb863da02c204b34c4e05d90d9f9660fe97`.
- No deploy run was started. The deploy workflow runs only on dispatch, and the live page is still v1.
- As a separate step, `dfaa7cb` was merged into `pilot/site-upgrade-14-records` without force, under the no-reply identity (`936a2c4`). There was no conflict. The helper there is now the alpha.14 helper (SHA-256 read from the file: `8ec1b22cd97d10e1873ed9dfa83a37fa58f036914452f1af6508564215748f3c`), and `bash scripts/validate.sh` passes.
