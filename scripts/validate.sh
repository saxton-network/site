#!/usr/bin/env bash
# Repository gate. Fails on any error.
#  1. Verifies every SHA-256 recorded in ADOPTION.md against the files.
#  2. Runs scripts/check-site.py when it exists; otherwise prints a note.
#  3. Validates every agent-work/<workflow-id>/manifest.toml with the Workflow helper.
set -Eeuo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT_DIR"

# 1. Vendored file hashes. ADOPTION.md rows have the form:
# | `<path here>` | `<source path>` | `<40-hex source commit>` | `<64-hex sha256>` |
row='^\| `([^`]+)` \| `([^`]+)` \| `([0-9a-f]{40})` \| `([0-9a-f]{64})` \|'
checked=0
failed=0
declare -A seen=()
while IFS= read -r line; do
  [[ "$line" =~ $row ]] || continue
  path="${BASH_REMATCH[1]}"
  expected="${BASH_REMATCH[4]}"
  if [[ -n "${seen[$path]:-}" ]]; then
    echo "FAIL: $path is recorded more than once in ADOPTION.md" >&2
    failed=1
    continue
  fi
  seen[$path]=1
  if [[ ! -f "$path" ]]; then
    echo "FAIL: $path is recorded in ADOPTION.md but missing" >&2
    failed=1
    continue
  fi
  actual="$(sha256sum -- "$path")"
  actual="${actual%% *}"
  if [[ "$actual" != "$expected" ]]; then
    echo "FAIL: $path SHA-256 is $actual, ADOPTION.md records $expected" >&2
    failed=1
    continue
  fi
  checked=$((checked + 1))
done < ADOPTION.md
if [[ "$failed" -ne 0 ]]; then
  exit 1
fi
if [[ "$checked" -eq 0 ]]; then
  echo "FAIL: no SHA-256 entries found in ADOPTION.md" >&2
  exit 1
fi
echo "PASS: $checked vendored file hashes match ADOPTION.md"

# 2. Site checks (added later).
if [[ -f scripts/check-site.py ]]; then
  python3 scripts/check-site.py
  echo "PASS: scripts/check-site.py"
else
  echo "NOTE: scripts/check-site.py does not exist yet; site checks skipped"
fi

# 3. Workflow manifests.
shopt -s nullglob
manifests=(agent-work/*/manifest.toml)
shopt -u nullglob
if [[ "${#manifests[@]}" -eq 0 ]]; then
  echo "NOTE: no agent-work/<workflow-id>/manifest.toml found; nothing to validate"
fi
for manifest in "${manifests[@]}"; do
  id="$(basename "$(dirname "$manifest")")"
  echo "== agent-task.py $id --all"
  python3 scripts/agent-task.py "$id" --all
  echo "PASS: $manifest"
done

echo "PASS: repository validation"
