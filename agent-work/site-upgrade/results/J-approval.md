# Task J: owner approval

On 2026-10-14 the coordinator showed the owner the plain-language live preview in this conversation, immediately before the owner's answer. The preview covered the visitor-visible date line, earlier public exposure of v2, main already holding v2, time and caching, the two possible dispatches and their hashes, the frozen fingerprint, checks and stop conditions, the emergency Unpublish option, the retry boundary and freeze, the four end states, and the dated ambiguity-7 clarification.

The question was: "Approve, and can you be reached within about 30 minutes if the rollback itself fails? (y/n)". The owner answered `y`. This answers both parts of that question: approval and availability within about 30 minutes if the rollback itself fails. The preview expressly said that a yes without availability counts as no.

This is the coordinator's own account of a chat approval. The platform exposes no message link or identifier, or exact message timestamps, for this exchange. The record was written on 2026-10-14 after the answer and before any dispatch.

## Exact approved batch

- Source: `95914a54336983fc48e286b8e16cb6780076d2f2`.
- Frozen batch fingerprint: `fcbe26fca2a95d6bcc621dbf27dd27b53eef7bc263c06e254f7404b8a2e1f33d`.
- One dispatch of `.github/workflows/deploy.yml` on `main`, using `agent-work/site-upgrade/results/R-dispatch-inputs.json`, with `sha=95914a54336983fc48e286b8e16cb6780076d2f2`. Input-file SHA-256: `6885c1e7e99229cda6ec3afaf5b74a31280b66717600c29983ace0433a3d4535`.
- At most one rollback dispatch of that workflow on `main`, using `agent-work/site-upgrade/results/R-rollback-inputs.json`, with `sha=8377801ebd47f8ce1ec96eac9bd807dc5a876273`. Input-file SHA-256: `927b8539ce464e5e7cd1c65b1b1d720f9b2ce972f2f2d39ce52744e8e054650a`. This is approved only under `CONTRACT.md` "Rollback (V)": J failed with `liveStateChanged` not false, its run completed, and the rollback recheck passes. If nothing published is proven, no rollback dispatch is approved.
- A cancel only for a run still unfinished after the 45-minute wait, followed by up to 10 minutes waiting for completion. No other cancel is approved. If it still has not completed, stop and ask the owner; do not dispatch rollback.

This approval does not cover a retry, another source or batch, a settings change (including Unpublish), a push to main, either records or history PR merge, or the later batch. Changed inputs require fresh readiness and approval.

## Clarification in force

The plan's 2026-10-14 ambiguity-7 correction applies: the alpha.13 threat model still mentions `docs/PILOT-HISTORY.md`; upstream adoption guidance explains that such references point back to Workflow. The ambiguity is answered, rather than removed. B-1 reviewed this clarification, and this preview included it.
