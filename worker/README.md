# wizz-aycf-trigger

Cloudflare Worker that reliably triggers the `wizz-scrape` GitHub Action every morning
at ~07:01 CET via `repository_dispatch`. Replaces the best-effort GitHub Actions cron
trigger; the scheduled cron in `.github/workflows/scrape.yaml` stays as a fallback.

## Logic per cron tick

1. Compute today's date in Europe/Vienna.
2. List `data/` via GitHub Contents API.
3. If a `${today}T*.csv` already exists -> exit (idempotent).
4. Otherwise POST to `/repos/.../dispatches` with `event_type=wizz-scrape`.

The cron runs `"1-15 6 * * *"` (winter, CET=UTC+1) and `"1-15 5 * * *"` (summer, CEST=UTC+2),
so it tries every minute for 15 minutes. The skip-guard means the first success wins.

## Setup

```
npm install
wrangler login
wrangler secret put GITHUB_TOKEN   # fine-grained PAT, repo scope: Contents:read + Actions:write
wrangler deploy
```

## Test locally

```
npm run dev
# in another shell:
curl http://localhost:8787/__scheduled
```

`wrangler dev` reads the secret from `.dev.vars` (gitignored) for local testing:

```
echo 'GITHUB_TOKEN=github_pat_...' > .dev.vars
```
