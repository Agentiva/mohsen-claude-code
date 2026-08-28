#!/usr/bin/env node
import { McpServer } from '@modelcontextprotocol/sdk/server/mcp.js';
import { StdioServerTransport } from '@modelcontextprotocol/sdk/server/stdio.js';
import { IcemailClient } from './client.js';
import { loadConfig } from './config.js';
import { registerDomainTools } from './tools/domains.js';
import { registerExportTools } from './tools/exports.js';
import { registerInboxTools } from './tools/inbox.js';
import { registerMailboxTools } from './tools/mailboxes.js';
import { registerRawTools } from './tools/raw.js';
import { registerWebhookTools } from './tools/webhooks.js';

async function main(): Promise<void> {
  const config = loadConfig();
  const client = new IcemailClient(config);

  const server = new McpServer(
    { name: 'icemail', version: '0.1.0' },
    {
      instructions:
        'Tools for the Icemail API: provision Google/Microsoft mailboxes, manage domains, export mailboxes to ' +
        'sequencers and read the unified inbox. Creating domains and mailboxes is billed, so those tools require ' +
        'confirm: true — check the exact domain, provider and count with the user before calling them. For an ' +
        'endpoint without a dedicated tool, look it up with icemail_openapi and call it via icemail_request.',
    }
  );

  registerMailboxTools(server, client);
  registerDomainTools(server, client);
  registerExportTools(server, client);
  registerInboxTools(server, client);
  registerWebhookTools(server, client);
  registerRawTools(server, client, config);

  await server.connect(new StdioServerTransport());
}

main().catch((error: unknown) => {
  // stdout is the MCP transport — diagnostics must go to stderr.
  console.error(`icemail-mcp failed to start: ${error instanceof Error ? error.message : String(error)}`);
  process.exit(1);
});
