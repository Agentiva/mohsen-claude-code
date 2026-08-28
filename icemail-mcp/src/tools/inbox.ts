import { z } from 'zod';
import type { McpServer } from '@modelcontextprotocol/sdk/server/mcp.js';
import type { IcemailClient } from '../client.js';
import { endpoint, endpointItem } from '../endpoints.js';
import { compact, guard } from './shared.js';

export function registerInboxTools(server: McpServer, client: IcemailClient): void {
  server.registerTool(
    'icemail_list_inbox_threads',
    {
      title: 'List unified-inbox threads',
      description:
        'Query threads and replies across every connected mailbox. Use this to find replies, bounces and out-of-office responses without opening each mailbox.',
      inputSchema: {
        mailbox_id: z.string().optional().describe('Restrict to one mailbox.'),
        domain: z.string().optional().describe('Restrict to mailboxes on one domain.'),
        query: z.string().optional().describe('Full-text search across subject and body.'),
        status: z.string().optional().describe('Thread status filter, e.g. "unread" or "replied".'),
        since: z.string().optional().describe('ISO 8601 lower bound on the last message time.'),
        until: z.string().optional().describe('ISO 8601 upper bound on the last message time.'),
        limit: z.number().int().min(1).max(200).optional(),
        page: z.number().int().min(1).optional(),
      },
      annotations: { readOnlyHint: true, openWorldHint: true },
    },
    async (args) =>
      guard(() => client.request({ method: 'GET', path: endpoint('INBOX_THREADS'), query: compact(args) }))
  );

  server.registerTool(
    'icemail_get_inbox_thread',
    {
      title: 'Get unified-inbox thread',
      description: 'Read one thread with its full message history.',
      inputSchema: { thread_id: z.string().min(1) },
      annotations: { readOnlyHint: true, openWorldHint: true },
    },
    async ({ thread_id }) =>
      guard(() => client.request({ method: 'GET', path: endpointItem('INBOX_THREADS', thread_id) }))
  );
}
