import { z } from 'zod';
import type { McpServer } from '@modelcontextprotocol/sdk/server/mcp.js';
import type { IcemailClient } from '../client.js';
import { endpoint, endpointItem } from '../endpoints.js';
import { compact, guard } from './shared.js';

export function registerExportTools(server: McpServer, client: IcemailClient): void {
  server.registerTool(
    'icemail_list_exports',
    {
      title: 'List Icemail exports',
      description: 'List export jobs that push mailboxes into a sequencer (Instantly, Smartlead, Bison, ...).',
      inputSchema: {
        status: z.string().optional(),
        limit: z.number().int().min(1).max(200).optional(),
        page: z.number().int().min(1).optional(),
      },
      annotations: { readOnlyHint: true, openWorldHint: true },
    },
    async (args) => guard(() => client.request({ method: 'GET', path: endpoint('EXPORTS'), query: compact(args) }))
  );

  server.registerTool(
    'icemail_get_export',
    {
      title: 'Get Icemail export',
      description: 'Read one export job, including per-mailbox results and any connection errors.',
      inputSchema: { export_id: z.string().min(1) },
      annotations: { readOnlyHint: true, openWorldHint: true },
    },
    async ({ export_id }) => guard(() => client.request({ method: 'GET', path: endpointItem('EXPORTS', export_id) }))
  );

  server.registerTool(
    'icemail_create_export',
    {
      title: 'Export Icemail mailboxes to a sequencer',
      description:
        'Push mailboxes into a sending platform. Runs asynchronously — poll icemail_get_export for the result. Connecting mailboxes starts real sending capacity, so confirm the target platform and mailbox set with the user first.',
      inputSchema: {
        destination: z
          .string()
          .min(1)
          .describe('Target platform, e.g. "instantly", "smartlead" or "bison". Use the identifier the API expects.'),
        mailbox_ids: z.array(z.string().min(1)).min(1).describe('Mailboxes to export.'),
        api_key: z.string().optional().describe('Destination platform API key, when the account is not already connected.'),
        workspace_id: z.string().optional().describe('Destination workspace/campaign id, when the platform needs one.'),
        confirm: z.literal(true).describe('Must be true.'),
        idempotency_key: z.string().optional(),
      },
      annotations: { readOnlyHint: false, destructiveHint: false, idempotentHint: false, openWorldHint: true },
    },
    async ({ confirm, idempotency_key, ...body }) =>
      guard(() =>
        client.request({
          method: 'POST',
          path: endpoint('EXPORTS'),
          body: compact(body),
          idempotencyKey: idempotency_key,
        })
      )
  );
}
