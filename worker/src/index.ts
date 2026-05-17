export interface Env {
  GITHUB_TOKEN: string;
  GITHUB_REPO: string;
  ADMIN_TOKEN?: string;
}

const CET_TZ = "Europe/Vienna";
const WIZZ_PDF_URL = "https://multipass.wizzair.com/aycf-availability.pdf";

function dateInCET(d: Date): string {
  return new Intl.DateTimeFormat("en-CA", {
    timeZone: CET_TZ,
    year: "numeric",
    month: "2-digit",
    day: "2-digit",
  }).format(d);
}

function todayInCET(now = new Date()): string {
  return dateInCET(now);
}

async function wizzPdfLastModifiedCET(): Promise<string | null> {
  const r = await fetch(WIZZ_PDF_URL, {
    method: "GET",
    headers: {
      Range: "bytes=0-0",
      "User-Agent": "wizz-aycf-cf-trigger",
      Accept: "*/*",
    },
  });
  const lm = r.headers.get("last-modified");
  console.log(`wizz check: status=${r.status} last-modified=${lm ?? "(none)"}`);
  if (!lm) return null;
  const d = new Date(lm);
  if (Number.isNaN(d.getTime())) return null;
  return dateInCET(d);
}

function ghHeaders(env: Env): HeadersInit {
  return {
    Authorization: `Bearer ${env.GITHUB_TOKEN}`,
    "User-Agent": "wizz-aycf-cf-trigger",
    Accept: "application/vnd.github+json",
    "X-GitHub-Api-Version": "2022-11-28",
  };
}

async function isTodayAlreadyCommitted(env: Env, today: string): Promise<boolean> {
  const url = `https://api.github.com/repos/${env.GITHUB_REPO}/contents/data`;
  const r = await fetch(url, { headers: ghHeaders(env) });
  if (!r.ok) {
    console.error(`contents/data ${r.status}: ${await r.text()}`);
    return false;
  }
  const files = (await r.json()) as Array<{ name: string; type: string }>;
  return files.some(
    (f) => f.type === "file" && f.name.startsWith(`${today}T`) && f.name.endsWith(".csv"),
  );
}

async function dispatchWorkflow(env: Env): Promise<void> {
  const url = `https://api.github.com/repos/${env.GITHUB_REPO}/actions/workflows/scrape.yaml/dispatches`;
  const body = JSON.stringify({ ref: "main" });
  const r = await fetch(url, { method: "POST", headers: ghHeaders(env), body });
  if (!r.ok) {
    throw new Error(`dispatch failed ${r.status}: ${await r.text()}`);
  }
}

async function tick(env: Env, todayOverride?: string, dryRun = false): Promise<string> {
  const today = todayOverride ?? todayInCET();
  if (await isTodayAlreadyCommitted(env, today)) {
    return `today=${today} already in repo — skipping`;
  }
  const pdfDate = await wizzPdfLastModifiedCET();
  if (pdfDate !== today) {
    return `wizz pdf last-modified=${pdfDate ?? "unknown"} != today=${today} — skipping`;
  }
  if (dryRun) {
    return `today=${today} not in repo, wizz pdf is fresh — would dispatch (dry run)`;
  }
  await dispatchWorkflow(env);
  return `dispatched scrape.yaml for ${today}`;
}

export default {
  async scheduled(_controller: ScheduledController, env: Env, ctx: ExecutionContext): Promise<void> {
    ctx.waitUntil(
      tick(env).then((msg) => console.log(msg)).catch((e) => console.error(e)),
    );
  },

  async fetch(request: Request, env: Env): Promise<Response> {
    const url = new URL(request.url);
    if (url.pathname === "/__scheduled" || url.pathname === "/run") {
      const auth = request.headers.get("Authorization") ?? "";
      const expected = env.ADMIN_TOKEN ? `Bearer ${env.ADMIN_TOKEN}` : null;
      if (!expected || auth !== expected) {
        return new Response("unauthorized\n", { status: 401 });
      }
      try {
        const override = url.searchParams.get("today") ?? undefined;
        const dryRun = url.searchParams.get("dry") === "1";
        const msg = await tick(env, override, dryRun);
        return new Response(msg + "\n", { status: 200 });
      } catch (e) {
        return new Response(`error: ${(e as Error).message}\n`, { status: 500 });
      }
    }
    return new Response("wizz-aycf-trigger\n", { status: 200 });
  },
} satisfies ExportedHandler<Env>;
