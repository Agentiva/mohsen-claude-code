import { z } from 'zod';
import type { McpServer } from '@modelcontextprotocol/sdk/server/mcp.js';
import type { IcemailClient } from '../client.js';
import { endpoint, endpointItem } from '../endpoints.js';
import { compact, guard } from './shared.js';

export function registerMailboxTools(server: McpServer, client: IcemailClient): void {
  server.registerTool(
    'icemail_list_mailboxes',
    {
      title: 'List Icemail mailboxes',
      description:
        'List provisioned mailboxes, optionally filtered by domain, provider or status. Use this before creating mailboxes to see what already exists.',
      inputSchema: {
        domain: z.string().optional().describe('Only mailboxes on this domain, e.g. "pamminger-auto.com".'),
        provider: z.enum(['google', 'microsoft']).optional(),
        status: z.string().optional().describe('Provisioning status filter, e.g. "active" or "pending".'),
        limit: z.number().int().min(1).max(200).optional(),
        page: z.number().int().min(1).optional(),
      },
      annotations: { readOnlyHint: true, openWorldHint: true },
    },
    async (args) =>
      guard(() => client.request({ method: 'GET', path: endpoint('MAILBOXES'), query: compact(args) }))
  );

  server.registerTool(
    'icemail_get_mailbox',
    {
      title: 'Get Icemail mailbox',
      description:
        'Read one mailbox by id, including provisioning status, warmup state and connection credentials (IMAP/SMTP) once ready.',
      inputSchema: { mailbox_id: z.string().min(1) },
      annotations: { readOnlyHint: true, openWorldHint: true },
    },
    async ({ mailbox_id }) =>
      guard(() => client.request({ method: 'GET', path: endpointItem('MAILBOXES', mailbox_id) }))
  );

  server.registerTool(
    'icemail_create_mailboxes',
    {
      title: 'Create Icemail mailboxes',
      description:
        'Provision N mailboxes on a domain via Google or Microsoft. This is a BILLED action — it consumes Icemail credits per mailbox. Confirm the domain, count and provider with the user first; `confirm` must be true.',
      inputSchema: {
        domain: z.string().min(1).describe('Domain the mailboxes are created on. Must already exist in Icemail.'),
        provider: z.enum(['google', 'microsoft']),
        count: z.number().int().min(1).max(100).optional().describe('How many mailboxes to create. Ignored when `mailboxes` is given.'),
        mailboxes: z
          .array(
            z.object({
              first_name: z.string().optional(),
              last_name: z.string().optional(),
              email: z.string().optional().describe('Full address or local part, depending on what the account expects.'),
            })
          )
          .optional()
          .describe('Explicit mailbox identities. Use this instead of `count` when the names matter.'),
        warmup: z.boolean().optional().describe('Start warmup immediately after provisioning.'),
        confirm: z.literal(true).describe('Must be true. Guards against accidental billed provisioning.'),
        idempotency_key: z.string().optional().describe('Reuse the same key to safely retry one logical create.'),
      },
      annotations: { readOnlyHint: false, destructiveHint: false, idempotentHint: false, openWorldHint: true },
    },
    async ({ confirm, idempotency_key, ...body }) =>
      guard(() =>
        client.request({
          method: 'POST',
          path: endpoint('MAILBOXES'),
          body: compact(body),
          idempotencyKey: idempotency_key,
        })
      )
  );

  server.registerTool(
    'icemail_update_mailbox',
    {
      title: 'Update Icemail mailbox',
      description: 'Patch a mailbox — e.g. toggle warmup, change the display name or signature.',
      inputSchema: {
        mailbox_id: z.string().min(1),
        first_name: z.string().optional(),
        last_name: z.string().optional(),
        display_name: z.string().optional(),
        signature: z.string().optional().describe('HTML signature for the mailbox.'),
        warmup: z.boolean().optional(),
      },
      annotations: { readOnlyHint: false, destructiveHint: false, idempotentHint: true, openWorldHint: true },
    },
    async ({ mailbox_id, ...body }) =>
      guard(() =>
        client.request({ method: 'PATCH', path: endpointItem('MAILBOXES', mailbox_id), body: compact(body) })
      )
  );

  server.registerTool(
    'icemail_delete_mailbox',
    {
      title: 'Delete Icemail mailbox',
      description:
        'Permanently delete a mailbox. Destructive and not reversible — any mail in it is lost and sequencers using it will start failing. `confirm` must be true.',
      inputSchema: {
        mailbox_id: z.string().min(1),
        confirm: z.literal(true).describe('Must be true. Guards against accidental deletion.'),
      },
      annotations: { readOnlyHint: false, destructiveHint: true, idempotentHint: true, openWorldHint: true },
    },
    async ({ mailbox_id }) =>
      guard(() => client.request({ method: 'DELETE', path: endpointItem('MAILBOXES', mailbox_id) }))
  );
}
