# Live settings change: turning on GitHub Pages

- **Preview:** shown to the owner in plain language on 2026-10-13. It covered:
  - steps: Settings → Pages → Build and deployment → Source → "GitHub Actions";
  - effect: allows a deploy workflow to publish, with nothing published yet;
  - exposure: none;
  - check: the site address still returns 404;
  - rollback: switch Source back, harmless with nothing deployed.
- **Owner action:** the owner made the change and sent a screenshot of the settings page. It showed Source **"GitHub Actions"**, suggested workflows ("GitHub Pages Jekyll", "Static HTML"), and the text "Workflow details will appear here once your site has been deployed." The screenshot is not stored in the repository.
- **Verification (2026-10-13T13:16:14Z):** `curl -sS --compressed 'https://saxton-network.github.io/site/?cb=<nonce>'` returned 404. Nothing is published, as expected.
- **Pages enablement remains accepted unknown 2.** This session cannot read the setting itself; the owner's screenshot is the evidence.
