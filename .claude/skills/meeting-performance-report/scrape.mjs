// scrape.mjs — Headless-Scraper für app.amplifa.ai
//
// Loggt sich mit App-eigenem Login (E-Mail + Passwort, KEIN Google-SSO) ein,
// öffnet die Admin-/Reports-Ansicht, liest pro Kunde die Meeting-Anzahl der
// rollierenden letzten 7 Tage aus und gibt das Ergebnis als JSON auf stdout aus.
//
// Aufruf:   node scrape.mjs
// Output:   eine einzige JSON-Zeile auf stdout (siehe Schema unten).
// Fehler:   JSON mit { ok:false, error, debug } auf stdout, Exit-Code 1.
//           Zusätzlich werden bei Fehler (oder SCRAPE_DEBUG=1) Screenshot +
//           Seiten-HTML nach ./debug/ geschrieben, damit Selektoren kalibriert
//           werden können.
//
// Konfiguration ausschließlich über ENV (Secrets) + selectors.json:
//   AMPLIFA_BASE_URL     Default https://app.amplifa.ai
//   AMPLIFA_EMAIL        Pflicht  – Login-E-Mail (Secret)
//   AMPLIFA_PASSWORD     Pflicht  – Login-Passwort (Secret)
//   AMPLIFA_REPORTS_PATH Optional – überschreibt reports.path aus selectors.json
//   AMPLIFA_SELECTORS    Optional – Pfad zur Selektor-Datei (Default ./selectors.json,
//                        Fallback ./selectors.example.json)
//   SCRAPE_DEBUG=1       Optional – immer Screenshot+HTML dumpen
//   SCRAPE_HEADFUL=1     Optional – sichtbarer Browser (nur lokal zum Debuggen)

import { chromium } from 'playwright-core'
import { readFileSync, mkdirSync, writeFileSync, existsSync } from 'node:fs'
import { fileURLToPath } from 'node:url'
import { dirname, resolve } from 'node:path'

const HERE = dirname(fileURLToPath(import.meta.url))
const RANGE_DAYS = 7

// ---------------------------------------------------------------- Konfiguration
const BASE_URL = (process.env.AMPLIFA_BASE_URL || 'https://app.amplifa.ai').replace(/\/+$/, '')
const EMAIL = process.env.AMPLIFA_EMAIL
const PASSWORD = process.env.AMPLIFA_PASSWORD
const DEBUG = process.env.SCRAPE_DEBUG === '1'
const HEADFUL = process.env.SCRAPE_HEADFUL === '1'

function loadSelectors() {
  const explicit = process.env.AMPLIFA_SELECTORS && resolve(process.env.AMPLIFA_SELECTORS)
  const candidates = [
    explicit,
    resolve(HERE, 'selectors.json'),
    resolve(HERE, 'selectors.example.json'),
  ].filter(Boolean)
  for (const p of candidates) {
    if (existsSync(p)) return { path: p, data: JSON.parse(readFileSync(p, 'utf8')) }
  }
  throw new Error('Keine selectors.json / selectors.example.json gefunden')
}

// ------------------------------------------------------------------- Hilfsmittel
function fail(error, extra = {}) {
  process.stdout.write(JSON.stringify({ ok: false, error: String(error), ...extra }) + '\n')
  process.exit(1)
}

async function dump(page, label) {
  try {
    const dir = resolve(HERE, 'debug')
    mkdirSync(dir, { recursive: true })
    await page.screenshot({ path: resolve(dir, `${label}.png`), fullPage: true }).catch(() => {})
    writeFileSync(resolve(dir, `${label}.html`), await page.content().catch(() => ''), 'utf8')
    return resolve(dir, `${label}.html`)
  } catch {
    return null
  }
}

// Wandelt "12", "1.234", "8 Meetings", "—", "" robust in eine Zahl (oder null).
function toNumber(raw) {
  if (raw == null) return null
  const m = String(raw).replace(/ /g, ' ').match(/-?\d[\d.\s]*/)
  if (!m) return null
  const n = Number(m[0].replace(/[.\s]/g, ''))
  return Number.isFinite(n) ? n : null
}

// ------------------------------------------------------------------------- Main
async function run() {
  if (!EMAIL || !PASSWORD) fail('AMPLIFA_EMAIL und/oder AMPLIFA_PASSWORD nicht gesetzt (als Secrets hinterlegen).')

  const { path: selPath, data: SEL } = loadSelectors()
  const reportsPath = process.env.AMPLIFA_REPORTS_PATH || SEL.reports?.path || '/admin/reports'

  const browser = await chromium.launch({ headless: !HEADFUL })
  const context = await browser.newContext({
    locale: 'de-DE',
    timezoneId: 'Europe/Berlin',
    viewport: { width: 1440, height: 900 },
    userAgent:
      'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 ' +
      '(KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36',
  })
  const page = await context.newPage()
  page.setDefaultTimeout(30_000)

  try {
    // 1) Startseite öffnen (führt i. d. R. zum Login-Redirect)
    await page.goto(BASE_URL + '/', { waitUntil: 'domcontentloaded' })

    // 2) Login, falls ein Passwortfeld sichtbar ist
    const pwSel = SEL.login?.passwordInput || 'input[type=password]'
    const emSel = SEL.login?.emailInput || 'input[type=email], input[name=email]'
    const needsLogin = await page.locator(pwSel).first().isVisible().catch(() => false)
    if (needsLogin) {
      await page.locator(emSel).first().fill(EMAIL)
      await page.locator(pwSel).first().fill(PASSWORD)
      const submit = SEL.login?.submitButton || 'button[type=submit]'
      await Promise.all([
        page.waitForLoadState('networkidle').catch(() => {}),
        page.locator(submit).first().click(),
      ])
      await page.waitForLoadState('networkidle').catch(() => {})

      // Erfolgsprüfung: kein Passwortfeld mehr, ggf. expliziter Marker
      const stillLogin = await page.locator(pwSel).first().isVisible().catch(() => false)
      const marker = SEL.login?.loggedInMarkerSelector
      const markerOk = marker ? await page.locator(marker).first().isVisible().catch(() => false) : true
      if (stillLogin || !markerOk) {
        const html = await dump(page, 'login-failed')
        fail('Login fehlgeschlagen – Passwortfeld noch sichtbar oder Login-Marker fehlt. Selektoren kalibrieren.', {
          debug: html,
        })
      }
    }

    // 3) Reports-Ansicht öffnen
    await page.goto(BASE_URL + reportsPath, { waitUntil: 'domcontentloaded' })
    await page.waitForLoadState('networkidle').catch(() => {})
    if (SEL.reports?.waitForSelector) {
      await page.waitForSelector(SEL.reports.waitForSelector, { timeout: 30_000 }).catch(() => {})
    }

    // 4) 7-Tage-Filter setzen, falls konfiguriert
    if (SEL.reports?.rangeControlSelector) {
      await page.locator(SEL.reports.rangeControlSelector).first().click().catch(() => {})
      if (SEL.reports?.rangeOption7dSelector) {
        await page.locator(SEL.reports.rangeOption7dSelector).first().click().catch(() => {})
      }
      await page.waitForLoadState('networkidle').catch(() => {})
    }

    // 5) Tabelle auslesen: pro Zeile Kundenname + Meeting-Zahl
    const rowSel = SEL.table?.rowSelector || 'table tbody tr'
    const nameSel = SEL.table?.nameSelector || 'td:nth-child(1)'
    const countSel = SEL.table?.countSelector || 'td:last-child'

    await page.waitForSelector(rowSel, { timeout: 30_000 }).catch(() => {})
    const rows = await page.locator(rowSel).all()
    const customers = []
    for (const row of rows) {
      const name = (await row.locator(nameSel).first().innerText().catch(() => '')).trim()
      const countRaw = (await row.locator(countSel).first().innerText().catch(() => '')).trim()
      const meetings = toNumber(countRaw)
      if (name && meetings != null) customers.push({ name, meetings })
    }

    if (customers.length === 0) {
      const html = await dump(page, 'no-rows')
      fail('Keine Kundenzeilen extrahiert – Tabellen-Selektoren stimmen nicht. Kalibrieren (siehe SKILL.md).', {
        debug: html,
        selectorsFile: selPath,
        triedSelectors: { rowSel, nameSel, countSel },
      })
    }

    if (DEBUG) await dump(page, 'ok')

    process.stdout.write(
      JSON.stringify({
        ok: true,
        source: BASE_URL + reportsPath,
        rangeDays: RANGE_DAYS,
        customerCount: customers.length,
        customers,
      }) + '\n',
    )
  } catch (err) {
    const html = await dump(page, 'error')
    fail(err?.message || err, { debug: html, stack: err?.stack })
  } finally {
    await browser.close().catch(() => {})
  }
}

run()
