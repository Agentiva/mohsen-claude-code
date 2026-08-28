/**
 * Every Icemail path this server calls, in one place.
 *
 * The paths below follow the public API reference (https://docs.icemail.ai).
 * If Icemail moves or renames a route, correct it here — or override a single
 * route at runtime without touching code, e.g.
 *   ICEMAIL_PATH_MAILBOXES=/v1/inboxes
 * Anything not covered here is still reachable through the icemail_request tool.
 */
const DEFAULTS = {
  MAILBOXES: '/v1/mailboxes',
  DOMAINS: '/v1/domains',
  EXPORTS: '/v1/exports',
  INBOX_THREADS: '/v1/inbox/threads',
  WEBHOOKS: '/v1/webhooks',
} as const;

export type EndpointName = keyof typeof DEFAULTS;

export function endpoint(name: EndpointName): string {
  const override = process.env[`ICEMAIL_PATH_${name}`]?.trim();
  return (override || DEFAULTS[name]).replace(/\/+$/, '');
}

/** Path for a single resource, e.g. endpointItem('MAILBOXES', 'mb_123'). */
export function endpointItem(name: EndpointName, id: string): string {
  return `${endpoint(name)}/${encodeURIComponent(id)}`;
}
