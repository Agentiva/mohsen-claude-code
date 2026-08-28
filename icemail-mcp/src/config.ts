export interface IcemailConfig {
  apiKey: string;
  baseUrl: string;
  timeoutMs: number;
  maxRetries: number;
  /** Docs site used by icemail_openapi to fetch the machine-readable spec. */
  docsUrl: string;
}

function envInt(name: string, fallback: number): number {
  const raw = process.env[name];
  if (!raw) return fallback;
  const parsed = Number.parseInt(raw, 10);
  if (!Number.isFinite(parsed) || parsed <= 0) {
    throw new Error(`${name} must be a positive integer, got ${JSON.stringify(raw)}`);
  }
  return parsed;
}

export function loadConfig(): IcemailConfig {
  const apiKey = process.env.ICEMAIL_API_KEY?.trim();
  if (!apiKey) {
    throw new Error(
      'ICEMAIL_API_KEY is not set. Put your Icemail API key in the environment ' +
        '(e.g. the "env" block of your MCP client config) and restart the server.'
    );
  }

  return {
    apiKey,
    baseUrl: (process.env.ICEMAIL_BASE_URL?.trim() || 'https://api.icemail.ai').replace(/\/+$/, ''),
    timeoutMs: envInt('ICEMAIL_TIMEOUT_MS', 60_000),
    maxRetries: envInt('ICEMAIL_MAX_RETRIES', 2),
    docsUrl: (process.env.ICEMAIL_DOCS_URL?.trim() || 'https://docs.icemail.ai').replace(/\/+$/, ''),
  };
}
