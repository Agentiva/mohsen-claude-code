import { z } from 'zod';
import type { McpServer } from '@modelcontextprotocol/sdk/server/mcp.js';
import type { IcemailClient } from '../client.js';
import { endpoint, endpointItem } from '../endpoints.js';
import { compact, guard } from './shared.js';

export function registerDomainTools(server: McpServer, client: IcemailClient): void {
  server.registerTool(
    'icemail_list_domains',
    {
      title: 'List Icemail domains',
      description: 'List domains in the Icemail account with their DNS/verification status.',
      inputSchema: {
        search: z.string().optional().describe('Substring match on the domain name.'),
        status: z.string().optional(),
        limit: z.number().int().min(1).max(200).optional(),
        page: z.number().int().min(1).optional(),
      },
      annotations: { readOnlyHint: true, openWorldHint: true },
    },
    async (args) => guard(() => client.request({ method: 'GET', path: endpoint('DOMAINS'), query: compact(args) }))
  );

  server.registerTool(
    'icemail_get_domain',
    {
      title: 'Get Icemail domain',
      description: 'Read one domain by id, including DNS records (SPF/DKIM/DMARC) and verification state.',
      inputSchema: { domain_id: z.string().min(1).describe('Domain id, or the domain name if the API accepts it.') },
      annotations: { readOnlyHint: true, openWorldHint: true },
    },
    async ({ domain_id }) => guard(() => client.request({ method: 'GET', path: endpointItem('DOMAINS', domain_id) }))
  );

  server.registerTool(
    'icemail_create_domain',
    {
      title: 'Purchase or attach an Icemail domain',
      description:
        'Register a new domain through Icemail or attach one you already own. Registering is a BILLED action. Always confirm the exact domain with the user first; `confirm` must be true.',
      inputSchema: {
        domain: z.string().min(1).describe('Fully qualified domain, e.g. "pamminger-auto.com".'),
        mode: z
          .enum(['purchase', 'attach'])
          .optional()
          .describe('"purchase" registers the domain through Icemail (billed); "attach" connects a domain you already own.'),
        redirect_url: z.string().optional().describe('Where the domain should redirect, typically the client website.'),
        organization_id: z.string().optional().describe('Assign the domain to an Icemail organization.'),
        confirm: z.literal(true).describe('Must be true. Guards against accidental billed registration.'),
        idempotency_key: z.string().optional(),
      },
      annotations: { readOnlyHint: false, destructiveHint: false, idempotentHint: false, openWorldHint: true },
    },
    async ({ confirm, idempotency_key, ...body }) =>
      guard(() =>
        client.request({
          method: 'POST',
          path: endpoint('DOMAINS'),
          body: compact(body),
          idempotencyKey: idempotency_key,
        })
      )
  );

  server.registerTool(
    'icemail_delete_domain',
    {
      title: 'Delete Icemail domain',
      description:
        'Remove a domain from Icemail. Destructive — mailboxes on the domain stop working. `confirm` must be true.',
      inputSchema: {
        domain_id: z.string().min(1),
        confirm: z.literal(true).describe('Must be true. Guards against accidental deletion.'),
      },
      annotations: { readOnlyHint: false, destructiveHint: true, idempotentHint: true, openWorldHint: true },
    },
    async ({ domain_id }) => guard(() => client.request({ method: 'DELETE', path: endpointItem('DOMAINS', domain_id) }))
  );
}
