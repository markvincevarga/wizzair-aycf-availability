## Deployment (Cloudflare Workers)

- Site: https://aycf.mvarga.dev, Worker `aycf`. There is no GitHub Actions or GitHub Pages deployment.
- After merging to `main`, run `npm run deploy` on an up-to-date `main`.
- When creating a pull request, run `npx cf previews deploy` from the PR branch and put the `preview_urls` entry (stable per branch) in the PR description. Re-run after more pushes.
- After merging or closing a pull request, delete the branch preview: `npx cf previews delete <branch-name> --worker aycf --force`.
- Check `npx cf auth whoami` before deploying. If not signed in, ask the user to run `! npx cf auth login`.
- Never use `--temporary-account` or `--delete-with-references`, and never commit API tokens.
- The daily scrape (`.github/workflows/scrape.yaml`) commits new CSVs plus `docs/aggregated-data.json` to `main`, then triggers `.github/workflows/deploy.yaml`, which runs `npm run deploy` using the repo secrets `CLOUDFLARE_API_TOKEN` and `CLOUDFLARE_ACCOUNT_ID`. Do not remove these workflows. For a manual deploy, run `npm run deploy` locally.
- The `worker/` directory is a separate Worker (`wizz-aycf-trigger`) that dispatches the scrape. It is not the site.
