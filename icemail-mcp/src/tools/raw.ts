import { z } from 'zod';
import type { McpServer } from '@modelcontextprotocol/sdk/server/mcp.js';
import type { IcemailClient } from '../client.js';
import type { IcemailConfig } from '../config.js';
import { compact, fail, guard, type ToolResult } from './shared.js';

export function registerRawTools(server: McpServer, client: IcemailClient, config: IcemailConfig): void {
  server.registerTool(
    'icemail_request',
    {
      title: 'Call any Icemail endpoint',
      description:
        'Escape hatch for endpoints without a dedicated tool. Authentication, retries and idempotency keys are handled for you — pass only the method, path and payload. Prefer the specific tools when one fits; use icemail_openapi first if you are unsure the path exists.',
      inputSchema: {
        method: z.enum(['GET', 'POST', 'PATCH', 'PUT', 'DELETE']),
        path: z.string().min(1).describe('Path below the API host, e.g. "/v1/mailboxes/mb_123".'),
        query: z.record(z.union([z.string(), z.number(), z.boolean(), z.array(z.string())])).optional(),
        body: z.record(z.unknown()).optional().describe('JSON request body for write methods.'),
        idempotency_key: z.string().optional(),
      },
      annotations: { readOnlyHint: false, destructiveHint: true, idempotentHint: false, openWorldHint: true },
    },
    async ({ method, path, query, body, idempotency_key }) =>
      guard(() => client.request({ method, path, query: compact(query ?? {}), body, idempotencyKey: idempotency_key }))
  );

  server.registerTool(
    'icemail_openapi',
    {
      title: 'Fetch the Icemail API spec',
      description:
        'Download the machine-readable Icemail OpenAPI spec and list its endpoints. Use this to confirm the exact path, method and payload of an endpoint before calling icemail_request, or when a dedicated tool returns 404 because a route moved.',
      inputSchema: {
        filter: z.string().optional().describe('Only list paths containing this substring, e.g. "mailbox".'),
        full: z
          .boolean()
          .optional()
          .describe('Return the raw spec instead of the endpoint summary. Large — only when you need schemas.'),
      },
      annotations: { readOnlyHint: true, openWorldHint: true },
    },
    async ({ filter, full }) => fetchSpec(config, filter, full ?? false)
  );
}

const SPEC_CANDIDATES = ['/openapi.json', '/openapi.yaml', '/spec.json', '/swagger.json', '/api.json'];

async function fetchSpec(config: IcemailConfig, filter?: string, full = false): Promise<ToolResult> {
  const tried: string[] = [];
  for (const base of [config.docsUrl, config.baseUrl]) {
    for (const candidate of SPEC_CANDIDATES) {
      const url = `${base}${candidate}`;
      tried.push(url);
      try {
        const response = await fetch(url, {
          headers: { Accept: 'application/json' },
          signal: AbortSignal.timeout(config.timeoutMs),
        });
        if (!response.ok) continue;
        const text = await response.text();
        let spec: unknown;
        try {
          spec = JSON.parse(text);
        } catch {
          continue; // YAML or an HTML shell — keep looking for a JSON spec.
        }
        return {
          content: [
            {
              type: 'text',
              text: full ? text : JSON.stringify({ source: url, endpoints: summarize(spec, filter) }, null, 2),
            },
          ],
        };
      } catch {
        continue;
      }
    }
  }
  return fail(
    new Error(
      `No machine-readable OpenAPI spec found. Tried: ${tried.join(', ')}. ` +
        'Set ICEMAIL_DOCS_URL to the host serving the spec, or read https://docs.icemail.ai by hand.'
    )
  );
}

function summarize(spec: unknown, filter?: string): Array<{ method: string; path: string; summary?: string }> {
  const paths = (spec as { paths?: Record<string, Record<string, { summary?: string }>> })?.paths;
  if (!paths) return [];
  const needle = filter?.toLowerCase();
  const out: Array<{ method: string; path: string; summary?: string }> = [];
  for (const [path, operations] of Object.entries(paths)) {
    if (needle && !path.toLowerCase().includes(needle)) continue;
    for (const [method, operation] of Object.entries(operations)) {
      if (!['get', 'post', 'put', 'patch', 'delete'].includes(method)) continue;
      out.push({ method: method.toUpperCase(), path, summary: operation?.summary });
    }
  }
  return out;
}
