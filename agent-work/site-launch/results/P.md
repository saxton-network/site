# Task P: authority promotion

Performed by the coordinator on 2026-10-13, under the approved plan (non-force fast-forward of `main`).

## Before the push

- `git fetch origin`; `origin/main` = `3da96f0555ea6484ab7630654af0fc1f6ec90ceb` (the bootstrap merge).
- Candidate: `8377801ebd47f8ce1ec96eac9bd807dc5a876273`, the commit B-4 passed.
- Validate CI on the candidate: run 38406090715 (push, `pilot/site-launch-fix`, `head_sha` = the candidate), conclusion `success`.
- Ancestry, run with every inherited `GIT_*` variable removed (git 2.43.0):
  `GIT_GRAFT_FILE=/dev/null git --no-replace-objects -c core.commitGraph=false -c advice.graftFileDeprecated=false merge-base --is-ancestor 3da96f0555ea6484ab7630654af0fc1f6ec90ceb 8377801ebd47f8ce1ec96eac9bd807dc5a876273` exited 0.
- `git log --oneline 3da96f0..8377801` lists four commits on one first-parent line: `0825055` (A), `4ab1498` (C-1), `6866001` (C-2), `8377801` (C-3).

## Push

```
$ git push origin 8377801ebd47f8ce1ec96eac9bd807dc5a876273:refs/heads/main
   3da96f0..8377801  8377801ebd47f8ce1ec96eac9bd807dc5a876273 -> main
```

A fast-forward, no force.

## After the push

- `git ls-remote origin refs/heads/main` = `8377801ebd47f8ce1ec96eac9bd807dc5a876273`.
- Validate CI on `main`: run 38406646291, `head_sha` = the candidate, conclusion `success`.
- `origin/main` was merged into `pilot/site-launch-records` without force (`2452b70`). The helper there is unchanged: SHA-256 `c7f5e5ed…0d00655`.

The main freeze is in effect from this point until K.
