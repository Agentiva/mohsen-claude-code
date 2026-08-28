# icemail-mcp

MCP server for the [Icemail API](https://icemail.ai/icemail-api) — provision Google/Microsoft
mailboxes, manage sending domains, export mailboxes to sequencers and read the unified inbox
from Claude Code, Claude Desktop, Cursor or any other MCP client.

## Setup

```bash
cd icemail-mcp
npm install
npm run build
```

Then point your MCP client at `dist/index.js` and pass the API key through `env`:

```json
{
  "mcpServers": {
    "icemail": {
      "command": "node",
      "args": ["/absolute/path/to/icemail-mcp/dist/index.js"],
      "env": { "ICEMAIL_API_KEY": "your-icemail-api-key" }
    }
  }
}
```

In Claude Code the repo's `.mcp.json` already declares the server and reads
`ICEMAIL_API_KEY` from the environment. Either export it before starting Claude Code:

```bash
export ICEMAIL_API_KEY=your-icemail-api-key
```

...or put it in `.claude/settings.local.json`, which is gitignored:

```json
{ "env": { "ICEMAIL_API_KEY": "your-icemail-api-key" } }
```

`dist/` is not committed, so run `npm install && npm run build` in `icemail-mcp/`
after cloning — without it the server cannot start and shows as failed to connect.

## Configuration

| Variable | Default | Purpose |
| --- | --- | --- |
| `ICEMAIL_API_KEY` | — | **Required.** Sent as `Authorization: Bearer <key>`. |
| `ICEMAIL_BASE_URL` | `https://api.icemail.ai` | API host. |
| `ICEMAIL_DOCS_URL` | `https://docs.icemail.ai` | Where `icemail_openapi` looks for the spec. |
| `ICEMAIL_TIMEOUT_MS` | `60000` | Per-request timeout. |
| `ICEMAIL_MAX_RETRIES` | `2` | Retries on 429/5xx and network errors. |
| `ICEMAIL_PATH_<ROUTE>` | see `src/endpoints.ts` | Override a single route without editing code. |

## Tools

**Mailboxes** — `icemail_list_mailboxes`, `icemail_get_mailbox`, `icemail_create_mailboxes`,
`icemail_update_mailbox`, `icemail_delete_mailbox`

**Domains** — `icemail_list_domains`, `icemail_get_domain`, `icemail_create_domain`,
`icemail_delete_domain`

**Exports** — `icemail_list_exports`, `icemail_get_export`, `icemail_create_export`

**Unified inbox** — `icemail_list_inbox_threads`, `icemail_get_inbox_thread`

**Webhooks** — `icemail_list_webhooks`, `icemail_create_webhook`, `icemail_delete_webhook`

**Escape hatches** — `icemail_request` (call any endpoint), `icemail_openapi` (fetch the spec
and list its endpoints)

### Safety

Billed and destructive tools (`icemail_create_domain`, `icemail_create_mailboxes`,
`icemail_create_export`, every delete) require `confirm: true`, so an agent cannot register a
domain or provision mailboxes by accident. Writes carry an `Idempotency-Key` — a retried
create replays instead of double-charging.

## Verifying the endpoint surface

The route paths in `src/endpoints.ts` follow Icemail's published API reference
(`POST /v1/mailboxes`, `GET /v1/mailboxes/:id`, `POST /v1/domains`, `POST /v1/exports`,
`GET /v1/inbox/threads`). Request and response field names for the write endpoints were not
verifiable from a network-restricted environment. Before relying on them:

1. Run `icemail_openapi` — it downloads the spec and lists every real method/path.
2. Correct anything that differs in `src/endpoints.ts`, or override it with
   `ICEMAIL_PATH_<ROUTE>`.
3. Anything without a dedicated tool works today through `icemail_request`.

Icemail also publishes its own hosted MCP server; if you only need the standard provisioning
tools, compare it against this one before investing in local maintenance.
