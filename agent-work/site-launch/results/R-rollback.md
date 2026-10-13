# Rollback artifact: pages-unpublished-404

- **Identity:** `pages-unpublished-404`. Before launch nothing is published, so the state to return to is "no site": `https://saxton-network.github.io/site/` returns 404.
- **Provenance:** the pre-launch baseline in `R.md` (status 404 at 2026-10-13T13:39:28Z) and `pages-enable.md` (404 after Pages was turned on).
- **How it is restored:** only by the owner, in Settings → Pages → Unpublish site, after seeing what failed (`CONTRACT.md` "Rollback"). This session has no tool that unpublishes.
- **How it is verified:** task V fetches `curl -sS --compressed 'https://saxton-network.github.io/site/?cb=<nonce>'` every 30 seconds, for up to 10 minutes, until it returns 404.
