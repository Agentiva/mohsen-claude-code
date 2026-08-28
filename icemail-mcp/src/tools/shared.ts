import { IcemailApiError, type IcemailResponse } from '../client.js';

export interface ToolResult {
  content: Array<{ type: 'text'; text: string }>;
  isError?: boolean;
  [key: string]: unknown;
}

export function ok(response: IcemailResponse): ToolResult {
  return {
    content: [{ type: 'text', text: JSON.stringify({ status: response.status, data: response.data }, null, 2) }],
  };
}

export function fail(error: unknown): ToolResult {
  const payload =
    error instanceof IcemailApiError
      ? { error: error.message, status: error.status, url: error.url, body: error.body }
      : { error: error instanceof Error ? error.message : String(error) };
  return {
    content: [{ type: 'text', text: JSON.stringify(payload, null, 2) }],
    isError: true,
  };
}

/** Wraps a tool handler so API failures come back as tool errors, not crashes. */
export async function guard(fn: () => Promise<IcemailResponse>): Promise<ToolResult> {
  try {
    return ok(await fn());
  } catch (error) {
    return fail(error);
  }
}

/** Drops undefined keys so optional args are never sent as explicit nulls. */
export function compact<T extends Record<string, unknown>>(input: T): Record<string, unknown> {
  return Object.fromEntries(Object.entries(input).filter(([, value]) => value !== undefined));
}
