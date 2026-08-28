import { z } from 'zod';
import type { McpServer } from '@modelcontextprotocol/sdk/server/mcp.js';
import type { IcemailClient } from '../client.js';
import { endpoint, endpointItem } from '../endpoints.js';
import { compact, guard } from './shared.js';

export function registerWebhookTools(server: McpServer, client: IcemailClient): void {
  server.registerTool(
    'icemail_list_webhooks',
    {
      title: 'List Icemail webhooks',
      description: 'List webhook subscriptions for async job completion and reply events.',
      inputSchema: {},
      annotations: { readOnlyHint: true, openWorldHint: true },
    },
    async () => guard(() => client.request({ method: 'GET', path: endpoint('WEBHOOKS') }))
  );

  server.registerTool(
    'icemail_create_webhook',
    {
      title: 'Create Icemail webhook',
      description: 'Subscribe an HTTPS endpoint to Icemail events (provisioning finished, reply received, ...).',
      inputSchema: {
        url: z.string().url().describe('HTTPS endpoint that receives the event payloads.'),
        events: z.array(z.string().min(1)).min(1).describe('Event names to subscribe to.'),
        secret: z.string().optional().describe('Shared secret used to sign deliveries.'),
        idempotency_key: z.string().optional(),
      },
      annotations: { readOnlyHint: false, destructiveHint: false, idempotentHint: false, openWorldHint: true },
    },
    async ({ idempotency_key, ...body }) =>
      guard(() =>
        client.request({
          method: 'POST',
          path: endpoint('WEBHOOKS'),
          body: compact(body),
          idempotencyKey: idempotency_key,
        })
      )
  );

  server.registerTool(
    'icemail_delete_webhook',
    {
      title: 'Delete Icemail webhook',
      description: 'Remove a webhook subscription. `confirm` must be true.',
      inputSchema: {
        webhook_id: z.string().min(1),
        confirm: z.literal(true).describe('Must be true.'),
      },
      annotations: { readOnlyHint: false, destructiveHint: true, idempotentHint: true, openWorldHint: true },
    },
    async ({ webhook_id }) =>
      guard(() => client.request({ method: 'DELETE', path: endpointItem('WEBHOOKS', webhook_id) }))
  );
}
