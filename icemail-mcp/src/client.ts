import { randomUUID } from 'node:crypto';
import type { IcemailConfig } from './config.js';

export type HttpMethod = 'GET' | 'POST' | 'PATCH' | 'PUT' | 'DELETE';

export interface RequestOptions {
  method: HttpMethod;
  path: string;
  query?: Record<string, unknown>;
  body?: unknown;
  /** Sent as Idempotency-Key. Generated for writes when omitted. */
  idempotencyKey?: string;
}

export interface IcemailResponse {
  status: number;
  ok: boolean;
  url: string;
  data: unknown;
}

export class IcemailApiError extends Error {
  constructor(
    readonly status: number,
    readonly url: string,
    readonly body: unknown,
    message: string
  ) {
    super(message);
    this.name = 'IcemailApiError';
  }
}

const RETRYABLE_STATUS = new Set([408, 425, 429, 500, 502, 503, 504]);

export class IcemailClient {
  constructor(private readonly config: IcemailConfig) {}

  async request(options: RequestOptions): Promise<IcemailResponse> {
    const url = this.buildUrl(options.path, options.query);
    const isWrite = options.method !== 'GET';

    const headers: Record<string, string> = {
      Authorization: `Bearer ${this.config.apiKey}`,
      Accept: 'application/json',
      'User-Agent': 'icemail-mcp/0.1.0',
    };
    if (options.body !== undefined) headers['Content-Type'] = 'application/json';
    if (isWrite) headers['Idempotency-Key'] = options.idempotencyKey ?? randomUUID();

    let lastError: unknown;
    for (let attempt = 0; attempt <= this.config.maxRetries; attempt++) {
      if (attempt > 0) await sleep(Math.min(2 ** attempt * 500, 8_000));

      let response: Response;
      try {
        response = await fetch(url, {
          method: options.method,
          headers,
          body: options.body === undefined ? undefined : JSON.stringify(options.body),
          signal: AbortSignal.timeout(this.config.timeoutMs),
        });
      } catch (error) {
        // Network/timeout failures are safe to retry: writes carry a stable
        // Idempotency-Key across attempts, so a replayed create cannot double-charge.
        lastError = error;
        continue;
      }

      const data = await parseBody(response);
      if (response.ok) return { status: response.status, ok: true, url, data };

      if (RETRYABLE_STATUS.has(response.status) && attempt < this.config.maxRetries) {
        lastError = new IcemailApiError(response.status, url, data, describe(response.status, data));
        continue;
      }

      throw new IcemailApiError(response.status, url, data, describe(response.status, data));
    }

    if (lastError instanceof IcemailApiError) throw lastError;
    throw new Error(
      `Icemail request to ${url} failed after ${this.config.maxRetries + 1} attempt(s): ${
        lastError instanceof Error ? lastError.message : String(lastError)
      }`
    );
  }

  private buildUrl(path: string, query?: Record<string, unknown>): string {
    const normalized = path.startsWith('/') ? path : `/${path}`;
    const url = new URL(this.config.baseUrl + normalized);
    for (const [key, value] of Object.entries(query ?? {})) {
      if (value === undefined || value === null) continue;
      if (Array.isArray(value)) {
        for (const item of value) url.searchParams.append(key, String(item));
      } else {
        url.searchParams.set(key, String(value));
      }
    }
    return url.toString();
  }
}

async function parseBody(response: Response): Promise<unknown> {
  const text = await response.text();
  if (!text) return null;
  try {
    return JSON.parse(text);
  } catch {
    return text;
  }
}

function describe(status: number, body: unknown): string {
  const detail =
    typeof body === 'string'
      ? body.slice(0, 500)
      : JSON.stringify(body ?? {}).slice(0, 500);
  return `Icemail API returned ${status}: ${detail}`;
}

function sleep(ms: number): Promise<void> {
  return new Promise((resolve) => setTimeout(resolve, ms));
}
